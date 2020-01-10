---
title: "SoftLayer_Network_Subnet"
description: "The SoftLayer_Network_Subnet data type contains general information relating to a single SoftLayer subnet. Personal info... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet"
---

# SoftLayer_Network_Subnet
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Subnet' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Subnet' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Subnet data type contains general information relating to a single SoftLayer subnet. Personal information in this type such as names, addresses, and phone numbers are assigned to the account only and not to users belonging to the account. 

### External Links


* [Subnetwork at Wikipedia](http://en.wikipedia.org/wiki/Subnetwork)


* [RFC950:Internet Standard Subnetting Procedure at ietf.org](http://tools.ietf.org/html/rfc950)


* [Classless Inter-Domain Routing at Wikipedia](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)



### associatedMethods

*  [SoftLayer_Network_Subnet::findAllSubnetsAndActiveSwipTransactionStatus](/reference/services/SoftLayer_Network_Subnet/findAllSubnetsAndActiveSwipTransactionStatus )
*  [SoftLayer_Network_Subnet::getObject](/reference/services/SoftLayer_Network_Subnet/getObject )
*  [SoftLayer_Network_Subnet::getSubnetForIpAddress](/reference/services/SoftLayer_Network_Subnet/getSubnetForIpAddress )
*  [SoftLayer_Network_Subnet_Swip_Transaction::getSubnet](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/getSubnet )
*  [SoftLayer_Network_Vlan::getSubnets](/reference/services/SoftLayer_Network_Vlan/getSubnets )
*  [SoftLayer_Network_Vlan::getSecondarySubnets](/reference/services/SoftLayer_Network_Vlan/getSecondarySubnets )





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[broadcastAddress]: #broadcastaddress
#### [broadcastAddress]
The last IP address in a subnet is the subnet's broadcast address. This is an IP address that will broadcast network requests to the entire subnet and may not be assigned to a network interface.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[cidr]: #cidr
#### [cidr]
A subnet's Classless Inter-Domain Routing prefix. This is a number between 0 and 32 signifying the number of bits in a subnet's netmask. These bits separate a subnet's network address from it's host addresses. It performs the same function as the ''netmask'' property, but is represented as an integer.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[gateway]: #gateway
#### [gateway]
A subnet's gateway address. This is an IP address that belongs to the router on the subnet and may not be assigned to a network interface.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A subnet's internal identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[isCustomerOwned]: #iscustomerowned
#### [isCustomerOwned]
  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[isCustomerRoutable]: #iscustomerroutable
#### [isCustomerRoutable]
  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The last time this subnet was last modified  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[netmask]: #netmask
#### [netmask]
A bitmask in dotted-quad format that is used to separate a subnet's network address from it's host addresses. This performs the same function as the ''cidr'' property, but is expressed in a string format.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[networkIdentifier]: #networkidentifier
#### [networkIdentifier]
A subnet's network identifier. This is the first IP address of a subnet and may not be assigned to a network interface.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[networkVlanId]: #networkvlanid
#### [networkVlanId]
A subnet's associated VLAN's internal identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[note]: #note
#### [note]
This is the note field.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[sortOrder]: #sortorder
#### [sortOrder]
A subnet can be one of several types. PRIMARY, ADDITIONAL_PRIMARY, SECONDARY, ROUTED_TO_VLAN, SECONDARY_ON_VLAN, and STATIC_IP_ROUTED. The type determines the order in which many subnets are sorted in the SoftLayer customer portal. This groups subnets of similar type together.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[subnetType]: #subnettype
#### [subnetType]
A subnet can be one of several types. PRIMARY, ADDITIONAL_PRIMARY, SECONDARY, ROUTED_TO_VLAN, SECONDARY_ON_VLAN, STORAGE_NETWORK, and STATIC_IP_ROUTED. A "PRIMARY" subnet is the primary network bound to a VLAN within the softlayer network. An "ADDITIONAL_PRIMARY" subnet is bound to a network VLAN to augment the pool of available primary IP addresses that may be assigned to a server. A "SECONDARY" subnet is any of the secondary subnet's bound to a VLAN interface. A "ROUTED_TO_VLAN" subnet is a portable subnet that can be routed to any server on a vlan. A "SECONDARY_ON_VLAN" subnet also doesn't exist as a VLAN interface, but is routed directly to a VLAN instead of a single IP address by SoftLayer's routers.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[totalIpAddresses]: #totalipaddresses
#### [totalIpAddresses]
The number of IP addresses contained within this subnet.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[usableIpAddressCount]: #usableipaddresscount
#### [usableIpAddressCount]
The number of IP addresses that can be addressed within this subnet. For IPv4 subnets with a CIDR value of at most 30, a discount of 3 is taken from the total number of IP addresses for the subnet's unusable network, gateway and broadcast IP addresses. For IPv6 subnets with a CIDR value of at most 126, a discount of 2 is taken for the subnet's network and gateway IP addresses.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[version]: #version
#### [version]
This is the Internet Protocol version. Current values may be either 4 or 6.   
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[activeRegistration]: #activeregistration
#### [activeRegistration]
If present, the active registration for this subnet.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration'>SoftLayer_Network_Subnet_Registration </a>**


</div>
<div class="prop-row">

-----
[activeSwipTransaction]: #activeswiptransaction
#### [activeSwipTransaction]
All the swip transactions associated with a subnet that are still active.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_Swip_Transaction'>SoftLayer_Network_Subnet_Swip_Transaction </a>**


</div>
<div class="prop-row">

-----
[activeTransaction]: #activetransaction
#### [activeTransaction]
The billing item for a subnet.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>**


</div>
<div class="prop-row">

-----
[addressSpace]: #addressspace
#### [addressSpace]
Identifier which distinguishes what classification of addresses the subnet represents.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[allowedHost]: #allowedhost
#### [allowedHost]
The SoftLayer_Network_Storage_Allowed_Host information to connect this Subnet to Network Storage supporting access control lists.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Allowed_Host'>SoftLayer_Network_Storage_Allowed_Host </a>**


</div>
<div class="prop-row">

-----
[allowedNetworkStorage]: #allowednetworkstorage
#### [allowedNetworkStorage]
The SoftLayer_Network_Storage objects that this SoftLayer_Hardware has access to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[allowedNetworkStorageReplicas]: #allowednetworkstoragereplicas
#### [allowedNetworkStorageReplicas]
The SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
The billing item for a subnet.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**


</div>
<div class="prop-row">

-----
[boundDescendants]: #bounddescendants
#### [boundDescendants]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**


</div>
<div class="prop-row">

-----
[boundRouterFlag]: #boundrouterflag
#### [boundRouterFlag]
Whether or not this subnet is associated with a router. Subnets that are not associated with a router cannot be routed.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[boundRouters]: #boundrouters
#### [boundRouters]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[children]: #children
#### [children]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**


</div>
<div class="prop-row">

-----
[datacenter]: #datacenter
#### [datacenter]
The data center this subnet may be routed within.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Datacenter'>SoftLayer_Location_Datacenter </a>**


</div>
<div class="prop-row">

-----
[descendants]: #descendants
#### [descendants]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**


</div>
<div class="prop-row">

-----
[displayLabel]: #displaylabel
#### [displayLabel]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[endPointIpAddress]: #endpointipaddress
#### [endPointIpAddress]
A static routed ip address  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a>**


</div>
<div class="prop-row">

-----
[globalIpRecord]: #globaliprecord
#### [globalIpRecord]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress_Global'>SoftLayer_Network_Subnet_IpAddress_Global </a>**


</div>
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
The hardware using IP addresses on this subnet.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[ipAddresses]: #ipaddresses
#### [ipAddresses]
All the ip addresses associated with a subnet.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>**


</div>
<div class="prop-row">

-----
[networkComponentFirewall]: #networkcomponentfirewall
#### [networkComponentFirewall]
The upstream network component firewall.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component_Firewall'>SoftLayer_Network_Component_Firewall </a>**


</div>
<div class="prop-row">

-----
[networkProtectionAddresses]: #networkprotectionaddresses
#### [networkProtectionAddresses]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Protection_Address'>SoftLayer_Network_Protection_Address[] </a>**


</div>
<div class="prop-row">

-----
[networkTunnelContexts]: #networktunnelcontexts
#### [networkTunnelContexts]
IPSec network tunnels that have access to a private subnet.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context'>SoftLayer_Network_Tunnel_Module_Context[] </a>**


</div>
<div class="prop-row">

-----
[networkVlan]: #networkvlan
#### [networkVlan]
The VLAN object that a subnet is associated with.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>**


</div>
<div class="prop-row">

-----
[podName]: #podname
#### [podName]
The pod in which this subnet resides.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[protectedIpAddresses]: #protectedipaddresses
#### [protectedIpAddresses]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>**


</div>
<div class="prop-row">

-----
[regionalInternetRegistry]: #regionalinternetregistry
#### [regionalInternetRegistry]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Regional_Internet_Registry'>SoftLayer_Network_Regional_Internet_Registry </a>**


</div>
<div class="prop-row">

-----
[registrations]: #registrations
#### [registrations]
All registrations that have been created for this subnet.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration'>SoftLayer_Network_Subnet_Registration[] </a>**


</div>
<div class="prop-row">

-----
[reverseDomain]: #reversedomain
#### [reverseDomain]
The reverse DNS domain associated with this subnet.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Domain'>SoftLayer_Dns_Domain </a>**


</div>
<div class="prop-row">

-----
[roleKeyName]: #rolekeyname
#### [roleKeyName]
An identifier of the role the subnet is within. Roles dictate how a subnet may be used.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[roleName]: #rolename
#### [roleName]
The name of the role the subnet is within. Roles dictate how a subnet may be used.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[routingTypeKeyName]: #routingtypekeyname
#### [routingTypeKeyName]
The identifier for the type of route then subnet is currently configured for.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[routingTypeName]: #routingtypename
#### [routingTypeName]
The name for the type of route then subnet is currently configured for.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[swipTransaction]: #swiptransaction
#### [swipTransaction]
All the swip transactions associated with a subnet.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_Swip_Transaction'>SoftLayer_Network_Subnet_Swip_Transaction[] </a>**


</div>
<div class="prop-row">

-----
[unboundDescendants]: #unbounddescendants
#### [unboundDescendants]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**


</div>
<div class="prop-row">

-----
[utilizedIpAddressCount]: #utilizedipaddresscount
#### [utilizedIpAddressCount]
Provides the total number of utilized IP addresses on this subnet. The primary consumer of IP addresses are compute resources, which can consume more than one address. This value is only supported for primary subnet types.  
<span class="type-label">Type: </span>**unsigned integer**


</div>
<div class="prop-row">

-----
[virtualGuests]: #virtualguests
#### [virtualGuests]
The Virtual Servers using IP addresses on this subnet.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>

## Count
<div class="prop-row">

-----
[allowedNetworkStorageCount]: #allowednetworkstoragecount
#### [allowedNetworkStorageCount]
A count of the SoftLayer_Network_Storage objects that this SoftLayer_Hardware has access to.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[allowedNetworkStorageReplicaCount]: #allowednetworkstoragereplicacount
#### [allowedNetworkStorageReplicaCount]
A count of the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[boundDescendantCount]: #bounddescendantcount
#### [boundDescendantCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[boundRouterCount]: #boundroutercount
#### [boundRouterCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[childrenCount]: #childrencount
#### [childrenCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[descendantCount]: #descendantcount
#### [descendantCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[hardwareCount]: #hardwarecount
#### [hardwareCount]
A count of the hardware using IP addresses on this subnet.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[ipAddressCount]: #ipaddresscount
#### [ipAddressCount]
A count of all the ip addresses associated with a subnet.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkProtectionAddressCount]: #networkprotectionaddresscount
#### [networkProtectionAddressCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkTunnelContextCount]: #networktunnelcontextcount
#### [networkTunnelContextCount]
A count of iPSec network tunnels that have access to a private subnet.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[protectedIpAddressCount]: #protectedipaddresscount
#### [protectedIpAddressCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[registrationCount]: #registrationcount
#### [registrationCount]
A count of all registrations that have been created for this subnet.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[swipTransactionCount]: #swiptransactioncount
#### [swipTransactionCount]
A count of all the swip transactions associated with a subnet.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[unboundDescendantCount]: #unbounddescendantcount
#### [unboundDescendantCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[virtualGuestCount]: #virtualguestcount
#### [virtualGuestCount]
A count of the Virtual Servers using IP addresses on this subnet.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


