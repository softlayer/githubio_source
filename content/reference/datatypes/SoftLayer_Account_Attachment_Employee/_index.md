---
title: "SoftLayer_Account_Attachment_Employee"
description: "A SoftLayer_Account_Attachment_Employee models an assignment of a single [SoftLayer_User_Employee]({{<ref 'reference/dat... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Attachment_Employee"
---

# SoftLayer_Account_Attachment_Employee
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Attachment_Employee' >Datatype</a></li>
    </ul>
</div>

## Description 
A SoftLayer_Account_Attachment_Employee models an assignment of a single [SoftLayer_User_Employee]({{<ref "reference/datatypes/SoftLayer_User_Employee">}}) 





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
[roleId]: #roleid
#### [roleId]
Role identifier.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
A [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[employee]: #employee
#### [employee]
A [SoftLayer_User_Employee]({{<ref "reference/datatypes/SoftLayer_User_Employee">}}).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a>**

-----
[employeeRole]: #employeerole
#### [employeeRole]
A [SoftLayer_User_Employee]({{<ref "reference/datatypes/SoftLayer_User_Employee">}}).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Attachment_Employee_Role'>SoftLayer_Account_Attachment_Employee_Role </a>**


## Count
</div>


