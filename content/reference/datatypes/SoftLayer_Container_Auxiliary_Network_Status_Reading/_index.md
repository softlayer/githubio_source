---
title: "SoftLayer_Container_Auxiliary_Network_Status_Reading"
description: "The SoftLayer_Container_Auxiliary_Network_Status_Reading data type contains information relating to an object being moni... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Auxiliary_Network_Status_Reading"
---

# SoftLayer_Container_Auxiliary_Network_Status_Reading
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Auxiliary_Network_Status_Reading' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_Auxiliary_Network_Status_Reading data type contains information relating to an object being monitored from outside the SoftLayer network.  It is primarily used to check the status of our edge routers from multiple locations around the world. 


### associatedMethods

*  [SoftLayer_Auxiliary_Network_Status::getObject](/reference/services/SoftLayer_Auxiliary_Network_Status/getObject )





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
[averagePing]: #averageping
#### [averagePing]
Average packet round-trip time.  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[fails]: #fails
#### [fails]
Number of failures since the target was last detected to be working properly.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[frequency]: #frequency
#### [frequency]
Monitoring frequency in minutes.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[label]: #label
#### [label]
The target babel.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[lastCheckDate]: #lastcheckdate
#### [lastCheckDate]
Last check date and time.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[lastDownDate]: #lastdowndate
#### [lastDownDate]
Date and time of the last problem detected.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[latency]: #latency
#### [latency]
The total response time in seconds calculated during the last check.  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[location]: #location
#### [location]
The monitoring location name.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[maximumPing]: #maximumping
#### [maximumPing]
Maximum packet round-trip time.  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[minimumPing]: #minimumping
#### [minimumPing]
Minimum packet round-trip time.  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[pingLoss]: #pingloss
#### [pingLoss]
Packet loss percentage.  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[startDate]: #startdate
#### [startDate]
The date monitoring first began  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[statusCode]: #statuscode
#### [statusCode]
Status Code - one of UP, Down, Test pending.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[statusMessage]: #statusmessage
#### [statusMessage]
The status message from the last effective check.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[target]: #target
#### [target]
The target object.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[targetType]: #targettype
#### [targetType]
A letter indicating the target type.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


