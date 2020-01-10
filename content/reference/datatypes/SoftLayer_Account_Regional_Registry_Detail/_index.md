---
title: "SoftLayer_Account_Regional_Registry_Detail"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Regional_Registry_Detail"
---

# SoftLayer_Account_Regional_Registry_Detail
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Regional_Registry_Detail' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail' >Datatype</a></li>
    </ul>
</div>

## Description 










<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[accountId]: #accountid
#### [accountId]
The detail object's associated [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) id   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date and time the detail object was created   
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[detailTypeId]: #detailtypeid
#### [detailTypeId]
The detail object's associated [SoftLayer_Account_Regional_Registry_Detail_Type]({{<ref "reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Type">}}) id   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Unique ID of the detail object   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date and time the detail object was last modified   
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[regionalInternetRegistryHandleId]: #regionalinternetregistryhandleid
#### [regionalInternetRegistryHandleId]
The detail object's associated [SoftLayer_Account_Rwhois_Handle]({{<ref "reference/datatypes/SoftLayer_Account_Rwhois_Handle">}}) id   
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account that this detail object belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[detailType]: #detailtype
#### [detailType]
The associated type of this detail object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Type'>SoftLayer_Account_Regional_Registry_Detail_Type </a>**


</div>
<div class="prop-row">

-----
[details]: #details
#### [details]
References to the [SoftLayer_Network_Subnet_Registration]({{<ref "reference/datatypes/SoftLayer_Network_Subnet_Registration">}}) that consume this detail object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration_Details'>SoftLayer_Network_Subnet_Registration_Details[] </a>**


</div>
<div class="prop-row">

-----
[properties]: #properties
#### [properties]
The individual properties that define this detail object's values.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Property'>SoftLayer_Account_Regional_Registry_Detail_Property[] </a>**


</div>
<div class="prop-row">

-----
[regionalInternetRegistryHandle]: #regionalinternetregistryhandle
#### [regionalInternetRegistryHandle]
The associated RWhois handle of this detail object. Used only when detailed reassignments are necessary.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Rwhois_Handle'>SoftLayer_Account_Rwhois_Handle </a>**


</div>

## Count
<div class="prop-row">

-----
[detailCount]: #detailcount
#### [detailCount]
A count of references to the [SoftLayer_Network_Subnet_Registration]({{<ref "reference/datatypes/SoftLayer_Network_Subnet_Registration">}}) that consume this detail object.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[propertyCount]: #propertycount
#### [propertyCount]
A count of the individual properties that define this detail object's values.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


