---
title: "SoftLayer_Network_LBaaS_Member"
description: "The SoftLayer_Network_LBaaS_Member service allows consumers to manage (backend) members for a given load balancer. A loa... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_Member"
---
# SoftLayer_Network_LBaaS_Member
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_LBaaS_Member' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LBaaS_Member' >Datatype</a></li>
    </ul>
</div>

## Description
The SoftLayer_Network_LBaaS_Member service allows consumers to manage (backend) members for a given load balancer. A load balancer may have one or more backend pools. Adding a backend member to the load balancer will add that member to all the backend pools. Similarly, deleting a backend member from the load balancer will remove that member from all associated backend pools. Weight of the backend member is a value between 1 and 256 but only applicable when the load balancing method configured is "Weighted Round Robin". 



        
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

#### [addLoadBalancerMembers](/reference/services/SoftLayer_Network_LBaaS_Member/addLoadBalancerMembers)
Add load balancer members

#### [deleteLoadBalancerMembers](/reference/services/SoftLayer_Network_LBaaS_Member/deleteLoadBalancerMembers)
Delete load balancer members

#### [getObject](/reference/services/SoftLayer_Network_LBaaS_Member/getObject)
Retrieve a SoftLayer_Network_LBaaS_Member record.

#### [updateLoadBalancerMembers](/reference/services/SoftLayer_Network_LBaaS_Member/updateLoadBalancerMembers)
Update members weight

</div>

