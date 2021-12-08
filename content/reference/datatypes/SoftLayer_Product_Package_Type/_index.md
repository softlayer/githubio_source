---
title: "SoftLayer_Product_Package_Type"
description: "The [SoftLayer_Product_Package_Type]({{<ref 'reference/datatypes/SoftLayer_Product_Package_Type'>}}) object indicates th... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package_Type"
---

# SoftLayer_Product_Package_Type
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Product_Package_Type' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Package_Type' >Datatype</a></li>
    </ul>
</div>

## Description 


The [SoftLayer_Product_Package_Type]({{<ref "reference/datatypes/SoftLayer_Product_Package_Type">}}) object indicates the type for a service offering (package). The type can be used to filter packages. For example, if you are looking for the package representing virtual servers, you can filter on the type's key name of '''VIRTUAL_SERVER_INSTANCE'''. For bare metal servers by core or CPU, filter on '''BARE_METAL_CORE''' or '''BARE_METAL_CPU''', respectively. 





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
[id]: #id
#### [id]
The package type's unique identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[keyName]: #keyname
#### [keyName]
The unique key name of the package type. Use this value when filtering.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The name of the package type.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[packages]: #packages
#### [packages]
All the packages associated with the given package type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[packageCount]: #packagecount
#### [packageCount]
A count of all the packages associated with the given package type.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


