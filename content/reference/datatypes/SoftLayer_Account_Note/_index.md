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
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[note]: #note
#### [note]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[noteTypeId]: #notetypeid
#### [noteTypeId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[userId]: #userid
#### [userId]
  
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
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[customer]: #customer
#### [customer]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**  



</div>
<div class="prop-row">

-----
[noteHistory]: #notehistory
#### [noteHistory]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Note_History'>SoftLayer_Account_Note_History[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[noteHistoryCount]: #notehistorycount
#### [noteHistoryCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


