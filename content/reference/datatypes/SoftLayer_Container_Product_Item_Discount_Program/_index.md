---
title: "SoftLayer_Container_Product_Item_Discount_Program"
description: "The SoftLayer_Container_Product_Item_Discount_Program data type represents the information about a discount that is rela... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Product_Item_Discount_Program"
---

# SoftLayer_Container_Product_Item_Discount_Program
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Product_Item_Discount_Program' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_Product_Item_Discount_Program data type represents the information about a discount that is related to a specific product item. 





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
[applicableQuantity]: #applicablequantity
#### [applicableQuantity]
The number of times the item discount(s) may be applied for that order container.  At a minimum the number will be 1 and at most, it will match the quantity of the order container.  
<span class="type-label">Type: </span>**integer**

-----
[item]: #item
#### [item]
The product item that the discount applies to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**

-----
[oneTimeAmount]: #onetimeamount
#### [oneTimeAmount]
The sum of the one time fees (one time, setup and labor) of the prices of this container multiplied by the applicable quantity of this container.  
<span class="type-label">Type: </span>**decimal**

-----
[oneTimeTax]: #onetimetax
#### [oneTimeTax]
The tax amount on the one time fees (one time, setup and labor) of the prices of this container mulitiplied by the applicable quantity of this container.  
<span class="type-label">Type: </span>**decimal**

-----
[prices]: #prices
#### [prices]
The item prices that contain the amount of the discount in the recurringFee field.  There may be one or more prices.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>**

-----
[proratedOneTimeAmount]: #proratedonetimeamount
#### [proratedOneTimeAmount]
The sum of the one time fees (one time, setup and labor) of the prices of this container multiplied by the applicable quantity of this container with the proration factor applied.  
<span class="type-label">Type: </span>**decimal**

-----
[proratedOneTimeTax]: #proratedonetimetax
#### [proratedOneTimeTax]
The tax amount on the one time fees (one time, setup and labor) of the prices of this container mulitiplied by the applicable quantity of this container with the proration factor applied.  
<span class="type-label">Type: </span>**decimal**

-----
[proratedRecurringAmount]: #proratedrecurringamount
#### [proratedRecurringAmount]
The sum of the recurring fees of the prices of this container multiplied by the applicable quantity of this container with the proration factor applied.  
<span class="type-label">Type: </span>**decimal**

-----
[proratedRecurringTax]: #proratedrecurringtax
#### [proratedRecurringTax]
The tax amount on the recurring fees of the prices of this container mulitiplied by the applicable quantity of this container with the proration factor applied.  
<span class="type-label">Type: </span>**decimal**

-----
[recurringAmount]: #recurringamount
#### [recurringAmount]
The sum of the recurring fees of the prices of this container multiplied by the applicable quantity of this container.  
<span class="type-label">Type: </span>**decimal**

-----
[recurringTax]: #recurringtax
#### [recurringTax]
The tax amount on the recurring fees of the prices of this container mulitiplied by the applicable quantity of this container.  
<span class="type-label">Type: </span>**decimal**

</div>
<!-- LOCAL PROPERTY END -->

</div>


