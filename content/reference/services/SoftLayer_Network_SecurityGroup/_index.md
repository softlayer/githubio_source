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
The Security Group service provides a common interface to interact with an account's security groups, their rules, and virtual guest instances associated with the groups. A security group contains a set of IP filter rules that define how to handle incoming (ingress) and outgoing (egress) traffic to both the public and private interfaces of a virtual server instance. The rules that you add to a security group are known as [[SoftLayer_Network_SecurityGroup_Rule (type)|security group rules]]. Security groups can be assigned to one or more virtual servers by attaching virtual guest network components through [[SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding (type)|bindings]]. 

Additional information can be found in Bluemix Docs and SoftLayer API Examples https://console.bluemix.net/docs/infrastructure/security-groups/sg_index.html https://softlayer.github.io/classes/softlayer_network_securitygroup/ 
        
        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_SecurityGroup/addRules'> addRules</a> </span>
            <div class='views-field-body'>Add new rules to a security group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_SecurityGroup/attachNetworkComponents'> attachNetworkComponents</a> </span>
            <div class='views-field-body'>Attach network components to a security group by creating a network component binding. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_SecurityGroup/createObject'> createObject</a> </span>
            <div class='views-field-body'>Create a new security group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_SecurityGroup/createObjects'> createObjects</a> </span>
            <div class='views-field-body'>Create new security groups.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_SecurityGroup/deleteObject'> deleteObject</a> </span>
            <div class='views-field-body'>Delete a security group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_SecurityGroup/deleteObjects'> deleteObjects</a> </span>
            <div class='views-field-body'>Delete security groups.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_SecurityGroup/detachNetworkComponents'> detachNetworkComponents</a> </span>
            <div class='views-field-body'>Detach network components from a security group by deleting its network component binding. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_SecurityGroup/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit a security group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_SecurityGroup/editObjects'> editObjects</a> </span>
            <div class='views-field-body'>Edit security groups.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_SecurityGroup/editRules'> editRules</a> </span>
            <div class='views-field-body'>Edit rules that belong to a security group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_SecurityGroup/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the account this security group belongs to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_SecurityGroup/getAllObjects'> getAllObjects</a> </span>
            <div class='views-field-body'>Get all security groups.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_SecurityGroup/getLimits'> getLimits</a> </span>
            <div class='views-field-body'>List the current security group limits </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_SecurityGroup/getNetworkComponentBindings'> getNetworkComponentBindings</a> </span>
            <div class='views-field-body'>Retrieve the network component bindings for this security group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_SecurityGroup/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_SecurityGroup record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_SecurityGroup/getOrderBindings'> getOrderBindings</a> </span>
            <div class='views-field-body'>Retrieve the order bindings for this security group</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_SecurityGroup/getRules'> getRules</a> </span>
            <div class='views-field-body'>Retrieve the rules for this security group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_SecurityGroup/getSupportedDataCenters'> getSupportedDataCenters</a> </span>
            <div class='views-field-body'>List the data centers that currently support the use of security groups. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_SecurityGroup/removeRules'> removeRules</a> </span>
            <div class='views-field-body'>Remove rules from a security group.</div>
        </div>
        </div>
</div>

