---
title: "SoftLayer_Account_Internal_Ibm"
description: "Processes requests by IBM employees to create an IaaS account tied to their email. Request process cannot be initiated d... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Internal_Ibm"
---
# SoftLayer_Account_Internal_Ibm
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Internal_Ibm' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Internal_Ibm' >Datatype</a></li>
    </ul>
</div>

## Description
Processes requests by IBM employees to create an IaaS account tied to their email. Request process cannot be initiated directly and must go through the Bluemix IBMer account request form. 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [getAccountTypes](/reference/services/SoftLayer_Account_Internal_Ibm/getAccountTypes)
Retrieves allowed internal IBM account categories
</div>

<div class="method-row">

#### [getAuthorizationUrl](/reference/services/SoftLayer_Account_Internal_Ibm/getAuthorizationUrl)
Gets the redirect URL for manager validation
</div>

<div class="method-row">

#### [getBmsCountryList](/reference/services/SoftLayer_Account_Internal_Ibm/getBmsCountryList)

</div>

<div class="method-row">

#### [getEmployeeAccessToken](/reference/services/SoftLayer_Account_Internal_Ibm/getEmployeeAccessToken)
Exchanges a token
</div>

<div class="method-row">

#### [getManagerPreview](/reference/services/SoftLayer_Account_Internal_Ibm/getManagerPreview)
Gets a container representing the pending request
</div>

<div class="method-row">

#### [hasExistingRequest](/reference/services/SoftLayer_Account_Internal_Ibm/hasExistingRequest)
Checks for an existing request which would block an IBMer application
</div>

<div class="method-row">

#### [managerApprove](/reference/services/SoftLayer_Account_Internal_Ibm/managerApprove)
Applies manager approval to a pending internal IBM account request
</div>

<div class="method-row">

#### [managerDeny](/reference/services/SoftLayer_Account_Internal_Ibm/managerDeny)
Applies manager denial to a pending request
</div>

<div class="method-row">

#### [requestAccount](/reference/services/SoftLayer_Account_Internal_Ibm/requestAccount)
Processes IBMer requests for new IaaS/PaaS accounts
</div>
</div>

</div>

