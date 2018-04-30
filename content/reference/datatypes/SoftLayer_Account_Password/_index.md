---
title: "SoftLayer_Account_Password"
description: "The SoftLayer_Account_Password contains username, passwords and notes for services that may require for external applica... "
layout: "datatype"
tags:
    - "datatype"
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
The SoftLayer_Account_Password contains username, passwords and notes for services that may require for external applications such the Webcc interface for the EVault Storage service. 


### associatedMethods

*  [SoftLayer_Account::getEvaultMasterUser](/reference/services/SoftLayer_Account/getEvaultMasterUser )



### seeAlso

* [SoftLayer_Software_Password](/reference/datatypes/SoftLayer_Software_Password )




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
                <a href="#accountId" name=accountId>accountId</a>
            </span>
            <div class='views-field-body'>The SoftLayer customer account id that a username/password combination is associated with. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>A username/password combination's internal identifier. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#notes" name=notes>notes</a>
            </span>
            <div class='views-field-body'>A simple description of a username/password combination. These notes don't affect portal functionality. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#password" name=password>password</a>
            </span>
            <div class='views-field-body'>The password portion of a username/password combination. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#typeId" name=typeId>typeId</a>
            </span>
            <div class='views-field-body'>An identifier relating to a username/password combinations's associated service. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#username" name=username>username</a>
            </span>
            <div class='views-field-body'>The username portion of a username/password combination. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#account" name=account>account</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#type" name=type>type</a>
            </span>
            <div class='views-field-body'>The service that an account/password combination is tied to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account_Password_Type'>SoftLayer_Account_Password_Type </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


