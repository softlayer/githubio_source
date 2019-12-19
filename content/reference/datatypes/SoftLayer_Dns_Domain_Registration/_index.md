---
title: "SoftLayer_Dns_Domain_Registration"
description: "The SoftLayer_Dns_Domain_Registration data type represents a domain registration record."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_Registration"
---

# SoftLayer_Dns_Domain_Registration
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Dns_Domain_Registration' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Dns_Domain_Registration' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Dns_Domain_Registration data type represents a domain registration record. 

### External Links


* [Domain Name Registry at Wikipedia](http://en.wikipedia.org/wiki/Domain_name_registration)




### seeAlso

* [SoftLayer_Dns_Domain_Registration_Status](/reference/services/SoftLayer_Dns_Domain_Registration_Status )




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
[createDate]: #createdate
#### [createDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[domainRegistrationStatusId]: #domainregistrationstatusid
#### [domainRegistrationStatusId]
  
<span class="type-label">Type: </span>**integer**

-----
[expireDate]: #expiredate
#### [expireDate]
The date that the domain registration will expire.  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
A domain record's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[lockedFlag]: #lockedflag
#### [lockedFlag]
Indicates whether a domain is locked or unlocked.  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
A domain's name, for example "example.com".  
<span class="type-label">Type: </span>**string**

-----
[registrantVerificationStatusId]: #registrantverificationstatusid
#### [registrantVerificationStatusId]
  
<span class="type-label">Type: </span>**integer**

-----
[serviceProviderId]: #serviceproviderid
#### [serviceProviderId]
  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The SoftLayer customer account that the domain is registered to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[domainRegistrationStatus]: #domainregistrationstatus
#### [domainRegistrationStatus]
The domain registration status.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Domain_Registration_Status'>SoftLayer_Dns_Domain_Registration_Status </a>**

-----
[registrantVerificationStatus]: #registrantverificationstatus
#### [registrantVerificationStatus]
The registrant verification status.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Domain_Registration_Registrant_Verification_Status'>SoftLayer_Dns_Domain_Registration_Registrant_Verification_Status </a>**

-----
[serviceProvider]: #serviceprovider
#### [serviceProvider]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Service_Provider'>SoftLayer_Service_Provider </a>**


## Count
</div>


