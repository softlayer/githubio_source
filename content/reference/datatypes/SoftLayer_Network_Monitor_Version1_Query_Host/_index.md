---
title: "SoftLayer_Network_Monitor_Version1_Query_Host"
description: "The Monitoring_Query_Host type represents a monitoring instance.  It consists of a hardware ID to monitor, an IP address... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Monitor_Version1_Query_Host"
---

# SoftLayer_Network_Monitor_Version1_Query_Host
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host' >Datatype</a></li>
    </ul>
</div>

## Description 
The Monitoring_Query_Host type represents a monitoring instance.  It consists of a hardware ID to monitor, an IP address attached to that hardware ID, a method of monitoring, and what to do in the instance that the monitor ever fails. 


### associatedMethods

*  [SoftLayer_Network_Monitor_Version1_Query_Host::findByHardwareId](/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/findByHardwareId )





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
[arg1Value]: #arg1value
#### [arg1Value]
The argument to be used for this monitor, if necessary.  The lowest monitoring levels (like ping) ignore this setting, but higher levels like HTTP custom use it.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[guestId]: #guestid
#### [guestId]
Virtual Guest Identification Number for the guest being monitored.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[hardwareId]: #hardwareid
#### [hardwareId]
The ID of the hardware being monitored  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[hostId]: #hostid
#### [hostId]
Identification Number for the host being monitored.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The unique identifier for this object  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[ipAddress]: #ipaddress
#### [ipAddress]
The IP address to be monitored.  Must be attached to the hardware on this object  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[queryTypeId]: #querytypeid
#### [queryTypeId]
The ID of the query type to use.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[responseActionId]: #responseactionid
#### [responseActionId]
The ID of the response action to take when the monitor fails  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
The status of this monitoring instance.  Anything other than "ON" means that the monitor has been disabled  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[waitCycles]: #waitcycles
#### [waitCycles]
The number of 5-minute cycles to wait before the "responseAction" is taken.  If set to 0, the response action will be taken immediately  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
The hardware that is being monitored by this monitoring instance  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**


</div>
<div class="prop-row">

-----
[lastResult]: #lastresult
#### [lastResult]
The most recent result for this particular monitoring instance.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Result'>SoftLayer_Network_Monitor_Version1_Query_Result </a>**


</div>
<div class="prop-row">

-----
[queryType]: #querytype
#### [queryType]
The type of monitoring query that is executed when this hardware is monitored.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Type'>SoftLayer_Network_Monitor_Version1_Query_Type </a>**


</div>
<div class="prop-row">

-----
[responseAction]: #responseaction
#### [responseAction]
The action taken when a monitor fails.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_ResponseType'>SoftLayer_Network_Monitor_Version1_Query_ResponseType </a>**


</div>

## Count
</div>


