---
title: "SoftLayer_Network_LoadBalancer_Global_Account"
description: "A global load balancer account enables you to load balance traffic between servers that are in geographically diverse lo... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Global_Account"
---
# SoftLayer_Network_LoadBalancer_Global_Account
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_LoadBalancer_Global_Account' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Global_Account' >Datatype</a></li>
    </ul>
</div>

## Description
A global load balancer account enables you to load balance traffic between servers that are in geographically diverse locations.  SoftLayer's global load balancers act as a highly modified DNS server.  SoftLayer's global load balancers work by accepting DNS requests for a specific hostname, choosing a host from a load balancing pool using the load balance method specified, and returning a destination IP address through a DNS response. 

A global load balancer account can be created by ordering it as an additional service through the SoftLayer customer portal.  You can modify your new global load balancer account once it's created and provisioned.  There is a delay before your global load balancer account is created because the purchase has to be approved by SoftLayer sales and provisioned. 

Hosts are created and modified through the [[SoftLayer_Network_LoadBalancer_Global_Account::editObject|editObject]] method instead of directly through the [[SoftLayer_Network_LoadBalancer_Global_Host|global load balancer host service]].  This allows you to update the properties of a global load balancer account and the hosts that make up the load balancing pool in a single request. 

To have SoftLayer's global load balancers respond to DNS requests, a nameserver resource record must be added for the hostname on your global load balancer account.  If your globally load balanced domain is hosted on the SoftLayer nameservers, the [[SoftLayer_Network_LoadBalancer_Global_Account::addNsRecord|addNsRecord]] method will create the required nameserver resource record in the zone file for you.  If your globally load balanced domain is hosted on any other nameservers, you will need to add the nameserver resource record yourself.  The SoftLayer Knowledge Layer contains information about [http://knowledgelayer.softlayer.com/questions/421/ configuring DNS] for a globally load balanced domain. 

Use the [[SoftLayer_Network_LoadBalancer_Global_Host::deleteObject]] method to remove a host from your global load balancing pool. 

Global load balancer accounts can only be removed by opening a ticket with the SoftLayer accounting team and request that the global load balancer service be canceled. 
        
        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_Global_Account/addNsRecord'> addNsRecord</a> </span>
            <div class='views-field-body'>Add the required nameserver resource record for a global load balancer account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_Global_Account/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit a global load balancer account and the hosts that make up the load balancing pool.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_Global_Account/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve your SoftLayer customer account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_Global_Account/getBillingItem'> getBillingItem</a> </span>
            <div class='views-field-body'>Retrieve the current billing item for a Global Load Balancer account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_Global_Account/getHosts'> getHosts</a> </span>
            <div class='views-field-body'>Retrieve the hosts in the load balancing pool for a global load balancer account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_Global_Account/getLoadBalanceType'> getLoadBalanceType</a> </span>
            <div class='views-field-body'>Retrieve the load balance method of a global load balancer account</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_Global_Account/getManagedResourceFlag'> getManagedResourceFlag</a> </span>
            <div class='views-field-body'>Retrieve a flag indicating that the global load balancer is a managed resource.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_Global_Account/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_LoadBalancer_Global_Account record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_Global_Account/removeNsRecord'> removeNsRecord</a> </span>
            <div class='views-field-body'>Remove the required nameserver resource record for a global load balancer account.</div>
        </div>
        </div>
</div>

