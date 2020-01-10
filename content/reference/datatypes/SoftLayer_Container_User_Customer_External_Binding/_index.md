---
title: "SoftLayer_Container_User_Customer_External_Binding"
description: "Container classed used to hold external authentication information"
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_User_Customer_External_Binding"
---

# SoftLayer_Container_User_Customer_External_Binding
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_User_Customer_External_Binding' >Datatype</a></li>
    </ul>
</div>

## Description 
Container classed used to hold external authentication information 





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
[authenticationToken]: #authenticationtoken
#### [authenticationToken]
The unique token that is created by an external authentication request.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[openIdConnectAccessToken]: #openidconnectaccesstoken
#### [openIdConnectAccessToken]
The OpenID Connect access token which provides access to a resource by the OpenID Connect provider.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[openIdConnectAccountId]: #openidconnectaccountid
#### [openIdConnectAccountId]
The account to login to, if not provided a default will be used.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[openIdConnectProvider]: #openidconnectprovider
#### [openIdConnectProvider]
The OpenID Connect provider type, as a string.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[password]: #password
#### [password]
Your SoftLayer customer portal user's portal password.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[securityQuestionAnswer]: #securityquestionanswer
#### [securityQuestionAnswer]
The answer to your security question.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[securityQuestionId]: #securityquestionid
#### [securityQuestionId]
A security question you wish to answer when authenticating to the SoftLayer customer portal. This parameter isn't required if no security questions are set on your portal account or if your account is configured to not require answering a security account upon login.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[username]: #username
#### [username]
The username you wish to authenticate to the SoftLayer customer portal with.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[vendor]: #vendor
#### [vendor]
The name of the vendor that will be used for external authentication  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


