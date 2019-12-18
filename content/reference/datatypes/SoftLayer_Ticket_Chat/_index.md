---
title: "SoftLayer_Ticket_Chat"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Chat"
---

# SoftLayer_Ticket_Chat
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Ticket_Chat' >Datatype</a></li>
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
[customerId]: #customerid
#### [customerId]
  
<span class="type-label">Type: </span>**integer**

-----
[endDate]: #enddate
#### [endDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[startDate]: #startdate
#### [startDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[transcript]: #transcript
#### [transcript]
  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[agent]: #agent
#### [agent]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a>**

-----
[customer]: #customer
#### [customer]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**

-----
[ticketUpdate]: #ticketupdate
#### [ticketUpdate]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Update_Chat'>SoftLayer_Ticket_Update_Chat </a>**


## Count
</div>


