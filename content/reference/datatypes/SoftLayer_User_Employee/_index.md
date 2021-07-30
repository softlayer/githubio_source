---
title: "SoftLayer_User_Employee"
description: "A SoftLayer_User_Employee models a single SoftLayer employee for the purposes of ticket updates created by SoftLayer emp... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Employee"
---

# SoftLayer_User_Employee
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Employee' >Datatype</a></li>
    </ul>
</div>

## Description 
A SoftLayer_User_Employee models a single SoftLayer employee for the purposes of ticket updates created by SoftLayer employees. SoftLayer portal and API users cannot see individual employee names in ticket responses.  SoftLayer employees can be assigned to customer accounts as a personal support representative.  Employee names and email will be available if an employee is assigned to the account. 


### associatedMethods

*  [SoftLayer_Account::getSupportRepresentatives](/reference/services/SoftLayer_Account/getSupportRepresentatives )



### seeAlso

* [SoftLayer_Ticket_Update_Employee](/reference/services/SoftLayer_Ticket_Update_Employee )




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
[displayName]: #displayname
#### [displayName]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[email]: #email
#### [email]
A SoftLayer employee's email address. Email addresses are only visible to [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) that are assigned to an employee   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[employeeDepartmentId]: #employeedepartmentid
#### [employeeDepartmentId]
A SoftLayer employee's [SoftLayer_User_Employee_Department]({{<ref "reference/datatypes/SoftLayer_User_Employee_Department">}}) id.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[firstName]: #firstname
#### [firstName]
A SoftLayer employee's first name. First names are only visible to [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) that are assigned to an employee   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[lastName]: #lastname
#### [lastName]
A SoftLayer employee's last name. Last names are only visible to [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) that are assigned to an employee   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[officePhone]: #officephone
#### [officePhone]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[username]: #username
#### [username]
A representation of a SoftLayer employee's username.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[chatTranscript]: #chattranscript
#### [chatTranscript]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Chat'>SoftLayer_Ticket_Chat[] </a>**


</div>
<div class="prop-row">

-----
[employeeDepartment]: #employeedepartment
#### [employeeDepartment]
The department that a SoftLayer employee belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee_Department'>SoftLayer_User_Employee_Department </a>**


</div>
<div class="prop-row">

-----
[layoutProfiles]: #layoutprofiles
#### [layoutProfiles]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Layout_Profile'>SoftLayer_Layout_Profile[] </a>**


</div>
<div class="prop-row">

-----
[metricTrackingObject]: #metrictrackingobject
#### [metricTrackingObject]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object'>SoftLayer_Metric_Tracking_Object </a>**


</div>
<div class="prop-row">

-----
[securityLevels]: #securitylevels
#### [securityLevels]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Level'>SoftLayer_Security_Level[] </a>**


</div>
<div class="prop-row">

-----
[ticketActivities]: #ticketactivities
#### [ticketActivities]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Activity'>SoftLayer_Ticket_Activity[] </a>**


</div>
<div class="prop-row">

-----
[ticketAttachmentReferences]: #ticketattachmentreferences
#### [ticketAttachmentReferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Attachment'>SoftLayer_Ticket_Attachment[] </a>**


</div>

## Count
<div class="prop-row">

-----
[chatTranscriptCount]: #chattranscriptcount
#### [chatTranscriptCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[layoutProfileCount]: #layoutprofilecount
#### [layoutProfileCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[securityLevelCount]: #securitylevelcount
#### [securityLevelCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[ticketActivityCount]: #ticketactivitycount
#### [ticketActivityCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[ticketAttachmentReferenceCount]: #ticketattachmentreferencecount
#### [ticketAttachmentReferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


