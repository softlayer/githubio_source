---
title: "editAccount"
description: "This method will edit the account's information. Pass in a SoftLayer_Account template with the fields to be modified. Ce... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/editAccount"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::editAccount

Edit an account's information.


## Overview 
This method will edit the account's information. Pass in a SoftLayer_Account template with the fields to be modified. Certain changes to the account will automatically create a ticket for manual review. This will be returned with the SoftLayer_Container_Account_Update_Response.<br> <br> The following fields are editable:<br> <br> <ul> <li>companyName</li> <li>firstName</li> <li>lastName</li> <li>address1</li> <li>address2</li> <li>city</li> <li>state</li> <li>country</li> <li>postalCode</li> <li>email</li> <li>officePhone</li> <li>alternatePhone</li> <li>faxPhone</li> <li>abuseEmails.email</li> <li>billingInfo.vatId</li> </ul> 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|modifiedAccountInformation| <a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>| Account template containing the information to update to.|


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Account_Update_Response'>SoftLayer_Container_Account_Update_Response </a>



### Error Handling

*  

> SoftLayer_Exception_Public_Validation 



