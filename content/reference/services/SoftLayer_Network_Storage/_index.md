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

For the EVault Storage services, the username and passwords in the SoftLayer_Network_Storage services are used to register the EVault server agent with the vault. Please see the [[SoftLayer_Account_Password]] service to edit the passwords and notes for the EVault Webcc tool. 



### seeAlso

* [SoftLayer_Network_Storage_Nas](/reference/datatypes/SoftLayer_Network_Storage_Nas )


* [SoftLayer_Network_Storage_Iscsi](/reference/services/SoftLayer_Network_Storage_Iscsi )


* [SoftLayer_Network_Storage_Hub](/reference/datatypes/SoftLayer_Network_Storage_Hub )


* [SoftLayer_Network_Storage_Backup_Evault](/reference/services/SoftLayer_Network_Storage_Backup_Evault )


        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/allowAccessFromHardware'> allowAccessFromHardware</a> </span>
            <div class='views-field-body'>Allow access to this volume from a specified SoftLayer_Hardware object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/allowAccessFromHardwareList'> allowAccessFromHardwareList</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/allowAccessFromHost'> allowAccessFromHost</a> </span>
            <div class='views-field-body'>Allow access to this volume from a specified [[SoftLayer_Hardware|SoftLayer_Virtual_Guest|SoftLayer_Network_Subnet|SoftLayer_Network_Subnet_IpAddress]] object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/allowAccessFromHostList'> allowAccessFromHostList</a> </span>
            <div class='views-field-body'>Allow access to this volume from multiple [[SoftLayer_Hardware|SoftLayer_Virtual_Guest|SoftLayer_Network_Subnet|SoftLayer_Network_Subnet_IpAddress]] objects.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/allowAccessFromIpAddress'> allowAccessFromIpAddress</a> </span>
            <div class='views-field-body'>Allow access to this volume from a specified SoftLayer_Network_Subnet_IpAddress object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/allowAccessFromIpAddressList'> allowAccessFromIpAddressList</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/allowAccessFromSubnet'> allowAccessFromSubnet</a> </span>
            <div class='views-field-body'>Allow access to this volume from multiple SoftLayer_Network_Subnet objects.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/allowAccessFromSubnetList'> allowAccessFromSubnetList</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/allowAccessFromVirtualGuest'> allowAccessFromVirtualGuest</a> </span>
            <div class='views-field-body'>Allow access to this volume from a specified SoftLayer_Virtual_Guest object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/allowAccessFromVirtualGuestList'> allowAccessFromVirtualGuestList</a> </span>
            <div class='views-field-body'>Allow access to this volume from multiple SoftLayer_Virtual_Guest objects.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/allowAccessToReplicantFromHardware'> allowAccessToReplicantFromHardware</a> </span>
            <div class='views-field-body'>Allow access to this replicant volume from a specified SoftLayer_Hardware object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/allowAccessToReplicantFromHardwareList'> allowAccessToReplicantFromHardwareList</a> </span>
            <div class='views-field-body'>allow access to this volume's replica from multiple SoftLayer_Hardware objects.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/allowAccessToReplicantFromIpAddress'> allowAccessToReplicantFromIpAddress</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/allowAccessToReplicantFromIpAddressList'> allowAccessToReplicantFromIpAddressList</a> </span>
            <div class='views-field-body'>allow access to this volume's replica from multiple SoftLayer_Network_Subnet_IpAddress objects.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/allowAccessToReplicantFromSubnet'> allowAccessToReplicantFromSubnet</a> </span>
            <div class='views-field-body'>Allow access to this replicant volume from multiple SoftLayer_Network_Subnet objects.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/allowAccessToReplicantFromSubnetList'> allowAccessToReplicantFromSubnetList</a> </span>
            <div class='views-field-body'>allow access to this volume's replica from multiple SoftLayer_Network_Subnet objects.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/allowAccessToReplicantFromVirtualGuest'> allowAccessToReplicantFromVirtualGuest</a> </span>
            <div class='views-field-body'>Allow access to this replicant volume from a specified SoftLayer_Virtual_Guest object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/allowAccessToReplicantFromVirtualGuestList'> allowAccessToReplicantFromVirtualGuestList</a> </span>
            <div class='views-field-body'>allow access to this volume's replica from multiple SoftLayer_Virtual_Guest objects.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/assignCredential'> assignCredential</a> </span>
            <div class='views-field-body'>This method will assign an existing credential to the current volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/assignNewCredential'> assignNewCredential</a> </span>
            <div class='views-field-body'>This method will set up a new credential for the remote storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/changePassword'> changePassword</a> </span>
            <div class='views-field-body'>Change the password for a Storage/Virtual Server Storage account</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/collectBandwidth'> collectBandwidth</a> </span>
            <div class='views-field-body'>Retrieve the bandwidth usage for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/collectBytesUsed'> collectBytesUsed</a> </span>
            <div class='views-field-body'>Retrieve the number of bytes capacity currently in use on a Storage account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/createFolder'> createFolder</a> </span>
            <div class='views-field-body'>Create a new folder in the root directory.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/createOrUpdateLunId'> createOrUpdateLunId</a> </span>
            <div class='views-field-body'>Creates or updates the LUN ID property on a volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/createSnapshot'> createSnapshot</a> </span>
            <div class='views-field-body'>Manually create a new snapshot of a storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/deleteAllFiles'> deleteAllFiles</a> </span>
            <div class='views-field-body'>Delete all files within a Storage account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/deleteFile'> deleteFile</a> </span>
            <div class='views-field-body'>Delete an individual file within a Storage account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/deleteFiles'> deleteFiles</a> </span>
            <div class='views-field-body'>Delete multiple files within a Storage account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/deleteFolder'> deleteFolder</a> </span>
            <div class='views-field-body'>Delete a folder in the root directory.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/deleteObject'> deleteObject</a> </span>
            <div class='views-field-body'>Delete a network storage volume</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/disableSnapshots'> disableSnapshots</a> </span>
            <div class='views-field-body'>Disable snapshots of this Storage Volume on a schedule.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/downloadFile'> downloadFile</a> </span>
            <div class='views-field-body'>Download a file from a Storage account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/editCredential'> editCredential</a> </span>
            <div class='views-field-body'>This method will change the password of a credential created using the 'addNewCredential' method.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit the password and/or notes for the Storage service</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/enableSnapshots'> enableSnapshots</a> </span>
            <div class='views-field-body'>Enable snapshots of this Storage Volume on a schedule.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/failbackFromReplicant'> failbackFromReplicant</a> </span>
            <div class='views-field-body'>Failback from a volume replicant.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/failoverToReplicant'> failoverToReplicant</a> </span>
            <div class='views-field-body'>Failover to a volume replicant.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the account that a Storage services belongs to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getAccountPassword'> getAccountPassword</a> </span>
            <div class='views-field-body'>Retrieve other usernames and passwords associated with a Storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getActiveTransactions'> getActiveTransactions</a> </span>
            <div class='views-field-body'>Retrieve the currently active transactions on a network storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getAllFiles'> getAllFiles</a> </span>
            <div class='views-field-body'>Retrieve a listing of all files in a Storage account's root directory.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getAllFilesByFilter'> getAllFilesByFilter</a> </span>
            <div class='views-field-body'>Retrieve a listing of all files matching the filter's criteria in a Storage account's root directory.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getAllowableHardware'> getAllowableHardware</a> </span>
            <div class='views-field-body'>Return a list of SoftLayer_Hardware that can be authorized to this volume. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getAllowableIpAddresses'> getAllowableIpAddresses</a> </span>
            <div class='views-field-body'>Return a list of SoftLayer_Network_Subnet_IpAddress that can be authorized to this volume. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getAllowableSubnets'> getAllowableSubnets</a> </span>
            <div class='views-field-body'>Return a list of SoftLayer_Network_Subnet that can be authorized to this volume. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getAllowableVirtualGuests'> getAllowableVirtualGuests</a> </span>
            <div class='views-field-body'>Return a list of SoftLayer_Virtual_Guest that can be authorized to this volume. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getAllowedHardware'> getAllowedHardware</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer_Hardware objects which are allowed access to this storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getAllowedHostsLimit'> getAllowedHostsLimit</a> </span>
            <div class='views-field-body'>Retrieves the total number of allowed hosts limit per volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getAllowedIpAddresses'> getAllowedIpAddresses</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer_Network_Subnet_IpAddress objects which are allowed access to this storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getAllowedReplicationHardware'> getAllowedReplicationHardware</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer_Hardware objects which are allowed access to this storage volume's Replicant.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getAllowedReplicationIpAddresses'> getAllowedReplicationIpAddresses</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer_Network_Subnet_IpAddress objects which are allowed access to this storage volume's Replicant.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getAllowedReplicationSubnets'> getAllowedReplicationSubnets</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer_Network_Subnet objects which are allowed access to this storage volume's Replicant.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getAllowedReplicationVirtualGuests'> getAllowedReplicationVirtualGuests</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer_Hardware objects which are allowed access to this storage volume's Replicant.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getAllowedSubnets'> getAllowedSubnets</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer_Network_Subnet objects which are allowed access to this storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getAllowedVirtualGuests'> getAllowedVirtualGuests</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer_Virtual_Guest objects which are allowed access to this storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getBillingItem'> getBillingItem</a> </span>
            <div class='views-field-body'>Retrieve the current billing item for a Storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getBillingItemCategory'> getBillingItemCategory</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getByUsername'> getByUsername</a> </span>
            <div class='views-field-body'>Retrieve network storage accounts by username. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getBytesUsed'> getBytesUsed</a> </span>
            <div class='views-field-body'>Retrieve the amount of space used by the volume, in bytes.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getCdnUrls'> getCdnUrls</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getClusterResource'> getClusterResource</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getCreationScheduleId'> getCreationScheduleId</a> </span>
            <div class='views-field-body'>Retrieve the schedule id which was executed to create a snapshot.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getCredentials'> getCredentials</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getDailySchedule'> getDailySchedule</a> </span>
            <div class='views-field-body'>Retrieve the Daily Schedule which is associated with this network storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getEvents'> getEvents</a> </span>
            <div class='views-field-body'>Retrieve the events which have taken place on a network storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getFileBlockEncryptedLocations'> getFileBlockEncryptedLocations</a> </span>
            <div class='views-field-body'>Returns a list of SoftLayer_Location_Datacenter objects corresponding to Datacenters in which File and Block Storage Volumes with Encryption at Rest may be ordered. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getFileByIdentifier'> getFileByIdentifier</a> </span>
            <div class='views-field-body'>Retrieve an individual file's details.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getFileCount'> getFileCount</a> </span>
            <div class='views-field-body'>Retrieve the file number of files in a Virtual Server Storage account's root directory.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getFileList'> getFileList</a> </span>
            <div class='views-field-body'>Retrieve list of files in a given folder for this account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getFileNetworkMountAddress'> getFileNetworkMountAddress</a> </span>
            <div class='views-field-body'>Retrieve retrieves the NFS Network Mount Address Name for a given File Storage Volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getFilePendingDeleteCount'> getFilePendingDeleteCount</a> </span>
            <div class='views-field-body'>Retrieve the number of files pending deletion in a Storage account's recycle bin.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getFilesPendingDelete'> getFilesPendingDelete</a> </span>
            <div class='views-field-body'>Retrieve a list of files in a Storage account's recycle bin.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getFolderList'> getFolderList</a> </span>
            <div class='views-field-body'>Retrieve a list of level 1 folders for this account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getGraph'> getGraph</a> </span>
            <div class='views-field-body'>Retrieve a graph representing the bandwidth used by a Storage account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getHardware'> getHardware</a> </span>
            <div class='views-field-body'>Retrieve when applicable, the hardware associated with a Storage service.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getHasEncryptionAtRest'> getHasEncryptionAtRest</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getHourlySchedule'> getHourlySchedule</a> </span>
            <div class='views-field-body'>Retrieve the Hourly Schedule which is associated with this network storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getIntervalSchedule'> getIntervalSchedule</a> </span>
            <div class='views-field-body'>Retrieve the Interval Schedule which is associated with this network storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getIops'> getIops</a> </span>
            <div class='views-field-body'>Retrieve the maximum number of IOPs selected for this volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getIsReadyForSnapshot'> getIsReadyForSnapshot</a> </span>
            <div class='views-field-body'>Retrieve determines whether a volume is ready to order snapshot space, or, if snapshot space is already available, to assign a snapshot schedule, or to take a manual snapshot.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getIsReadyToMount'> getIsReadyToMount</a> </span>
            <div class='views-field-body'>Retrieve determines whether a volume is ready to have Hosts authorized to access it. This does not indicate whether another operation may be blocking, please refer to this volume's volumeStatus property for details.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getIscsiLuns'> getIscsiLuns</a> </span>
            <div class='views-field-body'>Retrieve relationship between a container volume and iSCSI LUNs.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getIscsiTargetIpAddresses'> getIscsiTargetIpAddresses</a> </span>
            <div class='views-field-body'>Retrieve returns the target IP addresses of an iSCSI volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getLunId'> getLunId</a> </span>
            <div class='views-field-body'>Retrieve the ID of the LUN volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getManualSnapshots'> getManualSnapshots</a> </span>
            <div class='views-field-body'>Retrieve the manually-created snapshots associated with this SoftLayer_Network_Storage volume. Does not support pagination by result limit and offset.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getMaximumExpansionSize'> getMaximumExpansionSize</a> </span>
            <div class='views-field-body'>Returns the maximum volume expansion size in GB.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getMetricTrackingObject'> getMetricTrackingObject</a> </span>
            <div class='views-field-body'>Retrieve a network storage volume's metric tracking object. This object records all periodic polled data available to this volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getMountableFlag'> getMountableFlag</a> </span>
            <div class='views-field-body'>Retrieve whether or not a network storage volume may be mounted.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getMoveAndSplitStatus'> getMoveAndSplitStatus</a> </span>
            <div class='views-field-body'>Retrieve the current status of split or move operation as a part of volume duplication.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getNetworkConnectionDetails'> getNetworkConnectionDetails</a> </span>
            <div class='views-field-body'>Retrieve network connection details for complex network storage volumes.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getNetworkMountAddress'> getNetworkMountAddress</a> </span>
            <div class='views-field-body'>Displays the mount path of a storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getNotificationSubscribers'> getNotificationSubscribers</a> </span>
            <div class='views-field-body'>Retrieve the subscribers that will be notified for usage amount warnings and overages.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_Storage record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getObjectStorageConnectionInformation'> getObjectStorageConnectionInformation</a> </span>
            <div class='views-field-body'>Retrieve all object storage details for connection</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getObjectsByCredential'> getObjectsByCredential</a> </span>
            <div class='views-field-body'>Retrieve network storage accounts by SoftLayer_Network_Storage_Credential object. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getOriginalSnapshotName'> getOriginalSnapshotName</a> </span>
            <div class='views-field-body'>Retrieve the name of the snapshot that this volume was duplicated from.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getOriginalVolumeName'> getOriginalVolumeName</a> </span>
            <div class='views-field-body'>Retrieve the name of the volume that this volume was duplicated from.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getOriginalVolumeSize'> getOriginalVolumeSize</a> </span>
            <div class='views-field-body'>Retrieve the size (in GB) of the volume or LUN before any size expansion, or of the volume (before any possible size expansion) from which the duplicate volume or LUN was created.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getOsType'> getOsType</a> </span>
            <div class='views-field-body'>Retrieve a volume's configured SoftLayer_Network_Storage_Iscsi_OS_Type.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getOsTypeId'> getOsTypeId</a> </span>
            <div class='views-field-body'>Retrieve a volume's configured SoftLayer_Network_Storage_Iscsi_OS_Type ID.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getParentPartnerships'> getParentPartnerships</a> </span>
            <div class='views-field-body'>Retrieve the volumes or snapshots partnered with a network storage volume in a parental role.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getParentVolume'> getParentVolume</a> </span>
            <div class='views-field-body'>Retrieve the parent volume of a volume in a complex storage relationship.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getPartnerships'> getPartnerships</a> </span>
            <div class='views-field-body'>Retrieve the volumes or snapshots partnered with a network storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getPermissionsGroups'> getPermissionsGroups</a> </span>
            <div class='views-field-body'>Retrieve all permissions group(s) this volume is in.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getProperties'> getProperties</a> </span>
            <div class='views-field-body'>Retrieve the properties used to provide additional details about a network storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getProvisionedIops'> getProvisionedIops</a> </span>
            <div class='views-field-body'>Retrieve the number of IOPs provisioned for this volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getRecycleBinFileByIdentifier'> getRecycleBinFileByIdentifier</a> </span>
            <div class='views-field-body'>Retrieve all files that are in the recycle bin (pending delete).  This method is only used for Virtual Server Storage accounts at moment but may expanded to other Storage types in the future.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getRemainingAllowedHosts'> getRemainingAllowedHosts</a> </span>
            <div class='views-field-body'>Retrieves the remaining number of allowed hosts per volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getRemainingAllowedHostsForReplicant'> getRemainingAllowedHostsForReplicant</a> </span>
            <div class='views-field-body'>Retrieves the remaining number of allowed hosts for a volume's replicant.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getReplicatingLuns'> getReplicatingLuns</a> </span>
            <div class='views-field-body'>Retrieve the iSCSI LUN volumes being replicated by this network storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getReplicatingVolume'> getReplicatingVolume</a> </span>
            <div class='views-field-body'>Retrieve the network storage volume being replicated by a volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getReplicationEvents'> getReplicationEvents</a> </span>
            <div class='views-field-body'>Retrieve the volume replication events.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getReplicationPartners'> getReplicationPartners</a> </span>
            <div class='views-field-body'>Retrieve the network storage volumes configured to be replicants of a volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getReplicationSchedule'> getReplicationSchedule</a> </span>
            <div class='views-field-body'>Retrieve the Replication Schedule associated with a network storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getReplicationStatus'> getReplicationStatus</a> </span>
            <div class='views-field-body'>Retrieve the current replication status of a network storage volume. Indicates Failover or Failback status.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getSchedules'> getSchedules</a> </span>
            <div class='views-field-body'>Retrieve the schedules which are associated with a network storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getServiceResource'> getServiceResource</a> </span>
            <div class='views-field-body'>Retrieve the network resource a Storage service is connected to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getServiceResourceBackendIpAddress'> getServiceResourceBackendIpAddress</a> </span>
            <div class='views-field-body'>Retrieve the IP address of a Storage resource.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getServiceResourceName'> getServiceResourceName</a> </span>
            <div class='views-field-body'>Retrieve the name of a Storage's network resource.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getSnapshotCapacityGb'> getSnapshotCapacityGb</a> </span>
            <div class='views-field-body'>Retrieve a volume's configured snapshot space size.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getSnapshotCreationTimestamp'> getSnapshotCreationTimestamp</a> </span>
            <div class='views-field-body'>Retrieve the creation timestamp of the snapshot on the storage platform.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getSnapshotDeletionThresholdPercentage'> getSnapshotDeletionThresholdPercentage</a> </span>
            <div class='views-field-body'>Retrieve the percentage of used snapshot space after which to delete automated snapshots.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getSnapshotSizeBytes'> getSnapshotSizeBytes</a> </span>
            <div class='views-field-body'>Retrieve the snapshot size in bytes.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getSnapshotSpaceAvailable'> getSnapshotSpaceAvailable</a> </span>
            <div class='views-field-body'>Retrieve a volume's available snapshot reservation space.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getSnapshots'> getSnapshots</a> </span>
            <div class='views-field-body'>Retrieve the snapshots associated with this SoftLayer_Network_Storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getSnapshotsForVolume'> getSnapshotsForVolume</a> </span>
            <div class='views-field-body'>Retrieves a list oƒf snapshots for a given volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getStaasVersion'> getStaasVersion</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getStorageGroups'> getStorageGroups</a> </span>
            <div class='views-field-body'>Retrieve the network storage groups this volume is attached to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getStorageGroupsNetworkConnectionDetails'> getStorageGroupsNetworkConnectionDetails</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getStorageTierLevel'> getStorageTierLevel</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getStorageType'> getStorageType</a> </span>
            <div class='views-field-body'>Retrieve a description of the Storage object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getTargetIpAddresses'> getTargetIpAddresses</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getTotalBytesUsed'> getTotalBytesUsed</a> </span>
            <div class='views-field-body'>Retrieve the amount of space used by the volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getTotalScheduleSnapshotRetentionCount'> getTotalScheduleSnapshotRetentionCount</a> </span>
            <div class='views-field-body'>Retrieve the total snapshot retention count of all schedules on this network storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getUsageNotification'> getUsageNotification</a> </span>
            <div class='views-field-body'>Retrieve the usage notification for SL Storage services.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getValidReplicationTargetDatacenterLocations'> getValidReplicationTargetDatacenterLocations</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getVendorName'> getVendorName</a> </span>
            <div class='views-field-body'>Retrieve the type of network storage service.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getVirtualGuest'> getVirtualGuest</a> </span>
            <div class='views-field-body'>Retrieve when applicable, the virtual guest associated with a Storage service.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getVolumeDuplicateParameters'> getVolumeDuplicateParameters</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getVolumeHistory'> getVolumeHistory</a> </span>
            <div class='views-field-body'>Retrieve the username and password history for a Storage service.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getVolumeStatus'> getVolumeStatus</a> </span>
            <div class='views-field-body'>Retrieve the current status of a network storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getWebccAccount'> getWebccAccount</a> </span>
            <div class='views-field-body'>Retrieve the account username and password for the EVault webCC interface.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/getWeeklySchedule'> getWeeklySchedule</a> </span>
            <div class='views-field-body'>Retrieve the Weekly Schedule which is associated with this network storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/immediateFailoverToReplicant'> immediateFailoverToReplicant</a> </span>
            <div class='views-field-body'>Immediate Failover to a volume replicant.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/isBlockingOperationInProgress'> isBlockingOperationInProgress</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/isDuplicateReadyForSnapshot'> isDuplicateReadyForSnapshot</a> </span>
            <div class='views-field-body'>Displays the if clone snapshots can be ordered.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/isDuplicateReadyToMount'> isDuplicateReadyToMount</a> </span>
            <div class='views-field-body'>Displays the status of a clone mount.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/removeAccessFromHardware'> removeAccessFromHardware</a> </span>
            <div class='views-field-body'>Remove access to this volume from a specified SoftLayer_Hardware object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/removeAccessFromHardwareList'> removeAccessFromHardwareList</a> </span>
            <div class='views-field-body'>Remove access to this volume from multiple SoftLayer_Hardware objects.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/removeAccessFromHost'> removeAccessFromHost</a> </span>
            <div class='views-field-body'>Remove access to this volume from a specified [[SoftLayer_Hardware|SoftLayer_Virtual_Guest|SoftLayer_Network_Subnet|SoftLayer_Network_Subnet_IpAddress]] object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/removeAccessFromHostList'> removeAccessFromHostList</a> </span>
            <div class='views-field-body'>Remove access to this volume from multiple [[SoftLayer_Hardware|SoftLayer_Virtual_Guest|SoftLayer_Network_Subnet|SoftLayer_Network_Subnet_IpAddress]] objects.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/removeAccessFromIpAddress'> removeAccessFromIpAddress</a> </span>
            <div class='views-field-body'>Remove access to this volume from a specified SoftLayer_Network_Subnet_IpAddress object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/removeAccessFromIpAddressList'> removeAccessFromIpAddressList</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/removeAccessFromSubnet'> removeAccessFromSubnet</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/removeAccessFromSubnetList'> removeAccessFromSubnetList</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/removeAccessFromVirtualGuest'> removeAccessFromVirtualGuest</a> </span>
            <div class='views-field-body'>Remove access to this volume from a specified SoftLayer_Virtual_Guest object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/removeAccessFromVirtualGuestList'> removeAccessFromVirtualGuestList</a> </span>
            <div class='views-field-body'>Remove access to this volume from multiple SoftLayer_Virtual_Guest objects.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/removeAccessToReplicantFromHardwareList'> removeAccessToReplicantFromHardwareList</a> </span>
            <div class='views-field-body'>Remove access to this volume's replica from multiple SoftLayer_Hardware objects.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/removeAccessToReplicantFromIpAddressList'> removeAccessToReplicantFromIpAddressList</a> </span>
            <div class='views-field-body'>Remove access to this replica volume's replica from multiple SoftLayer_Network_Subnet_IpAddress objects.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/removeAccessToReplicantFromSubnet'> removeAccessToReplicantFromSubnet</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/removeAccessToReplicantFromSubnetList'> removeAccessToReplicantFromSubnetList</a> </span>
            <div class='views-field-body'>Remove access to this volume's replica from multiple SoftLayer_Network_Subnet objects.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/removeAccessToReplicantFromVirtualGuestList'> removeAccessToReplicantFromVirtualGuestList</a> </span>
            <div class='views-field-body'>Remove access to this volume's replica from multiple SoftLayer_Virtual_Guest objects.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/removeCredential'> removeCredential</a> </span>
            <div class='views-field-body'>This method will remove a credential from the current volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/restoreFile'> restoreFile</a> </span>
            <div class='views-field-body'>Restore access to an individual file in a Storage account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/restoreFromSnapshot'> restoreFromSnapshot</a> </span>
            <div class='views-field-body'>Restore from a volume snapshot.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/sendPasswordReminderEmail'> sendPasswordReminderEmail</a> </span>
            <div class='views-field-body'>Email the password for the Storage account to the master user.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/setMountable'> setMountable</a> </span>
            <div class='views-field-body'>Enable or disable mounting of a Storage volume.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/setSnapshotAllocation'> setSnapshotAllocation</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/upgradeVolumeCapacity'> upgradeVolumeCapacity</a> </span>
            <div class='views-field-body'>Edit the Storage volume to a different package</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage/uploadFile'> uploadFile</a> </span>
            <div class='views-field-body'>Upload a file to a Storage account's root directory.</div>
        </div>
        </div>
</div>

