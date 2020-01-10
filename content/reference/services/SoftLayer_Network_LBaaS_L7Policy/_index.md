---
title: "SoftLayer_Network_LBaaS_L7Policy"
description: "The SoftLayer_Network_LBaaS_L7Policy service allows consumers to manage the Policies associated with a Listener. A Liste... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Policy"
---
# SoftLayer_Network_LBaaS_L7Policy
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_LBaaS_L7Policy' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7Policy' >Datatype</a></li>
    </ul>
</div>

## Description
The SoftLayer_Network_LBaaS_L7Policy service allows consumers to manage the Policies associated with a Listener. A Listener can have multiple policies. Polices are associated with priorities. The priorities indicate the order in which policies are evaluated. Each policy is configured with an action which is applied when http traffic matches rules associated with the policy. A policy can be configured with one of the following actions: redirect to pool, redirect to url, or reject. Policies configured with reject are always evaluated first irrespective of the priority followed by redirect to url, after which policies with action set to redirect to pool are evaluated. Polices have multiple rules, each rule is evaluated to true or false. If all the rules of the policy evaluate to true then the action associated with that policy is applied to the request. 



        
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

#### [addL7Policies](/reference/services/SoftLayer_Network_LBaaS_L7Policy/addL7Policies)
Create layer 7 policies with rules for the given listener. 
</div>

<div class="method-row">

#### [deleteObject](/reference/services/SoftLayer_Network_LBaaS_L7Policy/deleteObject)
Deletes a l7 policy instance and the rules associated with the policy
</div>

<div class="method-row">

#### [editObject](/reference/services/SoftLayer_Network_LBaaS_L7Policy/editObject)
Edit a l7 policy instance's properties
</div>

<div class="method-row">

#### [getL7Rules](/reference/services/SoftLayer_Network_LBaaS_L7Policy/getL7Rules)

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_LBaaS_L7Policy/getObject)
Retrieve a SoftLayer_Network_LBaaS_L7Policy record.
</div>
</div>

</div>

