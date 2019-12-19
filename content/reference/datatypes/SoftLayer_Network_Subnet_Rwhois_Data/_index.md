---
title: "SoftLayer_Network_Subnet_Rwhois_Data"
description: "Every SoftLayer customer account has contact information associated with it for reverse WHOIS purposes. An account's RWH... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Rwhois_Data"
---

# SoftLayer_Network_Subnet_Rwhois_Data
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Subnet_Rwhois_Data' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Subnet_Rwhois_Data' >Datatype</a></li>
    </ul>
</div>

## Description 
Every SoftLayer customer account has contact information associated with it for reverse WHOIS purposes. An account's RWHOIS data, modeled by the SoftLayer_Network_Subnet_Rwhois_Data data type, is used by SoftLayer's reverse WHOIS server as well as for SWIP transactions. SoftLayer's reverse WHOIS servers respond to WHOIS queries for IP addresses belonging to a customer's servers, returning this RWHOIS data. 

A SoftLayer customer's RWHOIS data may not necessarily match their account or portal users' contact information. 

### External Links


* [WHOIS at Wikipedia](http://en.wikipedia.org/wiki/WHOIS)


* [ARIN WHOIS Database Search at arin.net](http://www.arin.net/whois/)



### associatedMethods

*  [SoftLayer_Network_Storage::getObject](/reference/services/SoftLayer_Network_Storage/getObject )
*  [SoftLayer_Account::getRwhoisData](/reference/services/SoftLayer_Account/getRwhoisData )



### seeAlso

* [SoftLayer_Account](/reference/services/SoftLayer_Account )


* [SoftLayer_Network_Subnet_Swip_Transaction](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction )




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
[abuseEmail]: #abuseemail
#### [abuseEmail]
An email address associated with an account's RWHOIS data that is responsible for responding to network abuse queries about malicious traffic coming from your servers' IP addresses.  
<span class="type-label">Type: </span>**string**

-----
[accountId]: #accountid
#### [accountId]
An account's RWHOIS data's associated account identifier.  
<span class="type-label">Type: </span>**integer**

-----
[address1]: #address1
#### [address1]
The first line of the mailing address associated with an account's RWHOIS data.  
<span class="type-label">Type: </span>**string**

-----
[address2]: #address2
#### [address2]
The second line of the mailing address associated with an account's RWHOIS data.  
<span class="type-label">Type: </span>**string**

-----
[city]: #city
#### [city]
The city of the mailing address associated with an account's RWHOIS data.  
<span class="type-label">Type: </span>**string**

-----
[companyName]: #companyname
#### [companyName]
The company name associated with an account's RWHOIS data.  
<span class="type-label">Type: </span>**string**

-----
[country]: #country
#### [country]
A two-letter abbreviation of the country of the mailing address associated with an account's RWHOIS data.  
<span class="type-label">Type: </span>**string**

-----
[createDate]: #createdate
#### [createDate]
The date an account's RWHOIS data was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[firstName]: #firstname
#### [firstName]
The first name associated with an account's RWHOIS data.  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
An account's RWHOIS data's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[lastName]: #lastname
#### [lastName]
The last name associated with an account's RWHOIS data.  
<span class="type-label">Type: </span>**string**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date an account's RWHOIS data was last modified.  
<span class="type-label">Type: </span>**dateTime**

-----
[postalCode]: #postalcode
#### [postalCode]
The postal code of the mailing address associated with an account's RWHOIS data.  
<span class="type-label">Type: </span>**string**

-----
[privateResidenceFlag]: #privateresidenceflag
#### [privateResidenceFlag]
Whether an account's RWHOIS data refers to a private residence or not.  
<span class="type-label">Type: </span>**boolean**

-----
[state]: #state
#### [state]
A two-letter abbreviation of the state of the mailing address associated with an account's RWHOIS data. If an account does not reside in a province then this is typically blank.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The SoftLayer customer account associated with this reverse WHOIS data.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


## Count
</div>


