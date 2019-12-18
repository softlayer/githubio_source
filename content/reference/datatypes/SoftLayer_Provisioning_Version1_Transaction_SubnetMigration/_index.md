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
The date a transaction was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[elapsedSeconds]: #elapsedseconds
#### [elapsedSeconds]
The amount of seconds that have elapsed since the transaction was last modified.  
<span class="type-label">Type: </span>**integer**

-----
[guestId]: #guestid
#### [guestId]
A transaction's associated guest identification number.  
<span class="type-label">Type: </span>**integer**

-----
[hardwareId]: #hardwareid
#### [hardwareId]
A transaction's associated hardware identification number.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
A transaction's identifying number.  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a transaction was last modified.  
<span class="type-label">Type: </span>**dateTime**

-----
[statusChangeDate]: #statuschangedate
#### [statusChangeDate]
The date the transaction status was last modified.  
<span class="type-label">Type: </span>**dateTime**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The account that a transaction belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[guest]: #guest
#### [guest]
The guest record for this transaction.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**

-----
[hardware]: #hardware
#### [hardware]
The hardware object for this transaction.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**

-----
[loopback]: #loopback
#### [loopback]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction[] </a>**

-----
[pendingTransactions]: #pendingtransactions
#### [pendingTransactions]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction[] </a>**

-----
[ticketScheduledActionReference]: #ticketscheduledactionreference
#### [ticketScheduledActionReference]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Attachment'>SoftLayer_Ticket_Attachment[] </a>**

-----
[transactionGroup]: #transactiongroup
#### [transactionGroup]
A transaction's group. This group object determines what type of service is being done on the hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction_Group'>SoftLayer_Provisioning_Version1_Transaction_Group </a>**

-----
[transactionStatus]: #transactionstatus
#### [transactionStatus]
A transaction's status. This status object determines the state it is in the transaction group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction_Status'>SoftLayer_Provisioning_Version1_Transaction_Status </a>**


## Count

-----
[loopbackCount]: #loopbackcount
#### [loopbackCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[pendingTransactionCount]: #pendingtransactioncount
#### [pendingTransactionCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[ticketScheduledActionReferenceCount]: #ticketscheduledactionreferencecount
#### [ticketScheduledActionReferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>


