---
title: "SoftLayer_Network_Storage_Iscsi"
description: "SoftLayer's iscsi product extends upon the base functionality of SoftLayer offerings by providing snapshot and replicati... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
---
# SoftLayer_Network_Storage_Iscsi
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Storage_Iscsi' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_Iscsi' >Datatype</a></li>
    </ul>
</div>

## Description
SoftLayer's iscsi product extends upon the base functionality of SoftLayer offerings by providing snapshot and replication capabilities. An iscsi volume is mounted through SoftLayer's private network and allows for block level additional storage on a highly redundant disk array. SoftLayer's iscsi offering is capable of taking volume snapshots which can be mounted read-only or used for an immediate volume data restore. This high-end Storage offering is also capable of being configured for remote data replication to any of SoftLayer's datacenters to provide a solid disaster recovery solution. 



        
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

#### [allowAccessFromHardware](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessFromHardware)
Allow access to this volume from a specified SoftLayer_Hardware object.

#### [allowAccessFromHardwareList](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessFromHardwareList)


#### [allowAccessFromHost](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessFromHost)
Allow access to this volume from a specified [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) object.

#### [allowAccessFromHostList](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessFromHostList)
Allow access to this volume from multiple [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) objects.

#### [allowAccessFromIpAddress](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessFromIpAddress)


#### [allowAccessFromIpAddressList](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessFromIpAddressList)


#### [allowAccessFromSubnet](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessFromSubnet)
Allow access to this volume from multiple SoftLayer_Network_Subnet objects.

#### [allowAccessFromSubnetList](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessFromSubnetList)


#### [allowAccessFromVirtualGuest](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessFromVirtualGuest)
Allow access to this volume from a specified SoftLayer_Virtual_Guest object.

#### [allowAccessFromVirtualGuestList](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessFromVirtualGuestList)
Allow access to this volume from multiple SoftLayer_Virtual_Guest objects.

#### [allowAccessToReplicantFromHardware](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessToReplicantFromHardware)
Allow access to this replicant volume from a specified SoftLayer_Hardware object.

#### [allowAccessToReplicantFromHardwareList](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessToReplicantFromHardwareList)
allow access to this replica volume from multiple SoftLayer_Hardware objects.

#### [allowAccessToReplicantFromIpAddress](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessToReplicantFromIpAddress)


#### [allowAccessToReplicantFromIpAddressList](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessToReplicantFromIpAddressList)
allow access to this volume from multiple SoftLayer_Network_Subnet_IpAddress objects.

#### [allowAccessToReplicantFromSubnet](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessToReplicantFromSubnet)
Allow access to this replicant volume from multiple SoftLayer_Network_Subnet objects.

#### [allowAccessToReplicantFromSubnetList](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessToReplicantFromSubnetList)
allow access to this volume's replica from multiple SoftLayer_Network_Subnet objects.

#### [allowAccessToReplicantFromVirtualGuest](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessToReplicantFromVirtualGuest)
Allow access to this replicant volume from a specified SoftLayer_Virtual_Guest object.

#### [allowAccessToReplicantFromVirtualGuestList](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessToReplicantFromVirtualGuestList)
allow access to this volume from multiple SoftLayer_Virtual_Guest objects.

#### [assignCredential](/reference/services/SoftLayer_Network_Storage_Iscsi/assignCredential)
This method will assign an existing credential to the current volume.

#### [assignNewCredential](/reference/services/SoftLayer_Network_Storage_Iscsi/assignNewCredential)
This method will set up a new credential for the remote storage volume.

#### [changePassword](/reference/services/SoftLayer_Network_Storage_Iscsi/changePassword)
Change the password for a Storage/Virtual Server Storage account

#### [collectBandwidth](/reference/services/SoftLayer_Network_Storage_Iscsi/collectBandwidth)
Retrieve the bandwidth usage for the current billing cycle.

#### [collectBytesUsed](/reference/services/SoftLayer_Network_Storage_Iscsi/collectBytesUsed)
Retrieve the number of bytes capacity currently in use on a Storage account.

#### [createFolder](/reference/services/SoftLayer_Network_Storage_Iscsi/createFolder)
Create a new folder in the root directory.

#### [createOrUpdateLunId](/reference/services/SoftLayer_Network_Storage_Iscsi/createOrUpdateLunId)
Creates or updates the LUN ID property on a volume.

#### [createSnapshot](/reference/services/SoftLayer_Network_Storage_Iscsi/createSnapshot)
Manually create a new snapshot of a storage volume.

#### [deleteAllFiles](/reference/services/SoftLayer_Network_Storage_Iscsi/deleteAllFiles)
Delete all files within a Storage account.

#### [deleteFile](/reference/services/SoftLayer_Network_Storage_Iscsi/deleteFile)
Delete an individual file within a Storage account.

#### [deleteFiles](/reference/services/SoftLayer_Network_Storage_Iscsi/deleteFiles)
Delete multiple files within a Storage account.

#### [deleteFolder](/reference/services/SoftLayer_Network_Storage_Iscsi/deleteFolder)
Delete a folder in the root directory.

#### [deleteObject](/reference/services/SoftLayer_Network_Storage_Iscsi/deleteObject)
Delete a network storage volume

#### [disableSnapshots](/reference/services/SoftLayer_Network_Storage_Iscsi/disableSnapshots)
Disable snapshots of this Storage Volume on a schedule.

#### [downloadFile](/reference/services/SoftLayer_Network_Storage_Iscsi/downloadFile)
Download a file from a Storage account.

#### [editCredential](/reference/services/SoftLayer_Network_Storage_Iscsi/editCredential)
This method will change the password of a credential created using the 'addNewCredential' method.

#### [editObject](/reference/services/SoftLayer_Network_Storage_Iscsi/editObject)
Edit the password and/or notes for the Storage service

#### [enableSnapshots](/reference/services/SoftLayer_Network_Storage_Iscsi/enableSnapshots)
Enable snapshots of this Storage Volume on a schedule.

#### [failbackFromReplicant](/reference/services/SoftLayer_Network_Storage_Iscsi/failbackFromReplicant)
Failback from a volume replicant.

#### [failoverToReplicant](/reference/services/SoftLayer_Network_Storage_Iscsi/failoverToReplicant)
Failover to a volume replicant.

#### [getAccount](/reference/services/SoftLayer_Network_Storage_Iscsi/getAccount)
Retrieve the account that a Storage services belongs to.

#### [getAccountPassword](/reference/services/SoftLayer_Network_Storage_Iscsi/getAccountPassword)
Retrieve other usernames and passwords associated with a Storage volume.

#### [getActiveTransactions](/reference/services/SoftLayer_Network_Storage_Iscsi/getActiveTransactions)
Retrieve the currently active transactions on a network storage volume.

#### [getAllFiles](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllFiles)
Retrieve a listing of all files in a Storage account's root directory.

#### [getAllFilesByFilter](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllFilesByFilter)
Retrieve a listing of all files matching the filter's criteria in a Storage account's root directory.

#### [getAllowableHardware](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowableHardware)
Return a list of SoftLayer_Hardware that can be authorized to this volume. 

#### [getAllowableIpAddresses](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowableIpAddresses)
Return a list of SoftLayer_Network_Subnet_IpAddress that can be authorized to this volume. 

#### [getAllowableSubnets](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowableSubnets)
Return a list of SoftLayer_Network_Subnet that can be authorized to this volume. 

#### [getAllowableVirtualGuests](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowableVirtualGuests)
Return a list of SoftLayer_Virtual_Guest that can be authorized to this volume. 

#### [getAllowedHardware](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowedHardware)
Retrieve the SoftLayer_Hardware objects which are allowed access to this storage volume.

#### [getAllowedHostsLimit](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowedHostsLimit)
Retrieves the total number of allowed hosts limit per volume.

#### [getAllowedIpAddresses](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowedIpAddresses)
Retrieve the SoftLayer_Network_Subnet_IpAddress objects which are allowed access to this storage volume.

#### [getAllowedReplicationHardware](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowedReplicationHardware)
Retrieve the SoftLayer_Hardware objects which are allowed access to this storage volume's Replicant.

#### [getAllowedReplicationIpAddresses](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowedReplicationIpAddresses)
Retrieve the SoftLayer_Network_Subnet_IpAddress objects which are allowed access to this storage volume's Replicant.

#### [getAllowedReplicationSubnets](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowedReplicationSubnets)
Retrieve the SoftLayer_Network_Subnet objects which are allowed access to this storage volume's Replicant.

#### [getAllowedReplicationVirtualGuests](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowedReplicationVirtualGuests)
Retrieve the SoftLayer_Hardware objects which are allowed access to this storage volume's Replicant.

#### [getAllowedSubnets](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowedSubnets)
Retrieve the SoftLayer_Network_Subnet objects which are allowed access to this storage volume.

#### [getAllowedVirtualGuests](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowedVirtualGuests)
Retrieve the SoftLayer_Virtual_Guest objects which are allowed access to this storage volume.

#### [getBillingItem](/reference/services/SoftLayer_Network_Storage_Iscsi/getBillingItem)
Retrieve the current billing item for a Storage volume.

#### [getBillingItemCategory](/reference/services/SoftLayer_Network_Storage_Iscsi/getBillingItemCategory)


#### [getByUsername](/reference/services/SoftLayer_Network_Storage_Iscsi/getByUsername)
Retrieve network storage accounts by username. 

#### [getBytesUsed](/reference/services/SoftLayer_Network_Storage_Iscsi/getBytesUsed)
Retrieve the amount of space used by the volume, in bytes.

#### [getCdnUrls](/reference/services/SoftLayer_Network_Storage_Iscsi/getCdnUrls)


#### [getClusterResource](/reference/services/SoftLayer_Network_Storage_Iscsi/getClusterResource)


#### [getCreationScheduleId](/reference/services/SoftLayer_Network_Storage_Iscsi/getCreationScheduleId)
Retrieve the schedule id which was executed to create a snapshot.

#### [getCredentials](/reference/services/SoftLayer_Network_Storage_Iscsi/getCredentials)


#### [getDailySchedule](/reference/services/SoftLayer_Network_Storage_Iscsi/getDailySchedule)
Retrieve the Daily Schedule which is associated with this network storage volume.

#### [getDependentDuplicate](/reference/services/SoftLayer_Network_Storage_Iscsi/getDependentDuplicate)
Retrieve whether or not a network storage volume is a dependent duplicate.

#### [getEvents](/reference/services/SoftLayer_Network_Storage_Iscsi/getEvents)
Retrieve the events which have taken place on a network storage volume.

#### [getFileBlockEncryptedLocations](/reference/services/SoftLayer_Network_Storage_Iscsi/getFileBlockEncryptedLocations)
Returns a list of SoftLayer_Location_Datacenter objects corresponding to Datacenters in which File and Block Storage Volumes with Encryption at Rest may be ordered. 

#### [getFileByIdentifier](/reference/services/SoftLayer_Network_Storage_Iscsi/getFileByIdentifier)
Retrieve an individual file's details.

#### [getFileCount](/reference/services/SoftLayer_Network_Storage_Iscsi/getFileCount)
Retrieve the file number of files in a Virtual Server Storage account's root directory.

#### [getFileList](/reference/services/SoftLayer_Network_Storage_Iscsi/getFileList)
Retrieve list of files in a given folder for this account.

#### [getFileNetworkMountAddress](/reference/services/SoftLayer_Network_Storage_Iscsi/getFileNetworkMountAddress)
Retrieve retrieves the NFS Network Mount Address Name for a given File Storage Volume.

#### [getFilePendingDeleteCount](/reference/services/SoftLayer_Network_Storage_Iscsi/getFilePendingDeleteCount)
Retrieve the number of files pending deletion in a Storage account's recycle bin.

#### [getFilesPendingDelete](/reference/services/SoftLayer_Network_Storage_Iscsi/getFilesPendingDelete)
Retrieve a list of files in a Storage account's recycle bin.

#### [getFolderList](/reference/services/SoftLayer_Network_Storage_Iscsi/getFolderList)
Retrieve a list of level 1 folders for this account.

#### [getGraph](/reference/services/SoftLayer_Network_Storage_Iscsi/getGraph)
Retrieve a graph representing the bandwidth used by a Storage account.

#### [getHardware](/reference/services/SoftLayer_Network_Storage_Iscsi/getHardware)
Retrieve when applicable, the hardware associated with a Storage service.

#### [getHasEncryptionAtRest](/reference/services/SoftLayer_Network_Storage_Iscsi/getHasEncryptionAtRest)


#### [getHourlySchedule](/reference/services/SoftLayer_Network_Storage_Iscsi/getHourlySchedule)
Retrieve the Hourly Schedule which is associated with this network storage volume.

#### [getIntervalSchedule](/reference/services/SoftLayer_Network_Storage_Iscsi/getIntervalSchedule)
Retrieve the Interval Schedule which is associated with this network storage volume.

#### [getIops](/reference/services/SoftLayer_Network_Storage_Iscsi/getIops)
Retrieve the maximum number of IOPs guaranteed for this LUN.

#### [getIsDependentDuplicateProvisionCompleted](/reference/services/SoftLayer_Network_Storage_Iscsi/getIsDependentDuplicateProvisionCompleted)
Retrieve determines whether dependent volume provision is completed on background.

#### [getIsReadyForSnapshot](/reference/services/SoftLayer_Network_Storage_Iscsi/getIsReadyForSnapshot)
Retrieve determines whether a volume is ready to order snapshot space, or, if snapshot space is already available, to assign a snapshot schedule, or to take a manual snapshot.

#### [getIsReadyToMount](/reference/services/SoftLayer_Network_Storage_Iscsi/getIsReadyToMount)
Retrieve determines whether a volume is ready to have Hosts authorized to access it. This does not indicate whether another operation may be blocking, please refer to this volume's volumeStatus property for details.

#### [getIscsiLuns](/reference/services/SoftLayer_Network_Storage_Iscsi/getIscsiLuns)
Retrieve relationship between a container volume and iSCSI LUNs.

#### [getIscsiTargetIpAddresses](/reference/services/SoftLayer_Network_Storage_Iscsi/getIscsiTargetIpAddresses)
Retrieve returns the target IP addresses of an iSCSI volume.

#### [getLunId](/reference/services/SoftLayer_Network_Storage_Iscsi/getLunId)
Retrieve the ID of the LUN volume.

#### [getManualSnapshots](/reference/services/SoftLayer_Network_Storage_Iscsi/getManualSnapshots)
Retrieve the snapshots associated with this SoftLayer_Network_Storage volume. Does not support pagination by result limit and offset.

#### [getMaximumExpansionSize](/reference/services/SoftLayer_Network_Storage_Iscsi/getMaximumExpansionSize)
Returns the maximum volume expansion size in GB.

#### [getMetricTrackingObject](/reference/services/SoftLayer_Network_Storage_Iscsi/getMetricTrackingObject)
Retrieve a network storage volume's metric tracking object. This object records all periodic polled data available to this volume.

#### [getMountableFlag](/reference/services/SoftLayer_Network_Storage_Iscsi/getMountableFlag)
Retrieve whether or not a network storage volume may be mounted.

#### [getMoveAndSplitStatus](/reference/services/SoftLayer_Network_Storage_Iscsi/getMoveAndSplitStatus)
Retrieve the current status of split or move operation as a part of volume duplication.

#### [getNetworkConnectionDetails](/reference/services/SoftLayer_Network_Storage_Iscsi/getNetworkConnectionDetails)
Retrieve network connection details for complex network storage volumes.

#### [getNetworkMountAddress](/reference/services/SoftLayer_Network_Storage_Iscsi/getNetworkMountAddress)
Displays the mount path of a storage volume.

#### [getNotificationSubscribers](/reference/services/SoftLayer_Network_Storage_Iscsi/getNotificationSubscribers)
Retrieve the subscribers that will be notified for usage amount warnings and overages.

#### [getObject](/reference/services/SoftLayer_Network_Storage_Iscsi/getObject)
Retrieve a SoftLayer_Network_Storage_Iscsi record.

#### [getObjectStorageConnectionInformation](/reference/services/SoftLayer_Network_Storage_Iscsi/getObjectStorageConnectionInformation)
Retrieve all object storage details for connection

#### [getObjectsByCredential](/reference/services/SoftLayer_Network_Storage_Iscsi/getObjectsByCredential)
Retrieve network storage accounts by SoftLayer_Network_Storage_Credential object. 

#### [getOriginalSnapshotName](/reference/services/SoftLayer_Network_Storage_Iscsi/getOriginalSnapshotName)
Retrieve the name of the snapshot that this volume was duplicated from.

#### [getOriginalVolumeName](/reference/services/SoftLayer_Network_Storage_Iscsi/getOriginalVolumeName)
Retrieve the name of the volume that this volume was duplicated from.

#### [getOriginalVolumeSize](/reference/services/SoftLayer_Network_Storage_Iscsi/getOriginalVolumeSize)
Retrieve the size (in GB) of the volume or LUN before any size expansion, or of the volume (before any possible size expansion) from which the duplicate volume or LUN was created.

#### [getOsType](/reference/services/SoftLayer_Network_Storage_Iscsi/getOsType)
Retrieve a volume's configured SoftLayer_Network_Storage_Iscsi_OS_Type.

#### [getOsTypeId](/reference/services/SoftLayer_Network_Storage_Iscsi/getOsTypeId)
Retrieve a volume's configured SoftLayer_Network_Storage_Iscsi_OS_Type ID.

#### [getParentPartnerships](/reference/services/SoftLayer_Network_Storage_Iscsi/getParentPartnerships)
Retrieve the volumes or snapshots partnered with a network storage volume in a parental role.

#### [getParentVolume](/reference/services/SoftLayer_Network_Storage_Iscsi/getParentVolume)
Retrieve the volume on which this iSCSI LUN is provisioned.

#### [getPartnerships](/reference/services/SoftLayer_Network_Storage_Iscsi/getPartnerships)
Retrieve the volumes or snapshots partnered with a network storage volume.

#### [getPermissionsGroups](/reference/services/SoftLayer_Network_Storage_Iscsi/getPermissionsGroups)
Retrieve all permissions group(s) this volume is in.

#### [getProperties](/reference/services/SoftLayer_Network_Storage_Iscsi/getProperties)
Retrieve the properties used to provide additional details about a network storage volume.

#### [getProvisionedIops](/reference/services/SoftLayer_Network_Storage_Iscsi/getProvisionedIops)
Retrieve the number of IOPs provisioned for this volume.

#### [getRecycleBinFileByIdentifier](/reference/services/SoftLayer_Network_Storage_Iscsi/getRecycleBinFileByIdentifier)
Retrieve all files that are in the recycle bin (pending delete).  This method is only used for Virtual Server Storage accounts at moment but may expanded to other Storage types in the future.

#### [getRemainingAllowedHosts](/reference/services/SoftLayer_Network_Storage_Iscsi/getRemainingAllowedHosts)
Retrieves the remaining number of allowed hosts per volume.

#### [getRemainingAllowedHostsForReplicant](/reference/services/SoftLayer_Network_Storage_Iscsi/getRemainingAllowedHostsForReplicant)
Retrieves the remaining number of allowed hosts for a volume's replicant.

#### [getReplicatingLuns](/reference/services/SoftLayer_Network_Storage_Iscsi/getReplicatingLuns)
Retrieve the iSCSI LUN volumes being replicated by this network storage volume.

#### [getReplicatingVolume](/reference/services/SoftLayer_Network_Storage_Iscsi/getReplicatingVolume)
Retrieve the network storage volume being replicated by a volume.

#### [getReplicationEvents](/reference/services/SoftLayer_Network_Storage_Iscsi/getReplicationEvents)
Retrieve the volume replication events.

#### [getReplicationPartners](/reference/services/SoftLayer_Network_Storage_Iscsi/getReplicationPartners)
Retrieve the network storage volumes configured to be replicants of a volume.

#### [getReplicationSchedule](/reference/services/SoftLayer_Network_Storage_Iscsi/getReplicationSchedule)
Retrieve the Replication Schedule associated with a network storage volume.

#### [getReplicationStatus](/reference/services/SoftLayer_Network_Storage_Iscsi/getReplicationStatus)
Retrieve the current replication status of a network storage volume. Indicates Failover or Failback status.

#### [getSchedules](/reference/services/SoftLayer_Network_Storage_Iscsi/getSchedules)
Retrieve the schedules which are associated with a network storage volume.

#### [getServiceResource](/reference/services/SoftLayer_Network_Storage_Iscsi/getServiceResource)
Retrieve the network resource a Storage service is connected to.

#### [getServiceResourceBackendIpAddress](/reference/services/SoftLayer_Network_Storage_Iscsi/getServiceResourceBackendIpAddress)
Retrieve the IP address of a Storage resource.

#### [getServiceResourceName](/reference/services/SoftLayer_Network_Storage_Iscsi/getServiceResourceName)
Retrieve the name of a Storage's network resource.

#### [getSnapshotCapacityGb](/reference/services/SoftLayer_Network_Storage_Iscsi/getSnapshotCapacityGb)
Retrieve a volume's configured snapshot space size.

#### [getSnapshotCreationTimestamp](/reference/services/SoftLayer_Network_Storage_Iscsi/getSnapshotCreationTimestamp)
Retrieve the creation timestamp of the snapshot on the storage platform.

#### [getSnapshotDeletionThresholdPercentage](/reference/services/SoftLayer_Network_Storage_Iscsi/getSnapshotDeletionThresholdPercentage)
Retrieve the percentage of used snapshot space after which to delete automated snapshots.

#### [getSnapshotSizeBytes](/reference/services/SoftLayer_Network_Storage_Iscsi/getSnapshotSizeBytes)
Retrieve the snapshot size in bytes.

#### [getSnapshotSpaceAvailable](/reference/services/SoftLayer_Network_Storage_Iscsi/getSnapshotSpaceAvailable)
Retrieve an volume's available snapshot reservation space.

#### [getSnapshots](/reference/services/SoftLayer_Network_Storage_Iscsi/getSnapshots)
Retrieve the snapshots associated with this iSCSI LUN's container volume, if applicable

#### [getSnapshotsForVolume](/reference/services/SoftLayer_Network_Storage_Iscsi/getSnapshotsForVolume)
Retrieves a list of snapshots for a given volume.

#### [getStaasVersion](/reference/services/SoftLayer_Network_Storage_Iscsi/getStaasVersion)


#### [getStorageGroups](/reference/services/SoftLayer_Network_Storage_Iscsi/getStorageGroups)
Retrieve the network storage groups this volume is attached to.

#### [getStorageGroupsNetworkConnectionDetails](/reference/services/SoftLayer_Network_Storage_Iscsi/getStorageGroupsNetworkConnectionDetails)


#### [getStorageTierLevel](/reference/services/SoftLayer_Network_Storage_Iscsi/getStorageTierLevel)


#### [getStorageType](/reference/services/SoftLayer_Network_Storage_Iscsi/getStorageType)
Retrieve a description of the Storage object.

#### [getTargetIpAddresses](/reference/services/SoftLayer_Network_Storage_Iscsi/getTargetIpAddresses)


#### [getTotalBytesUsed](/reference/services/SoftLayer_Network_Storage_Iscsi/getTotalBytesUsed)
Retrieve the amount of space used by the volume.

#### [getTotalScheduleSnapshotRetentionCount](/reference/services/SoftLayer_Network_Storage_Iscsi/getTotalScheduleSnapshotRetentionCount)
Retrieve the total snapshot retention count of all schedules on this network storage volume.

#### [getUsageNotification](/reference/services/SoftLayer_Network_Storage_Iscsi/getUsageNotification)
Retrieve the usage notification for SL Storage services.

#### [getValidReplicationTargetDatacenterLocations](/reference/services/SoftLayer_Network_Storage_Iscsi/getValidReplicationTargetDatacenterLocations)


#### [getVendorName](/reference/services/SoftLayer_Network_Storage_Iscsi/getVendorName)
Retrieve the type of network storage service.

#### [getVirtualGuest](/reference/services/SoftLayer_Network_Storage_Iscsi/getVirtualGuest)
Retrieve when applicable, the virtual guest associated with a Storage service.

#### [getVolumeDuplicateParameters](/reference/services/SoftLayer_Network_Storage_Iscsi/getVolumeDuplicateParameters)


#### [getVolumeHistory](/reference/services/SoftLayer_Network_Storage_Iscsi/getVolumeHistory)
Retrieve the username and password history for a Storage service.

#### [getVolumeStatus](/reference/services/SoftLayer_Network_Storage_Iscsi/getVolumeStatus)
Retrieve the current status of a network storage volume.

#### [getWebccAccount](/reference/services/SoftLayer_Network_Storage_Iscsi/getWebccAccount)
Retrieve the account username and password for the EVault webCC interface.

#### [getWeeklySchedule](/reference/services/SoftLayer_Network_Storage_Iscsi/getWeeklySchedule)
Retrieve the Weekly Schedule which is associated with this network storage volume.

#### [immediateFailoverToReplicant](/reference/services/SoftLayer_Network_Storage_Iscsi/immediateFailoverToReplicant)
Immediate Failover to a volume replicant.

#### [isBlockingOperationInProgress](/reference/services/SoftLayer_Network_Storage_Iscsi/isBlockingOperationInProgress)


#### [isDuplicateReadyForSnapshot](/reference/services/SoftLayer_Network_Storage_Iscsi/isDuplicateReadyForSnapshot)
Displays the if clone snapshots can be ordered.

#### [isDuplicateReadyToMount](/reference/services/SoftLayer_Network_Storage_Iscsi/isDuplicateReadyToMount)
Displays the status of a clone mount.

#### [isVolumeActive](/reference/services/SoftLayer_Network_Storage_Iscsi/isVolumeActive)


#### [removeAccessFromHardware](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessFromHardware)
Remove access to this volume from a specified SoftLayer_Hardware object.

#### [removeAccessFromHardwareList](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessFromHardwareList)
Remove access to this volume from multiple SoftLayer_Hardware objects.

#### [removeAccessFromHost](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessFromHost)
Remove access to this volume from a specified [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) object.

#### [removeAccessFromHostList](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessFromHostList)
Remove access to this volume from multiple [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) objects.

#### [removeAccessFromIpAddress](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessFromIpAddress)


#### [removeAccessFromIpAddressList](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessFromIpAddressList)


#### [removeAccessFromSubnet](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessFromSubnet)


#### [removeAccessFromSubnetList](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessFromSubnetList)


#### [removeAccessFromVirtualGuest](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessFromVirtualGuest)
Remove access to this volume from a specified SoftLayer_Virtual_Guest object.

#### [removeAccessFromVirtualGuestList](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessFromVirtualGuestList)
Remove access to this volume from multiple SoftLayer_Virtual_Guest objects.

#### [removeAccessToReplicantFromHardwareList](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessToReplicantFromHardwareList)
Remove access to this volume from multiple SoftLayer_Hardware objects.

#### [removeAccessToReplicantFromIpAddressList](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessToReplicantFromIpAddressList)
Remove access to this replica volume from multiple SoftLayer_Network_Subnet_IpAddress objects.

#### [removeAccessToReplicantFromSubnet](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessToReplicantFromSubnet)


#### [removeAccessToReplicantFromSubnetList](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessToReplicantFromSubnetList)
Remove access to this volume's replica from multiple SoftLayer_Network_Subnet objects.

#### [removeAccessToReplicantFromVirtualGuestList](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessToReplicantFromVirtualGuestList)
Remove access to this replica volume from multiple SoftLayer_Virtual_Guest objects.

#### [removeCredential](/reference/services/SoftLayer_Network_Storage_Iscsi/removeCredential)
This method will remove a credential from the current volume.

#### [restoreFile](/reference/services/SoftLayer_Network_Storage_Iscsi/restoreFile)
Restore access to an individual file in a Storage account.

#### [restoreFromSnapshot](/reference/services/SoftLayer_Network_Storage_Iscsi/restoreFromSnapshot)
Restore from a volume snapshot.

#### [sendPasswordReminderEmail](/reference/services/SoftLayer_Network_Storage_Iscsi/sendPasswordReminderEmail)
Email the password for the Storage account to the master user.

#### [setMountable](/reference/services/SoftLayer_Network_Storage_Iscsi/setMountable)
Enable or disable mounting of a Storage volume.

#### [setSnapshotAllocation](/reference/services/SoftLayer_Network_Storage_Iscsi/setSnapshotAllocation)


#### [upgradeVolumeCapacity](/reference/services/SoftLayer_Network_Storage_Iscsi/upgradeVolumeCapacity)
Edit the Storage volume to a different package

#### [uploadFile](/reference/services/SoftLayer_Network_Storage_Iscsi/uploadFile)
Upload a file to a Storage account's root directory.

</div>

