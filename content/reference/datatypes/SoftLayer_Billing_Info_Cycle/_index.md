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

* [SoftLayer_Billing_Info](/reference/datatypes/SoftLayer_Billing_Info )




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
                <a href="#currentCycleEndDate" name=currentCycleEndDate>currentCycleEndDate</a>
            </span>
            <div class='views-field-body'>The ending date of an account's current billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#currentCycleStartDate" name=currentCycleStartDate>currentCycleStartDate</a>
            </span>
            <div class='views-field-body'>The starting date of an account's current billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#nextCycleStartDate" name=nextCycleStartDate>nextCycleStartDate</a>
            </span>
            <div class='views-field-body'>The start date of an account's next billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#previousCycleEndDate" name=previousCycleEndDate>previousCycleEndDate</a>
            </span>
            <div class='views-field-body'>The ending date of an account's previous billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#previousCycleStartDate" name=previousCycleStartDate>previousCycleStartDate</a>
            </span>
            <div class='views-field-body'>The starting date of an account's previous billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#account" name=account>account</a>
            </span>
            <div class='views-field-body'>The account that a current billing cycle is associated with. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


