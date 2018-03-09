---
title: "SoftLayer_Network_LBaaS_LoadBalancerHealthMonitorConfiguration"
description: "SoftLayer_Network_LBaaS_LoadBalancerHealthMonitorConfiguration specifies the check method to be used for health monitori... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_LoadBalancerHealthMonitorConfiguration"
---

# SoftLayer_Network_LBaaS_LoadBalancerHealthMonitorConfiguration
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancerHealthMonitorConfiguration' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Network_LBaaS_LoadBalancerHealthMonitorConfiguration specifies the check method to be used for health monitoring backend members. 





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
            <span class='views-field-title'>
                <a href="#backendPort" name=backendPort>backendPort</a>
            </span>
            <div class='views-field-body'>Backends port </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#backendProtocol" name=backendProtocol>backendProtocol</a>
            </span>
            <div class='views-field-body'><<EOT </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#healthMonitorUuid" name=healthMonitorUuid>healthMonitorUuid</a>
            </span>
            <div class='views-field-body'>Health Monitor UUID, required for update only </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#interval" name=interval>interval</a>
            </span>
            <div class='views-field-body'>Interval in seconds to perform </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#maxRetries" name=maxRetries>maxRetries</a>
            </span>
            <div class='views-field-body'><<EOT </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#timeout" name=timeout>timeout</a>
            </span>
            <div class='views-field-body'>Health check methods timeout in </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#urlPath" name=urlPath>urlPath</a>
            </span>
            <div class='views-field-body'>If monitor is "HTTP", this specifies URL path </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
    </div>


