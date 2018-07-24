---
title: "Automating Block Storage"
description: "An example of how to order a VSI and then automatically add a storage volume with a post install script."
date: "2018-07-23"
tags:
    - "article"
    - "sldn"
    - "python"
---


## The Process

1. Order a VSI with a postInstall script
2. Order a storage volume
3. Update the metadata of the VSI to include the needed information to mount the storage volume
4. postInstall script gets metadata from the metadata service, and mounts the volume


## Ordering Code

This script will order a VSI, based on a configuration in the file, then order some storage, authorize storage to the new VSI, and set the VSI's metadata with the needed information for it to be mounted.


```python
"""
Create a new Virtual Guest and block storage.
allowAccessToNetworkStorageList, setUserMetadata

createObject() enables the creation of computing instances on an account.
This method is a simplified alternative to interacting with the ordering
system directly.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject
https://softlayer.github.io/reference/services/SoftLayer_Product_Order/placeOrder/
https://softlayer.github.io/reference/services/SoftLayer_Billing_Order/getObject/
https://softlayer.github.io/reference/services/SoftLayer_Account/getNetworkStorage/
https://softlayer.github.io/reference/services/SoftLayer_Virtual_Guest/setUserMetadata/
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/generateOrderTemplate
https://softlayer.github.io/reference/services/SoftLayer_Virtual_Guest/allowAccessToNetworkStorageList/

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import time
import SoftLayer


# For nice debug output:
from pprint import pprint as pp



# Initial setup of some variables

client = SoftLayer.create_client_from_env()
storage_manager =  SoftLayer.BlockStorageManager(client)
guest_manager = SoftLayer.VSManager(client)

vmId = None
username = None
password = None
targetAddress = None
blockStorageId = None
blockStorageOrderId = None
allowAccessToNetworkStorage = None


# Describes the VM we want to order
templateVirtualGuest = {
    "hostname": "tester",
    "domain": "ibm.com",
    "datacenter": "dal13",
    "flavor": "BL2_2X4X100",
    "hourlyBillingFlag": True,
    "os_code": "CENTOS_7_64",
    "nic_speed": 1000,
    "postInstallScriptUri": "https://pastebin.com/whatever",
    "ssh_keys": [87634],
    "public_security_groups": [128321, 128323]
}

# === ORDERS THE VM ===
virtualGuestResponse = guest_manager.create_instance(**templateVirtualGuest)
vmId = virtualGuestResponse['id']
pp("virtualGuestId " + str(vmId))


# === ORDERS THE STORAGE ===
blockStorageOrder = storage_manager.order_block_volume(
    storage_type="performance",
    location="dal13",
    size=100,
    os_type="LINUX",
    iops=1000,
    snapshot_size=None,
    service_offering='storage_as_a_service',
    hourly_billing_flag=True
)

blockStorageOrderId = blockStorageOrder['orderId']
pp("blockStorageOrderId " + str(blockStorageOrderId))

status = None
while status != "APPROVED":
    print("Checking storage order status...")
    orderStatus = client['Billing_Order'].getObject(id=blockStorageOrderId)
    status = orderStatus['status']
    if status == "APPROVED":
        break
    else:
        print("Order pending approval")
        time.sleep(60)

# Used to lookup the storage id based on its order
objectFilter = {
    "networkStorage": {
        "billingItem": {
            "orderItem": {
                "order": {
                    "id": {
                        "operation": blockStorageOrderId
                        }
                    }
                }
            }
        }
    }

objectMask = 'mask[billingItem[orderItem[order[id]]]]'

print("Getting block storage info")
blockStorageArray = client['Account'].getNetworkStorage(filter=objectFilter, mask=objectMask)

for blockStorage in blockStorageArray:
    blockStorageId = blockStorage['id']
    print("blockStorageId " + str(blockStorageId))

# Can't autorize a volume while there is an active transaction
activeTransaction = client['SoftLayer_Network_Storage'].getActiveTransactions(id=blockStorageId)
while (len(activeTransaction) > 0):
    activeTransaction = client['SoftLayer_Network_Storage'].getActiveTransactions(id=blockStorageId)
    print('There is a block storage transaction running')
    time.sleep(10)

blockStorageObject = [ {  "id": blockStorageId } ]
print("Granting vm {} access to {}".format(vmId, blockStorageId))
try:
    allowAccessToNetworkStorage = client['Virtual_Guest'].allowAccessToNetworkStorageList(blockStorageObject, id=vmId)
except SoftLayer.exceptions.SoftLayerAPIError as e:
    if e.faultCode == "SoftLayer_Exception_Network_Storage_Group_MassAccessControlModification":
        print("This host is already allowed access")



# Find out the username/password/ip for our iscsi target
objectMask = """mask[id, iscsiTargetIpAddresses, allowedVirtualGuests[fullyQualifiedDomainName, 
allowedHost[id,name,resourceTableId,resourceTableName, credential[id,username,password],sourceSubnet]]]"""
blockStorageCredentials = client['SoftLayer_Network_Storage'].getObject(mask=objectMask, id=blockStorageId)

# We assume this volume only has 1 host authorized to mount it.
pp(blockStorageCredentials)
allowedHost = blockStorageCredentials['allowedVirtualGuests'][0]
credentials = allowedHost['allowedHost']['credential']
targetAddress = blockStorageCredentials['iscsiTargetIpAddresses']
username = credentials['username']
password = credentials['password']
iqn = allowedHost['allowedHost']['name']

# Set the meta data for the vm
meta_string = "{storageId}, {iqn}, {target}, {user}, {password}".format(
                storageId=blockStorageId, target=", ".join(targetAddress), user=username, password=password, iqn=iqn)
metadata = [meta_string]

print("Setting MetaData:\n%s\n" % metadata)
metadataSet = client['Virtual_Guest'].setUserMetadata(metadata, id=vmId)



mask = "mask[userData]"
virtualGuestData = client['Virtual_Guest'].getObject(mask=mask, id=vmId)
pp(virtualGuestData)

print("FINISHED")

```

## Post install script

Most of the configuration for this script comes from https://console.bluemix.net/docs/infrastructure/BlockStorage/accessing_block_storage_linux.html#connecting-to-mpio-iscsi-luns-on-linux and this specific script is meant to run on Centos7. If you are not using Centos7, you will need to make some minor adjustments to the configuration files.

```bash
#!/bin/bash 
# *************************  Connecting to MPIO ISCSI lun on Linux OS *************************
# The following script uses steps for CentOS distribution only, to change configuration please review the following url:
# https://console.bluemix.net/docs/infrastructure/BlockStorage/accessing_block_storage_linux.html#connecting-to-mpio-iscsi-luns-on-linux

# Get the metadata
IFS=',' read -ra METAAA <<< `curl https://api.service.softlayer.com/rest/v3.1/SoftLayer_Resource_Metadata/getUserMetadata`
USERNAME=${METAAA[4]}
IP_1=${METAAA[3]}
IP_2=${METAAA[2]}
# This removes the trailing \" that comes from the curl command
PASSWORD="${METAAA[5]%\"}"
INITIATOR=${METAAA[1]}

#1 Install the iSCSI and multipath utilities to your host.
yum -y install iscsi-initiator-utils device-mapper-multipath

#2 Create/edit /etc/multipath.conf with the minimum configuration that is provided in the following commands. 
MINIMUMCONFIGURATION='
defaults {
user_friendly_names no
max_fds max
flush_on_last_del yes
queue_without_daemon no
dev_loss_tmo infinity
fast_io_fail_tmo 5
}
# All data under blacklist must be specific to your system.
blacklist {
wwid "SAdaptec*"
devnode "^hd[a-z]"
devnode "^(ram|raw|loop|fd|md|dm-|sr|scd|st)[0-9]*"
devnode "^cciss.*"  
}
devices {
device {
vendor "NETAPP"
product "LUN"
path_grouping_policy group_by_prio
features "3 queue_if_no_path pg_init_retries 50"
prio "alua"
path_checker tur
failback immediate
path_selector "round-robin 0"
hardware_handler "1 alua"
rr_weight uniform
rr_min_io 128
}
}
'
echo "$MINIMUMCONFIGURATION" > /etc/multipath.conf

#3 Load the multipath module, start multipath services, and set it start on boot.
# CentOS 7 commands, change the following according the SO type.
modprobe dm-multipath
systemctl start multipathd
systemctl enable multipathd

#4 Verify that multipath is working.
multipath -ll

#5 Update /etc/iscsi/initiatorname.iscsi file with the IQN from the IBM Cloud infrastructure customer portal. 
#  Enter the value as lowercase.
echo "InitiatorName=$INITIATOR" > /etc/iscsi/initiatorname.iscsi

#6 Edit the CHAP settings in /etc/iscsi/iscsid.conf by using the user name and password from the IBM Cloud infrastructure customer portal. 
#  Use uppercase for CHAP names.
ISCSIDCONF="
iscsid.startup = /bin/systemctl start iscsid.socket iscsiuio.socket
node.startup = automatic
node.leading_login = No
node.session.timeo.replacement_timeout = 120
node.conn[0].timeo.login_timeout = 15
node.conn[0].timeo.logout_timeout = 15
node.conn[0].timeo.noop_out_interval = 5
node.conn[0].timeo.noop_out_timeout = 5
node.session.err_timeo.abort_timeout = 15
node.session.err_timeo.lu_reset_timeout = 30
node.session.err_timeo.tgt_reset_timeout = 30
node.session.initial_login_retry_max = 8
node.session.cmds_max = 128
node.session.queue_depth = 32
node.session.xmit_thread_priority = -20
node.session.iscsi.InitialR2T = No
node.session.iscsi.ImmediateData = Yes
node.session.iscsi.FirstBurstLength = 262144
node.session.iscsi.MaxBurstLength = 16776192
node.conn[0].iscsi.MaxRecvDataSegmentLength = 262144
node.conn[0].iscsi.MaxXmitDataSegmentLength = 0
discovery.sendtargets.iscsi.MaxRecvDataSegmentLength = 32768
node.conn[0].iscsi.HeaderDigest = None
node.session.nr_sessions = 1
node.session.iscsi.FastAbort = Yes
node.session.scan = auto
node.session.auth.authmethod = CHAP
node.session.auth.username = ${USERNAME}
node.session.auth.password =  ${PASSWORD}
discovery.sendtargets.auth.authmethod = CHAP
discovery.sendtargets.auth.username =  ${USERNAME}
discovery.sendtargets.auth.password =  ${PASSWORD}"
echo "$ISCSIDCONF" > /etc/iscsi/iscsid.conf
 
#7 Set iSCSI to start at boot and start it now.
systemctl enable iscsi
systemctl enable iscsid
systemctl start iscsi
systemctl start iscsid

#8 Discover the device by using the Target IP address that was obtained from the IBM Cloud infrastructure customer portal.

#A. Run the discovery against the iSCSI array.

iscsiadm -m discovery -t sendtargets -p $IP_1

#B. Set the host to automatically log in to the iSCSI array.
iscsiadm -m node -L automatic

#9 Verify that the host is logged in to the iSCSI array and maintained its sessions.
iscsiadm -m session
multipath -l

#10 Verify that the device is connected. 
#   By default the device attaches to /dev/mapper/mpathX where X is the generated ID of the connected device.
fdisk -l | grep /dev/mapper

```
