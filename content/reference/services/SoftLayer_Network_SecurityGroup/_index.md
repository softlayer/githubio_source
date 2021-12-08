---
title: "SoftLayer_Network_SecurityGroup"
description: "The Security Group service provides a common interface to interact with an account's security groups, their rules, and v... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
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


The Security Group service provides a common interface to interact with an account's security groups, their rules, and virtual guest instances associated with the groups. A security group contains a set of IP filter rules that define how to handle incoming (ingress) and outgoing (egress) traffic to both the public and private interfaces of a virtual server instance. The rules that you add to a security group are known as [SoftLayer_Network_SecurityGroup_Rule]({{<ref "reference/datatypes/SoftLayer_Network_SecurityGroup_Rule">}}). 

Additional information can be found in IBM Cloud Docs and SoftLayer API Examples https://console.bluemix.net/docs/infrastructure/security-groups/sg_index.html https://softlayer.github.io/classes/softlayer_network_securitygroup/ 



        
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

#### [addRules](/reference/services/SoftLayer_Network_SecurityGroup/addRules)
Add new rules to a security group.

</div>

<div class="method-row">

#### [attachNetworkComponents](/reference/services/SoftLayer_Network_SecurityGroup/attachNetworkComponents)
Attach network components to a security group by creating a network component binding. 

</div>

<div class="method-row">

#### [createObject](/reference/services/SoftLayer_Network_SecurityGroup/createObject)
Create a new security group.

</div>

<div class="method-row">

#### [createObjects](/reference/services/SoftLayer_Network_SecurityGroup/createObjects)
Create new security groups.

</div>

<div class="method-row">

#### [deleteObject](/reference/services/SoftLayer_Network_SecurityGroup/deleteObject)
Delete a security group.

</div>

<div class="method-row">

#### [deleteObjects](/reference/services/SoftLayer_Network_SecurityGroup/deleteObjects)
Delete security groups.

</div>

<div class="method-row">

#### [detachNetworkComponents](/reference/services/SoftLayer_Network_SecurityGroup/detachNetworkComponents)
Detach network components from a security group by deleting its network component binding. 

</div>

<div class="method-row">

#### [editObject](/reference/services/SoftLayer_Network_SecurityGroup/editObject)
Edit a security group.

</div>

<div class="method-row">

#### [editObjects](/reference/services/SoftLayer_Network_SecurityGroup/editObjects)
Edit security groups.

</div>

<div class="method-row">

#### [editRules](/reference/services/SoftLayer_Network_SecurityGroup/editRules)
Edit rules that belong to a security group.

</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Network_SecurityGroup/getAccount)
Retrieve the account this security group belongs to.

</div>

<div class="method-row">

#### [getAllObjects](/reference/services/SoftLayer_Network_SecurityGroup/getAllObjects)
Get all security groups.

</div>

<div class="method-row">

#### [getLimits](/reference/services/SoftLayer_Network_SecurityGroup/getLimits)
List the current security group limits 

</div>

<div class="method-row">

#### [getNetworkComponentBindings](/reference/services/SoftLayer_Network_SecurityGroup/getNetworkComponentBindings)
Retrieve the network component bindings for this security group.

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_SecurityGroup/getObject)
Retrieve a SoftLayer_Network_SecurityGroup record.

</div>

<div class="method-row">

#### [getOrderBindings](/reference/services/SoftLayer_Network_SecurityGroup/getOrderBindings)
Retrieve the order bindings for this security group

</div>

<div class="method-row">

#### [getRules](/reference/services/SoftLayer_Network_SecurityGroup/getRules)
Retrieve the rules for this security group.

</div>

<div class="method-row">

#### [getSupportedDataCenters](/reference/services/SoftLayer_Network_SecurityGroup/getSupportedDataCenters)
List the data centers that currently support the use of security groups. 

</div>

<div class="method-row">

#### [removeRules](/reference/services/SoftLayer_Network_SecurityGroup/removeRules)
Remove rules from a security group.

</div>
</div>

</div>

