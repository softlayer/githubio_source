---
title: "SoftLayer_Virtual_Guest"
description: "The virtual guest data type presents the structure in which all virtual guests will be presented. Internally, the struct... "
layout: "datatype"
tags:
    - "datatype"
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


The virtual guest data type presents the structure in which all virtual guests will be presented. Internally, the structure supports various virtualization platforms with no change to external interaction. 

A guest, also known as a virtual server, represents an allocation of resources on a virtual host. 


### associatedMethods

*  [SoftLayer_Virtual_Guest::checkHostDiskAvailability](/reference/services/SoftLayer_Virtual_Guest/checkHostDiskAvailability )





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
A computing instance's associated [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) id   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date a virtual computing instance was created.   
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[dedicatedAccountHostOnlyFlag]: #dedicatedaccounthostonlyflag
#### [dedicatedAccountHostOnlyFlag]
When true this flag specifies that a compute instance is to run on hosts that only have guests from the same account.   
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[deviceStatusId]: #devicestatusid
#### [deviceStatusId]
The device status ID of the virtual guest.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[domain]: #domain
#### [domain]
A computing instance's domain name   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[fullyQualifiedDomainName]: #fullyqualifieddomainname
#### [fullyQualifiedDomainName]
A name reflecting the hostname and domain of the computing instance.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[hostname]: #hostname
#### [hostname]
A virtual computing instance's hostname   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Unique ID for a computing instance.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[lastPowerStateId]: #lastpowerstateid
#### [lastPowerStateId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[lastVerifiedDate]: #lastverifieddate
#### [lastVerifiedDate]
The last timestamp of when the guest was verified as a resident virtual machine on the host's hypervisor platform.   
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[maxCpu]: #maxcpu
#### [maxCpu]
The maximum amount of CPU resources a computing instance may utilize.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[maxCpuUnits]: #maxcpuunits
#### [maxCpuUnits]
The unit of the maximum amount of CPU resources a computing instance may utilize.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[maxMemory]: #maxmemory
#### [maxMemory]
The maximum amount of memory a computing instance may utilize.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[metricPollDate]: #metricpolldate
#### [metricPollDate]
The date of the most recent metric tracking poll performed.   
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a virtual computing instance was last modified.   
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[notes]: #notes
#### [notes]
A note of up to 1,000 characters about a virtual server.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[placementGroupId]: #placementgroupid
#### [placementGroupId]
The placement group ID that the virtual guest belongs to.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[postInstallScriptUri]: #postinstallscripturi
#### [postInstallScriptUri]
URI of the script to be downloaded and executed after installation is complete. This is deprecated in favor of supplementalCreateObjectOptions' postInstallScriptUri.   
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
[startCpus]: #startcpus
#### [startCpus]
The number of CPUs available to a computing instance upon startup.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[statusId]: #statusid
#### [statusId]
A computing instances [SoftLayer_Virtual_Guest_Status]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Status">}}) ID   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[supplementalCreateObjectOptions]: #supplementalcreateobjectoptions
#### [supplementalCreateObjectOptions]
Extra options needed for [SoftLayer_Virtual_Guest::createObject]({{<ref "reference/services/SoftLayer_Virtual_Guest/createObject">}}).   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_SupplementalCreateObjectOptions'>SoftLayer_Virtual_Guest_SupplementalCreateObjectOptions </a>**  



</div>
<div class="prop-row">

-----
[typeId]: #typeid
#### [typeId]
Gives the type of guest categorized as PUBLIC, DEDICATED or PRIVATE.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[uuid]: #uuid
#### [uuid]
Unique ID for a computing instance's record on a virtualization platform.   
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account that a virtual guest belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[accountOwnedPoolFlag]: #accountownedpoolflag
#### [accountOwnedPoolFlag]
  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[activeNetworkMonitorIncident]: #activenetworkmonitorincident
#### [activeNetworkMonitorIncident]
A virtual guest's currently active network monitoring incidents.  
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
A transaction that is still be performed on a cloud server.  
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
[allowedHost]: #allowedhost
#### [allowedHost]
The SoftLayer_Network_Storage_Allowed_Host information to connect this Virtual Guest to Network Storage volumes that require access control lists.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Allowed_Host'>SoftLayer_Network_Storage_Allowed_Host </a>**  



</div>
<div class="prop-row">

-----
[allowedNetworkStorage]: #allowednetworkstorage
#### [allowedNetworkStorage]
The SoftLayer_Network_Storage objects that this SoftLayer_Virtual_Guest has access to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**  



</div>
<div class="prop-row">

-----
[allowedNetworkStorageReplicas]: #allowednetworkstoragereplicas
#### [allowedNetworkStorageReplicas]
The SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Virtual_Guest has access to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**  



</div>
<div class="prop-row">

-----
[antivirusSpywareSoftwareComponent]: #antivirusspywaresoftwarecomponent
#### [antivirusSpywareSoftwareComponent]
A antivirus / spyware software component object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component'>SoftLayer_Software_Component </a>**  



</div>
<div class="prop-row">

-----
[applicationDeliveryController]: #applicationdeliverycontroller
#### [applicationDeliveryController]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller'>SoftLayer_Network_Application_Delivery_Controller </a>**  



</div>
<div class="prop-row">

-----
[attributes]: #attributes
#### [attributes]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Attribute'>SoftLayer_Virtual_Guest_Attribute[] </a>**  



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
A guests's backend network components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component'>SoftLayer_Virtual_Guest_Network_Component[] </a>**  



</div>
<div class="prop-row">

-----
[backendRouters]: #backendrouters
#### [backendRouters]
A guest's backend or private router.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**  



</div>
<div class="prop-row">

-----
[bandwidthAllocation]: #bandwidthallocation
#### [bandwidthAllocation]
A computing instance's allotted bandwidth (measured in GB).  
<span class="type-label">Type: </span>**decimal**  



</div>
<div class="prop-row">

-----
[bandwidthAllotmentDetail]: #bandwidthallotmentdetail
#### [bandwidthAllotmentDetail]
A computing instance's allotted detail record. Allotment details link bandwidth allocation with allotments.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment_Detail'>SoftLayer_Network_Bandwidth_Version1_Allotment_Detail </a>**  



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
The billing item for a CloudLayer Compute Instance.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Virtual_Guest'>SoftLayer_Billing_Item_Virtual_Guest </a>**  



</div>
<div class="prop-row">

-----
[blockCancelBecauseDisconnectedFlag]: #blockcancelbecausedisconnectedflag
#### [blockCancelBecauseDisconnectedFlag]
Determines whether the instance is ineligible for cancellation because it is disconnected.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[blockDeviceTemplateGroup]: #blockdevicetemplategroup
#### [blockDeviceTemplateGroup]
The global identifier for the image template that was used to provision or reload a guest.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group'>SoftLayer_Virtual_Guest_Block_Device_Template_Group </a>**  



</div>
<div class="prop-row">

-----
[blockDevices]: #blockdevices
#### [blockDevices]
A computing instance's block devices. Block devices link [SoftLayer_Virtual_Disk_Image]({{<ref "reference/datatypes/SoftLayer_Virtual_Disk_Image">}}) to computing instances.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device'>SoftLayer_Virtual_Guest_Block_Device[] </a>**  



</div>
<div class="prop-row">

-----
[browserConsoleAccessLogs]: #browserconsoleaccesslogs
#### [browserConsoleAccessLogs]
A virtual guest's browser access logs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_BrowserConsoleAccessLog'>SoftLayer_Virtual_BrowserConsoleAccessLog[] </a>**  



</div>
<div class="prop-row">

-----
[consoleData]: #consoledata
#### [consoleData]
A container for a guest's console data  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Virtual_ConsoleData'>SoftLayer_Container_Virtual_ConsoleData </a>**  



</div>
<div class="prop-row">

-----
[consoleIpAddressFlag]: #consoleipaddressflag
#### [consoleIpAddressFlag]
A flag indicating a computing instance's console IP address is assigned.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[consoleIpAddressRecord]: #consoleipaddressrecord
#### [consoleIpAddressRecord]
A record containing information about a computing instance's console IP and port number.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component_IpAddress'>SoftLayer_Virtual_Guest_Network_Component_IpAddress </a>**  



</div>
<div class="prop-row">

-----
[continuousDataProtectionSoftwareComponent]: #continuousdataprotectionsoftwarecomponent
#### [continuousDataProtectionSoftwareComponent]
A continuous data protection software component object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component'>SoftLayer_Software_Component </a>**  



</div>
<div class="prop-row">

-----
[controlPanel]: #controlpanel
#### [controlPanel]
A guest's control panel.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component'>SoftLayer_Software_Component </a>**  



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
[datacenter]: #datacenter
#### [datacenter]
The datacenter that a virtual guest resides in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**  



</div>
<div class="prop-row">

-----
[dedicatedHost]: #dedicatedhost
#### [dedicatedHost]
The dedicated host associated with this guest.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_DedicatedHost'>SoftLayer_Virtual_DedicatedHost </a>**  



</div>
<div class="prop-row">

-----
[deviceStatus]: #devicestatus
#### [deviceStatus]
The device status of this virtual guest.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Device_Status'>SoftLayer_Device_Status </a>**  



</div>
<div class="prop-row">

-----
[evaultNetworkStorage]: #evaultnetworkstorage
#### [evaultNetworkStorage]
A guest's associated EVault network storage service account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**  



</div>
<div class="prop-row">

-----
[firewallServiceComponent]: #firewallservicecomponent
#### [firewallServiceComponent]
A computing instance's hardware firewall services.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component_Firewall'>SoftLayer_Network_Component_Firewall </a>**  



</div>
<div class="prop-row">

-----
[frontendNetworkComponents]: #frontendnetworkcomponents
#### [frontendNetworkComponents]
A guest's frontend network components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component'>SoftLayer_Virtual_Guest_Network_Component[] </a>**  



</div>
<div class="prop-row">

-----
[frontendRouters]: #frontendrouters
#### [frontendRouters]
A guest's frontend or public router.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**  



</div>
<div class="prop-row">

-----
[globalIdentifier]: #globalidentifier
#### [globalIdentifier]
A guest's universally unique identifier.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[gpuCount]: #gpucount
#### [gpuCount]
The number of GPUs attached to the guest.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[gpuType]: #gputype
#### [gpuType]
The name of the GPU type attached to the guest.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[guestBootParameter]: #guestbootparameter
#### [guestBootParameter]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Boot_Parameter'>SoftLayer_Virtual_Guest_Boot_Parameter </a>**  



</div>
<div class="prop-row">

-----
[hardwareFunctionDescription]: #hardwarefunctiondescription
#### [hardwareFunctionDescription]
The object's function.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[host]: #host
#### [host]
The virtual host on which a virtual guest resides (available only on private clouds).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Host'>SoftLayer_Virtual_Host </a>**  



</div>
<div class="prop-row">

-----
[hostIpsSoftwareComponent]: #hostipssoftwarecomponent
#### [hostIpsSoftwareComponent]
A host IPS software component object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component'>SoftLayer_Software_Component </a>**  



</div>
<div class="prop-row">

-----
[hourlyBillingFlag]: #hourlybillingflag
#### [hourlyBillingFlag]
A guest's hourly billing status.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[inboundPrivateBandwidthUsage]: #inboundprivatebandwidthusage
#### [inboundPrivateBandwidthUsage]
The total private inbound bandwidth for this computing instance for the current billing cycle.  
<span class="type-label">Type: </span>**decimal**  



</div>
<div class="prop-row">

-----
[inboundPublicBandwidthUsage]: #inboundpublicbandwidthusage
#### [inboundPublicBandwidthUsage]
The total public inbound bandwidth for this computing instance for the current billing cycle.  
<span class="type-label">Type: </span>**decimal**  



</div>
<div class="prop-row">

-----
[internalTagReferences]: #internaltagreferences
#### [internalTagReferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Tag_Reference'>SoftLayer_Tag_Reference[] </a>**  



</div>
<div class="prop-row">

-----
[lastKnownPowerState]: #lastknownpowerstate
#### [lastKnownPowerState]
The last known power state of a virtual guest in the event the guest is turned off outside of IMS or has gone offline.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Power_State'>SoftLayer_Virtual_Guest_Power_State </a>**  



</div>
<div class="prop-row">

-----
[lastOperatingSystemReload]: #lastoperatingsystemreload
#### [lastOperatingSystemReload]
The last transaction that a cloud server's operating system was loaded.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>**  



</div>
<div class="prop-row">

-----
[lastTransaction]: #lasttransaction
#### [lastTransaction]
The last transaction a cloud server had performed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>**  



</div>
<div class="prop-row">

-----
[latestNetworkMonitorIncident]: #latestnetworkmonitorincident
#### [latestNetworkMonitorIncident]
A virtual guest's latest network monitoring incident.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Incident'>SoftLayer_Network_Monitor_Version1_Incident </a>**  



</div>
<div class="prop-row">

-----
[localDiskFlag]: #localdiskflag
#### [localDiskFlag]
A flag indicating that the virtual guest has at least one disk which is local to the host it runs on. This does not include a SWAP device.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[location]: #location
#### [location]
Where guest is located within SoftLayer's location hierarchy.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**  



</div>
<div class="prop-row">

-----
[managedResourceFlag]: #managedresourceflag
#### [managedResourceFlag]
A flag indicating that the virtual guest is a managed resource.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[metricTrackingObject]: #metrictrackingobject
#### [metricTrackingObject]
A guest's metric tracking object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object'>SoftLayer_Metric_Tracking_Object </a>**  



</div>
<div class="prop-row">

-----
[metricTrackingObjectId]: #metrictrackingobjectid
#### [metricTrackingObjectId]
The metric tracking object id for this guest.  
<span class="type-label">Type: </span>**integer**  



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
A virtual guest's network monitoring services.  
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
The monitoring notification objects for this guest. Each object links this guest instance to a user account that will be notified if monitoring on this guest object fails  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer_Notification_Virtual_Guest'>SoftLayer_User_Customer_Notification_Virtual_Guest[] </a>**  



</div>
<div class="prop-row">

-----
[networkComponents]: #networkcomponents
#### [networkComponents]
A guests's network components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component'>SoftLayer_Virtual_Guest_Network_Component[] </a>**  



</div>
<div class="prop-row">

-----
[networkMonitorIncidents]: #networkmonitorincidents
#### [networkMonitorIncidents]
All of a virtual guest's network monitoring incidents.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Incident'>SoftLayer_Network_Monitor_Version1_Incident[] </a>**  



</div>
<div class="prop-row">

-----
[networkMonitors]: #networkmonitors
#### [networkMonitors]
A guests's network monitors.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host'>SoftLayer_Network_Monitor_Version1_Query_Host[] </a>**  



</div>
<div class="prop-row">

-----
[networkStorage]: #networkstorage
#### [networkStorage]
A guest's associated network storage accounts.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**  



</div>
<div class="prop-row">

-----
[networkVlans]: #networkvlans
#### [networkVlans]
The network Vlans that a guest's network components are associated with.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a>**  



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
A guest's operating system.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component_OperatingSystem'>SoftLayer_Software_Component_OperatingSystem </a>**  



</div>
<div class="prop-row">

-----
[operatingSystemReferenceCode]: #operatingsystemreferencecode
#### [operatingSystemReferenceCode]
A guest's operating system software description.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[orderedPackageId]: #orderedpackageid
#### [orderedPackageId]
The original package id provided with the order for a Cloud Computing Instance.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[outboundPrivateBandwidthUsage]: #outboundprivatebandwidthusage
#### [outboundPrivateBandwidthUsage]
The total private outbound bandwidth for this computing instance for the current billing cycle.  
<span class="type-label">Type: </span>**decimal**  



</div>
<div class="prop-row">

-----
[outboundPublicBandwidthUsage]: #outboundpublicbandwidthusage
#### [outboundPublicBandwidthUsage]
The total public outbound bandwidth for this computing instance for the current billing cycle.  
<span class="type-label">Type: </span>**decimal**  



</div>
<div class="prop-row">

-----
[overBandwidthAllocationFlag]: #overbandwidthallocationflag
#### [overBandwidthAllocationFlag]
Whether the bandwidth usage for this computing instance for the current billing cycle exceeds the allocation.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[pendingMigrationFlag]: #pendingmigrationflag
#### [pendingMigrationFlag]
When true this virtual guest must be migrated using SoftLayer_Virtual_Guest::migrate.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[placementGroup]: #placementgroup
#### [placementGroup]
The placement group that a virtual guest belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_PlacementGroup'>SoftLayer_Virtual_PlacementGroup </a>**  



</div>
<div class="prop-row">

-----
[powerState]: #powerstate
#### [powerState]
The current power state of a virtual guest.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Power_State'>SoftLayer_Virtual_Guest_Power_State </a>**  



</div>
<div class="prop-row">

-----
[primaryBackendIpAddress]: #primarybackendipaddress
#### [primaryBackendIpAddress]
A guest's primary private IP address.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[primaryBackendNetworkComponent]: #primarybackendnetworkcomponent
#### [primaryBackendNetworkComponent]
A guest's primary backend network component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component'>SoftLayer_Virtual_Guest_Network_Component </a>**  



</div>
<div class="prop-row">

-----
[primaryIpAddress]: #primaryipaddress
#### [primaryIpAddress]
The guest's primary public IP address.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[primaryNetworkComponent]: #primarynetworkcomponent
#### [primaryNetworkComponent]
A guest's primary public network component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component'>SoftLayer_Virtual_Guest_Network_Component </a>**  



</div>
<div class="prop-row">

-----
[privateNetworkOnlyFlag]: #privatenetworkonlyflag
#### [privateNetworkOnlyFlag]
Whether the computing instance only has access to the private network.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[projectedOverBandwidthAllocationFlag]: #projectedoverbandwidthallocationflag
#### [projectedOverBandwidthAllocationFlag]
Whether the bandwidth usage for this computing instance for the current billing cycle is projected to exceed the allocation.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[projectedPublicBandwidthUsage]: #projectedpublicbandwidthusage
#### [projectedPublicBandwidthUsage]
The projected public outbound bandwidth for this computing instance for the current billing cycle.  
<span class="type-label">Type: </span>**float**  



</div>
<div class="prop-row">

-----
[recentEvents]: #recentevents
#### [recentEvents]
Recent events that impact this computing instance.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Event'>SoftLayer_Notification_Occurrence_Event[] </a>**  



</div>
<div class="prop-row">

-----
[regionalGroup]: #regionalgroup
#### [regionalGroup]
The regional group this guest is in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Group_Regional'>SoftLayer_Location_Group_Regional </a>**  



</div>
<div class="prop-row">

-----
[regionalInternetRegistry]: #regionalinternetregistry
#### [regionalInternetRegistry]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Regional_Internet_Registry'>SoftLayer_Network_Regional_Internet_Registry </a>**  



</div>
<div class="prop-row">

-----
[reservedCapacityGroup]: #reservedcapacitygroup
#### [reservedCapacityGroup]
The reserved capacity group the guest is associated with.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_ReservedCapacityGroup'>SoftLayer_Virtual_ReservedCapacityGroup </a>**  



</div>
<div class="prop-row">

-----
[reservedCapacityGroupFlag]: #reservedcapacitygroupflag
#### [reservedCapacityGroupFlag]
Flag to indicate whether or not a guest is part of a reserved capacity group.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[reservedCapacityGroupInstance]: #reservedcapacitygroupinstance
#### [reservedCapacityGroupInstance]
The reserved capacity group instance the guest is associated with.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_ReservedCapacityGroup_Instance'>SoftLayer_Virtual_ReservedCapacityGroup_Instance </a>**  



</div>
<div class="prop-row">

-----
[scaleAssets]: #scaleassets
#### [scaleAssets]
Collection of scale assets this guest corresponds to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Asset'>SoftLayer_Scale_Asset[] </a>**  



</div>
<div class="prop-row">

-----
[scaleMember]: #scalemember
#### [scaleMember]
The scale member for this guest, if applicable.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Member_Virtual_Guest'>SoftLayer_Scale_Member_Virtual_Guest </a>**  



</div>
<div class="prop-row">

-----
[scaledFlag]: #scaledflag
#### [scaledFlag]
Whether or not this guest is a member of a scale group and was automatically created as part of a scale group action.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[securityScanRequests]: #securityscanrequests
#### [securityScanRequests]
A guest's vulnerability scan requests.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Security_Scanner_Request'>SoftLayer_Network_Security_Scanner_Request[] </a>**  



</div>
<div class="prop-row">

-----
[serverRoom]: #serverroom
#### [serverRoom]
The server room that a guest is located at. There may be more than one server room for every data center.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**  



</div>
<div class="prop-row">

-----
[softwareComponents]: #softwarecomponents
#### [softwareComponents]
A guest's installed software.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component'>SoftLayer_Software_Component[] </a>**  



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
[status]: #status
#### [status]
A computing instance's status.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Status'>SoftLayer_Virtual_Guest_Status </a>**  



</div>
<div class="prop-row">

-----
[tagReferences]: #tagreferences
#### [tagReferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Tag_Reference'>SoftLayer_Tag_Reference[] </a>**  



</div>
<div class="prop-row">

-----
[transientGuestFlag]: #transientguestflag
#### [transientGuestFlag]
Whether or not a computing instance is a Transient Instance.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[transientWebhookURI]: #transientwebhookuri
#### [transientWebhookURI]
The endpoint used to notify customers their transient guest is terminating.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Attribute'>SoftLayer_Virtual_Guest_Attribute </a>**  



</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The type of this virtual guest.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Type'>SoftLayer_Virtual_Guest_Type </a>**  



</div>
<div class="prop-row">

-----
[upgradeRequest]: #upgraderequest
#### [upgradeRequest]
A computing instance's associated upgrade request object if any.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Upgrade_Request'>SoftLayer_Product_Upgrade_Request </a>**  



</div>
<div class="prop-row">

-----
[userData]: #userdata
#### [userData]
A base64 encoded string containing custom user data for a Cloud Computing Instance order.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Attribute'>SoftLayer_Virtual_Guest_Attribute[] </a>**  



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
[virtualRack]: #virtualrack
#### [virtualRack]
The name of the bandwidth allotment that a hardware belongs too.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment </a>**  



</div>
<div class="prop-row">

-----
[virtualRackId]: #virtualrackid
#### [virtualRackId]
The id of the bandwidth allotment that a computing instance belongs too.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[virtualRackName]: #virtualrackname
#### [virtualRackName]
The name of the bandwidth allotment that a computing instance belongs too.  
<span class="type-label">Type: </span>**string**  



</div>

## Count
<div class="prop-row">

-----
[activeNetworkMonitorIncidentCount]: #activenetworkmonitorincidentcount
#### [activeNetworkMonitorIncidentCount]
A count of a virtual guest's currently active network monitoring incidents.   
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
[allowedNetworkStorageCount]: #allowednetworkstoragecount
#### [allowedNetworkStorageCount]
A count of the SoftLayer_Network_Storage objects that this SoftLayer_Virtual_Guest has access to.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[allowedNetworkStorageReplicaCount]: #allowednetworkstoragereplicacount
#### [allowedNetworkStorageReplicaCount]
A count of the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Virtual_Guest has access to.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of    
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
A count of a guests's backend network components.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[backendRouterCount]: #backendroutercount
#### [backendRouterCount]
A count of a guest's backend or private router.   
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
[blockDeviceCount]: #blockdevicecount
#### [blockDeviceCount]
A count of a computing instance's block devices. Block devices link [SoftLayer_Virtual_Disk_Image]({{<ref "reference/datatypes/SoftLayer_Virtual_Disk_Image">}}) to computing instances.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[browserConsoleAccessLogCount]: #browserconsoleaccesslogcount
#### [browserConsoleAccessLogCount]
A count of a virtual guest's browser access logs.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[evaultNetworkStorageCount]: #evaultnetworkstoragecount
#### [evaultNetworkStorageCount]
A count of a guest's associated EVault network storage service account.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[frontendNetworkComponentCount]: #frontendnetworkcomponentcount
#### [frontendNetworkComponentCount]
A count of a guest's frontend network components.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[internalTagReferenceCount]: #internaltagreferencecount
#### [internalTagReferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[monitoringUserNotificationCount]: #monitoringusernotificationcount
#### [monitoringUserNotificationCount]
A count of the monitoring notification objects for this guest. Each object links this guest instance to a user account that will be notified if monitoring on this guest object fails   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[networkComponentCount]: #networkcomponentcount
#### [networkComponentCount]
A count of a guests's network components.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[networkMonitorCount]: #networkmonitorcount
#### [networkMonitorCount]
A count of a guests's network monitors.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[networkMonitorIncidentCount]: #networkmonitorincidentcount
#### [networkMonitorIncidentCount]
A count of all of a virtual guest's network monitoring incidents.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[networkStorageCount]: #networkstoragecount
#### [networkStorageCount]
A count of a guest's associated network storage accounts.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[networkVlanCount]: #networkvlancount
#### [networkVlanCount]
A count of the network Vlans that a guest's network components are associated with.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[recentEventCount]: #recenteventcount
#### [recentEventCount]
A count of recent events that impact this computing instance.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[scaleAssetCount]: #scaleassetcount
#### [scaleAssetCount]
A count of collection of scale assets this guest corresponds to.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[securityScanRequestCount]: #securityscanrequestcount
#### [securityScanRequestCount]
A count of a guest's vulnerability scan requests.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[softwareComponentCount]: #softwarecomponentcount
#### [softwareComponentCount]
A count of a guest's installed software.   
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
[tagReferenceCount]: #tagreferencecount
#### [tagReferenceCount]
A count of    
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
A count of a base64 encoded string containing custom user data for a Cloud Computing Instance order.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


