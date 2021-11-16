---
title: "SoftLayer_Network_LBaaS_L7Member"
description: "The SoftLayer_Network_LBaaS_L7Member service allows consumers to manage (backend) members for L7 pools. A load balancer... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Member"
---
# SoftLayer_Network_LBaaS_L7Member
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_LBaaS_L7Member' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7Member' >Datatype</a></li>
    </ul>
</div>

## Description


The SoftLayer_Network_LBaaS_L7Member service allows consumers to manage (backend) members for L7 pools. A load balancer may have one or more L7 backend pools. A member can be added to one or more L7 backend pools. Deleting a backend member from one L7 pool will not remove it from other L7 pools to which it is associated. Weight of the backend member is a value between 1 and 256 but only applicable when the load balancing method configured is "Weighted Round Robin". 



        
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

#### [addL7PoolMembers](/reference/services/SoftLayer_Network_LBaaS_L7Member/addL7PoolMembers)
Add load balancer L7 members

</div>

<div class="method-row">

#### [deleteL7PoolMembers](/reference/services/SoftLayer_Network_LBaaS_L7Member/deleteL7PoolMembers)
Delete load balancer members

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_LBaaS_L7Member/getObject)
Retrieve a SoftLayer_Network_LBaaS_L7Member record.

</div>

<div class="method-row">

#### [updateL7PoolMembers](/reference/services/SoftLayer_Network_LBaaS_L7Member/updateL7PoolMembers)
Update l7 members weight and port

</div>
</div>

</div>

