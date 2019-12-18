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
[displayName]: #displayname
#### [displayName]
  
<span class="type-label">Type: </span>**string**

-----
[email]: #email
#### [email]
A SoftLayer employee's email address. Email addresses are only visible to [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) that are assigned to an employee   
<span class="type-label">Type: </span>**string**

-----
[employeeDepartmentId]: #employeedepartmentid
#### [employeeDepartmentId]
A SoftLayer employee's [SoftLayer_User_Employee_Department]({{<ref "reference/datatypes/SoftLayer_User_Employee_Department">}}) id.   
<span class="type-label">Type: </span>**integer**

-----
[firstName]: #firstname
#### [firstName]
A SoftLayer employee's first name. First names are only visible to [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) that are assigned to an employee   
<span class="type-label">Type: </span>**string**

-----
[lastName]: #lastname
#### [lastName]
A SoftLayer employee's last name. Last names are only visible to [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) that are assigned to an employee   
<span class="type-label">Type: </span>**string**

-----
[officePhone]: #officephone
#### [officePhone]
  
<span class="type-label">Type: </span>**string**

-----
[username]: #username
#### [username]
A representation of a SoftLayer employee's username. In all cases this should simply state "Employee".  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[chatTranscript]: #chattranscript
#### [chatTranscript]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Chat'>SoftLayer_Ticket_Chat[] </a>**

-----
[employeeDepartment]: #employeedepartment
#### [employeeDepartment]
The department that a SoftLayer employee belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee_Department'>SoftLayer_User_Employee_Department </a>**

-----
[layoutProfiles]: #layoutprofiles
#### [layoutProfiles]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Layout_Profile'>SoftLayer_Layout_Profile[] </a>**

-----
[metricTrackingObject]: #metrictrackingobject
#### [metricTrackingObject]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object'>SoftLayer_Metric_Tracking_Object </a>**

-----
[securityLevels]: #securitylevels
#### [securityLevels]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Level'>SoftLayer_Security_Level[] </a>**

-----
[ticketActivities]: #ticketactivities
#### [ticketActivities]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Activity'>SoftLayer_Ticket_Activity[] </a>**

-----
[ticketAttachmentReferences]: #ticketattachmentreferences
#### [ticketAttachmentReferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Attachment'>SoftLayer_Ticket_Attachment[] </a>**


## Count

-----
[chatTranscriptCount]: #chattranscriptcount
#### [chatTranscriptCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[layoutProfileCount]: #layoutprofilecount
#### [layoutProfileCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[securityLevelCount]: #securitylevelcount
#### [securityLevelCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[ticketActivityCount]: #ticketactivitycount
#### [ticketActivityCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[ticketAttachmentReferenceCount]: #ticketattachmentreferencecount
#### [ticketAttachmentReferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>


