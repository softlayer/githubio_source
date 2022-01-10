---
title: "SoftLayer_Account_Reports_Request"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Reports_Request"
---

# SoftLayer_Account_Reports_Request
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Reports_Request' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Reports_Request' >Datatype</a></li>
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
[accountContactId]: #accountcontactid
#### [accountContactId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[accountId]: #accountid
#### [accountId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[complianceReportTypeId]: #compliancereporttypeid
#### [complianceReportTypeId]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[employeeRecordId]: #employeerecordid
#### [employeeRecordId]
  
<span class="type-label">Type: </span>**integer**  



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
[nda]: #nda
#### [nda]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[notes]: #notes
#### [notes]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[report]: #report
#### [report]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[requestKey]: #requestkey
#### [requestKey]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[requestorContactId]: #requestorcontactid
#### [requestorContactId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[ticketId]: #ticketid
#### [ticketId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[usrRecordId]: #usrrecordid
#### [usrRecordId]
  
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
[accountContact]: #accountcontact
#### [accountContact]
A request's corresponding external contact, if one exists.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Contact'>SoftLayer_Account_Contact </a>**  



</div>
<div class="prop-row">

-----
[reportType]: #reporttype
#### [reportType]
Type of the report customer is requesting for.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Compliance_Report_Type'>SoftLayer_Compliance_Report_Type </a>**  



</div>
<div class="prop-row">

-----
[requestorContact]: #requestorcontact
#### [requestorContact]
A request's corresponding requestor contact, if one exists.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Contact'>SoftLayer_Account_Contact </a>**  



</div>
<div class="prop-row">

-----
[ticket]: #ticket
#### [ticket]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>**  



</div>
<div class="prop-row">

-----
[user]: #user
#### [user]
The customer user that initiated a report request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**  



</div>

## Count
</div>


