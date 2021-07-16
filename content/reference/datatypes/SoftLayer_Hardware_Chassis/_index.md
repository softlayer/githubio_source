---
title: "SoftLayer_Hardware_Chassis"
description: "Every piece of hardware in SoftLayer's datacenters, including customer servers, are housed in one of many hardware chass... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Chassis"
---

# SoftLayer_Hardware_Chassis
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Chassis' >Datatype</a></li>
    </ul>
</div>

## Description 
Every piece of hardware in SoftLayer's datacenters, including customer servers, are housed in one of many hardware chassis. The SoftLayer_Hardware_Chassis data type defines these chassis. 


### associatedMethods

*  [SoftLayer_Hardware::getHardwareChassis](/reference/services/SoftLayer_Hardware/getHardwareChassis )



### seeAlso

* [SoftLayer_Hardware (type)](/reference/datatypes/SoftLayer_Hardware (type) )


* [SoftLayer_Hardware_Server (type)](/reference/datatypes/SoftLayer_Hardware_Server (type) )




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
[formFactorId]: #formfactorid
#### [formFactorId]
A hardware form factor internal identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A hardware chassis' internal identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[manufacturer]: #manufacturer
#### [manufacturer]
A hardware chassis' manufacturer.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A hardware chassis' name.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[unitSize]: #unitsize
#### [unitSize]
The physical size of a hardware chassis.  Currently this relates to the 'U' size of a chassis buy default.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[version]: #version
#### [version]
A hardware chassis' revision number.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[backplaneCapacity]: #backplanecapacity
#### [backplaneCapacity]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[bayCapacity]: #baycapacity
#### [bayCapacity]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[driveCapacity]: #drivecapacity
#### [driveCapacity]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[driveControllerCapacity]: #drivecontrollercapacity
#### [driveControllerCapacity]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[gpuCapacity]: #gpucapacity
#### [gpuCapacity]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[hardwareFunction]: #hardwarefunction
#### [hardwareFunction]
A hardware's function.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Function'>SoftLayer_Hardware_Function </a>**


</div>
<div class="prop-row">

-----
[moduleCapacity]: #modulecapacity
#### [moduleCapacity]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[powerCapacity]: #powercapacity
#### [powerCapacity]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[u2Capacity]: #u2capacity
#### [u2Capacity]
  
<span class="type-label">Type: </span>**string**


</div>

## Count
</div>


