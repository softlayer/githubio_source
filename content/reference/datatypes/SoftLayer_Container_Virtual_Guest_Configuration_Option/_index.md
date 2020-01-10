---
title: "SoftLayer_Container_Virtual_Guest_Configuration_Option"
description: "An option found within a [SoftLayer_Container_Virtual_Guest_Configuration]({{<ref 'reference/datatypes/SoftLayer_Contain... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Virtual_Guest_Configuration_Option"
---

# SoftLayer_Container_Virtual_Guest_Configuration_Option
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Virtual_Guest_Configuration_Option' >Datatype</a></li>
    </ul>
</div>

## Description 
An option found within a [SoftLayer_Container_Virtual_Guest_Configuration]({{<ref "reference/datatypes/SoftLayer_Container_Virtual_Guest_Configuration">}}) structure. 





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
[flavor]: #flavor
#### [flavor]

Provides a description of a pre-defined configuration with monthly and hourly costs.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Preset'>SoftLayer_Product_Package_Preset </a>**


</div>
<div class="prop-row">

-----
[itemPrice]: #itemprice
#### [itemPrice]

Provides hourly and monthly costs (if either are applicable), and a description of the option.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price </a>**


</div>
<div class="prop-row">

-----
[template]: #template
#### [template]

Provides a fragment of the request with the properties and values that must be sent when creating a computing instance with the option.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


