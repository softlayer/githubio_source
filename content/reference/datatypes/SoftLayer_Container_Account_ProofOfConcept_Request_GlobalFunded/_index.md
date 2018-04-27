---
title: "SoftLayer_Container_Account_ProofOfConcept_Request_GlobalFunded"
description: "Proof of concept request using the global funding model. Note that proof of concept account request are available only t... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Account_ProofOfConcept_Request_GlobalFunded"
---

# SoftLayer_Container_Account_ProofOfConcept_Request_GlobalFunded
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Request_GlobalFunded' >Datatype</a></li>
    </ul>
</div>

## Description 
Proof of concept request using the global funding model. Note that proof of concept account request are available only to internal IBM employees. 


### associatedMethods

*  [SoftLayer_Account_ProofOfConcept::requestAccount](/reference/services/SoftLayer_Account_ProofOfConcept/requestAccount )





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
                <a href="#amount" name=amount>amount</a>
            </span>
            <div class='views-field-body'>Dollar amount of funding requested for the proof of concept period </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#customer" name=customer>customer</a>
            </span>
            <div class='views-field-body'>Customer intended to take over ownership and and billing of the account </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Contact_Customer'>SoftLayer_Container_Account_ProofOfConcept_Contact_Customer </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#description" name=description>description</a>
            </span>
            <div class='views-field-body'>Explanation of the purpose of the proof of concept request </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#endDate" name=endDate>endDate</a>
            </span>
            <div class='views-field-body'>End date for the proof of concept period </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#opportunity" name=opportunity>opportunity</a>
            </span>
            <div class='views-field-body'>Internal opportunity system details </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Request_Opportunity'>SoftLayer_Container_Account_ProofOfConcept_Request_Opportunity </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#projectName" name=projectName>projectName</a>
            </span>
            <div class='views-field-body'>Name of the project or company and will become the account companyName </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#regionKeyName" name=regionKeyName>regionKeyName</a>
            </span>
            <div class='views-field-body'>IBM region responsible for overseeing the proof of concept account </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#requester" name=requester>requester</a>
            </span>
            <div class='views-field-body'>IBMer requesting the proof of concept account </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Contact_Ibmer_Requester'>SoftLayer_Container_Account_ProofOfConcept_Contact_Ibmer_Requester </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#startDate" name=startDate>startDate</a>
            </span>
            <div class='views-field-body'>Start date for the proof of concept period </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#technicalContact" name=technicalContact>technicalContact</a>
            </span>
            <div class='views-field-body'>IBMer assisting with technical aspects of account configuration </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Contact_Ibmer_Technical'>SoftLayer_Container_Account_ProofOfConcept_Contact_Ibmer_Technical </a></p>
            </div>
        </div>
            </div>
    </div>


