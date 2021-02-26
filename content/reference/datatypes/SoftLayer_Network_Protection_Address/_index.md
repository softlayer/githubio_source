---
title: "SoftLayer_Network_Protection_Address"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Protection_Address"
---

# SoftLayer_Network_Protection_Address
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Protection_Address' >Datatype</a></li>
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
[departmentId]: #departmentid
#### [departmentId]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[ipAddress]: #ipaddress
#### [ipAddress]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[managementMethodType]: #managementmethodtype
#### [managementMethodType]
  
<span class="type-label">Type: </span>**string**


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
[location]: #location
#### [location]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


</div>
<div class="prop-row">

-----
[modifiedUser]: #modifieduser
#### [modifiedUser]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a>**


</div>
<div class="prop-row">

-----
[primaryRouter]: #primaryrouter
#### [primaryRouter]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Router'>SoftLayer_Hardware_Router </a>**


</div>
<div class="prop-row">

-----
[serviceProvider]: #serviceprovider
#### [serviceProvider]
DEPRECATED  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Service_Provider'>SoftLayer_Service_Provider </a>**


</div>
<div class="prop-row">

-----
[subnet]: #subnet
#### [subnet]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a>**


</div>
<div class="prop-row">

-----
[subnetIpAddress]: #subnetipaddress
#### [subnetIpAddress]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a>**


</div>
<div class="prop-row">

-----
[terminatedUser]: #terminateduser
#### [terminatedUser]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a>**


</div>
<div class="prop-row">

-----
[ticket]: #ticket
#### [ticket]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>**


</div>
<div class="prop-row">

-----
[transactions]: #transactions
#### [transactions]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction[] </a>**


</div>
<div class="prop-row">

-----
[userDepartment]: #userdepartment
#### [userDepartment]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee_Department'>SoftLayer_User_Employee_Department </a>**


</div>
<div class="prop-row">

-----
[userRecord]: #userrecord
#### [userRecord]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a>**


</div>

## Count
<div class="prop-row">

-----
[transactionCount]: #transactioncount
#### [transactionCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


