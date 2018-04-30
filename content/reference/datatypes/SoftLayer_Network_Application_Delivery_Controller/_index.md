---
title: "SoftLayer_Network_Application_Delivery_Controller"
description: "The SoftLayer_Network_Application_Delivery_Controller data type models a single instance of an application delivery cont... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller"
---

# SoftLayer_Network_Application_Delivery_Controller
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Application_Delivery_Controller data type models a single instance of an application delivery controller. Local properties are read only, except for a ''notes'' property, which can be used to describe your application delivery controller service. The type's relational properties provide more information to the service's function and login information to the controller's backend management if advanced view is enabled. 





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
                <a href="#accountId" name=accountId>accountId</a>
            </span>
            <div class='views-field-body'>The unique identifier of the SoftLayer customer account that owns an application delivery controller record </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'>The date that an application delivery controller record was created </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>An application delivery controller's unique identifier </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'>The date that an application delivery controller record was last modified </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#name" name=name>name</a>
            </span>
            <div class='views-field-body'>An application delivery controller's name </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#notes" name=notes>notes</a>
            </span>
            <div class='views-field-body'>Editable notes used to describe an application delivery controller's function </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#typeId" name=typeId>typeId</a>
            </span>
            <div class='views-field-body'> </div>
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
                <a href="#account" name=account>account</a>
            </span>
            <div class='views-field-body'>The SoftLayer customer account that owns an application delivery controller record. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#averageDailyPublicBandwidthUsage" name=averageDailyPublicBandwidthUsage>averageDailyPublicBandwidthUsage</a>
            </span>
            <div class='views-field-body'>The average daily public bandwidth usage for the current billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingItem" name=billingItem>billingItem</a>
            </span>
            <div class='views-field-body'>The billing item for a Application Delivery Controller. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item_Network_Application_Delivery_Controller'>SoftLayer_Billing_Item_Network_Application_Delivery_Controller </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#configurationHistory" name=configurationHistory>configurationHistory</a>
            </span>
            <div class='views-field-body'>Previous configurations for an Application Delivery Controller. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_Configuration_History'>SoftLayer_Network_Application_Delivery_Controller_Configuration_History[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#datacenter" name=datacenter>datacenter</a>
            </span>
            <div class='views-field-body'>The datacenter that the application delivery controller resides in. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#description" name=description>description</a>
            </span>
            <div class='views-field-body'>A brief description of an application delivery controller record. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#licenseExpirationDate" name=licenseExpirationDate>licenseExpirationDate</a>
            </span>
            <div class='views-field-body'>The date in which the license for this application delivery controller will expire. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#loadBalancers" name=loadBalancers>loadBalancers</a>
            </span>
            <div class='views-field-body'>The virtual IP address records that belong to an application delivery controller based load balancer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_LoadBalancer_VirtualIpAddress[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#managedResourceFlag" name=managedResourceFlag>managedResourceFlag</a>
            </span>
            <div class='views-field-body'>A flag indicating that this Application Delivery Controller is a managed resource. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#managementIpAddress" name=managementIpAddress>managementIpAddress</a>
            </span>
            <div class='views-field-body'>An application delivery controller's management ip address. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#networkVlan" name=networkVlan>networkVlan</a>
            </span>
            <div class='views-field-body'>The network VLAN that an application delivery controller resides on. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#networkVlans" name=networkVlans>networkVlans</a>
            </span>
            <div class='views-field-body'>The network VLANs that an application delivery controller resides on. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#outboundPublicBandwidthUsage" name=outboundPublicBandwidthUsage>outboundPublicBandwidthUsage</a>
            </span>
            <div class='views-field-body'>The total public outbound bandwidth for the current billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#password" name=password>password</a>
            </span>
            <div class='views-field-body'>The password used to connect to an application delivery controller's management interface when it is operating in advanced view mode. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Software_Component_Password'>SoftLayer_Software_Component_Password </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#primaryIpAddress" name=primaryIpAddress>primaryIpAddress</a>
            </span>
            <div class='views-field-body'>An application delivery controller's primary public IP address. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#projectedPublicBandwidthUsage" name=projectedPublicBandwidthUsage>projectedPublicBandwidthUsage</a>
            </span>
            <div class='views-field-body'>The projected public outbound bandwidth for the current billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#subnets" name=subnets>subnets</a>
            </span>
            <div class='views-field-body'>A network application controller's subnets. A subnet is a group of IP addresses </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#tagReferences" name=tagReferences>tagReferences</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Tag_Reference'>SoftLayer_Tag_Reference[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#type" name=type>type</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_Type'>SoftLayer_Network_Application_Delivery_Controller_Type </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#virtualIpAddresses" name=virtualIpAddresses>virtualIpAddresses</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress[] </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#configurationHistoryCount" name=configurationHistoryCount>configurationHistoryCount</a>
            </span>
            <div class='views-field-body'>A count of previous configurations for an Application Delivery Controller. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#loadBalancerCount" name=loadBalancerCount>loadBalancerCount</a>
            </span>
            <div class='views-field-body'>A count of the virtual IP address records that belong to an application delivery controller based load balancer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#networkVlanCount" name=networkVlanCount>networkVlanCount</a>
            </span>
            <div class='views-field-body'>A count of the network VLANs that an application delivery controller resides on. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#subnetCount" name=subnetCount>subnetCount</a>
            </span>
            <div class='views-field-body'>A count of a network application controller's subnets. A subnet is a group of IP addresses </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#tagReferenceCount" name=tagReferenceCount>tagReferenceCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#virtualIpAddressCount" name=virtualIpAddressCount>virtualIpAddressCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


