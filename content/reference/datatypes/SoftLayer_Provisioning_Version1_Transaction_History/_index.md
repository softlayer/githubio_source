---
title: "SoftLayer_Provisioning_Version1_Transaction_History"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Provisioning"
classes:
    - "SoftLayer_Provisioning_Version1_Transaction_History"
---

# SoftLayer_Provisioning_Version1_Transaction_History
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction_History' >Datatype</a></li>
    </ul>
</div>

## Description 






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
[finishDate]: #finishdate
#### [finishDate]
The finish date of a transaction history record.  
<span class="type-label">Type: </span>**dateTime**

-----
[guestId]: #guestid
#### [guestId]
The guest ID associated with a transaction history.  
<span class="type-label">Type: </span>**integer**

-----
[hardwareId]: #hardwareid
#### [hardwareId]
The hardware ID associated with a transaction history.  
<span class="type-label">Type: </span>**integer**

-----
[hostId]: #hostid
#### [hostId]
The host ID associated with a transaction history.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
The ID associated with a transaction history.  
<span class="type-label">Type: </span>**integer**

-----
[startDate]: #startdate
#### [startDate]
The start date of a transaction history record.  
<span class="type-label">Type: </span>**dateTime**

-----
[transactionId]: #transactionid
#### [transactionId]
The transaction ID associated with a transaction history.  
<span class="type-label">Type: </span>**integer**

-----
[transactionStatusId]: #transactionstatusid
#### [transactionStatusId]
The transaction status ID associated with a transaction history.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[guest]: #guest
#### [guest]
The guest from where transaction history originates.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**

-----
[hardware]: #hardware
#### [hardware]
The hardware from where transaction history originates.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**

-----
[transaction]: #transaction
#### [transaction]
The transaction from where transaction history originates.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>**

-----
[transactionStatus]: #transactionstatus
#### [transactionStatus]
The transaction status of a transaction history.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction_Status'>SoftLayer_Provisioning_Version1_Transaction_Status </a>**


## Count
</div>


