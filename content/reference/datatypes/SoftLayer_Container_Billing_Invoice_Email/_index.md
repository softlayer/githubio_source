---
title: "SoftLayer_Container_Billing_Invoice_Email"
description: "This container is used to provide all the options for [[SoftLayer_Billing_Invoice/emailInvoices|emailInvoices]] in order... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Billing_Invoice_Email"
---

# SoftLayer_Container_Billing_Invoice_Email
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Billing_Invoice_Email' >Datatype</a></li>
    </ul>
</div>

## Description 
This container is used to provide all the options for [[SoftLayer_Billing_Invoice/emailInvoices|emailInvoices]] in order to have the necessary invoices generated and links sent to the user's email. 





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
                <a href="#excelInvoiceIds" name=excelInvoiceIds>excelInvoiceIds</a>
            </span>
            <div class='views-field-body'>Excel Invoices to email </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>array of integers</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#pdfDetailedInvoiceIds" name=pdfDetailedInvoiceIds>pdfDetailedInvoiceIds</a>
            </span>
            <div class='views-field-body'>PDF Invoice Details to email </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>array of integers</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#pdfInvoiceIds" name=pdfInvoiceIds>pdfInvoiceIds</a>
            </span>
            <div class='views-field-body'>PDF Invoices to email </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>array of integers</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#type" name=type>type</a>
            </span>
            <div class='views-field-body'>The type of Invoices to be emailed [current|next]. If next is selected, the account id will be used. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
    </div>


