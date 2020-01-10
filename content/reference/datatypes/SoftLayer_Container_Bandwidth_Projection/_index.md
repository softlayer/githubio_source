---
title: "SoftLayer_Container_Bandwidth_Projection"
description: "SoftLayer_Container_Bandwidth_Projection models projected bandwidth use over a time range."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Bandwidth_Projection"
---

# SoftLayer_Container_Bandwidth_Projection
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Bandwidth_Projection' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Container_Bandwidth_Projection models projected bandwidth use over a time range.


### associatedMethods

*  [SoftLayer_Bandwidth_Manager::getBandwidthList](/reference/services/SoftLayer_Bandwidth_Manager/getBandwidthList )





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
[allowedUsage]: #allowedusage
#### [allowedUsage]
Bandwidth limit for this hardware.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[estimatedUsage]: #estimatedusage
#### [estimatedUsage]
Estimated bandwidth usage so far this billing cycle.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[hardwareId]: #hardwareid
#### [hardwareId]
Hardware ID of server to monitor.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[projectedUsage]: #projectedusage
#### [projectedUsage]
Projected usage for this hardware based on previous usage this billing cycle.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[serverName]: #servername
#### [serverName]
the text name of the server being monitored.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[startDate]: #startdate
#### [startDate]
The minimum date included in this list.  
<span class="type-label">Type: </span>**dateTime**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


