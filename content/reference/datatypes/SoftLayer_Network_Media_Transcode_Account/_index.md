---
title: "SoftLayer_Network_Media_Transcode_Account"
description: "The SoftLayer_Network_Media_Transcode_Account contains information regarding a transcode account."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Media_Transcode_Account"
---

# SoftLayer_Network_Media_Transcode_Account
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Media_Transcode_Account' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Media_Transcode_Account' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Media_Transcode_Account contains information regarding a transcode account. 





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
The internal identifier of a SoftLayer account  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The created date  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The internal identifier of a transcode account  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The last modified date  
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
The SoftLayer account information  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[transcodeJobs]: #transcodejobs
#### [transcodeJobs]
Transcode jobs  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Media_Transcode_Job'>SoftLayer_Network_Media_Transcode_Job[] </a>**


</div>

## Count
<div class="prop-row">

-----
[transcodeJobCount]: #transcodejobcount
#### [transcodeJobCount]
A count of transcode jobs   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


