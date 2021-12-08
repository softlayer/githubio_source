---
title: "SoftLayer_Container_Bandwidth_GraphOutputsExtended"
description: "SoftLayer_Container_Bandwidth_GraphOutputs models an individual bandwidth graph image and certain details about that gra... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Bandwidth_GraphOutputsExtended"
---

# SoftLayer_Container_Bandwidth_GraphOutputsExtended
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Bandwidth_GraphOutputsExtended' >Datatype</a></li>
    </ul>
</div>

## Description 


SoftLayer_Container_Bandwidth_GraphOutputs models an individual bandwidth graph image and certain details about that graph image.


### associatedMethods

*  [SoftLayer_Network_ContentDelivery_Account::getBandwidthImage](/reference/services/SoftLayer_Network_ContentDelivery_Account/getBandwidthImage )



### seeAlso

* [SoftLayer_Container_Bandwidth_GraphInputs](/reference/datatypes/SoftLayer_Container_Bandwidth_GraphInputs )




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
[graphImage]: #graphimage
#### [graphImage]
The raw PNG binary data of a bandwidth graph image.  
<span class="type-label">Type: </span>**binary data**  



</div>
<div class="prop-row">

-----
[graphTitle]: #graphtitle
#### [graphTitle]
A bandwidth graph's title.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[inBoundTotalBytes]: #inboundtotalbytes
#### [inBoundTotalBytes]
The amount of inbound traffic reported on a bandwidth graph image.  
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[maxEndDate]: #maxenddate
#### [maxEndDate]
The ending date of the data represented in a bandwidth graph.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[minStartDate]: #minstartdate
#### [minStartDate]
The beginning date of the data represented in a bandwidth graph.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[outBoundTotalBytes]: #outboundtotalbytes
#### [outBoundTotalBytes]
The amount of outbound traffic reported on a bandwidth graph image.  
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


