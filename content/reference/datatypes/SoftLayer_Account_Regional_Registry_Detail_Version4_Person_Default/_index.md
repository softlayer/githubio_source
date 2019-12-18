---
title: "SoftLayer_Account_Regional_Registry_Detail_Version4_Person_Default"
description: "The SoftLayer_Account_Regional_Registry_Detail_Version4_Person_Default data type contains general information relating t... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Regional_Registry_Detail_Version4_Person_Default"
---

# SoftLayer_Account_Regional_Registry_Detail_Version4_Person_Default
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Version4_Person_Default' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Account_Regional_Registry_Detail_Version4_Person_Default data type contains general information relating to a single SoftLayer RIR account. RIR account information in this type such as names, addresses, and phone numbers are assigned to the registry only and not to users belonging to the account. 





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
[accountId]: #accountid
#### [accountId]
The detail object's associated [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) id   
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
The date and time the detail object was created   
<span class="type-label">Type: </span>**dateTime**

-----
[detailTypeId]: #detailtypeid
#### [detailTypeId]
The detail object's associated [SoftLayer_Account_Regional_Registry_Detail_Type]({{<ref "reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Type">}}) id   
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
Unique ID of the detail object   
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date and time the detail object was last modified   
<span class="type-label">Type: </span>**dateTime**

-----
[regionalInternetRegistryHandleId]: #regionalinternetregistryhandleid
#### [regionalInternetRegistryHandleId]
The detail object's associated [SoftLayer_Account_Rwhois_Handle]({{<ref "reference/datatypes/SoftLayer_Account_Rwhois_Handle">}}) id   
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The account that this detail object belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[detailType]: #detailtype
#### [detailType]
The associated type of this detail object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Type'>SoftLayer_Account_Regional_Registry_Detail_Type </a>**

-----
[details]: #details
#### [details]
References to the [SoftLayer_Network_Subnet_Registration]({{<ref "reference/datatypes/SoftLayer_Network_Subnet_Registration">}}) that consume this detail object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration_Details'>SoftLayer_Network_Subnet_Registration_Details[] </a>**

-----
[properties]: #properties
#### [properties]
The individual properties that define this detail object's values.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Property'>SoftLayer_Account_Regional_Registry_Detail_Property[] </a>**

-----
[regionalInternetRegistryHandle]: #regionalinternetregistryhandle
#### [regionalInternetRegistryHandle]
The associated RWhois handle of this detail object. Used only when detailed reassignments are necessary.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Rwhois_Handle'>SoftLayer_Account_Rwhois_Handle </a>**


## Count

-----
[detailCount]: #detailcount
#### [detailCount]
A count of references to the [SoftLayer_Network_Subnet_Registration]({{<ref "reference/datatypes/SoftLayer_Network_Subnet_Registration">}}) that consume this detail object.   
<span class="type-label">Type: </span>**unsigned long**


-----
[propertyCount]: #propertycount
#### [propertyCount]
A count of the individual properties that define this detail object's values.   
<span class="type-label">Type: </span>**unsigned long**

</div>


