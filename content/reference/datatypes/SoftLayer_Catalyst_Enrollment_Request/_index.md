---
title: "SoftLayer_Catalyst_Enrollment_Request"
description: "Contains user information for Catalyst self-enrollment."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Catalyst"
classes:
    - "SoftLayer_Catalyst_Enrollment_Request"
---

# SoftLayer_Catalyst_Enrollment_Request
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Catalyst_Enrollment_Request' >Datatype</a></li>
    </ul>
</div>

## Description 
Contains user information for Catalyst self-enrollment. 





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
[address1]: #address1
#### [address1]
Applicant's address  
<span class="type-label">Type: </span>**string**

-----
[address2]: #address2
#### [address2]
Additional field for extended address  
<span class="type-label">Type: </span>**string**

-----
[affiliateId]: #affiliateid
#### [affiliateId]
Id of the affiliate who referred applicant's  
<span class="type-label">Type: </span>**integer**

-----
[agreementCompleteFlag]: #agreementcompleteflag
#### [agreementCompleteFlag]
  
<span class="type-label">Type: </span>**boolean**

-----
[applyToGepFlag]: #applytogepflag
#### [applyToGepFlag]
Determines whether or not to also apply to the GEP program  
<span class="type-label">Type: </span>**boolean**

-----
[cardAccountNumber]: #cardaccountnumber
#### [cardAccountNumber]
  
<span class="type-label">Type: </span>**string**

-----
[cardExpirationMonth]: #cardexpirationmonth
#### [cardExpirationMonth]
  
<span class="type-label">Type: </span>**string**

-----
[cardExpirationYear]: #cardexpirationyear
#### [cardExpirationYear]
  
<span class="type-label">Type: </span>**string**

-----
[cardType]: #cardtype
#### [cardType]
  
<span class="type-label">Type: </span>**string**

-----
[cardVerificationNumber]: #cardverificationnumber
#### [cardVerificationNumber]
  
<span class="type-label">Type: </span>**string**

-----
[city]: #city
#### [city]
Applicant's city  
<span class="type-label">Type: </span>**string**

-----
[companyDescription]: #companydescription
#### [companyDescription]
Brief description of Startup's product and key differentiators  
<span class="type-label">Type: </span>**string**

-----
[companyName]: #companyname
#### [companyName]
Name of the applicant's company  
<span class="type-label">Type: </span>**string**

-----
[companyTypeId]: #companytypeid
#### [companyTypeId]
Id of the company type which best describes applicant's company  
<span class="type-label">Type: </span>**integer**

-----
[companyUrl]: #companyurl
#### [companyUrl]
URL to the Startup's site  
<span class="type-label">Type: </span>**string**

-----
[country]: #country
#### [country]
Applicant's country code  
<span class="type-label">Type: </span>**string**

-----
[currentUserChoice]: #currentuserchoice
#### [currentUserChoice]
Index of answer chosen for how many current users question  
<span class="type-label">Type: </span>**integer**

-----
[deviceFingerprintId]: #devicefingerprintid
#### [deviceFingerprintId]
Id of the fingerprint  
<span class="type-label">Type: </span>**string**

-----
[email]: #email
#### [email]
Applicant's email address  
<span class="type-label">Type: </span>**string**

-----
[firstName]: #firstname
#### [firstName]
Applicant's first name  
<span class="type-label">Type: </span>**string**

-----
[futureUserChoice]: #futureuserchoice
#### [futureUserChoice]
Index of answer chosen for how many future users question  
<span class="type-label">Type: </span>**integer**

-----
[ibmIdUsername]: #ibmidusername
#### [ibmIdUsername]
Master user's IBMId username  
<span class="type-label">Type: </span>**string**

-----
[incubatorName]: #incubatorname
#### [incubatorName]
Name of accelerator or incubator startup belongs to, if any  
<span class="type-label">Type: </span>**string**

-----
[investorName]: #investorname
#### [investorName]
Name of the investor, if any  
<span class="type-label">Type: </span>**string**

-----
[lastName]: #lastname
#### [lastName]
Applicant's last name  
<span class="type-label">Type: </span>**string**

-----
[officePhone]: #officephone
#### [officePhone]
Applicant's primary phone number  
<span class="type-label">Type: </span>**string**

-----
[overFiveYearsOldFlag]: #overfiveyearsoldflag
#### [overFiveYearsOldFlag]
Whether or not the startup has been operating for more than five years  
<span class="type-label">Type: </span>**boolean**

-----
[postalCode]: #postalcode
#### [postalCode]
Applicant's postal code  
<span class="type-label">Type: </span>**string**

-----
[referralCode]: #referralcode
#### [referralCode]
IBM referral code, if any  
<span class="type-label">Type: </span>**string**

-----
[revenueOverOneMillionFlag]: #revenueoveronemillionflag
#### [revenueOverOneMillionFlag]
Whether or not the startup has over one million in annual revenue  
<span class="type-label">Type: </span>**boolean**

-----
[skipCatalystApplicationFlag]: #skipcatalystapplicationflag
#### [skipCatalystApplicationFlag]
Determines whether or not to apply to the Catalyst program  
<span class="type-label">Type: </span>**boolean**

-----
[state]: #state
#### [state]
Applicant's state/region code  
<span class="type-label">Type: </span>**string**

-----
[vatId]: #vatid
#### [vatId]
Applicant's vatId, if one exists  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[affiliate]: #affiliate
#### [affiliate]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Catalyst_Affiliate'>SoftLayer_Catalyst_Affiliate </a>**

-----
[companyType]: #companytype
#### [companyType]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Catalyst_Company_Type'>SoftLayer_Catalyst_Company_Type </a>**


## Count
</div>


