---
title: "SoftLayer_Network_CdnMarketplace_Account"
description: "The SoftLayer_Network_CdnMarketplace_Account service allows customers to create, and delete CDN accounts. A SoftLayer_Ne... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Account"
---
# SoftLayer_Network_CdnMarketplace_Account
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_CdnMarketplace_Account' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_CdnMarketplace_Account' >Datatype</a></li>
    </ul>
</div>

## Description
The SoftLayer_Network_CdnMarketplace_Account service allows customers to create, and delete CDN accounts. A SoftLayer_Network_CdnMarketplace_Account record is created when the customer configures a CDN account for the first time. A customer will be able to create multiple CDN accounts, but each account will be bound to a single vendor. 



        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_CdnMarketplace_Account/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve softLayer account to which the CDN account belongs.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_CdnMarketplace_Account/getBillingItem'> getBillingItem</a> </span>
            <div class='views-field-body'>Retrieve an associated parent billing item which is active.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_CdnMarketplace_Account/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_CdnMarketplace_Account record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_CdnMarketplace_Account/verifyCdnAccountExists'> verifyCdnAccountExists</a> </span>
            <div class='views-field-body'>Wrapper for UI to verify whether or not an account exists for user under specified vendor. Returns true if account exists, else false. </div>
        </div>
        </div>
</div>

