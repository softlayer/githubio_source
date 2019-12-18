---
title: "SoftLayer_Network_Storage_Iscsi_EqualLogic_Version3_Snapshot"
description: "An iscsi snapshot is a point-in-time view of the data on an associated iscsi volume. Iscsi snapshots use a copy-on-write... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi_EqualLogic_Version3_Snapshot"
---

# SoftLayer_Network_Storage_Iscsi_EqualLogic_Version3_Snapshot
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_Iscsi_EqualLogic_Version3_Snapshot' >Datatype</a></li>
    </ul>
</div>

## Description 
An iscsi snapshot is a point-in-time view of the data on an associated iscsi volume. Iscsi snapshots use a copy-on-write technology to minimize the amount of snapshot space used. When a snapshot is initially created it will use no snapshot space. At the time data changes on a volume which existed when a snapshot was created the original data will be saved in the associated volume's snapshot reserve space. 

As a snapshot is created offline it must be set mountable in order to mount it via an iscsi initiator service. 





<!-- Service Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Method Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Service Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
-----
[accountId]: #accountid
#### [accountId]
The internal identifier of the SoftLayer customer account that a Storage account belongs to.   
<span class="type-label">Type: </span>**integer**

-----
[capacityGb]: #capacitygb
#### [capacityGb]
A Storage account's capacity, measured in gigabytes.   
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
The date a network storage volume was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[guestId]: #guestid
#### [guestId]
The unique identification number of the guest associated with a Storage volume.  
<span class="type-label">Type: </span>**integer**

-----
[hardwareId]: #hardwareid
#### [hardwareId]
The server that is associated with a Storage service.   
<span class="type-label">Type: </span>**integer**

-----
[hostId]: #hostid
#### [hostId]
The unique identification number of the host associated with a Storage volume.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
A Storage account's unique identifier.  
<span class="type-label">Type: </span>**integer**

-----
[nasType]: #nastype
#### [nasType]
The StorageLayer account's type (NAS, LOCKBOX, ISCSI, EVAULT).   
<span class="type-label">Type: </span>**string**

-----
[notes]: #notes
#### [notes]
Public notes related to a Storage volume.   
<span class="type-label">Type: </span>**string**

-----
[password]: #password
#### [password]
The password used to access a non-EVault Storage volume. This password is used to register the EVault server agent with the vault backup system.   
<span class="type-label">Type: </span>**string**

-----
[serviceProviderId]: #serviceproviderid
#### [serviceProviderId]
Service Provider ID   
<span class="type-label">Type: </span>**integer**

-----
[storageTypeId]: #storagetypeid
#### [storageTypeId]
A storage object's type.   
<span class="type-label">Type: </span>**string**

-----
[upgradableFlag]: #upgradableflag
#### [upgradableFlag]
This flag indicates whether this storage type is upgradable or not.   
<span class="type-label">Type: </span>**boolean**

-----
[username]: #username
#### [username]
The username used to access a non-EVault Storage volume. This username is used to register the EVault server agent with the vault backup system.   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The account that a Storage services belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[accountPassword]: #accountpassword
#### [accountPassword]
Other usernames and passwords associated with a Storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Password'>SoftLayer_Account_Password </a>**

-----
[activeTransactions]: #activetransactions
#### [activeTransactions]
The currently active transactions on a network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction[] </a>**

-----
[allowedHardware]: #allowedhardware
#### [allowedHardware]
The SoftLayer_Hardware objects which are allowed access to this storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[allowedIpAddresses]: #allowedipaddresses
#### [allowedIpAddresses]
The SoftLayer_Network_Subnet_IpAddress objects which are allowed access to this storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>**

-----
[allowedReplicationHardware]: #allowedreplicationhardware
#### [allowedReplicationHardware]
The SoftLayer_Hardware objects which are allowed access to this storage volume's Replicant.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[allowedReplicationIpAddresses]: #allowedreplicationipaddresses
#### [allowedReplicationIpAddresses]
The SoftLayer_Network_Subnet_IpAddress objects which are allowed access to this storage volume's Replicant.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>**

-----
[allowedReplicationSubnets]: #allowedreplicationsubnets
#### [allowedReplicationSubnets]
The SoftLayer_Network_Subnet objects which are allowed access to this storage volume's Replicant.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**

-----
[allowedReplicationVirtualGuests]: #allowedreplicationvirtualguests
#### [allowedReplicationVirtualGuests]
The SoftLayer_Hardware objects which are allowed access to this storage volume's Replicant.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[allowedSubnets]: #allowedsubnets
#### [allowedSubnets]
The SoftLayer_Network_Subnet objects which are allowed access to this storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**

-----
[allowedVirtualGuests]: #allowedvirtualguests
#### [allowedVirtualGuests]
The SoftLayer_Virtual_Guest objects which are allowed access to this storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[billingItem]: #billingitem
#### [billingItem]
The current billing item for this network storage iscsi volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**

-----
[billingItemCategory]: #billingitemcategory
#### [billingItemCategory]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category </a>**

-----
[bytesUsed]: #bytesused
#### [bytesUsed]
The amount of space used by the volume, in bytes.  
<span class="type-label">Type: </span>**string**

-----
[creationSchedule]: #creationschedule
#### [creationSchedule]
If applicable, the schedule which was executed to create a snapshot.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Schedule'>SoftLayer_Network_Storage_Schedule </a>**

-----
[creationScheduleId]: #creationscheduleid
#### [creationScheduleId]
The schedule id which was executed to create a snapshot.  
<span class="type-label">Type: </span>**string**

-----
[credentials]: #credentials
#### [credentials]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Credential'>SoftLayer_Network_Storage_Credential[] </a>**

-----
[dailySchedule]: #dailyschedule
#### [dailySchedule]
The Daily Schedule which is associated with this network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Schedule'>SoftLayer_Network_Storage_Schedule </a>**

-----
[dependentDuplicate]: #dependentduplicate
#### [dependentDuplicate]
Whether or not a network storage volume is a dependent duplicate.  
<span class="type-label">Type: </span>**string**

-----
[events]: #events
#### [events]
The events which have taken place on a network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Event'>SoftLayer_Network_Storage_Event[] </a>**

-----
[fileNetworkMountAddress]: #filenetworkmountaddress
#### [fileNetworkMountAddress]
Retrieves the NFS Network Mount Address Name for a given File Storage Volume.  
<span class="type-label">Type: </span>**string**

-----
[hardware]: #hardware
#### [hardware]
When applicable, the hardware associated with a Storage service.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**

-----
[hasEncryptionAtRest]: #hasencryptionatrest
#### [hasEncryptionAtRest]
  
<span class="type-label">Type: </span>**boolean**

-----
[hourlySchedule]: #hourlyschedule
#### [hourlySchedule]
The Hourly Schedule which is associated with this network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Schedule'>SoftLayer_Network_Storage_Schedule </a>**

-----
[intervalSchedule]: #intervalschedule
#### [intervalSchedule]
The Interval Schedule which is associated with this network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Schedule'>SoftLayer_Network_Storage_Schedule </a>**

-----
[iops]: #iops
#### [iops]
The maximum number of IOPs guaranteed for this LUN.  
<span class="type-label">Type: </span>**string**

-----
[isDependentDuplicateProvisionCompleted]: #isdependentduplicateprovisioncompleted
#### [isDependentDuplicateProvisionCompleted]
Determines whether dependent volume provision is completed on background.  
<span class="type-label">Type: </span>**boolean**

-----
[isReadyForSnapshot]: #isreadyforsnapshot
#### [isReadyForSnapshot]
Determines whether a volume is ready to order snapshot space, or, if snapshot space is already available, to assign a snapshot schedule, or to take a manual snapshot.  
<span class="type-label">Type: </span>**boolean**

-----
[isReadyToMount]: #isreadytomount
#### [isReadyToMount]
Determines whether a volume is ready to have Hosts authorized to access it. This does not indicate whether another operation may be blocking, please refer to this volume's volumeStatus property for details.  
<span class="type-label">Type: </span>**boolean**

-----
[iscsiLuns]: #iscsiluns
#### [iscsiLuns]
Relationship between a container volume and iSCSI LUNs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[iscsiTargetIpAddresses]: #iscsitargetipaddresses
#### [iscsiTargetIpAddresses]
Returns the target IP addresses of an iSCSI volume.  
<span class="type-label">Type: </span>**array of strings**

-----
[lunId]: #lunid
#### [lunId]
The ID of the LUN volume.  
<span class="type-label">Type: </span>**string**

-----
[manualSnapshots]: #manualsnapshots
#### [manualSnapshots]
The snapshots associated with this SoftLayer_Network_Storage volume. Does not support pagination by result limit and offset.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[metricTrackingObject]: #metrictrackingobject
#### [metricTrackingObject]
A network storage volume's metric tracking object. This object records all periodic polled data available to this volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object'>SoftLayer_Metric_Tracking_Object </a>**

-----
[mountableFlag]: #mountableflag
#### [mountableFlag]
Whether or not a network storage volume may be mounted.  
<span class="type-label">Type: </span>**string**

-----
[moveAndSplitStatus]: #moveandsplitstatus
#### [moveAndSplitStatus]
The current status of split or move operation as a part of volume duplication.  
<span class="type-label">Type: </span>**string**

-----
[notificationSubscribers]: #notificationsubscribers
#### [notificationSubscribers]
The subscribers that will be notified for usage amount warnings and overages.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber'>SoftLayer_Notification_User_Subscriber[] </a>**

-----
[originalSnapshotName]: #originalsnapshotname
#### [originalSnapshotName]
The name of the snapshot that this volume was duplicated from.  
<span class="type-label">Type: </span>**string**

-----
[originalVolumeName]: #originalvolumename
#### [originalVolumeName]
The name of the volume that this volume was duplicated from.  
<span class="type-label">Type: </span>**string**

-----
[originalVolumeSize]: #originalvolumesize
#### [originalVolumeSize]
The size (in GB) of the volume or LUN before any size expansion, or of the volume (before any possible size expansion) from which the duplicate volume or LUN was created.  
<span class="type-label">Type: </span>**string**

-----
[osType]: #ostype
#### [osType]
A volume's configured SoftLayer_Network_Storage_Iscsi_OS_Type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Iscsi_OS_Type'>SoftLayer_Network_Storage_Iscsi_OS_Type </a>**

-----
[osTypeId]: #ostypeid
#### [osTypeId]
A volume's configured SoftLayer_Network_Storage_Iscsi_OS_Type ID.  
<span class="type-label">Type: </span>**string**

-----
[parentPartnerships]: #parentpartnerships
#### [parentPartnerships]
The volumes or snapshots partnered with a network storage volume in a parental role.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Partnership'>SoftLayer_Network_Storage_Partnership[] </a>**

-----
[parentVolume]: #parentvolume
#### [parentVolume]
The volume for which a snapshot is associated with.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage </a>**

-----
[partnerships]: #partnerships
#### [partnerships]
The volumes or snapshots partnered with a network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Partnership'>SoftLayer_Network_Storage_Partnership[] </a>**

-----
[permissionsGroups]: #permissionsgroups
#### [permissionsGroups]
All permissions group(s) this volume is in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Group'>SoftLayer_Network_Storage_Group[] </a>**

-----
[properties]: #properties
#### [properties]
The properties used to provide additional details about a network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Property'>SoftLayer_Network_Storage_Property[] </a>**

-----
[provisionedIops]: #provisionediops
#### [provisionedIops]
The number of IOPs provisioned for this volume.  
<span class="type-label">Type: </span>**string**

-----
[replicatingLuns]: #replicatingluns
#### [replicatingLuns]
The iSCSI LUN volumes being replicated by this network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[replicatingVolume]: #replicatingvolume
#### [replicatingVolume]
The network storage volume being replicated by a volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage </a>**

-----
[replicationEvents]: #replicationevents
#### [replicationEvents]
The volume replication events.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Event'>SoftLayer_Network_Storage_Event[] </a>**

-----
[replicationPartners]: #replicationpartners
#### [replicationPartners]
The network storage volumes configured to be replicants of a volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[replicationSchedule]: #replicationschedule
#### [replicationSchedule]
The Replication Schedule associated with a network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Schedule'>SoftLayer_Network_Storage_Schedule </a>**

-----
[replicationStatus]: #replicationstatus
#### [replicationStatus]
The current replication status of a network storage volume. Indicates Failover or Failback status.  
<span class="type-label">Type: </span>**string**

-----
[schedules]: #schedules
#### [schedules]
The schedules which are associated with a network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Schedule'>SoftLayer_Network_Storage_Schedule[] </a>**

-----
[serviceResource]: #serviceresource
#### [serviceResource]
The network resource a Storage service is connected to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Service_Resource'>SoftLayer_Network_Service_Resource </a>**

-----
[serviceResourceBackendIpAddress]: #serviceresourcebackendipaddress
#### [serviceResourceBackendIpAddress]
The IP address of a Storage resource.  
<span class="type-label">Type: </span>**string**

-----
[serviceResourceName]: #serviceresourcename
#### [serviceResourceName]
The name of a Storage's network resource.  
<span class="type-label">Type: </span>**string**

-----
[snapshotCapacityGb]: #snapshotcapacitygb
#### [snapshotCapacityGb]
The maximum capacity available to use for volume snapshots.  
<span class="type-label">Type: </span>**decimal**

-----
[snapshotCreationTimestamp]: #snapshotcreationtimestamp
#### [snapshotCreationTimestamp]
The creation timestamp of the snapshot on the storage platform.  
<span class="type-label">Type: </span>**string**

-----
[snapshotDeletionThresholdPercentage]: #snapshotdeletionthresholdpercentage
#### [snapshotDeletionThresholdPercentage]
The percentage of used snapshot space after which to delete automated snapshots.  
<span class="type-label">Type: </span>**string**

-----
[snapshotSizeBytes]: #snapshotsizebytes
#### [snapshotSizeBytes]
The snapshot size in bytes.  
<span class="type-label">Type: </span>**string**

-----
[snapshotSpaceAvailable]: #snapshotspaceavailable
#### [snapshotSpaceAvailable]
An iscsi volume's available snapshot reservation space.  
<span class="type-label">Type: </span>**string**

-----
[snapshots]: #snapshots
#### [snapshots]
The snapshots associated with this SoftLayer_Network_Storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[staasVersion]: #staasversion
#### [staasVersion]
  
<span class="type-label">Type: </span>**string**

-----
[storageGroups]: #storagegroups
#### [storageGroups]
The network storage groups this volume is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Group'>SoftLayer_Network_Storage_Group[] </a>**

-----
[storageTierLevel]: #storagetierlevel
#### [storageTierLevel]
  
<span class="type-label">Type: </span>**string**

-----
[storageType]: #storagetype
#### [storageType]
A description of the Storage object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Type'>SoftLayer_Network_Storage_Type </a>**

-----
[totalBytesUsed]: #totalbytesused
#### [totalBytesUsed]
The amount of space used by the volume.  
<span class="type-label">Type: </span>**string**

-----
[totalScheduleSnapshotRetentionCount]: #totalschedulesnapshotretentioncount
#### [totalScheduleSnapshotRetentionCount]
The total snapshot retention count of all schedules on this network storage volume.  
<span class="type-label">Type: </span>**unsigned integer**

-----
[usageNotification]: #usagenotification
#### [usageNotification]
The usage notification for SL Storage services.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification'>SoftLayer_Notification </a>**

-----
[vendorName]: #vendorname
#### [vendorName]
The type of network storage service.  
<span class="type-label">Type: </span>**string**

-----
[virtualGuest]: #virtualguest
#### [virtualGuest]
When applicable, the virtual guest associated with a Storage service.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**

-----
[volumeHistory]: #volumehistory
#### [volumeHistory]
The username and password history for a Storage service.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_History'>SoftLayer_Network_Storage_History[] </a>**

-----
[volumeName]: #volumename
#### [volumeName]
The volume name for an iscsi snapshot.  
<span class="type-label">Type: </span>**string**

-----
[volumeStatus]: #volumestatus
#### [volumeStatus]
The current status of a network storage volume.  
<span class="type-label">Type: </span>**string**

-----
[webccAccount]: #webccaccount
#### [webccAccount]
The account username and password for the EVault webCC interface.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Password'>SoftLayer_Account_Password </a>**

-----
[weeklySchedule]: #weeklyschedule
#### [weeklySchedule]
The Weekly Schedule which is associated with this network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Schedule'>SoftLayer_Network_Storage_Schedule </a>**


## Count

-----
[activeTransactionCount]: #activetransactioncount
#### [activeTransactionCount]
A count of the currently active transactions on a network storage volume.   
<span class="type-label">Type: </span>**unsigned long**


-----
[allowedHardwareCount]: #allowedhardwarecount
#### [allowedHardwareCount]
A count of the SoftLayer_Hardware objects which are allowed access to this storage volume.   
<span class="type-label">Type: </span>**unsigned long**


-----
[allowedIpAddressCount]: #allowedipaddresscount
#### [allowedIpAddressCount]
A count of the SoftLayer_Network_Subnet_IpAddress objects which are allowed access to this storage volume.   
<span class="type-label">Type: </span>**unsigned long**


-----
[allowedReplicationHardwareCount]: #allowedreplicationhardwarecount
#### [allowedReplicationHardwareCount]
A count of the SoftLayer_Hardware objects which are allowed access to this storage volume's Replicant.   
<span class="type-label">Type: </span>**unsigned long**


-----
[allowedReplicationIpAddressCount]: #allowedreplicationipaddresscount
#### [allowedReplicationIpAddressCount]
A count of the SoftLayer_Network_Subnet_IpAddress objects which are allowed access to this storage volume's Replicant.   
<span class="type-label">Type: </span>**unsigned long**


-----
[allowedReplicationSubnetCount]: #allowedreplicationsubnetcount
#### [allowedReplicationSubnetCount]
A count of the SoftLayer_Network_Subnet objects which are allowed access to this storage volume's Replicant.   
<span class="type-label">Type: </span>**unsigned long**


-----
[allowedReplicationVirtualGuestCount]: #allowedreplicationvirtualguestcount
#### [allowedReplicationVirtualGuestCount]
A count of the SoftLayer_Hardware objects which are allowed access to this storage volume's Replicant.   
<span class="type-label">Type: </span>**unsigned long**


-----
[allowedSubnetCount]: #allowedsubnetcount
#### [allowedSubnetCount]
A count of the SoftLayer_Network_Subnet objects which are allowed access to this storage volume.   
<span class="type-label">Type: </span>**unsigned long**


-----
[allowedVirtualGuestCount]: #allowedvirtualguestcount
#### [allowedVirtualGuestCount]
A count of the SoftLayer_Virtual_Guest objects which are allowed access to this storage volume.   
<span class="type-label">Type: </span>**unsigned long**


-----
[credentialCount]: #credentialcount
#### [credentialCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[eventCount]: #eventcount
#### [eventCount]
A count of the events which have taken place on a network storage volume.   
<span class="type-label">Type: </span>**unsigned long**


-----
[iscsiLunCount]: #iscsiluncount
#### [iscsiLunCount]
A count of relationship between a container volume and iSCSI LUNs.   
<span class="type-label">Type: </span>**unsigned long**


-----
[iscsiTargetIpAddressCount]: #iscsitargetipaddresscount
#### [iscsiTargetIpAddressCount]
A count of returns the target IP addresses of an iSCSI volume.   
<span class="type-label">Type: </span>**unsigned long**


-----
[manualSnapshotCount]: #manualsnapshotcount
#### [manualSnapshotCount]
A count of the snapshots associated with this SoftLayer_Network_Storage volume. Does not support pagination by result limit and offset.   
<span class="type-label">Type: </span>**unsigned long**


-----
[notificationSubscriberCount]: #notificationsubscribercount
#### [notificationSubscriberCount]
A count of the subscribers that will be notified for usage amount warnings and overages.   
<span class="type-label">Type: </span>**unsigned long**


-----
[parentPartnershipCount]: #parentpartnershipcount
#### [parentPartnershipCount]
A count of the volumes or snapshots partnered with a network storage volume in a parental role.   
<span class="type-label">Type: </span>**unsigned long**


-----
[partnershipCount]: #partnershipcount
#### [partnershipCount]
A count of the volumes or snapshots partnered with a network storage volume.   
<span class="type-label">Type: </span>**unsigned long**


-----
[permissionsGroupCount]: #permissionsgroupcount
#### [permissionsGroupCount]
A count of all permissions group(s) this volume is in.   
<span class="type-label">Type: </span>**unsigned long**


-----
[propertyCount]: #propertycount
#### [propertyCount]
A count of the properties used to provide additional details about a network storage volume.   
<span class="type-label">Type: </span>**unsigned long**


-----
[replicatingLunCount]: #replicatingluncount
#### [replicatingLunCount]
A count of the iSCSI LUN volumes being replicated by this network storage volume.   
<span class="type-label">Type: </span>**unsigned long**


-----
[replicationEventCount]: #replicationeventcount
#### [replicationEventCount]
A count of the volume replication events.   
<span class="type-label">Type: </span>**unsigned long**


-----
[replicationPartnerCount]: #replicationpartnercount
#### [replicationPartnerCount]
A count of the network storage volumes configured to be replicants of a volume.   
<span class="type-label">Type: </span>**unsigned long**


-----
[scheduleCount]: #schedulecount
#### [scheduleCount]
A count of the schedules which are associated with a network storage volume.   
<span class="type-label">Type: </span>**unsigned long**


-----
[snapshotCount]: #snapshotcount
#### [snapshotCount]
A count of the snapshots associated with this SoftLayer_Network_Storage volume.   
<span class="type-label">Type: </span>**unsigned long**


-----
[storageGroupCount]: #storagegroupcount
#### [storageGroupCount]
A count of the network storage groups this volume is attached to.   
<span class="type-label">Type: </span>**unsigned long**


-----
[volumeHistoryCount]: #volumehistorycount
#### [volumeHistoryCount]
A count of the username and password history for a Storage service.   
<span class="type-label">Type: </span>**unsigned long**

</div>


