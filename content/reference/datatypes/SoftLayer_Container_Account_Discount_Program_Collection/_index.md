---
title: "SoftLayer_Container_Account_Discount_Program_Collection"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Account_Discount_Program_Collection"
---

# SoftLayer_Container_Account_Discount_Program_Collection
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Account_Discount_Program_Collection' >Datatype</a></li>
    </ul>
</div>

## Description 



### associatedMethods

*  [SoftLayer_Account::getFlexibleCreditProgramsInfo](/reference/services/SoftLayer_Account/getFlexibleCreditProgramsInfo )





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
                <a href="#accountLevelAppliedCredit" name=accountLevelAppliedCredit>accountLevelAppliedCredit</a>
            </span>
            <div class='views-field-body'>The amount of credit that has been used by all account level enrollments in the billing cycle.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#accountLevelLifetimeAppliedCredit" name=accountLevelLifetimeAppliedCredit>accountLevelLifetimeAppliedCredit</a>
            </span>
            <div class='views-field-body'>Account level credit allowance applied over the course of entire active program enrollments. For enrollments without a lifetime restriction, this property will not be populated as credit will be tracked on a purely monthly basis.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#accountLevelLifetimeCredit" name=accountLevelLifetimeCredit>accountLevelLifetimeCredit</a>
            </span>
            <div class='views-field-body'>The total account level credit over the course of an entire program enrollment. This value may be null, in which case the enrollment credit is applied on a monthly basis and there is no lifetime maximum.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#accountLevelLifetimeRemainingCredit" name=accountLevelLifetimeRemainingCredit>accountLevelLifetimeRemainingCredit</a>
            </span>
            <div class='views-field-body'>Remaining account level credit allowance available over the remaining duration of the program enrollments. If null, enrollment credit is applied on a strictly monthly basis and there is no lifetime maximum. Enrollments with non-null remaining lifetime credit will receive the lesser of the remaining monthly credit or the remaining lifetime credit.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#accountLevelMonthlyCredit" name=accountLevelMonthlyCredit>accountLevelMonthlyCredit</a>
            </span>
            <div class='views-field-body'>The total account level monthly credit allowance available at the beginning of a billing cycle.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#accountLevelRemainingCredit" name=accountLevelRemainingCredit>accountLevelRemainingCredit</a>
            </span>
            <div class='views-field-body'>The total account level credit allowance still available during the current billing cycle.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#enrollments" name=enrollments>enrollments</a>
            </span>
            <div class='views-field-body'>The active enrollments for this account.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_FlexibleCredit_Enrollment'>SoftLayer_FlexibleCredit_Enrollment[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#isAccountLevelParticipantFlag" name=isAccountLevelParticipantFlag>isAccountLevelParticipantFlag</a>
            </span>
            <div class='views-field-body'>Indicates whether or not the account is participating in any account level Flexible Credit programs.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#isParticipantFlag" name=isParticipantFlag>isParticipantFlag</a>
            </span>
            <div class='views-field-body'>Indicates whether or not the account is participating in any Flexible Credit programs.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#isProductSpecificParticipantFlag" name=isProductSpecificParticipantFlag>isProductSpecificParticipantFlag</a>
            </span>
            <div class='views-field-body'>Indicates whether or not the account is participating in any product specific level Flexible Credit programs.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#productSpecificAppliedCredit" name=productSpecificAppliedCredit>productSpecificAppliedCredit</a>
            </span>
            <div class='views-field-body'>The amount of credit that has been used by all product specific enrollments in the billing cycle.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#productSpecificLifetimeAppliedCredit" name=productSpecificLifetimeAppliedCredit>productSpecificLifetimeAppliedCredit</a>
            </span>
            <div class='views-field-body'>Product specific credit allowance applied over the course of entire active program enrollments. For enrollments without a lifetime restriction, this property will not be populated as credit will be tracked on a purely monthly basis.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#productSpecificLifetimeCredit" name=productSpecificLifetimeCredit>productSpecificLifetimeCredit</a>
            </span>
            <div class='views-field-body'>The total product specific credit over the course of an entire program enrollment. This value may be null, in which case the enrollment credit is applied on a monthly basis and there is no lifetime maximum.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#productSpecificLifetimeRemainingCredit" name=productSpecificLifetimeRemainingCredit>productSpecificLifetimeRemainingCredit</a>
            </span>
            <div class='views-field-body'>Remaining product specific level credit allowance available over the remaining duration of the program enrollments. If null, enrollment credit is applied on a strictly monthly basis and there is no lifetime maximum. Enrollments with non-null remaining lifetime credit will receive the lesser of the remaining monthly credit or the remaining lifetime credit.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#productSpecificMonthlyCredit" name=productSpecificMonthlyCredit>productSpecificMonthlyCredit</a>
            </span>
            <div class='views-field-body'>The total product specific monthly credit allowance available at the beginning of a billing cycle.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#productSpecificRemainingCredit" name=productSpecificRemainingCredit>productSpecificRemainingCredit</a>
            </span>
            <div class='views-field-body'>The total product specific credit allowance still available during the current billing cycle.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#totalAppliedCredit" name=totalAppliedCredit>totalAppliedCredit</a>
            </span>
            <div class='views-field-body'>The credit allowance that has already been applied during the current billing cycle from all enrollments. If the lifetime limit has been or soon will be reached, this amount may included credit applied in previous billing cycles.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#totalRemainingCredit" name=totalRemainingCredit>totalRemainingCredit</a>
            </span>
            <div class='views-field-body'>The credit allowance that is available during the current billing cycle from all enrollments. If the lifetime limit has been or soon will be reached, this amount may be reduced by credit applied in previous billing cycles.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
            </div>
    </div>


