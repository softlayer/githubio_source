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
[allocationId]: #allocationid
#### [allocationId]
Allocated bandwidth.  
<span class="type-label">Type: </span>**integer**

-----
[bandwidthAllotmentId]: #bandwidthallotmentid
#### [bandwidthAllotmentId]
Bandwidth Pool associated with this detail.  
<span class="type-label">Type: </span>**integer**

-----
[effectiveDate]: #effectivedate
#### [effectiveDate]
Beginning this date the bandwidth allotment is active.   
<span class="type-label">Type: </span>**dateTime**

-----
[endEffectiveDate]: #endeffectivedate
#### [endEffectiveDate]
From this date the bandwidth allotment is no longer active.   
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
Internal ID associated with this allotment detail.  
<span class="type-label">Type: </span>**integer**

-----
[serviceProviderId]: #serviceproviderid
#### [serviceProviderId]
Service Provider Id for an allotment  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[allocation]: #allocation
#### [allocation]
Allocated bandwidth.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allocation'>SoftLayer_Network_Bandwidth_Version1_Allocation </a>**

-----
[bandwidthAllotment]: #bandwidthallotment
#### [bandwidthAllotment]
The parent Bandwidth Pool.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment </a>**

-----
[bandwidthUsage]: #bandwidthusage
#### [bandwidthUsage]
Bandwidth used.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Usage'>SoftLayer_Network_Bandwidth_Version1_Usage[] </a>**


## Count

-----
[bandwidthUsageCount]: #bandwidthusagecount
#### [bandwidthUsageCount]
A count of bandwidth used.   
<span class="type-label">Type: </span>**unsigned long**

</div>


