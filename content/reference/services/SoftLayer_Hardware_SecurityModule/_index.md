---
title: "SoftLayer_Hardware_SecurityModule"
description: ""
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
---
# SoftLayer_Hardware_SecurityModule
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Hardware_SecurityModule' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_SecurityModule' >Datatype</a></li>
    </ul>
</div>

## Description




### seeAlso

* [SoftLayer_Hardware](/reference/services/SoftLayer_Hardware )


        
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

#### [activatePrivatePort](/reference/services/SoftLayer_Hardware_SecurityModule/activatePrivatePort)
Activate a server's private network interface.
</div>

<div class="method-row">

#### [activatePublicPort](/reference/services/SoftLayer_Hardware_SecurityModule/activatePublicPort)
Activate a server's public network interface.
</div>

<div class="method-row">

#### [allowAccessToNetworkStorage](/reference/services/SoftLayer_Hardware_SecurityModule/allowAccessToNetworkStorage)
Allow access to a SoftLayer_Network_Storage volume from this device. 
</div>

<div class="method-row">

#### [allowAccessToNetworkStorageList](/reference/services/SoftLayer_Hardware_SecurityModule/allowAccessToNetworkStorageList)
Allow access to multiple SoftLayer_Network_Storage volumes from this device. 
</div>

<div class="method-row">

#### [bootToRescueLayer](/reference/services/SoftLayer_Hardware_SecurityModule/bootToRescueLayer)
Initiates the Rescue Kernel to bring a server online to troubleshoot system problems.
</div>

<div class="method-row">

#### [captureImage](/reference/services/SoftLayer_Hardware_SecurityModule/captureImage)
Captures an Image of the hard disk on the physical machine.
</div>

<div class="method-row">

#### [createFirmwareReflashTransaction](/reference/services/SoftLayer_Hardware_SecurityModule/createFirmwareReflashTransaction)
Runs firmware reflash on the servers components.
</div>

<div class="method-row">

#### [createFirmwareUpdateTransaction](/reference/services/SoftLayer_Hardware_SecurityModule/createFirmwareUpdateTransaction)
Runs firmware updates on the servers components.
</div>

<div class="method-row">

#### [createHyperThreadingUpdateTransaction](/reference/services/SoftLayer_Hardware_SecurityModule/createHyperThreadingUpdateTransaction)
Runs BIOS update on the server to change the hyper-threading configuration.
</div>

<div class="method-row">

#### [createObject](/reference/services/SoftLayer_Hardware_SecurityModule/createObject)
Create a new server
</div>

<div class="method-row">

#### [createPostSoftwareInstallTransaction](/reference/services/SoftLayer_Hardware_SecurityModule/createPostSoftwareInstallTransaction)

</div>

<div class="method-row">

#### [deleteObject](/reference/services/SoftLayer_Hardware_SecurityModule/deleteObject)
Delete a server
</div>

<div class="method-row">

#### [deleteSoftwareComponentPasswords](/reference/services/SoftLayer_Hardware_SecurityModule/deleteSoftwareComponentPasswords)
Delete software component passwords.
</div>

<div class="method-row">

#### [deleteTag](/reference/services/SoftLayer_Hardware_SecurityModule/deleteTag)
Delete a tag
</div>

<div class="method-row">

#### [editObject](/reference/services/SoftLayer_Hardware_SecurityModule/editObject)
Edit a server's properties
</div>

<div class="method-row">

#### [editSoftwareComponentPasswords](/reference/services/SoftLayer_Hardware_SecurityModule/editSoftwareComponentPasswords)
Edit the properties of software component passwords.
</div>

<div class="method-row">

#### [executeRemoteScript](/reference/services/SoftLayer_Hardware_SecurityModule/executeRemoteScript)
Download and run remote script from uri on the hardware. Requires https for script to be executed after download. 
</div>

<div class="method-row">

#### [findByIpAddress](/reference/services/SoftLayer_Hardware_SecurityModule/findByIpAddress)
Find hardware by its primary public or private IP (ipv4) address.
</div>

<div class="method-row">

#### [generateOrderTemplate](/reference/services/SoftLayer_Hardware_SecurityModule/generateOrderTemplate)
Obtain an order container for a given template object
</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Hardware_SecurityModule/getAccount)
Retrieve the account associated with a piece of hardware.
</div>

<div class="method-row">

#### [getActiveComponents](/reference/services/SoftLayer_Hardware_SecurityModule/getActiveComponents)
Retrieve a piece of hardware's active physical components.
</div>

<div class="method-row">

#### [getActiveNetworkFirewallBillingItem](/reference/services/SoftLayer_Hardware_SecurityModule/getActiveNetworkFirewallBillingItem)
Retrieve the billing item for a server's attached network firewall.
</div>

<div class="method-row">

#### [getActiveNetworkMonitorIncident](/reference/services/SoftLayer_Hardware_SecurityModule/getActiveNetworkMonitorIncident)
Retrieve a piece of hardware's active network monitoring incidents.
</div>

<div class="method-row">

#### [getActiveTickets](/reference/services/SoftLayer_Hardware_SecurityModule/getActiveTickets)

</div>

<div class="method-row">

#### [getActiveTransaction](/reference/services/SoftLayer_Hardware_SecurityModule/getActiveTransaction)
Retrieve transaction currently running for server.
</div>

<div class="method-row">

#### [getActiveTransactions](/reference/services/SoftLayer_Hardware_SecurityModule/getActiveTransactions)
Retrieve any active transaction(s) that are currently running for the server (example: os reload).
</div>

<div class="method-row">

#### [getAllPowerComponents](/reference/services/SoftLayer_Hardware_SecurityModule/getAllPowerComponents)

</div>

<div class="method-row">

#### [getAllowedHost](/reference/services/SoftLayer_Hardware_SecurityModule/getAllowedHost)
Retrieve the SoftLayer_Network_Storage_Allowed_Host information to connect this server to Network Storage volumes that require access control lists.
</div>

<div class="method-row">

#### [getAllowedNetworkStorage](/reference/services/SoftLayer_Hardware_SecurityModule/getAllowedNetworkStorage)
Retrieve the SoftLayer_Network_Storage objects that this SoftLayer_Hardware has access to.
</div>

<div class="method-row">

#### [getAllowedNetworkStorageReplicas](/reference/services/SoftLayer_Hardware_SecurityModule/getAllowedNetworkStorageReplicas)
Retrieve the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to.
</div>

<div class="method-row">

#### [getAntivirusSpywareSoftwareComponent](/reference/services/SoftLayer_Hardware_SecurityModule/getAntivirusSpywareSoftwareComponent)
Retrieve information regarding an antivirus/spyware software component object.
</div>

<div class="method-row">

#### [getAttachedNetworkStorages](/reference/services/SoftLayer_Hardware_SecurityModule/getAttachedNetworkStorages)
Return a list of SoftLayer_Network_Storage volumes authorized to this device. 
</div>

<div class="method-row">

#### [getAttributes](/reference/services/SoftLayer_Hardware_SecurityModule/getAttributes)
Retrieve information regarding a piece of hardware's specific attributes.
</div>

<div class="method-row">

#### [getAvailableMonitoring](/reference/services/SoftLayer_Hardware_SecurityModule/getAvailableMonitoring)
Retrieve an object that stores the maximum level for the monitoring query types and response types.
</div>

<div class="method-row">

#### [getAvailableNetworkStorages](/reference/services/SoftLayer_Hardware_SecurityModule/getAvailableNetworkStorages)
Return a list of SoftLayer_Network_Storage volumes that can be authorized to this device. 
</div>

<div class="method-row">

#### [getAverageDailyBandwidthUsage](/reference/services/SoftLayer_Hardware_SecurityModule/getAverageDailyBandwidthUsage)
Retrieve the average daily total bandwidth usage for the current billing cycle.
</div>

<div class="method-row">

#### [getAverageDailyPrivateBandwidthUsage](/reference/services/SoftLayer_Hardware_SecurityModule/getAverageDailyPrivateBandwidthUsage)
Retrieve the average daily private bandwidth usage for the current billing cycle.
</div>

<div class="method-row">

#### [getAverageDailyPublicBandwidthUsage](/reference/services/SoftLayer_Hardware_SecurityModule/getAverageDailyPublicBandwidthUsage)
Retrieve the average daily public bandwidth usage for the current billing cycle.
</div>

<div class="method-row">

#### [getBackendBandwidthUsage](/reference/services/SoftLayer_Hardware_SecurityModule/getBackendBandwidthUsage)
Retrieves public bandwidth usage records.
</div>

<div class="method-row">

#### [getBackendBandwidthUse](/reference/services/SoftLayer_Hardware_SecurityModule/getBackendBandwidthUse)
Retrieves private bandwidth usage records.
</div>

<div class="method-row">

#### [getBackendIncomingBandwidth](/reference/services/SoftLayer_Hardware_SecurityModule/getBackendIncomingBandwidth)
Retrieve the amount of incoming private network bandwidth used by a server over a period of time. 
</div>

<div class="method-row">

#### [getBackendNetworkComponents](/reference/services/SoftLayer_Hardware_SecurityModule/getBackendNetworkComponents)
Retrieve a piece of hardware's back-end or private network components.
</div>

<div class="method-row">

#### [getBackendOutgoingBandwidth](/reference/services/SoftLayer_Hardware_SecurityModule/getBackendOutgoingBandwidth)
Retrieve the amount of outgoing private network bandwidth used by a server over a period of time. 
</div>

<div class="method-row">

#### [getBackendRouters](/reference/services/SoftLayer_Hardware_SecurityModule/getBackendRouters)
Retrieve a hardware's backend or private router.
</div>

<div class="method-row">

#### [getBandwidthAllocation](/reference/services/SoftLayer_Hardware_SecurityModule/getBandwidthAllocation)
Retrieve a hardware's allotted bandwidth (measured in GB).
</div>

<div class="method-row">

#### [getBandwidthAllotmentDetail](/reference/services/SoftLayer_Hardware_SecurityModule/getBandwidthAllotmentDetail)
Retrieve a hardware's allotted detail record. Allotment details link bandwidth allocation with allotments.
</div>

<div class="method-row">

#### [getBandwidthForDateRange](/reference/services/SoftLayer_Hardware_SecurityModule/getBandwidthForDateRange)
Retrieve bandwidth data from a tracking object.
</div>

<div class="method-row">

#### [getBandwidthImage](/reference/services/SoftLayer_Hardware_SecurityModule/getBandwidthImage)
Retrieve a bandwidth image and textual description of that image for this server.
</div>

<div class="method-row">

#### [getBenchmarkCertifications](/reference/services/SoftLayer_Hardware_SecurityModule/getBenchmarkCertifications)
Retrieve information regarding a piece of hardware's benchmark certifications.
</div>

<div class="method-row">

#### [getBillingCycleBandwidthUsage](/reference/services/SoftLayer_Hardware_SecurityModule/getBillingCycleBandwidthUsage)
Retrieve the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this server is attached to.
</div>

<div class="method-row">

#### [getBillingCyclePrivateBandwidthUsage](/reference/services/SoftLayer_Hardware_SecurityModule/getBillingCyclePrivateBandwidthUsage)
Retrieve the raw private bandwidth usage data for the current billing cycle.
</div>

<div class="method-row">

#### [getBillingCyclePublicBandwidthUsage](/reference/services/SoftLayer_Hardware_SecurityModule/getBillingCyclePublicBandwidthUsage)
Retrieve the raw public bandwidth usage data for the current billing cycle.
</div>

<div class="method-row">

#### [getBillingItem](/reference/services/SoftLayer_Hardware_SecurityModule/getBillingItem)
Retrieve information regarding the billing item for a server.
</div>

<div class="method-row">

#### [getBillingItemFlag](/reference/services/SoftLayer_Hardware_SecurityModule/getBillingItemFlag)
Retrieve a flag indicating that a billing item exists.
</div>

<div class="method-row">

#### [getBiosPasswordNullFlag](/reference/services/SoftLayer_Hardware_SecurityModule/getBiosPasswordNullFlag)
Retrieve determine if BIOS password should be left as null.
</div>

<div class="method-row">

#### [getBlockCancelBecauseDisconnectedFlag](/reference/services/SoftLayer_Hardware_SecurityModule/getBlockCancelBecauseDisconnectedFlag)
Retrieve determines whether the hardware is ineligible for cancellation because it is disconnected.
</div>

<div class="method-row">

#### [getBootModeOptions](/reference/services/SoftLayer_Hardware_SecurityModule/getBootModeOptions)
Retrieve the valid boot modes for this server.
</div>

<div class="method-row">

#### [getBusinessContinuanceInsuranceFlag](/reference/services/SoftLayer_Hardware_SecurityModule/getBusinessContinuanceInsuranceFlag)
Retrieve status indicating whether or not a piece of hardware has business continuance insurance.
</div>

<div class="method-row">

#### [getCaptureEnabledFlag](/reference/services/SoftLayer_Hardware_SecurityModule/getCaptureEnabledFlag)
Retrieve determine if the server is able to be image captured. If unable to image capture a reason will be provided.
</div>

<div class="method-row">

#### [getChildrenHardware](/reference/services/SoftLayer_Hardware_SecurityModule/getChildrenHardware)
Retrieve child hardware.
</div>

<div class="method-row">

#### [getComponentDetailsXML](/reference/services/SoftLayer_Hardware_SecurityModule/getComponentDetailsXML)

</div>

<div class="method-row">

#### [getComponents](/reference/services/SoftLayer_Hardware_SecurityModule/getComponents)
Retrieve a piece of hardware's components.
</div>

<div class="method-row">

#### [getContainsSolidStateDrivesFlag](/reference/services/SoftLayer_Hardware_SecurityModule/getContainsSolidStateDrivesFlag)

</div>

<div class="method-row">

#### [getContinuousDataProtectionSoftwareComponent](/reference/services/SoftLayer_Hardware_SecurityModule/getContinuousDataProtectionSoftwareComponent)
Retrieve a continuous data protection/server backup software component object.
</div>

<div class="method-row">

#### [getControlPanel](/reference/services/SoftLayer_Hardware_SecurityModule/getControlPanel)
Retrieve a server's control panel.
</div>

<div class="method-row">

#### [getCost](/reference/services/SoftLayer_Hardware_SecurityModule/getCost)
Retrieve the total cost of a server, measured in US Dollars ($USD).
</div>

<div class="method-row">

#### [getCreateObjectOptions](/reference/services/SoftLayer_Hardware_SecurityModule/getCreateObjectOptions)
Determine options available when creating a server
</div>

<div class="method-row">

#### [getCurrentBandwidthSummary](/reference/services/SoftLayer_Hardware_SecurityModule/getCurrentBandwidthSummary)
Retrieve an object that provides commonly used bandwidth summary components for the current billing cycle.
</div>

<div class="method-row">

#### [getCurrentBenchmarkCertificationResultFile](/reference/services/SoftLayer_Hardware_SecurityModule/getCurrentBenchmarkCertificationResultFile)
Get the file for the current benchmark certification result, if it exists.
</div>

<div class="method-row">

#### [getCurrentBillableBandwidthUsage](/reference/services/SoftLayer_Hardware_SecurityModule/getCurrentBillableBandwidthUsage)
Retrieve the current billable public outbound bandwidth for this hardware for the current billing cycle.
</div>

<div class="method-row">

#### [getCurrentBillingDetail](/reference/services/SoftLayer_Hardware_SecurityModule/getCurrentBillingDetail)
<< EOT
</div>

<div class="method-row">

#### [getCurrentBillingTotal](/reference/services/SoftLayer_Hardware_SecurityModule/getCurrentBillingTotal)
Get the billing total for this instance's usage up to this point. This total includes all bandwidth charges. 
</div>

<div class="method-row">

#### [getCustomBandwidthDataByDate](/reference/services/SoftLayer_Hardware_SecurityModule/getCustomBandwidthDataByDate)
Retrieve bandwidth graph by date.
</div>

<div class="method-row">

#### [getCustomerInstalledOperatingSystemFlag](/reference/services/SoftLayer_Hardware_SecurityModule/getCustomerInstalledOperatingSystemFlag)
Retrieve indicates if a server has a Customer Installed OS
</div>

<div class="method-row">

#### [getCustomerOwnedFlag](/reference/services/SoftLayer_Hardware_SecurityModule/getCustomerOwnedFlag)
Retrieve indicates if a server is a customer owned device.
</div>

<div class="method-row">

#### [getDailyAverage](/reference/services/SoftLayer_Hardware_SecurityModule/getDailyAverage)
calculate the average daily network traffic used by a server in gigabytes.
</div>

<div class="method-row">

#### [getDatacenter](/reference/services/SoftLayer_Hardware_SecurityModule/getDatacenter)
Retrieve information regarding the datacenter in which a piece of hardware resides.
</div>

<div class="method-row">

#### [getDatacenterName](/reference/services/SoftLayer_Hardware_SecurityModule/getDatacenterName)
Retrieve the name of the datacenter in which a piece of hardware resides.
</div>

<div class="method-row">

#### [getDaysInSparePool](/reference/services/SoftLayer_Hardware_SecurityModule/getDaysInSparePool)
Retrieve number of day(s) a server have been in spare pool.
</div>

<div class="method-row">

#### [getDownlinkHardware](/reference/services/SoftLayer_Hardware_SecurityModule/getDownlinkHardware)
Retrieve all hardware that has uplink network connections to a piece of hardware.
</div>

<div class="method-row">

#### [getDownlinkNetworkHardware](/reference/services/SoftLayer_Hardware_SecurityModule/getDownlinkNetworkHardware)
Retrieve all hardware that has uplink network connections to a piece of hardware.
</div>

<div class="method-row">

#### [getDownlinkServers](/reference/services/SoftLayer_Hardware_SecurityModule/getDownlinkServers)
Retrieve information regarding all servers attached to a piece of network hardware.
</div>

<div class="method-row">

#### [getDownlinkVirtualGuests](/reference/services/SoftLayer_Hardware_SecurityModule/getDownlinkVirtualGuests)
Retrieve information regarding all virtual guests attached to a piece of network hardware.
</div>

<div class="method-row">

#### [getDownstreamHardwareBindings](/reference/services/SoftLayer_Hardware_SecurityModule/getDownstreamHardwareBindings)
Retrieve all hardware downstream from a network device.
</div>

<div class="method-row">

#### [getDownstreamNetworkHardware](/reference/services/SoftLayer_Hardware_SecurityModule/getDownstreamNetworkHardware)
Retrieve all network hardware downstream from the selected piece of hardware.
</div>

<div class="method-row">

#### [getDownstreamNetworkHardwareWithIncidents](/reference/services/SoftLayer_Hardware_SecurityModule/getDownstreamNetworkHardwareWithIncidents)
Retrieve all network hardware with monitoring warnings or errors that are downstream from the selected piece of hardware.
</div>

<div class="method-row">

#### [getDownstreamServers](/reference/services/SoftLayer_Hardware_SecurityModule/getDownstreamServers)
Retrieve information regarding all servers attached downstream to a piece of network hardware.
</div>

<div class="method-row">

#### [getDownstreamVirtualGuests](/reference/services/SoftLayer_Hardware_SecurityModule/getDownstreamVirtualGuests)
Retrieve information regarding all virtual guests attached to a piece of network hardware.
</div>

<div class="method-row">

#### [getDriveControllers](/reference/services/SoftLayer_Hardware_SecurityModule/getDriveControllers)
Retrieve the drive controllers contained within a piece of hardware.
</div>

<div class="method-row">

#### [getEvaultNetworkStorage](/reference/services/SoftLayer_Hardware_SecurityModule/getEvaultNetworkStorage)
Retrieve information regarding a piece of hardware's associated EVault network storage service account.
</div>

<div class="method-row">

#### [getFirewallProtectableSubnets](/reference/services/SoftLayer_Hardware_SecurityModule/getFirewallProtectableSubnets)
Get the subnets associated with this server that are protectable by a network component firewall.
</div>

<div class="method-row">

#### [getFirewallServiceComponent](/reference/services/SoftLayer_Hardware_SecurityModule/getFirewallServiceComponent)
Retrieve information regarding a piece of hardware's firewall services.
</div>

<div class="method-row">

#### [getFixedConfigurationPreset](/reference/services/SoftLayer_Hardware_SecurityModule/getFixedConfigurationPreset)
Retrieve defines the fixed components in a fixed configuration bare metal server.
</div>

<div class="method-row">

#### [getFrontendBandwidthUsage](/reference/services/SoftLayer_Hardware_SecurityModule/getFrontendBandwidthUsage)
Retrieves public bandwidth usage records.
</div>

<div class="method-row">

#### [getFrontendBandwidthUse](/reference/services/SoftLayer_Hardware_SecurityModule/getFrontendBandwidthUse)
Retrieves public bandwidth usage records.
</div>

<div class="method-row">

#### [getFrontendIncomingBandwidth](/reference/services/SoftLayer_Hardware_SecurityModule/getFrontendIncomingBandwidth)
Retrieve the amount of incoming public network bandwidth used by a server over a period of time. 
</div>

<div class="method-row">

#### [getFrontendNetworkComponents](/reference/services/SoftLayer_Hardware_SecurityModule/getFrontendNetworkComponents)
Retrieve a piece of hardware's front-end or public network components.
</div>

<div class="method-row">

#### [getFrontendOutgoingBandwidth](/reference/services/SoftLayer_Hardware_SecurityModule/getFrontendOutgoingBandwidth)
Retrieve the amount of outgoing public network bandwidth used by a server over a period of time. 
</div>

<div class="method-row">

#### [getFrontendRouters](/reference/services/SoftLayer_Hardware_SecurityModule/getFrontendRouters)
Retrieve a hardware's frontend or public router.
</div>

<div class="method-row">

#### [getGlobalIdentifier](/reference/services/SoftLayer_Hardware_SecurityModule/getGlobalIdentifier)
Retrieve a hardware's universally unique identifier.
</div>

<div class="method-row">

#### [getHardDrives](/reference/services/SoftLayer_Hardware_SecurityModule/getHardDrives)
Retrieve the hard drives contained within a piece of hardware.
</div>

<div class="method-row">

#### [getHardwareByIpAddress](/reference/services/SoftLayer_Hardware_SecurityModule/getHardwareByIpAddress)
Retrieve a SoftLayer_Hardware_Server object by IP address.
</div>

<div class="method-row">

#### [getHardwareChassis](/reference/services/SoftLayer_Hardware_SecurityModule/getHardwareChassis)
Retrieve the chassis that a piece of hardware is housed in.
</div>

<div class="method-row">

#### [getHardwareFunction](/reference/services/SoftLayer_Hardware_SecurityModule/getHardwareFunction)
Retrieve a hardware's function.
</div>

<div class="method-row">

#### [getHardwareFunctionDescription](/reference/services/SoftLayer_Hardware_SecurityModule/getHardwareFunctionDescription)
Retrieve a hardware's function.
</div>

<div class="method-row">

#### [getHardwareStatus](/reference/services/SoftLayer_Hardware_SecurityModule/getHardwareStatus)
Retrieve a hardware's status.
</div>

<div class="method-row">

#### [getHasSingleRootVirtualizationBillingItemFlag](/reference/services/SoftLayer_Hardware_SecurityModule/getHasSingleRootVirtualizationBillingItemFlag)
Retrieve determine if hardware has Single Root IO VIrtualization (SR-IOV) billing item.
</div>

<div class="method-row">

#### [getHasTrustedPlatformModuleBillingItemFlag](/reference/services/SoftLayer_Hardware_SecurityModule/getHasTrustedPlatformModuleBillingItemFlag)
Retrieve determine in hardware object has TPM enabled.
</div>

<div class="method-row">

#### [getHostIpsSoftwareComponent](/reference/services/SoftLayer_Hardware_SecurityModule/getHostIpsSoftwareComponent)
Retrieve information regarding a host IPS software component object.
</div>

<div class="method-row">

#### [getHourlyBandwidth](/reference/services/SoftLayer_Hardware_SecurityModule/getHourlyBandwidth)
Retrieves bandwidth hourly over a 24-hour period for the specified hardware.
</div>

<div class="method-row">

#### [getHourlyBillingFlag](/reference/services/SoftLayer_Hardware_SecurityModule/getHourlyBillingFlag)
Retrieve a server's hourly billing status.
</div>

<div class="method-row">

#### [getInboundBandwidthUsage](/reference/services/SoftLayer_Hardware_SecurityModule/getInboundBandwidthUsage)
Retrieve the sum of all the inbound network traffic data for the last 30 days.
</div>

<div class="method-row">

#### [getInboundPrivateBandwidthUsage](/reference/services/SoftLayer_Hardware_SecurityModule/getInboundPrivateBandwidthUsage)
Retrieve the total private inbound bandwidth for this hardware for the current billing cycle.
</div>

<div class="method-row">

#### [getInboundPublicBandwidthUsage](/reference/services/SoftLayer_Hardware_SecurityModule/getInboundPublicBandwidthUsage)
Retrieve the total public inbound bandwidth for this hardware for the current billing cycle.
</div>

<div class="method-row">

#### [getIsCloudReadyNodeCertified](/reference/services/SoftLayer_Hardware_SecurityModule/getIsCloudReadyNodeCertified)
Retrieve determine if hardware object has the IBM_CLOUD_READY_NODE_CERTIFIED attribute.
</div>

<div class="method-row">

#### [getIsIpmiDisabled](/reference/services/SoftLayer_Hardware_SecurityModule/getIsIpmiDisabled)
Retrieve determine if remote management has been disabled due to port speed.
</div>

<div class="method-row">

#### [getIsVirtualPrivateCloudNode](/reference/services/SoftLayer_Hardware_SecurityModule/getIsVirtualPrivateCloudNode)
Retrieve determine if hardware object is a Virtual Private Cloud node.
</div>

<div class="method-row">

#### [getItemPricesFromSoftwareDescriptions](/reference/services/SoftLayer_Hardware_SecurityModule/getItemPricesFromSoftwareDescriptions)
Return a collection of SoftLayer_Item_Price objects from a collection of SoftLayer_Software_Description
</div>

<div class="method-row">

#### [getLastOperatingSystemReload](/reference/services/SoftLayer_Hardware_SecurityModule/getLastOperatingSystemReload)
Retrieve the last transaction that a server's operating system was loaded.
</div>

<div class="method-row">

#### [getLastTransaction](/reference/services/SoftLayer_Hardware_SecurityModule/getLastTransaction)
Retrieve information regarding the last transaction a server performed.
</div>

<div class="method-row">

#### [getLatestNetworkMonitorIncident](/reference/services/SoftLayer_Hardware_SecurityModule/getLatestNetworkMonitorIncident)
Retrieve a piece of hardware's latest network monitoring incident.
</div>

<div class="method-row">

#### [getLocation](/reference/services/SoftLayer_Hardware_SecurityModule/getLocation)
Retrieve where a piece of hardware is located within SoftLayer's location hierarchy.
</div>

<div class="method-row">

#### [getLocationPathString](/reference/services/SoftLayer_Hardware_SecurityModule/getLocationPathString)

</div>

<div class="method-row">

#### [getLockboxNetworkStorage](/reference/services/SoftLayer_Hardware_SecurityModule/getLockboxNetworkStorage)
Retrieve information regarding a lockbox account associated with a server.
</div>

<div class="method-row">

#### [getLogicalVolumeStorageGroups](/reference/services/SoftLayer_Hardware_SecurityModule/getLogicalVolumeStorageGroups)
Retrieve returns a list of logical volumes on the physical machine.
</div>

<div class="method-row">

#### [getManagedResourceFlag](/reference/services/SoftLayer_Hardware_SecurityModule/getManagedResourceFlag)
Retrieve a flag indicating that the hardware is a managed resource.
</div>

<div class="method-row">

#### [getManagementNetworkComponent](/reference/services/SoftLayer_Hardware_SecurityModule/getManagementNetworkComponent)
Retrieve a server's management network component.
</div>

<div class="method-row">

#### [getMemory](/reference/services/SoftLayer_Hardware_SecurityModule/getMemory)
Retrieve information regarding a piece of hardware's memory.
</div>

<div class="method-row">

#### [getMemoryCapacity](/reference/services/SoftLayer_Hardware_SecurityModule/getMemoryCapacity)
Retrieve the amount of memory a piece of hardware has, measured in gigabytes.
</div>

<div class="method-row">

#### [getMetricTrackingObject](/reference/services/SoftLayer_Hardware_SecurityModule/getMetricTrackingObject)
Retrieve a piece of hardware's metric tracking object.
</div>

<div class="method-row">

#### [getMetricTrackingObjectId](/reference/services/SoftLayer_Hardware_SecurityModule/getMetricTrackingObjectId)
Retrieve the metric tracking object id for this server.
</div>

<div class="method-row">

#### [getModules](/reference/services/SoftLayer_Hardware_SecurityModule/getModules)

</div>

<div class="method-row">

#### [getMonitoringRobot](/reference/services/SoftLayer_Hardware_SecurityModule/getMonitoringRobot)
Retrieve information regarding the hardware's monitoring robot.
</div>

<div class="method-row">

#### [getMonitoringServiceComponent](/reference/services/SoftLayer_Hardware_SecurityModule/getMonitoringServiceComponent)
Retrieve information regarding a piece of hardware's network monitoring services.
</div>

<div class="method-row">

#### [getMonitoringServiceEligibilityFlag](/reference/services/SoftLayer_Hardware_SecurityModule/getMonitoringServiceEligibilityFlag)
Retrieve the monitoring service flag eligibility status for a piece of hardware.
</div>

<div class="method-row">

#### [getMonitoringUserNotification](/reference/services/SoftLayer_Hardware_SecurityModule/getMonitoringUserNotification)
Retrieve the monitoring notification objects for this hardware. Each object links this hardware instance to a user account that will be notified if monitoring on this hardware object fails
</div>

<div class="method-row">

#### [getMotherboard](/reference/services/SoftLayer_Hardware_SecurityModule/getMotherboard)
Retrieve a server's motherboard.
</div>

<div class="method-row">

#### [getNetworkCards](/reference/services/SoftLayer_Hardware_SecurityModule/getNetworkCards)
Retrieve information regarding a piece of hardware's network cards.
</div>

<div class="method-row">

#### [getNetworkComponentFirewallProtectableIpAddresses](/reference/services/SoftLayer_Hardware_SecurityModule/getNetworkComponentFirewallProtectableIpAddresses)
Get the IP addresses associated with this server that are protectable by a network component firewall.
</div>

<div class="method-row">

#### [getNetworkComponents](/reference/services/SoftLayer_Hardware_SecurityModule/getNetworkComponents)
Retrieve returns a hardware's network components.
</div>

<div class="method-row">

#### [getNetworkGatewayMember](/reference/services/SoftLayer_Hardware_SecurityModule/getNetworkGatewayMember)
Retrieve the gateway member if this device is part of a network gateway.
</div>

<div class="method-row">

#### [getNetworkGatewayMemberFlag](/reference/services/SoftLayer_Hardware_SecurityModule/getNetworkGatewayMemberFlag)
Retrieve whether or not this device is part of a network gateway.
</div>

<div class="method-row">

#### [getNetworkManagementIpAddress](/reference/services/SoftLayer_Hardware_SecurityModule/getNetworkManagementIpAddress)
Retrieve a piece of hardware's network management IP address.
</div>

<div class="method-row">

#### [getNetworkMonitorAttachedDownHardware](/reference/services/SoftLayer_Hardware_SecurityModule/getNetworkMonitorAttachedDownHardware)
Retrieve all servers with failed monitoring that are attached downstream to a piece of hardware.
</div>

<div class="method-row">

#### [getNetworkMonitorAttachedDownVirtualGuests](/reference/services/SoftLayer_Hardware_SecurityModule/getNetworkMonitorAttachedDownVirtualGuests)
Retrieve virtual guests that are attached downstream to a hardware that have failed monitoring
</div>

<div class="method-row">

#### [getNetworkMonitorIncidents](/reference/services/SoftLayer_Hardware_SecurityModule/getNetworkMonitorIncidents)
Retrieve the status of all of a piece of hardware's network monitoring incidents.
</div>

<div class="method-row">

#### [getNetworkMonitors](/reference/services/SoftLayer_Hardware_SecurityModule/getNetworkMonitors)
Retrieve information regarding a piece of hardware's network monitors.
</div>

<div class="method-row">

#### [getNetworkStatus](/reference/services/SoftLayer_Hardware_SecurityModule/getNetworkStatus)
Retrieve the value of a hardware's network status attribute.
</div>

<div class="method-row">

#### [getNetworkStatusAttribute](/reference/services/SoftLayer_Hardware_SecurityModule/getNetworkStatusAttribute)
Retrieve the hardware's related network status attribute.
</div>

<div class="method-row">

#### [getNetworkStorage](/reference/services/SoftLayer_Hardware_SecurityModule/getNetworkStorage)
Retrieve information regarding a piece of hardware's associated network storage service account.
</div>

<div class="method-row">

#### [getNetworkVlans](/reference/services/SoftLayer_Hardware_SecurityModule/getNetworkVlans)
Retrieve the network virtual LANs (VLANs) associated with a piece of hardware's network components.
</div>

<div class="method-row">

#### [getNextBillingCycleBandwidthAllocation](/reference/services/SoftLayer_Hardware_SecurityModule/getNextBillingCycleBandwidthAllocation)
Retrieve a hardware's allotted bandwidth for the next billing cycle (measured in GB).
</div>

<div class="method-row">

#### [getNotesHistory](/reference/services/SoftLayer_Hardware_SecurityModule/getNotesHistory)

</div>

<div class="method-row">

#### [getNvRamCapacity](/reference/services/SoftLayer_Hardware_SecurityModule/getNvRamCapacity)
Retrieve the amount of non-volatile memory a piece of hardware has, measured in gigabytes.
</div>

<div class="method-row">

#### [getNvRamComponentModels](/reference/services/SoftLayer_Hardware_SecurityModule/getNvRamComponentModels)

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Hardware_SecurityModule/getObject)
Retrieve a SoftLayer_Hardware_SecurityModule record.
</div>

<div class="method-row">

#### [getOpenCancellationTicket](/reference/services/SoftLayer_Hardware_SecurityModule/getOpenCancellationTicket)
Retrieve an open ticket requesting cancellation of this server, if one exists.
</div>

<div class="method-row">

#### [getOperatingSystem](/reference/services/SoftLayer_Hardware_SecurityModule/getOperatingSystem)
Retrieve information regarding a piece of hardware's operating system.
</div>

<div class="method-row">

#### [getOperatingSystemReferenceCode](/reference/services/SoftLayer_Hardware_SecurityModule/getOperatingSystemReferenceCode)
Retrieve a hardware's operating system software description.
</div>

<div class="method-row">

#### [getOutboundBandwidthUsage](/reference/services/SoftLayer_Hardware_SecurityModule/getOutboundBandwidthUsage)
Retrieve the sum of all the outbound network traffic data for the last 30 days.
</div>

<div class="method-row">

#### [getOutboundPrivateBandwidthUsage](/reference/services/SoftLayer_Hardware_SecurityModule/getOutboundPrivateBandwidthUsage)
Retrieve the total private outbound bandwidth for this hardware for the current billing cycle.
</div>

<div class="method-row">

#### [getOutboundPublicBandwidthUsage](/reference/services/SoftLayer_Hardware_SecurityModule/getOutboundPublicBandwidthUsage)
Retrieve the total public outbound bandwidth for this hardware for the current billing cycle.
</div>

<div class="method-row">

#### [getOverBandwidthAllocationFlag](/reference/services/SoftLayer_Hardware_SecurityModule/getOverBandwidthAllocationFlag)
Retrieve whether the bandwidth usage for this hardware for the current billing cycle exceeds the allocation.
</div>

<div class="method-row">

#### [getPMInfo](/reference/services/SoftLayer_Hardware_SecurityModule/getPMInfo)
Retrieve a server's hardware state via its internal sensors.
</div>

<div class="method-row">

#### [getParentBay](/reference/services/SoftLayer_Hardware_SecurityModule/getParentBay)
Retrieve blade Bay
</div>

<div class="method-row">

#### [getParentHardware](/reference/services/SoftLayer_Hardware_SecurityModule/getParentHardware)
Retrieve parent Hardware.
</div>

<div class="method-row">

#### [getPointOfPresenceLocation](/reference/services/SoftLayer_Hardware_SecurityModule/getPointOfPresenceLocation)
Retrieve information regarding the Point of Presence (PoP) location in which a piece of hardware resides.
</div>

<div class="method-row">

#### [getPowerComponents](/reference/services/SoftLayer_Hardware_SecurityModule/getPowerComponents)
Retrieve the power components for a hardware object.
</div>

<div class="method-row">

#### [getPowerSupply](/reference/services/SoftLayer_Hardware_SecurityModule/getPowerSupply)
Retrieve a server's power supply.
</div>

<div class="method-row">

#### [getPrimaryBackendIpAddress](/reference/services/SoftLayer_Hardware_SecurityModule/getPrimaryBackendIpAddress)
Retrieve the hardware's primary private IP address.
</div>

<div class="method-row">

#### [getPrimaryDriveSize](/reference/services/SoftLayer_Hardware_SecurityModule/getPrimaryDriveSize)

</div>

<div class="method-row">

#### [getPrimaryIpAddress](/reference/services/SoftLayer_Hardware_SecurityModule/getPrimaryIpAddress)
Retrieve the hardware's primary public IP address.
</div>

<div class="method-row">

#### [getPrivateBandwidthData](/reference/services/SoftLayer_Hardware_SecurityModule/getPrivateBandwidthData)
Retrieve a graph of a server's private network usage.
</div>

<div class="method-row">

#### [getPrivateBandwidthDataSummary](/reference/services/SoftLayer_Hardware_SecurityModule/getPrivateBandwidthDataSummary)
Retrieve a server's private bandwidth usage summary
</div>

<div class="method-row">

#### [getPrivateBandwidthGraphImage](/reference/services/SoftLayer_Hardware_SecurityModule/getPrivateBandwidthGraphImage)
Retrieve a graph of a server's private network usage.
</div>

<div class="method-row">

#### [getPrivateIpAddress](/reference/services/SoftLayer_Hardware_SecurityModule/getPrivateIpAddress)
Retrieve a server's primary private IP address.
</div>

<div class="method-row">

#### [getPrivateNetworkComponent](/reference/services/SoftLayer_Hardware_SecurityModule/getPrivateNetworkComponent)
Retrieve a server's private network component.
</div>

<div class="method-row">

#### [getPrivateNetworkOnlyFlag](/reference/services/SoftLayer_Hardware_SecurityModule/getPrivateNetworkOnlyFlag)
Retrieve whether the hardware only has access to the private network.
</div>

<div class="method-row">

#### [getPrivateVlan](/reference/services/SoftLayer_Hardware_SecurityModule/getPrivateVlan)
Retrieve the backend VLAN for the primary IP address of the server.
</div>

<div class="method-row">

#### [getPrivateVlanByIpAddress](/reference/services/SoftLayer_Hardware_SecurityModule/getPrivateVlanByIpAddress)
Retrieve a backend network VLAN by searching for an IP address.
</div>

<div class="method-row">

#### [getProcessorCoreAmount](/reference/services/SoftLayer_Hardware_SecurityModule/getProcessorCoreAmount)
Retrieve the total number of processor cores, summed from all processors that are attached to a piece of hardware
</div>

<div class="method-row">

#### [getProcessorPhysicalCoreAmount](/reference/services/SoftLayer_Hardware_SecurityModule/getProcessorPhysicalCoreAmount)
Retrieve the total number of physical processor cores, summed from all processors that are attached to a piece of hardware
</div>

<div class="method-row">

#### [getProcessors](/reference/services/SoftLayer_Hardware_SecurityModule/getProcessors)
Retrieve information regarding a piece of hardware's processors.
</div>

<div class="method-row">

#### [getProjectedOverBandwidthAllocationFlag](/reference/services/SoftLayer_Hardware_SecurityModule/getProjectedOverBandwidthAllocationFlag)
Retrieve whether the bandwidth usage for this hardware for the current billing cycle is projected to exceed the allocation.
</div>

<div class="method-row">

#### [getProjectedPublicBandwidthUsage](/reference/services/SoftLayer_Hardware_SecurityModule/getProjectedPublicBandwidthUsage)
Retrieve the projected public outbound bandwidth for this hardware for the current billing cycle.
</div>

<div class="method-row">

#### [getProvisionDate](/reference/services/SoftLayer_Hardware_SecurityModule/getProvisionDate)

</div>

<div class="method-row">

#### [getPublicBandwidthData](/reference/services/SoftLayer_Hardware_SecurityModule/getPublicBandwidthData)
Retrieve a graph of a server's public network usage.
</div>

<div class="method-row">

#### [getPublicBandwidthDataSummary](/reference/services/SoftLayer_Hardware_SecurityModule/getPublicBandwidthDataSummary)
Retrieve a server's public bandwidth usage summary
</div>

<div class="method-row">

#### [getPublicBandwidthGraphImage](/reference/services/SoftLayer_Hardware_SecurityModule/getPublicBandwidthGraphImage)
Retrieve a graph of a server's public network usage.
</div>

<div class="method-row">

#### [getPublicBandwidthTotal](/reference/services/SoftLayer_Hardware_SecurityModule/getPublicBandwidthTotal)
Retrieve total number of public bytes used by a server over time period specified.
</div>

<div class="method-row">

#### [getPublicNetworkComponent](/reference/services/SoftLayer_Hardware_SecurityModule/getPublicNetworkComponent)
Retrieve a server's public network component.
</div>

<div class="method-row">

#### [getPublicVlan](/reference/services/SoftLayer_Hardware_SecurityModule/getPublicVlan)
Retrieve the frontend VLAN for the primary IP address of the server
</div>

<div class="method-row">

#### [getPublicVlanByHostname](/reference/services/SoftLayer_Hardware_SecurityModule/getPublicVlanByHostname)
Retrieve the frontend VLAN by a server's hostname.
</div>

<div class="method-row">

#### [getRack](/reference/services/SoftLayer_Hardware_SecurityModule/getRack)

</div>

<div class="method-row">

#### [getRaidControllers](/reference/services/SoftLayer_Hardware_SecurityModule/getRaidControllers)
Retrieve the RAID controllers contained within a piece of hardware.
</div>

<div class="method-row">

#### [getReadyNodeFlag](/reference/services/SoftLayer_Hardware_SecurityModule/getReadyNodeFlag)
Retrieve determine if hardware object is vSan Ready Node.
</div>

<div class="method-row">

#### [getRecentEvents](/reference/services/SoftLayer_Hardware_SecurityModule/getRecentEvents)
Retrieve recent events that impact this hardware.
</div>

<div class="method-row">

#### [getRecentRemoteManagementCommands](/reference/services/SoftLayer_Hardware_SecurityModule/getRecentRemoteManagementCommands)
Retrieve the last five commands issued to the server's remote management card.
</div>

<div class="method-row">

#### [getRegionalInternetRegistry](/reference/services/SoftLayer_Hardware_SecurityModule/getRegionalInternetRegistry)

</div>

<div class="method-row">

#### [getRemoteManagement](/reference/services/SoftLayer_Hardware_SecurityModule/getRemoteManagement)
Retrieve a server's remote management card.
</div>

<div class="method-row">

#### [getRemoteManagementAccounts](/reference/services/SoftLayer_Hardware_SecurityModule/getRemoteManagementAccounts)
Retrieve user credentials to issue commands and/or interact with the server's remote management card.
</div>

<div class="method-row">

#### [getRemoteManagementComponent](/reference/services/SoftLayer_Hardware_SecurityModule/getRemoteManagementComponent)
Retrieve a hardware's associated remote management component. This is normally IPMI.
</div>

<div class="method-row">

#### [getRemoteManagementUsers](/reference/services/SoftLayer_Hardware_SecurityModule/getRemoteManagementUsers)
Retrieve user(s) who have access to issue commands and/or interact with the server's remote management card.
</div>

<div class="method-row">

#### [getResourceConfigurations](/reference/services/SoftLayer_Hardware_SecurityModule/getResourceConfigurations)

</div>

<div class="method-row">

#### [getResourceGroupMemberReferences](/reference/services/SoftLayer_Hardware_SecurityModule/getResourceGroupMemberReferences)

</div>

<div class="method-row">

#### [getResourceGroupRoles](/reference/services/SoftLayer_Hardware_SecurityModule/getResourceGroupRoles)

</div>

<div class="method-row">

#### [getResourceGroups](/reference/services/SoftLayer_Hardware_SecurityModule/getResourceGroups)
Retrieve the resource groups in which this hardware is a member.
</div>

<div class="method-row">

#### [getReverseDomainRecords](/reference/services/SoftLayer_Hardware_SecurityModule/getReverseDomainRecords)
Retrieve the reverse domain records associated with a server.
</div>

<div class="method-row">

#### [getRouters](/reference/services/SoftLayer_Hardware_SecurityModule/getRouters)
Retrieve a hardware's routers.
</div>

<div class="method-row">

#### [getScaleAssets](/reference/services/SoftLayer_Hardware_SecurityModule/getScaleAssets)
Retrieve collection of scale assets this hardware corresponds to.
</div>

<div class="method-row">

#### [getSecurityScanRequests](/reference/services/SoftLayer_Hardware_SecurityModule/getSecurityScanRequests)
Retrieve information regarding a piece of hardware's vulnerability scan requests.
</div>

<div class="method-row">

#### [getSensorData](/reference/services/SoftLayer_Hardware_SecurityModule/getSensorData)
Retrieve a server's hardware state via its internal sensors.
</div>

<div class="method-row">

#### [getSensorDataWithGraphs](/reference/services/SoftLayer_Hardware_SecurityModule/getSensorDataWithGraphs)
Retrieve server's temperature and fan speed graphs as well the sensor raw data.
</div>

<div class="method-row">

#### [getServerDetails](/reference/services/SoftLayer_Hardware_SecurityModule/getServerDetails)
Retrieve a server's hardware components, software, and network components.
</div>

<div class="method-row">

#### [getServerFanSpeedGraphs](/reference/services/SoftLayer_Hardware_SecurityModule/getServerFanSpeedGraphs)
Retrieve server's fan speed graphs.
</div>

<div class="method-row">

#### [getServerPowerState](/reference/services/SoftLayer_Hardware_SecurityModule/getServerPowerState)
Retrieves server's power state
</div>

<div class="method-row">

#### [getServerRoom](/reference/services/SoftLayer_Hardware_SecurityModule/getServerRoom)
Retrieve information regarding the server room in which the hardware is located.
</div>

<div class="method-row">

#### [getServerTemperatureGraphs](/reference/services/SoftLayer_Hardware_SecurityModule/getServerTemperatureGraphs)
Retrieve server's temperature graphs
</div>

<div class="method-row">

#### [getServiceProvider](/reference/services/SoftLayer_Hardware_SecurityModule/getServiceProvider)
Retrieve information regarding the piece of hardware's service provider.
</div>

<div class="method-row">

#### [getSoftwareComponents](/reference/services/SoftLayer_Hardware_SecurityModule/getSoftwareComponents)
Retrieve information regarding a piece of hardware's installed software.
</div>

<div class="method-row">

#### [getSoftwareGuardExtensionEnabled](/reference/services/SoftLayer_Hardware_SecurityModule/getSoftwareGuardExtensionEnabled)
Retrieve determine if hardware object has Software Guard Extension (SGX) enabled.
</div>

<div class="method-row">

#### [getSshKeys](/reference/services/SoftLayer_Hardware_SecurityModule/getSshKeys)
Retrieve sSH keys to be installed on the server during provisioning or an OS reload.
</div>

<div class="method-row">

#### [getStatisticsRemoteManagement](/reference/services/SoftLayer_Hardware_SecurityModule/getStatisticsRemoteManagement)
Retrieve a server's remote management card used for statistics.
</div>

<div class="method-row">

#### [getStorageGroups](/reference/services/SoftLayer_Hardware_SecurityModule/getStorageGroups)

</div>

<div class="method-row">

#### [getStorageNetworkComponents](/reference/services/SoftLayer_Hardware_SecurityModule/getStorageNetworkComponents)
Retrieve a piece of hardware's private storage network components. [Deprecated]
</div>

<div class="method-row">

#### [getTagReferences](/reference/services/SoftLayer_Hardware_SecurityModule/getTagReferences)

</div>

<div class="method-row">

#### [getTopLevelLocation](/reference/services/SoftLayer_Hardware_SecurityModule/getTopLevelLocation)

</div>

<div class="method-row">

#### [getTransactionHistory](/reference/services/SoftLayer_Hardware_SecurityModule/getTransactionHistory)
Get transaction history for a piece of hardware.
</div>

<div class="method-row">

#### [getUefiBootFlag](/reference/services/SoftLayer_Hardware_SecurityModule/getUefiBootFlag)
Retrieve whether to use UEFI boot instead of BIOS.
</div>

<div class="method-row">

#### [getUpgradeItemPrices](/reference/services/SoftLayer_Hardware_SecurityModule/getUpgradeItemPrices)
Retrieve a list of upgradable items available to a piece of hardware.
</div>

<div class="method-row">

#### [getUpgradeRequest](/reference/services/SoftLayer_Hardware_SecurityModule/getUpgradeRequest)
Retrieve an account's associated upgrade request object, if any.
</div>

<div class="method-row">

#### [getUplinkHardware](/reference/services/SoftLayer_Hardware_SecurityModule/getUplinkHardware)
Retrieve the network device connected to a piece of hardware.
</div>

<div class="method-row">

#### [getUplinkNetworkComponents](/reference/services/SoftLayer_Hardware_SecurityModule/getUplinkNetworkComponents)
Retrieve information regarding the network component that is one level higher than a piece of hardware on the network infrastructure.
</div>

<div class="method-row">

#### [getUserData](/reference/services/SoftLayer_Hardware_SecurityModule/getUserData)
Retrieve an array containing a single string of custom user data for a hardware order. Max size is 16 kb.
</div>

<div class="method-row">

#### [getUsers](/reference/services/SoftLayer_Hardware_SecurityModule/getUsers)
Retrieve a list of users that have access to this computing instance.
</div>

<div class="method-row">

#### [getValidBlockDeviceTemplateGroups](/reference/services/SoftLayer_Hardware_SecurityModule/getValidBlockDeviceTemplateGroups)
Return a list of valid block device template groups based on this host
</div>

<div class="method-row">

#### [getVirtualChassis](/reference/services/SoftLayer_Hardware_SecurityModule/getVirtualChassis)
Retrieve information regarding the virtual chassis for a piece of hardware.
</div>

<div class="method-row">

#### [getVirtualChassisSiblings](/reference/services/SoftLayer_Hardware_SecurityModule/getVirtualChassisSiblings)
Retrieve information regarding the virtual chassis siblings for a piece of hardware.
</div>

<div class="method-row">

#### [getVirtualGuests](/reference/services/SoftLayer_Hardware_SecurityModule/getVirtualGuests)
Retrieve a hardware server's virtual servers.
</div>

<div class="method-row">

#### [getVirtualHost](/reference/services/SoftLayer_Hardware_SecurityModule/getVirtualHost)
Retrieve a piece of hardware's virtual host record.
</div>

<div class="method-row">

#### [getVirtualLicenses](/reference/services/SoftLayer_Hardware_SecurityModule/getVirtualLicenses)
Retrieve information regarding a piece of hardware's virtual software licenses.
</div>

<div class="method-row">

#### [getVirtualRack](/reference/services/SoftLayer_Hardware_SecurityModule/getVirtualRack)
Retrieve information regarding the bandwidth allotment to which a piece of hardware belongs.
</div>

<div class="method-row">

#### [getVirtualRackId](/reference/services/SoftLayer_Hardware_SecurityModule/getVirtualRackId)
Retrieve the name of the bandwidth allotment belonging to a piece of hardware.
</div>

<div class="method-row">

#### [getVirtualRackName](/reference/services/SoftLayer_Hardware_SecurityModule/getVirtualRackName)
Retrieve the name of the bandwidth allotment belonging to a piece of hardware.
</div>

<div class="method-row">

#### [getVirtualizationPlatform](/reference/services/SoftLayer_Hardware_SecurityModule/getVirtualizationPlatform)
Retrieve a piece of hardware's virtualization platform software.
</div>

<div class="method-row">

#### [getWindowsUpdateAvailableUpdates](/reference/services/SoftLayer_Hardware_SecurityModule/getWindowsUpdateAvailableUpdates)
Retrieve a list of Windows updates available to a server.
</div>

<div class="method-row">

#### [getWindowsUpdateInstalledUpdates](/reference/services/SoftLayer_Hardware_SecurityModule/getWindowsUpdateInstalledUpdates)
Retrieve a list of Windows updates installed on a server.
</div>

<div class="method-row">

#### [getWindowsUpdateStatus](/reference/services/SoftLayer_Hardware_SecurityModule/getWindowsUpdateStatus)
Retrieve a server's Windows update synchronization status
</div>

<div class="method-row">

#### [importVirtualHost](/reference/services/SoftLayer_Hardware_SecurityModule/importVirtualHost)
attempt to import the host record for the virtualization platform running on a server
</div>

<div class="method-row">

#### [initiateIderaBareMetalRestore](/reference/services/SoftLayer_Hardware_SecurityModule/initiateIderaBareMetalRestore)
Initiate an Idera bare metal restore for the server tied to an Idera Server Backup
</div>

<div class="method-row">

#### [initiateR1SoftBareMetalRestore](/reference/services/SoftLayer_Hardware_SecurityModule/initiateR1SoftBareMetalRestore)
Initiate an R1Soft bare metal restore for the server tied to an R1Soft CDP Server
</div>

<div class="method-row">

#### [isBackendPingable](/reference/services/SoftLayer_Hardware_SecurityModule/isBackendPingable)
Verifies if a server's backend ip address is pingable.
</div>

<div class="method-row">

#### [isPingable](/reference/services/SoftLayer_Hardware_SecurityModule/isPingable)
Verifies if server is pingable.
</div>

<div class="method-row">

#### [isWindowsServer](/reference/services/SoftLayer_Hardware_SecurityModule/isWindowsServer)
Determine if a server runs the Microsoft Windows operating system.
</div>

<div class="method-row">

#### [massFirmwareReflash](/reference/services/SoftLayer_Hardware_SecurityModule/massFirmwareReflash)
Runs firmware reflashes on the servers components.
</div>

<div class="method-row">

#### [massFirmwareUpdate](/reference/services/SoftLayer_Hardware_SecurityModule/massFirmwareUpdate)
Runs firmware updates on the servers components.
</div>

<div class="method-row">

#### [massHyperThreadingUpdate](/reference/services/SoftLayer_Hardware_SecurityModule/massHyperThreadingUpdate)
Runs firmware reflashes on the servers components.
</div>

<div class="method-row">

#### [massReloadOperatingSystem](/reference/services/SoftLayer_Hardware_SecurityModule/massReloadOperatingSystem)
Reloads operating system configuration on a set of hardware Ids.
</div>

<div class="method-row">

#### [massSparePool](/reference/services/SoftLayer_Hardware_SecurityModule/massSparePool)
Allows multiple servers to be added to or removed from the spare pool.
</div>

<div class="method-row">

#### [ping](/reference/services/SoftLayer_Hardware_SecurityModule/ping)
Issues ping command.
</div>

<div class="method-row">

#### [populateServerRam](/reference/services/SoftLayer_Hardware_SecurityModule/populateServerRam)

</div>

<div class="method-row">

#### [powerCycle](/reference/services/SoftLayer_Hardware_SecurityModule/powerCycle)
Issues power cycle to server.
</div>

<div class="method-row">

#### [powerOff](/reference/services/SoftLayer_Hardware_SecurityModule/powerOff)
Power off server.
</div>

<div class="method-row">

#### [powerOn](/reference/services/SoftLayer_Hardware_SecurityModule/powerOn)
Power on server.
</div>

<div class="method-row">

#### [rebootDefault](/reference/services/SoftLayer_Hardware_SecurityModule/rebootDefault)
Reboot the server via the default method.
</div>

<div class="method-row">

#### [rebootHard](/reference/services/SoftLayer_Hardware_SecurityModule/rebootHard)
Reboot the server via "hard" reboot.
</div>

<div class="method-row">

#### [rebootSoft](/reference/services/SoftLayer_Hardware_SecurityModule/rebootSoft)
Reboot the server via gracefully (soft reboot).
</div>

<div class="method-row">

#### [reloadCurrentOperatingSystemConfiguration](/reference/services/SoftLayer_Hardware_SecurityModule/reloadCurrentOperatingSystemConfiguration)
Reloads current operating system configuration.
</div>

<div class="method-row">

#### [reloadOperatingSystem](/reference/services/SoftLayer_Hardware_SecurityModule/reloadOperatingSystem)
Reloads operating system configuration.
</div>

<div class="method-row">

#### [removeAccessToNetworkStorage](/reference/services/SoftLayer_Hardware_SecurityModule/removeAccessToNetworkStorage)
Remove access to a SoftLayer_Network_Storage volume from this device. 
</div>

<div class="method-row">

#### [removeAccessToNetworkStorageList](/reference/services/SoftLayer_Hardware_SecurityModule/removeAccessToNetworkStorageList)
Remove access to multiple SoftLayer_Network_Storage volumes from this device. 
</div>

<div class="method-row">

#### [removeTags](/reference/services/SoftLayer_Hardware_SecurityModule/removeTags)
Remove a tag reference
</div>

<div class="method-row">

#### [runPassmarkCertificationBenchmark](/reference/services/SoftLayer_Hardware_SecurityModule/runPassmarkCertificationBenchmark)
Runs a hardware stress test on the server to obtain a Passmark Certification.
</div>

<div class="method-row">

#### [setOperatingSystemPassword](/reference/services/SoftLayer_Hardware_SecurityModule/setOperatingSystemPassword)
Changes the password stored in our system for a servers' Operating System
</div>

<div class="method-row">

#### [setPrivateNetworkInterfaceSpeed](/reference/services/SoftLayer_Hardware_SecurityModule/setPrivateNetworkInterfaceSpeed)
Set the speed and redundancy configuration of a server's private network interface.
</div>

<div class="method-row">

#### [setPublicNetworkInterfaceSpeed](/reference/services/SoftLayer_Hardware_SecurityModule/setPublicNetworkInterfaceSpeed)
Set the speed and redundancy configuration of a server's public network interface.
</div>

<div class="method-row">

#### [setTags](/reference/services/SoftLayer_Hardware_SecurityModule/setTags)

</div>

<div class="method-row">

#### [setUserMetadata](/reference/services/SoftLayer_Hardware_SecurityModule/setUserMetadata)
Sets the server's user metadata value.
</div>

<div class="method-row">

#### [shutdownPrivatePort](/reference/services/SoftLayer_Hardware_SecurityModule/shutdownPrivatePort)
Disconnect a server's private network interface.
</div>

<div class="method-row">

#### [shutdownPublicPort](/reference/services/SoftLayer_Hardware_SecurityModule/shutdownPublicPort)
Disconnect a server's public network interface.
</div>

<div class="method-row">

#### [sparePool](/reference/services/SoftLayer_Hardware_SecurityModule/sparePool)
Allows servers to be added to or removed from the spare pool.
</div>

<div class="method-row">

#### [testRaidAlertService](/reference/services/SoftLayer_Hardware_SecurityModule/testRaidAlertService)
Tests the RAID Alert service.
</div>

<div class="method-row">

#### [toggleManagementInterface](/reference/services/SoftLayer_Hardware_SecurityModule/toggleManagementInterface)
Toggle the IPMI interface on and off.
</div>

<div class="method-row">

#### [updateIpmiPassword](/reference/services/SoftLayer_Hardware_SecurityModule/updateIpmiPassword)
Update the root IPMI user password 
</div>

<div class="method-row">

#### [validatePartitionsForOperatingSystem](/reference/services/SoftLayer_Hardware_SecurityModule/validatePartitionsForOperatingSystem)
Validates a collection of partitions for an operating system
</div>
</div>

</div>

