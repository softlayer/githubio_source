---
title: "SoftLayer_Billing_Item_Cancellation_Reason"
description: "The SoftLayer_Billing_Item_Cancellation_Reason data type contains cancellation reasons."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Cancellation_Reason"
---

# SoftLayer_Billing_Item_Cancellation_Reason
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Billing_Item_Cancellation_Reason' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Reason' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Billing_Item_Cancellation_Reason data type contains cancellation reasons. 





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
[billingCancelReasonCategoryId]: #billingcancelreasoncategoryid
#### [billingCancelReasonCategoryId]
A cancel reason category internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
A reason internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[keyName]: #keyname
#### [keyName]
A standardized reason internal identifier.  
<span class="type-label">Type: </span>**string**

-----
[reason]: #reason
#### [reason]
The descriptoin of the reason  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[billingCancellationReasonCategory]: #billingcancellationreasoncategory
#### [billingCancellationReasonCategory]
An billing cancellation reason category.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Reason_Category'>SoftLayer_Billing_Item_Cancellation_Reason_Category </a>**

-----
[billingItems]: #billingitems
#### [billingItems]
The corresponding billing items having the specific cancellation reason.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**

-----
[translatedReason]: #translatedreason
#### [translatedReason]
  
<span class="type-label">Type: </span>**string**


## Count

-----
[billingItemCount]: #billingitemcount
#### [billingItemCount]
A count of the corresponding billing items having the specific cancellation reason.   
<span class="type-label">Type: </span>**unsigned long**

</div>


