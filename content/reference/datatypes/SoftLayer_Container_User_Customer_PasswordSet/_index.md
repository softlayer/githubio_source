---
title: "SoftLayer_Container_User_Customer_PasswordSet"
description: "Container for holding information necessary for the setting and resetting of customer passwords"
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_User_Customer_PasswordSet"
---

# SoftLayer_Container_User_Customer_PasswordSet
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_User_Customer_PasswordSet' >Datatype</a></li>
    </ul>
</div>

## Description 
Container for holding information necessary for the setting and resetting of customer passwords 





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
                <a href="#answeredSecurityQuestionId" name=answeredSecurityQuestionId>answeredSecurityQuestionId</a>
            </span>
            <div class='views-field-body'>Id of SoftLayer_User_Security_Question. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#authenticationMethods" name=authenticationMethods>authenticationMethods</a>
            </span>
            <div class='views-field-body'>The authentication methods required. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>array of integers</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#digitCountRequirement" name=digitCountRequirement>digitCountRequirement</a>
            </span>
            <div class='views-field-body'>The number of digits required. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#key" name=key>key</a>
            </span>
            <div class='views-field-body'>The password key provided to user in the password set url link sent via email.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#lowercaseCountRequirement" name=lowercaseCountRequirement>lowercaseCountRequirement</a>
            </span>
            <div class='views-field-body'>The number of lowercase letters required. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#maximumPasswordLengthRequirement" name=maximumPasswordLengthRequirement>maximumPasswordLengthRequirement</a>
            </span>
            <div class='views-field-body'>The maximum password length requirement. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#minimumPasswordLengthRequirement" name=minimumPasswordLengthRequirement>minimumPasswordLengthRequirement</a>
            </span>
            <div class='views-field-body'>The minimum password length requirement. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#password" name=password>password</a>
            </span>
            <div class='views-field-body'>The user's new password. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#securityAnswer" name=securityAnswer>securityAnswer</a>
            </span>
            <div class='views-field-body'>Answer to security question provided by the user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#securityQuestions" name=securityQuestions>securityQuestions</a>
            </span>
            <div class='views-field-body'>Array of SoftLayer_User_Security_Question. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Security_Question'>SoftLayer_User_Security_Question[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#specialCharacterCountRequirement" name=specialCharacterCountRequirement>specialCharacterCountRequirement</a>
            </span>
            <div class='views-field-body'>The number of special characters required. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#specialCharactersAllowed" name=specialCharactersAllowed>specialCharactersAllowed</a>
            </span>
            <div class='views-field-body'>List of the allowed special characters. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#uppercaseCountRequirement" name=uppercaseCountRequirement>uppercaseCountRequirement</a>
            </span>
            <div class='views-field-body'>The number of uppercase letters required. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#userId" name=userId>userId</a>
            </span>
            <div class='views-field-body'>The id of the user to authenticate. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
    </div>


