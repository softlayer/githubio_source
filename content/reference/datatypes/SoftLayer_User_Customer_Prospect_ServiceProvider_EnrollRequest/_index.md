---
title: "SoftLayer_User_Customer_Prospect_ServiceProvider_EnrollRequest"
description: "Contains user information for Service Provider Enrollment."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Prospect_ServiceProvider_EnrollRequest"
---

# SoftLayer_User_Customer_Prospect_ServiceProvider_EnrollRequest
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_User_Customer_Prospect_ServiceProvider_EnrollRequest' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_Prospect_ServiceProvider_EnrollRequest' >Datatype</a></li>
    </ul>
</div>

## Description 
Contains user information for Service Provider Enrollment. 





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
[acceptAllAgreementsFlag]: #acceptallagreementsflag
#### [acceptAllAgreementsFlag]
Flag indicating whether or not applicant has accepted all current SSP agreements.  
<span class="type-label">Type: </span>**boolean**

-----
[accountId]: #accountid
#### [accountId]
accountId of existing SoftLayer Customer  
<span class="type-label">Type: </span>**integer**

-----
[address1]: #address1
#### [address1]
Service provider address1  
<span class="type-label">Type: </span>**string**

-----
[address2]: #address2
#### [address2]
Service provider address2  
<span class="type-label">Type: </span>**string**

-----
[cardAccountNumber]: #cardaccountnumber
#### [cardAccountNumber]
Credit card account number  
<span class="type-label">Type: </span>**string**

-----
[cardExpirationMonth]: #cardexpirationmonth
#### [cardExpirationMonth]
Credit card expiration month  
<span class="type-label">Type: </span>**string**

-----
[cardExpirationYear]: #cardexpirationyear
#### [cardExpirationYear]
Credit card expiration year  
<span class="type-label">Type: </span>**string**

-----
[cardType]: #cardtype
#### [cardType]
Type of credit card being used  
<span class="type-label">Type: </span>**string**

-----
[cardVerificationNumber]: #cardverificationnumber
#### [cardVerificationNumber]
Credit card verification number  
<span class="type-label">Type: </span>**string**

-----
[city]: #city
#### [city]
Service provider city  
<span class="type-label">Type: </span>**string**

-----
[companyName]: #companyname
#### [companyName]
Service provider company name  
<span class="type-label">Type: </span>**string**

-----
[companyTypeId]: #companytypeid
#### [companyTypeId]
Id of the company type which best describes applicant's company  
<span class="type-label">Type: </span>**integer**

-----
[companyUrl]: #companyurl
#### [companyUrl]
Service provider company url  
<span class="type-label">Type: </span>**string**

-----
[contactEmail]: #contactemail
#### [contactEmail]
Service provider contact's email  
<span class="type-label">Type: </span>**string**

-----
[contactFirstName]: #contactfirstname
#### [contactFirstName]
Service provider contact's first name  
<span class="type-label">Type: </span>**string**

-----
[contactLastName]: #contactlastname
#### [contactLastName]
Service provider contact's last name  
<span class="type-label">Type: </span>**string**

-----
[contactPhone]: #contactphone
#### [contactPhone]
Service provider contact's Phone  
<span class="type-label">Type: </span>**string**

-----
[country]: #country
#### [country]
Service provider country  
<span class="type-label">Type: </span>**string**

-----
[customerProspectId]: #customerprospectid
#### [customerProspectId]
Customer Prospect id  
<span class="type-label">Type: </span>**integer**

-----
[deviceFingerprintId]: #devicefingerprintid
#### [deviceFingerprintId]
Id of the device fingerprint  
<span class="type-label">Type: </span>**string**

-----
[email]: #email
#### [email]
Service provider email  
<span class="type-label">Type: </span>**string**

-----
[existingCustomerFlag]: #existingcustomerflag
#### [existingCustomerFlag]
Indicates if customer has an existing SoftLayer account  
<span class="type-label">Type: </span>**boolean**

-----
[firstName]: #firstname
#### [firstName]
Service provider first name  
<span class="type-label">Type: </span>**string**

-----
[ibmIdUsername]: #ibmidusername
#### [ibmIdUsername]
Service provider IBMid username, if different than the email.  
<span class="type-label">Type: </span>**string**

-----
[ibmPartnerWorldId]: #ibmpartnerworldid
#### [ibmPartnerWorldId]
IBM partner world id  
<span class="type-label">Type: </span>**string**

-----
[ibmPartnerWorldMemberFlag]: #ibmpartnerworldmemberflag
#### [ibmPartnerWorldMemberFlag]
Indicates if the customer is IBM partner world member  
<span class="type-label">Type: </span>**boolean**

-----
[lastName]: #lastname
#### [lastName]
Service provider last name  
<span class="type-label">Type: </span>**string**

-----
[masterAgreementCompleteFlag]: #masteragreementcompleteflag
#### [masterAgreementCompleteFlag]
Flag indicating whether or not applicant acknowledged MSA  
<span class="type-label">Type: </span>**boolean**

-----
[officePhone]: #officephone
#### [officePhone]
Service provider office phone  
<span class="type-label">Type: </span>**string**

-----
[postalCode]: #postalcode
#### [postalCode]
Service provider postalCode  
<span class="type-label">Type: </span>**string**

-----
[serviceProviderAddendumFlag]: #serviceprovideraddendumflag
#### [serviceProviderAddendumFlag]
Flag indicating whether or not applicant acknowledged service provider addendum  
<span class="type-label">Type: </span>**boolean**

-----
[state]: #state
#### [state]
Service provider state  
<span class="type-label">Type: </span>**string**

-----
[surveyResponses]: #surveyresponses
#### [surveyResponses]
Survey responses  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Survey_Response'>SoftLayer_Survey_Response[] </a>**

-----
[vatId]: #vatid
#### [vatId]
Applicant's VAT id, if one exists  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[companyType]: #companytype
#### [companyType]
Catalyst company types.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Catalyst_Company_Type'>SoftLayer_Catalyst_Company_Type </a>**


## Count
</div>


