---
title: "SoftLayer_Container_Tax_Cache_Item"
description: "This represents one order item in a tax calculation."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Tax_Cache_Item"
---

# SoftLayer_Container_Tax_Cache_Item
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Tax_Cache_Item' >Datatype</a></li>
    </ul>
</div>

## Description 


This represents one order item in a tax calculation. 





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
[categoryCode]: #categorycode
#### [categoryCode]
The category code for the referenced product.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[containerHash]: #containerhash
#### [containerHash]
This hash will match to the hash on an order container.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[itemPriceId]: #itempriceid
#### [itemPriceId]
The reference to the price for this order item.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[taxRates]: #taxrates
#### [taxRates]
This is the container containing the individual tax rates.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Tax_Rates'>SoftLayer_Container_Tax_Rates </a>**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


