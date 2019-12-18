---
title: "SoftLayer_User_Customer_External_Binding_Verisign"
description: "SoftLayer provides its customers the ability to add an additional layer of security to the SoftLayer customer portal by... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_External_Binding_Verisign"
---
# SoftLayer_User_Customer_External_Binding_Verisign
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_User_Customer_External_Binding_Verisign' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_External_Binding_Verisign' >Datatype</a></li>
    </ul>
</div>

## Description
SoftLayer provides its customers the ability to add an additional layer of security to the SoftLayer customer portal by requiring that a user login and authenticate with a trusted 3rd party before they are given access to their SoftLayer account.  This is accomplished by creating an external binding for a specific vendor, in this case VeriSign.  When the SoftLayer user attempts to log in to the SoftLayer customer portal they will first be prompted for their normal SoftLayer username and password.  Once that information is verified they will be asked to generate and provide a security code from their VeriSign credential. Once the security code has been authenticated with VeriSign the user will be allowed access to the SoftLayer customer portal. 

The VeriSign external binding service allows a user to create an external binding, enable, disable, or unlock an external binding, and delete an external binding. Currently SoftLayer provides the master account user of a SoftLayer account with one free VeriSign external binding. All subsequent VeriSign external bindings will need to be created by placing an order. 

Once a SoftLayer user has a valid and active VeriSign external binding, they will be required to always use their credential to login to the SoftLayer customer portal.  In addition any user with an active external binding will be prohibited from using the API. 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [deleteObject](/reference/services/SoftLayer_User_Customer_External_Binding_Verisign/deleteObject)
Delete a VeriSign external binding.

#### [disable](/reference/services/SoftLayer_User_Customer_External_Binding_Verisign/disable)
Disable an external binding.

#### [enable](/reference/services/SoftLayer_User_Customer_External_Binding_Verisign/enable)
Enable an external binding.

#### [getActivationCodeForMobileClient](/reference/services/SoftLayer_User_Customer_External_Binding_Verisign/getActivationCodeForMobileClient)
Get an activation code that is used for provisioning a mobile credential.

#### [getAttributes](/reference/services/SoftLayer_User_Customer_External_Binding_Verisign/getAttributes)
Retrieve attributes of an external authentication binding.

#### [getBillingItem](/reference/services/SoftLayer_User_Customer_External_Binding_Verisign/getBillingItem)
Retrieve the current billing item for an external binding.

#### [getCredentialExpirationDate](/reference/services/SoftLayer_User_Customer_External_Binding_Verisign/getCredentialExpirationDate)
Retrieve the date that a VeriSign credential expires.

#### [getCredentialLastUpdateDate](/reference/services/SoftLayer_User_Customer_External_Binding_Verisign/getCredentialLastUpdateDate)
Retrieve the last time a VeriSign credential was updated.

#### [getCredentialState](/reference/services/SoftLayer_User_Customer_External_Binding_Verisign/getCredentialState)
Retrieve the current state of a VeriSign credential. This can be 'Enabled', 'Disabled', or 'Locked'.

#### [getCredentialType](/reference/services/SoftLayer_User_Customer_External_Binding_Verisign/getCredentialType)
Retrieve the type of VeriSign credential. This can be either 'Hardware' or 'Software'.

#### [getNote](/reference/services/SoftLayer_User_Customer_External_Binding_Verisign/getNote)
Retrieve an optional note for identifying the external binding.

#### [getObject](/reference/services/SoftLayer_User_Customer_External_Binding_Verisign/getObject)
Retrieve a SoftLayer_User_Customer_External_Binding_Verisign record.

#### [getType](/reference/services/SoftLayer_User_Customer_External_Binding_Verisign/getType)
Retrieve the type of external authentication binding.

#### [getUser](/reference/services/SoftLayer_User_Customer_External_Binding_Verisign/getUser)
Retrieve the SoftLayer user that the external authentication binding belongs to.

#### [getVendor](/reference/services/SoftLayer_User_Customer_External_Binding_Verisign/getVendor)
Retrieve the vendor of an external authentication binding.

#### [unlock](/reference/services/SoftLayer_User_Customer_External_Binding_Verisign/unlock)


#### [updateNote](/reference/services/SoftLayer_User_Customer_External_Binding_Verisign/updateNote)
Update the note of an external binding.

#### [validateCredentialId](/reference/services/SoftLayer_User_Customer_External_Binding_Verisign/validateCredentialId)
Validate a VeriSign credential id.

</div>

