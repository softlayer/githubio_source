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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#applicableQuantity" name=applicableQuantity>applicableQuantity</a>
            </span>
            <div class='views-field-body'>The number of times the item discount(s) may be applied for that order container.  At a minimum the number will be 1 and at most, it will match the quantity of the order container. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#item" name=item>item</a>
            </span>
            <div class='views-field-body'>The product item that the discount applies to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#oneTimeAmount" name=oneTimeAmount>oneTimeAmount</a>
            </span>
            <div class='views-field-body'>The sum of the one time fees (one time, setup and labor) of the prices of this container multiplied by the applicable quantity of this container. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#oneTimeTax" name=oneTimeTax>oneTimeTax</a>
            </span>
            <div class='views-field-body'>The tax amount on the one time fees (one time, setup and labor) of the prices of this container mulitiplied by the applicable quantity of this container. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#prices" name=prices>prices</a>
            </span>
            <div class='views-field-body'>The item prices that contain the amount of the discount in the recurringFee field.  There may be one or more prices. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#proratedOneTimeAmount" name=proratedOneTimeAmount>proratedOneTimeAmount</a>
            </span>
            <div class='views-field-body'>The sum of the one time fees (one time, setup and labor) of the prices of this container multiplied by the applicable quantity of this container with the proration factor applied. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#proratedOneTimeTax" name=proratedOneTimeTax>proratedOneTimeTax</a>
            </span>
            <div class='views-field-body'>The tax amount on the one time fees (one time, setup and labor) of the prices of this container mulitiplied by the applicable quantity of this container with the proration factor applied. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#proratedRecurringAmount" name=proratedRecurringAmount>proratedRecurringAmount</a>
            </span>
            <div class='views-field-body'>The sum of the recurring fees of the prices of this container multiplied by the applicable quantity of this container with the proration factor applied. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#proratedRecurringTax" name=proratedRecurringTax>proratedRecurringTax</a>
            </span>
            <div class='views-field-body'>The tax amount on the recurring fees of the prices of this container mulitiplied by the applicable quantity of this container with the proration factor applied. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#recurringAmount" name=recurringAmount>recurringAmount</a>
            </span>
            <div class='views-field-body'>The sum of the recurring fees of the prices of this container multiplied by the applicable quantity of this container. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#recurringTax" name=recurringTax>recurringTax</a>
            </span>
            <div class='views-field-body'>The tax amount on the recurring fees of the prices of this container mulitiplied by the applicable quantity of this container. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
            </div>
    </div>


