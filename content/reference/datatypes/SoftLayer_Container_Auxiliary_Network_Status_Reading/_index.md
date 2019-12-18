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
[averagePing]: #averageping
#### [averagePing]
Average packet round-trip time.  
<span class="type-label">Type: </span>**float**

-----
[fails]: #fails
#### [fails]
Number of failures since the target was last detected to be working properly.  
<span class="type-label">Type: </span>**integer**

-----
[frequency]: #frequency
#### [frequency]
Monitoring frequency in minutes.  
<span class="type-label">Type: </span>**integer**

-----
[label]: #label
#### [label]
The target babel.  
<span class="type-label">Type: </span>**string**

-----
[lastCheckDate]: #lastcheckdate
#### [lastCheckDate]
Last check date and time.  
<span class="type-label">Type: </span>**dateTime**

-----
[lastDownDate]: #lastdowndate
#### [lastDownDate]
Date and time of the last problem detected.  
<span class="type-label">Type: </span>**dateTime**

-----
[latency]: #latency
#### [latency]
The total response time in seconds calculated during the last check.  
<span class="type-label">Type: </span>**float**

-----
[location]: #location
#### [location]
The monitoring location name.  
<span class="type-label">Type: </span>**string**

-----
[maximumPing]: #maximumping
#### [maximumPing]
Maximum packet round-trip time.  
<span class="type-label">Type: </span>**float**

-----
[minimumPing]: #minimumping
#### [minimumPing]
Minimum packet round-trip time.  
<span class="type-label">Type: </span>**float**

-----
[pingLoss]: #pingloss
#### [pingLoss]
Packet loss percentage.  
<span class="type-label">Type: </span>**float**

-----
[startDate]: #startdate
#### [startDate]
The date monitoring first began  
<span class="type-label">Type: </span>**dateTime**

-----
[statusCode]: #statuscode
#### [statusCode]
Status Code - one of UP, Down, Test pending.  
<span class="type-label">Type: </span>**string**

-----
[statusMessage]: #statusmessage
#### [statusMessage]
The status message from the last effective check.  
<span class="type-label">Type: </span>**string**

-----
[target]: #target
#### [target]
The target object.  
<span class="type-label">Type: </span>**string**

-----
[targetType]: #targettype
#### [targetType]
A letter indicating the target type.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

</div>


