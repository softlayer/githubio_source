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

## Local
-----
[accountId]: #accountid
#### [accountId]
The unique identifier of the SoftLayer customer account that owns an application delivery controller record  
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
The date that an application delivery controller record was created  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
An application delivery controller's unique identifier  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date that an application delivery controller record was last modified  
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
An application delivery controller's name  
<span class="type-label">Type: </span>**string**

-----
[notes]: #notes
#### [notes]
Editable notes used to describe an application delivery controller's function  
<span class="type-label">Type: </span>**string**

-----
[typeId]: #typeid
#### [typeId]
  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The SoftLayer customer account that owns an application delivery controller record.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[averageDailyPublicBandwidthUsage]: #averagedailypublicbandwidthusage
#### [averageDailyPublicBandwidthUsage]
The average daily public bandwidth usage for the current billing cycle.  
<span class="type-label">Type: </span>**float**

-----
[billingItem]: #billingitem
#### [billingItem]
The billing item for a Application Delivery Controller.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Network_Application_Delivery_Controller'>SoftLayer_Billing_Item_Network_Application_Delivery_Controller </a>**

-----
[configurationHistory]: #configurationhistory
#### [configurationHistory]
Previous configurations for an Application Delivery Controller.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_Configuration_History'>SoftLayer_Network_Application_Delivery_Controller_Configuration_History[] </a>**

-----
[datacenter]: #datacenter
#### [datacenter]
The datacenter that the application delivery controller resides in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[description]: #description
#### [description]
A brief description of an application delivery controller record.  
<span class="type-label">Type: </span>**string**

-----
[licenseExpirationDate]: #licenseexpirationdate
#### [licenseExpirationDate]
The date in which the license for this application delivery controller will expire.  
<span class="type-label">Type: </span>**dateTime**

-----
[loadBalancers]: #loadbalancers
#### [loadBalancers]
The virtual IP address records that belong to an application delivery controller based load balancer.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_LoadBalancer_VirtualIpAddress[] </a>**

-----
[managedResourceFlag]: #managedresourceflag
#### [managedResourceFlag]
A flag indicating that this Application Delivery Controller is a managed resource.  
<span class="type-label">Type: </span>**boolean**

-----
[managementIpAddress]: #managementipaddress
#### [managementIpAddress]
An application delivery controller's management ip address.  
<span class="type-label">Type: </span>**string**

-----
[networkVlan]: #networkvlan
#### [networkVlan]
The network VLAN that an application delivery controller resides on.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>**

-----
[networkVlans]: #networkvlans
#### [networkVlans]
The network VLANs that an application delivery controller resides on.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a>**

-----
[outboundPublicBandwidthUsage]: #outboundpublicbandwidthusage
#### [outboundPublicBandwidthUsage]
The total public outbound bandwidth for the current billing cycle.  
<span class="type-label">Type: </span>**decimal**

-----
[password]: #password
#### [password]
The password used to connect to an application delivery controller's management interface when it is operating in advanced view mode.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component_Password'>SoftLayer_Software_Component_Password </a>**

-----
[primaryIpAddress]: #primaryipaddress
#### [primaryIpAddress]
An application delivery controller's primary public IP address.  
<span class="type-label">Type: </span>**string**

-----
[projectedPublicBandwidthUsage]: #projectedpublicbandwidthusage
#### [projectedPublicBandwidthUsage]
The projected public outbound bandwidth for the current billing cycle.  
<span class="type-label">Type: </span>**float**

-----
[subnets]: #subnets
#### [subnets]
A network application controller's subnets. A subnet is a group of IP addresses  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**

-----
[tagReferences]: #tagreferences
#### [tagReferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Tag_Reference'>SoftLayer_Tag_Reference[] </a>**

-----
[type]: #type
#### [type]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_Type'>SoftLayer_Network_Application_Delivery_Controller_Type </a>**

-----
[virtualIpAddresses]: #virtualipaddresses
#### [virtualIpAddresses]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress[] </a>**


## Count

-----
[configurationHistoryCount]: #configurationhistorycount
#### [configurationHistoryCount]
A count of previous configurations for an Application Delivery Controller.   
<span class="type-label">Type: </span>**unsigned long**


-----
[loadBalancerCount]: #loadbalancercount
#### [loadBalancerCount]
A count of the virtual IP address records that belong to an application delivery controller based load balancer.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkVlanCount]: #networkvlancount
#### [networkVlanCount]
A count of the network VLANs that an application delivery controller resides on.   
<span class="type-label">Type: </span>**unsigned long**


-----
[subnetCount]: #subnetcount
#### [subnetCount]
A count of a network application controller's subnets. A subnet is a group of IP addresses   
<span class="type-label">Type: </span>**unsigned long**


-----
[tagReferenceCount]: #tagreferencecount
#### [tagReferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualIpAddressCount]: #virtualipaddresscount
#### [virtualIpAddressCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>


