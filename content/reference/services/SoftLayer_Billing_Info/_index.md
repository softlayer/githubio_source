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



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [getAccount](/reference/services/SoftLayer_Billing_Info/getAccount)
Retrieve the SoftLayer customer account associated with this billing information.

#### [getAchInformation](/reference/services/SoftLayer_Billing_Info/getAchInformation)


#### [getCurrency](/reference/services/SoftLayer_Billing_Info/getCurrency)
Retrieve currency to be used by this customer account.

#### [getCurrentBillingCycle](/reference/services/SoftLayer_Billing_Info/getCurrentBillingCycle)
Retrieve information related to an account's current and previous billing cycles.

#### [getLastBillDate](/reference/services/SoftLayer_Billing_Info/getLastBillDate)
Retrieve the date on which an account was last billed.

#### [getNextBillDate](/reference/services/SoftLayer_Billing_Info/getNextBillDate)
Retrieve the date on which an account will be billed next.

#### [getObject](/reference/services/SoftLayer_Billing_Info/getObject)
Retrieve a SoftLayer_Billing_Info record.

</div>

