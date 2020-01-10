---
title: "SoftLayer_Billing_Info_Cycle"
description: "The SoftLayer_Billing_Info_Cycle data type models basic information concerning a SoftLayer account's previous and curren... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Info_Cycle"
---

# SoftLayer_Billing_Info_Cycle
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Info_Cycle' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Billing_Info_Cycle data type models basic information concerning a SoftLayer account's previous and current billing cycles. The information in this class is only populated for SoftLayer customers who are billed monthly. 



### seeAlso

* [SoftLayer_Billing_Info](/reference/services/SoftLayer_Billing_Info )




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
[currentCycleEndDate]: #currentcycleenddate
#### [currentCycleEndDate]
The ending date of an account's current billing cycle.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[currentCycleStartDate]: #currentcyclestartdate
#### [currentCycleStartDate]
The starting date of an account's current billing cycle.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[nextCycleStartDate]: #nextcyclestartdate
#### [nextCycleStartDate]
The start date of an account's next billing cycle.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[previousCycleEndDate]: #previouscycleenddate
#### [previousCycleEndDate]
The ending date of an account's previous billing cycle.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[previousCycleStartDate]: #previouscyclestartdate
#### [previousCycleStartDate]
The starting date of an account's previous billing cycle.  
<span class="type-label">Type: </span>**dateTime**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account that a current billing cycle is associated with.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>

## Count
</div>


