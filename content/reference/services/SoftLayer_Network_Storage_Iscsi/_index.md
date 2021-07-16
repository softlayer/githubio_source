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
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [allowAccessFromHardware](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessFromHardware)
Allow access to this volume from a specified SoftLayer_Hardware object.
</div>

<div class="method-row">

#### [allowAccessFromHardwareList](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessFromHardwareList)

</div>

<div class="method-row">

#### [allowAccessFromHost](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessFromHost)
Allow access to this volume from a specified [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) object.
</div>

<div class="method-row">

#### [allowAccessFromHostList](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessFromHostList)
Allow access to this volume from multiple [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) objects.
</div>

<div class="method-row">

#### [allowAccessFromIpAddress](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessFromIpAddress)

</div>

<div class="method-row">

#### [allowAccessFromIpAddressList](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessFromIpAddressList)

</div>

<div class="method-row">

#### [allowAccessFromSubnet](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessFromSubnet)
Allow access to this volume from multiple SoftLayer_Network_Subnet objects.
</div>

<div class="method-row">

#### [allowAccessFromSubnetList](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessFromSubnetList)

</div>

<div class="method-row">

#### [allowAccessFromVirtualGuest](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessFromVirtualGuest)
Allow access to this volume from a specified SoftLayer_Virtual_Guest object.
</div>

<div class="method-row">

#### [allowAccessFromVirtualGuestList](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessFromVirtualGuestList)
Allow access to this volume from multiple SoftLayer_Virtual_Guest objects.
</div>

<div class="method-row">

#### [allowAccessToReplicantFromHardware](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessToReplicantFromHardware)
Allow access to this replicant volume from a specified SoftLayer_Hardware object.
</div>

<div class="method-row">

#### [allowAccessToReplicantFromHardwareList](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessToReplicantFromHardwareList)
allow access to this replica volume from multiple SoftLayer_Hardware objects.
</div>

<div class="method-row">

#### [allowAccessToReplicantFromIpAddress](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessToReplicantFromIpAddress)

</div>

<div class="method-row">

#### [allowAccessToReplicantFromIpAddressList](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessToReplicantFromIpAddressList)
allow access to this volume from multiple SoftLayer_Network_Subnet_IpAddress objects.
</div>

<div class="method-row">

#### [allowAccessToReplicantFromSubnet](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessToReplicantFromSubnet)
Allow access to this replicant volume from multiple SoftLayer_Network_Subnet objects.
</div>

<div class="method-row">

#### [allowAccessToReplicantFromSubnetList](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessToReplicantFromSubnetList)
allow access to this volume's replica from multiple SoftLayer_Network_Subnet objects.
</div>

<div class="method-row">

#### [allowAccessToReplicantFromVirtualGuest](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessToReplicantFromVirtualGuest)
Allow access to this replicant volume from a specified SoftLayer_Virtual_Guest object.
</div>

<div class="method-row">

#### [allowAccessToReplicantFromVirtualGuestList](/reference/services/SoftLayer_Network_Storage_Iscsi/allowAccessToReplicantFromVirtualGuestList)
allow access to this volume from multiple SoftLayer_Virtual_Guest objects.
</div>

<div class="method-row">

#### [assignCredential](/reference/services/SoftLayer_Network_Storage_Iscsi/assignCredential)
This method will assign an existing credential to the current volume.
</div>

<div class="method-row">

#### [assignNewCredential](/reference/services/SoftLayer_Network_Storage_Iscsi/assignNewCredential)
This method will set up a new credential for the remote storage volume.
</div>

<div class="method-row">

#### [changePassword](/reference/services/SoftLayer_Network_Storage_Iscsi/changePassword)
Change the password for a Storage/Virtual Server Storage account
</div>

<div class="method-row">

#### [collectBandwidth](/reference/services/SoftLayer_Network_Storage_Iscsi/collectBandwidth)
Retrieve the bandwidth usage for the current billing cycle.
</div>

<div class="method-row">

#### [collectBytesUsed](/reference/services/SoftLayer_Network_Storage_Iscsi/collectBytesUsed)
Retrieve the number of bytes capacity currently in use on a Storage account.
</div>

<div class="method-row">

#### [convertCloneDependentToIndependent](/reference/services/SoftLayer_Network_Storage_Iscsi/convertCloneDependentToIndependent)
Splits a clone from its parent allowing it to be an independent volume.
</div>

<div class="method-row">

#### [createFolder](/reference/services/SoftLayer_Network_Storage_Iscsi/createFolder)
Create a new folder in the root directory.
</div>

<div class="method-row">

#### [createOrUpdateLunId](/reference/services/SoftLayer_Network_Storage_Iscsi/createOrUpdateLunId)
Creates or updates the LUN ID property on a volume.
</div>

<div class="method-row">

#### [createSnapshot](/reference/services/SoftLayer_Network_Storage_Iscsi/createSnapshot)
Manually create a new snapshot of a storage volume.
</div>

<div class="method-row">

#### [deleteAllFiles](/reference/services/SoftLayer_Network_Storage_Iscsi/deleteAllFiles)
Delete all files within a Storage account.
</div>

<div class="method-row">

#### [deleteFile](/reference/services/SoftLayer_Network_Storage_Iscsi/deleteFile)
Delete an individual file within a Storage account.
</div>

<div class="method-row">

#### [deleteFiles](/reference/services/SoftLayer_Network_Storage_Iscsi/deleteFiles)
Delete multiple files within a Storage account.
</div>

<div class="method-row">

#### [deleteFolder](/reference/services/SoftLayer_Network_Storage_Iscsi/deleteFolder)
Delete a folder in the root directory.
</div>

<div class="method-row">

#### [deleteObject](/reference/services/SoftLayer_Network_Storage_Iscsi/deleteObject)
Delete a network storage volume
</div>

<div class="method-row">

#### [disableSnapshots](/reference/services/SoftLayer_Network_Storage_Iscsi/disableSnapshots)
Disable snapshots of this Storage Volume on a schedule.
</div>

<div class="method-row">

#### [disasterRecoveryFailoverToReplicant](/reference/services/SoftLayer_Network_Storage_Iscsi/disasterRecoveryFailoverToReplicant)
Failover an inaccessible block/file volume to its available replicant volume.
</div>

<div class="method-row">

#### [downloadFile](/reference/services/SoftLayer_Network_Storage_Iscsi/downloadFile)
Download a file from a Storage account.
</div>

<div class="method-row">

#### [editCredential](/reference/services/SoftLayer_Network_Storage_Iscsi/editCredential)
This method will change the password of a credential created using the 'addNewCredential' method.
</div>

<div class="method-row">

#### [editObject](/reference/services/SoftLayer_Network_Storage_Iscsi/editObject)
Edit the password and/or notes for the Storage service
</div>

<div class="method-row">

#### [enableSnapshots](/reference/services/SoftLayer_Network_Storage_Iscsi/enableSnapshots)
Enable snapshots of this Storage Volume on a schedule.
</div>

<div class="method-row">

#### [failbackFromReplicant](/reference/services/SoftLayer_Network_Storage_Iscsi/failbackFromReplicant)
Failback from a volume replicant.
</div>

<div class="method-row">

#### [failoverToReplicant](/reference/services/SoftLayer_Network_Storage_Iscsi/failoverToReplicant)
Failover to a volume replicant.
</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Network_Storage_Iscsi/getAccount)
Retrieve the account that a Storage services belongs to.
</div>

<div class="method-row">

#### [getAccountPassword](/reference/services/SoftLayer_Network_Storage_Iscsi/getAccountPassword)
Retrieve other usernames and passwords associated with a Storage volume.
</div>

<div class="method-row">

#### [getActiveTransactions](/reference/services/SoftLayer_Network_Storage_Iscsi/getActiveTransactions)
Retrieve the currently active transactions on a network storage volume.
</div>

<div class="method-row">

#### [getAllFiles](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllFiles)
Retrieve a listing of all files in a Storage account's root directory.
</div>

<div class="method-row">

#### [getAllFilesByFilter](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllFilesByFilter)
Retrieve a listing of all files matching the filter's criteria in a Storage account's root directory.
</div>

<div class="method-row">

#### [getAllowDisasterRecoveryFailover](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowDisasterRecoveryFailover)

</div>

<div class="method-row">

#### [getAllowableHardware](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowableHardware)
Return a list of SoftLayer_Hardware that can be authorized to this volume. 
</div>

<div class="method-row">

#### [getAllowableIpAddresses](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowableIpAddresses)
Return a list of SoftLayer_Network_Subnet_IpAddress that can be authorized to this volume. 
</div>

<div class="method-row">

#### [getAllowableSubnets](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowableSubnets)
Return a list of SoftLayer_Network_Subnet that can be authorized to this volume. 
</div>

<div class="method-row">

#### [getAllowableVirtualGuests](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowableVirtualGuests)
Return a list of SoftLayer_Virtual_Guest that can be authorized to this volume. 
</div>

<div class="method-row">

#### [getAllowedHardware](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowedHardware)
Retrieve the SoftLayer_Hardware objects which are allowed access to this storage volume.
</div>

<div class="method-row">

#### [getAllowedHostsLimit](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowedHostsLimit)
Retrieves the total number of allowed hosts limit per volume.
</div>

<div class="method-row">

#### [getAllowedIpAddresses](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowedIpAddresses)
Retrieve the SoftLayer_Network_Subnet_IpAddress objects which are allowed access to this storage volume.
</div>

<div class="method-row">

#### [getAllowedReplicationHardware](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowedReplicationHardware)
Retrieve the SoftLayer_Hardware objects which are allowed access to this storage volume's Replicant.
</div>

<div class="method-row">

#### [getAllowedReplicationIpAddresses](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowedReplicationIpAddresses)
Retrieve the SoftLayer_Network_Subnet_IpAddress objects which are allowed access to this storage volume's Replicant.
</div>

<div class="method-row">

#### [getAllowedReplicationSubnets](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowedReplicationSubnets)
Retrieve the SoftLayer_Network_Subnet objects which are allowed access to this storage volume's Replicant.
</div>

<div class="method-row">

#### [getAllowedReplicationVirtualGuests](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowedReplicationVirtualGuests)
Retrieve the SoftLayer_Hardware objects which are allowed access to this storage volume's Replicant.
</div>

<div class="method-row">

#### [getAllowedSubnets](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowedSubnets)
Retrieve the SoftLayer_Network_Subnet objects which are allowed access to this storage volume.
</div>

<div class="method-row">

#### [getAllowedVirtualGuests](/reference/services/SoftLayer_Network_Storage_Iscsi/getAllowedVirtualGuests)
Retrieve the SoftLayer_Virtual_Guest objects which are allowed access to this storage volume.
</div>

<div class="method-row">

#### [getBillingItem](/reference/services/SoftLayer_Network_Storage_Iscsi/getBillingItem)
Retrieve the current billing item for a Storage volume.
</div>

<div class="method-row">

#### [getBillingItemCategory](/reference/services/SoftLayer_Network_Storage_Iscsi/getBillingItemCategory)

</div>

<div class="method-row">

#### [getByUsername](/reference/services/SoftLayer_Network_Storage_Iscsi/getByUsername)
Retrieve network storage accounts by username. 
</div>

<div class="method-row">

#### [getBytesUsed](/reference/services/SoftLayer_Network_Storage_Iscsi/getBytesUsed)
Retrieve the amount of space used by the volume, in bytes.
</div>

<div class="method-row">

#### [getCdnUrls](/reference/services/SoftLayer_Network_Storage_Iscsi/getCdnUrls)

</div>

<div class="method-row">

#### [getClusterResource](/reference/services/SoftLayer_Network_Storage_Iscsi/getClusterResource)

</div>

<div class="method-row">

#### [getCreationScheduleId](/reference/services/SoftLayer_Network_Storage_Iscsi/getCreationScheduleId)
Retrieve the schedule id which was executed to create a snapshot.
</div>

<div class="method-row">

#### [getCredentials](/reference/services/SoftLayer_Network_Storage_Iscsi/getCredentials)

</div>

<div class="method-row">

#### [getDailySchedule](/reference/services/SoftLayer_Network_Storage_Iscsi/getDailySchedule)
Retrieve the Daily Schedule which is associated with this network storage volume.
</div>

<div class="method-row">

#### [getDependentDuplicate](/reference/services/SoftLayer_Network_Storage_Iscsi/getDependentDuplicate)
Retrieve whether or not a network storage volume is a dependent duplicate.
</div>

<div class="method-row">

#### [getDependentDuplicates](/reference/services/SoftLayer_Network_Storage_Iscsi/getDependentDuplicates)
Retrieve the network storage volumes configured to be dependent duplicates of a volume.
</div>

<div class="method-row">

#### [getEvents](/reference/services/SoftLayer_Network_Storage_Iscsi/getEvents)
Retrieve the events which have taken place on a network storage volume.
</div>

<div class="method-row">

#### [getFailbackNotAllowed](/reference/services/SoftLayer_Network_Storage_Iscsi/getFailbackNotAllowed)
Retrieve determines whether the volume is allowed to failback
</div>

<div class="method-row">

#### [getFileBlockEncryptedLocations](/reference/services/SoftLayer_Network_Storage_Iscsi/getFileBlockEncryptedLocations)
Returns a list of SoftLayer_Location_Datacenter objects corresponding to Datacenters in which File and Block Storage Volumes with Encryption at Rest may be ordered. 
</div>

<div class="method-row">

#### [getFileByIdentifier](/reference/services/SoftLayer_Network_Storage_Iscsi/getFileByIdentifier)
Retrieve an individual file's details.
</div>

<div class="method-row">

#### [getFileCount](/reference/services/SoftLayer_Network_Storage_Iscsi/getFileCount)
Retrieve the file number of files in a Virtual Server Storage account's root directory.
</div>

<div class="method-row">

#### [getFileList](/reference/services/SoftLayer_Network_Storage_Iscsi/getFileList)
Retrieve list of files in a given folder for this account.
</div>

<div class="method-row">

#### [getFileNetworkMountAddress](/reference/services/SoftLayer_Network_Storage_Iscsi/getFileNetworkMountAddress)
Retrieve retrieves the NFS Network Mount Address Name for a given File Storage Volume.
</div>

<div class="method-row">

#### [getFilePendingDeleteCount](/reference/services/SoftLayer_Network_Storage_Iscsi/getFilePendingDeleteCount)
Retrieve the number of files pending deletion in a Storage account's recycle bin.
</div>

<div class="method-row">

#### [getFilesPendingDelete](/reference/services/SoftLayer_Network_Storage_Iscsi/getFilesPendingDelete)
Retrieve a list of files in a Storage account's recycle bin.
</div>

<div class="method-row">

#### [getFolderList](/reference/services/SoftLayer_Network_Storage_Iscsi/getFolderList)
Retrieve a list of level 1 folders for this account.
</div>

<div class="method-row">

#### [getGraph](/reference/services/SoftLayer_Network_Storage_Iscsi/getGraph)
Retrieve a graph representing the bandwidth used by a Storage account.
</div>

<div class="method-row">

#### [getHardware](/reference/services/SoftLayer_Network_Storage_Iscsi/getHardware)
Retrieve when applicable, the hardware associated with a Storage service.
</div>

<div class="method-row">

#### [getHasEncryptionAtRest](/reference/services/SoftLayer_Network_Storage_Iscsi/getHasEncryptionAtRest)

</div>

<div class="method-row">

#### [getHourlySchedule](/reference/services/SoftLayer_Network_Storage_Iscsi/getHourlySchedule)
Retrieve the Hourly Schedule which is associated with this network storage volume.
</div>

<div class="method-row">

#### [getIntervalSchedule](/reference/services/SoftLayer_Network_Storage_Iscsi/getIntervalSchedule)
Retrieve the Interval Schedule which is associated with this network storage volume.
</div>

<div class="method-row">

#### [getIops](/reference/services/SoftLayer_Network_Storage_Iscsi/getIops)
Retrieve the maximum number of IOPs guaranteed for this LUN.
</div>

<div class="method-row">

#### [getIsDependentDuplicateProvisionCompleted](/reference/services/SoftLayer_Network_Storage_Iscsi/getIsDependentDuplicateProvisionCompleted)
Retrieve determines whether dependent volume provision is completed on background.
</div>

<div class="method-row">

#### [getIsInDedicatedServiceResource](/reference/services/SoftLayer_Network_Storage_Iscsi/getIsInDedicatedServiceResource)

</div>

<div class="method-row">

#### [getIsReadyForSnapshot](/reference/services/SoftLayer_Network_Storage_Iscsi/getIsReadyForSnapshot)
Retrieve determines whether a volume is ready to order snapshot space, or, if snapshot space is already available, to assign a snapshot schedule, or to take a manual snapshot.
</div>

<div class="method-row">

#### [getIsReadyToMount](/reference/services/SoftLayer_Network_Storage_Iscsi/getIsReadyToMount)
Retrieve determines whether a volume is ready to have Hosts authorized to access it. This does not indicate whether another operation may be blocking, please refer to this volume's volumeStatus property for details.
</div>

<div class="method-row">

#### [getIscsiLuns](/reference/services/SoftLayer_Network_Storage_Iscsi/getIscsiLuns)
Retrieve relationship between a container volume and iSCSI LUNs.
</div>

<div class="method-row">

#### [getIscsiTargetIpAddresses](/reference/services/SoftLayer_Network_Storage_Iscsi/getIscsiTargetIpAddresses)
Retrieve returns the target IP addresses of an iSCSI volume.
</div>

<div class="method-row">

#### [getLunId](/reference/services/SoftLayer_Network_Storage_Iscsi/getLunId)
Retrieve the ID of the LUN volume.
</div>

<div class="method-row">

#### [getManualSnapshots](/reference/services/SoftLayer_Network_Storage_Iscsi/getManualSnapshots)
Retrieve the snapshots associated with this SoftLayer_Network_Storage volume. Does not support pagination by result limit and offset.
</div>

<div class="method-row">

#### [getMaximumExpansionSize](/reference/services/SoftLayer_Network_Storage_Iscsi/getMaximumExpansionSize)
Returns the maximum volume expansion size in GB.
</div>

<div class="method-row">

#### [getMetricTrackingObject](/reference/services/SoftLayer_Network_Storage_Iscsi/getMetricTrackingObject)
Retrieve a network storage volume's metric tracking object. This object records all periodic polled data available to this volume.
</div>

<div class="method-row">

#### [getMountPath](/reference/services/SoftLayer_Network_Storage_Iscsi/getMountPath)
Retrieve retrieves the NFS Network Mount Path for a given File Storage Volume.
</div>

<div class="method-row">

#### [getMountableFlag](/reference/services/SoftLayer_Network_Storage_Iscsi/getMountableFlag)
Retrieve whether or not a network storage volume may be mounted.
</div>

<div class="method-row">

#### [getMoveAndSplitStatus](/reference/services/SoftLayer_Network_Storage_Iscsi/getMoveAndSplitStatus)
Retrieve the current status of split or move operation as a part of volume duplication.
</div>

<div class="method-row">

#### [getNetworkConnectionDetails](/reference/services/SoftLayer_Network_Storage_Iscsi/getNetworkConnectionDetails)
Retrieve network connection details for complex network storage volumes.
</div>

<div class="method-row">

#### [getNetworkMountAddress](/reference/services/SoftLayer_Network_Storage_Iscsi/getNetworkMountAddress)
Displays the mount path of a storage volume.
</div>

<div class="method-row">

#### [getNetworkMountPath](/reference/services/SoftLayer_Network_Storage_Iscsi/getNetworkMountPath)
Displays the mount path of a storage volume.
</div>

<div class="method-row">

#### [getNotificationSubscribers](/reference/services/SoftLayer_Network_Storage_Iscsi/getNotificationSubscribers)
Retrieve the subscribers that will be notified for usage amount warnings and overages.
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_Storage_Iscsi/getObject)
Retrieve a SoftLayer_Network_Storage_Iscsi record.
</div>

<div class="method-row">

#### [getObjectStorageConnectionInformation](/reference/services/SoftLayer_Network_Storage_Iscsi/getObjectStorageConnectionInformation)
Retrieve all object storage details for connection
</div>

<div class="method-row">

#### [getObjectsByCredential](/reference/services/SoftLayer_Network_Storage_Iscsi/getObjectsByCredential)
Retrieve network storage accounts by SoftLayer_Network_Storage_Credential object. 
</div>

<div class="method-row">

#### [getOriginalSnapshotName](/reference/services/SoftLayer_Network_Storage_Iscsi/getOriginalSnapshotName)
Retrieve the name of the snapshot that this volume was duplicated from.
</div>

<div class="method-row">

#### [getOriginalVolumeName](/reference/services/SoftLayer_Network_Storage_Iscsi/getOriginalVolumeName)
Retrieve the name of the volume that this volume was duplicated from.
</div>

<div class="method-row">

#### [getOriginalVolumeSize](/reference/services/SoftLayer_Network_Storage_Iscsi/getOriginalVolumeSize)
Retrieve the size (in GB) of the volume or LUN before any size expansion, or of the volume (before any possible size expansion) from which the duplicate volume or LUN was created.
</div>

<div class="method-row">

#### [getOsType](/reference/services/SoftLayer_Network_Storage_Iscsi/getOsType)
Retrieve a volume's configured SoftLayer_Network_Storage_Iscsi_OS_Type.
</div>

<div class="method-row">

#### [getOsTypeId](/reference/services/SoftLayer_Network_Storage_Iscsi/getOsTypeId)
Retrieve a volume's configured SoftLayer_Network_Storage_Iscsi_OS_Type ID.
</div>

<div class="method-row">

#### [getParentPartnerships](/reference/services/SoftLayer_Network_Storage_Iscsi/getParentPartnerships)
Retrieve the volumes or snapshots partnered with a network storage volume in a parental role.
</div>

<div class="method-row">

#### [getParentVolume](/reference/services/SoftLayer_Network_Storage_Iscsi/getParentVolume)
Retrieve the volume on which this iSCSI LUN is provisioned.
</div>

<div class="method-row">

#### [getPartnerships](/reference/services/SoftLayer_Network_Storage_Iscsi/getPartnerships)
Retrieve the volumes or snapshots partnered with a network storage volume.
</div>

<div class="method-row">

#### [getPermissionsGroups](/reference/services/SoftLayer_Network_Storage_Iscsi/getPermissionsGroups)
Retrieve all permissions group(s) this volume is in.
</div>

<div class="method-row">

#### [getProperties](/reference/services/SoftLayer_Network_Storage_Iscsi/getProperties)
Retrieve the properties used to provide additional details about a network storage volume.
</div>

<div class="method-row">

#### [getProvisionedIops](/reference/services/SoftLayer_Network_Storage_Iscsi/getProvisionedIops)
Retrieve the number of IOPs provisioned for this volume.
</div>

<div class="method-row">

#### [getRecycleBinFileByIdentifier](/reference/services/SoftLayer_Network_Storage_Iscsi/getRecycleBinFileByIdentifier)
Retrieve all files that are in the recycle bin (pending delete).  This method is only used for Virtual Server Storage accounts at moment but may expanded to other Storage types in the future.
</div>

<div class="method-row">

#### [getRemainingAllowedHosts](/reference/services/SoftLayer_Network_Storage_Iscsi/getRemainingAllowedHosts)
Retrieves the remaining number of allowed hosts per volume.
</div>

<div class="method-row">

#### [getRemainingAllowedHostsForReplicant](/reference/services/SoftLayer_Network_Storage_Iscsi/getRemainingAllowedHostsForReplicant)
Retrieves the remaining number of allowed hosts for a volume's replicant.
</div>

<div class="method-row">

#### [getReplicatingLuns](/reference/services/SoftLayer_Network_Storage_Iscsi/getReplicatingLuns)
Retrieve the iSCSI LUN volumes being replicated by this network storage volume.
</div>

<div class="method-row">

#### [getReplicatingVolume](/reference/services/SoftLayer_Network_Storage_Iscsi/getReplicatingVolume)
Retrieve the network storage volume being replicated by a volume.
</div>

<div class="method-row">

#### [getReplicationEvents](/reference/services/SoftLayer_Network_Storage_Iscsi/getReplicationEvents)
Retrieve the volume replication events.
</div>

<div class="method-row">

#### [getReplicationPartners](/reference/services/SoftLayer_Network_Storage_Iscsi/getReplicationPartners)
Retrieve the network storage volumes configured to be replicants of a volume.
</div>

<div class="method-row">

#### [getReplicationSchedule](/reference/services/SoftLayer_Network_Storage_Iscsi/getReplicationSchedule)
Retrieve the Replication Schedule associated with a network storage volume.
</div>

<div class="method-row">

#### [getReplicationStatus](/reference/services/SoftLayer_Network_Storage_Iscsi/getReplicationStatus)
Retrieve the current replication status of a network storage volume. Indicates Failover or Failback status.
</div>

<div class="method-row">

#### [getReplicationTimestamp](/reference/services/SoftLayer_Network_Storage_Iscsi/getReplicationTimestamp)
An API call to fetch the last timestamp of the replication process
</div>

<div class="method-row">

#### [getSchedules](/reference/services/SoftLayer_Network_Storage_Iscsi/getSchedules)
Retrieve the schedules which are associated with a network storage volume.
</div>

<div class="method-row">

#### [getServiceResource](/reference/services/SoftLayer_Network_Storage_Iscsi/getServiceResource)
Retrieve the network resource a Storage service is connected to.
</div>

<div class="method-row">

#### [getServiceResourceBackendIpAddress](/reference/services/SoftLayer_Network_Storage_Iscsi/getServiceResourceBackendIpAddress)
Retrieve the IP address of a Storage resource.
</div>

<div class="method-row">

#### [getServiceResourceName](/reference/services/SoftLayer_Network_Storage_Iscsi/getServiceResourceName)
Retrieve the name of a Storage's network resource.
</div>

<div class="method-row">

#### [getSnapshotCapacityGb](/reference/services/SoftLayer_Network_Storage_Iscsi/getSnapshotCapacityGb)
Retrieve a volume's configured snapshot space size.
</div>

<div class="method-row">

#### [getSnapshotCreationTimestamp](/reference/services/SoftLayer_Network_Storage_Iscsi/getSnapshotCreationTimestamp)
Retrieve the creation timestamp of the snapshot on the storage platform.
</div>

<div class="method-row">

#### [getSnapshotDeletionThresholdPercentage](/reference/services/SoftLayer_Network_Storage_Iscsi/getSnapshotDeletionThresholdPercentage)
Retrieve the percentage of used snapshot space after which to delete automated snapshots.
</div>

<div class="method-row">

#### [getSnapshotSizeBytes](/reference/services/SoftLayer_Network_Storage_Iscsi/getSnapshotSizeBytes)
Retrieve the snapshot size in bytes.
</div>

<div class="method-row">

#### [getSnapshotSpaceAvailable](/reference/services/SoftLayer_Network_Storage_Iscsi/getSnapshotSpaceAvailable)
Retrieve an volume's available snapshot reservation space.
</div>

<div class="method-row">

#### [getSnapshots](/reference/services/SoftLayer_Network_Storage_Iscsi/getSnapshots)
Retrieve the snapshots associated with this iSCSI LUN's container volume, if applicable
</div>

<div class="method-row">

#### [getSnapshotsForVolume](/reference/services/SoftLayer_Network_Storage_Iscsi/getSnapshotsForVolume)
Retrieves a list of snapshots for a given volume.
</div>

<div class="method-row">

#### [getStaasVersion](/reference/services/SoftLayer_Network_Storage_Iscsi/getStaasVersion)

</div>

<div class="method-row">

#### [getStorageGroups](/reference/services/SoftLayer_Network_Storage_Iscsi/getStorageGroups)
Retrieve the network storage groups this volume is attached to.
</div>

<div class="method-row">

#### [getStorageGroupsNetworkConnectionDetails](/reference/services/SoftLayer_Network_Storage_Iscsi/getStorageGroupsNetworkConnectionDetails)

</div>

<div class="method-row">

#### [getStorageTierLevel](/reference/services/SoftLayer_Network_Storage_Iscsi/getStorageTierLevel)

</div>

<div class="method-row">

#### [getStorageType](/reference/services/SoftLayer_Network_Storage_Iscsi/getStorageType)
Retrieve a description of the Storage object.
</div>

<div class="method-row">

#### [getTargetIpAddresses](/reference/services/SoftLayer_Network_Storage_Iscsi/getTargetIpAddresses)

</div>

<div class="method-row">

#### [getTotalBytesUsed](/reference/services/SoftLayer_Network_Storage_Iscsi/getTotalBytesUsed)
Retrieve the amount of space used by the volume.
</div>

<div class="method-row">

#### [getTotalScheduleSnapshotRetentionCount](/reference/services/SoftLayer_Network_Storage_Iscsi/getTotalScheduleSnapshotRetentionCount)
Retrieve the total snapshot retention count of all schedules on this network storage volume.
</div>

<div class="method-row">

#### [getUsageNotification](/reference/services/SoftLayer_Network_Storage_Iscsi/getUsageNotification)
Retrieve the usage notification for SL Storage services.
</div>

<div class="method-row">

#### [getValidReplicationTargetDatacenterLocations](/reference/services/SoftLayer_Network_Storage_Iscsi/getValidReplicationTargetDatacenterLocations)

</div>

<div class="method-row">

#### [getVendorName](/reference/services/SoftLayer_Network_Storage_Iscsi/getVendorName)
Retrieve the type of network storage service.
</div>

<div class="method-row">

#### [getVirtualGuest](/reference/services/SoftLayer_Network_Storage_Iscsi/getVirtualGuest)
Retrieve when applicable, the virtual guest associated with a Storage service.
</div>

<div class="method-row">

#### [getVolumeCountLimits](/reference/services/SoftLayer_Network_Storage_Iscsi/getVolumeCountLimits)
Retrieves an array of volume count limits per location and globally.
</div>

<div class="method-row">

#### [getVolumeDuplicateParameters](/reference/services/SoftLayer_Network_Storage_Iscsi/getVolumeDuplicateParameters)

</div>

<div class="method-row">

#### [getVolumeHistory](/reference/services/SoftLayer_Network_Storage_Iscsi/getVolumeHistory)
Retrieve the username and password history for a Storage service.
</div>

<div class="method-row">

#### [getVolumeStatus](/reference/services/SoftLayer_Network_Storage_Iscsi/getVolumeStatus)
Retrieve the current status of a network storage volume.
</div>

<div class="method-row">

#### [getWebccAccount](/reference/services/SoftLayer_Network_Storage_Iscsi/getWebccAccount)
Retrieve the account username and password for the EVault webCC interface.
</div>

<div class="method-row">

#### [getWeeklySchedule](/reference/services/SoftLayer_Network_Storage_Iscsi/getWeeklySchedule)
Retrieve the Weekly Schedule which is associated with this network storage volume.
</div>

<div class="method-row">

#### [immediateFailoverToReplicant](/reference/services/SoftLayer_Network_Storage_Iscsi/immediateFailoverToReplicant)
Immediate Failover to a volume replicant.
</div>

<div class="method-row">

#### [initiateOriginVolumeReclaim](/reference/services/SoftLayer_Network_Storage_Iscsi/initiateOriginVolumeReclaim)
Initiates Origin Volume Reclaim to delete volume from NetApp.
</div>

<div class="method-row">

#### [initiateVolumeCutover](/reference/services/SoftLayer_Network_Storage_Iscsi/initiateVolumeCutover)
Initiates Volume Cutover to remove access from the old volume.
</div>

<div class="method-row">

#### [isBlockingOperationInProgress](/reference/services/SoftLayer_Network_Storage_Iscsi/isBlockingOperationInProgress)

</div>

<div class="method-row">

#### [isDuplicateReadyForSnapshot](/reference/services/SoftLayer_Network_Storage_Iscsi/isDuplicateReadyForSnapshot)
Displays the if clone snapshots can be ordered.
</div>

<div class="method-row">

#### [isDuplicateReadyToMount](/reference/services/SoftLayer_Network_Storage_Iscsi/isDuplicateReadyToMount)
Displays the status of a clone mount.
</div>

<div class="method-row">

#### [isVolumeActive](/reference/services/SoftLayer_Network_Storage_Iscsi/isVolumeActive)

</div>

<div class="method-row">

#### [refreshDependentDuplicate](/reference/services/SoftLayer_Network_Storage_Iscsi/refreshDependentDuplicate)
Refreshes a duplicate volume with a snapshot taken from its parent. This is deprecated now.
</div>

<div class="method-row">

#### [refreshDuplicate](/reference/services/SoftLayer_Network_Storage_Iscsi/refreshDuplicate)
Refreshes any duplicate volume with a snapshot taken from its parent.
</div>

<div class="method-row">

#### [removeAccessFromHardware](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessFromHardware)
Remove access to this volume from a specified SoftLayer_Hardware object.
</div>

<div class="method-row">

#### [removeAccessFromHardwareList](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessFromHardwareList)
Remove access to this volume from multiple SoftLayer_Hardware objects.
</div>

<div class="method-row">

#### [removeAccessFromHost](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessFromHost)
Remove access to this volume from a specified [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) object.
</div>

<div class="method-row">

#### [removeAccessFromHostList](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessFromHostList)
Remove access to this volume from multiple [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) objects.
</div>

<div class="method-row">

#### [removeAccessFromIpAddress](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessFromIpAddress)

</div>

<div class="method-row">

#### [removeAccessFromIpAddressList](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessFromIpAddressList)

</div>

<div class="method-row">

#### [removeAccessFromSubnet](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessFromSubnet)

</div>

<div class="method-row">

#### [removeAccessFromSubnetList](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessFromSubnetList)

</div>

<div class="method-row">

#### [removeAccessFromVirtualGuest](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessFromVirtualGuest)
Remove access to this volume from a specified SoftLayer_Virtual_Guest object.
</div>

<div class="method-row">

#### [removeAccessFromVirtualGuestList](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessFromVirtualGuestList)
Remove access to this volume from multiple SoftLayer_Virtual_Guest objects.
</div>

<div class="method-row">

#### [removeAccessToReplicantFromHardwareList](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessToReplicantFromHardwareList)
Remove access to this volume from multiple SoftLayer_Hardware objects.
</div>

<div class="method-row">

#### [removeAccessToReplicantFromIpAddressList](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessToReplicantFromIpAddressList)
Remove access to this replica volume from multiple SoftLayer_Network_Subnet_IpAddress objects.
</div>

<div class="method-row">

#### [removeAccessToReplicantFromSubnet](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessToReplicantFromSubnet)

</div>

<div class="method-row">

#### [removeAccessToReplicantFromSubnetList](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessToReplicantFromSubnetList)
Remove access to this volume's replica from multiple SoftLayer_Network_Subnet objects.
</div>

<div class="method-row">

#### [removeAccessToReplicantFromVirtualGuestList](/reference/services/SoftLayer_Network_Storage_Iscsi/removeAccessToReplicantFromVirtualGuestList)
Remove access to this replica volume from multiple SoftLayer_Virtual_Guest objects.
</div>

<div class="method-row">

#### [removeCredential](/reference/services/SoftLayer_Network_Storage_Iscsi/removeCredential)
This method will remove a credential from the current volume.
</div>

<div class="method-row">

#### [restoreFile](/reference/services/SoftLayer_Network_Storage_Iscsi/restoreFile)
Restore access to an individual file in a Storage account.
</div>

<div class="method-row">

#### [restoreFromSnapshot](/reference/services/SoftLayer_Network_Storage_Iscsi/restoreFromSnapshot)
Restore from a volume snapshot.
</div>

<div class="method-row">

#### [sendPasswordReminderEmail](/reference/services/SoftLayer_Network_Storage_Iscsi/sendPasswordReminderEmail)
Email the password for the Storage account to the master user.
</div>

<div class="method-row">

#### [setMountable](/reference/services/SoftLayer_Network_Storage_Iscsi/setMountable)
Enable or disable mounting of a Storage volume.
</div>

<div class="method-row">

#### [setSnapshotAllocation](/reference/services/SoftLayer_Network_Storage_Iscsi/setSnapshotAllocation)

</div>

<div class="method-row">

#### [upgradeVolumeCapacity](/reference/services/SoftLayer_Network_Storage_Iscsi/upgradeVolumeCapacity)
Edit the Storage volume to a different package
</div>

<div class="method-row">

#### [uploadFile](/reference/services/SoftLayer_Network_Storage_Iscsi/uploadFile)
Upload a file to a Storage account's root directory.
</div>
</div>

</div>

