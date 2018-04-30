---
title: "SoftLayer_Container_Account_Internal_Ibm_Request"
description: "Contains data required to both request a new IaaS account for active IBM employees and review pending requests. Fields u... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Account_Internal_Ibm_Request"
---

# SoftLayer_Container_Account_Internal_Ibm_Request
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Account_Internal_Ibm_Request' >Datatype</a></li>
    </ul>
</div>

## Description 
Contains data required to both request a new IaaS account for active IBM employees and review pending requests. Fields used exclusively in the review process are scrubbed of user input. 


### associatedMethods

*  [SoftLayer_Account_Internal_Ibm::requestAccount](/reference/services/SoftLayer_Account_Internal_Ibm/requestAccount )
*  [SoftLayer_Account_Internal_Ibm::getAccountTypes](/reference/services/SoftLayer_Account_Internal_Ibm/getAccountTypes )





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
                <a href="#accountType" name=accountType>accountType</a>
            </span>
            <div class='views-field-body'>Purpose of the internal IBM account chosen from the list of available </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#address1" name=address1>address1</a>
            </span>
            <div class='views-field-body'>If not provided, will attempt to retrieve from BluePages </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#address2" name=address2>address2</a>
            </span>
            <div class='views-field-body'>If no address provided, will attempt to retrieve from BluePages </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#city" name=city>city</a>
            </span>
            <div class='views-field-body'>If not provided, will attempt to retrieve from BluePages </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#companyName" name=companyName>companyName</a>
            </span>
            <div class='views-field-body'>Name of the company displayed on the IaaS account </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#country" name=country>country</a>
            </span>
            <div class='views-field-body'>If not provided, will attempt to retrieve from BluePages </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#deniedFlag" name=deniedFlag>deniedFlag</a>
            </span>
            <div class='views-field-body'>True if the request has been denied by either the IaaS team or the </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#departmentCode" name=departmentCode>departmentCode</a>
            </span>
            <div class='views-field-body'>Department within the division which will be changed during cost recovery. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#departmentCountry" name=departmentCountry>departmentCountry</a>
            </span>
            <div class='views-field-body'>Country assigned to the department for cost recovery. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#divisionCode" name=divisionCode>divisionCode</a>
            </span>
            <div class='views-field-body'>Division code used for cost recovery. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#emailAddress" name=emailAddress>emailAddress</a>
            </span>
            <div class='views-field-body'>Account owner's IBM email address. Must be a discoverable email </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#firstName" name=firstName>firstName</a>
            </span>
            <div class='views-field-body'>Applicant's first name, as provided by IBM BluePages API. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#lastName" name=lastName>lastName</a>
            </span>
            <div class='views-field-body'>Applicant's last name, as provided by IBM BluePages API. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#managerApprovalStatus" name=managerApprovalStatus>managerApprovalStatus</a>
            </span>
            <div class='views-field-body'>APPROVED if the request has been approved by the first-line manager, </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#multiTenantFlag" name=multiTenantFlag>multiTenantFlag</a>
            </span>
            <div class='views-field-body'>True for accounts intended to be multi-tenant and false otherwise </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#officePhone" name=officePhone>officePhone</a>
            </span>
            <div class='views-field-body'>Account owner's primary phone number. If no phone number is available </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#paasAccountId" name=paasAccountId>paasAccountId</a>
            </span>
            <div class='views-field-body'>Bluemix PaaS 32 digit hexadecimal account id being automatically linked </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#postalCode" name=postalCode>postalCode</a>
            </span>
            <div class='views-field-body'>If not provided, will attempt to retrieve from BluePages </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#purpose" name=purpose>purpose</a>
            </span>
            <div class='views-field-body'>Stated purpose of the new account this request would create </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#securitySubjectMatterExpertEmail" name=securitySubjectMatterExpertEmail>securitySubjectMatterExpertEmail</a>
            </span>
            <div class='views-field-body'>Division's security SME's email address, if available </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#securitySubjectMatterExpertName" name=securitySubjectMatterExpertName>securitySubjectMatterExpertName</a>
            </span>
            <div class='views-field-body'>Division's security SME's name, if available </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#securitySubjectMatterExpertPhone" name=securitySubjectMatterExpertPhone>securitySubjectMatterExpertPhone</a>
            </span>
            <div class='views-field-body'>Division's security SME's phone, if available </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#state" name=state>state</a>
            </span>
            <div class='views-field-body'>If required for chosen country and not provided, will attempt </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
    </div>


