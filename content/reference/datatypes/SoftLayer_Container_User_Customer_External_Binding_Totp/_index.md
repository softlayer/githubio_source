---
title: "SoftLayer_Container_User_Customer_External_Binding_Totp"
description: "Container classed used to hold portal token"
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_User_Customer_External_Binding_Totp"
---

# SoftLayer_Container_User_Customer_External_Binding_Totp
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_User_Customer_External_Binding_Totp' >Datatype</a></li>
    </ul>
</div>

## Description 
Container classed used to hold portal token 





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
[authenticationToken]: #authenticationtoken
#### [authenticationToken]
The unique token that is created by an external authentication request.  
<span class="type-label">Type: </span>**string**

-----
[openIdConnectAccessToken]: #openidconnectaccesstoken
#### [openIdConnectAccessToken]
The OpenID Connect access token which provides access to a resource by the OpenID Connect provider.  
<span class="type-label">Type: </span>**string**

-----
[openIdConnectAccountId]: #openidconnectaccountid
#### [openIdConnectAccountId]
The account to login to, if not provided a default will be used.  
<span class="type-label">Type: </span>**integer**

-----
[openIdConnectProvider]: #openidconnectprovider
#### [openIdConnectProvider]
The OpenID Connect provider type, as a string.  
<span class="type-label">Type: </span>**string**

-----
[password]: #password
#### [password]
Your SoftLayer customer portal user's portal password.  
<span class="type-label">Type: </span>**string**

-----
[securityCode]: #securitycode
#### [securityCode]
The security code used to validate a Totp credential.  
<span class="type-label">Type: </span>**string**

-----
[securityQuestionAnswer]: #securityquestionanswer
#### [securityQuestionAnswer]
The answer to your security question.  
<span class="type-label">Type: </span>**string**

-----
[securityQuestionId]: #securityquestionid
#### [securityQuestionId]
A security question you wish to answer when authenticating to the SoftLayer customer portal. This parameter isn't required if no security questions are set on your portal account or if your account is configured to not require answering a security account upon login.  
<span class="type-label">Type: </span>**integer**

-----
[username]: #username
#### [username]
The username you wish to authenticate to the SoftLayer customer portal with.  
<span class="type-label">Type: </span>**string**

-----
[vendor]: #vendor
#### [vendor]
The name of the vendor that will be used for external authentication  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

</div>


