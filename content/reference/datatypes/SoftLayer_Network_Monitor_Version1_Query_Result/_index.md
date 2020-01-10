---
title: "SoftLayer_Network_Monitor_Version1_Query_Result"
description: "The monitoring result object is used to show the status of the actions taken by the monitoring system. 

In general, onl... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Monitor_Version1_Query_Result"
---

# SoftLayer_Network_Monitor_Version1_Query_Result
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Result' >Datatype</a></li>
    </ul>
</div>

## Description 
The monitoring result object is used to show the status of the actions taken by the monitoring system. 

In general, only the responseStatus variable is needed, as it holds the information on the status of the service. 





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
[finishTime]: #finishtime
#### [finishTime]
The timestamp of when this monitor was co  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[responseStatus]: #responsestatus
#### [responseStatus]
The response status for this server.  The response status meanings are: 0:  Down/Critical: Server is down and/or has passed the critical response threshold (extremely long ping response, abnormal behavior, etc.) 1:  Warning - Server may be recovering from a previous down state, or may have taken too long to respond 2:  Up 3:  Not used 4:  Unknown - An unknown error has occurred.  If the problem persists, contact support. 5:  Unknown - An unknown error has occurred.  If the problem persists, contact support.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[responseTime]: #responsetime
#### [responseTime]
The length of time it took the server to respond  
<span class="type-label">Type: </span>**float**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[queryHost]: #queryhost
#### [queryHost]
References the queryHost that this response relates to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host'>SoftLayer_Network_Monitor_Version1_Query_Host </a>**


</div>

## Count
</div>


