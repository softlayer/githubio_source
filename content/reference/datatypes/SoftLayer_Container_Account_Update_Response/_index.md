---
title: "SoftLayer_Container_Account_Update_Response"
description: "Contains data related to an account after editing its information."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Account_Update_Response"
---

# SoftLayer_Container_Account_Update_Response
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Account_Update_Response' >Datatype</a></li>
    </ul>
</div>

## Description 
Contains data related to an account after editing its information. 


### associatedMethods

*  [SoftLayer_Account::editAccount](/reference/services/SoftLayer_Account/editAccount )





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
[acceptedFlag]: #acceptedflag
#### [acceptedFlag]
Whether or not the update was accepted and applied.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[account]: #account
#### [account]
The updated SoftLayer_Account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[ticket]: #ticket
#### [ticket]
If a manual review is required, this will be populated with the SoftLayer_Ticket for that review.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


