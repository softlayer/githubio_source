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
            <span class='views-field-title'><a href="#authenticationToken" name=authenticationToken>authenticationToken</a></span>
            <div class='views-field-body'>The unique token that is created by an external authentication request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#openIdConnectAccessToken" name=openIdConnectAccessToken>openIdConnectAccessToken</a></span>
            <div class='views-field-body'>The OpenID Connect access token which provides access to a resource by the OpenID Connect provider. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#openIdConnectAccountId" name=openIdConnectAccountId>openIdConnectAccountId</a></span>
            <div class='views-field-body'>The account to login to, if not provided a default will be used. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#openIdConnectProvider" name=openIdConnectProvider>openIdConnectProvider</a></span>
            <div class='views-field-body'>The OpenID Connect provider type, as a string. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#password" name=password>password</a></span>
            <div class='views-field-body'>Your SoftLayer customer portal user's portal password. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#securityQuestionAnswer" name=securityQuestionAnswer>securityQuestionAnswer</a></span>
            <div class='views-field-body'>The answer to your security question. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#securityQuestionId" name=securityQuestionId>securityQuestionId</a></span>
            <div class='views-field-body'>A security question you wish to answer when authenticating to the SoftLayer customer portal. This parameter isn't required if no security questions are set on your portal account or if your account is configured to not require answering a security account upon login. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#username" name=username>username</a></span>
            <div class='views-field-body'>The username you wish to authenticate to the SoftLayer customer portal with. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#vendor" name=vendor>vendor</a></span>
            <div class='views-field-body'>The name of the vendor that will be used for external authentication </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
    </div>


