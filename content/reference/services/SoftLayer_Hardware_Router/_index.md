---
title: "SoftLayer_Hardware_Router"
description: "This service provides access to the device responsible for routing a particular SoftLayer Router."
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Router"
---
# SoftLayer_Hardware_Router
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Hardware_Router' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Router' >Datatype</a></li>
    </ul>
</div>

## Description
This service provides access to the device responsible for routing a particular SoftLayer Router. 



### seeAlso

* [SoftLayer_Hardware](/reference/datatypes/SoftLayer_Hardware )


        
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

#### [allowAccessToNetworkStorage](/reference/services/SoftLayer_Hardware_Router/allowAccessToNetworkStorage)
Allow access to a SoftLayer_Network_Storage volume from this device. 
</div>

<div class="method-row">

#### [allowAccessToNetworkStorageList](/reference/services/SoftLayer_Hardware_Router/allowAccessToNetworkStorageList)
Allow access to multiple SoftLayer_Network_Storage volumes from this device. 
</div>

<div class="method-row">

#### [captureImage](/reference/services/SoftLayer_Hardware_Router/captureImage)
Captures an Image of the hard disk on the physical machine.
</div>

<div class="method-row">

#### [createObject](/reference/services/SoftLayer_Hardware_Router/createObject)
Create a new server
</div>

<div class="method-row">

#### [deleteObject](/reference/services/SoftLayer_Hardware_Router/deleteObject)
Delete a server
</div>

<div class="method-row">

#### [deleteSoftwareComponentPasswords](/reference/services/SoftLayer_Hardware_Router/deleteSoftwareComponentPasswords)
Delete software component passwords.
</div>

<div class="method-row">

#### [deleteTag](/reference/services/SoftLayer_Hardware_Router/deleteTag)
Delete a tag
</div>

<div class="method-row">

#### [editSoftwareComponentPasswords](/reference/services/SoftLayer_Hardware_Router/editSoftwareComponentPasswords)
Edit the properties of software component passwords.
</div>

<div class="method-row">

#### [executeRemoteScript](/reference/services/SoftLayer_Hardware_Router/executeRemoteScript)
Download and run remote script from uri on the hardware. Requires https for script to be executed after download. 
</div>

<div class="method-row">

#### [findByIpAddress](/reference/services/SoftLayer_Hardware_Router/findByIpAddress)
Find hardware by its primary public or private IP (ipv4) address.
</div>

<div class="method-row">

#### [generateOrderTemplate](/reference/services/SoftLayer_Hardware_Router/generateOrderTemplate)
Obtain an order container for a given template object
</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Hardware_Router/getAccount)
Retrieve the account associated with a piece of hardware.
</div>

<div class="method-row">

#### [getActiveComponents](/reference/services/SoftLayer_Hardware_Router/getActiveComponents)
Retrieve a piece of hardware's active physical components.
</div>

<div class="method-row">

#### [getActiveNetworkMonitorIncident](/reference/services/SoftLayer_Hardware_Router/getActiveNetworkMonitorIncident)
Retrieve a piece of hardware's active network monitoring incidents.
</div>

<div class="method-row">

#### [getAllPowerComponents](/reference/services/SoftLayer_Hardware_Router/getAllPowerComponents)

</div>

<div class="method-row">

#### [getAllowedHost](/reference/services/SoftLayer_Hardware_Router/getAllowedHost)
Retrieve the SoftLayer_Network_Storage_Allowed_Host information to connect this server to Network Storage volumes that require access control lists.
</div>

<div class="method-row">

#### [getAllowedNetworkStorage](/reference/services/SoftLayer_Hardware_Router/getAllowedNetworkStorage)
Retrieve the SoftLayer_Network_Storage objects that this SoftLayer_Hardware has access to.
</div>

<div class="method-row">

#### [getAllowedNetworkStorageReplicas](/reference/services/SoftLayer_Hardware_Router/getAllowedNetworkStorageReplicas)
Retrieve the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to.
</div>

<div class="method-row">

#### [getAntivirusSpywareSoftwareComponent](/reference/services/SoftLayer_Hardware_Router/getAntivirusSpywareSoftwareComponent)
Retrieve information regarding an antivirus/spyware software component object.
</div>

<div class="method-row">

#### [getAttachedNetworkStorages](/reference/services/SoftLayer_Hardware_Router/getAttachedNetworkStorages)
Return a list of SoftLayer_Network_Storage volumes authorized to this device. 
</div>

<div class="method-row">

#### [getAttributes](/reference/services/SoftLayer_Hardware_Router/getAttributes)
Retrieve information regarding a piece of hardware's specific attributes.
</div>

<div class="method-row">

#### [getAvailableNetworkStorages](/reference/services/SoftLayer_Hardware_Router/getAvailableNetworkStorages)
Return a list of SoftLayer_Network_Storage volumes that can be authorized to this device. 
</div>

<div class="method-row">

#### [getAverageDailyPublicBandwidthUsage](/reference/services/SoftLayer_Hardware_Router/getAverageDailyPublicBandwidthUsage)
Retrieve the average daily public bandwidth usage for the current billing cycle.
</div>

<div class="method-row">

#### [getBackendIncomingBandwidth](/reference/services/SoftLayer_Hardware_Router/getBackendIncomingBandwidth)
Retrieve the amount of incoming private network bandwidth used by a server over a period of time. 
</div>

<div class="method-row">

#### [getBackendNetworkComponents](/reference/services/SoftLayer_Hardware_Router/getBackendNetworkComponents)
Retrieve a piece of hardware's back-end or private network components.
</div>

<div class="method-row">

#### [getBackendOutgoingBandwidth](/reference/services/SoftLayer_Hardware_Router/getBackendOutgoingBandwidth)
Retrieve the amount of outgoing private network bandwidth used by a server over a period of time. 
</div>

<div class="method-row">

#### [getBackendRouters](/reference/services/SoftLayer_Hardware_Router/getBackendRouters)
Retrieve a hardware's backend or private router.
</div>

<div class="method-row">

#### [getBandwidthAllocation](/reference/services/SoftLayer_Hardware_Router/getBandwidthAllocation)
Retrieve a hardware's allotted bandwidth (measured in GB).
</div>

<div class="method-row">

#### [getBandwidthAllotmentDetail](/reference/services/SoftLayer_Hardware_Router/getBandwidthAllotmentDetail)
Retrieve a hardware's allotted detail record. Allotment details link bandwidth allocation with allotments.
</div>

<div class="method-row">

#### [getBenchmarkCertifications](/reference/services/SoftLayer_Hardware_Router/getBenchmarkCertifications)
Retrieve information regarding a piece of hardware's benchmark certifications.
</div>

<div class="method-row">

#### [getBillingItem](/reference/services/SoftLayer_Hardware_Router/getBillingItem)
Retrieve information regarding the billing item for a server.
</div>

<div class="method-row">

#### [getBillingItemFlag](/reference/services/SoftLayer_Hardware_Router/getBillingItemFlag)
Retrieve a flag indicating that a billing item exists.
</div>

<div class="method-row">

#### [getBlockCancelBecauseDisconnectedFlag](/reference/services/SoftLayer_Hardware_Router/getBlockCancelBecauseDisconnectedFlag)
Retrieve determines whether the hardware is ineligible for cancellation because it is disconnected.
</div>

<div class="method-row">

#### [getBoundSubnets](/reference/services/SoftLayer_Hardware_Router/getBoundSubnets)
Retrieve associated subnets for a router object.
</div>

<div class="method-row">

#### [getBusinessContinuanceInsuranceFlag](/reference/services/SoftLayer_Hardware_Router/getBusinessContinuanceInsuranceFlag)
Retrieve status indicating whether or not a piece of hardware has business continuance insurance.
</div>

<div class="method-row">

#### [getChildrenHardware](/reference/services/SoftLayer_Hardware_Router/getChildrenHardware)
Retrieve child hardware.
</div>

<div class="method-row">

#### [getComponentDetailsXML](/reference/services/SoftLayer_Hardware_Router/getComponentDetailsXML)

</div>

<div class="method-row">

#### [getComponents](/reference/services/SoftLayer_Hardware_Router/getComponents)
Retrieve a piece of hardware's components.
</div>

<div class="method-row">

#### [getContinuousDataProtectionSoftwareComponent](/reference/services/SoftLayer_Hardware_Router/getContinuousDataProtectionSoftwareComponent)
Retrieve a continuous data protection/server backup software component object.
</div>

<div class="method-row">

#### [getCreateObjectOptions](/reference/services/SoftLayer_Hardware_Router/getCreateObjectOptions)
Determine options available when creating a server
</div>

<div class="method-row">

#### [getCurrentBillableBandwidthUsage](/reference/services/SoftLayer_Hardware_Router/getCurrentBillableBandwidthUsage)
Retrieve the current billable public outbound bandwidth for this hardware for the current billing cycle.
</div>

<div class="method-row">

#### [getCurrentBillingDetail](/reference/services/SoftLayer_Hardware_Router/getCurrentBillingDetail)
<< EOT
</div>

<div class="method-row">

#### [getCurrentBillingTotal](/reference/services/SoftLayer_Hardware_Router/getCurrentBillingTotal)
Get the billing total for this instance's usage up to this point. This total includes all bandwidth charges. 
</div>

<div class="method-row">

#### [getDailyAverage](/reference/services/SoftLayer_Hardware_Router/getDailyAverage)
calculate the average daily network traffic used by a server in gigabytes.
</div>

<div class="method-row">

#### [getDatacenter](/reference/services/SoftLayer_Hardware_Router/getDatacenter)
Retrieve information regarding the datacenter in which a piece of hardware resides.
</div>

<div class="method-row">

#### [getDatacenterName](/reference/services/SoftLayer_Hardware_Router/getDatacenterName)
Retrieve the name of the datacenter in which a piece of hardware resides.
</div>

<div class="method-row">

#### [getDaysInSparePool](/reference/services/SoftLayer_Hardware_Router/getDaysInSparePool)
Retrieve number of day(s) a server have been in spare pool.
</div>

<div class="method-row">

#### [getDownlinkHardware](/reference/services/SoftLayer_Hardware_Router/getDownlinkHardware)
Retrieve all hardware that has uplink network connections to a piece of hardware.
</div>

<div class="method-row">

#### [getDownlinkNetworkHardware](/reference/services/SoftLayer_Hardware_Router/getDownlinkNetworkHardware)
Retrieve all hardware that has uplink network connections to a piece of hardware.
</div>

<div class="method-row">

#### [getDownlinkServers](/reference/services/SoftLayer_Hardware_Router/getDownlinkServers)
Retrieve information regarding all servers attached to a piece of network hardware.
</div>

<div class="method-row">

#### [getDownlinkVirtualGuests](/reference/services/SoftLayer_Hardware_Router/getDownlinkVirtualGuests)
Retrieve information regarding all virtual guests attached to a piece of network hardware.
</div>

<div class="method-row">

#### [getDownstreamHardwareBindings](/reference/services/SoftLayer_Hardware_Router/getDownstreamHardwareBindings)
Retrieve all hardware downstream from a network device.
</div>

<div class="method-row">

#### [getDownstreamNetworkHardware](/reference/services/SoftLayer_Hardware_Router/getDownstreamNetworkHardware)
Retrieve all network hardware downstream from the selected piece of hardware.
</div>

<div class="method-row">

#### [getDownstreamNetworkHardwareWithIncidents](/reference/services/SoftLayer_Hardware_Router/getDownstreamNetworkHardwareWithIncidents)
Retrieve all network hardware with monitoring warnings or errors that are downstream from the selected piece of hardware.
</div>

<div class="method-row">

#### [getDownstreamServers](/reference/services/SoftLayer_Hardware_Router/getDownstreamServers)
Retrieve information regarding all servers attached downstream to a piece of network hardware.
</div>

<div class="method-row">

#### [getDownstreamVirtualGuests](/reference/services/SoftLayer_Hardware_Router/getDownstreamVirtualGuests)
Retrieve information regarding all virtual guests attached to a piece of network hardware.
</div>

<div class="method-row">

#### [getDriveControllers](/reference/services/SoftLayer_Hardware_Router/getDriveControllers)
Retrieve the drive controllers contained within a piece of hardware.
</div>

<div class="method-row">

#### [getEvaultNetworkStorage](/reference/services/SoftLayer_Hardware_Router/getEvaultNetworkStorage)
Retrieve information regarding a piece of hardware's associated EVault network storage service account.
</div>

<div class="method-row">

#### [getFirewallServiceComponent](/reference/services/SoftLayer_Hardware_Router/getFirewallServiceComponent)
Retrieve information regarding a piece of hardware's firewall services.
</div>

<div class="method-row">

#### [getFixedConfigurationPreset](/reference/services/SoftLayer_Hardware_Router/getFixedConfigurationPreset)
Retrieve defines the fixed components in a fixed configuration bare metal server.
</div>

<div class="method-row">

#### [getFrontendIncomingBandwidth](/reference/services/SoftLayer_Hardware_Router/getFrontendIncomingBandwidth)
Retrieve the amount of incoming public network bandwidth used by a server over a period of time. 
</div>

<div class="method-row">

#### [getFrontendNetworkComponents](/reference/services/SoftLayer_Hardware_Router/getFrontendNetworkComponents)
Retrieve a piece of hardware's front-end or public network components.
</div>

<div class="method-row">

#### [getFrontendOutgoingBandwidth](/reference/services/SoftLayer_Hardware_Router/getFrontendOutgoingBandwidth)
Retrieve the amount of outgoing public network bandwidth used by a server over a period of time. 
</div>

<div class="method-row">

#### [getFrontendRouters](/reference/services/SoftLayer_Hardware_Router/getFrontendRouters)
Retrieve a hardware's frontend or public router.
</div>

<div class="method-row">

#### [getGlobalIdentifier](/reference/services/SoftLayer_Hardware_Router/getGlobalIdentifier)
Retrieve a hardware's universally unique identifier.
</div>

<div class="method-row">

#### [getHardDrives](/reference/services/SoftLayer_Hardware_Router/getHardDrives)
Retrieve the hard drives contained within a piece of hardware.
</div>

<div class="method-row">

#### [getHardwareChassis](/reference/services/SoftLayer_Hardware_Router/getHardwareChassis)
Retrieve the chassis that a piece of hardware is housed in.
</div>

<div class="method-row">

#### [getHardwareFunction](/reference/services/SoftLayer_Hardware_Router/getHardwareFunction)
Retrieve a hardware's function.
</div>

<div class="method-row">

#### [getHardwareFunctionDescription](/reference/services/SoftLayer_Hardware_Router/getHardwareFunctionDescription)
Retrieve a hardware's function.
</div>

<div class="method-row">

#### [getHardwareStatus](/reference/services/SoftLayer_Hardware_Router/getHardwareStatus)
Retrieve a hardware's status.
</div>

<div class="method-row">

#### [getHasTrustedPlatformModuleBillingItemFlag](/reference/services/SoftLayer_Hardware_Router/getHasTrustedPlatformModuleBillingItemFlag)
Retrieve determine in hardware object has TPM enabled.
</div>

<div class="method-row">

#### [getHostIpsSoftwareComponent](/reference/services/SoftLayer_Hardware_Router/getHostIpsSoftwareComponent)
Retrieve information regarding a host IPS software component object.
</div>

<div class="method-row">

#### [getHourlyBandwidth](/reference/services/SoftLayer_Hardware_Router/getHourlyBandwidth)
Retrieves bandwidth hourly over a 24-hour period for the specified hardware.
</div>

<div class="method-row">

#### [getHourlyBillingFlag](/reference/services/SoftLayer_Hardware_Router/getHourlyBillingFlag)
Retrieve a server's hourly billing status.
</div>

<div class="method-row">

#### [getInboundBandwidthUsage](/reference/services/SoftLayer_Hardware_Router/getInboundBandwidthUsage)
Retrieve the sum of all the inbound network traffic data for the last 30 days.
</div>

<div class="method-row">

#### [getInboundPublicBandwidthUsage](/reference/services/SoftLayer_Hardware_Router/getInboundPublicBandwidthUsage)
Retrieve the total public inbound bandwidth for this hardware for the current billing cycle.
</div>

<div class="method-row">

#### [getLastTransaction](/reference/services/SoftLayer_Hardware_Router/getLastTransaction)
Retrieve information regarding the last transaction a server performed.
</div>

<div class="method-row">

#### [getLatestNetworkMonitorIncident](/reference/services/SoftLayer_Hardware_Router/getLatestNetworkMonitorIncident)
Retrieve a piece of hardware's latest network monitoring incident.
</div>

<div class="method-row">

#### [getLocalDiskStorageCapabilityFlag](/reference/services/SoftLayer_Hardware_Router/getLocalDiskStorageCapabilityFlag)
Retrieve a flag indicating that a VLAN on the router can be assigned to a host that has local disk functionality.
</div>

<div class="method-row">

#### [getLocation](/reference/services/SoftLayer_Hardware_Router/getLocation)
Retrieve where a piece of hardware is located within SoftLayer's location hierarchy.
</div>

<div class="method-row">

#### [getLocationPathString](/reference/services/SoftLayer_Hardware_Router/getLocationPathString)

</div>

<div class="method-row">

#### [getLockboxNetworkStorage](/reference/services/SoftLayer_Hardware_Router/getLockboxNetworkStorage)
Retrieve information regarding a lockbox account associated with a server.
</div>

<div class="method-row">

#### [getManagedResourceFlag](/reference/services/SoftLayer_Hardware_Router/getManagedResourceFlag)
Retrieve a flag indicating that the hardware is a managed resource.
</div>

<div class="method-row">

#### [getMemory](/reference/services/SoftLayer_Hardware_Router/getMemory)
Retrieve information regarding a piece of hardware's memory.
</div>

<div class="method-row">

#### [getMemoryCapacity](/reference/services/SoftLayer_Hardware_Router/getMemoryCapacity)
Retrieve the amount of memory a piece of hardware has, measured in gigabytes.
</div>

<div class="method-row">

#### [getMetricTrackingObject](/reference/services/SoftLayer_Hardware_Router/getMetricTrackingObject)
Retrieve a piece of hardware's metric tracking object.
</div>

<div class="method-row">

#### [getModules](/reference/services/SoftLayer_Hardware_Router/getModules)

</div>

<div class="method-row">

#### [getMonitoringRobot](/reference/services/SoftLayer_Hardware_Router/getMonitoringRobot)
Retrieve information regarding the hardware's monitoring robot.
</div>

<div class="method-row">

#### [getMonitoringServiceComponent](/reference/services/SoftLayer_Hardware_Router/getMonitoringServiceComponent)
Retrieve information regarding a piece of hardware's network monitoring services.
</div>

<div class="method-row">

#### [getMonitoringServiceEligibilityFlag](/reference/services/SoftLayer_Hardware_Router/getMonitoringServiceEligibilityFlag)
Retrieve the monitoring service flag eligibility status for a piece of hardware.
</div>

<div class="method-row">

#### [getMotherboard](/reference/services/SoftLayer_Hardware_Router/getMotherboard)
Retrieve information regarding a piece of hardware's motherboard.
</div>

<div class="method-row">

#### [getNetworkCards](/reference/services/SoftLayer_Hardware_Router/getNetworkCards)
Retrieve information regarding a piece of hardware's network cards.
</div>

<div class="method-row">

#### [getNetworkComponents](/reference/services/SoftLayer_Hardware_Router/getNetworkComponents)
Retrieve returns a hardware's network components.
</div>

<div class="method-row">

#### [getNetworkGatewayMember](/reference/services/SoftLayer_Hardware_Router/getNetworkGatewayMember)
Retrieve the gateway member if this device is part of a network gateway.
</div>

<div class="method-row">

#### [getNetworkGatewayMemberFlag](/reference/services/SoftLayer_Hardware_Router/getNetworkGatewayMemberFlag)
Retrieve whether or not this device is part of a network gateway.
</div>

<div class="method-row">

#### [getNetworkMonitorAttachedDownHardware](/reference/services/SoftLayer_Hardware_Router/getNetworkMonitorAttachedDownHardware)
Retrieve all servers with failed monitoring that are attached downstream to a piece of hardware.
</div>

<div class="method-row">

#### [getNetworkMonitorAttachedDownVirtualGuests](/reference/services/SoftLayer_Hardware_Router/getNetworkMonitorAttachedDownVirtualGuests)
Retrieve virtual guests that are attached downstream to a hardware that have failed monitoring
</div>

<div class="method-row">

#### [getNetworkMonitorIncidents](/reference/services/SoftLayer_Hardware_Router/getNetworkMonitorIncidents)
Retrieve the status of all of a piece of hardware's network monitoring incidents.
</div>

<div class="method-row">

#### [getNetworkMonitors](/reference/services/SoftLayer_Hardware_Router/getNetworkMonitors)
Retrieve information regarding a piece of hardware's network monitors.
</div>

<div class="method-row">

#### [getNetworkStatus](/reference/services/SoftLayer_Hardware_Router/getNetworkStatus)
Retrieve the value of a hardware's network status attribute.
</div>

<div class="method-row">

#### [getNetworkStatusAttribute](/reference/services/SoftLayer_Hardware_Router/getNetworkStatusAttribute)
Retrieve the hardware's related network status attribute.
</div>

<div class="method-row">

#### [getNetworkStorage](/reference/services/SoftLayer_Hardware_Router/getNetworkStorage)
Retrieve information regarding a piece of hardware's associated network storage service account.
</div>

<div class="method-row">

#### [getNextBillingCycleBandwidthAllocation](/reference/services/SoftLayer_Hardware_Router/getNextBillingCycleBandwidthAllocation)
Retrieve a hardware's allotted bandwidth for the next billing cycle (measured in GB).
</div>

<div class="method-row">

#### [getNotesHistory](/reference/services/SoftLayer_Hardware_Router/getNotesHistory)

</div>

<div class="method-row">

#### [getNvRamCapacity](/reference/services/SoftLayer_Hardware_Router/getNvRamCapacity)
Retrieve the amount of non-volatile memory a piece of hardware has, measured in gigabytes.
</div>

<div class="method-row">

#### [getNvRamComponentModels](/reference/services/SoftLayer_Hardware_Router/getNvRamComponentModels)

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Hardware_Router/getObject)
Retrieve a SoftLayer_Hardware_Router record.
</div>

<div class="method-row">

#### [getOperatingSystem](/reference/services/SoftLayer_Hardware_Router/getOperatingSystem)
Retrieve information regarding a piece of hardware's operating system.
</div>

<div class="method-row">

#### [getOperatingSystemReferenceCode](/reference/services/SoftLayer_Hardware_Router/getOperatingSystemReferenceCode)
Retrieve a hardware's operating system software description.
</div>

<div class="method-row">

#### [getOutboundBandwidthUsage](/reference/services/SoftLayer_Hardware_Router/getOutboundBandwidthUsage)
Retrieve the sum of all the outbound network traffic data for the last 30 days.
</div>

<div class="method-row">

#### [getOutboundPublicBandwidthUsage](/reference/services/SoftLayer_Hardware_Router/getOutboundPublicBandwidthUsage)
Retrieve the total public outbound bandwidth for this hardware for the current billing cycle.
</div>

<div class="method-row">

#### [getParentBay](/reference/services/SoftLayer_Hardware_Router/getParentBay)
Retrieve blade Bay
</div>

<div class="method-row">

#### [getParentHardware](/reference/services/SoftLayer_Hardware_Router/getParentHardware)
Retrieve parent Hardware.
</div>

<div class="method-row">

#### [getPointOfPresenceLocation](/reference/services/SoftLayer_Hardware_Router/getPointOfPresenceLocation)
Retrieve information regarding the Point of Presence (PoP) location in which a piece of hardware resides.
</div>

<div class="method-row">

#### [getPowerComponents](/reference/services/SoftLayer_Hardware_Router/getPowerComponents)
Retrieve the power components for a hardware object.
</div>

<div class="method-row">

#### [getPowerSupply](/reference/services/SoftLayer_Hardware_Router/getPowerSupply)
Retrieve information regarding a piece of hardware's power supply.
</div>

<div class="method-row">

#### [getPrimaryBackendNetworkComponent](/reference/services/SoftLayer_Hardware_Router/getPrimaryBackendNetworkComponent)
Retrieve information regarding the hardware's primary back-end network component.
</div>

<div class="method-row">

#### [getPrimaryNetworkComponent](/reference/services/SoftLayer_Hardware_Router/getPrimaryNetworkComponent)
Retrieve information regarding the hardware's primary public network component.
</div>

<div class="method-row">

#### [getPrivateBandwidthData](/reference/services/SoftLayer_Hardware_Router/getPrivateBandwidthData)
Retrieve a graph of a server's private network usage.
</div>

<div class="method-row">

#### [getPrivateNetworkOnlyFlag](/reference/services/SoftLayer_Hardware_Router/getPrivateNetworkOnlyFlag)
Retrieve whether the hardware only has access to the private network.
</div>

<div class="method-row">

#### [getProcessorCoreAmount](/reference/services/SoftLayer_Hardware_Router/getProcessorCoreAmount)
Retrieve the total number of processor cores, summed from all processors that are attached to a piece of hardware
</div>

<div class="method-row">

#### [getProcessorPhysicalCoreAmount](/reference/services/SoftLayer_Hardware_Router/getProcessorPhysicalCoreAmount)
Retrieve the total number of physical processor cores, summed from all processors that are attached to a piece of hardware
</div>

<div class="method-row">

#### [getProcessors](/reference/services/SoftLayer_Hardware_Router/getProcessors)
Retrieve information regarding a piece of hardware's processors.
</div>

<div class="method-row">

#### [getPublicBandwidthData](/reference/services/SoftLayer_Hardware_Router/getPublicBandwidthData)
Retrieve a graph of a server's public network usage.
</div>

<div class="method-row">

#### [getRack](/reference/services/SoftLayer_Hardware_Router/getRack)

</div>

<div class="method-row">

#### [getRaidControllers](/reference/services/SoftLayer_Hardware_Router/getRaidControllers)
Retrieve the RAID controllers contained within a piece of hardware.
</div>

<div class="method-row">

#### [getRecentEvents](/reference/services/SoftLayer_Hardware_Router/getRecentEvents)
Retrieve recent events that impact this hardware.
</div>

<div class="method-row">

#### [getRemoteManagementAccounts](/reference/services/SoftLayer_Hardware_Router/getRemoteManagementAccounts)
Retrieve user credentials to issue commands and/or interact with the server's remote management card.
</div>

<div class="method-row">

#### [getRemoteManagementComponent](/reference/services/SoftLayer_Hardware_Router/getRemoteManagementComponent)
Retrieve a hardware's associated remote management component. This is normally IPMI.
</div>

<div class="method-row">

#### [getResourceConfigurations](/reference/services/SoftLayer_Hardware_Router/getResourceConfigurations)

</div>

<div class="method-row">

#### [getResourceGroupMemberReferences](/reference/services/SoftLayer_Hardware_Router/getResourceGroupMemberReferences)

</div>

<div class="method-row">

#### [getResourceGroupRoles](/reference/services/SoftLayer_Hardware_Router/getResourceGroupRoles)

</div>

<div class="method-row">

#### [getResourceGroups](/reference/services/SoftLayer_Hardware_Router/getResourceGroups)
Retrieve the resource groups in which this hardware is a member.
</div>

<div class="method-row">

#### [getRouters](/reference/services/SoftLayer_Hardware_Router/getRouters)
Retrieve a hardware's routers.
</div>

<div class="method-row">

#### [getSanStorageCapabilityFlag](/reference/services/SoftLayer_Hardware_Router/getSanStorageCapabilityFlag)
Retrieve a flag indicating that a VLAN on the router can be assigned to a host that has SAN disk functionality.
</div>

<div class="method-row">

#### [getScaleAssets](/reference/services/SoftLayer_Hardware_Router/getScaleAssets)
Retrieve collection of scale assets this hardware corresponds to.
</div>

<div class="method-row">

#### [getSecurityScanRequests](/reference/services/SoftLayer_Hardware_Router/getSecurityScanRequests)
Retrieve information regarding a piece of hardware's vulnerability scan requests.
</div>

<div class="method-row">

#### [getSensorData](/reference/services/SoftLayer_Hardware_Router/getSensorData)
Retrieve a server's hardware state via its internal sensors
</div>

<div class="method-row">

#### [getSensorDataWithGraphs](/reference/services/SoftLayer_Hardware_Router/getSensorDataWithGraphs)
Retrieve server's temperature and fan speed graphs as well the sensor raw data.
</div>

<div class="method-row">

#### [getServerFanSpeedGraphs](/reference/services/SoftLayer_Hardware_Router/getServerFanSpeedGraphs)
Retrieve a server's fan speed graphs.
</div>

<div class="method-row">

#### [getServerPowerState](/reference/services/SoftLayer_Hardware_Router/getServerPowerState)
Retrieves a server's power state.
</div>

<div class="method-row">

#### [getServerRoom](/reference/services/SoftLayer_Hardware_Router/getServerRoom)
Retrieve information regarding the server room in which the hardware is located.
</div>

<div class="method-row">

#### [getServerTemperatureGraphs](/reference/services/SoftLayer_Hardware_Router/getServerTemperatureGraphs)
Retrieve server's temperature graphs
</div>

<div class="method-row">

#### [getServiceProvider](/reference/services/SoftLayer_Hardware_Router/getServiceProvider)
Retrieve information regarding the piece of hardware's service provider.
</div>

<div class="method-row">

#### [getSoftwareComponents](/reference/services/SoftLayer_Hardware_Router/getSoftwareComponents)
Retrieve information regarding a piece of hardware's installed software.
</div>

<div class="method-row">

#### [getSparePoolBillingItem](/reference/services/SoftLayer_Hardware_Router/getSparePoolBillingItem)
Retrieve information regarding the billing item for a spare pool server.
</div>

<div class="method-row">

#### [getSshKeys](/reference/services/SoftLayer_Hardware_Router/getSshKeys)
Retrieve sSH keys to be installed on the server during provisioning or an OS reload.
</div>

<div class="method-row">

#### [getStorageGroups](/reference/services/SoftLayer_Hardware_Router/getStorageGroups)

</div>

<div class="method-row">

#### [getStorageNetworkComponents](/reference/services/SoftLayer_Hardware_Router/getStorageNetworkComponents)
Retrieve a piece of hardware's private storage network components. [Deprecated]
</div>

<div class="method-row">

#### [getTagReferences](/reference/services/SoftLayer_Hardware_Router/getTagReferences)

</div>

<div class="method-row">

#### [getTopLevelLocation](/reference/services/SoftLayer_Hardware_Router/getTopLevelLocation)

</div>

<div class="method-row">

#### [getTransactionHistory](/reference/services/SoftLayer_Hardware_Router/getTransactionHistory)
Get transaction history for a piece of hardware.
</div>

<div class="method-row">

#### [getUpgradeItemPrices](/reference/services/SoftLayer_Hardware_Router/getUpgradeItemPrices)
Retrieve a list of upgradable items available to a piece of hardware.
</div>

<div class="method-row">

#### [getUpgradeRequest](/reference/services/SoftLayer_Hardware_Router/getUpgradeRequest)
Retrieve an account's associated upgrade request object, if any.
</div>

<div class="method-row">

#### [getUplinkHardware](/reference/services/SoftLayer_Hardware_Router/getUplinkHardware)
Retrieve the network device connected to a piece of hardware.
</div>

<div class="method-row">

#### [getUplinkNetworkComponents](/reference/services/SoftLayer_Hardware_Router/getUplinkNetworkComponents)
Retrieve information regarding the network component that is one level higher than a piece of hardware on the network infrastructure.
</div>

<div class="method-row">

#### [getUserData](/reference/services/SoftLayer_Hardware_Router/getUserData)
Retrieve an array containing a single string of custom user data for a hardware order. Max size is 16 kb.
</div>

<div class="method-row">

#### [getVirtualChassis](/reference/services/SoftLayer_Hardware_Router/getVirtualChassis)
Retrieve information regarding the virtual chassis for a piece of hardware.
</div>

<div class="method-row">

#### [getVirtualChassisSiblings](/reference/services/SoftLayer_Hardware_Router/getVirtualChassisSiblings)
Retrieve information regarding the virtual chassis siblings for a piece of hardware.
</div>

<div class="method-row">

#### [getVirtualHost](/reference/services/SoftLayer_Hardware_Router/getVirtualHost)
Retrieve a piece of hardware's virtual host record.
</div>

<div class="method-row">

#### [getVirtualLicenses](/reference/services/SoftLayer_Hardware_Router/getVirtualLicenses)
Retrieve information regarding a piece of hardware's virtual software licenses.
</div>

<div class="method-row">

#### [getVirtualRack](/reference/services/SoftLayer_Hardware_Router/getVirtualRack)
Retrieve information regarding the bandwidth allotment to which a piece of hardware belongs.
</div>

<div class="method-row">

#### [getVirtualRackId](/reference/services/SoftLayer_Hardware_Router/getVirtualRackId)
Retrieve the name of the bandwidth allotment belonging to a piece of hardware.
</div>

<div class="method-row">

#### [getVirtualRackName](/reference/services/SoftLayer_Hardware_Router/getVirtualRackName)
Retrieve the name of the bandwidth allotment belonging to a piece of hardware.
</div>

<div class="method-row">

#### [getVirtualizationPlatform](/reference/services/SoftLayer_Hardware_Router/getVirtualizationPlatform)
Retrieve a piece of hardware's virtualization platform software.
</div>

<div class="method-row">

#### [importVirtualHost](/reference/services/SoftLayer_Hardware_Router/importVirtualHost)
attempt to import the host record for the virtualization platform running on a server
</div>

<div class="method-row">

#### [isPingable](/reference/services/SoftLayer_Hardware_Router/isPingable)
Verifies whether or not a server is pingable.
</div>

<div class="method-row">

#### [ping](/reference/services/SoftLayer_Hardware_Router/ping)
Issues ping command.
</div>

<div class="method-row">

#### [powerCycle](/reference/services/SoftLayer_Hardware_Router/powerCycle)
Issues power cycle to server.
</div>

<div class="method-row">

#### [powerOff](/reference/services/SoftLayer_Hardware_Router/powerOff)
Power off server.
</div>

<div class="method-row">

#### [powerOn](/reference/services/SoftLayer_Hardware_Router/powerOn)
Power on server.
</div>

<div class="method-row">

#### [rebootDefault](/reference/services/SoftLayer_Hardware_Router/rebootDefault)
Reboot the server via the default method.
</div>

<div class="method-row">

#### [rebootHard](/reference/services/SoftLayer_Hardware_Router/rebootHard)
Reboot the server via "hard" reboot.
</div>

<div class="method-row">

#### [rebootSoft](/reference/services/SoftLayer_Hardware_Router/rebootSoft)
Execute a soft reboot to the server.
</div>

<div class="method-row">

#### [removeAccessToNetworkStorage](/reference/services/SoftLayer_Hardware_Router/removeAccessToNetworkStorage)
Remove access to a SoftLayer_Network_Storage volume from this device. 
</div>

<div class="method-row">

#### [removeAccessToNetworkStorageList](/reference/services/SoftLayer_Hardware_Router/removeAccessToNetworkStorageList)
Remove access to multiple SoftLayer_Network_Storage volumes from this device. 
</div>

<div class="method-row">

#### [removeTags](/reference/services/SoftLayer_Hardware_Router/removeTags)
Remove a tag reference
</div>

<div class="method-row">

#### [setTags](/reference/services/SoftLayer_Hardware_Router/setTags)

</div>

<div class="method-row">

#### [updateIpmiPassword](/reference/services/SoftLayer_Hardware_Router/updateIpmiPassword)
Update the root IPMI user password 
</div>
</div>

</div>

