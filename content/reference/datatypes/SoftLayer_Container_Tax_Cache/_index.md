---
title: "SoftLayer_Container_Tax_Cache"
description: "These are the results of a tax calculation. The tax calculation was kicked off but allowed to run in the background. Thi... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Tax_Cache"
---

# SoftLayer_Container_Tax_Cache
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Tax_Cache' >Datatype</a></li>
    </ul>
</div>

## Description 
These are the results of a tax calculation. The tax calculation was kicked off but allowed to run in the background. This type stores the results so that an interface can be updated with up-to-date information. 





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
[effectiveTaxRate]: #effectivetaxrate
#### [effectiveTaxRate]
The percentage of the final total that should be tax.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[failureMessage]: #failuremessage
#### [failureMessage]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[items]: #items
#### [items]
The container that holds the four actual tax rates, one for each fee type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Tax_Cache_Item'>SoftLayer_Container_Tax_Cache_Item[] </a>**


</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
The status of the tax request. This should be PENDING, FAILED, or COMPLETED.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[totalTaxAmount]: #totaltaxamount
#### [totalTaxAmount]
The final amount of tax for the order.  
<span class="type-label">Type: </span>**decimal**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


