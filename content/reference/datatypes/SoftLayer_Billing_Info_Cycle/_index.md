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
[currentCycleEndDate]: #currentcycleenddate
#### [currentCycleEndDate]
The ending date of an account's current billing cycle.  
<span class="type-label">Type: </span>**dateTime**

-----
[currentCycleStartDate]: #currentcyclestartdate
#### [currentCycleStartDate]
The starting date of an account's current billing cycle.  
<span class="type-label">Type: </span>**dateTime**

-----
[nextCycleStartDate]: #nextcyclestartdate
#### [nextCycleStartDate]
The start date of an account's next billing cycle.  
<span class="type-label">Type: </span>**dateTime**

-----
[previousCycleEndDate]: #previouscycleenddate
#### [previousCycleEndDate]
The ending date of an account's previous billing cycle.  
<span class="type-label">Type: </span>**dateTime**

-----
[previousCycleStartDate]: #previouscyclestartdate
#### [previousCycleStartDate]
The starting date of an account's previous billing cycle.  
<span class="type-label">Type: </span>**dateTime**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The account that a current billing cycle is associated with.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


## Count
</div>


