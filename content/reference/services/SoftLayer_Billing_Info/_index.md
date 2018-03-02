---
title: "SoftLayer_Billing_Info"
description: "SoftLayer billing info contains company billing information such as the last date a payment was made and the last time a... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Info"
---
# SoftLayer_Billing_Info
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Billing_Info' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Info' >Datatype</a></li>
    </ul>
</div>

## Description
SoftLayer billing info contains company billing information such as the last date a payment was made and the last time any billing information was update. Use the data returned by these methods with other API services to get more detailed information about your billing information. 

Due to the sensitivity of your billing information we don't allow changing this data through the API. Please open a sales ticket in our customer portal if you need to change this information. 



        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Info/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer customer account associated with this billing information.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Info/getAchInformation'> getAchInformation</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Info/getCurrency'> getCurrency</a> </span>
            <div class='views-field-body'>Retrieve currency to be used by this customer account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Info/getCurrentBillingCycle'> getCurrentBillingCycle</a> </span>
            <div class='views-field-body'>Retrieve information related to an account's current and previous billing cycles.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Info/getLastBillDate'> getLastBillDate</a> </span>
            <div class='views-field-body'>Retrieve the date on which an account was last billed.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Info/getNextBillDate'> getNextBillDate</a> </span>
            <div class='views-field-body'>Retrieve the date on which an account will be billed next.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Info/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Billing_Info record.</div>
        </div>
        </div>
</div>

