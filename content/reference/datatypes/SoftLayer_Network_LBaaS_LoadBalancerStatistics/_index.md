---
title: "SoftLayer_Network_LBaaS_LoadBalancerStatistics"
description: "SoftLayer_Network_LBaaS_LoadBalancerStatistics is a collection of metrics retrieved from a load balancer instance. The a... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_LoadBalancerStatistics"
---

# SoftLayer_Network_LBaaS_LoadBalancerStatistics
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancerStatistics' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Network_LBaaS_LoadBalancerStatistics is a collection of metrics retrieved from a load balancer instance. The available metrics are: <ul> <li>NUmber of members up</li> <li>Number of members down</li> <li>Total number of active connections</li> <li>Throughput</li> <li>Data processed by month</li> <li>Connection rate</li> </ul> 





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
[connectionRate]: #connectionrate
#### [connectionRate]
Number of connections seen at the  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[dataProcessedByMonth]: #dataprocessedbymonth
#### [dataProcessedByMonth]
Data processed by month is the total of bin and bout  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[numberOfMembersDown]: #numberofmembersdown
#### [numberOfMembersDown]
Number of members in DOWN health state  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[numberOfMembersUp]: #numberofmembersup
#### [numberOfMembersUp]
Number of members in UP health state  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[throughput]: #throughput
#### [throughput]
Throughput measures the total number of bits  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[totalConnections]: #totalconnections
#### [totalConnections]
Number of total active established connections  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


