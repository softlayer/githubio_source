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

## Local
-----
[accountType]: #accounttype
#### [accountType]
Purpose of the internal IBM account chosen from the list of available  
<span class="type-label">Type: </span>**string**

-----
[address1]: #address1
#### [address1]
If not provided, will attempt to retrieve from BluePages  
<span class="type-label">Type: </span>**string**

-----
[address2]: #address2
#### [address2]
If no address provided, will attempt to retrieve from BluePages  
<span class="type-label">Type: </span>**string**

-----
[city]: #city
#### [city]
If not provided, will attempt to retrieve from BluePages  
<span class="type-label">Type: </span>**string**

-----
[companyName]: #companyname
#### [companyName]
Name of the company displayed on the IaaS account  
<span class="type-label">Type: </span>**string**

-----
[country]: #country
#### [country]
If not provided, will attempt to retrieve from BluePages  
<span class="type-label">Type: </span>**string**

-----
[deniedFlag]: #deniedflag
#### [deniedFlag]
True if the request has been denied by either the IaaS team or the  
<span class="type-label">Type: </span>**boolean**

-----
[departmentCode]: #departmentcode
#### [departmentCode]
Department within the division which will be changed during cost recovery.  
<span class="type-label">Type: </span>**string**

-----
[departmentCountry]: #departmentcountry
#### [departmentCountry]
Country assigned to the department for cost recovery.  
<span class="type-label">Type: </span>**string**

-----
[divisionCode]: #divisioncode
#### [divisionCode]
Division code used for cost recovery.  
<span class="type-label">Type: </span>**string**

-----
[emailAddress]: #emailaddress
#### [emailAddress]
Account owner's IBM email address. Must be a discoverable email  
<span class="type-label">Type: </span>**string**

-----
[firstName]: #firstname
#### [firstName]
Applicant's first name, as provided by IBM BluePages API.  
<span class="type-label">Type: </span>**string**

-----
[lastName]: #lastname
#### [lastName]
Applicant's last name, as provided by IBM BluePages API.  
<span class="type-label">Type: </span>**string**

-----
[managerApprovalStatus]: #managerapprovalstatus
#### [managerApprovalStatus]
APPROVED if the request has been approved by the first-line manager,  
<span class="type-label">Type: </span>**string**

-----
[multiTenantFlag]: #multitenantflag
#### [multiTenantFlag]
True for accounts intended to be multi-tenant and false otherwise  
<span class="type-label">Type: </span>**boolean**

-----
[officePhone]: #officephone
#### [officePhone]
Account owner's primary phone number. If no phone number is available  
<span class="type-label">Type: </span>**string**

-----
[paasAccountId]: #paasaccountid
#### [paasAccountId]
Bluemix PaaS 32 digit hexadecimal account id being automatically linked  
<span class="type-label">Type: </span>**string**

-----
[postalCode]: #postalcode
#### [postalCode]
If not provided, will attempt to retrieve from BluePages  
<span class="type-label">Type: </span>**string**

-----
[purpose]: #purpose
#### [purpose]
Stated purpose of the new account this request would create  
<span class="type-label">Type: </span>**string**

-----
[securitySubjectMatterExpertEmail]: #securitysubjectmatterexpertemail
#### [securitySubjectMatterExpertEmail]
Division's security SME's email address, if available  
<span class="type-label">Type: </span>**string**

-----
[securitySubjectMatterExpertName]: #securitysubjectmatterexpertname
#### [securitySubjectMatterExpertName]
Division's security SME's name, if available  
<span class="type-label">Type: </span>**string**

-----
[securitySubjectMatterExpertPhone]: #securitysubjectmatterexpertphone
#### [securitySubjectMatterExpertPhone]
Division's security SME's phone, if available  
<span class="type-label">Type: </span>**string**

-----
[state]: #state
#### [state]
If required for chosen country and not provided, will attempt  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

</div>


