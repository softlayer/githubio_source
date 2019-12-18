---
title: "SoftLayer_Software_AccountLicense"
description: "SoftLayer_Software_AccountLicense is a class that represents software licenses that are tied only to a customer's accoun... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_AccountLicense"
---

# SoftLayer_Software_AccountLicense
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Software_AccountLicense' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Software_AccountLicense' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Software_AccountLicense is a class that represents software licenses that are tied only to a customer's account and not to any particular hardware, IP address, etc. 



### seeAlso

* [SoftLayer_Account](/reference/datatypes/SoftLayer_Account )


* [SoftLayer_Software_Description](/reference/datatypes/SoftLayer_Software_Description )




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
[accountId]: #accountid
#### [accountId]
The ID of the SoftLayer Account to which this Account License belongs to.  
<span class="type-label">Type: </span>**integer**

-----
[capacity]: #capacity
#### [capacity]
Some Account Licenses have capacity information such as CPU specified in the units key. This provides the numerical representation of the capacity of the units.   
<span class="type-label">Type: </span>**string**

-----
[key]: #key
#### [key]
The License Key for this specific Account License.  
<span class="type-label">Type: </span>**string**

-----
[units]: #units
#### [units]
The unit of measurement that an account license has the capacity of.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The customer account this Account License belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[billingItem]: #billingitem
#### [billingItem]
The billing item for a software account license.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**

-----
[softwareDescription]: #softwaredescription
#### [softwareDescription]
The SoftLayer_Software_Description that this account license is for.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description </a>**


## Count
</div>


