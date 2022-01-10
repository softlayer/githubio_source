---
title: "SoftLayer_Network_SecurityGroup"
description: "The SoftLayer_Network_SecurityGroup data type contains general information for a single security group. A security group... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_SecurityGroup"
---

# SoftLayer_Network_SecurityGroup
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_SecurityGroup' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_SecurityGroup' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Network_SecurityGroup data type contains general information for a single security group. A security group contains a set of IP filter [SoftLayer_Network_SecurityGroup_Rule]({{<ref "reference/datatypes/SoftLayer_Network_SecurityGroup_Rule">}}) to associate virtual guest network components with the security group. 





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
[createDate]: #createdate
#### [createDate]
The date a security group was created.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
The (optional) description for a security group.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The unique ID for a security group.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[metadata]: #metadata
#### [metadata]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a security group was last modified.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The (optional) name for a security group.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account this security group belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[networkComponentBindings]: #networkcomponentbindings
#### [networkComponentBindings]
The network component bindings for this security group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding'>SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding[] </a>**  



</div>
<div class="prop-row">

-----
[orderBindings]: #orderbindings
#### [orderBindings]
The order bindings for this security group  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_SecurityGroup_OrderBinding'>SoftLayer_Network_SecurityGroup_OrderBinding[] </a>**  



</div>
<div class="prop-row">

-----
[rules]: #rules
#### [rules]
The rules for this security group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_SecurityGroup_Rule'>SoftLayer_Network_SecurityGroup_Rule[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[networkComponentBindingCount]: #networkcomponentbindingcount
#### [networkComponentBindingCount]
A count of the network component bindings for this security group.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[orderBindingCount]: #orderbindingcount
#### [orderBindingCount]
A count of the order bindings for this security group   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[ruleCount]: #rulecount
#### [ruleCount]
A count of the rules for this security group.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


