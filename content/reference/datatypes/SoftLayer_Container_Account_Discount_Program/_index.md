---
title: "SoftLayer_Container_Account_Discount_Program"
description: "SoftLayer_Container_Account_Discount_Program models a single outbound object for a graph of given data sets."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Account_Discount_Program"
---

# SoftLayer_Container_Account_Discount_Program
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Account_Discount_Program' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Container_Account_Discount_Program models a single outbound object for a graph of given data sets.


### associatedMethods

*  [SoftLayer_Account::getBandwidthImage](/reference/services/SoftLayer_Account/getBandwidthImage )





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
            <span class='views-field-title'><a href="#appliedCredit" name=appliedCredit>appliedCredit</a></span>
            <div class='views-field-body'>The credit allowance that has already been applied during the current billing cycle. If the lifetime limit has been or soon will be reached, this amount may included credit applied in previous billing cycles.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#isParticipant" name=isParticipant>isParticipant</a></span>
            <div class='views-field-body'>Flag to signify whether the account is a participant in the discount program. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#lifetimeAppliedCredit" name=lifetimeAppliedCredit>lifetimeAppliedCredit</a></span>
            <div class='views-field-body'>Credit allowance applied over the course of the entire program enrollment. For enrollments without a lifetime restriction, this property will not be populated as credit will be tracked on a purely monthly basis.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#lifetimeCredit" name=lifetimeCredit>lifetimeCredit</a></span>
            <div class='views-field-body'>Credit allowance available over the course of the entire program enrollment. If null, enrollment credit is applied on a strictly monthly basis and there is no lifetime maximum. Enrollments with non-null lifetime credit will receive the lesser of the remaining monthly credit or the remaining lifetime credit.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#lifetimeRemainingCredit" name=lifetimeRemainingCredit>lifetimeRemainingCredit</a></span>
            <div class='views-field-body'>Remaining credit allowance available over the remaining duration of the program enrollment. If null, enrollment credit is applied on a strictly monthly basis and there is no lifetime maximum. Enrollments with non-null remaining lifetime credit will receive the lesser of the remaining monthly credit or the remaining lifetime credit.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#maximumActiveOrders" name=maximumActiveOrders>maximumActiveOrders</a></span>
            <div class='views-field-body'>Maximum number of orders the enrolled account is allowed to have open at one time. If null, then the Flexible Credit Program does not impose an order limit.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#monthlyCredit" name=monthlyCredit>monthlyCredit</a></span>
            <div class='views-field-body'>The monthly credit allowance that is available at the beginning of the billing cycle. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#postTaxRemainingCredit" name=postTaxRemainingCredit>postTaxRemainingCredit</a></span>
            <div class='views-field-body'>DEPRECATED: Taxes are calculated in real time and discount amounts are shown pre-tax in all cases. Tax values in the SoftLayer_Container_Account_Discount_Program container are now populated with the related pre-tax values.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#programEndDate" name=programEndDate>programEndDate</a></span>
            <div class='views-field-body'>The date at which the program expires in MM/DD/YYYY format. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#programName" name=programName>programName</a></span>
            <div class='views-field-body'>Name of the Flexible Credit Program the account is enrolled in. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#remainingCredit" name=remainingCredit>remainingCredit</a></span>
            <div class='views-field-body'>The credit allowance that is available during the current billing cycle. If the lifetime limit has been or soon will be reached, this amount may be reduced by credit applied in previous billing cycles.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#remainingCreditTax" name=remainingCreditTax>remainingCreditTax</a></span>
            <div class='views-field-body'>DEPRECATED: Taxes are calculated in real time and discount amounts are shown pre-tax in all cases. Tax values in the SoftLayer_Container_Account_Discount_Program container are now populated with the related pre-tax values.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
            </div>
    </div>


