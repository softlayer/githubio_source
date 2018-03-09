---
title: "SoftLayer_Container_User_Customer_External_Binding_Phone_Mode"
description: "This container can be used to configure the phone authentication mode. By default, 'VOICE_CALL' in 'STANDARD' mode with... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_User_Customer_External_Binding_Phone_Mode"
---

# SoftLayer_Container_User_Customer_External_Binding_Phone_Mode
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_User_Customer_External_Binding_Phone_Mode' >Datatype</a></li>
    </ul>
</div>

## Description 
This container can be used to configure the phone authentication mode. By default, "VOICE_CALL" in "STANDARD" mode with no Pin number will be used. With the default mode, you will have to answer a phone call from a trusted 2 form factor vendor during authentication process. You have to answer the call and follow the instruction in order to complete the authentication. 

You can also use SMS text message or PhoneFactor mobile app modes (in case you're using PhoneFactor). Additionally, you can set up a Pin number. By requiring you to verify your secret PIN, you can ensure that you have possession of your phone. 





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
                <a href="#mode" name=mode>mode</a>
            </span>
            <div class='views-field-body'>Authentication mode. Valid modes are: VOICE_CALL, SMS_TEXT, PHONE_APP 


*VOICE_CALL
In this mode, users will receive a phone call to authenticate. Using PIN can enhance the security of the phone authentication by requiring the user to enter a PIN during the authentication call. Valid Pin modes are: PIN, VOICE_PRINT, STANDARD 


**STANDARD: (default) No PIN is used.
**PIN: 4 to 10 digit numeric value
**VOICE_PRINT: The user's voice will be used to identify the user.


*SMS_TEXT
SMS Text mode will send a SMS text message to the user's phone to complete the authentication.  There are 2 different pin modes: 


**OTP: (default) A text message containing a One-Time Passcode (OTP) is sent to the user. The user must reply to the text message entering this OTP to complete the authentication.
**OTP_PIN: This mode enhances the security of the authentication by requiring the user to enter the OTP + their PIN in the text reply.




*PHONE_APP
This mode is applicable for PhoneFactor. Phone App mode results in a notification being sent to the user's PhoneFactor phone app. There are 2 different pin modes for the mobile app authentication. 
**STANDARD: (default) The first authentication is when the user signs on using a username and password.
The second authentication is when the user receives a notification in the PhoneFactor phone app. In Standard Mode, users will prompted to authenticate, deny, or deny and report fraud. 
**PIN: This mode enhances the security of the authentication by requiring the user to enter their PIN in the phone app. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#pin" name=pin>pin</a>
            </span>
            <div class='views-field-body'>Optional authentication pin. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#pinMode" name=pinMode>pinMode</a>
            </span>
            <div class='views-field-body'>Available Pin modes are: PIN, VOICE_PRINT, STANDARD Default: STANDARD (Pin is not used)  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
    </div>


