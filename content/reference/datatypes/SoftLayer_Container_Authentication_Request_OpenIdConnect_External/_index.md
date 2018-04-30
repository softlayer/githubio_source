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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#openIdConnectAccessToken" name=openIdConnectAccessToken>openIdConnectAccessToken</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#openIdConnectAccountId" name=openIdConnectAccountId>openIdConnectAccountId</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#openIdConnectProvider" name=openIdConnectProvider>openIdConnectProvider</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#securityQuestionAnswer" name=securityQuestionAnswer>securityQuestionAnswer</a>
            </span>
            <div class='views-field-body'>The answer to your security question. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#securityQuestionId" name=securityQuestionId>securityQuestionId</a>
            </span>
            <div class='views-field-body'>A security question you wish to answer when authenticating to the SoftLayer customer portal. This parameter isn't required if no security questions are set on your portal account or if your account is configured to not require answering a security account upon login. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
    </div>


