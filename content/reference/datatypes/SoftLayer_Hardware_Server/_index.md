---
title: "SoftLayer_Hardware_Server"
description: "The SoftLayer_Hardware_Server data type contains general information relating to a single SoftLayer server."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
---

# SoftLayer_Hardware_Server
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Hardware_Server' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Server' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Hardware_Server data type contains general information relating to a single SoftLayer server. 


### associatedMethods

*  [SoftLayer_Account::getHardware](/reference/services/SoftLayer_Account/getHardware )
*  [SoftLayer_Hardware::findByIpAddress](/reference/services/SoftLayer_Hardware/findByIpAddress )
*  [SoftLayer_Hardware::getObject](/reference/services/SoftLayer_Hardware/getObject )
*  [SoftLayer_Hardware_Server::getHardwareByIpAddress](/reference/services/SoftLayer_Hardware_Server/getHardwareByIpAddress )
*  [SoftLayer_Hardware_Server::getObject](/reference/services/SoftLayer_Hardware_Server/getObject )





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[accountId]: #accountid
#### [accountId]
A hardware's associated [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) id.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[bareMetalInstanceFlag]: #baremetalinstanceflag
#### [bareMetalInstanceFlag]
When true, this flag specifies that a hardware is Bare Metal Server. Bare Metal Servers are physical bare metal servers that are billed with the same options as Virtual Servers, with monthly and hourly rates.  Bare Metal instances are ordered based on processor core count and ram amount.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[domain]: #domain
#### [domain]
A piece of hardware's local network domain name.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[fullyQualifiedDomainName]: #fullyqualifieddomainname
#### [fullyQualifiedDomainName]
A name reflecting the hostname and domain of the hardware. This is created from the combined values of the hardware's hostname and domain name automatically, and thus should not be edited directly.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[hardwareStatusId]: #hardwarestatusid
#### [hardwareStatusId]
A number reflecting the state of a hardware  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[hostname]: #hostname
#### [hostname]
A hardware's hostname  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A hardware's internal identification number  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[manufacturerSerialNumber]: #manufacturerserialnumber
#### [manufacturerSerialNumber]
A hardware's serial number that is supplied by the manufacturer.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[notes]: #notes
#### [notes]
A small note about a piece of hardware to use at your discretion.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[postInstallScriptUri]: #postinstallscripturi
#### [postInstallScriptUri]
URI of the script to be downloaded and executed after installation is complete.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[provisionDate]: #provisiondate
#### [provisionDate]
  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[serialNumber]: #serialnumber
#### [serialNumber]
A hardware's serial number that is supplied by SoftLayer.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[serviceProviderId]: #serviceproviderid
#### [serviceProviderId]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[serviceProviderResourceId]: #serviceproviderresourceid
#### [serviceProviderResourceId]
A hardware's internal identification number at its service provider  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account associated with a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[activeComponents]: #activecomponents
#### [activeComponents]
A piece of hardware's active physical components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**


</div>
<div class="prop-row">

-----
[activeNetworkFirewallBillingItem]: #activenetworkfirewallbillingitem
#### [activeNetworkFirewallBillingItem]
The billing item for a server's attached network firewall.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**


</div>
<div class="prop-row">

-----
[activeNetworkMonitorIncident]: #activenetworkmonitorincident
#### [activeNetworkMonitorIncident]
A piece of hardware's active network monitoring incidents.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Incident'>SoftLayer_Network_Monitor_Version1_Incident[] </a>**


</div>
<div class="prop-row">

-----
[activeTickets]: #activetickets
#### [activeTickets]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[activeTransaction]: #activetransaction
#### [activeTransaction]
Transaction currently running for server.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>**


</div>
<div class="prop-row">

-----
[activeTransactions]: #activetransactions
#### [activeTransactions]
Any active transaction(s) that are currently running for the server (example: os reload).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction[] </a>**


</div>
<div class="prop-row">

-----
[allPowerComponents]: #allpowercomponents
#### [allPowerComponents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Power_Component'>SoftLayer_Hardware_Power_Component[] </a>**


</div>
<div class="prop-row">

-----
[allowedHost]: #allowedhost
#### [allowedHost]
The SoftLayer_Network_Storage_Allowed_Host information to connect this server to Network Storage volumes that require access control lists.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Allowed_Host'>SoftLayer_Network_Storage_Allowed_Host </a>**


</div>
<div class="prop-row">

-----
[allowedNetworkStorage]: #allowednetworkstorage
#### [allowedNetworkStorage]
The SoftLayer_Network_Storage objects that this SoftLayer_Hardware has access to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[allowedNetworkStorageReplicas]: #allowednetworkstoragereplicas
#### [allowedNetworkStorageReplicas]
The SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[antivirusSpywareSoftwareComponent]: #antivirusspywaresoftwarecomponent
#### [antivirusSpywareSoftwareComponent]
Information regarding an antivirus/spyware software component object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component'>SoftLayer_Software_Component </a>**


</div>
<div class="prop-row">

-----
[attributes]: #attributes
#### [attributes]
Information regarding a piece of hardware's specific attributes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Attribute'>SoftLayer_Hardware_Attribute[] </a>**


</div>
<div class="prop-row">

-----
[availableMonitoring]: #availablemonitoring
#### [availableMonitoring]
An object that stores the maximum level for the monitoring query types and response types.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host_Stratum'>SoftLayer_Network_Monitor_Version1_Query_Host_Stratum[] </a>**


</div>
<div class="prop-row">

-----
[averageDailyBandwidthUsage]: #averagedailybandwidthusage
#### [averageDailyBandwidthUsage]
The average daily total bandwidth usage for the current billing cycle.  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[averageDailyPrivateBandwidthUsage]: #averagedailyprivatebandwidthusage
#### [averageDailyPrivateBandwidthUsage]
The average daily private bandwidth usage for the current billing cycle.  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[averageDailyPublicBandwidthUsage]: #averagedailypublicbandwidthusage
#### [averageDailyPublicBandwidthUsage]
The average daily public bandwidth usage for the current billing cycle.  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[backendNetworkComponents]: #backendnetworkcomponents
#### [backendNetworkComponents]
A piece of hardware's back-end or private network components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component[] </a>**


</div>
<div class="prop-row">

-----
[backendRouters]: #backendrouters
#### [backendRouters]
A hardware's backend or private router.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[bandwidthAllocation]: #bandwidthallocation
#### [bandwidthAllocation]
A hardware's allotted bandwidth (measured in GB).  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[bandwidthAllotmentDetail]: #bandwidthallotmentdetail
#### [bandwidthAllotmentDetail]
A hardware's allotted detail record. Allotment details link bandwidth allocation with allotments.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment_Detail'>SoftLayer_Network_Bandwidth_Version1_Allotment_Detail </a>**


</div>
<div class="prop-row">

-----
[benchmarkCertifications]: #benchmarkcertifications
#### [benchmarkCertifications]
Information regarding a piece of hardware's benchmark certifications.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Benchmark_Certification'>SoftLayer_Hardware_Benchmark_Certification[] </a>**


</div>
<div class="prop-row">

-----
[billingCycleBandwidthUsage]: #billingcyclebandwidthusage
#### [billingCycleBandwidthUsage]
The raw bandwidth usage data for the current billing cycle. One object will be returned for each network this server is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage[] </a>**


</div>
<div class="prop-row">

-----
[billingCyclePrivateBandwidthUsage]: #billingcycleprivatebandwidthusage
#### [billingCyclePrivateBandwidthUsage]
The raw private bandwidth usage data for the current billing cycle.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage </a>**


</div>
<div class="prop-row">

-----
[billingCyclePublicBandwidthUsage]: #billingcyclepublicbandwidthusage
#### [billingCyclePublicBandwidthUsage]
The raw public bandwidth usage data for the current billing cycle.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage </a>**


</div>
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
The billing item for a server.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Hardware'>SoftLayer_Billing_Item_Hardware </a>**


</div>
<div class="prop-row">

-----
[billingItemFlag]: #billingitemflag
#### [billingItemFlag]
A flag indicating that a billing item exists.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[biosPasswordNullFlag]: #biospasswordnullflag
#### [biosPasswordNullFlag]
Determine if BIOS password should be left as null.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[blockCancelBecauseDisconnectedFlag]: #blockcancelbecausedisconnectedflag
#### [blockCancelBecauseDisconnectedFlag]
Determines whether the hardware is ineligible for cancellation because it is disconnected.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[businessContinuanceInsuranceFlag]: #businesscontinuanceinsuranceflag
#### [businessContinuanceInsuranceFlag]
Status indicating whether or not a piece of hardware has business continuance insurance.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[captureEnabledFlag]: #captureenabledflag
#### [captureEnabledFlag]
Determine if the server is able to be image captured. If unable to image capture a reason will be provided.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Hardware_CaptureEnabled'>SoftLayer_Container_Hardware_CaptureEnabled </a>**


</div>
<div class="prop-row">

-----
[childrenHardware]: #childrenhardware
#### [childrenHardware]
Child hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[components]: #components
#### [components]
A piece of hardware's components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**


</div>
<div class="prop-row">

-----
[containsSolidStateDrivesFlag]: #containssolidstatedrivesflag
#### [containsSolidStateDrivesFlag]
  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[continuousDataProtectionSoftwareComponent]: #continuousdataprotectionsoftwarecomponent
#### [continuousDataProtectionSoftwareComponent]
A continuous data protection/server backup software component object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component'>SoftLayer_Software_Component </a>**


</div>
<div class="prop-row">

-----
[controlPanel]: #controlpanel
#### [controlPanel]
A server's control panel.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component_ControlPanel'>SoftLayer_Software_Component_ControlPanel </a>**


</div>
<div class="prop-row">

-----
[cost]: #cost
#### [cost]
The total cost of a server, measured in US Dollars ($USD).  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[currentBandwidthSummary]: #currentbandwidthsummary
#### [currentBandwidthSummary]
An object that provides commonly used bandwidth summary components for the current billing cycle.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Bandwidth_Summary'>SoftLayer_Metric_Tracking_Object_Bandwidth_Summary </a>**


</div>
<div class="prop-row">

-----
[currentBillableBandwidthUsage]: #currentbillablebandwidthusage
#### [currentBillableBandwidthUsage]
The current billable public outbound bandwidth for this hardware for the current billing cycle.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[customerInstalledOperatingSystemFlag]: #customerinstalledoperatingsystemflag
#### [customerInstalledOperatingSystemFlag]
Indicates if a server has a Customer Installed OS  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[customerOwnedFlag]: #customerownedflag
#### [customerOwnedFlag]
Indicates if a server is a customer owned device.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[datacenter]: #datacenter
#### [datacenter]
Information regarding the datacenter in which a piece of hardware resides.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


</div>
<div class="prop-row">

-----
[datacenterName]: #datacentername
#### [datacenterName]
The name of the datacenter in which a piece of hardware resides.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[daysInSparePool]: #daysinsparepool
#### [daysInSparePool]
Number of day(s) a server have been in spare pool.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[downlinkHardware]: #downlinkhardware
#### [downlinkHardware]
All hardware that has uplink network connections to a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[downlinkNetworkHardware]: #downlinknetworkhardware
#### [downlinkNetworkHardware]
All hardware that has uplink network connections to a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[downlinkServers]: #downlinkservers
#### [downlinkServers]
Information regarding all servers attached to a piece of network hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[downlinkVirtualGuests]: #downlinkvirtualguests
#### [downlinkVirtualGuests]
Information regarding all virtual guests attached to a piece of network hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[downstreamHardwareBindings]: #downstreamhardwarebindings
#### [downstreamHardwareBindings]
All hardware downstream from a network device.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component_Uplink_Hardware'>SoftLayer_Network_Component_Uplink_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[downstreamNetworkHardware]: #downstreamnetworkhardware
#### [downstreamNetworkHardware]
All network hardware downstream from the selected piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[downstreamNetworkHardwareWithIncidents]: #downstreamnetworkhardwarewithincidents
#### [downstreamNetworkHardwareWithIncidents]
All network hardware with monitoring warnings or errors that are downstream from the selected piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[downstreamServers]: #downstreamservers
#### [downstreamServers]
Information regarding all servers attached downstream to a piece of network hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[downstreamVirtualGuests]: #downstreamvirtualguests
#### [downstreamVirtualGuests]
Information regarding all virtual guests attached to a piece of network hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[driveControllers]: #drivecontrollers
#### [driveControllers]
The drive controllers contained within a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**


</div>
<div class="prop-row">

-----
[evaultNetworkStorage]: #evaultnetworkstorage
#### [evaultNetworkStorage]
Information regarding a piece of hardware's associated EVault network storage service account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[firewallServiceComponent]: #firewallservicecomponent
#### [firewallServiceComponent]
Information regarding a piece of hardware's firewall services.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component_Firewall'>SoftLayer_Network_Component_Firewall </a>**


</div>
<div class="prop-row">

-----
[fixedConfigurationPreset]: #fixedconfigurationpreset
#### [fixedConfigurationPreset]
Defines the fixed components in a fixed configuration bare metal server.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Preset'>SoftLayer_Product_Package_Preset </a>**


</div>
<div class="prop-row">

-----
[frontendNetworkComponents]: #frontendnetworkcomponents
#### [frontendNetworkComponents]
A piece of hardware's front-end or public network components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component[] </a>**


</div>
<div class="prop-row">

-----
[frontendRouters]: #frontendrouters
#### [frontendRouters]
A hardware's frontend or public router.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[globalIdentifier]: #globalidentifier
#### [globalIdentifier]
A hardware's universally unique identifier.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[hardDrives]: #harddrives
#### [hardDrives]
The hard drives contained within a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**


</div>
<div class="prop-row">

-----
[hardwareChassis]: #hardwarechassis
#### [hardwareChassis]
The chassis that a piece of hardware is housed in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Chassis'>SoftLayer_Hardware_Chassis </a>**


</div>
<div class="prop-row">

-----
[hardwareFunction]: #hardwarefunction
#### [hardwareFunction]
A hardware's function.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Function'>SoftLayer_Hardware_Function </a>**


</div>
<div class="prop-row">

-----
[hardwareFunctionDescription]: #hardwarefunctiondescription
#### [hardwareFunctionDescription]
A hardware's function.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[hardwareStatus]: #hardwarestatus
#### [hardwareStatus]
A hardware's status.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Status'>SoftLayer_Hardware_Status </a>**


</div>
<div class="prop-row">

-----
[hasSingleRootVirtualizationBillingItemFlag]: #hassinglerootvirtualizationbillingitemflag
#### [hasSingleRootVirtualizationBillingItemFlag]
Determine if hardware has Single Root IO VIrtualization (SR-IOV) billing item.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[hasTrustedPlatformModuleBillingItemFlag]: #hastrustedplatformmodulebillingitemflag
#### [hasTrustedPlatformModuleBillingItemFlag]
Determine in hardware object has TPM enabled.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[hostIpsSoftwareComponent]: #hostipssoftwarecomponent
#### [hostIpsSoftwareComponent]
Information regarding a host IPS software component object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component'>SoftLayer_Software_Component </a>**


</div>
<div class="prop-row">

-----
[hourlyBillingFlag]: #hourlybillingflag
#### [hourlyBillingFlag]
A server's hourly billing status.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[inboundBandwidthUsage]: #inboundbandwidthusage
#### [inboundBandwidthUsage]
The sum of all the inbound network traffic data for the last 30 days.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[inboundPrivateBandwidthUsage]: #inboundprivatebandwidthusage
#### [inboundPrivateBandwidthUsage]
The total private inbound bandwidth for this hardware for the current billing cycle.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[inboundPublicBandwidthUsage]: #inboundpublicbandwidthusage
#### [inboundPublicBandwidthUsage]
The total public inbound bandwidth for this hardware for the current billing cycle.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[isCloudReadyNodeCertified]: #iscloudreadynodecertified
#### [isCloudReadyNodeCertified]
Determine if hardware object has the IBM_CLOUD_READY_NODE_CERTIFIED attribute.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[isIpmiDisabled]: #isipmidisabled
#### [isIpmiDisabled]
Determine if remote management has been disabled due to port speed.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[isVirtualPrivateCloudNode]: #isvirtualprivatecloudnode
#### [isVirtualPrivateCloudNode]
Determine if hardware object is a Virtual Private Cloud node.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[lastOperatingSystemReload]: #lastoperatingsystemreload
#### [lastOperatingSystemReload]
The last transaction that a server's operating system was loaded.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>**


</div>
<div class="prop-row">

-----
[lastTransaction]: #lasttransaction
#### [lastTransaction]
Information regarding the last transaction a server performed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>**


</div>
<div class="prop-row">

-----
[latestNetworkMonitorIncident]: #latestnetworkmonitorincident
#### [latestNetworkMonitorIncident]
A piece of hardware's latest network monitoring incident.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Incident'>SoftLayer_Network_Monitor_Version1_Incident </a>**


</div>
<div class="prop-row">

-----
[location]: #location
#### [location]
Where a piece of hardware is located within SoftLayer's location hierarchy.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


</div>
<div class="prop-row">

-----
[locationPathString]: #locationpathstring
#### [locationPathString]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[lockboxNetworkStorage]: #lockboxnetworkstorage
#### [lockboxNetworkStorage]
Information regarding a lockbox account associated with a server.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage </a>**


</div>
<div class="prop-row">

-----
[logicalVolumeStorageGroups]: #logicalvolumestoragegroups
#### [logicalVolumeStorageGroups]
Returns a list of logical volumes on the physical machine.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group'>SoftLayer_Configuration_Storage_Group[] </a>**


</div>
<div class="prop-row">

-----
[managedResourceFlag]: #managedresourceflag
#### [managedResourceFlag]
A flag indicating that the hardware is a managed resource.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[memory]: #memory
#### [memory]
Information regarding a piece of hardware's memory.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**


</div>
<div class="prop-row">

-----
[memoryCapacity]: #memorycapacity
#### [memoryCapacity]
The amount of memory a piece of hardware has, measured in gigabytes.  
<span class="type-label">Type: </span>**unsigned integer**


</div>
<div class="prop-row">

-----
[metricTrackingObject]: #metrictrackingobject
#### [metricTrackingObject]
A piece of hardware's metric tracking object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_HardwareServer'>SoftLayer_Metric_Tracking_Object_HardwareServer </a>**


</div>
<div class="prop-row">

-----
[metricTrackingObjectId]: #metrictrackingobjectid
#### [metricTrackingObjectId]
The metric tracking object id for this server.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modules]: #modules
#### [modules]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**


</div>
<div class="prop-row">

-----
[monitoringRobot]: #monitoringrobot
#### [monitoringRobot]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Monitoring_Robot'>SoftLayer_Monitoring_Robot </a>**


</div>
<div class="prop-row">

-----
[monitoringServiceComponent]: #monitoringservicecomponent
#### [monitoringServiceComponent]
Information regarding a piece of hardware's network monitoring services.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host_Stratum'>SoftLayer_Network_Monitor_Version1_Query_Host_Stratum </a>**


</div>
<div class="prop-row">

-----
[monitoringServiceEligibilityFlag]: #monitoringserviceeligibilityflag
#### [monitoringServiceEligibilityFlag]
  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[monitoringUserNotification]: #monitoringusernotification
#### [monitoringUserNotification]
The monitoring notification objects for this hardware. Each object links this hardware instance to a user account that will be notified if monitoring on this hardware object fails  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer_Notification_Hardware'>SoftLayer_User_Customer_Notification_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[motherboard]: #motherboard
#### [motherboard]
A server's motherboard.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component </a>**


</div>
<div class="prop-row">

-----
[networkCards]: #networkcards
#### [networkCards]
Information regarding a piece of hardware's network cards.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**


</div>
<div class="prop-row">

-----
[networkComponents]: #networkcomponents
#### [networkComponents]
Returns a hardware's network components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component[] </a>**


</div>
<div class="prop-row">

-----
[networkGatewayMember]: #networkgatewaymember
#### [networkGatewayMember]
The gateway member if this device is part of a network gateway.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway_Member'>SoftLayer_Network_Gateway_Member </a>**


</div>
<div class="prop-row">

-----
[networkGatewayMemberFlag]: #networkgatewaymemberflag
#### [networkGatewayMemberFlag]
Whether or not this device is part of a network gateway.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[networkManagementIpAddress]: #networkmanagementipaddress
#### [networkManagementIpAddress]
A piece of hardware's network management IP address.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[networkMonitorAttachedDownHardware]: #networkmonitorattacheddownhardware
#### [networkMonitorAttachedDownHardware]
All servers with failed monitoring that are attached downstream to a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[networkMonitorAttachedDownVirtualGuests]: #networkmonitorattacheddownvirtualguests
#### [networkMonitorAttachedDownVirtualGuests]
Virtual guests that are attached downstream to a hardware that have failed monitoring  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[networkMonitorIncidents]: #networkmonitorincidents
#### [networkMonitorIncidents]
The status of all of a piece of hardware's network monitoring incidents.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Incident'>SoftLayer_Network_Monitor_Version1_Incident[] </a>**


</div>
<div class="prop-row">

-----
[networkMonitors]: #networkmonitors
#### [networkMonitors]
Information regarding a piece of hardware's network monitors.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host'>SoftLayer_Network_Monitor_Version1_Query_Host[] </a>**


</div>
<div class="prop-row">

-----
[networkStatus]: #networkstatus
#### [networkStatus]
The value of a hardware's network status attribute.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[networkStatusAttribute]: #networkstatusattribute
#### [networkStatusAttribute]
The hardware's related network status attribute.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Attribute'>SoftLayer_Hardware_Attribute </a>**


</div>
<div class="prop-row">

-----
[networkStorage]: #networkstorage
#### [networkStorage]
Information regarding a piece of hardware's associated network storage service account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[networkVlans]: #networkvlans
#### [networkVlans]
The network virtual LANs (VLANs) associated with a piece of hardware's network components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a>**


</div>
<div class="prop-row">

-----
[nextBillingCycleBandwidthAllocation]: #nextbillingcyclebandwidthallocation
#### [nextBillingCycleBandwidthAllocation]
A hardware's allotted bandwidth for the next billing cycle (measured in GB).  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[notesHistory]: #noteshistory
#### [notesHistory]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Note'>SoftLayer_Hardware_Note[] </a>**


</div>
<div class="prop-row">

-----
[nvRamCapacity]: #nvramcapacity
#### [nvRamCapacity]
The amount of non-volatile memory a piece of hardware has, measured in gigabytes.  
<span class="type-label">Type: </span>**unsigned integer**


</div>
<div class="prop-row">

-----
[nvRamComponentModels]: #nvramcomponentmodels
#### [nvRamComponentModels]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model'>SoftLayer_Hardware_Component_Model[] </a>**


</div>
<div class="prop-row">

-----
[openCancellationTicket]: #opencancellationticket
#### [openCancellationTicket]
An open ticket requesting cancellation of this server, if one exists.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>**


</div>
<div class="prop-row">

-----
[operatingSystem]: #operatingsystem
#### [operatingSystem]
Information regarding a piece of hardware's operating system.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component_OperatingSystem'>SoftLayer_Software_Component_OperatingSystem </a>**


</div>
<div class="prop-row">

-----
[operatingSystemReferenceCode]: #operatingsystemreferencecode
#### [operatingSystemReferenceCode]
A hardware's operating system software description.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[outboundBandwidthUsage]: #outboundbandwidthusage
#### [outboundBandwidthUsage]
The sum of all the outbound network traffic data for the last 30 days.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[outboundPrivateBandwidthUsage]: #outboundprivatebandwidthusage
#### [outboundPrivateBandwidthUsage]
The total private outbound bandwidth for this hardware for the current billing cycle.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[outboundPublicBandwidthUsage]: #outboundpublicbandwidthusage
#### [outboundPublicBandwidthUsage]
The total public outbound bandwidth for this hardware for the current billing cycle.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[overBandwidthAllocationFlag]: #overbandwidthallocationflag
#### [overBandwidthAllocationFlag]
Whether the bandwidth usage for this hardware for the current billing cycle exceeds the allocation.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[parentBay]: #parentbay
#### [parentBay]
Blade Bay  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Blade'>SoftLayer_Hardware_Blade </a>**


</div>
<div class="prop-row">

-----
[parentHardware]: #parenthardware
#### [parentHardware]
Parent Hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**


</div>
<div class="prop-row">

-----
[pointOfPresenceLocation]: #pointofpresencelocation
#### [pointOfPresenceLocation]
Information regarding the Point of Presence (PoP) location in which a piece of hardware resides.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


</div>
<div class="prop-row">

-----
[powerComponents]: #powercomponents
#### [powerComponents]
The power components for a hardware object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Power_Component'>SoftLayer_Hardware_Power_Component[] </a>**


</div>
<div class="prop-row">

-----
[powerSupply]: #powersupply
#### [powerSupply]
A server's power supply.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**


</div>
<div class="prop-row">

-----
[primaryBackendIpAddress]: #primarybackendipaddress
#### [primaryBackendIpAddress]
The hardware's primary private IP address.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[primaryBackendNetworkComponent]: #primarybackendnetworkcomponent
#### [primaryBackendNetworkComponent]
Information regarding the hardware's primary back-end network component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a>**


</div>
<div class="prop-row">

-----
[primaryIpAddress]: #primaryipaddress
#### [primaryIpAddress]
The hardware's primary public IP address.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[primaryNetworkComponent]: #primarynetworkcomponent
#### [primaryNetworkComponent]
Information regarding the hardware's primary public network component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a>**


</div>
<div class="prop-row">

-----
[privateIpAddress]: #privateipaddress
#### [privateIpAddress]
A server's primary private IP address.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[privateNetworkOnlyFlag]: #privatenetworkonlyflag
#### [privateNetworkOnlyFlag]
Whether the hardware only has access to the private network.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[processorCoreAmount]: #processorcoreamount
#### [processorCoreAmount]
The total number of processor cores, summed from all processors that are attached to a piece of hardware  
<span class="type-label">Type: </span>**unsigned integer**


</div>
<div class="prop-row">

-----
[processorPhysicalCoreAmount]: #processorphysicalcoreamount
#### [processorPhysicalCoreAmount]
The total number of physical processor cores, summed from all processors that are attached to a piece of hardware  
<span class="type-label">Type: </span>**unsigned integer**


</div>
<div class="prop-row">

-----
[processors]: #processors
#### [processors]
Information regarding a piece of hardware's processors.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**


</div>
<div class="prop-row">

-----
[projectedOverBandwidthAllocationFlag]: #projectedoverbandwidthallocationflag
#### [projectedOverBandwidthAllocationFlag]
Whether the bandwidth usage for this hardware for the current billing cycle is projected to exceed the allocation.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[projectedPublicBandwidthUsage]: #projectedpublicbandwidthusage
#### [projectedPublicBandwidthUsage]
The projected public outbound bandwidth for this hardware for the current billing cycle.  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[rack]: #rack
#### [rack]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


</div>
<div class="prop-row">

-----
[raidControllers]: #raidcontrollers
#### [raidControllers]
The RAID controllers contained within a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**


</div>
<div class="prop-row">

-----
[readyNodeFlag]: #readynodeflag
#### [readyNodeFlag]
Determine if hardware object is vSan Ready Node.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[recentEvents]: #recentevents
#### [recentEvents]
Recent events that impact this hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Event'>SoftLayer_Notification_Occurrence_Event[] </a>**


</div>
<div class="prop-row">

-----
[recentRemoteManagementCommands]: #recentremotemanagementcommands
#### [recentRemoteManagementCommands]
The last five commands issued to the server's remote management card.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_Command_Request'>SoftLayer_Hardware_Component_RemoteManagement_Command_Request[] </a>**


</div>
<div class="prop-row">

-----
[regionalInternetRegistry]: #regionalinternetregistry
#### [regionalInternetRegistry]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Regional_Internet_Registry'>SoftLayer_Network_Regional_Internet_Registry </a>**


</div>
<div class="prop-row">

-----
[remoteManagement]: #remotemanagement
#### [remoteManagement]
A server's remote management card.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement'>SoftLayer_Hardware_Component_RemoteManagement </a>**


</div>
<div class="prop-row">

-----
[remoteManagementAccounts]: #remotemanagementaccounts
#### [remoteManagementAccounts]
User credentials to issue commands and/or interact with the server's remote management card.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_User'>SoftLayer_Hardware_Component_RemoteManagement_User[] </a>**


</div>
<div class="prop-row">

-----
[remoteManagementComponent]: #remotemanagementcomponent
#### [remoteManagementComponent]
A hardware's associated remote management component. This is normally IPMI.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a>**


</div>
<div class="prop-row">

-----
[remoteManagementUsers]: #remotemanagementusers
#### [remoteManagementUsers]
User(s) who have access to issue commands and/or interact with the server's remote management card.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_User'>SoftLayer_Hardware_Component_RemoteManagement_User[] </a>**


</div>
<div class="prop-row">

-----
[resourceConfigurations]: #resourceconfigurations
#### [resourceConfigurations]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Resource_Configuration'>SoftLayer_Hardware_Resource_Configuration[] </a>**


</div>
<div class="prop-row">

-----
[resourceGroupMemberReferences]: #resourcegroupmemberreferences
#### [resourceGroupMemberReferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Member'>SoftLayer_Resource_Group_Member[] </a>**


</div>
<div class="prop-row">

-----
[resourceGroupRoles]: #resourcegrouproles
#### [resourceGroupRoles]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Role'>SoftLayer_Resource_Group_Role[] </a>**


</div>
<div class="prop-row">

-----
[resourceGroups]: #resourcegroups
#### [resourceGroups]
The resource groups in which this hardware is a member.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group'>SoftLayer_Resource_Group[] </a>**


</div>
<div class="prop-row">

-----
[routers]: #routers
#### [routers]
A hardware's routers.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[scaleAssets]: #scaleassets
#### [scaleAssets]
Collection of scale assets this hardware corresponds to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Asset'>SoftLayer_Scale_Asset[] </a>**


</div>
<div class="prop-row">

-----
[securityScanRequests]: #securityscanrequests
#### [securityScanRequests]
Information regarding a piece of hardware's vulnerability scan requests.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Security_Scanner_Request'>SoftLayer_Network_Security_Scanner_Request[] </a>**


</div>
<div class="prop-row">

-----
[serverRoom]: #serverroom
#### [serverRoom]
Information regarding the server room in which the hardware is located.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


</div>
<div class="prop-row">

-----
[serviceProvider]: #serviceprovider
#### [serviceProvider]
Information regarding the piece of hardware's service provider.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Service_Provider'>SoftLayer_Service_Provider </a>**


</div>
<div class="prop-row">

-----
[softwareComponents]: #softwarecomponents
#### [softwareComponents]
Information regarding a piece of hardware's installed software.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component'>SoftLayer_Software_Component[] </a>**


</div>
<div class="prop-row">

-----
[softwareGuardExtensionEnabled]: #softwareguardextensionenabled
#### [softwareGuardExtensionEnabled]
Determine if hardware object has Software Guard Extension (SGX) enabled.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[sshKeys]: #sshkeys
#### [sshKeys]
SSH keys to be installed on the server during provisioning or an OS reload.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Ssh_Key'>SoftLayer_Security_Ssh_Key[] </a>**


</div>
<div class="prop-row">

-----
[statisticsRemoteManagement]: #statisticsremotemanagement
#### [statisticsRemoteManagement]
A server's remote management card used for statistics.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement'>SoftLayer_Hardware_Component_RemoteManagement </a>**


</div>
<div class="prop-row">

-----
[storageGroups]: #storagegroups
#### [storageGroups]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group'>SoftLayer_Configuration_Storage_Group[] </a>**


</div>
<div class="prop-row">

-----
[storageNetworkComponents]: #storagenetworkcomponents
#### [storageNetworkComponents]
A piece of hardware's private storage network components. [Deprecated]  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component[] </a>**


</div>
<div class="prop-row">

-----
[tagReferences]: #tagreferences
#### [tagReferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Tag_Reference'>SoftLayer_Tag_Reference[] </a>**


</div>
<div class="prop-row">

-----
[topLevelLocation]: #toplevellocation
#### [topLevelLocation]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


</div>
<div class="prop-row">

-----
[uefiBootFlag]: #uefibootflag
#### [uefiBootFlag]
Whether to use UEFI boot instead of BIOS.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[upgradeRequest]: #upgraderequest
#### [upgradeRequest]
An account's associated upgrade request object, if any.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Upgrade_Request'>SoftLayer_Product_Upgrade_Request </a>**


</div>
<div class="prop-row">

-----
[uplinkHardware]: #uplinkhardware
#### [uplinkHardware]
The network device connected to a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**


</div>
<div class="prop-row">

-----
[uplinkNetworkComponents]: #uplinknetworkcomponents
#### [uplinkNetworkComponents]
Information regarding the network component that is one level higher than a piece of hardware on the network infrastructure.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component[] </a>**


</div>
<div class="prop-row">

-----
[userData]: #userdata
#### [userData]
An array containing a single string of custom user data for a hardware order. Max size is 16 kb.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Attribute'>SoftLayer_Hardware_Attribute[] </a>**


</div>
<div class="prop-row">

-----
[users]: #users
#### [users]
A list of users that have access to this computing instance.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer[] </a>**


</div>
<div class="prop-row">

-----
[virtualChassis]: #virtualchassis
#### [virtualChassis]
Information regarding the virtual chassis for a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Group'>SoftLayer_Hardware_Group </a>**


</div>
<div class="prop-row">

-----
[virtualChassisSiblings]: #virtualchassissiblings
#### [virtualChassisSiblings]
Information regarding the virtual chassis siblings for a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[virtualGuests]: #virtualguests
#### [virtualGuests]
A hardware server's virtual servers.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[virtualHost]: #virtualhost
#### [virtualHost]
A piece of hardware's virtual host record.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Host'>SoftLayer_Virtual_Host </a>**


</div>
<div class="prop-row">

-----
[virtualLicenses]: #virtuallicenses
#### [virtualLicenses]
Information regarding a piece of hardware's virtual software licenses.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_VirtualLicense'>SoftLayer_Software_VirtualLicense[] </a>**


</div>
<div class="prop-row">

-----
[virtualRack]: #virtualrack
#### [virtualRack]
Information regarding the bandwidth allotment to which a piece of hardware belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment </a>**


</div>
<div class="prop-row">

-----
[virtualRackId]: #virtualrackid
#### [virtualRackId]
The name of the bandwidth allotment belonging to a piece of hardware.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[virtualRackName]: #virtualrackname
#### [virtualRackName]
The name of the bandwidth allotment belonging to a piece of hardware.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[virtualizationPlatform]: #virtualizationplatform
#### [virtualizationPlatform]
A piece of hardware's virtualization platform software.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component'>SoftLayer_Software_Component </a>**


</div>

## Count
<div class="prop-row">

-----
[activeComponentCount]: #activecomponentcount
#### [activeComponentCount]
A count of a piece of hardware's active physical components.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[activeNetworkMonitorIncidentCount]: #activenetworkmonitorincidentcount
#### [activeNetworkMonitorIncidentCount]
A count of a piece of hardware's active network monitoring incidents.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[activeTicketCount]: #activeticketcount
#### [activeTicketCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[activeTransactionCount]: #activetransactioncount
#### [activeTransactionCount]
A count of any active transaction(s) that are currently running for the server (example: os reload).   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[allPowerComponentCount]: #allpowercomponentcount
#### [allPowerComponentCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[allowedNetworkStorageCount]: #allowednetworkstoragecount
#### [allowedNetworkStorageCount]
A count of the SoftLayer_Network_Storage objects that this SoftLayer_Hardware has access to.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[allowedNetworkStorageReplicaCount]: #allowednetworkstoragereplicacount
#### [allowedNetworkStorageReplicaCount]
A count of the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of information regarding a piece of hardware's specific attributes.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[availableMonitoringCount]: #availablemonitoringcount
#### [availableMonitoringCount]
A count of an object that stores the maximum level for the monitoring query types and response types.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[backendNetworkComponentCount]: #backendnetworkcomponentcount
#### [backendNetworkComponentCount]
A count of a piece of hardware's back-end or private network components.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[backendRouterCount]: #backendroutercount
#### [backendRouterCount]
A count of a hardware's backend or private router.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[benchmarkCertificationCount]: #benchmarkcertificationcount
#### [benchmarkCertificationCount]
A count of information regarding a piece of hardware's benchmark certifications.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[billingCycleBandwidthUsageCount]: #billingcyclebandwidthusagecount
#### [billingCycleBandwidthUsageCount]
A count of the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this server is attached to.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[childrenHardwareCount]: #childrenhardwarecount
#### [childrenHardwareCount]
A count of child hardware.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[componentCount]: #componentcount
#### [componentCount]
A count of a piece of hardware's components.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[downlinkHardwareCount]: #downlinkhardwarecount
#### [downlinkHardwareCount]
A count of all hardware that has uplink network connections to a piece of hardware.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[downlinkNetworkHardwareCount]: #downlinknetworkhardwarecount
#### [downlinkNetworkHardwareCount]
A count of all hardware that has uplink network connections to a piece of hardware.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[downlinkServerCount]: #downlinkservercount
#### [downlinkServerCount]
A count of information regarding all servers attached to a piece of network hardware.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[downlinkVirtualGuestCount]: #downlinkvirtualguestcount
#### [downlinkVirtualGuestCount]
A count of information regarding all virtual guests attached to a piece of network hardware.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[downstreamHardwareBindingCount]: #downstreamhardwarebindingcount
#### [downstreamHardwareBindingCount]
A count of all hardware downstream from a network device.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[downstreamNetworkHardwareCount]: #downstreamnetworkhardwarecount
#### [downstreamNetworkHardwareCount]
A count of all network hardware downstream from the selected piece of hardware.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[downstreamNetworkHardwareWithIncidentCount]: #downstreamnetworkhardwarewithincidentcount
#### [downstreamNetworkHardwareWithIncidentCount]
A count of all network hardware with monitoring warnings or errors that are downstream from the selected piece of hardware.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[downstreamServerCount]: #downstreamservercount
#### [downstreamServerCount]
A count of information regarding all servers attached downstream to a piece of network hardware.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[downstreamVirtualGuestCount]: #downstreamvirtualguestcount
#### [downstreamVirtualGuestCount]
A count of information regarding all virtual guests attached to a piece of network hardware.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[driveControllerCount]: #drivecontrollercount
#### [driveControllerCount]
A count of the drive controllers contained within a piece of hardware.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[evaultNetworkStorageCount]: #evaultnetworkstoragecount
#### [evaultNetworkStorageCount]
A count of information regarding a piece of hardware's associated EVault network storage service account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[frontendNetworkComponentCount]: #frontendnetworkcomponentcount
#### [frontendNetworkComponentCount]
A count of a piece of hardware's front-end or public network components.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[frontendRouterCount]: #frontendroutercount
#### [frontendRouterCount]
A count of a hardware's frontend or public router.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[hardDriveCount]: #harddrivecount
#### [hardDriveCount]
A count of the hard drives contained within a piece of hardware.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[logicalVolumeStorageGroupCount]: #logicalvolumestoragegroupcount
#### [logicalVolumeStorageGroupCount]
A count of returns a list of logical volumes on the physical machine.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[memoryCount]: #memorycount
#### [memoryCount]
A count of information regarding a piece of hardware's memory.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[moduleCount]: #modulecount
#### [moduleCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[monitoringUserNotificationCount]: #monitoringusernotificationcount
#### [monitoringUserNotificationCount]
A count of the monitoring notification objects for this hardware. Each object links this hardware instance to a user account that will be notified if monitoring on this hardware object fails   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkCardCount]: #networkcardcount
#### [networkCardCount]
A count of information regarding a piece of hardware's network cards.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkComponentCount]: #networkcomponentcount
#### [networkComponentCount]
A count of returns a hardware's network components.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkMonitorAttachedDownHardwareCount]: #networkmonitorattacheddownhardwarecount
#### [networkMonitorAttachedDownHardwareCount]
A count of all servers with failed monitoring that are attached downstream to a piece of hardware.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkMonitorAttachedDownVirtualGuestCount]: #networkmonitorattacheddownvirtualguestcount
#### [networkMonitorAttachedDownVirtualGuestCount]
A count of virtual guests that are attached downstream to a hardware that have failed monitoring   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkMonitorCount]: #networkmonitorcount
#### [networkMonitorCount]
A count of information regarding a piece of hardware's network monitors.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkMonitorIncidentCount]: #networkmonitorincidentcount
#### [networkMonitorIncidentCount]
A count of the status of all of a piece of hardware's network monitoring incidents.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkStorageCount]: #networkstoragecount
#### [networkStorageCount]
A count of information regarding a piece of hardware's associated network storage service account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkVlanCount]: #networkvlancount
#### [networkVlanCount]
A count of the network virtual LANs (VLANs) associated with a piece of hardware's network components.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[notesHistoryCount]: #noteshistorycount
#### [notesHistoryCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[nvRamComponentModelCount]: #nvramcomponentmodelcount
#### [nvRamComponentModelCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[powerComponentCount]: #powercomponentcount
#### [powerComponentCount]
A count of the power components for a hardware object.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[powerSupplyCount]: #powersupplycount
#### [powerSupplyCount]
A count of a server's power supply.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[processorCount]: #processorcount
#### [processorCount]
A count of information regarding a piece of hardware's processors.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[raidControllerCount]: #raidcontrollercount
#### [raidControllerCount]
A count of the RAID controllers contained within a piece of hardware.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[recentEventCount]: #recenteventcount
#### [recentEventCount]
A count of recent events that impact this hardware.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[recentRemoteManagementCommandCount]: #recentremotemanagementcommandcount
#### [recentRemoteManagementCommandCount]
A count of the last five commands issued to the server's remote management card.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[remoteManagementAccountCount]: #remotemanagementaccountcount
#### [remoteManagementAccountCount]
A count of user credentials to issue commands and/or interact with the server's remote management card.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[remoteManagementUserCount]: #remotemanagementusercount
#### [remoteManagementUserCount]
A count of user(s) who have access to issue commands and/or interact with the server's remote management card.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[resourceConfigurationCount]: #resourceconfigurationcount
#### [resourceConfigurationCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[resourceGroupCount]: #resourcegroupcount
#### [resourceGroupCount]
A count of the resource groups in which this hardware is a member.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[resourceGroupMemberReferenceCount]: #resourcegroupmemberreferencecount
#### [resourceGroupMemberReferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[resourceGroupRoleCount]: #resourcegrouprolecount
#### [resourceGroupRoleCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[routerCount]: #routercount
#### [routerCount]
A count of a hardware's routers.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[scaleAssetCount]: #scaleassetcount
#### [scaleAssetCount]
A count of collection of scale assets this hardware corresponds to.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[securityScanRequestCount]: #securityscanrequestcount
#### [securityScanRequestCount]
A count of information regarding a piece of hardware's vulnerability scan requests.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[softwareComponentCount]: #softwarecomponentcount
#### [softwareComponentCount]
A count of information regarding a piece of hardware's installed software.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[sshKeyCount]: #sshkeycount
#### [sshKeyCount]
A count of sSH keys to be installed on the server during provisioning or an OS reload.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[storageGroupCount]: #storagegroupcount
#### [storageGroupCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[storageNetworkComponentCount]: #storagenetworkcomponentcount
#### [storageNetworkComponentCount]
A count of a piece of hardware's private storage network components. [Deprecated]   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[tagReferenceCount]: #tagreferencecount
#### [tagReferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[uplinkNetworkComponentCount]: #uplinknetworkcomponentcount
#### [uplinkNetworkComponentCount]
A count of information regarding the network component that is one level higher than a piece of hardware on the network infrastructure.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[userCount]: #usercount
#### [userCount]
A count of a list of users that have access to this computing instance.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[userDataCount]: #userdatacount
#### [userDataCount]
A count of an array containing a single string of custom user data for a hardware order. Max size is 16 kb.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[virtualChassisSiblingCount]: #virtualchassissiblingcount
#### [virtualChassisSiblingCount]
A count of information regarding the virtual chassis siblings for a piece of hardware.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[virtualGuestCount]: #virtualguestcount
#### [virtualGuestCount]
A count of a hardware server's virtual servers.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[virtualLicenseCount]: #virtuallicensecount
#### [virtualLicenseCount]
A count of information regarding a piece of hardware's virtual software licenses.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


