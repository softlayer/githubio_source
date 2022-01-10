---
title: "SoftLayer_Network_Bandwidth_Version1_Allotment_Detail"
description: "The SoftLayer_Network_Bandwidth_Version1_Allotment_Detail data type contains specific information relating to a single b... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment_Detail"
---

# SoftLayer_Network_Bandwidth_Version1_Allotment_Detail
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment_Detail' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Network_Bandwidth_Version1_Allotment_Detail data type contains specific information relating to a single bandwidth allotment record. 





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
[allocationId]: #allocationid
#### [allocationId]
Allocated bandwidth.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[bandwidthAllotmentId]: #bandwidthallotmentid
#### [bandwidthAllotmentId]
Bandwidth Pool associated with this detail.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[effectiveDate]: #effectivedate
#### [effectiveDate]
Beginning this date the bandwidth allotment is active.   
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[endEffectiveDate]: #endeffectivedate
#### [endEffectiveDate]
From this date the bandwidth allotment is no longer active.   
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Internal ID associated with this allotment detail.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[serviceProviderId]: #serviceproviderid
#### [serviceProviderId]
Service Provider Id for an allotment  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[allocation]: #allocation
#### [allocation]
Allocated bandwidth.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allocation'>SoftLayer_Network_Bandwidth_Version1_Allocation </a>**  



</div>
<div class="prop-row">

-----
[bandwidthAllotment]: #bandwidthallotment
#### [bandwidthAllotment]
The parent Bandwidth Pool.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment </a>**  



</div>
<div class="prop-row">

-----
[bandwidthUsage]: #bandwidthusage
#### [bandwidthUsage]
Bandwidth used.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Usage'>SoftLayer_Network_Bandwidth_Version1_Usage[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[bandwidthUsageCount]: #bandwidthusagecount
#### [bandwidthUsageCount]
A count of bandwidth used.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


