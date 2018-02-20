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
        
        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/checkPhoneValidationResult'> checkPhoneValidationResult</a> </span>
            <div class='views-field-body'>Return a phone validation result</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/deleteObject'> deleteObject</a> </span>
            <div class='views-field-body'>Delete an external authentication binding.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/disable'> disable</a> </span>
            <div class='views-field-body'>Disable an external binding.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/enable'> enable</a> </span>
            <div class='views-field-body'>Enable an external binding.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getAllAuthenticationModes'> getAllAuthenticationModes</a> </span>
            <div class='views-field-body'>Returns available authentication modes</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getAllAuthenticationPinModes'> getAllAuthenticationPinModes</a> </span>
            <div class='views-field-body'>Returns available authentication pin modes</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getAttributes'> getAttributes</a> </span>
            <div class='views-field-body'>Retrieve attributes of an external authentication binding.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getAuthenticationMode'> getAuthenticationMode</a> </span>
            <div class='views-field-body'>Returns the authentication mode</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getBillingItem'> getBillingItem</a> </span>
            <div class='views-field-body'>Retrieve the current billing item for an external binding.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getBindingStatus'> getBindingStatus</a> </span>
            <div class='views-field-body'>Retrieve the current external binding status. It can be "ACTIVE" or "BLOCKED".</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getNote'> getNote</a> </span>
            <div class='views-field-body'>Retrieve an optional note for identifying the external binding.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_User_Customer_External_Binding_Phone record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getPhoneAppActivationCode'> getPhoneAppActivationCode</a> </span>
            <div class='views-field-body'>Return a mobile phone app activation code</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getPhoneData'> getPhoneData</a> </span>
            <div class='views-field-body'>Returns the authentication phone data.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getPinLength'> getPinLength</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getType'> getType</a> </span>
            <div class='views-field-body'>Retrieve the type of external authentication binding.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getUser'> getUser</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer user that the external authentication binding belongs to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/getVendor'> getVendor</a> </span>
            <div class='views-field-body'>Retrieve the vendor of an external authentication binding.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/requestPhoneValidation'> requestPhoneValidation</a> </span>
            <div class='views-field-body'>Initiates a phone validation requests and returns a unique token</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/updateAuthenticationMode'> updateAuthenticationMode</a> </span>
            <div class='views-field-body'>Updates the authentication mode</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/updateNote'> updateNote</a> </span>
            <div class='views-field-body'>Update the note of an external binding.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone/updatePhone'> updatePhone</a> </span>
            <div class='views-field-body'>Updates the authentication phone numbers.</div>
        </div>
        </div>
</div>

