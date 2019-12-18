---
title: "SoftLayer_Hardware_Firewall"
description: "The SoftLayer_Hardware_Firewall data type contains general information relating to a single SoftLayer firewall."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Firewall"
---

# SoftLayer_Hardware_Firewall
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Firewall' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Hardware_Firewall data type contains general information relating to a single SoftLayer firewall. 





<!-- Service Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Method Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Service Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
-----
[accountId]: #accountid
#### [accountId]
A hardware's associated [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) id.  
<span class="type-label">Type: </span>**integer**

-----
[bareMetalInstanceFlag]: #baremetalinstanceflag
#### [bareMetalInstanceFlag]
When true, this flag specifies that a hardware is Bare Metal Server. Bare Metal Servers are physical bare metal servers that are billed with the same options as Virtual Servers, with monthly and hourly rates.  Bare Metal instances are ordered based on processor core count and ram amount.   
<span class="type-label">Type: </span>**integer**

-----
[domain]: #domain
#### [domain]
A piece of hardware's local network domain name.  
<span class="type-label">Type: </span>**string**

-----
[fullyQualifiedDomainName]: #fullyqualifieddomainname
#### [fullyQualifiedDomainName]
A name reflecting the hostname and domain of the hardware. This is created from the combined values of the hardware's hostname and domain name automatically, and thus should not be edited directly.   
<span class="type-label">Type: </span>**string**

-----
[hardwareStatusId]: #hardwarestatusid
#### [hardwareStatusId]
A number reflecting the state of a hardware  
<span class="type-label">Type: </span>**integer**

-----
[hostname]: #hostname
#### [hostname]
A hardware's hostname  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
A hardware's internal identification number  
<span class="type-label">Type: </span>**integer**

-----
[manufacturerSerialNumber]: #manufacturerserialnumber
#### [manufacturerSerialNumber]
A hardware's serial number that is supplied by the manufacturer.  
<span class="type-label">Type: </span>**string**

-----
[notes]: #notes
#### [notes]
A small note about a piece of hardware to use at your discretion.  
<span class="type-label">Type: </span>**string**

-----
[postInstallScriptUri]: #postinstallscripturi
#### [postInstallScriptUri]
URI of the script to be downloaded and executed after installation is complete.  
<span class="type-label">Type: </span>**string**

-----
[provisionDate]: #provisiondate
#### [provisionDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[serialNumber]: #serialnumber
#### [serialNumber]
A hardware's serial number that is supplied by SoftLayer.  
<span class="type-label">Type: </span>**string**

-----
[serviceProviderId]: #serviceproviderid
#### [serviceProviderId]
  
<span class="type-label">Type: </span>**integer**

-----
[serviceProviderResourceId]: #serviceproviderresourceid
#### [serviceProviderResourceId]
A hardware's internal identification number at its service provider  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The account associated with a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[activeComponents]: #activecomponents
#### [activeComponents]
A piece of hardware's active physical components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**

-----
[activeNetworkMonitorIncident]: #activenetworkmonitorincident
#### [activeNetworkMonitorIncident]
A piece of hardware's active network monitoring incidents.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Incident'>SoftLayer_Network_Monitor_Version1_Incident[] </a>**

-----
[allPowerComponents]: #allpowercomponents
#### [allPowerComponents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Power_Component'>SoftLayer_Hardware_Power_Component[] </a>**

-----
[allowedHost]: #allowedhost
#### [allowedHost]
The SoftLayer_Network_Storage_Allowed_Host information to connect this server to Network Storage volumes that require access control lists.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Allowed_Host'>SoftLayer_Network_Storage_Allowed_Host </a>**

-----
[allowedNetworkStorage]: #allowednetworkstorage
#### [allowedNetworkStorage]
The SoftLayer_Network_Storage objects that this SoftLayer_Hardware has access to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[allowedNetworkStorageReplicas]: #allowednetworkstoragereplicas
#### [allowedNetworkStorageReplicas]
The SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[antivirusSpywareSoftwareComponent]: #antivirusspywaresoftwarecomponent
#### [antivirusSpywareSoftwareComponent]
Information regarding an antivirus/spyware software component object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component'>SoftLayer_Software_Component </a>**

-----
[attributes]: #attributes
#### [attributes]
Information regarding a piece of hardware's specific attributes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Attribute'>SoftLayer_Hardware_Attribute[] </a>**

-----
[averageDailyPublicBandwidthUsage]: #averagedailypublicbandwidthusage
#### [averageDailyPublicBandwidthUsage]
The average daily public bandwidth usage for the current billing cycle.  
<span class="type-label">Type: </span>**float**

-----
[backendNetworkComponents]: #backendnetworkcomponents
#### [backendNetworkComponents]
A piece of hardware's back-end or private network components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component[] </a>**

-----
[backendRouters]: #backendrouters
#### [backendRouters]
A hardware's backend or private router.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[bandwidthAllocation]: #bandwidthallocation
#### [bandwidthAllocation]
A hardware's allotted bandwidth (measured in GB).  
<span class="type-label">Type: </span>**decimal**

-----
[bandwidthAllotmentDetail]: #bandwidthallotmentdetail
#### [bandwidthAllotmentDetail]
A hardware's allotted detail record. Allotment details link bandwidth allocation with allotments.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment_Detail'>SoftLayer_Network_Bandwidth_Version1_Allotment_Detail </a>**

-----
[benchmarkCertifications]: #benchmarkcertifications
#### [benchmarkCertifications]
Information regarding a piece of hardware's benchmark certifications.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Benchmark_Certification'>SoftLayer_Hardware_Benchmark_Certification[] </a>**

-----
[billingItem]: #billingitem
#### [billingItem]
Information regarding the billing item for a server.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Hardware'>SoftLayer_Billing_Item_Hardware </a>**

-----
[billingItemFlag]: #billingitemflag
#### [billingItemFlag]
A flag indicating that a billing item exists.  
<span class="type-label">Type: </span>**boolean**

-----
[blockCancelBecauseDisconnectedFlag]: #blockcancelbecausedisconnectedflag
#### [blockCancelBecauseDisconnectedFlag]
Determines whether the hardware is ineligible for cancellation because it is disconnected.  
<span class="type-label">Type: </span>**boolean**

-----
[businessContinuanceInsuranceFlag]: #businesscontinuanceinsuranceflag
#### [businessContinuanceInsuranceFlag]
Status indicating whether or not a piece of hardware has business continuance insurance.  
<span class="type-label">Type: </span>**boolean**

-----
[childrenHardware]: #childrenhardware
#### [childrenHardware]
Child hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[components]: #components
#### [components]
A piece of hardware's components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**

-----
[continuousDataProtectionSoftwareComponent]: #continuousdataprotectionsoftwarecomponent
#### [continuousDataProtectionSoftwareComponent]
A continuous data protection/server backup software component object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component'>SoftLayer_Software_Component </a>**

-----
[currentBillableBandwidthUsage]: #currentbillablebandwidthusage
#### [currentBillableBandwidthUsage]
The current billable public outbound bandwidth for this hardware for the current billing cycle.  
<span class="type-label">Type: </span>**decimal**

-----
[datacenter]: #datacenter
#### [datacenter]
Information regarding the datacenter in which a piece of hardware resides.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[datacenterName]: #datacentername
#### [datacenterName]
The name of the datacenter in which a piece of hardware resides.  
<span class="type-label">Type: </span>**string**

-----
[daysInSparePool]: #daysinsparepool
#### [daysInSparePool]
Number of day(s) a server have been in spare pool.  
<span class="type-label">Type: </span>**integer**

-----
[downlinkHardware]: #downlinkhardware
#### [downlinkHardware]
All hardware that has uplink network connections to a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[downlinkNetworkHardware]: #downlinknetworkhardware
#### [downlinkNetworkHardware]
All hardware that has uplink network connections to a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[downlinkServers]: #downlinkservers
#### [downlinkServers]
Information regarding all servers attached to a piece of network hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[downlinkVirtualGuests]: #downlinkvirtualguests
#### [downlinkVirtualGuests]
Information regarding all virtual guests attached to a piece of network hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[downstreamHardwareBindings]: #downstreamhardwarebindings
#### [downstreamHardwareBindings]
All hardware downstream from a network device.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component_Uplink_Hardware'>SoftLayer_Network_Component_Uplink_Hardware[] </a>**

-----
[downstreamNetworkHardware]: #downstreamnetworkhardware
#### [downstreamNetworkHardware]
All network hardware downstream from the selected piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[downstreamNetworkHardwareWithIncidents]: #downstreamnetworkhardwarewithincidents
#### [downstreamNetworkHardwareWithIncidents]
All network hardware with monitoring warnings or errors that are downstream from the selected piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[downstreamServers]: #downstreamservers
#### [downstreamServers]
Information regarding all servers attached downstream to a piece of network hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[downstreamVirtualGuests]: #downstreamvirtualguests
#### [downstreamVirtualGuests]
Information regarding all virtual guests attached to a piece of network hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[driveControllers]: #drivecontrollers
#### [driveControllers]
The drive controllers contained within a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**

-----
[evaultNetworkStorage]: #evaultnetworkstorage
#### [evaultNetworkStorage]
Information regarding a piece of hardware's associated EVault network storage service account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[firewallServiceComponent]: #firewallservicecomponent
#### [firewallServiceComponent]
Information regarding a piece of hardware's firewall services.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component_Firewall'>SoftLayer_Network_Component_Firewall </a>**

-----
[fixedConfigurationPreset]: #fixedconfigurationpreset
#### [fixedConfigurationPreset]
Defines the fixed components in a fixed configuration bare metal server.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Preset'>SoftLayer_Product_Package_Preset </a>**

-----
[frontendNetworkComponents]: #frontendnetworkcomponents
#### [frontendNetworkComponents]
A piece of hardware's front-end or public network components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component[] </a>**

-----
[frontendRouters]: #frontendrouters
#### [frontendRouters]
A hardware's frontend or public router.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[globalIdentifier]: #globalidentifier
#### [globalIdentifier]
A hardware's universally unique identifier.  
<span class="type-label">Type: </span>**string**

-----
[hardDrives]: #harddrives
#### [hardDrives]
The hard drives contained within a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**

-----
[hardwareChassis]: #hardwarechassis
#### [hardwareChassis]
The chassis that a piece of hardware is housed in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Chassis'>SoftLayer_Hardware_Chassis </a>**

-----
[hardwareFunction]: #hardwarefunction
#### [hardwareFunction]
A hardware's function.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Function'>SoftLayer_Hardware_Function </a>**

-----
[hardwareFunctionDescription]: #hardwarefunctiondescription
#### [hardwareFunctionDescription]
A hardware's function.  
<span class="type-label">Type: </span>**string**

-----
[hardwareStatus]: #hardwarestatus
#### [hardwareStatus]
A hardware's status.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Status'>SoftLayer_Hardware_Status </a>**

-----
[hasTrustedPlatformModuleBillingItemFlag]: #hastrustedplatformmodulebillingitemflag
#### [hasTrustedPlatformModuleBillingItemFlag]
Determine in hardware object has TPM enabled.  
<span class="type-label">Type: </span>**boolean**

-----
[hostIpsSoftwareComponent]: #hostipssoftwarecomponent
#### [hostIpsSoftwareComponent]
Information regarding a host IPS software component object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component'>SoftLayer_Software_Component </a>**

-----
[hourlyBillingFlag]: #hourlybillingflag
#### [hourlyBillingFlag]
A server's hourly billing status.  
<span class="type-label">Type: </span>**boolean**

-----
[inboundBandwidthUsage]: #inboundbandwidthusage
#### [inboundBandwidthUsage]
The sum of all the inbound network traffic data for the last 30 days.  
<span class="type-label">Type: </span>**decimal**

-----
[inboundPublicBandwidthUsage]: #inboundpublicbandwidthusage
#### [inboundPublicBandwidthUsage]
The total public inbound bandwidth for this hardware for the current billing cycle.  
<span class="type-label">Type: </span>**decimal**

-----
[lastTransaction]: #lasttransaction
#### [lastTransaction]
Information regarding the last transaction a server performed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>**

-----
[latestNetworkMonitorIncident]: #latestnetworkmonitorincident
#### [latestNetworkMonitorIncident]
A piece of hardware's latest network monitoring incident.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Incident'>SoftLayer_Network_Monitor_Version1_Incident </a>**

-----
[location]: #location
#### [location]
Where a piece of hardware is located within SoftLayer's location hierarchy.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[locationPathString]: #locationpathstring
#### [locationPathString]
  
<span class="type-label">Type: </span>**string**

-----
[lockboxNetworkStorage]: #lockboxnetworkstorage
#### [lockboxNetworkStorage]
Information regarding a lockbox account associated with a server.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage </a>**

-----
[managedResourceFlag]: #managedresourceflag
#### [managedResourceFlag]
A flag indicating that the hardware is a managed resource.  
<span class="type-label">Type: </span>**boolean**

-----
[memory]: #memory
#### [memory]
Information regarding a piece of hardware's memory.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**

-----
[memoryCapacity]: #memorycapacity
#### [memoryCapacity]
The amount of memory a piece of hardware has, measured in gigabytes.  
<span class="type-label">Type: </span>**unsigned integer**

-----
[metricTrackingObject]: #metrictrackingobject
#### [metricTrackingObject]
A piece of hardware's metric tracking object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_HardwareServer'>SoftLayer_Metric_Tracking_Object_HardwareServer </a>**

-----
[modules]: #modules
#### [modules]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**

-----
[monitoringAgents]: #monitoringagents
#### [monitoringAgents]
Information regarding the monitoring agents associated with a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Monitoring_Agent'>SoftLayer_Monitoring_Agent[] </a>**

-----
[monitoringRobot]: #monitoringrobot
#### [monitoringRobot]
Information regarding the hardware's monitoring robot.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Monitoring_Robot'>SoftLayer_Monitoring_Robot </a>**

-----
[monitoringServiceComponent]: #monitoringservicecomponent
#### [monitoringServiceComponent]
Information regarding a piece of hardware's network monitoring services.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host_Stratum'>SoftLayer_Network_Monitor_Version1_Query_Host_Stratum </a>**

-----
[monitoringServiceEligibilityFlag]: #monitoringserviceeligibilityflag
#### [monitoringServiceEligibilityFlag]
The monitoring service flag eligibility status for a piece of hardware.  
<span class="type-label">Type: </span>**boolean**

-----
[monitoringServiceFlag]: #monitoringserviceflag
#### [monitoringServiceFlag]
The service flag status for a piece of hardware.  
<span class="type-label">Type: </span>**boolean**

-----
[motherboard]: #motherboard
#### [motherboard]
Information regarding a piece of hardware's motherboard.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component </a>**

-----
[networkCards]: #networkcards
#### [networkCards]
Information regarding a piece of hardware's network cards.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**

-----
[networkComponents]: #networkcomponents
#### [networkComponents]
Returns a hardware's network components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component[] </a>**

-----
[networkGatewayMember]: #networkgatewaymember
#### [networkGatewayMember]
The gateway member if this device is part of a network gateway.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway_Member'>SoftLayer_Network_Gateway_Member </a>**

-----
[networkGatewayMemberFlag]: #networkgatewaymemberflag
#### [networkGatewayMemberFlag]
Whether or not this device is part of a network gateway.  
<span class="type-label">Type: </span>**boolean**

-----
[networkMonitorAttachedDownHardware]: #networkmonitorattacheddownhardware
#### [networkMonitorAttachedDownHardware]
All servers with failed monitoring that are attached downstream to a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[networkMonitorAttachedDownVirtualGuests]: #networkmonitorattacheddownvirtualguests
#### [networkMonitorAttachedDownVirtualGuests]
Virtual guests that are attached downstream to a hardware that have failed monitoring  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[networkMonitorIncidents]: #networkmonitorincidents
#### [networkMonitorIncidents]
The status of all of a piece of hardware's network monitoring incidents.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Incident'>SoftLayer_Network_Monitor_Version1_Incident[] </a>**

-----
[networkMonitors]: #networkmonitors
#### [networkMonitors]
Information regarding a piece of hardware's network monitors.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host'>SoftLayer_Network_Monitor_Version1_Query_Host[] </a>**

-----
[networkStatus]: #networkstatus
#### [networkStatus]
The value of a hardware's network status attribute.  
<span class="type-label">Type: </span>**string**

-----
[networkStatusAttribute]: #networkstatusattribute
#### [networkStatusAttribute]
The hardware's related network status attribute.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Attribute'>SoftLayer_Hardware_Attribute </a>**

-----
[networkStorage]: #networkstorage
#### [networkStorage]
Information regarding a piece of hardware's associated network storage service account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[networkVlans]: #networkvlans
#### [networkVlans]
The network virtual LANs (VLANs) associated with a piece of hardware's network components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a>**

-----
[nextBillingCycleBandwidthAllocation]: #nextbillingcyclebandwidthallocation
#### [nextBillingCycleBandwidthAllocation]
A hardware's allotted bandwidth for the next billing cycle (measured in GB).  
<span class="type-label">Type: </span>**decimal**

-----
[notesHistory]: #noteshistory
#### [notesHistory]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Note'>SoftLayer_Hardware_Note[] </a>**

-----
[nvRamCapacity]: #nvramcapacity
#### [nvRamCapacity]
The amount of non-volatile memory a piece of hardware has, measured in gigabytes.  
<span class="type-label">Type: </span>**unsigned integer**

-----
[nvRamComponentModels]: #nvramcomponentmodels
#### [nvRamComponentModels]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model'>SoftLayer_Hardware_Component_Model[] </a>**

-----
[operatingSystemReferenceCode]: #operatingsystemreferencecode
#### [operatingSystemReferenceCode]
A hardware's operating system software description.  
<span class="type-label">Type: </span>**string**

-----
[outboundBandwidthUsage]: #outboundbandwidthusage
#### [outboundBandwidthUsage]
The sum of all the outbound network traffic data for the last 30 days.  
<span class="type-label">Type: </span>**decimal**

-----
[outboundPublicBandwidthUsage]: #outboundpublicbandwidthusage
#### [outboundPublicBandwidthUsage]
The total public outbound bandwidth for this hardware for the current billing cycle.  
<span class="type-label">Type: </span>**decimal**

-----
[parentBay]: #parentbay
#### [parentBay]
Blade Bay  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Blade'>SoftLayer_Hardware_Blade </a>**

-----
[parentHardware]: #parenthardware
#### [parentHardware]
Parent Hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**

-----
[pointOfPresenceLocation]: #pointofpresencelocation
#### [pointOfPresenceLocation]
Information regarding the Point of Presence (PoP) location in which a piece of hardware resides.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[powerComponents]: #powercomponents
#### [powerComponents]
The power components for a hardware object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Power_Component'>SoftLayer_Hardware_Power_Component[] </a>**

-----
[powerSupply]: #powersupply
#### [powerSupply]
Information regarding a piece of hardware's power supply.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**

-----
[primaryIpAddress]: #primaryipaddress
#### [primaryIpAddress]
The firewall's primary public IP address.  
<span class="type-label">Type: </span>**string**

-----
[privateNetworkOnlyFlag]: #privatenetworkonlyflag
#### [privateNetworkOnlyFlag]
Whether the hardware only has access to the private network.  
<span class="type-label">Type: </span>**boolean**

-----
[processorCoreAmount]: #processorcoreamount
#### [processorCoreAmount]
The total number of processor cores, summed from all processors that are attached to a piece of hardware  
<span class="type-label">Type: </span>**unsigned integer**

-----
[processorPhysicalCoreAmount]: #processorphysicalcoreamount
#### [processorPhysicalCoreAmount]
The total number of physical processor cores, summed from all processors that are attached to a piece of hardware  
<span class="type-label">Type: </span>**unsigned integer**

-----
[processors]: #processors
#### [processors]
Information regarding a piece of hardware's processors.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**

-----
[rack]: #rack
#### [rack]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[raidControllers]: #raidcontrollers
#### [raidControllers]
The RAID controllers contained within a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**

-----
[recentEvents]: #recentevents
#### [recentEvents]
Recent events that impact this hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Event'>SoftLayer_Notification_Occurrence_Event[] </a>**

-----
[remoteManagementAccounts]: #remotemanagementaccounts
#### [remoteManagementAccounts]
User credentials to issue commands and/or interact with the server's remote management card.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_User'>SoftLayer_Hardware_Component_RemoteManagement_User[] </a>**

-----
[remoteManagementComponent]: #remotemanagementcomponent
#### [remoteManagementComponent]
A hardware's associated remote management component. This is normally IPMI.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a>**

-----
[resourceConfigurations]: #resourceconfigurations
#### [resourceConfigurations]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Resource_Configuration'>SoftLayer_Hardware_Resource_Configuration[] </a>**

-----
[resourceGroupMemberReferences]: #resourcegroupmemberreferences
#### [resourceGroupMemberReferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Member'>SoftLayer_Resource_Group_Member[] </a>**

-----
[resourceGroupRoles]: #resourcegrouproles
#### [resourceGroupRoles]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Role'>SoftLayer_Resource_Group_Role[] </a>**

-----
[resourceGroups]: #resourcegroups
#### [resourceGroups]
The resource groups in which this hardware is a member.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group'>SoftLayer_Resource_Group[] </a>**

-----
[routers]: #routers
#### [routers]
A hardware's routers.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[scaleAssets]: #scaleassets
#### [scaleAssets]
Collection of scale assets this hardware corresponds to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Asset'>SoftLayer_Scale_Asset[] </a>**

-----
[securityScanRequests]: #securityscanrequests
#### [securityScanRequests]
Information regarding a piece of hardware's vulnerability scan requests.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Security_Scanner_Request'>SoftLayer_Network_Security_Scanner_Request[] </a>**

-----
[serverRoom]: #serverroom
#### [serverRoom]
Information regarding the server room in which the hardware is located.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[serviceProvider]: #serviceprovider
#### [serviceProvider]
Information regarding the piece of hardware's service provider.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Service_Provider'>SoftLayer_Service_Provider </a>**

-----
[softwareComponents]: #softwarecomponents
#### [softwareComponents]
Information regarding a piece of hardware's installed software.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component'>SoftLayer_Software_Component[] </a>**

-----
[sparePoolBillingItem]: #sparepoolbillingitem
#### [sparePoolBillingItem]
Information regarding the billing item for a spare pool server.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Hardware'>SoftLayer_Billing_Item_Hardware </a>**

-----
[sshKeys]: #sshkeys
#### [sshKeys]
SSH keys to be installed on the server during provisioning or an OS reload.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Ssh_Key'>SoftLayer_Security_Ssh_Key[] </a>**

-----
[storageNetworkComponents]: #storagenetworkcomponents
#### [storageNetworkComponents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component[] </a>**

-----
[tagReferences]: #tagreferences
#### [tagReferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Tag_Reference'>SoftLayer_Tag_Reference[] </a>**

-----
[topLevelLocation]: #toplevellocation
#### [topLevelLocation]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[upgradeRequest]: #upgraderequest
#### [upgradeRequest]
An account's associated upgrade request object, if any.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Upgrade_Request'>SoftLayer_Product_Upgrade_Request </a>**

-----
[uplinkHardware]: #uplinkhardware
#### [uplinkHardware]
The network device connected to a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**

-----
[uplinkNetworkComponents]: #uplinknetworkcomponents
#### [uplinkNetworkComponents]
Information regarding the network component that is one level higher than a piece of hardware on the network infrastructure.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component[] </a>**

-----
[userData]: #userdata
#### [userData]
An array containing a single string of custom user data for a hardware order. Max size is 16 kb.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Attribute'>SoftLayer_Hardware_Attribute[] </a>**

-----
[users]: #users
#### [users]
A list of users that have access to this hardware firewall.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer[] </a>**

-----
[virtualChassis]: #virtualchassis
#### [virtualChassis]
Information regarding the virtual chassis for a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Group'>SoftLayer_Hardware_Group </a>**

-----
[virtualChassisSiblings]: #virtualchassissiblings
#### [virtualChassisSiblings]
Information regarding the virtual chassis siblings for a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[virtualHost]: #virtualhost
#### [virtualHost]
A piece of hardware's virtual host record.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Host'>SoftLayer_Virtual_Host </a>**

-----
[virtualLicenses]: #virtuallicenses
#### [virtualLicenses]
Information regarding a piece of hardware's virtual software licenses.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_VirtualLicense'>SoftLayer_Software_VirtualLicense[] </a>**

-----
[virtualRack]: #virtualrack
#### [virtualRack]
Information regarding the bandwidth allotment to which a piece of hardware belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment </a>**

-----
[virtualRackId]: #virtualrackid
#### [virtualRackId]
The name of the bandwidth allotment belonging to a piece of hardware.  
<span class="type-label">Type: </span>**integer**

-----
[virtualRackName]: #virtualrackname
#### [virtualRackName]
The name of the bandwidth allotment belonging to a piece of hardware.  
<span class="type-label">Type: </span>**string**

-----
[virtualizationPlatform]: #virtualizationplatform
#### [virtualizationPlatform]
A piece of hardware's virtualization platform software.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component'>SoftLayer_Software_Component </a>**


## Count

-----
[activeComponentCount]: #activecomponentcount
#### [activeComponentCount]
A count of a piece of hardware's active physical components.   
<span class="type-label">Type: </span>**unsigned long**


-----
[activeNetworkMonitorIncidentCount]: #activenetworkmonitorincidentcount
#### [activeNetworkMonitorIncidentCount]
A count of a piece of hardware's active network monitoring incidents.   
<span class="type-label">Type: </span>**unsigned long**


-----
[allPowerComponentCount]: #allpowercomponentcount
#### [allPowerComponentCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[allowedNetworkStorageCount]: #allowednetworkstoragecount
#### [allowedNetworkStorageCount]
A count of the SoftLayer_Network_Storage objects that this SoftLayer_Hardware has access to.   
<span class="type-label">Type: </span>**unsigned long**


-----
[allowedNetworkStorageReplicaCount]: #allowednetworkstoragereplicacount
#### [allowedNetworkStorageReplicaCount]
A count of the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to.   
<span class="type-label">Type: </span>**unsigned long**


-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of information regarding a piece of hardware's specific attributes.   
<span class="type-label">Type: </span>**unsigned long**


-----
[backendNetworkComponentCount]: #backendnetworkcomponentcount
#### [backendNetworkComponentCount]
A count of a piece of hardware's back-end or private network components.   
<span class="type-label">Type: </span>**unsigned long**


-----
[backendRouterCount]: #backendroutercount
#### [backendRouterCount]
A count of a hardware's backend or private router.   
<span class="type-label">Type: </span>**unsigned long**


-----
[benchmarkCertificationCount]: #benchmarkcertificationcount
#### [benchmarkCertificationCount]
A count of information regarding a piece of hardware's benchmark certifications.   
<span class="type-label">Type: </span>**unsigned long**


-----
[childrenHardwareCount]: #childrenhardwarecount
#### [childrenHardwareCount]
A count of child hardware.   
<span class="type-label">Type: </span>**unsigned long**


-----
[componentCount]: #componentcount
#### [componentCount]
A count of a piece of hardware's components.   
<span class="type-label">Type: </span>**unsigned long**


-----
[downlinkHardwareCount]: #downlinkhardwarecount
#### [downlinkHardwareCount]
A count of all hardware that has uplink network connections to a piece of hardware.   
<span class="type-label">Type: </span>**unsigned long**


-----
[downlinkNetworkHardwareCount]: #downlinknetworkhardwarecount
#### [downlinkNetworkHardwareCount]
A count of all hardware that has uplink network connections to a piece of hardware.   
<span class="type-label">Type: </span>**unsigned long**


-----
[downlinkServerCount]: #downlinkservercount
#### [downlinkServerCount]
A count of information regarding all servers attached to a piece of network hardware.   
<span class="type-label">Type: </span>**unsigned long**


-----
[downlinkVirtualGuestCount]: #downlinkvirtualguestcount
#### [downlinkVirtualGuestCount]
A count of information regarding all virtual guests attached to a piece of network hardware.   
<span class="type-label">Type: </span>**unsigned long**


-----
[downstreamHardwareBindingCount]: #downstreamhardwarebindingcount
#### [downstreamHardwareBindingCount]
A count of all hardware downstream from a network device.   
<span class="type-label">Type: </span>**unsigned long**


-----
[downstreamNetworkHardwareCount]: #downstreamnetworkhardwarecount
#### [downstreamNetworkHardwareCount]
A count of all network hardware downstream from the selected piece of hardware.   
<span class="type-label">Type: </span>**unsigned long**


-----
[downstreamNetworkHardwareWithIncidentCount]: #downstreamnetworkhardwarewithincidentcount
#### [downstreamNetworkHardwareWithIncidentCount]
A count of all network hardware with monitoring warnings or errors that are downstream from the selected piece of hardware.   
<span class="type-label">Type: </span>**unsigned long**


-----
[downstreamServerCount]: #downstreamservercount
#### [downstreamServerCount]
A count of information regarding all servers attached downstream to a piece of network hardware.   
<span class="type-label">Type: </span>**unsigned long**


-----
[downstreamVirtualGuestCount]: #downstreamvirtualguestcount
#### [downstreamVirtualGuestCount]
A count of information regarding all virtual guests attached to a piece of network hardware.   
<span class="type-label">Type: </span>**unsigned long**


-----
[driveControllerCount]: #drivecontrollercount
#### [driveControllerCount]
A count of the drive controllers contained within a piece of hardware.   
<span class="type-label">Type: </span>**unsigned long**


-----
[evaultNetworkStorageCount]: #evaultnetworkstoragecount
#### [evaultNetworkStorageCount]
A count of information regarding a piece of hardware's associated EVault network storage service account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[frontendNetworkComponentCount]: #frontendnetworkcomponentcount
#### [frontendNetworkComponentCount]
A count of a piece of hardware's front-end or public network components.   
<span class="type-label">Type: </span>**unsigned long**


-----
[frontendRouterCount]: #frontendroutercount
#### [frontendRouterCount]
A count of a hardware's frontend or public router.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hardDriveCount]: #harddrivecount
#### [hardDriveCount]
A count of the hard drives contained within a piece of hardware.   
<span class="type-label">Type: </span>**unsigned long**


-----
[memoryCount]: #memorycount
#### [memoryCount]
A count of information regarding a piece of hardware's memory.   
<span class="type-label">Type: </span>**unsigned long**


-----
[moduleCount]: #modulecount
#### [moduleCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[monitoringAgentCount]: #monitoringagentcount
#### [monitoringAgentCount]
A count of information regarding the monitoring agents associated with a piece of hardware.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkCardCount]: #networkcardcount
#### [networkCardCount]
A count of information regarding a piece of hardware's network cards.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkComponentCount]: #networkcomponentcount
#### [networkComponentCount]
A count of returns a hardware's network components.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkMonitorAttachedDownHardwareCount]: #networkmonitorattacheddownhardwarecount
#### [networkMonitorAttachedDownHardwareCount]
A count of all servers with failed monitoring that are attached downstream to a piece of hardware.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkMonitorAttachedDownVirtualGuestCount]: #networkmonitorattacheddownvirtualguestcount
#### [networkMonitorAttachedDownVirtualGuestCount]
A count of virtual guests that are attached downstream to a hardware that have failed monitoring   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkMonitorCount]: #networkmonitorcount
#### [networkMonitorCount]
A count of information regarding a piece of hardware's network monitors.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkMonitorIncidentCount]: #networkmonitorincidentcount
#### [networkMonitorIncidentCount]
A count of the status of all of a piece of hardware's network monitoring incidents.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkStorageCount]: #networkstoragecount
#### [networkStorageCount]
A count of information regarding a piece of hardware's associated network storage service account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkVlanCount]: #networkvlancount
#### [networkVlanCount]
A count of the network virtual LANs (VLANs) associated with a piece of hardware's network components.   
<span class="type-label">Type: </span>**unsigned long**


-----
[notesHistoryCount]: #noteshistorycount
#### [notesHistoryCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[nvRamComponentModelCount]: #nvramcomponentmodelcount
#### [nvRamComponentModelCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[powerComponentCount]: #powercomponentcount
#### [powerComponentCount]
A count of the power components for a hardware object.   
<span class="type-label">Type: </span>**unsigned long**


-----
[powerSupplyCount]: #powersupplycount
#### [powerSupplyCount]
A count of information regarding a piece of hardware's power supply.   
<span class="type-label">Type: </span>**unsigned long**


-----
[processorCount]: #processorcount
#### [processorCount]
A count of information regarding a piece of hardware's processors.   
<span class="type-label">Type: </span>**unsigned long**


-----
[raidControllerCount]: #raidcontrollercount
#### [raidControllerCount]
A count of the RAID controllers contained within a piece of hardware.   
<span class="type-label">Type: </span>**unsigned long**


-----
[recentEventCount]: #recenteventcount
#### [recentEventCount]
A count of recent events that impact this hardware.   
<span class="type-label">Type: </span>**unsigned long**


-----
[remoteManagementAccountCount]: #remotemanagementaccountcount
#### [remoteManagementAccountCount]
A count of user credentials to issue commands and/or interact with the server's remote management card.   
<span class="type-label">Type: </span>**unsigned long**


-----
[resourceConfigurationCount]: #resourceconfigurationcount
#### [resourceConfigurationCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[resourceGroupCount]: #resourcegroupcount
#### [resourceGroupCount]
A count of the resource groups in which this hardware is a member.   
<span class="type-label">Type: </span>**unsigned long**


-----
[resourceGroupMemberReferenceCount]: #resourcegroupmemberreferencecount
#### [resourceGroupMemberReferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[resourceGroupRoleCount]: #resourcegrouprolecount
#### [resourceGroupRoleCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[routerCount]: #routercount
#### [routerCount]
A count of a hardware's routers.   
<span class="type-label">Type: </span>**unsigned long**


-----
[scaleAssetCount]: #scaleassetcount
#### [scaleAssetCount]
A count of collection of scale assets this hardware corresponds to.   
<span class="type-label">Type: </span>**unsigned long**


-----
[securityScanRequestCount]: #securityscanrequestcount
#### [securityScanRequestCount]
A count of information regarding a piece of hardware's vulnerability scan requests.   
<span class="type-label">Type: </span>**unsigned long**


-----
[softwareComponentCount]: #softwarecomponentcount
#### [softwareComponentCount]
A count of information regarding a piece of hardware's installed software.   
<span class="type-label">Type: </span>**unsigned long**


-----
[sshKeyCount]: #sshkeycount
#### [sshKeyCount]
A count of sSH keys to be installed on the server during provisioning or an OS reload.   
<span class="type-label">Type: </span>**unsigned long**


-----
[storageNetworkComponentCount]: #storagenetworkcomponentcount
#### [storageNetworkComponentCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[tagReferenceCount]: #tagreferencecount
#### [tagReferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[uplinkNetworkComponentCount]: #uplinknetworkcomponentcount
#### [uplinkNetworkComponentCount]
A count of information regarding the network component that is one level higher than a piece of hardware on the network infrastructure.   
<span class="type-label">Type: </span>**unsigned long**


-----
[userCount]: #usercount
#### [userCount]
A count of a list of users that have access to this hardware firewall.   
<span class="type-label">Type: </span>**unsigned long**


-----
[userDataCount]: #userdatacount
#### [userDataCount]
A count of an array containing a single string of custom user data for a hardware order. Max size is 16 kb.   
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualChassisSiblingCount]: #virtualchassissiblingcount
#### [virtualChassisSiblingCount]
A count of information regarding the virtual chassis siblings for a piece of hardware.   
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualLicenseCount]: #virtuallicensecount
#### [virtualLicenseCount]
A count of information regarding a piece of hardware's virtual software licenses.   
<span class="type-label">Type: </span>**unsigned long**

</div>


