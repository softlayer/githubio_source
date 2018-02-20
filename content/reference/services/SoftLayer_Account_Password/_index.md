---
title: "SoftLayer_Account_Password"
description: "As a SoftLayer customer accumulates services they may accumulate usernames and passwords to those services. The SoftLaye... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Password"
---
# SoftLayer_Account_Password
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Password' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Password' >Datatype</a></li>
    </ul>
</div>

## Description
As a SoftLayer customer accumulates services they may accumulate usernames and passwords to those services. The SoftLayer_Account_Password data type stores a username and password combination for these services that are tied their customer account. This shouldn't be confused with username and password combinations for server-specific services. 

For instance, an account's EVault WebCC information is kept in a SoftLayer_Account_Password record, but a server's root or control panel password isn't. Server software specific usernames and passwords are handled by the SoftLayer_Hardware_Software_Password data type. 
        
        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_Password/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit the password and/or notes for an account password.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_Password/getAccount'> getAccount</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_Password/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Account_Password record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_Password/getType'> getType</a> </span>
            <div class='views-field-body'>Retrieve the service that an account/password combination is tied to.</div>
        </div>
        </div>
</div>

