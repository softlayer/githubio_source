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
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [activatePrivatePort](/reference/services/SoftLayer_Virtual_Guest/activatePrivatePort)
Activate the private port

#### [activatePublicPort](/reference/services/SoftLayer_Virtual_Guest/activatePublicPort)
Activate the public port

#### [allowAccessToNetworkStorage](/reference/services/SoftLayer_Virtual_Guest/allowAccessToNetworkStorage)
Allow access to a SoftLayer_Network_Storage volume from this device. 

#### [allowAccessToNetworkStorageList](/reference/services/SoftLayer_Virtual_Guest/allowAccessToNetworkStorageList)
Allow access to multiple SoftLayer_Network_Storage volumes from this device. 

#### [attachDiskImage](/reference/services/SoftLayer_Virtual_Guest/attachDiskImage)
Attaches a disk image.

#### [cancelIsolationForDestructiveAction](/reference/services/SoftLayer_Virtual_Guest/cancelIsolationForDestructiveAction)


#### [captureImage](/reference/services/SoftLayer_Virtual_Guest/captureImage)
Captures a Flex Image of the hard disk on the virtual machine.

#### [checkHostDiskAvailability](/reference/services/SoftLayer_Virtual_Guest/checkHostDiskAvailability)


#### [closeAlarm](/reference/services/SoftLayer_Virtual_Guest/closeAlarm)
Returns monitoring alarm detailed history

#### [configureMetadataDisk](/reference/services/SoftLayer_Virtual_Guest/configureMetadataDisk)
Configures the guest's metadata disk.

#### [createArchiveTransaction](/reference/services/SoftLayer_Virtual_Guest/createArchiveTransaction)
[SoftLayer_Virtual_Guest_Block_Device]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Block_Device">}}) can be grouped together in and backed up in an archive for later use. This method generates a transaction to perform an archive of the provided block devices. 

#### [createObject](/reference/services/SoftLayer_Virtual_Guest/createObject)
Create a new computing instance

#### [createObjects](/reference/services/SoftLayer_Virtual_Guest/createObjects)
Create new computing instances

#### [createPostSoftwareInstallTransaction](/reference/services/SoftLayer_Virtual_Guest/createPostSoftwareInstallTransaction)


#### [deleteObject](/reference/services/SoftLayer_Virtual_Guest/deleteObject)
Delete a computing instance

#### [deleteTag](/reference/services/SoftLayer_Virtual_Guest/deleteTag)
Delete a tag

#### [deleteTransientWebhook](/reference/services/SoftLayer_Virtual_Guest/deleteTransientWebhook)


#### [detachDiskImage](/reference/services/SoftLayer_Virtual_Guest/detachDiskImage)
Detaches a disk image.

#### [editObject](/reference/services/SoftLayer_Virtual_Guest/editObject)
Edit a computing instance's properties

#### [executeIderaBareMetalRestore](/reference/services/SoftLayer_Virtual_Guest/executeIderaBareMetalRestore)
Reboot a guest into the Idera Bare Metal Restore image.

#### [executeR1SoftBareMetalRestore](/reference/services/SoftLayer_Virtual_Guest/executeR1SoftBareMetalRestore)
Reboot a guest into the R1Soft Bare Metal Restore image.

#### [executeRemoteScript](/reference/services/SoftLayer_Virtual_Guest/executeRemoteScript)
Download and run remote script from uri on the virtual guest. Requires https for script to be executed after download. 

#### [executeRescueLayer](/reference/services/SoftLayer_Virtual_Guest/executeRescueLayer)
Reboot a Linux guest into the Xen rescue image.

#### [findByIpAddress](/reference/services/SoftLayer_Virtual_Guest/findByIpAddress)
Find CCI by its primary public or private IP (ipv4) address.

#### [generateOrderTemplate](/reference/services/SoftLayer_Virtual_Guest/generateOrderTemplate)
Obtain an order container for a given template object

#### [getAccount](/reference/services/SoftLayer_Virtual_Guest/getAccount)
Retrieve the account that a virtual guest belongs to.

#### [getAccountOwnedPoolFlag](/reference/services/SoftLayer_Virtual_Guest/getAccountOwnedPoolFlag)


#### [getActiveNetworkMonitorIncident](/reference/services/SoftLayer_Virtual_Guest/getActiveNetworkMonitorIncident)
Retrieve a virtual guest's currently active network monitoring incidents.

#### [getActiveTickets](/reference/services/SoftLayer_Virtual_Guest/getActiveTickets)


#### [getActiveTransaction](/reference/services/SoftLayer_Virtual_Guest/getActiveTransaction)
Retrieve a transaction that is still be performed on a cloud server.

#### [getActiveTransactions](/reference/services/SoftLayer_Virtual_Guest/getActiveTransactions)
Retrieve any active transaction(s) that are currently running for the server (example: os reload).

#### [getAdditionalRequiredPricesForOsReload](/reference/services/SoftLayer_Virtual_Guest/getAdditionalRequiredPricesForOsReload)
Return a collection of SoftLayer_Item_Price objects for an OS reload

#### [getAlarmHistory](/reference/services/SoftLayer_Virtual_Guest/getAlarmHistory)
Returns monitoring alarm detailed history

#### [getAllowedHost](/reference/services/SoftLayer_Virtual_Guest/getAllowedHost)
Retrieve the SoftLayer_Network_Storage_Allowed_Host information to connect this Virtual Guest to Network Storage volumes that require access control lists.

#### [getAllowedNetworkStorage](/reference/services/SoftLayer_Virtual_Guest/getAllowedNetworkStorage)
Retrieve the SoftLayer_Network_Storage objects that this SoftLayer_Virtual_Guest has access to.

#### [getAllowedNetworkStorageReplicas](/reference/services/SoftLayer_Virtual_Guest/getAllowedNetworkStorageReplicas)
Retrieve the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Virtual_Guest has access to.

#### [getAntivirusSpywareSoftwareComponent](/reference/services/SoftLayer_Virtual_Guest/getAntivirusSpywareSoftwareComponent)
Retrieve a antivirus / spyware software component object.

#### [getApplicationDeliveryController](/reference/services/SoftLayer_Virtual_Guest/getApplicationDeliveryController)


#### [getAttachedNetworkStorages](/reference/services/SoftLayer_Virtual_Guest/getAttachedNetworkStorages)
Return a list of SoftLayer_Network_Storage volumes authorized to this device. 

#### [getAttributes](/reference/services/SoftLayer_Virtual_Guest/getAttributes)


#### [getAvailableBlockDevicePositions](/reference/services/SoftLayer_Virtual_Guest/getAvailableBlockDevicePositions)


#### [getAvailableMonitoring](/reference/services/SoftLayer_Virtual_Guest/getAvailableMonitoring)
Retrieve an object that stores the maximum level for the monitoring query types and response types.

#### [getAvailableNetworkStorages](/reference/services/SoftLayer_Virtual_Guest/getAvailableNetworkStorages)
Return a list of SoftLayer_Network_Storage volumes that can be authorized to this device. 

#### [getAverageDailyPrivateBandwidthUsage](/reference/services/SoftLayer_Virtual_Guest/getAverageDailyPrivateBandwidthUsage)
Retrieve the average daily private bandwidth usage for the current billing cycle.

#### [getAverageDailyPublicBandwidthUsage](/reference/services/SoftLayer_Virtual_Guest/getAverageDailyPublicBandwidthUsage)
Retrieve the average daily public bandwidth usage for the current billing cycle.

#### [getBackendNetworkComponents](/reference/services/SoftLayer_Virtual_Guest/getBackendNetworkComponents)
Retrieve a guests's backend network components.

#### [getBackendRouters](/reference/services/SoftLayer_Virtual_Guest/getBackendRouters)
Retrieve a guest's backend or private router.

#### [getBandwidthAllocation](/reference/services/SoftLayer_Virtual_Guest/getBandwidthAllocation)
Retrieve a computing instance's allotted bandwidth (measured in GB).

#### [getBandwidthAllotmentDetail](/reference/services/SoftLayer_Virtual_Guest/getBandwidthAllotmentDetail)
Retrieve a computing instance's allotted detail record. Allotment details link bandwidth allocation with allotments.

#### [getBandwidthDataByDate](/reference/services/SoftLayer_Virtual_Guest/getBandwidthDataByDate)
Retrieve the amount of network traffic that occurred for the specified time frame for a computing instance. 

#### [getBandwidthForDateRange](/reference/services/SoftLayer_Virtual_Guest/getBandwidthForDateRange)
Retrieve bandwidth data from a tracking object.

#### [getBandwidthImage](/reference/services/SoftLayer_Virtual_Guest/getBandwidthImage)
Retrieve a visual representation of the amount of network traffic that occurred for the specified time frame for a computing instance. 

#### [getBandwidthImageByDate](/reference/services/SoftLayer_Virtual_Guest/getBandwidthImageByDate)
Retrieve a visual representation of the amount of network traffic that occurred for the specified time frame for a computing instance. 

#### [getBandwidthTotal](/reference/services/SoftLayer_Virtual_Guest/getBandwidthTotal)
Retrieve total amount of network traffic that was in use during the time specified by the input parameters for a computing instance. 

#### [getBillingCycleBandwidthUsage](/reference/services/SoftLayer_Virtual_Guest/getBillingCycleBandwidthUsage)
Retrieve the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this server is attached to.

#### [getBillingCyclePrivateBandwidthUsage](/reference/services/SoftLayer_Virtual_Guest/getBillingCyclePrivateBandwidthUsage)
Retrieve the raw private bandwidth usage data for the current billing cycle.

#### [getBillingCyclePublicBandwidthUsage](/reference/services/SoftLayer_Virtual_Guest/getBillingCyclePublicBandwidthUsage)
Retrieve the raw public bandwidth usage data for the current billing cycle.

#### [getBillingItem](/reference/services/SoftLayer_Virtual_Guest/getBillingItem)
Retrieve the billing item for a CloudLayer Compute Instance.

#### [getBlockCancelBecauseDisconnectedFlag](/reference/services/SoftLayer_Virtual_Guest/getBlockCancelBecauseDisconnectedFlag)
Retrieve determines whether the instance is ineligible for cancellation because it is disconnected.

#### [getBlockDeviceTemplateGroup](/reference/services/SoftLayer_Virtual_Guest/getBlockDeviceTemplateGroup)
Retrieve the global identifier for the image template that was used to provision or reload a guest.

#### [getBlockDevices](/reference/services/SoftLayer_Virtual_Guest/getBlockDevices)
Retrieve a computing instance's block devices. Block devices link [SoftLayer_Virtual_Disk_Image]({{<ref "reference/datatypes/SoftLayer_Virtual_Disk_Image">}}) to computing instances.

#### [getBootMode](/reference/services/SoftLayer_Virtual_Guest/getBootMode)
Retrieves the boot mode of the VSI.

#### [getBootOrder](/reference/services/SoftLayer_Virtual_Guest/getBootOrder)


#### [getConsoleAccessLog](/reference/services/SoftLayer_Virtual_Guest/getConsoleAccessLog)
get console access logs

#### [getConsoleIpAddressFlag](/reference/services/SoftLayer_Virtual_Guest/getConsoleIpAddressFlag)
Retrieve a flag indicating a computing instance's console IP address is assigned.

#### [getConsoleIpAddressRecord](/reference/services/SoftLayer_Virtual_Guest/getConsoleIpAddressRecord)
Retrieve a record containing information about a computing instance's console IP and port number.

#### [getContinuousDataProtectionSoftwareComponent](/reference/services/SoftLayer_Virtual_Guest/getContinuousDataProtectionSoftwareComponent)
Retrieve a continuous data protection software component object.

#### [getControlPanel](/reference/services/SoftLayer_Virtual_Guest/getControlPanel)
Retrieve a guest's control panel.

#### [getCoreRestrictedOperatingSystemPrice](/reference/services/SoftLayer_Virtual_Guest/getCoreRestrictedOperatingSystemPrice)
Return the associated core-restricted operating system item price for the virtual server.

#### [getCpuMetricDataByDate](/reference/services/SoftLayer_Virtual_Guest/getCpuMetricDataByDate)
Retrieve records containing the percentage of the amount of time that a cpu was in use for the specified time frame for a computing instance. 

#### [getCpuMetricImage](/reference/services/SoftLayer_Virtual_Guest/getCpuMetricImage)
Retrieve a visual representation of the percentage of the amount of time that a cpu was in use for the specified time frame for a computing instance. 

#### [getCpuMetricImageByDate](/reference/services/SoftLayer_Virtual_Guest/getCpuMetricImageByDate)
Retrieve a visual representation of the percentage of the amount of time that a cpu was in use for the specified time frame for a computing instance. 

#### [getCreateObjectOptions](/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions)
Determine options available when creating a computing instance

#### [getCurrentBandwidthSummary](/reference/services/SoftLayer_Virtual_Guest/getCurrentBandwidthSummary)
Retrieve an object that provides commonly used bandwidth summary components for the current billing cycle.

#### [getCurrentBillingDetail](/reference/services/SoftLayer_Virtual_Guest/getCurrentBillingDetail)
<< EOT

#### [getCurrentBillingTotal](/reference/services/SoftLayer_Virtual_Guest/getCurrentBillingTotal)
Get the billing total for this instance's usage up to this point. This total includes all bandwidth charges. 

#### [getCustomBandwidthDataByDate](/reference/services/SoftLayer_Virtual_Guest/getCustomBandwidthDataByDate)
Retrieve bandwidth graph by date.

#### [getCustomMetricDataByDate](/reference/services/SoftLayer_Virtual_Guest/getCustomMetricDataByDate)
Retrieve bandwidth graph by date.

#### [getDatacenter](/reference/services/SoftLayer_Virtual_Guest/getDatacenter)
Retrieve the datacenter that a virtual guest resides in.

#### [getDedicatedHost](/reference/services/SoftLayer_Virtual_Guest/getDedicatedHost)
Retrieve the dedicated host associated with this guest.

#### [getDriveRetentionItemPrice](/reference/services/SoftLayer_Virtual_Guest/getDriveRetentionItemPrice)
Return a drive retention SoftLayer_Item_Price object for a guest.

#### [getEvaultNetworkStorage](/reference/services/SoftLayer_Virtual_Guest/getEvaultNetworkStorage)
Retrieve a guest's associated EVault network storage service account.

#### [getFirewallProtectableSubnets](/reference/services/SoftLayer_Virtual_Guest/getFirewallProtectableSubnets)
Get the subnets associated with this CloudLayer computing instance that are protectable by a network component firewall.

#### [getFirewallServiceComponent](/reference/services/SoftLayer_Virtual_Guest/getFirewallServiceComponent)
Retrieve a computing instance's hardware firewall services.

#### [getFirstAvailableBlockDevicePosition](/reference/services/SoftLayer_Virtual_Guest/getFirstAvailableBlockDevicePosition)


#### [getFrontendNetworkComponents](/reference/services/SoftLayer_Virtual_Guest/getFrontendNetworkComponents)
Retrieve a guest's frontend network components.

#### [getFrontendRouters](/reference/services/SoftLayer_Virtual_Guest/getFrontendRouters)
Retrieve a guest's frontend or public router.

#### [getGlobalIdentifier](/reference/services/SoftLayer_Virtual_Guest/getGlobalIdentifier)
Retrieve a guest's universally unique identifier.

#### [getGpuCount](/reference/services/SoftLayer_Virtual_Guest/getGpuCount)
Retrieve the number of GPUs attached to the guest.

#### [getGpuType](/reference/services/SoftLayer_Virtual_Guest/getGpuType)
Retrieve the name of the GPU type attached to the guest.

#### [getGuestBootParameter](/reference/services/SoftLayer_Virtual_Guest/getGuestBootParameter)


#### [getHost](/reference/services/SoftLayer_Virtual_Guest/getHost)
Retrieve the virtual host on which a virtual guest resides (available only on private clouds).

#### [getHostIpsSoftwareComponent](/reference/services/SoftLayer_Virtual_Guest/getHostIpsSoftwareComponent)
Retrieve a host IPS software component object.

#### [getHourlyBillingFlag](/reference/services/SoftLayer_Virtual_Guest/getHourlyBillingFlag)
Retrieve a guest's hourly billing status.

#### [getInboundPrivateBandwidthUsage](/reference/services/SoftLayer_Virtual_Guest/getInboundPrivateBandwidthUsage)
Retrieve the total private inbound bandwidth for this computing instance for the current billing cycle.

#### [getInboundPublicBandwidthUsage](/reference/services/SoftLayer_Virtual_Guest/getInboundPublicBandwidthUsage)
Retrieve the total public inbound bandwidth for this computing instance for the current billing cycle.

#### [getInternalTagReferences](/reference/services/SoftLayer_Virtual_Guest/getInternalTagReferences)


#### [getIsoBootImage](/reference/services/SoftLayer_Virtual_Guest/getIsoBootImage)


#### [getItemPricesFromSoftwareDescriptions](/reference/services/SoftLayer_Virtual_Guest/getItemPricesFromSoftwareDescriptions)
Return a collection of SoftLayer_Item_Price objects from a collection of SoftLayer_Software_Description

#### [getLastKnownPowerState](/reference/services/SoftLayer_Virtual_Guest/getLastKnownPowerState)
Retrieve the last known power state of a virtual guest in the event the guest is turned off outside of IMS or has gone offline.

#### [getLastOperatingSystemReload](/reference/services/SoftLayer_Virtual_Guest/getLastOperatingSystemReload)
Retrieve the last transaction that a cloud server's operating system was loaded.

#### [getLastTransaction](/reference/services/SoftLayer_Virtual_Guest/getLastTransaction)
Retrieve the last transaction a cloud server had performed.

#### [getLatestNetworkMonitorIncident](/reference/services/SoftLayer_Virtual_Guest/getLatestNetworkMonitorIncident)
Retrieve a virtual guest's latest network monitoring incident.

#### [getLocalDiskFlag](/reference/services/SoftLayer_Virtual_Guest/getLocalDiskFlag)
Retrieve a flag indicating that the virtual guest has at least one disk which is local to the host it runs on. This does not include a SWAP device.

#### [getLocation](/reference/services/SoftLayer_Virtual_Guest/getLocation)
Retrieve where guest is located within SoftLayer's location hierarchy.

#### [getManagedResourceFlag](/reference/services/SoftLayer_Virtual_Guest/getManagedResourceFlag)
Retrieve a flag indicating that the virtual guest is a managed resource.

#### [getMemoryMetricDataByDate](/reference/services/SoftLayer_Virtual_Guest/getMemoryMetricDataByDate)
Retrieve records containing the amount memory that was used for the specified time frame for a computing instance. 

#### [getMemoryMetricImage](/reference/services/SoftLayer_Virtual_Guest/getMemoryMetricImage)
Retrieve a visual representation of the amount of memory used for the specified time frame for a computing instance. 

#### [getMemoryMetricImageByDate](/reference/services/SoftLayer_Virtual_Guest/getMemoryMetricImageByDate)
Retrieve a visual representation of the amount of memory used for the specified time frame for a computing instance. 

#### [getMetricTrackingObject](/reference/services/SoftLayer_Virtual_Guest/getMetricTrackingObject)
Retrieve a guest's metric tracking object.

#### [getMetricTrackingObjectId](/reference/services/SoftLayer_Virtual_Guest/getMetricTrackingObjectId)
Retrieve the metric tracking object id for this guest.

#### [getMonitoringActiveAlarms](/reference/services/SoftLayer_Virtual_Guest/getMonitoringActiveAlarms)
Returns open monitoring alarms for a given time period

#### [getMonitoringAgents](/reference/services/SoftLayer_Virtual_Guest/getMonitoringAgents)


#### [getMonitoringClosedAlarms](/reference/services/SoftLayer_Virtual_Guest/getMonitoringClosedAlarms)
Returns closed monitoring alarms for a given time period

#### [getMonitoringRobot](/reference/services/SoftLayer_Virtual_Guest/getMonitoringRobot)


#### [getMonitoringServiceComponent](/reference/services/SoftLayer_Virtual_Guest/getMonitoringServiceComponent)
Retrieve a virtual guest's network monitoring services.

#### [getMonitoringServiceEligibilityFlag](/reference/services/SoftLayer_Virtual_Guest/getMonitoringServiceEligibilityFlag)


#### [getMonitoringServiceFlag](/reference/services/SoftLayer_Virtual_Guest/getMonitoringServiceFlag)


#### [getMonitoringUserNotification](/reference/services/SoftLayer_Virtual_Guest/getMonitoringUserNotification)
Retrieve the monitoring notification objects for this guest. Each object links this guest instance to a user account that will be notified if monitoring on this guest object fails

#### [getNetworkComponentFirewallProtectableIpAddresses](/reference/services/SoftLayer_Virtual_Guest/getNetworkComponentFirewallProtectableIpAddresses)
Get the IP addresses associated with this CloudLayer computing instance that are protectable by a network component firewall.

#### [getNetworkComponents](/reference/services/SoftLayer_Virtual_Guest/getNetworkComponents)
Retrieve a guests's network components.

#### [getNetworkMonitorIncidents](/reference/services/SoftLayer_Virtual_Guest/getNetworkMonitorIncidents)
Retrieve all of a virtual guest's network monitoring incidents.

#### [getNetworkMonitors](/reference/services/SoftLayer_Virtual_Guest/getNetworkMonitors)
Retrieve a guests's network monitors.

#### [getNetworkStorage](/reference/services/SoftLayer_Virtual_Guest/getNetworkStorage)
Retrieve a guest's associated network storage accounts.

#### [getNetworkVlans](/reference/services/SoftLayer_Virtual_Guest/getNetworkVlans)
Retrieve the network Vlans that a guest's network components are associated with.

#### [getObject](/reference/services/SoftLayer_Virtual_Guest/getObject)
Retrieve a SoftLayer_Virtual_Guest record.

#### [getOpenCancellationTicket](/reference/services/SoftLayer_Virtual_Guest/getOpenCancellationTicket)
Retrieve an open ticket requesting cancellation of this server, if one exists.

#### [getOperatingSystem](/reference/services/SoftLayer_Virtual_Guest/getOperatingSystem)
Retrieve a guest's operating system.

#### [getOperatingSystemReferenceCode](/reference/services/SoftLayer_Virtual_Guest/getOperatingSystemReferenceCode)
Retrieve a guest's operating system software description.

#### [getOrderTemplate](/reference/services/SoftLayer_Virtual_Guest/getOrderTemplate)
Obtain an order container that is ready to be sent to the [[SoftLayer_Product_Order#placeOrder|SoftLayer_Product_Order::placeOrder]] method.

#### [getOrderedPackageId](/reference/services/SoftLayer_Virtual_Guest/getOrderedPackageId)
Retrieve the original package id provided with the order for a Cloud Computing Instance.

#### [getOutboundPrivateBandwidthUsage](/reference/services/SoftLayer_Virtual_Guest/getOutboundPrivateBandwidthUsage)
Retrieve the total private outbound bandwidth for this computing instance for the current billing cycle.

#### [getOutboundPublicBandwidthUsage](/reference/services/SoftLayer_Virtual_Guest/getOutboundPublicBandwidthUsage)
Retrieve the total public outbound bandwidth for this computing instance for the current billing cycle.

#### [getOverBandwidthAllocationFlag](/reference/services/SoftLayer_Virtual_Guest/getOverBandwidthAllocationFlag)
Retrieve whether the bandwidth usage for this computing instance for the current billing cycle exceeds the allocation.

#### [getPendingMaintenanceActions](/reference/services/SoftLayer_Virtual_Guest/getPendingMaintenanceActions)
Returns a list of all the pending maintenance actions affecting this guest. 

#### [getPendingMigrationFlag](/reference/services/SoftLayer_Virtual_Guest/getPendingMigrationFlag)
Retrieve when true this virtual guest must be migrated using SoftLayer_Virtual_Guest::migrate.

#### [getPlacementGroup](/reference/services/SoftLayer_Virtual_Guest/getPlacementGroup)
Retrieve the placement group that a virtual guest belongs to.

#### [getPowerState](/reference/services/SoftLayer_Virtual_Guest/getPowerState)
Retrieve the current power state of a virtual guest.

#### [getPrimaryBackendIpAddress](/reference/services/SoftLayer_Virtual_Guest/getPrimaryBackendIpAddress)
Retrieve a guest's primary private IP address.

#### [getPrimaryBackendNetworkComponent](/reference/services/SoftLayer_Virtual_Guest/getPrimaryBackendNetworkComponent)
Retrieve a guest's primary backend network component.

#### [getPrimaryIpAddress](/reference/services/SoftLayer_Virtual_Guest/getPrimaryIpAddress)
Retrieve the guest's primary public IP address.

#### [getPrimaryNetworkComponent](/reference/services/SoftLayer_Virtual_Guest/getPrimaryNetworkComponent)
Retrieve a guest's primary public network component.

#### [getPrivateNetworkOnlyFlag](/reference/services/SoftLayer_Virtual_Guest/getPrivateNetworkOnlyFlag)
Retrieve whether the computing instance only has access to the private network.

#### [getProjectedOverBandwidthAllocationFlag](/reference/services/SoftLayer_Virtual_Guest/getProjectedOverBandwidthAllocationFlag)
Retrieve whether the bandwidth usage for this computing instance for the current billing cycle is projected to exceed the allocation.

#### [getProjectedPublicBandwidthUsage](/reference/services/SoftLayer_Virtual_Guest/getProjectedPublicBandwidthUsage)
Retrieve the projected public outbound bandwidth for this computing instance for the current billing cycle.

#### [getProvisionDate](/reference/services/SoftLayer_Virtual_Guest/getProvisionDate)


#### [getRecentEvents](/reference/services/SoftLayer_Virtual_Guest/getRecentEvents)
Retrieve recent events that impact this computing instance.

#### [getRecentMetricData](/reference/services/SoftLayer_Virtual_Guest/getRecentMetricData)
Recent metric data for a guest 

#### [getRegionalGroup](/reference/services/SoftLayer_Virtual_Guest/getRegionalGroup)
Retrieve the regional group this guest is in.

#### [getRegionalInternetRegistry](/reference/services/SoftLayer_Virtual_Guest/getRegionalInternetRegistry)


#### [getRemoteMonitoringActiveAlarms](/reference/services/SoftLayer_Virtual_Guest/getRemoteMonitoringActiveAlarms)
Returns open monitoring alarms for a given time period

#### [getRemoteMonitoringClosedAlarms](/reference/services/SoftLayer_Virtual_Guest/getRemoteMonitoringClosedAlarms)
Returns closed monitoring alarms for a given time period

#### [getReservedCapacityGroup](/reference/services/SoftLayer_Virtual_Guest/getReservedCapacityGroup)
Retrieve the reserved capacity group the guest is associated with.

#### [getReservedCapacityGroupFlag](/reference/services/SoftLayer_Virtual_Guest/getReservedCapacityGroupFlag)
Retrieve flag to indicate whether or not a guest is part of a reserved capacity group.

#### [getReservedCapacityGroupInstance](/reference/services/SoftLayer_Virtual_Guest/getReservedCapacityGroupInstance)
Retrieve the reserved capacity group instance the guest is associated with.

#### [getReverseDomainRecords](/reference/services/SoftLayer_Virtual_Guest/getReverseDomainRecords)
Retrieve the reverse domain records associated with a server.

#### [getScaleAssets](/reference/services/SoftLayer_Virtual_Guest/getScaleAssets)
Retrieve collection of scale assets this guest corresponds to.

#### [getScaleMember](/reference/services/SoftLayer_Virtual_Guest/getScaleMember)
Retrieve the scale member for this guest, if applicable.

#### [getScaledFlag](/reference/services/SoftLayer_Virtual_Guest/getScaledFlag)
Retrieve whether or not this guest is a member of a scale group and was automatically created as part of a scale group action.

#### [getSecurityScanRequests](/reference/services/SoftLayer_Virtual_Guest/getSecurityScanRequests)
Retrieve a guest's vulnerability scan requests.

#### [getServerRoom](/reference/services/SoftLayer_Virtual_Guest/getServerRoom)
Retrieve the server room that a guest is located at. There may be more than one server room for every data center.

#### [getSoftwareComponents](/reference/services/SoftLayer_Virtual_Guest/getSoftwareComponents)
Retrieve a guest's installed software.

#### [getSshKeys](/reference/services/SoftLayer_Virtual_Guest/getSshKeys)
Retrieve sSH keys to be installed on the server during provisioning or an OS reload.

#### [getStatus](/reference/services/SoftLayer_Virtual_Guest/getStatus)
Retrieve a computing instance's status.

#### [getTagReferences](/reference/services/SoftLayer_Virtual_Guest/getTagReferences)


#### [getTransientGuestFlag](/reference/services/SoftLayer_Virtual_Guest/getTransientGuestFlag)
Retrieve whether or not a computing instance is a Transient Instance.

#### [getTransientWebhookURI](/reference/services/SoftLayer_Virtual_Guest/getTransientWebhookURI)
Retrieve the endpoint used to notify customers their transient guest is terminating.

#### [getType](/reference/services/SoftLayer_Virtual_Guest/getType)
Retrieve the type of this virtual guest.

#### [getUpgradeItemPrices](/reference/services/SoftLayer_Virtual_Guest/getUpgradeItemPrices)
Retrieve a computing instance's upgradeable items.

#### [getUpgradeRequest](/reference/services/SoftLayer_Virtual_Guest/getUpgradeRequest)
Retrieve a computing instance's associated upgrade request object if any.

#### [getUserData](/reference/services/SoftLayer_Virtual_Guest/getUserData)
Retrieve a base64 encoded string containing custom user data for a Cloud Computing Instance order.

#### [getUsers](/reference/services/SoftLayer_Virtual_Guest/getUsers)
Retrieve a list of users that have access to this computing instance.

#### [getValidBlockDeviceTemplateGroups](/reference/services/SoftLayer_Virtual_Guest/getValidBlockDeviceTemplateGroups)
Return a list of valid block device template groups based on this host

#### [getVirtualRack](/reference/services/SoftLayer_Virtual_Guest/getVirtualRack)
Retrieve the name of the bandwidth allotment that a hardware belongs too.

#### [getVirtualRackId](/reference/services/SoftLayer_Virtual_Guest/getVirtualRackId)
Retrieve the id of the bandwidth allotment that a computing instance belongs too.

#### [getVirtualRackName](/reference/services/SoftLayer_Virtual_Guest/getVirtualRackName)
Retrieve the name of the bandwidth allotment that a computing instance belongs too.

#### [isBackendPingable](/reference/services/SoftLayer_Virtual_Guest/isBackendPingable)
Verifies if a guest's backend ip address is pingable.

#### [isPingable](/reference/services/SoftLayer_Virtual_Guest/isPingable)
Verifies if guest is pingable.

#### [isolateInstanceForDestructiveAction](/reference/services/SoftLayer_Virtual_Guest/isolateInstanceForDestructiveAction)


#### [migrate](/reference/services/SoftLayer_Virtual_Guest/migrate)
Creates a transaction to migrate a virtual guest to a new host. NOTE: Will only migrate if SoftLayer_Virtual_Guest property pendingMigrationFlag = true 

#### [migrateDedicatedHost](/reference/services/SoftLayer_Virtual_Guest/migrateDedicatedHost)
Migrate a dedicated instance from one dedicated host to another dedicated host 

#### [mountIsoImage](/reference/services/SoftLayer_Virtual_Guest/mountIsoImage)


#### [pause](/reference/services/SoftLayer_Virtual_Guest/pause)
Pause a guest.

#### [powerCycle](/reference/services/SoftLayer_Virtual_Guest/powerCycle)
Power cycle a guest.

#### [powerOff](/reference/services/SoftLayer_Virtual_Guest/powerOff)
Power off a guest.

#### [powerOffSoft](/reference/services/SoftLayer_Virtual_Guest/powerOffSoft)
Cleanly shut down a guest and disable power

#### [powerOn](/reference/services/SoftLayer_Virtual_Guest/powerOn)
Power on a guest.

#### [rebootDefault](/reference/services/SoftLayer_Virtual_Guest/rebootDefault)
Power cycle a guest.

#### [rebootHard](/reference/services/SoftLayer_Virtual_Guest/rebootHard)
Power cycle a guest.

#### [rebootSoft](/reference/services/SoftLayer_Virtual_Guest/rebootSoft)
Attempt to complete a soft reboot of a guest by shutting down the operating system.

#### [reloadCurrentOperatingSystemConfiguration](/reference/services/SoftLayer_Virtual_Guest/reloadCurrentOperatingSystemConfiguration)
Perform an OS reload

#### [reloadOperatingSystem](/reference/services/SoftLayer_Virtual_Guest/reloadOperatingSystem)
Reloads operating system configuration.

#### [removeAccessToNetworkStorage](/reference/services/SoftLayer_Virtual_Guest/removeAccessToNetworkStorage)
Remove access to a SoftLayer_Network_Storage volume from this device. 

#### [removeAccessToNetworkStorageList](/reference/services/SoftLayer_Virtual_Guest/removeAccessToNetworkStorageList)
Remove access to multiple SoftLayer_Network_Storage volumes from this device. 

#### [removeTags](/reference/services/SoftLayer_Virtual_Guest/removeTags)
Remove a tag reference

#### [resume](/reference/services/SoftLayer_Virtual_Guest/resume)
Resume a guest.

#### [sendTestReclaimScheduledAlert](/reference/services/SoftLayer_Virtual_Guest/sendTestReclaimScheduledAlert)


#### [setPrivateNetworkInterfaceSpeed](/reference/services/SoftLayer_Virtual_Guest/setPrivateNetworkInterfaceSpeed)
Updates the private network interface (eth0) speed.

#### [setPublicNetworkInterfaceSpeed](/reference/services/SoftLayer_Virtual_Guest/setPublicNetworkInterfaceSpeed)
Updates the public network interface (eth1) speed.

#### [setTags](/reference/services/SoftLayer_Virtual_Guest/setTags)


#### [setTransientWebhook](/reference/services/SoftLayer_Virtual_Guest/setTransientWebhook)


#### [setUserMetadata](/reference/services/SoftLayer_Virtual_Guest/setUserMetadata)
Configures the guest's metadata disk.

#### [shutdownPrivatePort](/reference/services/SoftLayer_Virtual_Guest/shutdownPrivatePort)
Shuts down the private port

#### [shutdownPublicPort](/reference/services/SoftLayer_Virtual_Guest/shutdownPublicPort)
Shuts down the public port

#### [unmountIsoImage](/reference/services/SoftLayer_Virtual_Guest/unmountIsoImage)


#### [validateImageTemplate](/reference/services/SoftLayer_Virtual_Guest/validateImageTemplate)
Validates an image template for OS Reload

#### [verifyReloadOperatingSystem](/reference/services/SoftLayer_Virtual_Guest/verifyReloadOperatingSystem)
Verify that a virtual server can go through the operating system reload process.

</div>

