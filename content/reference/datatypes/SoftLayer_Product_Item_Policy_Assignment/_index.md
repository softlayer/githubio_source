---
title: "SoftLayer_Product_Item_Policy_Assignment"
description: "Represents the assignment of a policy to a product. The existence of a record means that the associated product is subje... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Policy_Assignment"
---

# SoftLayer_Product_Item_Policy_Assignment
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Product_Item_Policy_Assignment' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Item_Policy_Assignment' >Datatype</a></li>
    </ul>
</div>

## Description 


Represents the assignment of a policy to a product. The existence of a record means that the associated product is subject to the terms defined in the document content of the policy. 





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
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[productId]: #productid
#### [productId]
  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[policyName]: #policyname
#### [policyName]
The name of the assigned policy.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[product]: #product
#### [product]
The [SoftLayer_Product_Item]({{<ref "reference/datatypes/SoftLayer_Product_Item">}}) for this policy assignment.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**  



</div>

## Count
</div>


