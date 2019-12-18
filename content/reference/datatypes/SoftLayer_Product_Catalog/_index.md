---
title: "SoftLayer_Product_Catalog"
description: "A Catalog is defined as a set of prices for products that SoftLayer offers for sale. These prices are organized into pac... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Catalog"
---

# SoftLayer_Product_Catalog
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Catalog' >Datatype</a></li>
    </ul>
</div>

## Description 
A Catalog is defined as a set of prices for products that SoftLayer offers for sale. These prices are organized into packages which represent the different servers and services that SoftLayer offers. 





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
[keyName]: #keyname
#### [keyName]
The Key Name of the Catalog, used for direct references  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[brands]: #brands
#### [brands]
Brands using this Catalog  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand'>SoftLayer_Brand[] </a>**

-----
[packages]: #packages
#### [packages]
Packages available in this catalog  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package[] </a>**

-----
[prices]: #prices
#### [prices]
Prices available in this catalog  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>**

-----
[products]: #products
#### [products]
Products available in catalog  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a>**


## Count

-----
[brandCount]: #brandcount
#### [brandCount]
A count of brands using this Catalog   
<span class="type-label">Type: </span>**unsigned long**


-----
[packageCount]: #packagecount
#### [packageCount]
A count of packages available in this catalog   
<span class="type-label">Type: </span>**unsigned long**


-----
[priceCount]: #pricecount
#### [priceCount]
A count of prices available in this catalog   
<span class="type-label">Type: </span>**unsigned long**


-----
[productCount]: #productcount
#### [productCount]
A count of products available in catalog   
<span class="type-label">Type: </span>**unsigned long**

</div>


