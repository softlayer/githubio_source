---
title: "SoftLayer_Network_Storage_Backup_Evault"
description: "SoftLayer provides the EVault backup system as a part of it's Storage service offerings. EVault is an incremental and au... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
---
# SoftLayer_Network_Storage_Backup_Evault
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Storage_Backup_Evault' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_Backup_Evault' >Datatype</a></li>
    </ul>
</div>

## Description
SoftLayer provides the EVault backup system as a part of it's Storage service offerings. EVault is an incremental and automated backup solution with Windows and web-based management clients. The SoftLayer_Network_Storage_Backup_Evault service allows portal and API users to work with their EVault accounts. The large majority of EVault functionality is implemented in the SoftLayer_Network_Storage_Backup_Evault_Version6 service. 

### External Links


* [SoftLayer's service offerings](http://www.softlayer.com/services.html)




### seeAlso

* [SoftLayer_Network_Storage_Backup_Evault_Version6](/reference/datatypes/SoftLayer_Network_Storage_Backup_Evault_Version6 )


        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [allowAccessFromHardware](/reference/services/SoftLayer_Network_Storage_Backup_Evault/allowAccessFromHardware)
Allow access to this volume from a specified SoftLayer_Hardware object.

#### [allowAccessFromHardwareList](/reference/services/SoftLayer_Network_Storage_Backup_Evault/allowAccessFromHardwareList)


#### [allowAccessFromHost](/reference/services/SoftLayer_Network_Storage_Backup_Evault/allowAccessFromHost)
Allow access to this volume from a specified [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) object.

#### [allowAccessFromHostList](/reference/services/SoftLayer_Network_Storage_Backup_Evault/allowAccessFromHostList)
Allow access to this volume from multiple [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) objects.

#### [allowAccessFromIpAddress](/reference/services/SoftLayer_Network_Storage_Backup_Evault/allowAccessFromIpAddress)
Allow access to this volume from a specified SoftLayer_Network_Subnet_IpAddress object.

#### [allowAccessFromIpAddressList](/reference/services/SoftLayer_Network_Storage_Backup_Evault/allowAccessFromIpAddressList)


#### [allowAccessFromSubnet](/reference/services/SoftLayer_Network_Storage_Backup_Evault/allowAccessFromSubnet)
Allow access to this volume from multiple SoftLayer_Network_Subnet objects.

#### [allowAccessFromSubnetList](/reference/services/SoftLayer_Network_Storage_Backup_Evault/allowAccessFromSubnetList)


#### [allowAccessFromVirtualGuest](/reference/services/SoftLayer_Network_Storage_Backup_Evault/allowAccessFromVirtualGuest)
Allow access to this volume from a specified SoftLayer_Virtual_Guest object.

#### [allowAccessFromVirtualGuestList](/reference/services/SoftLayer_Network_Storage_Backup_Evault/allowAccessFromVirtualGuestList)
Allow access to this volume from multiple SoftLayer_Virtual_Guest objects.

#### [allowAccessToReplicantFromHardware](/reference/services/SoftLayer_Network_Storage_Backup_Evault/allowAccessToReplicantFromHardware)
Allow access to this replicant volume from a specified SoftLayer_Hardware object.

#### [allowAccessToReplicantFromHardwareList](/reference/services/SoftLayer_Network_Storage_Backup_Evault/allowAccessToReplicantFromHardwareList)
allow access to this volume's replica from multiple SoftLayer_Hardware objects.

#### [allowAccessToReplicantFromIpAddress](/reference/services/SoftLayer_Network_Storage_Backup_Evault/allowAccessToReplicantFromIpAddress)


#### [allowAccessToReplicantFromIpAddressList](/reference/services/SoftLayer_Network_Storage_Backup_Evault/allowAccessToReplicantFromIpAddressList)
allow access to this volume's replica from multiple SoftLayer_Network_Subnet_IpAddress objects.

#### [allowAccessToReplicantFromSubnet](/reference/services/SoftLayer_Network_Storage_Backup_Evault/allowAccessToReplicantFromSubnet)
Allow access to this replicant volume from multiple SoftLayer_Network_Subnet objects.

#### [allowAccessToReplicantFromSubnetList](/reference/services/SoftLayer_Network_Storage_Backup_Evault/allowAccessToReplicantFromSubnetList)
allow access to this volume's replica from multiple SoftLayer_Network_Subnet objects.

#### [allowAccessToReplicantFromVirtualGuest](/reference/services/SoftLayer_Network_Storage_Backup_Evault/allowAccessToReplicantFromVirtualGuest)
Allow access to this replicant volume from a specified SoftLayer_Virtual_Guest object.

#### [allowAccessToReplicantFromVirtualGuestList](/reference/services/SoftLayer_Network_Storage_Backup_Evault/allowAccessToReplicantFromVirtualGuestList)
allow access to this volume's replica from multiple SoftLayer_Virtual_Guest objects.

#### [assignCredential](/reference/services/SoftLayer_Network_Storage_Backup_Evault/assignCredential)
This method will assign an existing credential to the current volume.

#### [assignNewCredential](/reference/services/SoftLayer_Network_Storage_Backup_Evault/assignNewCredential)
This method will set up a new credential for the remote storage volume.

#### [changePassword](/reference/services/SoftLayer_Network_Storage_Backup_Evault/changePassword)
Change the password for a Storage/Virtual Server Storage account

#### [collectBandwidth](/reference/services/SoftLayer_Network_Storage_Backup_Evault/collectBandwidth)
Retrieve the bandwidth usage for the current billing cycle.

#### [collectBytesUsed](/reference/services/SoftLayer_Network_Storage_Backup_Evault/collectBytesUsed)
Retrieve the number of bytes capacity currently in use on a Storage account.

#### [createFolder](/reference/services/SoftLayer_Network_Storage_Backup_Evault/createFolder)
Create a new folder in the root directory.

#### [createOrUpdateLunId](/reference/services/SoftLayer_Network_Storage_Backup_Evault/createOrUpdateLunId)
Creates or updates the LUN ID property on a volume.

#### [createSnapshot](/reference/services/SoftLayer_Network_Storage_Backup_Evault/createSnapshot)
Manually create a new snapshot of a storage volume.

#### [deleteAllFiles](/reference/services/SoftLayer_Network_Storage_Backup_Evault/deleteAllFiles)
Delete all files within a Storage account.

#### [deleteFile](/reference/services/SoftLayer_Network_Storage_Backup_Evault/deleteFile)
Delete an individual file within a Storage account.

#### [deleteFiles](/reference/services/SoftLayer_Network_Storage_Backup_Evault/deleteFiles)
Delete multiple files within a Storage account.

#### [deleteFolder](/reference/services/SoftLayer_Network_Storage_Backup_Evault/deleteFolder)
Delete a folder in the root directory.

#### [deleteObject](/reference/services/SoftLayer_Network_Storage_Backup_Evault/deleteObject)
Delete a network storage volume

#### [deleteTasks](/reference/services/SoftLayer_Network_Storage_Backup_Evault/deleteTasks)
Delete task(s)

#### [disableSnapshots](/reference/services/SoftLayer_Network_Storage_Backup_Evault/disableSnapshots)
Disable snapshots of this Storage Volume on a schedule.

#### [downloadFile](/reference/services/SoftLayer_Network_Storage_Backup_Evault/downloadFile)
Download a file from a Storage account.

#### [editCredential](/reference/services/SoftLayer_Network_Storage_Backup_Evault/editCredential)
This method will change the password of a credential created using the 'addNewCredential' method.

#### [editObject](/reference/services/SoftLayer_Network_Storage_Backup_Evault/editObject)
Edit the password and/or notes for the Storage service

#### [enableSnapshots](/reference/services/SoftLayer_Network_Storage_Backup_Evault/enableSnapshots)
Enable snapshots of this Storage Volume on a schedule.

#### [failbackFromReplicant](/reference/services/SoftLayer_Network_Storage_Backup_Evault/failbackFromReplicant)
Failback from a volume replicant.

#### [failoverToReplicant](/reference/services/SoftLayer_Network_Storage_Backup_Evault/failoverToReplicant)
Failover to a volume replicant.

#### [getAccount](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getAccount)
Retrieve the account that a Storage services belongs to.

#### [getAccountPassword](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getAccountPassword)
Retrieve other usernames and passwords associated with a Storage volume.

#### [getActiveTransactions](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getActiveTransactions)
Retrieve the currently active transactions on a network storage volume.

#### [getAllFiles](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getAllFiles)
Retrieve a listing of all files in a Storage account's root directory.

#### [getAllFilesByFilter](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getAllFilesByFilter)
Retrieve a listing of all files matching the filter's criteria in a Storage account's root directory.

#### [getAllowableHardware](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getAllowableHardware)
Return a list of SoftLayer_Hardware that can be authorized to this volume. 

#### [getAllowableIpAddresses](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getAllowableIpAddresses)
Return a list of SoftLayer_Network_Subnet_IpAddress that can be authorized to this volume. 

#### [getAllowableSubnets](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getAllowableSubnets)
Return a list of SoftLayer_Network_Subnet that can be authorized to this volume. 

#### [getAllowableVirtualGuests](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getAllowableVirtualGuests)
Return a list of SoftLayer_Virtual_Guest that can be authorized to this volume. 

#### [getAllowedHardware](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getAllowedHardware)
Retrieve the SoftLayer_Hardware objects which are allowed access to this storage volume.

#### [getAllowedHostsLimit](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getAllowedHostsLimit)
Retrieves the total number of allowed hosts limit per volume.

#### [getAllowedIpAddresses](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getAllowedIpAddresses)
Retrieve the SoftLayer_Network_Subnet_IpAddress objects which are allowed access to this storage volume.

#### [getAllowedReplicationHardware](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getAllowedReplicationHardware)
Retrieve the SoftLayer_Hardware objects which are allowed access to this storage volume's Replicant.

#### [getAllowedReplicationIpAddresses](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getAllowedReplicationIpAddresses)
Retrieve the SoftLayer_Network_Subnet_IpAddress objects which are allowed access to this storage volume's Replicant.

#### [getAllowedReplicationSubnets](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getAllowedReplicationSubnets)
Retrieve the SoftLayer_Network_Subnet objects which are allowed access to this storage volume's Replicant.

#### [getAllowedReplicationVirtualGuests](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getAllowedReplicationVirtualGuests)
Retrieve the SoftLayer_Hardware objects which are allowed access to this storage volume's Replicant.

#### [getAllowedSubnets](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getAllowedSubnets)
Retrieve the SoftLayer_Network_Subnet objects which are allowed access to this storage volume.

#### [getAllowedVirtualGuests](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getAllowedVirtualGuests)
Retrieve the SoftLayer_Virtual_Guest objects which are allowed access to this storage volume.

#### [getBillingItem](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getBillingItem)
Retrieve the current billing item for the Storage volume.

#### [getBillingItemCategory](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getBillingItemCategory)


#### [getByUsername](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getByUsername)
Retrieve network storage accounts by username. 

#### [getBytesUsed](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getBytesUsed)
Retrieve the amount of space used by the volume, in bytes.

#### [getCdnUrls](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getCdnUrls)


#### [getClusterResource](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getClusterResource)


#### [getCreationScheduleId](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getCreationScheduleId)
Retrieve the schedule id which was executed to create a snapshot.

#### [getCredentials](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getCredentials)


#### [getCurrentCyclePeakUsage](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getCurrentCyclePeakUsage)
Retrieve peak number of bytes used in the vault for the current billing cycle.

#### [getDailySchedule](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getDailySchedule)
Retrieve the Daily Schedule which is associated with this network storage volume.

#### [getDependentDuplicate](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getDependentDuplicate)
Retrieve whether or not a network storage volume is a dependent duplicate.

#### [getEvents](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getEvents)
Retrieve the events which have taken place on a network storage volume.

#### [getFileBlockEncryptedLocations](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getFileBlockEncryptedLocations)
Returns a list of SoftLayer_Location_Datacenter objects corresponding to Datacenters in which File and Block Storage Volumes with Encryption at Rest may be ordered. 

#### [getFileByIdentifier](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getFileByIdentifier)
Retrieve an individual file's details.

#### [getFileCount](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getFileCount)
Retrieve the file number of files in a Virtual Server Storage account's root directory.

#### [getFileList](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getFileList)
Retrieve list of files in a given folder for this account.

#### [getFileNetworkMountAddress](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getFileNetworkMountAddress)
Retrieve retrieves the NFS Network Mount Address Name for a given File Storage Volume.

#### [getFilePendingDeleteCount](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getFilePendingDeleteCount)
Retrieve the number of files pending deletion in a Storage account's recycle bin.

#### [getFilesPendingDelete](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getFilesPendingDelete)
Retrieve a list of files in a Storage account's recycle bin.

#### [getFolderList](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getFolderList)
Retrieve a list of level 1 folders for this account.

#### [getGraph](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getGraph)
Retrieve a graph representing the bandwidth used by a Storage account.

#### [getHardware](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getHardware)
Retrieve when applicable, the hardware associated with a Storage service.

#### [getHardwareWithEvaultFirst](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getHardwareWithEvaultFirst)
Retrieve all the hardware for the account listing the hardware with EVault Storage service first. The output will be paginated having 25 items on each page. 

#### [getHasEncryptionAtRest](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getHasEncryptionAtRest)


#### [getHourlySchedule](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getHourlySchedule)
Retrieve the Hourly Schedule which is associated with this network storage volume.

#### [getIntervalSchedule](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getIntervalSchedule)
Retrieve the Interval Schedule which is associated with this network storage volume.

#### [getIops](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getIops)
Retrieve the maximum number of IOPs selected for this volume.

#### [getIsDependentDuplicateProvisionCompleted](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getIsDependentDuplicateProvisionCompleted)
Retrieve determines whether dependent volume provision is completed on background.

#### [getIsReadyForSnapshot](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getIsReadyForSnapshot)
Retrieve determines whether a volume is ready to order snapshot space, or, if snapshot space is already available, to assign a snapshot schedule, or to take a manual snapshot.

#### [getIsReadyToMount](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getIsReadyToMount)
Retrieve determines whether a volume is ready to have Hosts authorized to access it. This does not indicate whether another operation may be blocking, please refer to this volume's volumeStatus property for details.

#### [getIscsiLuns](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getIscsiLuns)
Retrieve relationship between a container volume and iSCSI LUNs.

#### [getIscsiTargetIpAddresses](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getIscsiTargetIpAddresses)
Retrieve returns the target IP addresses of an iSCSI volume.

#### [getLunId](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getLunId)
Retrieve the ID of the LUN volume.

#### [getManualSnapshots](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getManualSnapshots)
Retrieve the manually-created snapshots associated with this SoftLayer_Network_Storage volume. Does not support pagination by result limit and offset.

#### [getMaximumExpansionSize](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getMaximumExpansionSize)
Returns the maximum volume expansion size in GB.

#### [getMetricTrackingObject](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getMetricTrackingObject)
Retrieve a network storage volume's metric tracking object. This object records all periodic polled data available to this volume.

#### [getMountableFlag](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getMountableFlag)
Retrieve whether or not a network storage volume may be mounted.

#### [getMoveAndSplitStatus](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getMoveAndSplitStatus)
Retrieve the current status of split or move operation as a part of volume duplication.

#### [getNetworkConnectionDetails](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getNetworkConnectionDetails)
Retrieve network connection details for complex network storage volumes.

#### [getNetworkMountAddress](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getNetworkMountAddress)
Displays the mount path of a storage volume.

#### [getNotificationSubscribers](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getNotificationSubscribers)
Retrieve the subscribers that will be notified for usage amount warnings and overages.

#### [getObject](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getObject)
Retrieve a SoftLayer_Network_Storage_Backup_Evault record.

#### [getObjectStorageConnectionInformation](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getObjectStorageConnectionInformation)
Retrieve all object storage details for connection

#### [getObjectsByCredential](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getObjectsByCredential)
Retrieve network storage accounts by SoftLayer_Network_Storage_Credential object. 

#### [getOriginalSnapshotName](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getOriginalSnapshotName)
Retrieve the name of the snapshot that this volume was duplicated from.

#### [getOriginalVolumeName](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getOriginalVolumeName)
Retrieve the name of the volume that this volume was duplicated from.

#### [getOriginalVolumeSize](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getOriginalVolumeSize)
Retrieve the size (in GB) of the volume or LUN before any size expansion, or of the volume (before any possible size expansion) from which the duplicate volume or LUN was created.

#### [getOsType](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getOsType)
Retrieve a volume's configured SoftLayer_Network_Storage_Iscsi_OS_Type.

#### [getOsTypeId](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getOsTypeId)
Retrieve a volume's configured SoftLayer_Network_Storage_Iscsi_OS_Type ID.

#### [getParentPartnerships](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getParentPartnerships)
Retrieve the volumes or snapshots partnered with a network storage volume in a parental role.

#### [getParentVolume](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getParentVolume)
Retrieve the parent volume of a volume in a complex storage relationship.

#### [getPartnerships](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getPartnerships)
Retrieve the volumes or snapshots partnered with a network storage volume.

#### [getPermissionsGroups](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getPermissionsGroups)
Retrieve all permissions group(s) this volume is in.

#### [getPreviousCyclePeakUsage](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getPreviousCyclePeakUsage)
Retrieve peak number of bytes used in the vault for the previous billing cycle.

#### [getProperties](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getProperties)
Retrieve the properties used to provide additional details about a network storage volume.

#### [getProvisionedIops](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getProvisionedIops)
Retrieve the number of IOPs provisioned for this volume.

#### [getRecycleBinFileByIdentifier](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getRecycleBinFileByIdentifier)
Retrieve all files that are in the recycle bin (pending delete).  This method is only used for Virtual Server Storage accounts at moment but may expanded to other Storage types in the future.

#### [getRemainingAllowedHosts](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getRemainingAllowedHosts)
Retrieves the remaining number of allowed hosts per volume.

#### [getRemainingAllowedHostsForReplicant](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getRemainingAllowedHostsForReplicant)
Retrieves the remaining number of allowed hosts for a volume's replicant.

#### [getReplicatingLuns](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getReplicatingLuns)
Retrieve the iSCSI LUN volumes being replicated by this network storage volume.

#### [getReplicatingVolume](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getReplicatingVolume)
Retrieve the network storage volume being replicated by a volume.

#### [getReplicationEvents](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getReplicationEvents)
Retrieve the volume replication events.

#### [getReplicationPartners](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getReplicationPartners)
Retrieve the network storage volumes configured to be replicants of a volume.

#### [getReplicationSchedule](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getReplicationSchedule)
Retrieve the Replication Schedule associated with a network storage volume.

#### [getReplicationStatus](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getReplicationStatus)
Retrieve the current replication status of a network storage volume. Indicates Failover or Failback status.

#### [getSchedules](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getSchedules)
Retrieve the schedules which are associated with a network storage volume.

#### [getServiceResource](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getServiceResource)
Retrieve the network resource a Storage service is connected to.

#### [getServiceResourceBackendIpAddress](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getServiceResourceBackendIpAddress)
Retrieve the IP address of a Storage resource.

#### [getServiceResourceName](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getServiceResourceName)
Retrieve the name of a Storage's network resource.

#### [getSnapshotCapacityGb](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getSnapshotCapacityGb)
Retrieve a volume's configured snapshot space size.

#### [getSnapshotCreationTimestamp](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getSnapshotCreationTimestamp)
Retrieve the creation timestamp of the snapshot on the storage platform.

#### [getSnapshotDeletionThresholdPercentage](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getSnapshotDeletionThresholdPercentage)
Retrieve the percentage of used snapshot space after which to delete automated snapshots.

#### [getSnapshotSizeBytes](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getSnapshotSizeBytes)
Retrieve the snapshot size in bytes.

#### [getSnapshotSpaceAvailable](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getSnapshotSpaceAvailable)
Retrieve a volume's available snapshot reservation space.

#### [getSnapshots](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getSnapshots)
Retrieve the snapshots associated with this SoftLayer_Network_Storage volume.

#### [getSnapshotsForVolume](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getSnapshotsForVolume)
Retrieves a list oƒf snapshots for a given volume.

#### [getStaasVersion](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getStaasVersion)


#### [getStorageGroups](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getStorageGroups)
Retrieve the network storage groups this volume is attached to.

#### [getStorageGroupsNetworkConnectionDetails](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getStorageGroupsNetworkConnectionDetails)


#### [getStorageTierLevel](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getStorageTierLevel)


#### [getStorageType](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getStorageType)
Retrieve a description of the Storage object.

#### [getTargetIpAddresses](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getTargetIpAddresses)


#### [getTotalBytesUsed](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getTotalBytesUsed)
Retrieve the amount of space used by the volume.

#### [getTotalScheduleSnapshotRetentionCount](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getTotalScheduleSnapshotRetentionCount)
Retrieve the total snapshot retention count of all schedules on this network storage volume.

#### [getUsageNotification](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getUsageNotification)
Retrieve the usage notification for SL Storage services.

#### [getValidReplicationTargetDatacenterLocations](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getValidReplicationTargetDatacenterLocations)


#### [getVendorName](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getVendorName)
Retrieve the type of network storage service.

#### [getVirtualGuest](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getVirtualGuest)
Retrieve when applicable, the virtual guest associated with a Storage service.

#### [getVolumeDuplicateParameters](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getVolumeDuplicateParameters)


#### [getVolumeHistory](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getVolumeHistory)
Retrieve the username and password history for a Storage service.

#### [getVolumeStatus](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getVolumeStatus)
Retrieve the current status of a network storage volume.

#### [getWebCCAuthenticationDetails](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getWebCCAuthenticationDetails)
Retrieve WebCC authentication details value. This value is required for the login process associated to the session information for WebCC. 

#### [getWebccAccount](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getWebccAccount)
Retrieve the account username and password for the EVault webCC interface.

#### [getWeeklySchedule](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getWeeklySchedule)
Retrieve the Weekly Schedule which is associated with this network storage volume.

#### [immediateFailoverToReplicant](/reference/services/SoftLayer_Network_Storage_Backup_Evault/immediateFailoverToReplicant)
Immediate Failover to a volume replicant.

#### [initiateBareMetalRestore](/reference/services/SoftLayer_Network_Storage_Backup_Evault/initiateBareMetalRestore)
Initiate a bare metal restore for the server tied to the EVault account

#### [initiateBareMetalRestoreForServer](/reference/services/SoftLayer_Network_Storage_Backup_Evault/initiateBareMetalRestoreForServer)
Initiate a bare metal restore for the specified server

#### [isBlockingOperationInProgress](/reference/services/SoftLayer_Network_Storage_Backup_Evault/isBlockingOperationInProgress)


#### [isDuplicateReadyForSnapshot](/reference/services/SoftLayer_Network_Storage_Backup_Evault/isDuplicateReadyForSnapshot)
Displays the if clone snapshots can be ordered.

#### [isDuplicateReadyToMount](/reference/services/SoftLayer_Network_Storage_Backup_Evault/isDuplicateReadyToMount)
Displays the status of a clone mount.

#### [isVolumeActive](/reference/services/SoftLayer_Network_Storage_Backup_Evault/isVolumeActive)


#### [removeAccessFromHardware](/reference/services/SoftLayer_Network_Storage_Backup_Evault/removeAccessFromHardware)
Remove access to this volume from a specified SoftLayer_Hardware object.

#### [removeAccessFromHardwareList](/reference/services/SoftLayer_Network_Storage_Backup_Evault/removeAccessFromHardwareList)
Remove access to this volume from multiple SoftLayer_Hardware objects.

#### [removeAccessFromHost](/reference/services/SoftLayer_Network_Storage_Backup_Evault/removeAccessFromHost)
Remove access to this volume from a specified [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) object.

#### [removeAccessFromHostList](/reference/services/SoftLayer_Network_Storage_Backup_Evault/removeAccessFromHostList)
Remove access to this volume from multiple [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) objects.

#### [removeAccessFromIpAddress](/reference/services/SoftLayer_Network_Storage_Backup_Evault/removeAccessFromIpAddress)
Remove access to this volume from a specified SoftLayer_Network_Subnet_IpAddress object.

#### [removeAccessFromIpAddressList](/reference/services/SoftLayer_Network_Storage_Backup_Evault/removeAccessFromIpAddressList)


#### [removeAccessFromSubnet](/reference/services/SoftLayer_Network_Storage_Backup_Evault/removeAccessFromSubnet)


#### [removeAccessFromSubnetList](/reference/services/SoftLayer_Network_Storage_Backup_Evault/removeAccessFromSubnetList)


#### [removeAccessFromVirtualGuest](/reference/services/SoftLayer_Network_Storage_Backup_Evault/removeAccessFromVirtualGuest)
Remove access to this volume from a specified SoftLayer_Virtual_Guest object.

#### [removeAccessFromVirtualGuestList](/reference/services/SoftLayer_Network_Storage_Backup_Evault/removeAccessFromVirtualGuestList)
Remove access to this volume from multiple SoftLayer_Virtual_Guest objects.

#### [removeAccessToReplicantFromHardwareList](/reference/services/SoftLayer_Network_Storage_Backup_Evault/removeAccessToReplicantFromHardwareList)
Remove access to this volume's replica from multiple SoftLayer_Hardware objects.

#### [removeAccessToReplicantFromIpAddressList](/reference/services/SoftLayer_Network_Storage_Backup_Evault/removeAccessToReplicantFromIpAddressList)
Remove access to this replica volume's replica from multiple SoftLayer_Network_Subnet_IpAddress objects.

#### [removeAccessToReplicantFromSubnet](/reference/services/SoftLayer_Network_Storage_Backup_Evault/removeAccessToReplicantFromSubnet)


#### [removeAccessToReplicantFromSubnetList](/reference/services/SoftLayer_Network_Storage_Backup_Evault/removeAccessToReplicantFromSubnetList)
Remove access to this volume's replica from multiple SoftLayer_Network_Subnet objects.

#### [removeAccessToReplicantFromVirtualGuestList](/reference/services/SoftLayer_Network_Storage_Backup_Evault/removeAccessToReplicantFromVirtualGuestList)
Remove access to this volume's replica from multiple SoftLayer_Virtual_Guest objects.

#### [removeCredential](/reference/services/SoftLayer_Network_Storage_Backup_Evault/removeCredential)
This method will remove a credential from the current volume.

#### [restoreFile](/reference/services/SoftLayer_Network_Storage_Backup_Evault/restoreFile)
Restore access to an individual file in a Storage account.

#### [restoreFromSnapshot](/reference/services/SoftLayer_Network_Storage_Backup_Evault/restoreFromSnapshot)
Restore from a volume snapshot.

#### [sendPasswordReminderEmail](/reference/services/SoftLayer_Network_Storage_Backup_Evault/sendPasswordReminderEmail)
Email the password for the Storage account to the master user.

#### [setMountable](/reference/services/SoftLayer_Network_Storage_Backup_Evault/setMountable)
Enable or disable mounting of a Storage volume.

#### [setSnapshotAllocation](/reference/services/SoftLayer_Network_Storage_Backup_Evault/setSnapshotAllocation)


#### [upgradeVolumeCapacity](/reference/services/SoftLayer_Network_Storage_Backup_Evault/upgradeVolumeCapacity)
Edit the Storage volume to a different package

#### [uploadFile](/reference/services/SoftLayer_Network_Storage_Backup_Evault/uploadFile)
Upload a file to a Storage account's root directory.

</div>

