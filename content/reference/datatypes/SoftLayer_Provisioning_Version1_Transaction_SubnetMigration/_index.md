---
title: "SoftLayer_Provisioning_Version1_Transaction_SubnetMigration"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Provisioning"
classes:
    - "SoftLayer_Provisioning_Version1_Transaction_SubnetMigration"
---

# SoftLayer_Provisioning_Version1_Transaction_SubnetMigration
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction_SubnetMigration' >Datatype</a></li>
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
[createDate]: #createdate
#### [createDate]
The date a transaction was created.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[elapsedSeconds]: #elapsedseconds
#### [elapsedSeconds]
The amount of seconds that have elapsed since the transaction was last modified.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[guestId]: #guestid
#### [guestId]
A transaction's associated guest identification number.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[hardwareId]: #hardwareid
#### [hardwareId]
A transaction's associated hardware identification number.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A transaction's identifying number.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a transaction was last modified.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[statusChangeDate]: #statuschangedate
#### [statusChangeDate]
The date the transaction status was last modified.  
<span class="type-label">Type: </span>**dateTime**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account that a transaction belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[guest]: #guest
#### [guest]
The guest record for this transaction.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**


</div>
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
The hardware object for this transaction.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**


</div>
<div class="prop-row">

-----
[loopback]: #loopback
#### [loopback]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction[] </a>**


</div>
<div class="prop-row">

-----
[pendingTransactions]: #pendingtransactions
#### [pendingTransactions]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction[] </a>**


</div>
<div class="prop-row">

-----
[ticketScheduledActionReference]: #ticketscheduledactionreference
#### [ticketScheduledActionReference]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Attachment'>SoftLayer_Ticket_Attachment[] </a>**


</div>
<div class="prop-row">

-----
[transactionGroup]: #transactiongroup
#### [transactionGroup]
A transaction's group. This group object determines what type of service is being done on the hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction_Group'>SoftLayer_Provisioning_Version1_Transaction_Group </a>**


</div>
<div class="prop-row">

-----
[transactionStatus]: #transactionstatus
#### [transactionStatus]
A transaction's status. This status object determines the state it is in the transaction group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction_Status'>SoftLayer_Provisioning_Version1_Transaction_Status </a>**


</div>

## Count
<div class="prop-row">

-----
[loopbackCount]: #loopbackcount
#### [loopbackCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[pendingTransactionCount]: #pendingtransactioncount
#### [pendingTransactionCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[ticketScheduledActionReferenceCount]: #ticketscheduledactionreferencecount
#### [ticketScheduledActionReferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


