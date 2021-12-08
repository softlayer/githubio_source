---
title: "SoftLayer_Network_Pod"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Pod"
---

# SoftLayer_Network_Pod
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Pod' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Pod' >Datatype</a></li>
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
[backendRouterId]: #backendrouterid
#### [backendRouterId]
Identifier for this Pod's Backend Customer Router (BCR)  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[backendRouterName]: #backendroutername
#### [backendRouterName]
Host name of Pod's Backend Customer Router (BCR), e.g. bcr01a.dal09  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[capabilities]: #capabilities
#### [capabilities]
Property providing a means to filter Pods based on available capabitilies. See [SoftLayer_Network_Pod::getAllObjects]({{<ref "reference/services/SoftLayer_Network_Pod/getAllObjects">}}) to filter for Pods with specific capabilities. See [SoftLayer_Network_Pod::getCapabilities]({{<ref "reference/services/SoftLayer_Network_Pod/getCapabilities">}}) to retrieve capabilities of a specific Pod.   
<span class="type-label">Type: </span>**array of strings**  



</div>
<div class="prop-row">

-----
[datacenterId]: #datacenterid
#### [datacenterId]
Identifier for the Data Center the Pod resides within  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[datacenterLongName]: #datacenterlongname
#### [datacenterLongName]
Long form name of the data center in which this Pod resides, e.g. Dallas 9  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[datacenterName]: #datacentername
#### [datacenterName]
Name of data center in which this Pod resides, e.g. dal09  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[frontendRouterId]: #frontendrouterid
#### [frontendRouterId]
(optional) Identifier for this Pod's Frontend Customer Router (FCR)  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[frontendRouterName]: #frontendroutername
#### [frontendRouterName]
(optional) Host name of Pod's Frontend Customer Router (FCR), e.g. fcr01a.dal09  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The unique name of the Pod. See [SoftLayer_Network_Pod]({{<ref "reference/datatypes/SoftLayer_Network_Pod">}}) for details of the name's construction.   
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


