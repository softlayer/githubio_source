---
title: "SoftLayer_Account_Note"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Note"
---

# SoftLayer_Account_Note
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Note' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Note' >Datatype</a></li>
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
[accountId]: #accountid
#### [accountId]
  
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[note]: #note
#### [note]
  
<span class="type-label">Type: </span>**string**

-----
[noteTypeId]: #notetypeid
#### [noteTypeId]
  
<span class="type-label">Type: </span>**integer**

-----
[userId]: #userid
#### [userId]
  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[customer]: #customer
#### [customer]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**

-----
[noteHistory]: #notehistory
#### [noteHistory]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Note_History'>SoftLayer_Account_Note_History[] </a>**


## Count

-----
[noteHistoryCount]: #notehistorycount
#### [noteHistoryCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>


