---
title: "SoftLayer_Account_Lockdown_Request"
description: "This service allows approved brands the ability to disconnect, reconnect, and disable customer accounts under that brand... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Lockdown_Request"
---
# SoftLayer_Account_Lockdown_Request
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Lockdown_Request' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Lockdown_Request' >Datatype</a></li>
    </ul>
</div>

## Description
This service allows approved brands the ability to disconnect, reconnect, and disable customer accounts under that brand. Brand customers are able to make requests on their customers through an API call to this service. 

Disconnecting a customer will disable all hardware resources (servers and virtual machines) via a lockdown event. The customer will continue to have control portal access as well as access to their private ports. 

Reconnecting a customer will restore all previously disconnected public access. The original lockdown event will be closed. 

Disabling an account is a PERMANENT action. All billable items under the account will be canceled, access to the control portal, all resources, network access and hardware will be permanently disabled and reclaimed. 



        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_Lockdown_Request/cancelRequest'> cancelRequest</a> </span>
            <div class='views-field-body'>Allows approved brands to cancel a previously scheduled lockdown request.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_Lockdown_Request/disableLockedAccount'> disableLockedAccount</a> </span>
            <div class='views-field-body'>Disabling an account is a PERMANENT action. All billable items associated</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_Lockdown_Request/disconnectCompute'> disconnectCompute</a> </span>
            <div class='views-field-body'>Disconnecting a customer will disable all hardware resources (servers and</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_Lockdown_Request/getAccountHistory'> getAccountHistory</a> </span>
            <div class='views-field-body'>Provides a history of an account's lockdown requests and their status.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_Lockdown_Request/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Account_Lockdown_Request record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_Lockdown_Request/reconnectCompute'> reconnectCompute</a> </span>
            <div class='views-field-body'>Reconnecting a customer will reconnect all previously disconnected</div>
        </div>
        </div>
</div>

