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
[accountContactId]: #accountcontactid
#### [accountContactId]
  
<span class="type-label">Type: </span>**integer**

-----
[accountId]: #accountid
#### [accountId]
  
<span class="type-label">Type: </span>**integer**

-----
[complianceReportTypeId]: #compliancereporttypeid
#### [complianceReportTypeId]
  
<span class="type-label">Type: </span>**string**

-----
[createDate]: #createdate
#### [createDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[employeeRecordId]: #employeerecordid
#### [employeeRecordId]
  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[nda]: #nda
#### [nda]
  
<span class="type-label">Type: </span>**string**

-----
[notes]: #notes
#### [notes]
  
<span class="type-label">Type: </span>**string**

-----
[report]: #report
#### [report]
  
<span class="type-label">Type: </span>**string**

-----
[requestKey]: #requestkey
#### [requestKey]
  
<span class="type-label">Type: </span>**string**

-----
[requestorContactId]: #requestorcontactid
#### [requestorContactId]
  
<span class="type-label">Type: </span>**integer**

-----
[status]: #status
#### [status]
  
<span class="type-label">Type: </span>**string**

-----
[ticketId]: #ticketid
#### [ticketId]
  
<span class="type-label">Type: </span>**integer**

-----
[usrRecordId]: #usrrecordid
#### [usrRecordId]
  
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
[accountContact]: #accountcontact
#### [accountContact]
A request's corresponding external contact, if one exists.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Contact'>SoftLayer_Account_Contact </a>**

-----
[reportType]: #reporttype
#### [reportType]
Type of the report customer is requesting for.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Compliance_Report_Type'>SoftLayer_Compliance_Report_Type </a>**

-----
[requestorContact]: #requestorcontact
#### [requestorContact]
A request's corresponding requestor contact, if one exists.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Contact'>SoftLayer_Account_Contact </a>**

-----
[ticket]: #ticket
#### [ticket]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>**

-----
[user]: #user
#### [user]
The customer user that initiated a report request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**


## Count
</div>


