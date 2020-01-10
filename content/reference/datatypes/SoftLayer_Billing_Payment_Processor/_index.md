---
title: "SoftLayer_Billing_Payment_Processor"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Payment_Processor"
---

# SoftLayer_Billing_Payment_Processor
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Payment_Processor' >Datatype</a></li>
    </ul>
</div>

## Description 






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
[description]: #description
#### [description]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[brandAssignments]: #brandassignments
#### [brandAssignments]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand_Payment_Processor'>SoftLayer_Brand_Payment_Processor[] </a>**


</div>
<div class="prop-row">

-----
[ownerAccount]: #owneraccount
#### [ownerAccount]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[paymentMethods]: #paymentmethods
#### [paymentMethods]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Payment_Processor_Method'>SoftLayer_Billing_Payment_Processor_Method[] </a>**


</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Payment_Processor_Type'>SoftLayer_Billing_Payment_Processor_Type </a>**


</div>

## Count
<div class="prop-row">

-----
[brandAssignmentCount]: #brandassignmentcount
#### [brandAssignmentCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[paymentMethodCount]: #paymentmethodcount
#### [paymentMethodCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


