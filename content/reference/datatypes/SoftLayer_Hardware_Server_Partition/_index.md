---
title: "SoftLayer_Hardware_Server_Partition"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server_Partition"
---

# SoftLayer_Hardware_Server_Partition
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Server_Partition' >Datatype</a></li>
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
[hardwareId]: #hardwareid
#### [hardwareId]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[hostname]: #hostname
#### [hostname]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[macAddress]: #macaddress
#### [macAddress]
  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**


</div>
<div class="prop-row">

-----
[networkComponentAttributes]: #networkcomponentattributes
#### [networkComponentAttributes]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Server_Partition_Network_Attribute'>SoftLayer_Hardware_Server_Partition_Network_Attribute[] </a>**


</div>
<div class="prop-row">

-----
[networkComponents]: #networkcomponents
#### [networkComponents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component[] </a>**


</div>

## Count
<div class="prop-row">

-----
[networkComponentAttributeCount]: #networkcomponentattributecount
#### [networkComponentAttributeCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkComponentCount]: #networkcomponentcount
#### [networkComponentCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


