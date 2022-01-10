---
title: "SoftLayer_Provisioning_Version1_Transaction_Status"
description: "The SoftLayer_Provisioning_Version1_Transaction_Status data type contains general information relating to a single SoftL... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Provisioning"
classes:
    - "SoftLayer_Provisioning_Version1_Transaction_Status"
---

# SoftLayer_Provisioning_Version1_Transaction_Status
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction_Status' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Provisioning_Version1_Transaction_Status data type contains general information relating to a single SoftLayer hardware transaction status. 

SoftLayer customers are unable to change their hardware transaction status. 


### associatedMethods

*  [SoftLayer_Provisioning_Version1_Transaction_Status::getObject](/reference/services/SoftLayer_Provisioning_Version1_Transaction_Status/getObject )





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
[averageDuration]: #averageduration
#### [averageDuration]
Hardware transaction status average duration.  
<span class="type-label">Type: </span>**decimal**  



</div>
<div class="prop-row">

-----
[friendlyName]: #friendlyname
#### [friendlyName]
Transaction status friendly name.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
Transaction status name.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[nonCompletedTransactions]: #noncompletedtransactions
#### [nonCompletedTransactions]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[nonCompletedTransactionCount]: #noncompletedtransactioncount
#### [nonCompletedTransactionCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


