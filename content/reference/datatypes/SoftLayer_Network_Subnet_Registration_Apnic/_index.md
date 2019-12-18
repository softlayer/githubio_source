---
title: "SoftLayer_Network_Subnet_Registration_Apnic"
description: "APNIC-specific registration object. For more detail see [SoftLayer_Network_Subnet_Registration]({{<ref 'reference/dataty... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Registration_Apnic"
---

# SoftLayer_Network_Subnet_Registration_Apnic
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration_Apnic' >Datatype</a></li>
    </ul>
</div>

## Description 
APNIC-specific registration object. For more detail see [SoftLayer_Network_Subnet_Registration]({{<ref "reference/datatypes/SoftLayer_Network_Subnet_Registration">}}). 





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
The registration object's associated [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) id   
<span class="type-label">Type: </span>**integer**

-----
[cidr]: #cidr
#### [cidr]
The CIDR prefix for the registered subnet   
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
Unique ID of the registration object   
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[networkHandle]: #networkhandle
#### [networkHandle]
The RIR-specific handle or name of the registered subnet. This field is read-only.   
<span class="type-label">Type: </span>**string**

-----
[networkIdentifier]: #networkidentifier
#### [networkIdentifier]
The base IP address of the registered subnet   
<span class="type-label">Type: </span>**string**

-----
[regionalInternetRegistryHandleId]: #regionalinternetregistryhandleid
#### [regionalInternetRegistryHandleId]
The registration object's associated [SoftLayer_Account_Rwhois_Handle]({{<ref "reference/datatypes/SoftLayer_Account_Rwhois_Handle">}}) id   
<span class="type-label">Type: </span>**integer**

-----
[regionalInternetRegistryId]: #regionalinternetregistryid
#### [regionalInternetRegistryId]
The registration object's associated [SoftLayer_Network_Regional_Internet_Registry]({{<ref "reference/datatypes/SoftLayer_Network_Regional_Internet_Registry">}}) id   
<span class="type-label">Type: </span>**integer**

-----
[statusId]: #statusid
#### [statusId]
The registration object's associated [SoftLayer_Network_Subnet_Registration_Status]({{<ref "reference/datatypes/SoftLayer_Network_Subnet_Registration_Status">}}) id   
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The account that this registration belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[detailReferences]: #detailreferences
#### [detailReferences]
The cross-reference records that tie the [SoftLayer_Account_Regional_Registry_Detail]({{<ref "reference/datatypes/SoftLayer_Account_Regional_Registry_Detail">}}) objects to the registration object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration_Details'>SoftLayer_Network_Subnet_Registration_Details[] </a>**

-----
[events]: #events
#### [events]
The related registration events.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration_Event'>SoftLayer_Network_Subnet_Registration_Event[] </a>**

-----
[networkDetail]: #networkdetail
#### [networkDetail]
The "network" detail object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail'>SoftLayer_Account_Regional_Registry_Detail </a>**

-----
[personDetail]: #persondetail
#### [personDetail]
The "person" detail object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail'>SoftLayer_Account_Regional_Registry_Detail </a>**

-----
[regionalInternetRegistry]: #regionalinternetregistry
#### [regionalInternetRegistry]
The related Regional Internet Registry.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Regional_Internet_Registry'>SoftLayer_Network_Regional_Internet_Registry </a>**

-----
[regionalInternetRegistryHandle]: #regionalinternetregistryhandle
#### [regionalInternetRegistryHandle]
The RIR handle that this registration object belongs to. This field may not be populated until the registration is complete.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Rwhois_Handle'>SoftLayer_Account_Rwhois_Handle </a>**

-----
[status]: #status
#### [status]
The status of this registration.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration_Status'>SoftLayer_Network_Subnet_Registration_Status </a>**

-----
[subnet]: #subnet
#### [subnet]
The subnet that this registration pertains to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a>**


## Count

-----
[detailReferenceCount]: #detailreferencecount
#### [detailReferenceCount]
A count of the cross-reference records that tie the [SoftLayer_Account_Regional_Registry_Detail]({{<ref "reference/datatypes/SoftLayer_Account_Regional_Registry_Detail">}}) objects to the registration object.   
<span class="type-label">Type: </span>**unsigned long**


-----
[eventCount]: #eventcount
#### [eventCount]
A count of the related registration events.   
<span class="type-label">Type: </span>**unsigned long**

</div>


