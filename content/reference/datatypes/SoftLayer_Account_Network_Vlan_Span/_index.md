---
title: "SoftLayer_Account_Network_Vlan_Span"
description: "The SoftLayer_Account_Network_Vlan_Span data type exposes the setting which controls the automatic spanning of private V... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Network_Vlan_Span"
---

# SoftLayer_Account_Network_Vlan_Span
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Network_Vlan_Span' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Account_Network_Vlan_Span data type exposes the setting which controls the automatic spanning of private VLANs attached to a given customers account. 


### associatedMethods

*  [SoftLayer_Account::setVlanSpan](/reference/services/SoftLayer_Account/setVlanSpan )





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
[enabledFlag]: #enabledflag
#### [enabledFlag]
Flag indicating whether the customer wishes to have all private network VLANs associated with account automatically joined [0 or 1]  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The unique internal identifier of the SoftLayer_Account_Network_Vlan_Span object.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[lastAppliedDate]: #lastapplieddate
#### [lastAppliedDate]
Timestamp of the last time the ACL for this account was applied.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[lastVerifiedDate]: #lastverifieddate
#### [lastVerifiedDate]
Timestamp of the last time the subnet hash was verified for this VLAN span record.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
Timestamp of the last edit of the record.  
<span class="type-label">Type: </span>**dateTime**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The SoftLayer customer account associated with a VLAN.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>

## Count
</div>


