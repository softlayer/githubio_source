---
title: "SoftLayer_Container_Authentication_Request_OpenIdConnect_External_Verisign"
description: "The SoftLayer_Container_Authentication_Request_OpenIdConnect_External_Verisign data type contains information for reques... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Authentication_Request_OpenIdConnect_External_Verisign"
---

# SoftLayer_Container_Authentication_Request_OpenIdConnect_External_Verisign
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Authentication_Request_OpenIdConnect_External_Verisign' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Container_Authentication_Request_OpenIdConnect_External_Verisign data type contains information for requests to the getPortalLogin API. This class provides information to allow the user to submit a request to the SoftLayer OpenIdConnect (token) login service for a portal login token, as well as submitting a request to the Verisign 2 factor authentication service. 





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
[openIdConnectAccessToken]: #openidconnectaccesstoken
#### [openIdConnectAccessToken]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[openIdConnectAccountId]: #openidconnectaccountid
#### [openIdConnectAccountId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[openIdConnectProvider]: #openidconnectprovider
#### [openIdConnectProvider]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[secondSecurityCode]: #secondsecuritycode
#### [secondSecurityCode]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[securityCode]: #securitycode
#### [securityCode]
  
<span class="type-label">Type: </span>**integer**  



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
[vendor]: #vendor
#### [vendor]
  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


