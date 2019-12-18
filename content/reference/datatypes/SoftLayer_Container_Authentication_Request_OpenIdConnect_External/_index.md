---
title: "SoftLayer_Container_Authentication_Request_OpenIdConnect_External"
description: "The SoftLayer_Container_Authentication_Request_OpenIdConnect_External data type contains information for requests to the... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Authentication_Request_OpenIdConnect_External"
---

# SoftLayer_Container_Authentication_Request_OpenIdConnect_External
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Authentication_Request_OpenIdConnect_External' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_Authentication_Request_OpenIdConnect_External data type contains information for requests to the getPortalLogin API. This class serves as a base class for more specialized external authentication classes to the SoftLayer OpenIdConnect login service. 





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
[openIdConnectAccessToken]: #openidconnectaccesstoken
#### [openIdConnectAccessToken]
  
<span class="type-label">Type: </span>**string**

-----
[openIdConnectAccountId]: #openidconnectaccountid
#### [openIdConnectAccountId]
  
<span class="type-label">Type: </span>**integer**

-----
[openIdConnectProvider]: #openidconnectprovider
#### [openIdConnectProvider]
  
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

</div>
<!-- LOCAL PROPERTY END -->

</div>


