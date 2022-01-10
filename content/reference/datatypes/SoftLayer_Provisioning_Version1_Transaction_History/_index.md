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
[finishDate]: #finishdate
#### [finishDate]
The finish date of a transaction history record.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[guestId]: #guestid
#### [guestId]
The guest ID associated with a transaction history.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[hardwareId]: #hardwareid
#### [hardwareId]
The hardware ID associated with a transaction history.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[hostId]: #hostid
#### [hostId]
The host ID associated with a transaction history.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The ID associated with a transaction history.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[startDate]: #startdate
#### [startDate]
The start date of a transaction history record.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[transactionId]: #transactionid
#### [transactionId]
The transaction ID associated with a transaction history.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[transactionStatusId]: #transactionstatusid
#### [transactionStatusId]
The transaction status ID associated with a transaction history.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[guest]: #guest
#### [guest]
The guest from where transaction history originates.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**  



</div>
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
The hardware from where transaction history originates.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**  



</div>
<div class="prop-row">

-----
[transaction]: #transaction
#### [transaction]
The transaction from where transaction history originates.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>**  



</div>
<div class="prop-row">

-----
[transactionStatus]: #transactionstatus
#### [transactionStatus]
The transaction status of a transaction history.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction_Status'>SoftLayer_Provisioning_Version1_Transaction_Status </a>**  



</div>

## Count
</div>


