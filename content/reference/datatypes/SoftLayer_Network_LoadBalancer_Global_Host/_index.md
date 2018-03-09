---
title: "SoftLayer_Network_LoadBalancer_Global_Host"
description: "The SoftLayer_Network_LoadBalancer_Global_Host data type represents a single host that belongs to a global load balancer... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Global_Host"
---

# SoftLayer_Network_LoadBalancer_Global_Host
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_LoadBalancer_Global_Host' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Global_Host' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_LoadBalancer_Global_Host data type represents a single host that belongs to a global load balancer account's load balancing pool. 

The destination IP address of a host must be one that belongs to your SoftLayer customer account, or to a datacenter load balancer virtual ip that belongs to your SoftLayer customer account.  The destination IP address and port of a global load balancer host is a required field and must exist during creation and can not be removed.  The acceptable values for the health check type are 'none', 'http', and 'tcp'. The status property is updated in 5 minute intervals and the hits property is updated in 10 minute intervals. 

The order of the host is only important if you are using the 'failover' load balance method, and the weight is only important if you are using the 'weighted round robin' load balance method. 


### associatedMethods

*  [SoftLayer_Network_LoadBalancer_Global_Account::editObject](/reference/services/SoftLayer_Network_LoadBalancer_Global_Account/editObject )
*  [SoftLayer_Network_LoadBalancer_Global_Host::getObject](/reference/services/SoftLayer_Network_LoadBalancer_Global_Host/getObject )





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
            <span class='views-field-title'>
                <a href="#destinationIp" name=destinationIp>destinationIp</a>
            </span>
            <div class='views-field-body'>The IP address of the host that will be returned by the global load balancers in response to a dns request. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#destinationPort" name=destinationPort>destinationPort</a>
            </span>
            <div class='views-field-body'>The port of the host that will be used for health checks. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#enabled" name=enabled>enabled</a>
            </span>
            <div class='views-field-body'>Whether the host is enabled or not.  The value can be '0' for disabled, or '1' for enabled. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#healthCheck" name=healthCheck>healthCheck</a>
            </span>
            <div class='views-field-body'>The health check type of a host.  Valid values include 'none', 'http', and 'tcp'. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hits" name=hits>hits</a>
            </span>
            <div class='views-field-body'>The number of times the host was selected by the load balance method. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The unique identifier of a global load balancer host. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#loadBalanceOrder" name=loadBalanceOrder>loadBalanceOrder</a>
            </span>
            <div class='views-field-body'>The order of this host within the load balance pool.  This is only significant if the load balance method is set to failover. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#location" name=location>location</a>
            </span>
            <div class='views-field-body'>The location of a host in a datacenter.serverRoom format. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#status" name=status>status</a>
            </span>
            <div class='views-field-body'>The health status of a host.  The status can be either 'UP', 'DOWN', or null which could mean that the health check type is set to 'none' or an update to the ip, port, or health check type was recently done and the host is waiting for the new status.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#weight" name=weight>weight</a>
            </span>
            <div class='views-field-body'>The load balance weight of a host.  The total weight of all hosts in the load balancing pool must not exceed 100. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#loadBalancerAccount" name=loadBalancerAccount>loadBalancerAccount</a>
            </span>
            <div class='views-field-body'>The global load balancer account a host belongs to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Global_Account'>SoftLayer_Network_LoadBalancer_Global_Account </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


