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

## Local
-----
[createDate]: #createdate
#### [createDate]
The date a security group was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[description]: #description
#### [description]
The (optional) description for a security group.  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
The unique ID for a security group.  
<span class="type-label">Type: </span>**integer**

-----
[metadata]: #metadata
#### [metadata]
  
<span class="type-label">Type: </span>**string**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a security group was last modified.  
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
The (optional) name for a security group.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The account this security group belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[networkComponentBindings]: #networkcomponentbindings
#### [networkComponentBindings]
The network component bindings for this security group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding'>SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding[] </a>**

-----
[orderBindings]: #orderbindings
#### [orderBindings]
The order bindings for this security group  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_SecurityGroup_OrderBinding'>SoftLayer_Network_SecurityGroup_OrderBinding[] </a>**

-----
[rules]: #rules
#### [rules]
The rules for this security group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_SecurityGroup_Rule'>SoftLayer_Network_SecurityGroup_Rule[] </a>**


## Count

-----
[networkComponentBindingCount]: #networkcomponentbindingcount
#### [networkComponentBindingCount]
A count of the network component bindings for this security group.   
<span class="type-label">Type: </span>**unsigned long**


-----
[orderBindingCount]: #orderbindingcount
#### [orderBindingCount]
A count of the order bindings for this security group   
<span class="type-label">Type: </span>**unsigned long**


-----
[ruleCount]: #rulecount
#### [ruleCount]
A count of the rules for this security group.   
<span class="type-label">Type: </span>**unsigned long**

</div>


