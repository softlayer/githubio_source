---
title: "SoftLayer_Container_Account_ProofOfConcept_Review"
description: "Full details presented to reviewers when determining whether or not to accept a proof of concept request. Note that revi... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Account_ProofOfConcept_Review"
---

# SoftLayer_Container_Account_ProofOfConcept_Review
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Review' >Datatype</a></li>
    </ul>
</div>

## Description 
Full details presented to reviewers when determining whether or not to accept a proof of concept request. Note that reviewers are internal IBM employees and reviews are not exposed to external users. 


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
                <a href="#accountType" name=accountType>accountType</a>
            </span>
            <div class='views-field-body'>Type of brand the account will use </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#costRecoveryCodes" name=costRecoveryCodes>costRecoveryCodes</a>
            </span>
            <div class='views-field-body'>Internal billing codes </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Request_CostRecovery'>SoftLayer_Container_Account_ProofOfConcept_Request_CostRecovery </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#customer" name=customer>customer</a>
            </span>
            <div class='views-field-body'>Customer intended to take over billing after the proof of concept period </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Contact_Customer'>SoftLayer_Container_Account_ProofOfConcept_Contact_Customer </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#description" name=description>description</a>
            </span>
            <div class='views-field-body'>Describes the purpose and rationale of the request </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#endDate" name=endDate>endDate</a>
            </span>
            <div class='views-field-body'>Expected end date of the proof of concept period </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#fundingAmount" name=fundingAmount>fundingAmount</a>
            </span>
            <div class='views-field-body'>Dollar amount of funding requested </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#fundingType" name=fundingType>fundingType</a>
            </span>
            <div class='views-field-body'>Funding option chosen for the request </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>System id of the request </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#iotLeadName" name=iotLeadName>iotLeadName</a>
            </span>
            <div class='views-field-body'>Name of the integrated offering team lead reviewing the request </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#iotRegionName" name=iotRegionName>iotRegionName</a>
            </span>
            <div class='views-field-body'>Name of the integrated offering team region </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#managerName" name=managerName>managerName</a>
            </span>
            <div class='views-field-body'>Name of requesting IBMer's manager </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#opportunity" name=opportunity>opportunity</a>
            </span>
            <div class='views-field-body'>Internal opportunity tracking information </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Request_Opportunity'>SoftLayer_Container_Account_ProofOfConcept_Request_Opportunity </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#projectName" name=projectName>projectName</a>
            </span>
            <div class='views-field-body'>Project name chosen by the requesting IBMer </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#requester" name=requester>requester</a>
            </span>
            <div class='views-field-body'>IBMer requesting the account on behalf of a customer </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Contact_Ibmer_Requester'>SoftLayer_Container_Account_ProofOfConcept_Contact_Ibmer_Requester </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#startDate" name=startDate>startDate</a>
            </span>
            <div class='views-field-body'>Expected start date of the proof of concept period </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#technicalContact" name=technicalContact>technicalContact</a>
            </span>
            <div class='views-field-body'>Additional IBMer responsible for configuring the cloud capabilities </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Contact_Ibmer_Technical'>SoftLayer_Container_Account_ProofOfConcept_Contact_Ibmer_Technical </a></p>
            </div>
        </div>
            </div>
    </div>


