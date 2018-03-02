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
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_SecurityGroup' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_SecurityGroup data type contains general information for a single security group. A security group contains a set of IP filter [[SoftLayer_Network_SecurityGroup_Rule (type)|rules]] that define how to handle incoming (ingress) and outgoing (egress) traffic to both the public and private interfaces of a virtual server instance and a set of [[SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding (type)|bindings]] to associate virtual guest network components with the security group. 





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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The date a security group was created. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#description" name=description>description</a></span>
            <div class='views-field-body'>The (optional) description for a security group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The unique ID for a security group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>The date a security group was last modified. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>The (optional) name for a security group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'>The account this security group belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkComponentBindings" name=networkComponentBindings>networkComponentBindings</a></span>
            <div class='views-field-body'>The network component bindings for this security group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding'>SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderBindings" name=orderBindings>orderBindings</a></span>
            <div class='views-field-body'>The order bindings for this security group </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_SecurityGroup_OrderBinding'>SoftLayer_Network_SecurityGroup_OrderBinding[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#rules" name=rules>rules</a></span>
            <div class='views-field-body'>The rules for this security group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_SecurityGroup_Rule'>SoftLayer_Network_SecurityGroup_Rule[] </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkComponentBindingCount" name=networkComponentBindingCount>networkComponentBindingCount</a></span>
            <div class='views-field-body'>A count of the network component bindings for this security group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderBindingCount" name=orderBindingCount>orderBindingCount</a></span>
            <div class='views-field-body'>A count of the order bindings for this security group </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ruleCount" name=ruleCount>ruleCount</a></span>
            <div class='views-field-body'>A count of the rules for this security group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


