---
title: "SoftLayer_Network_Storage"
description: "SoftLayer customers may have a Storage volume associated with their account. Storage types include NAS, Lockbox, iSCSI,... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
---
# SoftLayer_Network_Storage
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Storage' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage' >Datatype</a></li>
    </ul>
</div>

## Description
SoftLayer customers may have a Storage volume associated with their account. Storage types include NAS, Lockbox, iSCSI, EVault backup, and Hub cloud storage. Information such as the account the Storage volume is associated to, username and password to access the Storage volume, related server (EVault only) and the capacity used are some of the details that may be retrieved using this service. Information regarding the Storage's resource that is useful in reconfiguring and mounting a StorageLayer volume may also be retrieved from this service. 

For the EVault Storage services, the username and passwords in the SoftLayer_Network_Storage services are used to register the EVault server agent with the vault. Please see the [SoftLayer_Account_Password]({{<ref "reference/datatypes/SoftLayer_Account_Password">}}) service to edit the passwords and notes for the EVault Webcc tool. 



### seeAlso

* [SoftLayer_Network_Storage_Nas](/reference/datatypes/SoftLayer_Network_Storage_Nas )


* [SoftLayer_Network_Storage_Iscsi](/reference/services/SoftLayer_Network_Storage_Iscsi )


* [SoftLayer_Network_Storage_Hub](/reference/datatypes/SoftLayer_Network_Storage_Hub )


* [SoftLayer_Network_Storage_Backup_Evault](/reference/services/SoftLayer_Network_Storage_Backup_Evault )


        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [allowAccessFromHardware](/reference/services/SoftLayer_Network_Storage/allowAccessFromHardware)
Allow access to this volume from a specified SoftLayer_Hardware object.
</div>

<div class="method-row">

#### [allowAccessFromHardwareList](/reference/services/SoftLayer_Network_Storage/allowAccessFromHardwareList)

</div>

<div class="method-row">

#### [allowAccessFromHost](/reference/services/SoftLayer_Network_Storage/allowAccessFromHost)
Allow access to this volume from a specified [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) object.
</div>

<div class="method-row">

#### [allowAccessFromHostList](/reference/services/SoftLayer_Network_Storage/allowAccessFromHostList)
Allow access to this volume from multiple [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) objects.
</div>

<div class="method-row">

#### [allowAccessFromIpAddress](/reference/services/SoftLayer_Network_Storage/allowAccessFromIpAddress)
Allow access to this volume from a specified SoftLayer_Network_Subnet_IpAddress object.
</div>

<div class="method-row">

#### [allowAccessFromIpAddressList](/reference/services/SoftLayer_Network_Storage/allowAccessFromIpAddressList)

</div>

<div class="method-row">

#### [allowAccessFromSubnet](/reference/services/SoftLayer_Network_Storage/allowAccessFromSubnet)
Allow access to this volume from multiple SoftLayer_Network_Subnet objects.
</div>

<div class="method-row">

#### [allowAccessFromSubnetList](/reference/services/SoftLayer_Network_Storage/allowAccessFromSubnetList)

</div>

<div class="method-row">

#### [allowAccessFromVirtualGuest](/reference/services/SoftLayer_Network_Storage/allowAccessFromVirtualGuest)
Allow access to this volume from a specified SoftLayer_Virtual_Guest object.
</div>

<div class="method-row">

#### [allowAccessFromVirtualGuestList](/reference/services/SoftLayer_Network_Storage/allowAccessFromVirtualGuestList)
Allow access to this volume from multiple SoftLayer_Virtual_Guest objects.
</div>

<div class="method-row">

#### [allowAccessToReplicantFromHardware](/reference/services/SoftLayer_Network_Storage/allowAccessToReplicantFromHardware)
Allow access to this replicant volume from a specified SoftLayer_Hardware object.
</div>

<div class="method-row">

#### [allowAccessToReplicantFromHardwareList](/reference/services/SoftLayer_Network_Storage/allowAccessToReplicantFromHardwareList)
allow access to this volume's replica from multiple SoftLayer_Hardware objects.
</div>

<div class="method-row">

#### [allowAccessToReplicantFromIpAddress](/reference/services/SoftLayer_Network_Storage/allowAccessToReplicantFromIpAddress)

</div>

<div class="method-row">

#### [allowAccessToReplicantFromIpAddressList](/reference/services/SoftLayer_Network_Storage/allowAccessToReplicantFromIpAddressList)
allow access to this volume's replica from multiple SoftLayer_Network_Subnet_IpAddress objects.
</div>

<div class="method-row">

#### [allowAccessToReplicantFromSubnet](/reference/services/SoftLayer_Network_Storage/allowAccessToReplicantFromSubnet)
Allow access to this replicant volume from multiple SoftLayer_Network_Subnet objects.
</div>

<div class="method-row">

#### [allowAccessToReplicantFromSubnetList](/reference/services/SoftLayer_Network_Storage/allowAccessToReplicantFromSubnetList)
allow access to this volume's replica from multiple SoftLayer_Network_Subnet objects.
</div>

<div class="method-row">

#### [allowAccessToReplicantFromVirtualGuest](/reference/services/SoftLayer_Network_Storage/allowAccessToReplicantFromVirtualGuest)
Allow access to this replicant volume from a specified SoftLayer_Virtual_Guest object.
</div>

<div class="method-row">

#### [allowAccessToReplicantFromVirtualGuestList](/reference/services/SoftLayer_Network_Storage/allowAccessToReplicantFromVirtualGuestList)
allow access to this volume's replica from multiple SoftLayer_Virtual_Guest objects.
</div>

<div class="method-row">

#### [assignCredential](/reference/services/SoftLayer_Network_Storage/assignCredential)
This method will assign an existing credential to the current volume.
</div>

<div class="method-row">

#### [assignNewCredential](/reference/services/SoftLayer_Network_Storage/assignNewCredential)
This method will set up a new credential for the remote storage volume.
</div>

<div class="method-row">

#### [changePassword](/reference/services/SoftLayer_Network_Storage/changePassword)
Change the password for a Storage/Virtual Server Storage account
</div>

<div class="method-row">

#### [collectBandwidth](/reference/services/SoftLayer_Network_Storage/collectBandwidth)
Retrieve the bandwidth usage for the current billing cycle.
</div>

<div class="method-row">

#### [collectBytesUsed](/reference/services/SoftLayer_Network_Storage/collectBytesUsed)
Retrieve the number of bytes capacity currently in use on a Storage account.
</div>

<div class="method-row">

#### [convertCloneDependentToIndependent](/reference/services/SoftLayer_Network_Storage/convertCloneDependentToIndependent)

</div>

<div class="method-row">

#### [createFolder](/reference/services/SoftLayer_Network_Storage/createFolder)
Create a new folder in the root directory.
</div>

<div class="method-row">

#### [createOrUpdateLunId](/reference/services/SoftLayer_Network_Storage/createOrUpdateLunId)
Creates or updates the LUN ID property on a volume.
</div>

<div class="method-row">

#### [createSnapshot](/reference/services/SoftLayer_Network_Storage/createSnapshot)
Manually create a new snapshot of a storage volume.
</div>

<div class="method-row">

#### [deleteAllFiles](/reference/services/SoftLayer_Network_Storage/deleteAllFiles)
Delete all files within a Storage account.
</div>

<div class="method-row">

#### [deleteFile](/reference/services/SoftLayer_Network_Storage/deleteFile)
Delete an individual file within a Storage account.
</div>

<div class="method-row">

#### [deleteFiles](/reference/services/SoftLayer_Network_Storage/deleteFiles)
Delete multiple files within a Storage account.
</div>

<div class="method-row">

#### [deleteFolder](/reference/services/SoftLayer_Network_Storage/deleteFolder)
Delete a folder in the root directory.
</div>

<div class="method-row">

#### [deleteObject](/reference/services/SoftLayer_Network_Storage/deleteObject)
Delete a network storage volume
</div>

<div class="method-row">

#### [disableSnapshots](/reference/services/SoftLayer_Network_Storage/disableSnapshots)
Disable snapshots of this Storage Volume on a schedule.
</div>

<div class="method-row">

#### [downloadFile](/reference/services/SoftLayer_Network_Storage/downloadFile)
Download a file from a Storage account.
</div>

<div class="method-row">

#### [editCredential](/reference/services/SoftLayer_Network_Storage/editCredential)
This method will change the password of a credential created using the 'addNewCredential' method.
</div>

<div class="method-row">

#### [editObject](/reference/services/SoftLayer_Network_Storage/editObject)
Edit the password and/or notes for the Storage service
</div>

<div class="method-row">

#### [enableSnapshots](/reference/services/SoftLayer_Network_Storage/enableSnapshots)
Enable snapshots of this Storage Volume on a schedule.
</div>

<div class="method-row">

#### [failbackFromReplicant](/reference/services/SoftLayer_Network_Storage/failbackFromReplicant)
Failback from a volume replicant.
</div>

<div class="method-row">

#### [failoverToReplicant](/reference/services/SoftLayer_Network_Storage/failoverToReplicant)
Failover to a volume replicant.
</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Network_Storage/getAccount)
Retrieve the account that a Storage services belongs to.
</div>

<div class="method-row">

#### [getAccountPassword](/reference/services/SoftLayer_Network_Storage/getAccountPassword)
Retrieve other usernames and passwords associated with a Storage volume.
</div>

<div class="method-row">

#### [getActiveTransactions](/reference/services/SoftLayer_Network_Storage/getActiveTransactions)
Retrieve the currently active transactions on a network storage volume.
</div>

<div class="method-row">

#### [getAllFiles](/reference/services/SoftLayer_Network_Storage/getAllFiles)
Retrieve a listing of all files in a Storage account's root directory.
</div>

<div class="method-row">

#### [getAllFilesByFilter](/reference/services/SoftLayer_Network_Storage/getAllFilesByFilter)
Retrieve a listing of all files matching the filter's criteria in a Storage account's root directory.
</div>

<div class="method-row">

#### [getAllowableHardware](/reference/services/SoftLayer_Network_Storage/getAllowableHardware)
Return a list of SoftLayer_Hardware that can be authorized to this volume. 
</div>

<div class="method-row">

#### [getAllowableIpAddresses](/reference/services/SoftLayer_Network_Storage/getAllowableIpAddresses)
Return a list of SoftLayer_Network_Subnet_IpAddress that can be authorized to this volume. 
</div>

<div class="method-row">

#### [getAllowableSubnets](/reference/services/SoftLayer_Network_Storage/getAllowableSubnets)
Return a list of SoftLayer_Network_Subnet that can be authorized to this volume. 
</div>

<div class="method-row">

#### [getAllowableVirtualGuests](/reference/services/SoftLayer_Network_Storage/getAllowableVirtualGuests)
Return a list of SoftLayer_Virtual_Guest that can be authorized to this volume. 
</div>

<div class="method-row">

#### [getAllowedHardware](/reference/services/SoftLayer_Network_Storage/getAllowedHardware)
Retrieve the SoftLayer_Hardware objects which are allowed access to this storage volume.
</div>

<div class="method-row">

#### [getAllowedHostsLimit](/reference/services/SoftLayer_Network_Storage/getAllowedHostsLimit)
Retrieves the total number of allowed hosts limit per volume.
</div>

<div class="method-row">

#### [getAllowedIpAddresses](/reference/services/SoftLayer_Network_Storage/getAllowedIpAddresses)
Retrieve the SoftLayer_Network_Subnet_IpAddress objects which are allowed access to this storage volume.
</div>

<div class="method-row">

#### [getAllowedReplicationHardware](/reference/services/SoftLayer_Network_Storage/getAllowedReplicationHardware)
Retrieve the SoftLayer_Hardware objects which are allowed access to this storage volume's Replicant.
</div>

<div class="method-row">

#### [getAllowedReplicationIpAddresses](/reference/services/SoftLayer_Network_Storage/getAllowedReplicationIpAddresses)
Retrieve the SoftLayer_Network_Subnet_IpAddress objects which are allowed access to this storage volume's Replicant.
</div>

<div class="method-row">

#### [getAllowedReplicationSubnets](/reference/services/SoftLayer_Network_Storage/getAllowedReplicationSubnets)
Retrieve the SoftLayer_Network_Subnet objects which are allowed access to this storage volume's Replicant.
</div>

<div class="method-row">

#### [getAllowedReplicationVirtualGuests](/reference/services/SoftLayer_Network_Storage/getAllowedReplicationVirtualGuests)
Retrieve the SoftLayer_Hardware objects which are allowed access to this storage volume's Replicant.
</div>

<div class="method-row">

#### [getAllowedSubnets](/reference/services/SoftLayer_Network_Storage/getAllowedSubnets)
Retrieve the SoftLayer_Network_Subnet objects which are allowed access to this storage volume.
</div>

<div class="method-row">

#### [getAllowedVirtualGuests](/reference/services/SoftLayer_Network_Storage/getAllowedVirtualGuests)
Retrieve the SoftLayer_Virtual_Guest objects which are allowed access to this storage volume.
</div>

<div class="method-row">

#### [getBillingItem](/reference/services/SoftLayer_Network_Storage/getBillingItem)
Retrieve the current billing item for a Storage volume.
</div>

<div class="method-row">

#### [getBillingItemCategory](/reference/services/SoftLayer_Network_Storage/getBillingItemCategory)

</div>

<div class="method-row">

#### [getByUsername](/reference/services/SoftLayer_Network_Storage/getByUsername)
Retrieve network storage accounts by username. 
</div>

<div class="method-row">

#### [getBytesUsed](/reference/services/SoftLayer_Network_Storage/getBytesUsed)
Retrieve the amount of space used by the volume, in bytes.
</div>

<div class="method-row">

#### [getCdnUrls](/reference/services/SoftLayer_Network_Storage/getCdnUrls)

</div>

<div class="method-row">

#### [getClusterResource](/reference/services/SoftLayer_Network_Storage/getClusterResource)

</div>

<div class="method-row">

#### [getCreationScheduleId](/reference/services/SoftLayer_Network_Storage/getCreationScheduleId)
Retrieve the schedule id which was executed to create a snapshot.
</div>

<div class="method-row">

#### [getCredentials](/reference/services/SoftLayer_Network_Storage/getCredentials)

</div>

<div class="method-row">

#### [getDailySchedule](/reference/services/SoftLayer_Network_Storage/getDailySchedule)
Retrieve the Daily Schedule which is associated with this network storage volume.
</div>

<div class="method-row">

#### [getDependentDuplicate](/reference/services/SoftLayer_Network_Storage/getDependentDuplicate)
Retrieve whether or not a network storage volume is a dependent duplicate.
</div>

<div class="method-row">

#### [getDependentDuplicates](/reference/services/SoftLayer_Network_Storage/getDependentDuplicates)
Retrieve the network storage volumes configured to be dependent duplicates of a volume.
</div>

<div class="method-row">

#### [getEvents](/reference/services/SoftLayer_Network_Storage/getEvents)
Retrieve the events which have taken place on a network storage volume.
</div>

<div class="method-row">

#### [getFileBlockEncryptedLocations](/reference/services/SoftLayer_Network_Storage/getFileBlockEncryptedLocations)
Returns a list of SoftLayer_Location_Datacenter objects corresponding to Datacenters in which File and Block Storage Volumes with Encryption at Rest may be ordered. 
</div>

<div class="method-row">

#### [getFileByIdentifier](/reference/services/SoftLayer_Network_Storage/getFileByIdentifier)
Retrieve an individual file's details.
</div>

<div class="method-row">

#### [getFileCount](/reference/services/SoftLayer_Network_Storage/getFileCount)
Retrieve the file number of files in a Virtual Server Storage account's root directory.
</div>

<div class="method-row">

#### [getFileList](/reference/services/SoftLayer_Network_Storage/getFileList)
Retrieve list of files in a given folder for this account.
</div>

<div class="method-row">

#### [getFileNetworkMountAddress](/reference/services/SoftLayer_Network_Storage/getFileNetworkMountAddress)
Retrieve retrieves the NFS Network Mount Address Name for a given File Storage Volume.
</div>

<div class="method-row">

#### [getFilePendingDeleteCount](/reference/services/SoftLayer_Network_Storage/getFilePendingDeleteCount)
Retrieve the number of files pending deletion in a Storage account's recycle bin.
</div>

<div class="method-row">

#### [getFilesPendingDelete](/reference/services/SoftLayer_Network_Storage/getFilesPendingDelete)
Retrieve a list of files in a Storage account's recycle bin.
</div>

<div class="method-row">

#### [getFolderList](/reference/services/SoftLayer_Network_Storage/getFolderList)
Retrieve a list of level 1 folders for this account.
</div>

<div class="method-row">

#### [getGraph](/reference/services/SoftLayer_Network_Storage/getGraph)
Retrieve a graph representing the bandwidth used by a Storage account.
</div>

<div class="method-row">

#### [getHardware](/reference/services/SoftLayer_Network_Storage/getHardware)
Retrieve when applicable, the hardware associated with a Storage service.
</div>

<div class="method-row">

#### [getHasEncryptionAtRest](/reference/services/SoftLayer_Network_Storage/getHasEncryptionAtRest)

</div>

<div class="method-row">

#### [getHourlySchedule](/reference/services/SoftLayer_Network_Storage/getHourlySchedule)
Retrieve the Hourly Schedule which is associated with this network storage volume.
</div>

<div class="method-row">

#### [getIntervalSchedule](/reference/services/SoftLayer_Network_Storage/getIntervalSchedule)
Retrieve the Interval Schedule which is associated with this network storage volume.
</div>

<div class="method-row">

#### [getIops](/reference/services/SoftLayer_Network_Storage/getIops)
Retrieve the maximum number of IOPs selected for this volume.
</div>

<div class="method-row">

#### [getIsDependentDuplicateProvisionCompleted](/reference/services/SoftLayer_Network_Storage/getIsDependentDuplicateProvisionCompleted)
Retrieve determines whether dependent volume provision is completed on background.
</div>

<div class="method-row">

#### [getIsReadyForSnapshot](/reference/services/SoftLayer_Network_Storage/getIsReadyForSnapshot)
Retrieve determines whether a volume is ready to order snapshot space, or, if snapshot space is already available, to assign a snapshot schedule, or to take a manual snapshot.
</div>

<div class="method-row">

#### [getIsReadyToMount](/reference/services/SoftLayer_Network_Storage/getIsReadyToMount)
Retrieve determines whether a volume is ready to have Hosts authorized to access it. This does not indicate whether another operation may be blocking, please refer to this volume's volumeStatus property for details.
</div>

<div class="method-row">

#### [getIscsiLuns](/reference/services/SoftLayer_Network_Storage/getIscsiLuns)
Retrieve relationship between a container volume and iSCSI LUNs.
</div>

<div class="method-row">

#### [getIscsiTargetIpAddresses](/reference/services/SoftLayer_Network_Storage/getIscsiTargetIpAddresses)
Retrieve returns the target IP addresses of an iSCSI volume.
</div>

<div class="method-row">

#### [getLunId](/reference/services/SoftLayer_Network_Storage/getLunId)
Retrieve the ID of the LUN volume.
</div>

<div class="method-row">

#### [getManualSnapshots](/reference/services/SoftLayer_Network_Storage/getManualSnapshots)
Retrieve the manually-created snapshots associated with this SoftLayer_Network_Storage volume. Does not support pagination by result limit and offset.
</div>

<div class="method-row">

#### [getMaximumExpansionSize](/reference/services/SoftLayer_Network_Storage/getMaximumExpansionSize)
Returns the maximum volume expansion size in GB.
</div>

<div class="method-row">

#### [getMetricTrackingObject](/reference/services/SoftLayer_Network_Storage/getMetricTrackingObject)
Retrieve a network storage volume's metric tracking object. This object records all periodic polled data available to this volume.
</div>

<div class="method-row">

#### [getMountableFlag](/reference/services/SoftLayer_Network_Storage/getMountableFlag)
Retrieve whether or not a network storage volume may be mounted.
</div>

<div class="method-row">

#### [getMoveAndSplitStatus](/reference/services/SoftLayer_Network_Storage/getMoveAndSplitStatus)
Retrieve the current status of split or move operation as a part of volume duplication.
</div>

<div class="method-row">

#### [getNetworkConnectionDetails](/reference/services/SoftLayer_Network_Storage/getNetworkConnectionDetails)
Retrieve network connection details for complex network storage volumes.
</div>

<div class="method-row">

#### [getNetworkMountAddress](/reference/services/SoftLayer_Network_Storage/getNetworkMountAddress)
Displays the mount path of a storage volume.
</div>

<div class="method-row">

#### [getNotificationSubscribers](/reference/services/SoftLayer_Network_Storage/getNotificationSubscribers)
Retrieve the subscribers that will be notified for usage amount warnings and overages.
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_Storage/getObject)
Retrieve a SoftLayer_Network_Storage record.
</div>

<div class="method-row">

#### [getObjectStorageConnectionInformation](/reference/services/SoftLayer_Network_Storage/getObjectStorageConnectionInformation)
Retrieve all object storage details for connection
</div>

<div class="method-row">

#### [getObjectsByCredential](/reference/services/SoftLayer_Network_Storage/getObjectsByCredential)
Retrieve network storage accounts by SoftLayer_Network_Storage_Credential object. 
</div>

<div class="method-row">

#### [getOriginalSnapshotName](/reference/services/SoftLayer_Network_Storage/getOriginalSnapshotName)
Retrieve the name of the snapshot that this volume was duplicated from.
</div>

<div class="method-row">

#### [getOriginalVolumeName](/reference/services/SoftLayer_Network_Storage/getOriginalVolumeName)
Retrieve the name of the volume that this volume was duplicated from.
</div>

<div class="method-row">

#### [getOriginalVolumeSize](/reference/services/SoftLayer_Network_Storage/getOriginalVolumeSize)
Retrieve the size (in GB) of the volume or LUN before any size expansion, or of the volume (before any possible size expansion) from which the duplicate volume or LUN was created.
</div>

<div class="method-row">

#### [getOsType](/reference/services/SoftLayer_Network_Storage/getOsType)
Retrieve a volume's configured SoftLayer_Network_Storage_Iscsi_OS_Type.
</div>

<div class="method-row">

#### [getOsTypeId](/reference/services/SoftLayer_Network_Storage/getOsTypeId)
Retrieve a volume's configured SoftLayer_Network_Storage_Iscsi_OS_Type ID.
</div>

<div class="method-row">

#### [getParentPartnerships](/reference/services/SoftLayer_Network_Storage/getParentPartnerships)
Retrieve the volumes or snapshots partnered with a network storage volume in a parental role.
</div>

<div class="method-row">

#### [getParentVolume](/reference/services/SoftLayer_Network_Storage/getParentVolume)
Retrieve the parent volume of a volume in a complex storage relationship.
</div>

<div class="method-row">

#### [getPartnerships](/reference/services/SoftLayer_Network_Storage/getPartnerships)
Retrieve the volumes or snapshots partnered with a network storage volume.
</div>

<div class="method-row">

#### [getPermissionsGroups](/reference/services/SoftLayer_Network_Storage/getPermissionsGroups)
Retrieve all permissions group(s) this volume is in.
</div>

<div class="method-row">

#### [getProperties](/reference/services/SoftLayer_Network_Storage/getProperties)
Retrieve the properties used to provide additional details about a network storage volume.
</div>

<div class="method-row">

#### [getProvisionedIops](/reference/services/SoftLayer_Network_Storage/getProvisionedIops)
Retrieve the number of IOPs provisioned for this volume.
</div>

<div class="method-row">

#### [getRecycleBinFileByIdentifier](/reference/services/SoftLayer_Network_Storage/getRecycleBinFileByIdentifier)
Retrieve all files that are in the recycle bin (pending delete).  This method is only used for Virtual Server Storage accounts at moment but may expanded to other Storage types in the future.
</div>

<div class="method-row">

#### [getRemainingAllowedHosts](/reference/services/SoftLayer_Network_Storage/getRemainingAllowedHosts)
Retrieves the remaining number of allowed hosts per volume.
</div>

<div class="method-row">

#### [getRemainingAllowedHostsForReplicant](/reference/services/SoftLayer_Network_Storage/getRemainingAllowedHostsForReplicant)
Retrieves the remaining number of allowed hosts for a volume's replicant.
</div>

<div class="method-row">

#### [getReplicatingLuns](/reference/services/SoftLayer_Network_Storage/getReplicatingLuns)
Retrieve the iSCSI LUN volumes being replicated by this network storage volume.
</div>

<div class="method-row">

#### [getReplicatingVolume](/reference/services/SoftLayer_Network_Storage/getReplicatingVolume)
Retrieve the network storage volume being replicated by a volume.
</div>

<div class="method-row">

#### [getReplicationEvents](/reference/services/SoftLayer_Network_Storage/getReplicationEvents)
Retrieve the volume replication events.
</div>

<div class="method-row">

#### [getReplicationPartners](/reference/services/SoftLayer_Network_Storage/getReplicationPartners)
Retrieve the network storage volumes configured to be replicants of a volume.
</div>

<div class="method-row">

#### [getReplicationSchedule](/reference/services/SoftLayer_Network_Storage/getReplicationSchedule)
Retrieve the Replication Schedule associated with a network storage volume.
</div>

<div class="method-row">

#### [getReplicationStatus](/reference/services/SoftLayer_Network_Storage/getReplicationStatus)
Retrieve the current replication status of a network storage volume. Indicates Failover or Failback status.
</div>

<div class="method-row">

#### [getSchedules](/reference/services/SoftLayer_Network_Storage/getSchedules)
Retrieve the schedules which are associated with a network storage volume.
</div>

<div class="method-row">

#### [getServiceResource](/reference/services/SoftLayer_Network_Storage/getServiceResource)
Retrieve the network resource a Storage service is connected to.
</div>

<div class="method-row">

#### [getServiceResourceBackendIpAddress](/reference/services/SoftLayer_Network_Storage/getServiceResourceBackendIpAddress)
Retrieve the IP address of a Storage resource.
</div>

<div class="method-row">

#### [getServiceResourceName](/reference/services/SoftLayer_Network_Storage/getServiceResourceName)
Retrieve the name of a Storage's network resource.
</div>

<div class="method-row">

#### [getSnapshotCapacityGb](/reference/services/SoftLayer_Network_Storage/getSnapshotCapacityGb)
Retrieve a volume's configured snapshot space size.
</div>

<div class="method-row">

#### [getSnapshotCreationTimestamp](/reference/services/SoftLayer_Network_Storage/getSnapshotCreationTimestamp)
Retrieve the creation timestamp of the snapshot on the storage platform.
</div>

<div class="method-row">

#### [getSnapshotDeletionThresholdPercentage](/reference/services/SoftLayer_Network_Storage/getSnapshotDeletionThresholdPercentage)
Retrieve the percentage of used snapshot space after which to delete automated snapshots.
</div>

<div class="method-row">

#### [getSnapshotSizeBytes](/reference/services/SoftLayer_Network_Storage/getSnapshotSizeBytes)
Retrieve the snapshot size in bytes.
</div>

<div class="method-row">

#### [getSnapshotSpaceAvailable](/reference/services/SoftLayer_Network_Storage/getSnapshotSpaceAvailable)
Retrieve a volume's available snapshot reservation space.
</div>

<div class="method-row">

#### [getSnapshots](/reference/services/SoftLayer_Network_Storage/getSnapshots)
Retrieve the snapshots associated with this SoftLayer_Network_Storage volume.
</div>

<div class="method-row">

#### [getSnapshotsForVolume](/reference/services/SoftLayer_Network_Storage/getSnapshotsForVolume)
Retrieves a list oƒf snapshots for a given volume.
</div>

<div class="method-row">

#### [getStaasVersion](/reference/services/SoftLayer_Network_Storage/getStaasVersion)

</div>

<div class="method-row">

#### [getStorageGroups](/reference/services/SoftLayer_Network_Storage/getStorageGroups)
Retrieve the network storage groups this volume is attached to.
</div>

<div class="method-row">

#### [getStorageGroupsNetworkConnectionDetails](/reference/services/SoftLayer_Network_Storage/getStorageGroupsNetworkConnectionDetails)

</div>

<div class="method-row">

#### [getStorageTierLevel](/reference/services/SoftLayer_Network_Storage/getStorageTierLevel)

</div>

<div class="method-row">

#### [getStorageType](/reference/services/SoftLayer_Network_Storage/getStorageType)
Retrieve a description of the Storage object.
</div>

<div class="method-row">

#### [getTargetIpAddresses](/reference/services/SoftLayer_Network_Storage/getTargetIpAddresses)

</div>

<div class="method-row">

#### [getTotalBytesUsed](/reference/services/SoftLayer_Network_Storage/getTotalBytesUsed)
Retrieve the amount of space used by the volume.
</div>

<div class="method-row">

#### [getTotalScheduleSnapshotRetentionCount](/reference/services/SoftLayer_Network_Storage/getTotalScheduleSnapshotRetentionCount)
Retrieve the total snapshot retention count of all schedules on this network storage volume.
</div>

<div class="method-row">

#### [getUsageNotification](/reference/services/SoftLayer_Network_Storage/getUsageNotification)
Retrieve the usage notification for SL Storage services.
</div>

<div class="method-row">

#### [getValidReplicationTargetDatacenterLocations](/reference/services/SoftLayer_Network_Storage/getValidReplicationTargetDatacenterLocations)

</div>

<div class="method-row">

#### [getVendorName](/reference/services/SoftLayer_Network_Storage/getVendorName)
Retrieve the type of network storage service.
</div>

<div class="method-row">

#### [getVirtualGuest](/reference/services/SoftLayer_Network_Storage/getVirtualGuest)
Retrieve when applicable, the virtual guest associated with a Storage service.
</div>

<div class="method-row">

#### [getVolumeDuplicateParameters](/reference/services/SoftLayer_Network_Storage/getVolumeDuplicateParameters)

</div>

<div class="method-row">

#### [getVolumeHistory](/reference/services/SoftLayer_Network_Storage/getVolumeHistory)
Retrieve the username and password history for a Storage service.
</div>

<div class="method-row">

#### [getVolumeStatus](/reference/services/SoftLayer_Network_Storage/getVolumeStatus)
Retrieve the current status of a network storage volume.
</div>

<div class="method-row">

#### [getWebccAccount](/reference/services/SoftLayer_Network_Storage/getWebccAccount)
Retrieve the account username and password for the EVault webCC interface.
</div>

<div class="method-row">

#### [getWeeklySchedule](/reference/services/SoftLayer_Network_Storage/getWeeklySchedule)
Retrieve the Weekly Schedule which is associated with this network storage volume.
</div>

<div class="method-row">

#### [immediateFailoverToReplicant](/reference/services/SoftLayer_Network_Storage/immediateFailoverToReplicant)
Immediate Failover to a volume replicant.
</div>

<div class="method-row">

#### [isBlockingOperationInProgress](/reference/services/SoftLayer_Network_Storage/isBlockingOperationInProgress)

</div>

<div class="method-row">

#### [isDuplicateReadyForSnapshot](/reference/services/SoftLayer_Network_Storage/isDuplicateReadyForSnapshot)
Displays the if clone snapshots can be ordered.
</div>

<div class="method-row">

#### [isDuplicateReadyToMount](/reference/services/SoftLayer_Network_Storage/isDuplicateReadyToMount)
Displays the status of a clone mount.
</div>

<div class="method-row">

#### [isVolumeActive](/reference/services/SoftLayer_Network_Storage/isVolumeActive)

</div>

<div class="method-row">

#### [removeAccessFromHardware](/reference/services/SoftLayer_Network_Storage/removeAccessFromHardware)
Remove access to this volume from a specified SoftLayer_Hardware object.
</div>

<div class="method-row">

#### [removeAccessFromHardwareList](/reference/services/SoftLayer_Network_Storage/removeAccessFromHardwareList)
Remove access to this volume from multiple SoftLayer_Hardware objects.
</div>

<div class="method-row">

#### [removeAccessFromHost](/reference/services/SoftLayer_Network_Storage/removeAccessFromHost)
Remove access to this volume from a specified [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) object.
</div>

<div class="method-row">

#### [removeAccessFromHostList](/reference/services/SoftLayer_Network_Storage/removeAccessFromHostList)
Remove access to this volume from multiple [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) objects.
</div>

<div class="method-row">

#### [removeAccessFromIpAddress](/reference/services/SoftLayer_Network_Storage/removeAccessFromIpAddress)
Remove access to this volume from a specified SoftLayer_Network_Subnet_IpAddress object.
</div>

<div class="method-row">

#### [removeAccessFromIpAddressList](/reference/services/SoftLayer_Network_Storage/removeAccessFromIpAddressList)

</div>

<div class="method-row">

#### [removeAccessFromSubnet](/reference/services/SoftLayer_Network_Storage/removeAccessFromSubnet)

</div>

<div class="method-row">

#### [removeAccessFromSubnetList](/reference/services/SoftLayer_Network_Storage/removeAccessFromSubnetList)

</div>

<div class="method-row">

#### [removeAccessFromVirtualGuest](/reference/services/SoftLayer_Network_Storage/removeAccessFromVirtualGuest)
Remove access to this volume from a specified SoftLayer_Virtual_Guest object.
</div>

<div class="method-row">

#### [removeAccessFromVirtualGuestList](/reference/services/SoftLayer_Network_Storage/removeAccessFromVirtualGuestList)
Remove access to this volume from multiple SoftLayer_Virtual_Guest objects.
</div>

<div class="method-row">

#### [removeAccessToReplicantFromHardwareList](/reference/services/SoftLayer_Network_Storage/removeAccessToReplicantFromHardwareList)
Remove access to this volume's replica from multiple SoftLayer_Hardware objects.
</div>

<div class="method-row">

#### [removeAccessToReplicantFromIpAddressList](/reference/services/SoftLayer_Network_Storage/removeAccessToReplicantFromIpAddressList)
Remove access to this replica volume's replica from multiple SoftLayer_Network_Subnet_IpAddress objects.
</div>

<div class="method-row">

#### [removeAccessToReplicantFromSubnet](/reference/services/SoftLayer_Network_Storage/removeAccessToReplicantFromSubnet)

</div>

<div class="method-row">

#### [removeAccessToReplicantFromSubnetList](/reference/services/SoftLayer_Network_Storage/removeAccessToReplicantFromSubnetList)
Remove access to this volume's replica from multiple SoftLayer_Network_Subnet objects.
</div>

<div class="method-row">

#### [removeAccessToReplicantFromVirtualGuestList](/reference/services/SoftLayer_Network_Storage/removeAccessToReplicantFromVirtualGuestList)
Remove access to this volume's replica from multiple SoftLayer_Virtual_Guest objects.
</div>

<div class="method-row">

#### [removeCredential](/reference/services/SoftLayer_Network_Storage/removeCredential)
This method will remove a credential from the current volume.
</div>

<div class="method-row">

#### [restoreFile](/reference/services/SoftLayer_Network_Storage/restoreFile)
Restore access to an individual file in a Storage account.
</div>

<div class="method-row">

#### [restoreFromSnapshot](/reference/services/SoftLayer_Network_Storage/restoreFromSnapshot)
Restore from a volume snapshot.
</div>

<div class="method-row">

#### [sendPasswordReminderEmail](/reference/services/SoftLayer_Network_Storage/sendPasswordReminderEmail)
Email the password for the Storage account to the master user.
</div>

<div class="method-row">

#### [setMountable](/reference/services/SoftLayer_Network_Storage/setMountable)
Enable or disable mounting of a Storage volume.
</div>

<div class="method-row">

#### [setSnapshotAllocation](/reference/services/SoftLayer_Network_Storage/setSnapshotAllocation)

</div>

<div class="method-row">

#### [upgradeVolumeCapacity](/reference/services/SoftLayer_Network_Storage/upgradeVolumeCapacity)
Edit the Storage volume to a different package
</div>

<div class="method-row">

#### [uploadFile](/reference/services/SoftLayer_Network_Storage/uploadFile)
Upload a file to a Storage account's root directory.
</div>
</div>

</div>

