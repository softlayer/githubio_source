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
[departmentId]: #departmentid
#### [departmentId]
  
<span class="type-label">Type: </span>**integer**

-----
[ipAddress]: #ipaddress
#### [ipAddress]
  
<span class="type-label">Type: </span>**string**

-----
[managementMethodType]: #managementmethodtype
#### [managementMethodType]
  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[location]: #location
#### [location]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[modifiedUser]: #modifieduser
#### [modifiedUser]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a>**

-----
[primaryRouter]: #primaryrouter
#### [primaryRouter]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Router'>SoftLayer_Hardware_Router </a>**

-----
[serviceProvider]: #serviceprovider
#### [serviceProvider]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Service_Provider'>SoftLayer_Service_Provider </a>**

-----
[subnet]: #subnet
#### [subnet]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a>**

-----
[subnetIpAddress]: #subnetipaddress
#### [subnetIpAddress]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a>**

-----
[terminatedUser]: #terminateduser
#### [terminatedUser]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a>**

-----
[ticket]: #ticket
#### [ticket]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>**

-----
[transactions]: #transactions
#### [transactions]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction[] </a>**

-----
[userDepartment]: #userdepartment
#### [userDepartment]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee_Department'>SoftLayer_User_Employee_Department </a>**

-----
[userRecord]: #userrecord
#### [userRecord]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a>**


## Count

-----
[transactionCount]: #transactioncount
#### [transactionCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>


