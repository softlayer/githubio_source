---
title: "SoftLayer_Account_Partner_Referral_Prospect"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Partner_Referral_Prospect"
---

# SoftLayer_Account_Partner_Referral_Prospect
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Partner_Referral_Prospect' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Partner_Referral_Prospect' >Datatype</a></li>
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
[companyName]: #companyname
#### [companyName]
  
<span class="type-label">Type: </span>**string**

-----
[emailAddress]: #emailaddress
#### [emailAddress]
  
<span class="type-label">Type: </span>**string**

-----
[firstName]: #firstname
#### [firstName]
  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**

-----
[lastName]: #lastname
#### [lastName]
  
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
[assignedEmployees]: #assignedemployees
#### [assignedEmployees]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee[] </a>**

-----
[quotes]: #quotes
#### [quotes]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Quote'>SoftLayer_Billing_Order_Quote[] </a>**

-----
[type]: #type
#### [type]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer_Prospect_Type'>SoftLayer_User_Customer_Prospect_Type </a>**


## Count

-----
[assignedEmployeeCount]: #assignedemployeecount
#### [assignedEmployeeCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[quoteCount]: #quotecount
#### [quoteCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>


