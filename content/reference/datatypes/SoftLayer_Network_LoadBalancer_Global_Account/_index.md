---
title: "SoftLayer_Network_LoadBalancer_Global_Account"
description: "The SoftLayer_Network_LoadBalancer_Global_Account data type contains the properties for a single global load balancer ac... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Global_Account"
---

# SoftLayer_Network_LoadBalancer_Global_Account
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Global_Account' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_LoadBalancer_Global_Account data type contains the properties for a single global load balancer account.  The properties you are able to edit are fallbackIp, loadBalanceTypeId, and notes. The hosts relational property can be used for creating and editing hosts that belong to the global load balancer account.  The [[SoftLayer_Network_LoadBalancer_Global_Account::editObject|editObject]] method contains details on creating and edited hosts through the hosts relational property. 


### associatedMethods

*  [SoftLayer_Account::getGlobalLoadBalancerAccounts](/reference/services/SoftLayer_Account/getGlobalLoadBalancerAccounts )
*  [SoftLayer_Network_LoadBalancer_Global_Account::getObject](/reference/services/SoftLayer_Network_LoadBalancer_Global_Account/getObject )





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
            <span class='views-field-title'><a href="#allowedNumberOfHosts" name=allowedNumberOfHosts>allowedNumberOfHosts</a></span>
            <div class='views-field-body'>The maximum number of hosts that a global load balancer account is allowed to have. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#averageConnectionsPerSecond" name=averageConnectionsPerSecond>averageConnectionsPerSecond</a></span>
            <div class='views-field-body'>The average amount of connections per second used within the current billing cycle.  This number is updated daily. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>float</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#connectionsPerSecond" name=connectionsPerSecond>connectionsPerSecond</a></span>
            <div class='views-field-body'>The amount of connections per second a global load balancer account may use within a billing cycle without being billed for an overage. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#fallbackIp" name=fallbackIp>fallbackIp</a></span>
            <div class='views-field-body'>The IP address that will be return to a DNS request when none of the hosts for a global load balancer account could be returned. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hostname" name=hostname>hostname</a></span>
            <div class='views-field-body'>The hostname of a global load balancer account that is being load balanced. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The unique identifier of a global load balancer account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#loadBalanceTypeId" name=loadBalanceTypeId>loadBalanceTypeId</a></span>
            <div class='views-field-body'>The identifier of the load balance method for a global load balancer account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#notes" name=notes>notes</a></span>
            <div class='views-field-body'>Additional customer defined information for a global load balancer account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'>Your SoftLayer customer account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingItem" name=billingItem>billingItem</a></span>
            <div class='views-field-body'>The current billing item for a Global Load Balancer account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hosts" name=hosts>hosts</a></span>
            <div class='views-field-body'>The hosts in the load balancing pool for a global load balancer account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Global_Host'>SoftLayer_Network_LoadBalancer_Global_Host[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#loadBalanceType" name=loadBalanceType>loadBalanceType</a></span>
            <div class='views-field-body'>The load balance method of a global load balancer account </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Global_Type'>SoftLayer_Network_LoadBalancer_Global_Type </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#managedResourceFlag" name=managedResourceFlag>managedResourceFlag</a></span>
            <div class='views-field-body'>A flag indicating that the global load balancer is a managed resource. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hostCount" name=hostCount>hostCount</a></span>
            <div class='views-field-body'>A count of the hosts in the load balancing pool for a global load balancer account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


