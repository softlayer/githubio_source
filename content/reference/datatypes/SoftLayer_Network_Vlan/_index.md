---
title: "SoftLayer_Network_Vlan"
description: "The SoftLayer_Network_Vlan data type models a single VLAN within SoftLayer's public and private networks. a Virtual LAN... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
---

# SoftLayer_Network_Vlan
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Vlan' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Vlan' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Vlan data type models a single VLAN within SoftLayer's public and private networks. a Virtual LAN is a structure that associates network interfaces on routers, switches, and servers in different locations to act as if they were on the same local network broadcast domain. VLANs are a central part of the SoftLayer network. They can determine how new IP subnets are routed and how individual servers communicate to each other. 

### External Links


* [Virtual LAN at Wikipedia](http://en.wikipedia.org/wiki/Virtual_LAN)



### associatedMethods

*  [SoftLayer_Network_Subnet::getNetworkVlan](/reference/services/SoftLayer_Network_Subnet/getNetworkVlan )
*  [SoftLayer_Network_Vlan::getObject](/reference/services/SoftLayer_Network_Vlan/getObject )
*  [SoftLayer_Network_Vlan::getVlanForIpAddress](/reference/services/SoftLayer_Network_Vlan/getVlanForIpAddress )
*  [SoftLayer_Network_Vlan::getPrivateVlanByIpAddress](/reference/services/SoftLayer_Network_Vlan/getPrivateVlanByIpAddress )
*  [SoftLayer_Network_Vlan::getPrivateVlan](/reference/services/SoftLayer_Network_Vlan/getPrivateVlan )
*  [SoftLayer_Network_Vlan::getPublicVlanByFqdn](/reference/services/SoftLayer_Network_Vlan/getPublicVlanByFqdn )





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
The internal identifier of the SoftLayer customer account that a VLAN is associated with.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
A VLAN's internal identifier. This should not be confused with the ''vlanNumber'' property, which is used in network configuration.  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a VLAN was last modified.  
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
The optional name for this VLAN  
<span class="type-label">Type: </span>**string**

-----
[note]: #note
#### [note]
The note for this vlan.  
<span class="type-label">Type: </span>**string**

-----
[primarySubnetId]: #primarysubnetid
#### [primarySubnetId]
The internal identifier of the primary subnet addressed on a VLAN.  
<span class="type-label">Type: </span>**integer**

-----
[vlanNumber]: #vlannumber
#### [vlanNumber]
A VLAN's number as recorded within the SoftLayer network. This is configured directly on SoftLayer's networking equipment and should not be confused with a VLAN's ''id'' property.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The SoftLayer customer account associated with a VLAN.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[additionalPrimarySubnets]: #additionalprimarysubnets
#### [additionalPrimarySubnets]
A VLAN's additional primary subnets. These are used to extend the number of servers attached to the VLAN by adding more ip addresses to the primary IP address pool.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**

-----
[attachedNetworkGateway]: #attachednetworkgateway
#### [attachedNetworkGateway]
The gateway this VLAN is inside of.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway </a>**

-----
[attachedNetworkGatewayFlag]: #attachednetworkgatewayflag
#### [attachedNetworkGatewayFlag]
Whether or not this VLAN is inside a gateway.  
<span class="type-label">Type: </span>**boolean**

-----
[attachedNetworkGatewayVlan]: #attachednetworkgatewayvlan
#### [attachedNetworkGatewayVlan]
The inside VLAN record if this VLAN is inside a network gateway.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway_Vlan'>SoftLayer_Network_Gateway_Vlan </a>**

-----
[billingItem]: #billingitem
#### [billingItem]
The billing item for a network vlan.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**

-----
[dedicatedFirewallFlag]: #dedicatedfirewallflag
#### [dedicatedFirewallFlag]
A flag indicating that a network vlan is on a Hardware Firewall (Dedicated).  
<span class="type-label">Type: </span>**integer**

-----
[extensionRouter]: #extensionrouter
#### [extensionRouter]
The extension router that a VLAN is associated with.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Router'>SoftLayer_Hardware_Router </a>**

-----
[firewallGuestNetworkComponents]: #firewallguestnetworkcomponents
#### [firewallGuestNetworkComponents]
A firewalled Vlan's network components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component_Firewall'>SoftLayer_Network_Component_Firewall[] </a>**

-----
[firewallInterfaces]: #firewallinterfaces
#### [firewallInterfaces]
A firewalled vlan's inbound/outbound interfaces.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Firewall_Module_Context_Interface'>SoftLayer_Network_Firewall_Module_Context_Interface[] </a>**

-----
[firewallNetworkComponents]: #firewallnetworkcomponents
#### [firewallNetworkComponents]
A firewalled Vlan's network components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component_Firewall'>SoftLayer_Network_Component_Firewall[] </a>**

-----
[firewallRules]: #firewallrules
#### [firewallRules]
The currently running rule set of a firewalled VLAN.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan_Firewall_Rule'>SoftLayer_Network_Vlan_Firewall_Rule[] </a>**

-----
[guestNetworkComponents]: #guestnetworkcomponents
#### [guestNetworkComponents]
The networking components that are connected to a VLAN.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component'>SoftLayer_Virtual_Guest_Network_Component[] </a>**

-----
[hardware]: #hardware
#### [hardware]
All of the hardware that exists on a VLAN. Hardware is associated with a VLAN by its networking components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[highAvailabilityFirewallFlag]: #highavailabilityfirewallflag
#### [highAvailabilityFirewallFlag]
  
<span class="type-label">Type: </span>**boolean**

-----
[localDiskStorageCapabilityFlag]: #localdiskstoragecapabilityflag
#### [localDiskStorageCapabilityFlag]
A flag indicating that a vlan can be assigned to a host that has local disk functionality.  
<span class="type-label">Type: </span>**boolean**

-----
[network]: #network
#### [network]
The network in which this VLAN resides.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network'>SoftLayer_Network </a>**

-----
[networkComponentTrunks]: #networkcomponenttrunks
#### [networkComponentTrunks]
The network components that are connected to this VLAN through a trunk.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component_Network_Vlan_Trunk'>SoftLayer_Network_Component_Network_Vlan_Trunk[] </a>**

-----
[networkComponents]: #networkcomponents
#### [networkComponents]
The networking components that are connected to a VLAN.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component[] </a>**

-----
[networkSpace]: #networkspace
#### [networkSpace]
Identifier to denote whether a VLAN is used for public or private connectivity.  
<span class="type-label">Type: </span>**string**

-----
[networkVlanFirewall]: #networkvlanfirewall
#### [networkVlanFirewall]
The Hardware Firewall (Dedicated) for a network vlan.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan_Firewall'>SoftLayer_Network_Vlan_Firewall </a>**

-----
[primaryRouter]: #primaryrouter
#### [primaryRouter]
The primary router that a VLAN is associated with. Every SoftLayer VLAN is connected to more than one router for greater network redundancy.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Router'>SoftLayer_Hardware_Router </a>**

-----
[primarySubnet]: #primarysubnet
#### [primarySubnet]
A VLAN's primary subnet. Each VLAN has at least one subnet, usually the subnet that is assigned to a server or new IP address block when it's purchased.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a>**

-----
[primarySubnetVersion6]: #primarysubnetversion6
#### [primarySubnetVersion6]
A VLAN's primary IPv6 subnet. Some VLAN's may not have a primary IPv6 subnet.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a>**

-----
[primarySubnets]: #primarysubnets
#### [primarySubnets]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**

-----
[privateNetworkGateways]: #privatenetworkgateways
#### [privateNetworkGateways]
The gateways this VLAN is the private VLAN of.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway[] </a>**

-----
[protectedIpAddresses]: #protectedipaddresses
#### [protectedIpAddresses]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>**

-----
[publicNetworkGateways]: #publicnetworkgateways
#### [publicNetworkGateways]
The gateways this VLAN is the public VLAN of.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway[] </a>**

-----
[sanStorageCapabilityFlag]: #sanstoragecapabilityflag
#### [sanStorageCapabilityFlag]
A flag indicating that a vlan can be assigned to a host that has SAN disk functionality.  
<span class="type-label">Type: </span>**boolean**

-----
[scaleVlans]: #scalevlans
#### [scaleVlans]
Collection of scale VLANs this VLAN applies to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Network_Vlan'>SoftLayer_Scale_Network_Vlan[] </a>**

-----
[secondaryRouter]: #secondaryrouter
#### [secondaryRouter]
The secondary router that a VLAN is associated with. Every SoftLayer VLAN is connected to more than one router for greater network redundancy.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**

-----
[secondarySubnets]: #secondarysubnets
#### [secondarySubnets]
The subnets that exist as secondary interfaces on a VLAN  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**

-----
[subnets]: #subnets
#### [subnets]
All of the subnets that exist as VLAN interfaces.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**

-----
[tagReferences]: #tagreferences
#### [tagReferences]
References to all tags for this VLAN.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Tag_Reference'>SoftLayer_Tag_Reference[] </a>**

-----
[totalPrimaryIpAddressCount]: #totalprimaryipaddresscount
#### [totalPrimaryIpAddressCount]
The number of primary IP addresses in a VLAN.  
<span class="type-label">Type: </span>**unsigned integer**

-----
[type]: #type
#### [type]
The type of this VLAN.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan_Type'>SoftLayer_Network_Vlan_Type </a>**

-----
[virtualGuests]: #virtualguests
#### [virtualGuests]
All of the Virtual Servers that are connected to a VLAN.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


## Count

-----
[additionalPrimarySubnetCount]: #additionalprimarysubnetcount
#### [additionalPrimarySubnetCount]
A count of a VLAN's additional primary subnets. These are used to extend the number of servers attached to the VLAN by adding more ip addresses to the primary IP address pool.   
<span class="type-label">Type: </span>**unsigned long**


-----
[firewallGuestNetworkComponentCount]: #firewallguestnetworkcomponentcount
#### [firewallGuestNetworkComponentCount]
A count of a firewalled Vlan's network components.   
<span class="type-label">Type: </span>**unsigned long**


-----
[firewallInterfaceCount]: #firewallinterfacecount
#### [firewallInterfaceCount]
A count of a firewalled vlan's inbound/outbound interfaces.   
<span class="type-label">Type: </span>**unsigned long**


-----
[firewallNetworkComponentCount]: #firewallnetworkcomponentcount
#### [firewallNetworkComponentCount]
A count of a firewalled Vlan's network components.   
<span class="type-label">Type: </span>**unsigned long**


-----
[firewallRuleCount]: #firewallrulecount
#### [firewallRuleCount]
A count of the currently running rule set of a firewalled VLAN.   
<span class="type-label">Type: </span>**unsigned long**


-----
[guestNetworkComponentCount]: #guestnetworkcomponentcount
#### [guestNetworkComponentCount]
A count of the networking components that are connected to a VLAN.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hardwareCount]: #hardwarecount
#### [hardwareCount]
A count of all of the hardware that exists on a VLAN. Hardware is associated with a VLAN by its networking components.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkComponentCount]: #networkcomponentcount
#### [networkComponentCount]
A count of the networking components that are connected to a VLAN.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkComponentTrunkCount]: #networkcomponenttrunkcount
#### [networkComponentTrunkCount]
A count of the network components that are connected to this VLAN through a trunk.   
<span class="type-label">Type: </span>**unsigned long**


-----
[primarySubnetCount]: #primarysubnetcount
#### [primarySubnetCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[privateNetworkGatewayCount]: #privatenetworkgatewaycount
#### [privateNetworkGatewayCount]
A count of the gateways this VLAN is the private VLAN of.   
<span class="type-label">Type: </span>**unsigned long**


-----
[protectedIpAddressCount]: #protectedipaddresscount
#### [protectedIpAddressCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[publicNetworkGatewayCount]: #publicnetworkgatewaycount
#### [publicNetworkGatewayCount]
A count of the gateways this VLAN is the public VLAN of.   
<span class="type-label">Type: </span>**unsigned long**


-----
[scaleVlanCount]: #scalevlancount
#### [scaleVlanCount]
A count of collection of scale VLANs this VLAN applies to.   
<span class="type-label">Type: </span>**unsigned long**


-----
[secondarySubnetCount]: #secondarysubnetcount
#### [secondarySubnetCount]
A count of the subnets that exist as secondary interfaces on a VLAN   
<span class="type-label">Type: </span>**unsigned long**


-----
[subnetCount]: #subnetcount
#### [subnetCount]
A count of all of the subnets that exist as VLAN interfaces.   
<span class="type-label">Type: </span>**unsigned long**


-----
[tagReferenceCount]: #tagreferencecount
#### [tagReferenceCount]
A count of references to all tags for this VLAN.   
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualGuestCount]: #virtualguestcount
#### [virtualGuestCount]
A count of all of the Virtual Servers that are connected to a VLAN.   
<span class="type-label">Type: </span>**unsigned long**

</div>


