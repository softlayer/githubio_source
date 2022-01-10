---
title: "SoftLayer_Virtual_Host"
description: "The virtual host represents the platform on which virtual guests reside. At times a virtual host has no allocations on t... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Host"
---

# SoftLayer_Virtual_Host
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Virtual_Host' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Host' >Datatype</a></li>
    </ul>
</div>

## Description 


The virtual host represents the platform on which virtual guests reside. At times a virtual host has no allocations on the physical server, however with many modern platforms it is a virtual machine with small CPU and Memory allocations that runs in the Control Domain. 





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
A virtual host's associated account id   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date a virtual host was created.   
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
A virtual host's description.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[enabledFlag]: #enabledflag
#### [enabledFlag]
The enabled flag specifies whether a virtual host can run guests.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[hardwareId]: #hardwareid
#### [hardwareId]
A hardware device which a virtual host resides.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Unique ID for a virtual host.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a virtual host was last modified.   
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A virtual host's name.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[physicalMemoryCapacity]: #physicalmemorycapacity
#### [physicalMemoryCapacity]
The amount of memory physically available for a virtual host.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[uuid]: #uuid
#### [uuid]
Unique ID for a virtual host's record on a virtualization platform.   
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
The account which a virtual host belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[billedPerGuestFlag]: #billedperguestflag
#### [billedPerGuestFlag]
Boolean flag indicating whether this virtualization platform gets billed per guest rather than at a fixed rate.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[billedPerMemoryUsageFlag]: #billedpermemoryusageflag
#### [billedPerMemoryUsageFlag]
Boolean flag indicating whether this virtualization platform gets billed per memory usage rather than at a fixed rate.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[guests]: #guests
#### [guests]
The guests associated with a virtual host.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**  



</div>
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
The hardware record which a virtual host resides on.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Server'>SoftLayer_Hardware_Server </a>**  



</div>
<div class="prop-row">

-----
[metricTrackingObject]: #metrictrackingobject
#### [metricTrackingObject]
The metric tracking object for this virtual host.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object'>SoftLayer_Metric_Tracking_Object </a>**  



</div>
<div class="prop-row">

-----
[pciDevices]: #pcidevices
#### [pciDevices]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Host_PciDevice'>SoftLayer_Virtual_Host_PciDevice[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[guestCount]: #guestcount
#### [guestCount]
A count of the guests associated with a virtual host.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[pciDeviceCount]: #pcidevicecount
#### [pciDeviceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


