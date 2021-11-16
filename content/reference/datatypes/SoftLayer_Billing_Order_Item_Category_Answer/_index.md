---
title: "SoftLayer_Billing_Order_Item_Category_Answer"
description: "The SoftLayer_Billing_Order_Item_Category_Answer data type represents a single answer to an item category question."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Item_Category_Answer"
---

# SoftLayer_Billing_Order_Item_Category_Answer
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Order_Item_Category_Answer' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Billing_Order_Item_Category_Answer data type represents a single answer to an item category question. 





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
[answer]: #answer
#### [answer]
The answer to the question.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date that the answer was created.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[questionId]: #questionid
#### [questionId]
The identifier for the question that the answer belongs to.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[orderItem]: #orderitem
#### [orderItem]
The billing order item that the answer is for.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item </a>**  



</div>
<div class="prop-row">

-----
[question]: #question
#### [question]
The question that is being answered.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category_Question'>SoftLayer_Product_Item_Category_Question </a>**  



</div>

## Count
</div>


