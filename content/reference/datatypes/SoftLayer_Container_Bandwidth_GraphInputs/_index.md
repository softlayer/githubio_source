---
title: "SoftLayer_Container_Bandwidth_GraphInputs"
description: "SoftLayer_Container_Bandwidth_GraphInputs models a single inbound object for a given bandwidth graph."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Bandwidth_GraphInputs"
---

# SoftLayer_Container_Bandwidth_GraphInputs
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Bandwidth_GraphInputs' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Container_Bandwidth_GraphInputs models a single inbound object for a given bandwidth graph.



### seeAlso

* [SoftLayer_Container_Bandwidth_GraphOutputs](/reference/datatypes/SoftLayer_Container_Bandwidth_GraphOutputs )




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
[endDate]: #enddate
#### [endDate]
This is a unix timestamp that represents the stop date/time for a graph.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[networkInterfaceId]: #networkinterfaceid
#### [networkInterfaceId]
The front-end or back-end network uplink interface associated with this server.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[pod]: #pod
#### [pod]
*  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[serverName]: #servername
#### [serverName]
This is a human readable name for the server or rack being graphed.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[startDate]: #startdate
#### [startDate]
This is a unix timestamp that represents the begin date/time for a graph.  
<span class="type-label">Type: </span>**dateTime**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


