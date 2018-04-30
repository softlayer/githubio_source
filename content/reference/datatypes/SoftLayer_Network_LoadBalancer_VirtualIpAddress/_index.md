---
title: "SoftLayer_Network_LoadBalancer_VirtualIpAddress"
description: "The SoftLayer_Network_LoadBalancer_VirtualIpAddress data type contains all the information relating to a specific load b... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_VirtualIpAddress"
---

# SoftLayer_Network_LoadBalancer_VirtualIpAddress
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_VirtualIpAddress' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_LoadBalancer_VirtualIpAddress data type contains all the information relating to a specific load balancer assigned to a customer account. 

Information retained on the object itself is the virtual IP address, load balancing method, and any notes that are related to the load balancer.  There is also an array of SoftLayer_Network_LoadBalancer_Service objects, which represent the load balancer services, explained more fully in the SoftLayer_Network_LoadBalancer_Service documentation. 


### associatedMethods

*  [SoftLayer_Network_LoadBalancer_VirtualIpAddress::getObject](/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/getObject )





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
                <a href="#connectionLimit" name=connectionLimit>connectionLimit</a>
            </span>
            <div class='views-field-body'>Connection limit on this VIP.  Can be upgraded through the upgradeConnectionLimit() function </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>Unique ID for this object, used for the getObject method, and must be set if you are editing this object. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#loadBalancingMethod" name=loadBalancingMethod>loadBalancingMethod</a>
            </span>
            <div class='views-field-body'>The load balancing method that determines which server is used "next" by the load balancer.  The method is stored in an abbreviated form, represented in parentheses after the full name. Methods include: Round Robin (Value "rr"):  Each server is used sequentially in a circular queue Shortest Response (Value "sr"):  The server with the lowest ping at the last health check gets the next request Least Connections (Value "lc"):  The server with the least current connections is given the next request Persistent IP - Round Robin (Value "pi"): The same server will be returned to a request during a users session.  Servers are chosen through round robin. Persistent IP - Shortest Response (Value "pi-sr"): The same server will be returned to a request during a users session.  Servers are chosen through shortest response. Persistent IP - Least Connections (Value "pi-lc"): The same server will be returned to a request during a users session.  Servers are chosen through least connections. Insert Cookie - Round Robin (Value "ic"):  Inserts a cookie into the HTTP stream that will tie that client to a particular balanced server. Servers are chosen through round robin. Insert Cookie - Shortest Response (Value "ic-sr"): Inserts a cookie into the HTTP stream that will tie that client to a particular balanced server. Servers are chosen through shortest response. Insert Cookie - Least Connections (Value "ic-lc"): Inserts a cookie into the HTTP stream that will tie that client to a particular balanced server. Servers are chosen through least connections.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#loadBalancingMethodFullName" name=loadBalancingMethodFullName>loadBalancingMethodFullName</a>
            </span>
            <div class='views-field-body'>A human readable version of loadBalancingMethod, intended mainly for API users. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'>Date this load balancer was last modified </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#name" name=name>name</a>
            </span>
            <div class='views-field-body'>The name of the load balancer instance </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#notes" name=notes>notes</a>
            </span>
            <div class='views-field-body'>User-created notes on this load balancer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#securityCertificateId" name=securityCertificateId>securityCertificateId</a>
            </span>
            <div class='views-field-body'>The unique identifier of the Security Certificate to be utilized when SSL support is enabled.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#sourcePort" name=sourcePort>sourcePort</a>
            </span>
            <div class='views-field-body'>This is the port for incoming traffic. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#type" name=type>type</a>
            </span>
            <div class='views-field-body'>The connection type of this VIP.  Valid values are HTTP, FTP, TCP, UDP, and DNS. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#virtualIpAddress" name=virtualIpAddress>virtualIpAddress</a>
            </span>
            <div class='views-field-body'>The virtual, public-facing IP address for your load balancer.  This is the address of all incoming traffic </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#account" name=account>account</a>
            </span>
            <div class='views-field-body'>The account that owns this load balancer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingItem" name=billingItem>billingItem</a>
            </span>
            <div class='views-field-body'>The current billing item for the Load Balancer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#customerManagedFlag" name=customerManagedFlag>customerManagedFlag</a>
            </span>
            <div class='views-field-body'>If false, this VIP and associated services may be edited via the portal or the API. If true, you must configure this VIP manually on the device. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#managedResourceFlag" name=managedResourceFlag>managedResourceFlag</a>
            </span>
            <div class='views-field-body'>A flag indicating that the load balancer is a managed resource. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#services" name=services>services</a>
            </span>
            <div class='views-field-body'>the services on this load balancer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Service'>SoftLayer_Network_LoadBalancer_Service[] </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#serviceCount" name=serviceCount>serviceCount</a>
            </span>
            <div class='views-field-body'>A count of the services on this load balancer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


