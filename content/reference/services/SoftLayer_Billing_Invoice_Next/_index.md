---
title: "SoftLayer_Billing_Invoice_Next"
description: "Service for an account's next invoice. The 'next invoice' is what a customer will be billed on their next invoice, assum... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice_Next"
---
# SoftLayer_Billing_Invoice_Next
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Billing_Invoice_Next' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Invoice_Next' >Datatype</a></li>
    </ul>
</div>

## Description


Service for an account's next invoice. The "next invoice" is what a customer will be billed on their next invoice, assuming no changes are made. Currently this does not include Bandwidth Pooling charges. Note, this should be considered preliminary as you may add, remove, or change billing items on your account. 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [getExcel](/reference/services/SoftLayer_Billing_Invoice_Next/getExcel)
Retrieve the next billing period's invoice as an Excel.

</div>

<div class="method-row">

#### [getPdf](/reference/services/SoftLayer_Billing_Invoice_Next/getPdf)
Retrieve the next billing period's invoice as a PDF.

</div>

<div class="method-row">

#### [getPdfDetailed](/reference/services/SoftLayer_Billing_Invoice_Next/getPdfDetailed)
Retrieve the next billing period's detailed invoice as a PDF.

</div>
</div>

</div>

