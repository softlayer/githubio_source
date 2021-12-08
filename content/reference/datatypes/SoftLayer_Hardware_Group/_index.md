---
title: "SoftLayer_Hardware_Group"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Group"
---

# SoftLayer_Hardware_Group
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Group' >Datatype</a></li>
    </ul>
</div>

## Description 








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
[domain]: #domain
#### [domain]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[hostname]: #hostname
#### [hostname]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[downlinkServers]: #downlinkservers
#### [downlinkServers]
All servers attached to a network hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**  



</div>
<div class="prop-row">

-----
[downlinkVirtualGuests]: #downlinkvirtualguests
#### [downlinkVirtualGuests]
All virtual guests attached to a network hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**  



</div>
<div class="prop-row">

-----
[downstreamNetworkHardware]: #downstreamnetworkhardware
#### [downstreamNetworkHardware]
All network hardware downstream from this hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**  



</div>
<div class="prop-row">

-----
[downstreamNetworkHardwareWithIncidents]: #downstreamnetworkhardwarewithincidents
#### [downstreamNetworkHardwareWithIncidents]
All network hardware with monitoring warnings or errors downstream from this hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**  



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
[networkMonitorAttachedDownHardware]: #networkmonitorattacheddownhardware
#### [networkMonitorAttachedDownHardware]
All servers attached downstream to a hardware that have failed monitoring  
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
[networkStatus]: #networkstatus
#### [networkStatus]
The value of a hardware's network status attribute.  
<span class="type-label">Type: </span>**string**  



</div>

## Count
<div class="prop-row">

-----
[downlinkServerCount]: #downlinkservercount
#### [downlinkServerCount]
A count of all servers attached to a network hardware.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[downlinkVirtualGuestCount]: #downlinkvirtualguestcount
#### [downlinkVirtualGuestCount]
A count of all virtual guests attached to a network hardware.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[downstreamNetworkHardwareCount]: #downstreamnetworkhardwarecount
#### [downstreamNetworkHardwareCount]
A count of all network hardware downstream from this hardware.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[downstreamNetworkHardwareWithIncidentCount]: #downstreamnetworkhardwarewithincidentcount
#### [downstreamNetworkHardwareWithIncidentCount]
A count of all network hardware with monitoring warnings or errors downstream from this hardware.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[networkMonitorAttachedDownHardwareCount]: #networkmonitorattacheddownhardwarecount
#### [networkMonitorAttachedDownHardwareCount]
A count of all servers attached downstream to a hardware that have failed monitoring   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[networkMonitorAttachedDownVirtualGuestCount]: #networkmonitorattacheddownvirtualguestcount
#### [networkMonitorAttachedDownVirtualGuestCount]
A count of virtual guests that are attached downstream to a hardware that have failed monitoring   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


