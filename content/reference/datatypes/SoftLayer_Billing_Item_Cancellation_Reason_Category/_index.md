---
title: "SoftLayer_Billing_Item_Cancellation_Reason_Category"
description: "The SoftLayer_Billing_Item_Cancellation_Reason_Category data type contains cancellation reason categories."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Cancellation_Reason_Category"
---

# SoftLayer_Billing_Item_Cancellation_Reason_Category
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Billing_Item_Cancellation_Reason_Category' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Reason_Category' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Billing_Item_Cancellation_Reason_Category data type contains cancellation reason categories. 





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
[id]: #id
#### [id]
A category internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[name]: #name
#### [name]
The description of the category  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[billingCancellationReasons]: #billingcancellationreasons
#### [billingCancellationReasons]
The corresponding billing cancellation reasons having the specific billing cancellation reason category.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Reason'>SoftLayer_Billing_Item_Cancellation_Reason[] </a>**


## Count

-----
[billingCancellationReasonCount]: #billingcancellationreasoncount
#### [billingCancellationReasonCount]
A count of the corresponding billing cancellation reasons having the specific billing cancellation reason category.   
<span class="type-label">Type: </span>**unsigned long**

</div>


