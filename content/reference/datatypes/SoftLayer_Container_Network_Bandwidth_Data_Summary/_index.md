---
title: "SoftLayer_Container_Network_Bandwidth_Data_Summary"
description: "SoftLayer_Container_Network_Bandwidth_Data_Summary models an interface's overall bandwidth usage during it's current bil... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_Bandwidth_Data_Summary"
---

# SoftLayer_Container_Network_Bandwidth_Data_Summary
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_Bandwidth_Data_Summary' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Container_Network_Bandwidth_Data_Summary models an interface's overall bandwidth usage during it's current billing cycle. 


### associatedMethods

*  [SoftLayer_Hardware_Server::getPublicBandwidthDataSummary](/reference/services/SoftLayer_Hardware_Server/getPublicBandwidthDataSummary )
*  [SoftLayer_Hardware_Server::getPrivateBandwidthDataSummary](/reference/services/SoftLayer_Hardware_Server/getPrivateBandwidthDataSummary )





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
[allowedUsage]: #allowedusage
#### [allowedUsage]
The amount of bandwidth a server has allocated to it in it's current billing period.  
<span class="type-label">Type: </span>**float**

-----
[estimatedUsage]: #estimatedusage
#### [estimatedUsage]
The amount of bandwidth that a server has used within it's current billing period.  
<span class="type-label">Type: </span>**float**

-----
[projectedUsage]: #projectedusage
#### [projectedUsage]
The amount of bandwidth a server is projected to use within its billing period, based on it's current usage.  
<span class="type-label">Type: </span>**float**

-----
[usageUnits]: #usageunits
#### [usageUnits]
The unit of measurement used in a bandwidth data summary.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

</div>


