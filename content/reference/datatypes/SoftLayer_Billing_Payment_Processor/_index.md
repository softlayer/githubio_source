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
[description]: #description
#### [description]
  
<span class="type-label">Type: </span>**string**

-----
[name]: #name
#### [name]
  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[brandAssignments]: #brandassignments
#### [brandAssignments]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand_Payment_Processor'>SoftLayer_Brand_Payment_Processor[] </a>**

-----
[ownerAccount]: #owneraccount
#### [ownerAccount]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[paymentMethods]: #paymentmethods
#### [paymentMethods]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Payment_Processor_Method'>SoftLayer_Billing_Payment_Processor_Method[] </a>**

-----
[type]: #type
#### [type]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Payment_Processor_Type'>SoftLayer_Billing_Payment_Processor_Type </a>**


## Count

-----
[brandAssignmentCount]: #brandassignmentcount
#### [brandAssignmentCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[paymentMethodCount]: #paymentmethodcount
#### [paymentMethodCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>


