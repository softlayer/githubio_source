---
title: "SoftLayer_Virtual_Guest"
description: "The virtual guest service provides a common interface to any virtualization platform supported by SoftLayer. The interac... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# SoftLayer_Virtual_Guest
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Virtual_Guest' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Guest' >Datatype</a></li>
    </ul>
</div>

## Description
The virtual guest service provides a common interface to any virtualization platform supported by SoftLayer. The interaction with various third party APIs is not needed when implementing this service to administer your guests. The SoftLayer_Virtual_Guest service also controls individual CloudLayer Computing Instances purchased from SoftLayer in a way that is analogous to the [SoftLayer_Hardware_Server]({{<ref "reference/datatypes/SoftLayer_Hardware_Server">}}) service's control over physical hardware purchased form SoftLayer. 



        
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

#### [activatePrivatePort](/reference/services/SoftLayer_Virtual_Guest/activatePrivatePort)
Activate the private port
</div>

<div class="method-row">

#### [activatePublicPort](/reference/services/SoftLayer_Virtual_Guest/activatePublicPort)
Activate the public port
</div>

<div class="method-row">

#### [allowAccessToNetworkStorage](/reference/services/SoftLayer_Virtual_Guest/allowAccessToNetworkStorage)
Allow access to a SoftLayer_Network_Storage volume from this device. 
</div>

<div class="method-row">

#### [allowAccessToNetworkStorageList](/reference/services/SoftLayer_Virtual_Guest/allowAccessToNetworkStorageList)
Allow access to multiple SoftLayer_Network_Storage volumes from this device. 
</div>

<div class="method-row">

#### [attachDiskImage](/reference/services/SoftLayer_Virtual_Guest/attachDiskImage)
Attaches a disk image.
</div>

<div class="method-row">

#### [cancelIsolationForDestructiveAction](/reference/services/SoftLayer_Virtual_Guest/cancelIsolationForDestructiveAction)

</div>

<div class="method-row">

#### [captureImage](/reference/services/SoftLayer_Virtual_Guest/captureImage)
Captures a Flex Image of the hard disk on the virtual machine.
</div>

<div class="method-row">

#### [checkHostDiskAvailability](/reference/services/SoftLayer_Virtual_Guest/checkHostDiskAvailability)

</div>

<div class="method-row">

#### [configureMetadataDisk](/reference/services/SoftLayer_Virtual_Guest/configureMetadataDisk)
Configures the guest's metadata disk.
</div>

<div class="method-row">

#### [createArchiveTemplate](/reference/services/SoftLayer_Virtual_Guest/createArchiveTemplate)
[SoftLayer_Virtual_Guest_Block_Devices]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Block_Devices">}}) can be grouped together in and backed up in an archive for later use. This method generates a transaction to perform an archive of the provided block devices. 
</div>

<div class="method-row">

#### [createArchiveTransaction](/reference/services/SoftLayer_Virtual_Guest/createArchiveTransaction)
[SoftLayer_Virtual_Guest_Block_Device]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Block_Device">}}) can be grouped together in and backed up in an archive for later use. This method generates a transaction to perform an archive of the provided block devices. 
</div>

<div class="method-row">

#### [createObject](/reference/services/SoftLayer_Virtual_Guest/createObject)
Create a new computing instance
</div>

<div class="method-row">

#### [createObjects](/reference/services/SoftLayer_Virtual_Guest/createObjects)
Create new computing instances
</div>

<div class="method-row">

#### [createPostSoftwareInstallTransaction](/reference/services/SoftLayer_Virtual_Guest/createPostSoftwareInstallTransaction)

</div>

<div class="method-row">

#### [deleteObject](/reference/services/SoftLayer_Virtual_Guest/deleteObject)
Delete a computing instance
</div>

<div class="method-row">

#### [deleteTag](/reference/services/SoftLayer_Virtual_Guest/deleteTag)
Delete a tag
</div>

<div class="method-row">

#### [deleteTransientWebhook](/reference/services/SoftLayer_Virtual_Guest/deleteTransientWebhook)

</div>

<div class="method-row">

#### [detachDiskImage](/reference/services/SoftLayer_Virtual_Guest/detachDiskImage)
Detaches a disk image.
</div>

<div class="method-row">

#### [editObject](/reference/services/SoftLayer_Virtual_Guest/editObject)
Edit a computing instance's properties
</div>

<div class="method-row">

#### [executeIderaBareMetalRestore](/reference/services/SoftLayer_Virtual_Guest/executeIderaBareMetalRestore)
Reboot a guest into the Idera Bare Metal Restore image.
</div>

<div class="method-row">

#### [executeR1SoftBareMetalRestore](/reference/services/SoftLayer_Virtual_Guest/executeR1SoftBareMetalRestore)
Reboot a guest into the R1Soft Bare Metal Restore image.
</div>

<div class="method-row">

#### [executeRemoteScript](/reference/services/SoftLayer_Virtual_Guest/executeRemoteScript)
Download and run remote script from uri on the virtual guest. Requires https for script to be executed after download. 
</div>

<div class="method-row">

#### [executeRescueLayer](/reference/services/SoftLayer_Virtual_Guest/executeRescueLayer)
Reboot a Linux guest into the Xen rescue image.
</div>

<div class="method-row">

#### [findByHostname](/reference/services/SoftLayer_Virtual_Guest/findByHostname)

</div>

<div class="method-row">

#### [findByIpAddress](/reference/services/SoftLayer_Virtual_Guest/findByIpAddress)
Find CCI by its primary public or private IP (ipv4) address.
</div>

<div class="method-row">

#### [generateOrderTemplate](/reference/services/SoftLayer_Virtual_Guest/generateOrderTemplate)
Obtain an order container for a given template object
</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Virtual_Guest/getAccount)
Retrieve the account that a virtual guest belongs to.
</div>

<div class="method-row">

#### [getAccountOwnedPoolFlag](/reference/services/SoftLayer_Virtual_Guest/getAccountOwnedPoolFlag)

</div>

<div class="method-row">

#### [getActiveNetworkMonitorIncident](/reference/services/SoftLayer_Virtual_Guest/getActiveNetworkMonitorIncident)
Retrieve a virtual guest's currently active network monitoring incidents.
</div>

<div class="method-row">

#### [getActiveTickets](/reference/services/SoftLayer_Virtual_Guest/getActiveTickets)

</div>

<div class="method-row">

#### [getActiveTransaction](/reference/services/SoftLayer_Virtual_Guest/getActiveTransaction)
Retrieve a transaction that is still be performed on a cloud server.
</div>

<div class="method-row">

#### [getActiveTransactions](/reference/services/SoftLayer_Virtual_Guest/getActiveTransactions)
Retrieve any active transaction(s) that are currently running for the server (example: os reload).
</div>

<div class="method-row">

#### [getAdditionalRequiredPricesForOsReload](/reference/services/SoftLayer_Virtual_Guest/getAdditionalRequiredPricesForOsReload)
Return a collection of SoftLayer_Item_Price objects for an OS reload
</div>

<div class="method-row">

#### [getAllowedHost](/reference/services/SoftLayer_Virtual_Guest/getAllowedHost)
Retrieve the SoftLayer_Network_Storage_Allowed_Host information to connect this Virtual Guest to Network Storage volumes that require access control lists.
</div>

<div class="method-row">

#### [getAllowedNetworkStorage](/reference/services/SoftLayer_Virtual_Guest/getAllowedNetworkStorage)
Retrieve the SoftLayer_Network_Storage objects that this SoftLayer_Virtual_Guest has access to.
</div>

<div class="method-row">

#### [getAllowedNetworkStorageReplicas](/reference/services/SoftLayer_Virtual_Guest/getAllowedNetworkStorageReplicas)
Retrieve the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Virtual_Guest has access to.
</div>

<div class="method-row">

#### [getAntivirusSpywareSoftwareComponent](/reference/services/SoftLayer_Virtual_Guest/getAntivirusSpywareSoftwareComponent)
Retrieve a antivirus / spyware software component object.
</div>

<div class="method-row">

#### [getApplicationDeliveryController](/reference/services/SoftLayer_Virtual_Guest/getApplicationDeliveryController)

</div>

<div class="method-row">

#### [getAttachedNetworkStorages](/reference/services/SoftLayer_Virtual_Guest/getAttachedNetworkStorages)
Return a list of SoftLayer_Network_Storage volumes authorized to this device. 
</div>

<div class="method-row">

#### [getAttributes](/reference/services/SoftLayer_Virtual_Guest/getAttributes)

</div>

<div class="method-row">

#### [getAvailableBlockDevicePositions](/reference/services/SoftLayer_Virtual_Guest/getAvailableBlockDevicePositions)

</div>

<div class="method-row">

#### [getAvailableMonitoring](/reference/services/SoftLayer_Virtual_Guest/getAvailableMonitoring)
Retrieve an object that stores the maximum level for the monitoring query types and response types.
</div>

<div class="method-row">

#### [getAvailableNetworkStorages](/reference/services/SoftLayer_Virtual_Guest/getAvailableNetworkStorages)
Return a list of SoftLayer_Network_Storage volumes that can be authorized to this device. 
</div>

<div class="method-row">

#### [getAverageDailyPrivateBandwidthUsage](/reference/services/SoftLayer_Virtual_Guest/getAverageDailyPrivateBandwidthUsage)
Retrieve the average daily private bandwidth usage for the current billing cycle.
</div>

<div class="method-row">

#### [getAverageDailyPublicBandwidthUsage](/reference/services/SoftLayer_Virtual_Guest/getAverageDailyPublicBandwidthUsage)
Retrieve the average daily public bandwidth usage for the current billing cycle.
</div>

<div class="method-row">

#### [getBackendNetworkComponents](/reference/services/SoftLayer_Virtual_Guest/getBackendNetworkComponents)
Retrieve a guests's backend network components.
</div>

<div class="method-row">

#### [getBackendRouters](/reference/services/SoftLayer_Virtual_Guest/getBackendRouters)
Retrieve a guest's backend or private router.
</div>

<div class="method-row">

#### [getBandwidthAllocation](/reference/services/SoftLayer_Virtual_Guest/getBandwidthAllocation)
Retrieve a computing instance's allotted bandwidth (measured in GB).
</div>

<div class="method-row">

#### [getBandwidthAllotmentDetail](/reference/services/SoftLayer_Virtual_Guest/getBandwidthAllotmentDetail)
Retrieve a computing instance's allotted detail record. Allotment details link bandwidth allocation with allotments.
</div>

<div class="method-row">

#### [getBandwidthDataByDate](/reference/services/SoftLayer_Virtual_Guest/getBandwidthDataByDate)
Retrieve the amount of network traffic that occurred for the specified time frame for a computing instance. 
</div>

<div class="method-row">

#### [getBandwidthForDateRange](/reference/services/SoftLayer_Virtual_Guest/getBandwidthForDateRange)
Retrieve bandwidth data from a tracking object.
</div>

<div class="method-row">

#### [getBandwidthImage](/reference/services/SoftLayer_Virtual_Guest/getBandwidthImage)
Retrieve a visual representation of the amount of network traffic that occurred for the specified time frame for a computing instance. 
</div>

<div class="method-row">

#### [getBandwidthImageByDate](/reference/services/SoftLayer_Virtual_Guest/getBandwidthImageByDate)
Retrieve a visual representation of the amount of network traffic that occurred for the specified time frame for a computing instance. 
</div>

<div class="method-row">

#### [getBandwidthTotal](/reference/services/SoftLayer_Virtual_Guest/getBandwidthTotal)
Retrieve total amount of network traffic that was in use during the time specified by the input parameters for a computing instance. 
</div>

<div class="method-row">

#### [getBillingCycleBandwidthUsage](/reference/services/SoftLayer_Virtual_Guest/getBillingCycleBandwidthUsage)
Retrieve the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this server is attached to.
</div>

<div class="method-row">

#### [getBillingCyclePrivateBandwidthUsage](/reference/services/SoftLayer_Virtual_Guest/getBillingCyclePrivateBandwidthUsage)
Retrieve the raw private bandwidth usage data for the current billing cycle.
</div>

<div class="method-row">

#### [getBillingCyclePublicBandwidthUsage](/reference/services/SoftLayer_Virtual_Guest/getBillingCyclePublicBandwidthUsage)
Retrieve the raw public bandwidth usage data for the current billing cycle.
</div>

<div class="method-row">

#### [getBillingItem](/reference/services/SoftLayer_Virtual_Guest/getBillingItem)
Retrieve the billing item for a CloudLayer Compute Instance.
</div>

<div class="method-row">

#### [getBlockCancelBecauseDisconnectedFlag](/reference/services/SoftLayer_Virtual_Guest/getBlockCancelBecauseDisconnectedFlag)
Retrieve determines whether the instance is ineligible for cancellation because it is disconnected.
</div>

<div class="method-row">

#### [getBlockDeviceTemplateGroup](/reference/services/SoftLayer_Virtual_Guest/getBlockDeviceTemplateGroup)
Retrieve the global identifier for the image template that was used to provision or reload a guest.
</div>

<div class="method-row">

#### [getBlockDevices](/reference/services/SoftLayer_Virtual_Guest/getBlockDevices)
Retrieve a computing instance's block devices. Block devices link [SoftLayer_Virtual_Disk_Image]({{<ref "reference/datatypes/SoftLayer_Virtual_Disk_Image">}}) to computing instances.
</div>

<div class="method-row">

#### [getBootMode](/reference/services/SoftLayer_Virtual_Guest/getBootMode)
Retrieves the boot mode of the VSI.
</div>

<div class="method-row">

#### [getBootOrder](/reference/services/SoftLayer_Virtual_Guest/getBootOrder)

</div>

<div class="method-row">

#### [getBrowserConsoleAccessLogs](/reference/services/SoftLayer_Virtual_Guest/getBrowserConsoleAccessLogs)
Retrieve a virtual guest's browser access logs.
</div>

<div class="method-row">

#### [getConsoleAccessLog](/reference/services/SoftLayer_Virtual_Guest/getConsoleAccessLog)
get console access logs
</div>

<div class="method-row">

#### [getConsoleData](/reference/services/SoftLayer_Virtual_Guest/getConsoleData)
Retrieve a container for a guest's console data
</div>

<div class="method-row">

#### [getConsoleIpAddressFlag](/reference/services/SoftLayer_Virtual_Guest/getConsoleIpAddressFlag)
Retrieve a flag indicating a computing instance's console IP address is assigned.
</div>

<div class="method-row">

#### [getConsoleIpAddressRecord](/reference/services/SoftLayer_Virtual_Guest/getConsoleIpAddressRecord)
Retrieve a record containing information about a computing instance's console IP and port number.
</div>

<div class="method-row">

#### [getContinuousDataProtectionSoftwareComponent](/reference/services/SoftLayer_Virtual_Guest/getContinuousDataProtectionSoftwareComponent)
Retrieve a continuous data protection software component object.
</div>

<div class="method-row">

#### [getControlPanel](/reference/services/SoftLayer_Virtual_Guest/getControlPanel)
Retrieve a guest's control panel.
</div>

<div class="method-row">

#### [getCoreRestrictedOperatingSystemPrice](/reference/services/SoftLayer_Virtual_Guest/getCoreRestrictedOperatingSystemPrice)
Return the associated core-restricted operating system item price for the virtual server.
</div>

<div class="method-row">

#### [getCpuMetricDataByDate](/reference/services/SoftLayer_Virtual_Guest/getCpuMetricDataByDate)
Retrieve records containing the percentage of the amount of time that a cpu was in use for the specified time frame for a computing instance. 
</div>

<div class="method-row">

#### [getCpuMetricImage](/reference/services/SoftLayer_Virtual_Guest/getCpuMetricImage)
Retrieve a visual representation of the percentage of the amount of time that a cpu was in use for the specified time frame for a computing instance. 
</div>

<div class="method-row">

#### [getCpuMetricImageByDate](/reference/services/SoftLayer_Virtual_Guest/getCpuMetricImageByDate)
Retrieve a visual representation of the percentage of the amount of time that a cpu was in use for the specified time frame for a computing instance. 
</div>

<div class="method-row">

#### [getCreateObjectOptions](/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions)
Determine options available when creating a computing instance
</div>

<div class="method-row">

#### [getCurrentBandwidthSummary](/reference/services/SoftLayer_Virtual_Guest/getCurrentBandwidthSummary)
Retrieve an object that provides commonly used bandwidth summary components for the current billing cycle.
</div>

<div class="method-row">

#### [getCurrentBillingDetail](/reference/services/SoftLayer_Virtual_Guest/getCurrentBillingDetail)
<< EOT
</div>

<div class="method-row">

#### [getCurrentBillingTotal](/reference/services/SoftLayer_Virtual_Guest/getCurrentBillingTotal)
Get the billing total for this instance's usage up to this point. This total includes all bandwidth charges. 
</div>

<div class="method-row">

#### [getCustomBandwidthDataByDate](/reference/services/SoftLayer_Virtual_Guest/getCustomBandwidthDataByDate)
Retrieve bandwidth graph by date.
</div>

<div class="method-row">

#### [getCustomMetricDataByDate](/reference/services/SoftLayer_Virtual_Guest/getCustomMetricDataByDate)
Retrieve bandwidth graph by date.
</div>

<div class="method-row">

#### [getDatacenter](/reference/services/SoftLayer_Virtual_Guest/getDatacenter)
Retrieve the datacenter that a virtual guest resides in.
</div>

<div class="method-row">

#### [getDedicatedHost](/reference/services/SoftLayer_Virtual_Guest/getDedicatedHost)
Retrieve the dedicated host associated with this guest.
</div>

<div class="method-row">

#### [getDriveRetentionItemPrice](/reference/services/SoftLayer_Virtual_Guest/getDriveRetentionItemPrice)
Return a drive retention SoftLayer_Item_Price object for a guest.
</div>

<div class="method-row">

#### [getEvaultNetworkStorage](/reference/services/SoftLayer_Virtual_Guest/getEvaultNetworkStorage)
Retrieve a guest's associated EVault network storage service account.
</div>

<div class="method-row">

#### [getFirewallProtectableSubnets](/reference/services/SoftLayer_Virtual_Guest/getFirewallProtectableSubnets)
Get the subnets associated with this CloudLayer computing instance that are protectable by a network component firewall.
</div>

<div class="method-row">

#### [getFirewallServiceComponent](/reference/services/SoftLayer_Virtual_Guest/getFirewallServiceComponent)
Retrieve a computing instance's hardware firewall services.
</div>

<div class="method-row">

#### [getFirstAvailableBlockDevicePosition](/reference/services/SoftLayer_Virtual_Guest/getFirstAvailableBlockDevicePosition)

</div>

<div class="method-row">

#### [getFrontendNetworkComponents](/reference/services/SoftLayer_Virtual_Guest/getFrontendNetworkComponents)
Retrieve a guest's frontend network components.
</div>

<div class="method-row">

#### [getFrontendRouters](/reference/services/SoftLayer_Virtual_Guest/getFrontendRouters)
Retrieve a guest's frontend or public router.
</div>

<div class="method-row">

#### [getGlobalIdentifier](/reference/services/SoftLayer_Virtual_Guest/getGlobalIdentifier)
Retrieve a guest's universally unique identifier.
</div>

<div class="method-row">

#### [getGpuCount](/reference/services/SoftLayer_Virtual_Guest/getGpuCount)
Retrieve the number of GPUs attached to the guest.
</div>

<div class="method-row">

#### [getGpuType](/reference/services/SoftLayer_Virtual_Guest/getGpuType)
Retrieve the name of the GPU type attached to the guest.
</div>

<div class="method-row">

#### [getGuestBootParameter](/reference/services/SoftLayer_Virtual_Guest/getGuestBootParameter)

</div>

<div class="method-row">

#### [getHost](/reference/services/SoftLayer_Virtual_Guest/getHost)
Retrieve the virtual host on which a virtual guest resides (available only on private clouds).
</div>

<div class="method-row">

#### [getHostIpsSoftwareComponent](/reference/services/SoftLayer_Virtual_Guest/getHostIpsSoftwareComponent)
Retrieve a host IPS software component object.
</div>

<div class="method-row">

#### [getHourlyBillingFlag](/reference/services/SoftLayer_Virtual_Guest/getHourlyBillingFlag)
Retrieve a guest's hourly billing status.
</div>

<div class="method-row">

#### [getInboundPrivateBandwidthUsage](/reference/services/SoftLayer_Virtual_Guest/getInboundPrivateBandwidthUsage)
Retrieve the total private inbound bandwidth for this computing instance for the current billing cycle.
</div>

<div class="method-row">

#### [getInboundPublicBandwidthUsage](/reference/services/SoftLayer_Virtual_Guest/getInboundPublicBandwidthUsage)
Retrieve the total public inbound bandwidth for this computing instance for the current billing cycle.
</div>

<div class="method-row">

#### [getInternalTagReferences](/reference/services/SoftLayer_Virtual_Guest/getInternalTagReferences)

</div>

<div class="method-row">

#### [getIsoBootImage](/reference/services/SoftLayer_Virtual_Guest/getIsoBootImage)

</div>

<div class="method-row">

#### [getItemPricesFromSoftwareDescriptions](/reference/services/SoftLayer_Virtual_Guest/getItemPricesFromSoftwareDescriptions)
Return a collection of SoftLayer_Item_Price objects from a collection of SoftLayer_Software_Description
</div>

<div class="method-row">

#### [getLastKnownPowerState](/reference/services/SoftLayer_Virtual_Guest/getLastKnownPowerState)
Retrieve the last known power state of a virtual guest in the event the guest is turned off outside of IMS or has gone offline.
</div>

<div class="method-row">

#### [getLastOperatingSystemReload](/reference/services/SoftLayer_Virtual_Guest/getLastOperatingSystemReload)
Retrieve the last transaction that a cloud server's operating system was loaded.
</div>

<div class="method-row">

#### [getLastTransaction](/reference/services/SoftLayer_Virtual_Guest/getLastTransaction)
Retrieve the last transaction a cloud server had performed.
</div>

<div class="method-row">

#### [getLatestNetworkMonitorIncident](/reference/services/SoftLayer_Virtual_Guest/getLatestNetworkMonitorIncident)
Retrieve a virtual guest's latest network monitoring incident.
</div>

<div class="method-row">

#### [getLocalDiskFlag](/reference/services/SoftLayer_Virtual_Guest/getLocalDiskFlag)
Retrieve a flag indicating that the virtual guest has at least one disk which is local to the host it runs on. This does not include a SWAP device.
</div>

<div class="method-row">

#### [getLocation](/reference/services/SoftLayer_Virtual_Guest/getLocation)
Retrieve where guest is located within SoftLayer's location hierarchy.
</div>

<div class="method-row">

#### [getManagedResourceFlag](/reference/services/SoftLayer_Virtual_Guest/getManagedResourceFlag)
Retrieve a flag indicating that the virtual guest is a managed resource.
</div>

<div class="method-row">

#### [getMemoryMetricDataByDate](/reference/services/SoftLayer_Virtual_Guest/getMemoryMetricDataByDate)
Retrieve records containing the amount memory that was used for the specified time frame for a computing instance. 
</div>

<div class="method-row">

#### [getMemoryMetricImage](/reference/services/SoftLayer_Virtual_Guest/getMemoryMetricImage)
Retrieve a visual representation of the amount of memory used for the specified time frame for a computing instance. 
</div>

<div class="method-row">

#### [getMemoryMetricImageByDate](/reference/services/SoftLayer_Virtual_Guest/getMemoryMetricImageByDate)
Retrieve a visual representation of the amount of memory used for the specified time frame for a computing instance. 
</div>

<div class="method-row">

#### [getMetricTrackingObject](/reference/services/SoftLayer_Virtual_Guest/getMetricTrackingObject)
Retrieve a guest's metric tracking object.
</div>

<div class="method-row">

#### [getMetricTrackingObjectId](/reference/services/SoftLayer_Virtual_Guest/getMetricTrackingObjectId)
Retrieve the metric tracking object id for this guest.
</div>

<div class="method-row">

#### [getMonitoringRobot](/reference/services/SoftLayer_Virtual_Guest/getMonitoringRobot)

</div>

<div class="method-row">

#### [getMonitoringServiceComponent](/reference/services/SoftLayer_Virtual_Guest/getMonitoringServiceComponent)
Retrieve a virtual guest's network monitoring services.
</div>

<div class="method-row">

#### [getMonitoringServiceEligibilityFlag](/reference/services/SoftLayer_Virtual_Guest/getMonitoringServiceEligibilityFlag)

</div>

<div class="method-row">

#### [getMonitoringUserNotification](/reference/services/SoftLayer_Virtual_Guest/getMonitoringUserNotification)
Retrieve the monitoring notification objects for this guest. Each object links this guest instance to a user account that will be notified if monitoring on this guest object fails
</div>

<div class="method-row">

#### [getNetworkComponentFirewallProtectableIpAddresses](/reference/services/SoftLayer_Virtual_Guest/getNetworkComponentFirewallProtectableIpAddresses)
Get the IP addresses associated with this CloudLayer computing instance that are protectable by a network component firewall.
</div>

<div class="method-row">

#### [getNetworkComponents](/reference/services/SoftLayer_Virtual_Guest/getNetworkComponents)
Retrieve a guests's network components.
</div>

<div class="method-row">

#### [getNetworkMonitorIncidents](/reference/services/SoftLayer_Virtual_Guest/getNetworkMonitorIncidents)
Retrieve all of a virtual guest's network monitoring incidents.
</div>

<div class="method-row">

#### [getNetworkMonitors](/reference/services/SoftLayer_Virtual_Guest/getNetworkMonitors)
Retrieve a guests's network monitors.
</div>

<div class="method-row">

#### [getNetworkStorage](/reference/services/SoftLayer_Virtual_Guest/getNetworkStorage)
Retrieve a guest's associated network storage accounts.
</div>

<div class="method-row">

#### [getNetworkVlans](/reference/services/SoftLayer_Virtual_Guest/getNetworkVlans)
Retrieve the network Vlans that a guest's network components are associated with.
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Virtual_Guest/getObject)
Retrieve a SoftLayer_Virtual_Guest record.
</div>

<div class="method-row">

#### [getOpenCancellationTicket](/reference/services/SoftLayer_Virtual_Guest/getOpenCancellationTicket)
Retrieve an open ticket requesting cancellation of this server, if one exists.
</div>

<div class="method-row">

#### [getOperatingSystem](/reference/services/SoftLayer_Virtual_Guest/getOperatingSystem)
Retrieve a guest's operating system.
</div>

<div class="method-row">

#### [getOperatingSystemReferenceCode](/reference/services/SoftLayer_Virtual_Guest/getOperatingSystemReferenceCode)
Retrieve a guest's operating system software description.
</div>

<div class="method-row">

#### [getOrderTemplate](/reference/services/SoftLayer_Virtual_Guest/getOrderTemplate)
Obtain an order container that is ready to be sent to the [[SoftLayer_Product_Order#placeOrder|SoftLayer_Product_Order::placeOrder]] method.
</div>

<div class="method-row">

#### [getOrderedPackageId](/reference/services/SoftLayer_Virtual_Guest/getOrderedPackageId)
Retrieve the original package id provided with the order for a Cloud Computing Instance.
</div>

<div class="method-row">

#### [getOutboundPrivateBandwidthUsage](/reference/services/SoftLayer_Virtual_Guest/getOutboundPrivateBandwidthUsage)
Retrieve the total private outbound bandwidth for this computing instance for the current billing cycle.
</div>

<div class="method-row">

#### [getOutboundPublicBandwidthUsage](/reference/services/SoftLayer_Virtual_Guest/getOutboundPublicBandwidthUsage)
Retrieve the total public outbound bandwidth for this computing instance for the current billing cycle.
</div>

<div class="method-row">

#### [getOverBandwidthAllocationFlag](/reference/services/SoftLayer_Virtual_Guest/getOverBandwidthAllocationFlag)
Retrieve whether the bandwidth usage for this computing instance for the current billing cycle exceeds the allocation.
</div>

<div class="method-row">

#### [getPendingMaintenanceActions](/reference/services/SoftLayer_Virtual_Guest/getPendingMaintenanceActions)
Returns a list of all the pending maintenance actions affecting this guest. 
</div>

<div class="method-row">

#### [getPendingMigrationFlag](/reference/services/SoftLayer_Virtual_Guest/getPendingMigrationFlag)
Retrieve when true this virtual guest must be migrated using SoftLayer_Virtual_Guest::migrate.
</div>

<div class="method-row">

#### [getPlacementGroup](/reference/services/SoftLayer_Virtual_Guest/getPlacementGroup)
Retrieve the placement group that a virtual guest belongs to.
</div>

<div class="method-row">

#### [getPowerState](/reference/services/SoftLayer_Virtual_Guest/getPowerState)
Retrieve the current power state of a virtual guest.
</div>

<div class="method-row">

#### [getPrimaryBackendIpAddress](/reference/services/SoftLayer_Virtual_Guest/getPrimaryBackendIpAddress)
Retrieve a guest's primary private IP address.
</div>

<div class="method-row">

#### [getPrimaryBackendNetworkComponent](/reference/services/SoftLayer_Virtual_Guest/getPrimaryBackendNetworkComponent)
Retrieve a guest's primary backend network component.
</div>

<div class="method-row">

#### [getPrimaryIpAddress](/reference/services/SoftLayer_Virtual_Guest/getPrimaryIpAddress)
Retrieve the guest's primary public IP address.
</div>

<div class="method-row">

#### [getPrimaryNetworkComponent](/reference/services/SoftLayer_Virtual_Guest/getPrimaryNetworkComponent)
Retrieve a guest's primary public network component.
</div>

<div class="method-row">

#### [getPrivateNetworkOnlyFlag](/reference/services/SoftLayer_Virtual_Guest/getPrivateNetworkOnlyFlag)
Retrieve whether the computing instance only has access to the private network.
</div>

<div class="method-row">

#### [getProjectedOverBandwidthAllocationFlag](/reference/services/SoftLayer_Virtual_Guest/getProjectedOverBandwidthAllocationFlag)
Retrieve whether the bandwidth usage for this computing instance for the current billing cycle is projected to exceed the allocation.
</div>

<div class="method-row">

#### [getProjectedPublicBandwidthUsage](/reference/services/SoftLayer_Virtual_Guest/getProjectedPublicBandwidthUsage)
Retrieve the projected public outbound bandwidth for this computing instance for the current billing cycle.
</div>

<div class="method-row">

#### [getProvisionDate](/reference/services/SoftLayer_Virtual_Guest/getProvisionDate)

</div>

<div class="method-row">

#### [getRecentEvents](/reference/services/SoftLayer_Virtual_Guest/getRecentEvents)
Retrieve recent events that impact this computing instance.
</div>

<div class="method-row">

#### [getRecentMetricData](/reference/services/SoftLayer_Virtual_Guest/getRecentMetricData)
Recent metric data for a guest 
</div>

<div class="method-row">

#### [getRegionalGroup](/reference/services/SoftLayer_Virtual_Guest/getRegionalGroup)
Retrieve the regional group this guest is in.
</div>

<div class="method-row">

#### [getRegionalInternetRegistry](/reference/services/SoftLayer_Virtual_Guest/getRegionalInternetRegistry)

</div>

<div class="method-row">

#### [getReservedCapacityGroup](/reference/services/SoftLayer_Virtual_Guest/getReservedCapacityGroup)
Retrieve the reserved capacity group the guest is associated with.
</div>

<div class="method-row">

#### [getReservedCapacityGroupFlag](/reference/services/SoftLayer_Virtual_Guest/getReservedCapacityGroupFlag)
Retrieve flag to indicate whether or not a guest is part of a reserved capacity group.
</div>

<div class="method-row">

#### [getReservedCapacityGroupInstance](/reference/services/SoftLayer_Virtual_Guest/getReservedCapacityGroupInstance)
Retrieve the reserved capacity group instance the guest is associated with.
</div>

<div class="method-row">

#### [getReverseDomainRecords](/reference/services/SoftLayer_Virtual_Guest/getReverseDomainRecords)
Retrieve the reverse domain records associated with a server.
</div>

<div class="method-row">

#### [getScaleAssets](/reference/services/SoftLayer_Virtual_Guest/getScaleAssets)
Retrieve collection of scale assets this guest corresponds to.
</div>

<div class="method-row">

#### [getScaleMember](/reference/services/SoftLayer_Virtual_Guest/getScaleMember)
Retrieve the scale member for this guest, if applicable.
</div>

<div class="method-row">

#### [getScaledFlag](/reference/services/SoftLayer_Virtual_Guest/getScaledFlag)
Retrieve whether or not this guest is a member of a scale group and was automatically created as part of a scale group action.
</div>

<div class="method-row">

#### [getSecurityScanRequests](/reference/services/SoftLayer_Virtual_Guest/getSecurityScanRequests)
Retrieve a guest's vulnerability scan requests.
</div>

<div class="method-row">

#### [getServerRoom](/reference/services/SoftLayer_Virtual_Guest/getServerRoom)
Retrieve the server room that a guest is located at. There may be more than one server room for every data center.
</div>

<div class="method-row">

#### [getSoftwareComponents](/reference/services/SoftLayer_Virtual_Guest/getSoftwareComponents)
Retrieve a guest's installed software.
</div>

<div class="method-row">

#### [getSshKeys](/reference/services/SoftLayer_Virtual_Guest/getSshKeys)
Retrieve sSH keys to be installed on the server during provisioning or an OS reload.
</div>

<div class="method-row">

#### [getStatus](/reference/services/SoftLayer_Virtual_Guest/getStatus)
Retrieve a computing instance's status.
</div>

<div class="method-row">

#### [getTagReferences](/reference/services/SoftLayer_Virtual_Guest/getTagReferences)

</div>

<div class="method-row">

#### [getTransientGuestFlag](/reference/services/SoftLayer_Virtual_Guest/getTransientGuestFlag)
Retrieve whether or not a computing instance is a Transient Instance.
</div>

<div class="method-row">

#### [getTransientWebhookURI](/reference/services/SoftLayer_Virtual_Guest/getTransientWebhookURI)
Retrieve the endpoint used to notify customers their transient guest is terminating.
</div>

<div class="method-row">

#### [getType](/reference/services/SoftLayer_Virtual_Guest/getType)
Retrieve the type of this virtual guest.
</div>

<div class="method-row">

#### [getUpgradeItemPrices](/reference/services/SoftLayer_Virtual_Guest/getUpgradeItemPrices)
Retrieve a computing instance's upgradeable items.
</div>

<div class="method-row">

#### [getUpgradeRequest](/reference/services/SoftLayer_Virtual_Guest/getUpgradeRequest)
Retrieve a computing instance's associated upgrade request object if any.
</div>

<div class="method-row">

#### [getUserData](/reference/services/SoftLayer_Virtual_Guest/getUserData)
Retrieve a base64 encoded string containing custom user data for a Cloud Computing Instance order.
</div>

<div class="method-row">

#### [getUsers](/reference/services/SoftLayer_Virtual_Guest/getUsers)
Retrieve a list of users that have access to this computing instance.
</div>

<div class="method-row">

#### [getValidBlockDeviceTemplateGroups](/reference/services/SoftLayer_Virtual_Guest/getValidBlockDeviceTemplateGroups)
Return a list of valid block device template groups based on this host
</div>

<div class="method-row">

#### [getVirtualRack](/reference/services/SoftLayer_Virtual_Guest/getVirtualRack)
Retrieve the name of the bandwidth allotment that a hardware belongs too.
</div>

<div class="method-row">

#### [getVirtualRackId](/reference/services/SoftLayer_Virtual_Guest/getVirtualRackId)
Retrieve the id of the bandwidth allotment that a computing instance belongs too.
</div>

<div class="method-row">

#### [getVirtualRackName](/reference/services/SoftLayer_Virtual_Guest/getVirtualRackName)
Retrieve the name of the bandwidth allotment that a computing instance belongs too.
</div>

<div class="method-row">

#### [isBackendPingable](/reference/services/SoftLayer_Virtual_Guest/isBackendPingable)
Verifies if a guest's backend ip address is pingable.
</div>

<div class="method-row">

#### [isCloudInit](/reference/services/SoftLayer_Virtual_Guest/isCloudInit)
Determines if the virtual guest was provisioned from a cloud-init enabled image. 
</div>

<div class="method-row">

#### [isPingable](/reference/services/SoftLayer_Virtual_Guest/isPingable)
Verifies if guest is pingable.
</div>

<div class="method-row">

#### [isolateInstanceForDestructiveAction](/reference/services/SoftLayer_Virtual_Guest/isolateInstanceForDestructiveAction)

</div>

<div class="method-row">

#### [migrate](/reference/services/SoftLayer_Virtual_Guest/migrate)
Creates a transaction to migrate a virtual guest to a new host. NOTE: Will only migrate if SoftLayer_Virtual_Guest property pendingMigrationFlag = true 
</div>

<div class="method-row">

#### [migrateDedicatedHost](/reference/services/SoftLayer_Virtual_Guest/migrateDedicatedHost)
Migrate a dedicated instance from one dedicated host to another dedicated host 
</div>

<div class="method-row">

#### [mountIsoImage](/reference/services/SoftLayer_Virtual_Guest/mountIsoImage)

</div>

<div class="method-row">

#### [pause](/reference/services/SoftLayer_Virtual_Guest/pause)
Pause a guest.
</div>

<div class="method-row">

#### [powerCycle](/reference/services/SoftLayer_Virtual_Guest/powerCycle)
Power cycle a guest.
</div>

<div class="method-row">

#### [powerOff](/reference/services/SoftLayer_Virtual_Guest/powerOff)
Power off a guest.
</div>

<div class="method-row">

#### [powerOffSoft](/reference/services/SoftLayer_Virtual_Guest/powerOffSoft)
Cleanly shut down a guest and disable power
</div>

<div class="method-row">

#### [powerOn](/reference/services/SoftLayer_Virtual_Guest/powerOn)
Power on a guest.
</div>

<div class="method-row">

#### [rebootDefault](/reference/services/SoftLayer_Virtual_Guest/rebootDefault)
Power cycle a guest.
</div>

<div class="method-row">

#### [rebootHard](/reference/services/SoftLayer_Virtual_Guest/rebootHard)
Power cycle a guest.
</div>

<div class="method-row">

#### [rebootSoft](/reference/services/SoftLayer_Virtual_Guest/rebootSoft)
Attempt to complete a soft reboot of a guest by shutting down the operating system.
</div>

<div class="method-row">

#### [reloadCurrentOperatingSystemConfiguration](/reference/services/SoftLayer_Virtual_Guest/reloadCurrentOperatingSystemConfiguration)
Perform an OS reload
</div>

<div class="method-row">

#### [reloadOperatingSystem](/reference/services/SoftLayer_Virtual_Guest/reloadOperatingSystem)
Reloads operating system configuration.
</div>

<div class="method-row">

#### [removeAccessToNetworkStorage](/reference/services/SoftLayer_Virtual_Guest/removeAccessToNetworkStorage)
Remove access to a SoftLayer_Network_Storage volume from this device. 
</div>

<div class="method-row">

#### [removeAccessToNetworkStorageList](/reference/services/SoftLayer_Virtual_Guest/removeAccessToNetworkStorageList)
Remove access to multiple SoftLayer_Network_Storage volumes from this device. 
</div>

<div class="method-row">

#### [removeTags](/reference/services/SoftLayer_Virtual_Guest/removeTags)
Remove a tag reference
</div>

<div class="method-row">

#### [resume](/reference/services/SoftLayer_Virtual_Guest/resume)
Resume a guest.
</div>

<div class="method-row">

#### [sendTestReclaimScheduledAlert](/reference/services/SoftLayer_Virtual_Guest/sendTestReclaimScheduledAlert)

</div>

<div class="method-row">

#### [setPrivateNetworkInterfaceSpeed](/reference/services/SoftLayer_Virtual_Guest/setPrivateNetworkInterfaceSpeed)
Updates the private network interface (eth0) speed.
</div>

<div class="method-row">

#### [setPublicNetworkInterfaceSpeed](/reference/services/SoftLayer_Virtual_Guest/setPublicNetworkInterfaceSpeed)
Updates the public network interface (eth1) speed.
</div>

<div class="method-row">

#### [setTags](/reference/services/SoftLayer_Virtual_Guest/setTags)

</div>

<div class="method-row">

#### [setTransientWebhook](/reference/services/SoftLayer_Virtual_Guest/setTransientWebhook)

</div>

<div class="method-row">

#### [setUserMetadata](/reference/services/SoftLayer_Virtual_Guest/setUserMetadata)
Configures the guest's metadata disk.
</div>

<div class="method-row">

#### [shutdownPrivatePort](/reference/services/SoftLayer_Virtual_Guest/shutdownPrivatePort)
Shuts down the private port
</div>

<div class="method-row">

#### [shutdownPublicPort](/reference/services/SoftLayer_Virtual_Guest/shutdownPublicPort)
Shuts down the public port
</div>

<div class="method-row">

#### [unmountIsoImage](/reference/services/SoftLayer_Virtual_Guest/unmountIsoImage)

</div>

<div class="method-row">

#### [validateImageTemplate](/reference/services/SoftLayer_Virtual_Guest/validateImageTemplate)
Validates an image template for OS Reload
</div>

<div class="method-row">

#### [verifyReloadOperatingSystem](/reference/services/SoftLayer_Virtual_Guest/verifyReloadOperatingSystem)
Verify that a virtual server can go through the operating system reload process.
</div>
</div>

</div>

