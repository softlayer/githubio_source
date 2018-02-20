---
title: "SoftLayer_User_Customer_Access_Authentication"
description: "SoftLayer_User_Customer_Access_Authentication models a single attempt to log into the SoftLayer customer portal. A SoftL... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Access_Authentication"
---

# SoftLayer_User_Customer_Access_Authentication
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_Access_Authentication' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_User_Customer_Access_Authentication models a single attempt to log into the SoftLayer customer portal. A SoftLayer_User_Customer_Access_Authentication record is created every time a user attempts to log into the portal. Use this service to audit your users' portal activity and diagnose potential security breaches of your SoftLayer portal accounts. 

Unsuccessful login attempts can be caused by an incorrect password, failing to answer or not answering a login security question if the user has them configured, or attempting to log in from an IP address outside of the user's IP address restriction list. 

SoftLayer employees periodically log into our customer portal as users to diagnose portal issues, verify settings and configuration, and to perform maintenance on your account or services. SoftLayer employees only log into customer accounts from the following IP ranges: 
* 2607:f0d0:1000::/48
* 2607:f0d0:2000::/48
* 2607:f0d0:3000::/48
* 66.228.118.67/32
* 66.228.118.86/32
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
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The date of an attempt to log into the SoftLayer customer portal. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ipAddress" name=ipAddress>ipAddress</a></span>
            <div class='views-field-body'>The IP address of the user who attempted to log into the SoftLayer customer portal. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#successFlag" name=successFlag>successFlag</a></span>
            <div class='views-field-body'>Whether an attempt to log into the SoftLayer customer portal was successful or not. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#userId" name=userId>userId</a></span>
            <div class='views-field-body'>The internal identifier of the user who attempted to log into the SoftLayer customer portal. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#username" name=username>username</a></span>
            <div class='views-field-body'>The username used when attempting to log into the SoftLayer customer portal </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#user" name=user>user</a></span>
            <div class='views-field-body'>The user who has attempted to log into the SoftLayer customer portal. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a></p></div>
        </div>
            </div>
</div>


