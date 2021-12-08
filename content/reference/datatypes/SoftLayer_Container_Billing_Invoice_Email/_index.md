---
title: "SoftLayer_Container_Billing_Invoice_Email"
description: "This container is used to provide all the options for [SoftLayer_Billing_Invoice::emailInvoices]({{<ref 'reference/servi... "
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


This container is used to provide all the options for [SoftLayer_Billing_Invoice::emailInvoices]({{<ref "reference/services/SoftLayer_Billing_Invoice/emailInvoices">}}) in order to have the necessary invoices generated and links sent to the user's email. 





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[excelInvoiceIds]: #excelinvoiceids
#### [excelInvoiceIds]
Excel Invoices to email  
<span class="type-label">Type: </span>**array of integers**  



</div>
<div class="prop-row">

-----
[pdfDetailedInvoiceIds]: #pdfdetailedinvoiceids
#### [pdfDetailedInvoiceIds]
PDF Invoice Details to email  
<span class="type-label">Type: </span>**array of integers**  



</div>
<div class="prop-row">

-----
[pdfInvoiceIds]: #pdfinvoiceids
#### [pdfInvoiceIds]
PDF Invoices to email  
<span class="type-label">Type: </span>**array of integers**  



</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The type of Invoices to be emailed [current|next]. If next is selected, the account id will be used.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


