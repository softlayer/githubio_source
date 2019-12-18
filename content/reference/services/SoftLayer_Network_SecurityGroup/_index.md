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
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [addRules](/reference/services/SoftLayer_Network_SecurityGroup/addRules)
Add new rules to a security group.

#### [attachNetworkComponents](/reference/services/SoftLayer_Network_SecurityGroup/attachNetworkComponents)
Attach network components to a security group by creating a network component binding. 

#### [createObject](/reference/services/SoftLayer_Network_SecurityGroup/createObject)
Create a new security group.

#### [createObjects](/reference/services/SoftLayer_Network_SecurityGroup/createObjects)
Create new security groups.

#### [deleteObject](/reference/services/SoftLayer_Network_SecurityGroup/deleteObject)
Delete a security group.

#### [deleteObjects](/reference/services/SoftLayer_Network_SecurityGroup/deleteObjects)
Delete security groups.

#### [detachNetworkComponents](/reference/services/SoftLayer_Network_SecurityGroup/detachNetworkComponents)
Detach network components from a security group by deleting its network component binding. 

#### [editObject](/reference/services/SoftLayer_Network_SecurityGroup/editObject)
Edit a security group.

#### [editObjects](/reference/services/SoftLayer_Network_SecurityGroup/editObjects)
Edit security groups.

#### [editRules](/reference/services/SoftLayer_Network_SecurityGroup/editRules)
Edit rules that belong to a security group.

#### [getAccount](/reference/services/SoftLayer_Network_SecurityGroup/getAccount)
Retrieve the account this security group belongs to.

#### [getAllObjects](/reference/services/SoftLayer_Network_SecurityGroup/getAllObjects)
Get all security groups.

#### [getLimits](/reference/services/SoftLayer_Network_SecurityGroup/getLimits)
List the current security group limits 

#### [getNetworkComponentBindings](/reference/services/SoftLayer_Network_SecurityGroup/getNetworkComponentBindings)
Retrieve the network component bindings for this security group.

#### [getObject](/reference/services/SoftLayer_Network_SecurityGroup/getObject)
Retrieve a SoftLayer_Network_SecurityGroup record.

#### [getOrderBindings](/reference/services/SoftLayer_Network_SecurityGroup/getOrderBindings)
Retrieve the order bindings for this security group

#### [getRules](/reference/services/SoftLayer_Network_SecurityGroup/getRules)
Retrieve the rules for this security group.

#### [getSupportedDataCenters](/reference/services/SoftLayer_Network_SecurityGroup/getSupportedDataCenters)
List the data centers that currently support the use of security groups. 

#### [removeRules](/reference/services/SoftLayer_Network_SecurityGroup/removeRules)
Remove rules from a security group.

</div>

