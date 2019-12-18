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
[formFactorId]: #formfactorid
#### [formFactorId]
A hardware form factor internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
A hardware chassis' internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[manufacturer]: #manufacturer
#### [manufacturer]
A hardware chassis' manufacturer.  
<span class="type-label">Type: </span>**string**

-----
[name]: #name
#### [name]
A hardware chassis' name.  
<span class="type-label">Type: </span>**string**

-----
[unitSize]: #unitsize
#### [unitSize]
The physical size of a hardware chassis.  Currently this relates to the 'U' size of a chassis buy default.  
<span class="type-label">Type: </span>**integer**

-----
[version]: #version
#### [version]
A hardware chassis' revision number.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[backplaneCapacity]: #backplanecapacity
#### [backplaneCapacity]
  
<span class="type-label">Type: </span>**string**

-----
[bayCapacity]: #baycapacity
#### [bayCapacity]
  
<span class="type-label">Type: </span>**string**

-----
[driveCapacity]: #drivecapacity
#### [driveCapacity]
  
<span class="type-label">Type: </span>**string**

-----
[driveControllerCapacity]: #drivecontrollercapacity
#### [driveControllerCapacity]
  
<span class="type-label">Type: </span>**string**

-----
[gpuCapacity]: #gpucapacity
#### [gpuCapacity]
  
<span class="type-label">Type: </span>**string**

-----
[hardwareFunction]: #hardwarefunction
#### [hardwareFunction]
A hardware's function.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Function'>SoftLayer_Hardware_Function </a>**

-----
[moduleCapacity]: #modulecapacity
#### [moduleCapacity]
  
<span class="type-label">Type: </span>**string**

-----
[powerCapacity]: #powercapacity
#### [powerCapacity]
  
<span class="type-label">Type: </span>**string**

-----
[u2Capacity]: #u2capacity
#### [u2Capacity]
  
<span class="type-label">Type: </span>**string**


## Count
</div>


