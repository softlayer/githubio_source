---
title: "SoftLayer_Hardware"
description: "Every SoftLayer hardware is defined in the SoftLayer_Hardware service. SoftLayer hardware has network components, softwa... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
---
# SoftLayer_Hardware
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Hardware' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware' >Datatype</a></li>
    </ul>
</div>

## Description
Every SoftLayer hardware is defined in the SoftLayer_Hardware service. SoftLayer hardware has network components, software, monitoring services such as network monitoring, and hardware components such as hard drives. The SoftLayer_Hardware service is a convenient way to obtain general information about your SoftLayer hardware. Use the data returned by these methods with other API services to get more detailed information about your services and to make changes to your servers and services. 



        
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

#### [allowAccessToNetworkStorage](/reference/services/SoftLayer_Hardware/allowAccessToNetworkStorage)
Allow access to a SoftLayer_Network_Storage volume from this device. 

#### [allowAccessToNetworkStorageList](/reference/services/SoftLayer_Hardware/allowAccessToNetworkStorageList)
Allow access to multiple SoftLayer_Network_Storage volumes from this device. 

#### [captureImage](/reference/services/SoftLayer_Hardware/captureImage)
Captures a Flex Image of the hard disk on the physical machine.

#### [closeAlarm](/reference/services/SoftLayer_Hardware/closeAlarm)
Returns monitoring alarm detailed history

#### [createObject](/reference/services/SoftLayer_Hardware/createObject)
Create a new server

#### [deleteObject](/reference/services/SoftLayer_Hardware/deleteObject)
Delete a server

#### [deleteSoftwareComponentPasswords](/reference/services/SoftLayer_Hardware/deleteSoftwareComponentPasswords)
Delete software component passwords.

#### [deleteTag](/reference/services/SoftLayer_Hardware/deleteTag)
Delete a tag

#### [editSoftwareComponentPasswords](/reference/services/SoftLayer_Hardware/editSoftwareComponentPasswords)
Edit the properties of software component passwords.

#### [executeRemoteScript](/reference/services/SoftLayer_Hardware/executeRemoteScript)
Download and run remote script from uri on the hardware. Requires https for script to be executed after download. 

#### [findByIpAddress](/reference/services/SoftLayer_Hardware/findByIpAddress)
Find hardware by its primary public or private IP (ipv4) address.

#### [generateOrderTemplate](/reference/services/SoftLayer_Hardware/generateOrderTemplate)
Obtain an order container for a given template object

#### [getAccount](/reference/services/SoftLayer_Hardware/getAccount)
Retrieve the account associated with a piece of hardware.

#### [getActiveComponents](/reference/services/SoftLayer_Hardware/getActiveComponents)
Retrieve a piece of hardware's active physical components.

#### [getActiveNetworkMonitorIncident](/reference/services/SoftLayer_Hardware/getActiveNetworkMonitorIncident)
Retrieve a piece of hardware's active network monitoring incidents.

#### [getAlarmHistory](/reference/services/SoftLayer_Hardware/getAlarmHistory)
Returns monitoring alarm detailed history

#### [getAllPowerComponents](/reference/services/SoftLayer_Hardware/getAllPowerComponents)


#### [getAllowedHost](/reference/services/SoftLayer_Hardware/getAllowedHost)
Retrieve the SoftLayer_Network_Storage_Allowed_Host information to connect this server to Network Storage volumes that require access control lists.

#### [getAllowedNetworkStorage](/reference/services/SoftLayer_Hardware/getAllowedNetworkStorage)
Retrieve the SoftLayer_Network_Storage objects that this SoftLayer_Hardware has access to.

#### [getAllowedNetworkStorageReplicas](/reference/services/SoftLayer_Hardware/getAllowedNetworkStorageReplicas)
Retrieve the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to.

#### [getAntivirusSpywareSoftwareComponent](/reference/services/SoftLayer_Hardware/getAntivirusSpywareSoftwareComponent)
Retrieve information regarding an antivirus/spyware software component object.

#### [getAttachedNetworkStorages](/reference/services/SoftLayer_Hardware/getAttachedNetworkStorages)
Return a list of SoftLayer_Network_Storage volumes authorized to this device. 

#### [getAttributes](/reference/services/SoftLayer_Hardware/getAttributes)
Retrieve information regarding a piece of hardware's specific attributes.

#### [getAvailableNetworkStorages](/reference/services/SoftLayer_Hardware/getAvailableNetworkStorages)
Return a list of SoftLayer_Network_Storage volumes that can be authorized to this device. 

#### [getAverageDailyPublicBandwidthUsage](/reference/services/SoftLayer_Hardware/getAverageDailyPublicBandwidthUsage)
Retrieve the average daily public bandwidth usage for the current billing cycle.

#### [getBackendIncomingBandwidth](/reference/services/SoftLayer_Hardware/getBackendIncomingBandwidth)
Retrieve the amount of incoming private network bandwidth used by a server over a period of time. 

#### [getBackendNetworkComponents](/reference/services/SoftLayer_Hardware/getBackendNetworkComponents)
Retrieve a piece of hardware's back-end or private network components.

#### [getBackendOutgoingBandwidth](/reference/services/SoftLayer_Hardware/getBackendOutgoingBandwidth)
Retrieve the amount of outgoing private network bandwidth used by a server over a period of time. 

#### [getBackendRouters](/reference/services/SoftLayer_Hardware/getBackendRouters)
Retrieve a hardware's backend or private router.

#### [getBandwidthAllocation](/reference/services/SoftLayer_Hardware/getBandwidthAllocation)
Retrieve a hardware's allotted bandwidth (measured in GB).

#### [getBandwidthAllotmentDetail](/reference/services/SoftLayer_Hardware/getBandwidthAllotmentDetail)
Retrieve a hardware's allotted detail record. Allotment details link bandwidth allocation with allotments.

#### [getBenchmarkCertifications](/reference/services/SoftLayer_Hardware/getBenchmarkCertifications)
Retrieve information regarding a piece of hardware's benchmark certifications.

#### [getBillingItem](/reference/services/SoftLayer_Hardware/getBillingItem)
Retrieve information regarding the billing item for a server.

#### [getBillingItemFlag](/reference/services/SoftLayer_Hardware/getBillingItemFlag)
Retrieve a flag indicating that a billing item exists.

#### [getBlockCancelBecauseDisconnectedFlag](/reference/services/SoftLayer_Hardware/getBlockCancelBecauseDisconnectedFlag)
Retrieve determines whether the hardware is ineligible for cancellation because it is disconnected.

#### [getBusinessContinuanceInsuranceFlag](/reference/services/SoftLayer_Hardware/getBusinessContinuanceInsuranceFlag)
Retrieve status indicating whether or not a piece of hardware has business continuance insurance.

#### [getChildrenHardware](/reference/services/SoftLayer_Hardware/getChildrenHardware)
Retrieve child hardware.

#### [getComponentDetailsXML](/reference/services/SoftLayer_Hardware/getComponentDetailsXML)


#### [getComponents](/reference/services/SoftLayer_Hardware/getComponents)
Retrieve a piece of hardware's components.

#### [getContinuousDataProtectionSoftwareComponent](/reference/services/SoftLayer_Hardware/getContinuousDataProtectionSoftwareComponent)
Retrieve a continuous data protection/server backup software component object.

#### [getCreateObjectOptions](/reference/services/SoftLayer_Hardware/getCreateObjectOptions)
Determine options available when creating a server

#### [getCurrentBillableBandwidthUsage](/reference/services/SoftLayer_Hardware/getCurrentBillableBandwidthUsage)
Retrieve the current billable public outbound bandwidth for this hardware for the current billing cycle.

#### [getCurrentBillingDetail](/reference/services/SoftLayer_Hardware/getCurrentBillingDetail)
<< EOT

#### [getCurrentBillingTotal](/reference/services/SoftLayer_Hardware/getCurrentBillingTotal)
Get the billing total for this instance's usage up to this point. This total includes all bandwidth charges. 

#### [getDailyAverage](/reference/services/SoftLayer_Hardware/getDailyAverage)
calculate the average daily network traffic used by a server in gigabytes.

#### [getDatacenter](/reference/services/SoftLayer_Hardware/getDatacenter)
Retrieve information regarding the datacenter in which a piece of hardware resides.

#### [getDatacenterName](/reference/services/SoftLayer_Hardware/getDatacenterName)
Retrieve the name of the datacenter in which a piece of hardware resides.

#### [getDaysInSparePool](/reference/services/SoftLayer_Hardware/getDaysInSparePool)
Retrieve number of day(s) a server have been in spare pool.

#### [getDownlinkHardware](/reference/services/SoftLayer_Hardware/getDownlinkHardware)
Retrieve all hardware that has uplink network connections to a piece of hardware.

#### [getDownlinkNetworkHardware](/reference/services/SoftLayer_Hardware/getDownlinkNetworkHardware)
Retrieve all hardware that has uplink network connections to a piece of hardware.

#### [getDownlinkServers](/reference/services/SoftLayer_Hardware/getDownlinkServers)
Retrieve information regarding all servers attached to a piece of network hardware.

#### [getDownlinkVirtualGuests](/reference/services/SoftLayer_Hardware/getDownlinkVirtualGuests)
Retrieve information regarding all virtual guests attached to a piece of network hardware.

#### [getDownstreamHardwareBindings](/reference/services/SoftLayer_Hardware/getDownstreamHardwareBindings)
Retrieve all hardware downstream from a network device.

#### [getDownstreamNetworkHardware](/reference/services/SoftLayer_Hardware/getDownstreamNetworkHardware)
Retrieve all network hardware downstream from the selected piece of hardware.

#### [getDownstreamNetworkHardwareWithIncidents](/reference/services/SoftLayer_Hardware/getDownstreamNetworkHardwareWithIncidents)
Retrieve all network hardware with monitoring warnings or errors that are downstream from the selected piece of hardware.

#### [getDownstreamServers](/reference/services/SoftLayer_Hardware/getDownstreamServers)
Retrieve information regarding all servers attached downstream to a piece of network hardware.

#### [getDownstreamVirtualGuests](/reference/services/SoftLayer_Hardware/getDownstreamVirtualGuests)
Retrieve information regarding all virtual guests attached to a piece of network hardware.

#### [getDriveControllers](/reference/services/SoftLayer_Hardware/getDriveControllers)
Retrieve the drive controllers contained within a piece of hardware.

#### [getEvaultNetworkStorage](/reference/services/SoftLayer_Hardware/getEvaultNetworkStorage)
Retrieve information regarding a piece of hardware's associated EVault network storage service account.

#### [getFirewallServiceComponent](/reference/services/SoftLayer_Hardware/getFirewallServiceComponent)
Retrieve information regarding a piece of hardware's firewall services.

#### [getFixedConfigurationPreset](/reference/services/SoftLayer_Hardware/getFixedConfigurationPreset)
Retrieve defines the fixed components in a fixed configuration bare metal server.

#### [getFrontendIncomingBandwidth](/reference/services/SoftLayer_Hardware/getFrontendIncomingBandwidth)
Retrieve the amount of incoming public network bandwidth used by a server over a period of time. 

#### [getFrontendNetworkComponents](/reference/services/SoftLayer_Hardware/getFrontendNetworkComponents)
Retrieve a piece of hardware's front-end or public network components.

#### [getFrontendOutgoingBandwidth](/reference/services/SoftLayer_Hardware/getFrontendOutgoingBandwidth)
Retrieve the amount of outgoing public network bandwidth used by a server over a period of time. 

#### [getFrontendRouters](/reference/services/SoftLayer_Hardware/getFrontendRouters)
Retrieve a hardware's frontend or public router.

#### [getGlobalIdentifier](/reference/services/SoftLayer_Hardware/getGlobalIdentifier)
Retrieve a hardware's universally unique identifier.

#### [getHardDrives](/reference/services/SoftLayer_Hardware/getHardDrives)
Retrieve the hard drives contained within a piece of hardware.

#### [getHardwareChassis](/reference/services/SoftLayer_Hardware/getHardwareChassis)
Retrieve the chassis that a piece of hardware is housed in.

#### [getHardwareFunction](/reference/services/SoftLayer_Hardware/getHardwareFunction)
Retrieve a hardware's function.

#### [getHardwareFunctionDescription](/reference/services/SoftLayer_Hardware/getHardwareFunctionDescription)
Retrieve a hardware's function.

#### [getHardwareStatus](/reference/services/SoftLayer_Hardware/getHardwareStatus)
Retrieve a hardware's status.

#### [getHasTrustedPlatformModuleBillingItemFlag](/reference/services/SoftLayer_Hardware/getHasTrustedPlatformModuleBillingItemFlag)
Retrieve determine in hardware object has TPM enabled.

#### [getHostIpsSoftwareComponent](/reference/services/SoftLayer_Hardware/getHostIpsSoftwareComponent)
Retrieve information regarding a host IPS software component object.

#### [getHourlyBandwidth](/reference/services/SoftLayer_Hardware/getHourlyBandwidth)
Retrieves bandwidth hourly over a 24-hour period for the specified hardware.

#### [getHourlyBillingFlag](/reference/services/SoftLayer_Hardware/getHourlyBillingFlag)
Retrieve a server's hourly billing status.

#### [getInboundBandwidthUsage](/reference/services/SoftLayer_Hardware/getInboundBandwidthUsage)
Retrieve the sum of all the inbound network traffic data for the last 30 days.

#### [getInboundPublicBandwidthUsage](/reference/services/SoftLayer_Hardware/getInboundPublicBandwidthUsage)
Retrieve the total public inbound bandwidth for this hardware for the current billing cycle.

#### [getLastTransaction](/reference/services/SoftLayer_Hardware/getLastTransaction)
Retrieve information regarding the last transaction a server performed.

#### [getLatestNetworkMonitorIncident](/reference/services/SoftLayer_Hardware/getLatestNetworkMonitorIncident)
Retrieve a piece of hardware's latest network monitoring incident.

#### [getLocation](/reference/services/SoftLayer_Hardware/getLocation)
Retrieve where a piece of hardware is located within SoftLayer's location hierarchy.

#### [getLocationPathString](/reference/services/SoftLayer_Hardware/getLocationPathString)


#### [getLockboxNetworkStorage](/reference/services/SoftLayer_Hardware/getLockboxNetworkStorage)
Retrieve information regarding a lockbox account associated with a server.

#### [getManagedResourceFlag](/reference/services/SoftLayer_Hardware/getManagedResourceFlag)
Retrieve a flag indicating that the hardware is a managed resource.

#### [getMemory](/reference/services/SoftLayer_Hardware/getMemory)
Retrieve information regarding a piece of hardware's memory.

#### [getMemoryCapacity](/reference/services/SoftLayer_Hardware/getMemoryCapacity)
Retrieve the amount of memory a piece of hardware has, measured in gigabytes.

#### [getMetricTrackingObject](/reference/services/SoftLayer_Hardware/getMetricTrackingObject)
Retrieve a piece of hardware's metric tracking object.

#### [getModules](/reference/services/SoftLayer_Hardware/getModules)


#### [getMonitoringActiveAlarms](/reference/services/SoftLayer_Hardware/getMonitoringActiveAlarms)
Returns open monitoring alarms for a given time period

#### [getMonitoringAgents](/reference/services/SoftLayer_Hardware/getMonitoringAgents)
Retrieve information regarding the monitoring agents associated with a piece of hardware.

#### [getMonitoringClosedAlarms](/reference/services/SoftLayer_Hardware/getMonitoringClosedAlarms)
Returns closed monitoring alarms for a given time period

#### [getMonitoringRobot](/reference/services/SoftLayer_Hardware/getMonitoringRobot)
Retrieve information regarding the hardware's monitoring robot.

#### [getMonitoringServiceComponent](/reference/services/SoftLayer_Hardware/getMonitoringServiceComponent)
Retrieve information regarding a piece of hardware's network monitoring services.

#### [getMonitoringServiceEligibilityFlag](/reference/services/SoftLayer_Hardware/getMonitoringServiceEligibilityFlag)
Retrieve the monitoring service flag eligibility status for a piece of hardware.

#### [getMonitoringServiceFlag](/reference/services/SoftLayer_Hardware/getMonitoringServiceFlag)
Retrieve the service flag status for a piece of hardware.

#### [getMotherboard](/reference/services/SoftLayer_Hardware/getMotherboard)
Retrieve information regarding a piece of hardware's motherboard.

#### [getNetworkCards](/reference/services/SoftLayer_Hardware/getNetworkCards)
Retrieve information regarding a piece of hardware's network cards.

#### [getNetworkComponents](/reference/services/SoftLayer_Hardware/getNetworkComponents)
Retrieve returns a hardware's network components.

#### [getNetworkGatewayMember](/reference/services/SoftLayer_Hardware/getNetworkGatewayMember)
Retrieve the gateway member if this device is part of a network gateway.

#### [getNetworkGatewayMemberFlag](/reference/services/SoftLayer_Hardware/getNetworkGatewayMemberFlag)
Retrieve whether or not this device is part of a network gateway.

#### [getNetworkManagementIpAddress](/reference/services/SoftLayer_Hardware/getNetworkManagementIpAddress)
Retrieve a piece of hardware's network management IP address.

#### [getNetworkMonitorAttachedDownHardware](/reference/services/SoftLayer_Hardware/getNetworkMonitorAttachedDownHardware)
Retrieve all servers with failed monitoring that are attached downstream to a piece of hardware.

#### [getNetworkMonitorAttachedDownVirtualGuests](/reference/services/SoftLayer_Hardware/getNetworkMonitorAttachedDownVirtualGuests)
Retrieve virtual guests that are attached downstream to a hardware that have failed monitoring

#### [getNetworkMonitorIncidents](/reference/services/SoftLayer_Hardware/getNetworkMonitorIncidents)
Retrieve the status of all of a piece of hardware's network monitoring incidents.

#### [getNetworkMonitors](/reference/services/SoftLayer_Hardware/getNetworkMonitors)
Retrieve information regarding a piece of hardware's network monitors.

#### [getNetworkStatus](/reference/services/SoftLayer_Hardware/getNetworkStatus)
Retrieve the value of a hardware's network status attribute.

#### [getNetworkStatusAttribute](/reference/services/SoftLayer_Hardware/getNetworkStatusAttribute)
Retrieve the hardware's related network status attribute.

#### [getNetworkStorage](/reference/services/SoftLayer_Hardware/getNetworkStorage)
Retrieve information regarding a piece of hardware's associated network storage service account.

#### [getNetworkVlans](/reference/services/SoftLayer_Hardware/getNetworkVlans)
Retrieve the network virtual LANs (VLANs) associated with a piece of hardware's network components.

#### [getNextBillingCycleBandwidthAllocation](/reference/services/SoftLayer_Hardware/getNextBillingCycleBandwidthAllocation)
Retrieve a hardware's allotted bandwidth for the next billing cycle (measured in GB).

#### [getNotesHistory](/reference/services/SoftLayer_Hardware/getNotesHistory)


#### [getNvRamCapacity](/reference/services/SoftLayer_Hardware/getNvRamCapacity)
Retrieve the amount of non-volatile memory a piece of hardware has, measured in gigabytes.

#### [getNvRamComponentModels](/reference/services/SoftLayer_Hardware/getNvRamComponentModels)


#### [getObject](/reference/services/SoftLayer_Hardware/getObject)
Retrieve a SoftLayer_Hardware record.

#### [getOperatingSystem](/reference/services/SoftLayer_Hardware/getOperatingSystem)
Retrieve information regarding a piece of hardware's operating system.

#### [getOperatingSystemReferenceCode](/reference/services/SoftLayer_Hardware/getOperatingSystemReferenceCode)
Retrieve a hardware's operating system software description.

#### [getOutboundBandwidthUsage](/reference/services/SoftLayer_Hardware/getOutboundBandwidthUsage)
Retrieve the sum of all the outbound network traffic data for the last 30 days.

#### [getOutboundPublicBandwidthUsage](/reference/services/SoftLayer_Hardware/getOutboundPublicBandwidthUsage)
Retrieve the total public outbound bandwidth for this hardware for the current billing cycle.

#### [getParentBay](/reference/services/SoftLayer_Hardware/getParentBay)
Retrieve blade Bay

#### [getParentHardware](/reference/services/SoftLayer_Hardware/getParentHardware)
Retrieve parent Hardware.

#### [getPointOfPresenceLocation](/reference/services/SoftLayer_Hardware/getPointOfPresenceLocation)
Retrieve information regarding the Point of Presence (PoP) location in which a piece of hardware resides.

#### [getPowerComponents](/reference/services/SoftLayer_Hardware/getPowerComponents)
Retrieve the power components for a hardware object.

#### [getPowerSupply](/reference/services/SoftLayer_Hardware/getPowerSupply)
Retrieve information regarding a piece of hardware's power supply.

#### [getPrimaryBackendIpAddress](/reference/services/SoftLayer_Hardware/getPrimaryBackendIpAddress)
Retrieve the hardware's primary private IP address.

#### [getPrimaryBackendNetworkComponent](/reference/services/SoftLayer_Hardware/getPrimaryBackendNetworkComponent)
Retrieve information regarding the hardware's primary back-end network component.

#### [getPrimaryIpAddress](/reference/services/SoftLayer_Hardware/getPrimaryIpAddress)
Retrieve the hardware's primary public IP address.

#### [getPrimaryNetworkComponent](/reference/services/SoftLayer_Hardware/getPrimaryNetworkComponent)
Retrieve information regarding the hardware's primary public network component.

#### [getPrivateBandwidthData](/reference/services/SoftLayer_Hardware/getPrivateBandwidthData)
Retrieve a graph of a server's private network usage.

#### [getPrivateNetworkOnlyFlag](/reference/services/SoftLayer_Hardware/getPrivateNetworkOnlyFlag)
Retrieve whether the hardware only has access to the private network.

#### [getProcessorCoreAmount](/reference/services/SoftLayer_Hardware/getProcessorCoreAmount)
Retrieve the total number of processor cores, summed from all processors that are attached to a piece of hardware

#### [getProcessorPhysicalCoreAmount](/reference/services/SoftLayer_Hardware/getProcessorPhysicalCoreAmount)
Retrieve the total number of physical processor cores, summed from all processors that are attached to a piece of hardware

#### [getProcessors](/reference/services/SoftLayer_Hardware/getProcessors)
Retrieve information regarding a piece of hardware's processors.

#### [getPublicBandwidthData](/reference/services/SoftLayer_Hardware/getPublicBandwidthData)
Retrieve a graph of a server's public network usage.

#### [getRack](/reference/services/SoftLayer_Hardware/getRack)


#### [getRaidControllers](/reference/services/SoftLayer_Hardware/getRaidControllers)
Retrieve the RAID controllers contained within a piece of hardware.

#### [getRecentEvents](/reference/services/SoftLayer_Hardware/getRecentEvents)
Retrieve recent events that impact this hardware.

#### [getRemoteManagementAccounts](/reference/services/SoftLayer_Hardware/getRemoteManagementAccounts)
Retrieve user credentials to issue commands and/or interact with the server's remote management card.

#### [getRemoteManagementComponent](/reference/services/SoftLayer_Hardware/getRemoteManagementComponent)
Retrieve a hardware's associated remote management component. This is normally IPMI.

#### [getResourceConfigurations](/reference/services/SoftLayer_Hardware/getResourceConfigurations)


#### [getResourceGroupMemberReferences](/reference/services/SoftLayer_Hardware/getResourceGroupMemberReferences)


#### [getResourceGroupRoles](/reference/services/SoftLayer_Hardware/getResourceGroupRoles)


#### [getResourceGroups](/reference/services/SoftLayer_Hardware/getResourceGroups)
Retrieve the resource groups in which this hardware is a member.

#### [getRouters](/reference/services/SoftLayer_Hardware/getRouters)
Retrieve a hardware's routers.

#### [getScaleAssets](/reference/services/SoftLayer_Hardware/getScaleAssets)
Retrieve collection of scale assets this hardware corresponds to.

#### [getSecurityScanRequests](/reference/services/SoftLayer_Hardware/getSecurityScanRequests)
Retrieve information regarding a piece of hardware's vulnerability scan requests.

#### [getSensorData](/reference/services/SoftLayer_Hardware/getSensorData)
Retrieve a server's hardware state via its internal sensors

#### [getSensorDataWithGraphs](/reference/services/SoftLayer_Hardware/getSensorDataWithGraphs)
Retrieve server's temperature and fan speed graphs as well the sensor raw data.

#### [getServerFanSpeedGraphs](/reference/services/SoftLayer_Hardware/getServerFanSpeedGraphs)
Retrieve a server's fan speed graphs.

#### [getServerPowerState](/reference/services/SoftLayer_Hardware/getServerPowerState)
Retrieves a server's power state.

#### [getServerRoom](/reference/services/SoftLayer_Hardware/getServerRoom)
Retrieve information regarding the server room in which the hardware is located.

#### [getServerTemperatureGraphs](/reference/services/SoftLayer_Hardware/getServerTemperatureGraphs)
Retrieve server's temperature graphs

#### [getServiceProvider](/reference/services/SoftLayer_Hardware/getServiceProvider)
Retrieve information regarding the piece of hardware's service provider.

#### [getSoftwareComponents](/reference/services/SoftLayer_Hardware/getSoftwareComponents)
Retrieve information regarding a piece of hardware's installed software.

#### [getSparePoolBillingItem](/reference/services/SoftLayer_Hardware/getSparePoolBillingItem)
Retrieve information regarding the billing item for a spare pool server.

#### [getSshKeys](/reference/services/SoftLayer_Hardware/getSshKeys)
Retrieve sSH keys to be installed on the server during provisioning or an OS reload.

#### [getStorageNetworkComponents](/reference/services/SoftLayer_Hardware/getStorageNetworkComponents)


#### [getTagReferences](/reference/services/SoftLayer_Hardware/getTagReferences)


#### [getTopLevelLocation](/reference/services/SoftLayer_Hardware/getTopLevelLocation)


#### [getTransactionHistory](/reference/services/SoftLayer_Hardware/getTransactionHistory)
Get transaction history for a piece of hardware.

#### [getUpgradeItemPrices](/reference/services/SoftLayer_Hardware/getUpgradeItemPrices)
Retrieve a list of upgradable items available to a piece of hardware.

#### [getUpgradeRequest](/reference/services/SoftLayer_Hardware/getUpgradeRequest)
Retrieve an account's associated upgrade request object, if any.

#### [getUplinkHardware](/reference/services/SoftLayer_Hardware/getUplinkHardware)
Retrieve the network device connected to a piece of hardware.

#### [getUplinkNetworkComponents](/reference/services/SoftLayer_Hardware/getUplinkNetworkComponents)
Retrieve information regarding the network component that is one level higher than a piece of hardware on the network infrastructure.

#### [getUserData](/reference/services/SoftLayer_Hardware/getUserData)
Retrieve an array containing a single string of custom user data for a hardware order. Max size is 16 kb.

#### [getVirtualChassis](/reference/services/SoftLayer_Hardware/getVirtualChassis)
Retrieve information regarding the virtual chassis for a piece of hardware.

#### [getVirtualChassisSiblings](/reference/services/SoftLayer_Hardware/getVirtualChassisSiblings)
Retrieve information regarding the virtual chassis siblings for a piece of hardware.

#### [getVirtualHost](/reference/services/SoftLayer_Hardware/getVirtualHost)
Retrieve a piece of hardware's virtual host record.

#### [getVirtualLicenses](/reference/services/SoftLayer_Hardware/getVirtualLicenses)
Retrieve information regarding a piece of hardware's virtual software licenses.

#### [getVirtualRack](/reference/services/SoftLayer_Hardware/getVirtualRack)
Retrieve information regarding the bandwidth allotment to which a piece of hardware belongs.

#### [getVirtualRackId](/reference/services/SoftLayer_Hardware/getVirtualRackId)
Retrieve the name of the bandwidth allotment belonging to a piece of hardware.

#### [getVirtualRackName](/reference/services/SoftLayer_Hardware/getVirtualRackName)
Retrieve the name of the bandwidth allotment belonging to a piece of hardware.

#### [getVirtualizationPlatform](/reference/services/SoftLayer_Hardware/getVirtualizationPlatform)
Retrieve a piece of hardware's virtualization platform software.

#### [importVirtualHost](/reference/services/SoftLayer_Hardware/importVirtualHost)
attempt to import the host record for the virtualization platform running on a server

#### [isPingable](/reference/services/SoftLayer_Hardware/isPingable)
Verifies whether or not a server is pingable.

#### [ping](/reference/services/SoftLayer_Hardware/ping)
Issues ping command.

#### [powerCycle](/reference/services/SoftLayer_Hardware/powerCycle)
Issues power cycle to server.

#### [powerOff](/reference/services/SoftLayer_Hardware/powerOff)
Power off server.

#### [powerOn](/reference/services/SoftLayer_Hardware/powerOn)
Power on server.

#### [rebootDefault](/reference/services/SoftLayer_Hardware/rebootDefault)
Reboot the server via the default method.

#### [rebootHard](/reference/services/SoftLayer_Hardware/rebootHard)
Reboot the server via "hard" reboot.

#### [rebootSoft](/reference/services/SoftLayer_Hardware/rebootSoft)
Execute a soft reboot to the server.

#### [removeAccessToNetworkStorage](/reference/services/SoftLayer_Hardware/removeAccessToNetworkStorage)
Remove access to a SoftLayer_Network_Storage volume from this device. 

#### [removeAccessToNetworkStorageList](/reference/services/SoftLayer_Hardware/removeAccessToNetworkStorageList)
Remove access to multiple SoftLayer_Network_Storage volumes from this device. 

#### [removeTags](/reference/services/SoftLayer_Hardware/removeTags)
Remove a tag reference

#### [setTags](/reference/services/SoftLayer_Hardware/setTags)


#### [updateIpmiPassword](/reference/services/SoftLayer_Hardware/updateIpmiPassword)
Update the root IPMI user password 

</div>

