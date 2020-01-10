---
title: "SoftLayer_Network_Storage_Iscsi_EqualLogic_Version3_Replicant"
description: "An iscsi replicant receives incoming data from an associated iscsi volume.  While the replicant is not in failover mode... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi_EqualLogic_Version3_Replicant"
---

# SoftLayer_Network_Storage_Iscsi_EqualLogic_Version3_Replicant
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_Iscsi_EqualLogic_Version3_Replicant' >Datatype</a></li>
    </ul>
</div>

## Description 
An iscsi replicant receives incoming data from an associated iscsi volume.  While the replicant is not in failover mode it will not be mountable.  Upon failover the replicant can be mounted and used as a normal volume.  It is suggested to only do this as part of a disaster recovery plan. 





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[accountId]: #accountid
#### [accountId]
The internal identifier of the SoftLayer customer account that a Storage account belongs to.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[capacityGb]: #capacitygb
#### [capacityGb]
A Storage account's capacity, measured in gigabytes.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date a network storage volume was created.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[guestId]: #guestid
#### [guestId]
The unique identification number of the guest associated with a Storage volume.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[hardwareId]: #hardwareid
#### [hardwareId]
The server that is associated with a Storage service.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[hostId]: #hostid
#### [hostId]
The unique identification number of the host associated with a Storage volume.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A Storage account's unique identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[nasType]: #nastype
#### [nasType]
The StorageLayer account's type (NAS, LOCKBOX, ISCSI, EVAULT).   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[notes]: #notes
#### [notes]
Public notes related to a Storage volume.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[password]: #password
#### [password]
The password used to access a non-EVault Storage volume. This password is used to register the EVault server agent with the vault backup system.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[serviceProviderId]: #serviceproviderid
#### [serviceProviderId]
Service Provider ID   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[storageTypeId]: #storagetypeid
#### [storageTypeId]
A storage object's type.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[upgradableFlag]: #upgradableflag
#### [upgradableFlag]
This flag indicates whether this storage type is upgradable or not.   
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[username]: #username
#### [username]
The username used to access a non-EVault Storage volume. This username is used to register the EVault server agent with the vault backup system.   
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account that a Storage services belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[accountPassword]: #accountpassword
#### [accountPassword]
Other usernames and passwords associated with a Storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Password'>SoftLayer_Account_Password </a>**


</div>
<div class="prop-row">

-----
[activeTransactions]: #activetransactions
#### [activeTransactions]
The currently active transactions on a network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction[] </a>**


</div>
<div class="prop-row">

-----
[allowedHardware]: #allowedhardware
#### [allowedHardware]
The SoftLayer_Hardware objects which are allowed access to this storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[allowedIpAddresses]: #allowedipaddresses
#### [allowedIpAddresses]
The SoftLayer_Network_Subnet_IpAddress objects which are allowed access to this storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>**


</div>
<div class="prop-row">

-----
[allowedReplicationHardware]: #allowedreplicationhardware
#### [allowedReplicationHardware]
The SoftLayer_Hardware objects which are allowed access to this storage volume's Replicant.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[allowedReplicationIpAddresses]: #allowedreplicationipaddresses
#### [allowedReplicationIpAddresses]
The SoftLayer_Network_Subnet_IpAddress objects which are allowed access to this storage volume's Replicant.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>**


</div>
<div class="prop-row">

-----
[allowedReplicationSubnets]: #allowedreplicationsubnets
#### [allowedReplicationSubnets]
The SoftLayer_Network_Subnet objects which are allowed access to this storage volume's Replicant.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**


</div>
<div class="prop-row">

-----
[allowedReplicationVirtualGuests]: #allowedreplicationvirtualguests
#### [allowedReplicationVirtualGuests]
The SoftLayer_Hardware objects which are allowed access to this storage volume's Replicant.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[allowedSubnets]: #allowedsubnets
#### [allowedSubnets]
The SoftLayer_Network_Subnet objects which are allowed access to this storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**


</div>
<div class="prop-row">

-----
[allowedVirtualGuests]: #allowedvirtualguests
#### [allowedVirtualGuests]
The SoftLayer_Virtual_Guest objects which are allowed access to this storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
The current billing item for this network storage iscsi replicant volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**


</div>
<div class="prop-row">

-----
[billingItemCategory]: #billingitemcategory
#### [billingItemCategory]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category </a>**


</div>
<div class="prop-row">

-----
[bytesUsed]: #bytesused
#### [bytesUsed]
The amount of space used by the volume, in bytes.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[creationScheduleId]: #creationscheduleid
#### [creationScheduleId]
The schedule id which was executed to create a snapshot.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[credentials]: #credentials
#### [credentials]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Credential'>SoftLayer_Network_Storage_Credential[] </a>**


</div>
<div class="prop-row">

-----
[dailySchedule]: #dailyschedule
#### [dailySchedule]
The Daily Schedule which is associated with this network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Schedule'>SoftLayer_Network_Storage_Schedule </a>**


</div>
<div class="prop-row">

-----
[dependentDuplicate]: #dependentduplicate
#### [dependentDuplicate]
Whether or not a network storage volume is a dependent duplicate.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[events]: #events
#### [events]
The events which have taken place on a network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Event'>SoftLayer_Network_Storage_Event[] </a>**


</div>
<div class="prop-row">

-----
[failbackInProgressFlag]: #failbackinprogressflag
#### [failbackInProgressFlag]
When a replicant is in the process of synchronizing with the parent volume this flag will be true.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[fileNetworkMountAddress]: #filenetworkmountaddress
#### [fileNetworkMountAddress]
Retrieves the NFS Network Mount Address Name for a given File Storage Volume.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
When applicable, the hardware associated with a Storage service.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**


</div>
<div class="prop-row">

-----
[hasEncryptionAtRest]: #hasencryptionatrest
#### [hasEncryptionAtRest]
  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[hourlySchedule]: #hourlyschedule
#### [hourlySchedule]
The Hourly Schedule which is associated with this network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Schedule'>SoftLayer_Network_Storage_Schedule </a>**


</div>
<div class="prop-row">

-----
[intervalSchedule]: #intervalschedule
#### [intervalSchedule]
The Interval Schedule which is associated with this network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Schedule'>SoftLayer_Network_Storage_Schedule </a>**


</div>
<div class="prop-row">

-----
[iops]: #iops
#### [iops]
The maximum number of IOPs guaranteed for this LUN.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[isDependentDuplicateProvisionCompleted]: #isdependentduplicateprovisioncompleted
#### [isDependentDuplicateProvisionCompleted]
Determines whether dependent volume provision is completed on background.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[isReadyForSnapshot]: #isreadyforsnapshot
#### [isReadyForSnapshot]
Determines whether a volume is ready to order snapshot space, or, if snapshot space is already available, to assign a snapshot schedule, or to take a manual snapshot.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[isReadyToMount]: #isreadytomount
#### [isReadyToMount]
Determines whether a volume is ready to have Hosts authorized to access it. This does not indicate whether another operation may be blocking, please refer to this volume's volumeStatus property for details.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[iscsiLuns]: #iscsiluns
#### [iscsiLuns]
Relationship between a container volume and iSCSI LUNs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[iscsiTargetIpAddresses]: #iscsitargetipaddresses
#### [iscsiTargetIpAddresses]
Returns the target IP addresses of an iSCSI volume.  
<span class="type-label">Type: </span>**array of strings**


</div>
<div class="prop-row">

-----
[lunId]: #lunid
#### [lunId]
The ID of the LUN volume.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[manualSnapshots]: #manualsnapshots
#### [manualSnapshots]
The snapshots associated with this SoftLayer_Network_Storage volume. Does not support pagination by result limit and offset.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[metricTrackingObject]: #metrictrackingobject
#### [metricTrackingObject]
A network storage volume's metric tracking object. This object records all periodic polled data available to this volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object'>SoftLayer_Metric_Tracking_Object </a>**


</div>
<div class="prop-row">

-----
[mountableFlag]: #mountableflag
#### [mountableFlag]
Whether or not a network storage volume may be mounted.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[moveAndSplitStatus]: #moveandsplitstatus
#### [moveAndSplitStatus]
The current status of split or move operation as a part of volume duplication.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[notificationSubscribers]: #notificationsubscribers
#### [notificationSubscribers]
The subscribers that will be notified for usage amount warnings and overages.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber'>SoftLayer_Notification_User_Subscriber[] </a>**


</div>
<div class="prop-row">

-----
[originalSnapshotName]: #originalsnapshotname
#### [originalSnapshotName]
The name of the snapshot that this volume was duplicated from.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[originalVolumeName]: #originalvolumename
#### [originalVolumeName]
The name of the volume that this volume was duplicated from.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[originalVolumeSize]: #originalvolumesize
#### [originalVolumeSize]
The size (in GB) of the volume or LUN before any size expansion, or of the volume (before any possible size expansion) from which the duplicate volume or LUN was created.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[osType]: #ostype
#### [osType]
A volume's configured SoftLayer_Network_Storage_Iscsi_OS_Type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Iscsi_OS_Type'>SoftLayer_Network_Storage_Iscsi_OS_Type </a>**


</div>
<div class="prop-row">

-----
[osTypeId]: #ostypeid
#### [osTypeId]
A volume's configured SoftLayer_Network_Storage_Iscsi_OS_Type ID.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[parentPartnerships]: #parentpartnerships
#### [parentPartnerships]
The volumes or snapshots partnered with a network storage volume in a parental role.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Partnership'>SoftLayer_Network_Storage_Partnership[] </a>**


</div>
<div class="prop-row">

-----
[parentVolume]: #parentvolume
#### [parentVolume]
The volume for which a replicant is receiving incoming data for.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage </a>**


</div>
<div class="prop-row">

-----
[partnerships]: #partnerships
#### [partnerships]
The volumes or snapshots partnered with a network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Partnership'>SoftLayer_Network_Storage_Partnership[] </a>**


</div>
<div class="prop-row">

-----
[permissionsGroups]: #permissionsgroups
#### [permissionsGroups]
All permissions group(s) this volume is in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Group'>SoftLayer_Network_Storage_Group[] </a>**


</div>
<div class="prop-row">

-----
[properties]: #properties
#### [properties]
The properties used to provide additional details about a network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Property'>SoftLayer_Network_Storage_Property[] </a>**


</div>
<div class="prop-row">

-----
[provisionedIops]: #provisionediops
#### [provisionedIops]
The number of IOPs provisioned for this volume.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[replicatingLuns]: #replicatingluns
#### [replicatingLuns]
The iSCSI LUN volumes being replicated by this network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[replicatingVolume]: #replicatingvolume
#### [replicatingVolume]
The network storage volume being replicated by a volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage </a>**


</div>
<div class="prop-row">

-----
[replicationEvents]: #replicationevents
#### [replicationEvents]
The volume replication events.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Event'>SoftLayer_Network_Storage_Event[] </a>**


</div>
<div class="prop-row">

-----
[replicationPartners]: #replicationpartners
#### [replicationPartners]
The network storage volumes configured to be replicants of a volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[replicationSchedule]: #replicationschedule
#### [replicationSchedule]
The Replication Schedule associated with a network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Schedule'>SoftLayer_Network_Storage_Schedule </a>**


</div>
<div class="prop-row">

-----
[replicationStatus]: #replicationstatus
#### [replicationStatus]
The current replication status of a network storage volume. Indicates Failover or Failback status.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[schedules]: #schedules
#### [schedules]
The schedules which are associated with a network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Schedule'>SoftLayer_Network_Storage_Schedule[] </a>**


</div>
<div class="prop-row">

-----
[serviceResource]: #serviceresource
#### [serviceResource]
The network resource a Storage service is connected to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Service_Resource'>SoftLayer_Network_Service_Resource </a>**


</div>
<div class="prop-row">

-----
[serviceResourceBackendIpAddress]: #serviceresourcebackendipaddress
#### [serviceResourceBackendIpAddress]
The IP address of a Storage resource.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[serviceResourceName]: #serviceresourcename
#### [serviceResourceName]
The name of a Storage's network resource.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[snapshotCapacityGb]: #snapshotcapacitygb
#### [snapshotCapacityGb]
The maximum capacity available to use for volume snapshots.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[snapshotCreationTimestamp]: #snapshotcreationtimestamp
#### [snapshotCreationTimestamp]
The creation timestamp of the snapshot on the storage platform.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[snapshotDeletionThresholdPercentage]: #snapshotdeletionthresholdpercentage
#### [snapshotDeletionThresholdPercentage]
The percentage of used snapshot space after which to delete automated snapshots.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[snapshotSizeBytes]: #snapshotsizebytes
#### [snapshotSizeBytes]
The snapshot size in bytes.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[snapshotSpaceAvailable]: #snapshotspaceavailable
#### [snapshotSpaceAvailable]
An iscsi volume's available snapshot reservation space.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[snapshots]: #snapshots
#### [snapshots]
The snapshots associated with this SoftLayer_Network_Storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[staasVersion]: #staasversion
#### [staasVersion]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[storageGroups]: #storagegroups
#### [storageGroups]
The network storage groups this volume is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Group'>SoftLayer_Network_Storage_Group[] </a>**


</div>
<div class="prop-row">

-----
[storageTierLevel]: #storagetierlevel
#### [storageTierLevel]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[storageType]: #storagetype
#### [storageType]
A description of the Storage object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Type'>SoftLayer_Network_Storage_Type </a>**


</div>
<div class="prop-row">

-----
[totalBytesUsed]: #totalbytesused
#### [totalBytesUsed]
The amount of space used by the volume.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[totalScheduleSnapshotRetentionCount]: #totalschedulesnapshotretentioncount
#### [totalScheduleSnapshotRetentionCount]
The total snapshot retention count of all schedules on this network storage volume.  
<span class="type-label">Type: </span>**unsigned integer**


</div>
<div class="prop-row">

-----
[usageNotification]: #usagenotification
#### [usageNotification]
The usage notification for SL Storage services.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification'>SoftLayer_Notification </a>**


</div>
<div class="prop-row">

-----
[vendorName]: #vendorname
#### [vendorName]
The type of network storage service.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[virtualGuest]: #virtualguest
#### [virtualGuest]
When applicable, the virtual guest associated with a Storage service.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**


</div>
<div class="prop-row">

-----
[volumeHistory]: #volumehistory
#### [volumeHistory]
The username and password history for a Storage service.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_History'>SoftLayer_Network_Storage_History[] </a>**


</div>
<div class="prop-row">

-----
[volumeName]: #volumename
#### [volumeName]
The volume name for an iscsi replicant.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[volumeStatus]: #volumestatus
#### [volumeStatus]
The current status of a network storage volume.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[webccAccount]: #webccaccount
#### [webccAccount]
The account username and password for the EVault webCC interface.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Password'>SoftLayer_Account_Password </a>**


</div>
<div class="prop-row">

-----
[weeklySchedule]: #weeklyschedule
#### [weeklySchedule]
The Weekly Schedule which is associated with this network storage volume.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Schedule'>SoftLayer_Network_Storage_Schedule </a>**


</div>

## Count
<div class="prop-row">

-----
[activeTransactionCount]: #activetransactioncount
#### [activeTransactionCount]
A count of the currently active transactions on a network storage volume.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[allowedHardwareCount]: #allowedhardwarecount
#### [allowedHardwareCount]
A count of the SoftLayer_Hardware objects which are allowed access to this storage volume.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[allowedIpAddressCount]: #allowedipaddresscount
#### [allowedIpAddressCount]
A count of the SoftLayer_Network_Subnet_IpAddress objects which are allowed access to this storage volume.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[allowedReplicationHardwareCount]: #allowedreplicationhardwarecount
#### [allowedReplicationHardwareCount]
A count of the SoftLayer_Hardware objects which are allowed access to this storage volume's Replicant.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[allowedReplicationIpAddressCount]: #allowedreplicationipaddresscount
#### [allowedReplicationIpAddressCount]
A count of the SoftLayer_Network_Subnet_IpAddress objects which are allowed access to this storage volume's Replicant.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[allowedReplicationSubnetCount]: #allowedreplicationsubnetcount
#### [allowedReplicationSubnetCount]
A count of the SoftLayer_Network_Subnet objects which are allowed access to this storage volume's Replicant.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[allowedReplicationVirtualGuestCount]: #allowedreplicationvirtualguestcount
#### [allowedReplicationVirtualGuestCount]
A count of the SoftLayer_Hardware objects which are allowed access to this storage volume's Replicant.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[allowedSubnetCount]: #allowedsubnetcount
#### [allowedSubnetCount]
A count of the SoftLayer_Network_Subnet objects which are allowed access to this storage volume.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[allowedVirtualGuestCount]: #allowedvirtualguestcount
#### [allowedVirtualGuestCount]
A count of the SoftLayer_Virtual_Guest objects which are allowed access to this storage volume.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[credentialCount]: #credentialcount
#### [credentialCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[eventCount]: #eventcount
#### [eventCount]
A count of the events which have taken place on a network storage volume.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[iscsiLunCount]: #iscsiluncount
#### [iscsiLunCount]
A count of relationship between a container volume and iSCSI LUNs.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[iscsiTargetIpAddressCount]: #iscsitargetipaddresscount
#### [iscsiTargetIpAddressCount]
A count of returns the target IP addresses of an iSCSI volume.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[manualSnapshotCount]: #manualsnapshotcount
#### [manualSnapshotCount]
A count of the snapshots associated with this SoftLayer_Network_Storage volume. Does not support pagination by result limit and offset.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[notificationSubscriberCount]: #notificationsubscribercount
#### [notificationSubscriberCount]
A count of the subscribers that will be notified for usage amount warnings and overages.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[parentPartnershipCount]: #parentpartnershipcount
#### [parentPartnershipCount]
A count of the volumes or snapshots partnered with a network storage volume in a parental role.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[partnershipCount]: #partnershipcount
#### [partnershipCount]
A count of the volumes or snapshots partnered with a network storage volume.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[permissionsGroupCount]: #permissionsgroupcount
#### [permissionsGroupCount]
A count of all permissions group(s) this volume is in.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[propertyCount]: #propertycount
#### [propertyCount]
A count of the properties used to provide additional details about a network storage volume.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[replicatingLunCount]: #replicatingluncount
#### [replicatingLunCount]
A count of the iSCSI LUN volumes being replicated by this network storage volume.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[replicationEventCount]: #replicationeventcount
#### [replicationEventCount]
A count of the volume replication events.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[replicationPartnerCount]: #replicationpartnercount
#### [replicationPartnerCount]
A count of the network storage volumes configured to be replicants of a volume.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[scheduleCount]: #schedulecount
#### [scheduleCount]
A count of the schedules which are associated with a network storage volume.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[snapshotCount]: #snapshotcount
#### [snapshotCount]
A count of the snapshots associated with this SoftLayer_Network_Storage volume.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[storageGroupCount]: #storagegroupcount
#### [storageGroupCount]
A count of the network storage groups this volume is attached to.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[volumeHistoryCount]: #volumehistorycount
#### [volumeHistoryCount]
A count of the username and password history for a Storage service.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


