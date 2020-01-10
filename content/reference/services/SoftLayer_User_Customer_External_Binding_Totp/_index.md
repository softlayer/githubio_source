---
title: "SoftLayer_User_Customer_External_Binding_Totp"
description: "SoftLayer provides its customers the ability to add an additional layer of security to the SoftLayer customer portal by... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_External_Binding_Totp"
---
# SoftLayer_User_Customer_External_Binding_Totp
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_User_Customer_External_Binding_Totp' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_External_Binding_Totp' >Datatype</a></li>
    </ul>
</div>

## Description
SoftLayer provides its customers the ability to add an additional layer of security to the SoftLayer customer portal by requiring that a user login and authenticate with a trusted 3rd party before they are given access to their SoftLayer account.  This is accomplished by creating an external binding for a specific vendor, in this case Time-based One Time Password.  When the SoftLayer user attempts to log in to the SoftLayer customer portal they will first be prompted for their normal SoftLayer username and password.  Once that information is verified they will be asked to generate and provide a security code from their Time-based One Time Password application. Once the security code has been authenticated the user will be allowed access to the SoftLayer customer portal. 

The time-based one time password external binding service allows a user to create an external binding, enable, disable, and delete an external binding. 

Once a SoftLayer user has a valid and active time-based one time password external binding, they will be required to always use their credential to login to the SoftLayer customer portal.  In addition any user with an active external binding will be prohibited from using the API. 



        
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

#### [activate](/reference/services/SoftLayer_User_Customer_External_Binding_Totp/activate)

</div>

<div class="method-row">

#### [deactivate](/reference/services/SoftLayer_User_Customer_External_Binding_Totp/deactivate)

</div>

<div class="method-row">

#### [deleteObject](/reference/services/SoftLayer_User_Customer_External_Binding_Totp/deleteObject)
Delete an external authentication binding.
</div>

<div class="method-row">

#### [disable](/reference/services/SoftLayer_User_Customer_External_Binding_Totp/disable)
Disable an external binding.
</div>

<div class="method-row">

#### [enable](/reference/services/SoftLayer_User_Customer_External_Binding_Totp/enable)
Enable an external binding.
</div>

<div class="method-row">

#### [generateSecretKey](/reference/services/SoftLayer_User_Customer_External_Binding_Totp/generateSecretKey)

</div>

<div class="method-row">

#### [getAttributes](/reference/services/SoftLayer_User_Customer_External_Binding_Totp/getAttributes)
Retrieve attributes of an external authentication binding.
</div>

<div class="method-row">

#### [getBillingItem](/reference/services/SoftLayer_User_Customer_External_Binding_Totp/getBillingItem)
Retrieve information regarding the billing item for external authentication.
</div>

<div class="method-row">

#### [getNote](/reference/services/SoftLayer_User_Customer_External_Binding_Totp/getNote)
Retrieve an optional note for identifying the external binding.
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_User_Customer_External_Binding_Totp/getObject)
Retrieve a SoftLayer_User_Customer_External_Binding_Totp record.
</div>

<div class="method-row">

#### [getType](/reference/services/SoftLayer_User_Customer_External_Binding_Totp/getType)
Retrieve the type of external authentication binding.
</div>

<div class="method-row">

#### [getUser](/reference/services/SoftLayer_User_Customer_External_Binding_Totp/getUser)
Retrieve the SoftLayer user that the external authentication binding belongs to.
</div>

<div class="method-row">

#### [getVendor](/reference/services/SoftLayer_User_Customer_External_Binding_Totp/getVendor)
Retrieve the vendor of an external authentication binding.
</div>

<div class="method-row">

#### [updateNote](/reference/services/SoftLayer_User_Customer_External_Binding_Totp/updateNote)
Update the note of an external binding.
</div>
</div>

</div>

