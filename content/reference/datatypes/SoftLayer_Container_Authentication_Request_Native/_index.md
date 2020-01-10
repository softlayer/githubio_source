---
title: "SoftLayer_Container_Authentication_Request_Native"
description: "The SoftLayer_Container_Authentication_Request_Native data type contains information for requests to the getPortalLogin... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Authentication_Request_Native"
---

# SoftLayer_Container_Authentication_Request_Native
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Authentication_Request_Native' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_Authentication_Request_Native data type contains information for requests to the getPortalLogin API. This class is specific to the SoftLayer Native login (username/password). The request information will be verified to ensure it is valid, and then there will be an attempt to obtain a portal login token in authenticating the user with the provided information. 





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
[auxiliaryClaimsMiniToken]: #auxiliaryclaimsminitoken
#### [auxiliaryClaimsMiniToken]
  
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
</div>
<!-- LOCAL PROPERTY END -->

</div>


