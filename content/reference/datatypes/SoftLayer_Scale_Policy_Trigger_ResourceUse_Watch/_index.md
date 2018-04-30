---
title: "SoftLayer_Scale_Policy_Trigger_ResourceUse_Watch"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Policy_Trigger_ResourceUse_Watch"
---

# SoftLayer_Scale_Policy_Trigger_ResourceUse_Watch
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Scale_Policy_Trigger_ResourceUse_Watch' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Scale_Policy_Trigger_ResourceUse_Watch' >Datatype</a></li>
    </ul>
</div>

## Description 






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
                <a href="#algorithm" name=algorithm>algorithm</a>
            </span>
            <div class='views-field-body'>The algorithm to use when aggregating and comparing. Currently, the only value that is accepted is EWMA (Exponential Weighted Moving Average). EWMA is the default value if no value is given.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'>When this watch was created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#deleteFlag" name=deleteFlag>deleteFlag</a>
            </span>
            <div class='views-field-body'>When set and true any edit that happens on this object, be it calling edit on this directly or setting as a child while editing a parent object, will end up being a deletion.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>A watch's internal identifier. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#metric" name=metric>metric</a>
            </span>
            <div class='views-field-body'>The metric to watch. Possible values: 


* host.cpu.percent - On a scale of 0 to 100, the percent CPU a guest is using.
* host.network.backend.in and host.network.frontend.in - The network bytes-per-second incoming on the interface
of either the frontend or backend network. 
* host.network.backend.out and host.network.frontend.out - The network bytes-per-second incoming on the interface
of either the frontend or backend network.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'>When this watch was last modified. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#operator" name=operator>operator</a>
            </span>
            <div class='views-field-body'>The operator to use for comparison. The only two valid values are ">" and "<".  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#period" name=period>period</a>
            </span>
            <div class='views-field-body'>The number of seconds the values are aggregated for when compared to value. If values are not retrieved steadily and consecutively for the length of this period, nothing is compared.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#scalePolicyTriggerId" name=scalePolicyTriggerId>scalePolicyTriggerId</a>
            </span>
            <div class='views-field-body'>The trigger this watch is on. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#value" name=value>value</a>
            </span>
            <div class='views-field-body'>The value to compare against. Although the value is a string, validation will be done on the value for restrictions (such as numeric-only) based on the metric.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#scalePolicyTrigger" name=scalePolicyTrigger>scalePolicyTrigger</a>
            </span>
            <div class='views-field-body'>The trigger this watch is on. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Scale_Policy_Trigger_ResourceUse'>SoftLayer_Scale_Policy_Trigger_ResourceUse </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


