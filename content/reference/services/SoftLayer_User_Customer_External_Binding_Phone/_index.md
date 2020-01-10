---
title: "SoftLayer_User_Customer_External_Binding_Phone"
description: "SoftLayer provides its customers the ability to add an additional layer of security to the SoftLayer customer portal by... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_External_Binding_Phone"
---
# SoftLayer_User_Customer_External_Binding_Phone
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_External_Binding_Phone' >Datatype</a></li>
    </ul>
</div>

## Description
SoftLayer provides its customers the ability to add an additional layer of security to the SoftLayer customer portal by requiring that a user login and authenticate with a trusted 3rd party before they are given access to their SoftLayer account.  This is accomplished by creating an external binding for a specific vendor such as PhoneFactor. When the SoftLayer user attempts to log in to the SoftLayer customer portal or VPN, they will first be prompted for their normal SoftLayer username and password.  Once that information is verified they will be asked to authenticate via phone, SMS or mobile phone application. Once authenticated with the trusted vendor the user will be allowed access to the SoftLayer customer portal or VPN. 

The Phone external binding service allows a user to create an external binding, enable, disable, or unlock an external binding, and delete an external binding. 

Once a SoftLayer user has a valid and active external binding, they will be required to always use their credential to login to the SoftLayer customer portal.  In addition any user with an active external binding will be prohibited from using the API. 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [checkPhoneValidationResult](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/checkPhoneValidationResult)
Return a phone validation result
</div>

<div class="method-row">

#### [deleteObject](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/deleteObject)
Delete an external authentication binding.
</div>

<div class="method-row">

#### [disable](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/disable)
Disable an external binding.
</div>

<div class="method-row">

#### [enable](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/enable)
Enable an external binding.
</div>

<div class="method-row">

#### [getAllAuthenticationModes](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getAllAuthenticationModes)
Returns available authentication modes
</div>

<div class="method-row">

#### [getAllAuthenticationPinModes](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getAllAuthenticationPinModes)
Returns available authentication pin modes
</div>

<div class="method-row">

#### [getAttributes](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getAttributes)
Retrieve attributes of an external authentication binding.
</div>

<div class="method-row">

#### [getAuthenticationMode](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getAuthenticationMode)
Returns the authentication mode
</div>

<div class="method-row">

#### [getBillingItem](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getBillingItem)
Retrieve the current billing item for an external binding.
</div>

<div class="method-row">

#### [getBindingStatus](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getBindingStatus)
Retrieve the current external binding status. It can be "ACTIVE" or "BLOCKED".
</div>

<div class="method-row">

#### [getNote](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getNote)
Retrieve an optional note for identifying the external binding.
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getObject)
Retrieve a SoftLayer_User_Customer_External_Binding_Phone record.
</div>

<div class="method-row">

#### [getPhoneAppActivationCode](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getPhoneAppActivationCode)
Return a mobile phone app activation code
</div>

<div class="method-row">

#### [getPhoneData](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getPhoneData)
Returns the authentication phone data.
</div>

<div class="method-row">

#### [getPinLength](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getPinLength)

</div>

<div class="method-row">

#### [getType](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getType)
Retrieve the type of external authentication binding.
</div>

<div class="method-row">

#### [getUser](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getUser)
Retrieve the SoftLayer user that the external authentication binding belongs to.
</div>

<div class="method-row">

#### [getVendor](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getVendor)
Retrieve the vendor of an external authentication binding.
</div>

<div class="method-row">

#### [requestPhoneValidation](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/requestPhoneValidation)
Initiates a phone validation requests and returns a unique token
</div>

<div class="method-row">

#### [updateAuthenticationMode](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/updateAuthenticationMode)
Updates the authentication mode
</div>

<div class="method-row">

#### [updateNote](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/updateNote)
Update the note of an external binding.
</div>

<div class="method-row">

#### [updatePhone](/reference/services/SoftLayer_User_Customer_External_Binding_Phone/updatePhone)
Updates the authentication phone numbers.
</div>
</div>

</div>

