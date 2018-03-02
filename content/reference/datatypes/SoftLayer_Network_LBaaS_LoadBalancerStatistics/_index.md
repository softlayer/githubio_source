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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#connectionRate" name=connectionRate>connectionRate</a></span>
            <div class='views-field-body'>Number of connections seen at the </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#dataProcessedByMonth" name=dataProcessedByMonth>dataProcessedByMonth</a></span>
            <div class='views-field-body'>Data processed by month is the total of bin and bout </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#numberOfMembersDown" name=numberOfMembersDown>numberOfMembersDown</a></span>
            <div class='views-field-body'>Number of members in DOWN health state </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#numberOfMembersUp" name=numberOfMembersUp>numberOfMembersUp</a></span>
            <div class='views-field-body'>Number of members in UP health state </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#throughput" name=throughput>throughput</a></span>
            <div class='views-field-body'>Throughput measures the total number of bits </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>float</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#totalConnections" name=totalConnections>totalConnections</a></span>
            <div class='views-field-body'>Number of total active established connections </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
    </div>


