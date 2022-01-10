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
[algorithm]: #algorithm
#### [algorithm]
The algorithm to use when aggregating and comparing. Currently, the only value that is accepted is EWMA (Exponential Weighted Moving Average). EWMA is the default value if no value is given.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
When this watch was created.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[deleteFlag]: #deleteflag
#### [deleteFlag]
When set and true any edit that happens on this object, be it calling edit on this directly or setting as a child while editing a parent object, will end up being a deletion.   
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A watch's internal identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[metric]: #metric
#### [metric]
The metric to watch. Possible values: 


* host.cpu.percent - On a scale of 0 to 100, the percent CPU a guest is using.
* host.network.backend.in and host.network.frontend.in - The network bytes-per-second incoming on the interface
of either the frontend or backend network. 
* host.network.backend.out and host.network.frontend.out - The network bytes-per-second incoming on the interface
of either the frontend or backend network.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
When this watch was last modified.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[operator]: #operator
#### [operator]
The operator to use for comparison. The only two valid values are ">" and "<".   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[period]: #period
#### [period]
The number of seconds the values are aggregated for when compared to value. If values are not retrieved steadily and consecutively for the length of this period, nothing is compared.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[scalePolicyTriggerId]: #scalepolicytriggerid
#### [scalePolicyTriggerId]
The trigger this watch is on.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[value]: #value
#### [value]
The value to compare against. Although the value is a string, validation will be done on the value for restrictions (such as numeric-only) based on the metric.   
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[scalePolicyTrigger]: #scalepolicytrigger
#### [scalePolicyTrigger]
The trigger this watch is on.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Policy_Trigger_ResourceUse'>SoftLayer_Scale_Policy_Trigger_ResourceUse </a>**  



</div>

## Count
</div>


