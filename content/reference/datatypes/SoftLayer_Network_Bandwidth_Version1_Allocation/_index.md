---
title: "SoftLayer_Network_Bandwidth_Version1_Allocation"
description: "The SoftLayer_Network_Bandwidth_Version1_Allocation data type contains general information relating to a single bandwidt... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allocation"
---

# SoftLayer_Network_Bandwidth_Version1_Allocation
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allocation' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Network_Bandwidth_Version1_Allocation data type contains general information relating to a single bandwidth allocation record. 





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
[amount]: #amount
#### [amount]
The amount of bandwidth allocated.  
<span class="type-label">Type: </span>**decimal**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Internal ID associated with this allocation.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[allotmentDetail]: #allotmentdetail
#### [allotmentDetail]
A bandwidth allotment detail.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment_Detail'>SoftLayer_Network_Bandwidth_Version1_Allotment_Detail </a>**  



</div>
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
Billing item associated with this hardware allocation.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Hardware'>SoftLayer_Billing_Item_Hardware </a>**  



</div>

## Count
</div>


