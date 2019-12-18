---
title: "SoftLayer_Network_Vlan"
description: "Virtual LANs are an integral part of SoftLayer' s public and private networks. A VLAN is a networking concept in which n... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
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
Virtual LANs are an integral part of SoftLayer' s public and private networks. A VLAN is a networking concept in which network interfaces on different routers, switches, and servers act as if they're on the same local network broadcast domain. This kind of network segmentation helps keep SoftLayer customers' networks separate from each other and provides a convenient mechanism for routing new IP subnets to servers. They also enable easy IP address sharing and swapping between servers on the same VLAN. SoftLayer servers are provisioned on private VLANs per router on the public and private networks. 

The SoftLayer_Network_Vlan service controls these VLANs and provides relationships between VLANs, subnets, IP addresses, and network components. 

### External Links


* [Virtual LAN at Wikipedia](http://en.wikipedia.org/wiki/Virtual_LAN)




### seeAlso

* [SoftLayer_Network_Subnet](/reference/services/SoftLayer_Network_Subnet )


* [SoftLayer_Network_Subnet_IpAddress](/reference/services/SoftLayer_Network_Subnet_IpAddress )


        
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

#### [editObject](/reference/services/SoftLayer_Network_Vlan/editObject)
Edit a VLAN's properties

#### [getAccount](/reference/services/SoftLayer_Network_Vlan/getAccount)
Retrieve the SoftLayer customer account associated with a VLAN.

#### [getAdditionalPrimarySubnets](/reference/services/SoftLayer_Network_Vlan/getAdditionalPrimarySubnets)
Retrieve a VLAN's additional primary subnets. These are used to extend the number of servers attached to the VLAN by adding more ip addresses to the primary IP address pool.

#### [getAttachedNetworkGateway](/reference/services/SoftLayer_Network_Vlan/getAttachedNetworkGateway)
Retrieve the gateway this VLAN is inside of.

#### [getAttachedNetworkGatewayFlag](/reference/services/SoftLayer_Network_Vlan/getAttachedNetworkGatewayFlag)
Retrieve whether or not this VLAN is inside a gateway.

#### [getAttachedNetworkGatewayVlan](/reference/services/SoftLayer_Network_Vlan/getAttachedNetworkGatewayVlan)
Retrieve the inside VLAN record if this VLAN is inside a network gateway.

#### [getBillingItem](/reference/services/SoftLayer_Network_Vlan/getBillingItem)
Retrieve the billing item for a network vlan.

#### [getCancelFailureReasons](/reference/services/SoftLayer_Network_Vlan/getCancelFailureReasons)
Get a set of reasons why this VLAN may not be cancelled.

#### [getDedicatedFirewallFlag](/reference/services/SoftLayer_Network_Vlan/getDedicatedFirewallFlag)
Retrieve a flag indicating that a network vlan is on a Hardware Firewall (Dedicated).

#### [getExtensionRouter](/reference/services/SoftLayer_Network_Vlan/getExtensionRouter)
Retrieve the extension router that a VLAN is associated with.

#### [getFirewallGuestNetworkComponents](/reference/services/SoftLayer_Network_Vlan/getFirewallGuestNetworkComponents)
Retrieve a firewalled Vlan's network components.

#### [getFirewallInterfaces](/reference/services/SoftLayer_Network_Vlan/getFirewallInterfaces)
Retrieve a firewalled vlan's inbound/outbound interfaces.

#### [getFirewallNetworkComponents](/reference/services/SoftLayer_Network_Vlan/getFirewallNetworkComponents)
Retrieve a firewalled Vlan's network components.

#### [getFirewallProtectableIpAddresses](/reference/services/SoftLayer_Network_Vlan/getFirewallProtectableIpAddresses)
Get the IP addresses associated with this server that are protectable by a network component firewall.

#### [getFirewallProtectableSubnets](/reference/services/SoftLayer_Network_Vlan/getFirewallProtectableSubnets)
Get the subnets associated with this server that are protectable by a network component firewall.

#### [getFirewallRules](/reference/services/SoftLayer_Network_Vlan/getFirewallRules)
Retrieve the currently running rule set of a firewalled VLAN.

#### [getGuestNetworkComponents](/reference/services/SoftLayer_Network_Vlan/getGuestNetworkComponents)
Retrieve the networking components that are connected to a VLAN.

#### [getHardware](/reference/services/SoftLayer_Network_Vlan/getHardware)
Retrieve all of the hardware that exists on a VLAN. Hardware is associated with a VLAN by its networking components.

#### [getHighAvailabilityFirewallFlag](/reference/services/SoftLayer_Network_Vlan/getHighAvailabilityFirewallFlag)


#### [getLocalDiskStorageCapabilityFlag](/reference/services/SoftLayer_Network_Vlan/getLocalDiskStorageCapabilityFlag)
Retrieve a flag indicating that a vlan can be assigned to a host that has local disk functionality.

#### [getNetwork](/reference/services/SoftLayer_Network_Vlan/getNetwork)
Retrieve the network in which this VLAN resides.

#### [getNetworkComponentTrunks](/reference/services/SoftLayer_Network_Vlan/getNetworkComponentTrunks)
Retrieve the network components that are connected to this VLAN through a trunk.

#### [getNetworkComponents](/reference/services/SoftLayer_Network_Vlan/getNetworkComponents)
Retrieve the networking components that are connected to a VLAN.

#### [getNetworkSpace](/reference/services/SoftLayer_Network_Vlan/getNetworkSpace)
Retrieve identifier to denote whether a VLAN is used for public or private connectivity.

#### [getNetworkVlanFirewall](/reference/services/SoftLayer_Network_Vlan/getNetworkVlanFirewall)
Retrieve the Hardware Firewall (Dedicated) for a network vlan.

#### [getObject](/reference/services/SoftLayer_Network_Vlan/getObject)
Retrieve a SoftLayer_Network_Vlan record.

#### [getPrimaryRouter](/reference/services/SoftLayer_Network_Vlan/getPrimaryRouter)
Retrieve the primary router that a VLAN is associated with. Every SoftLayer VLAN is connected to more than one router for greater network redundancy.

#### [getPrimarySubnet](/reference/services/SoftLayer_Network_Vlan/getPrimarySubnet)
Retrieve a VLAN's primary subnet. Each VLAN has at least one subnet, usually the subnet that is assigned to a server or new IP address block when it's purchased.

#### [getPrimarySubnetVersion6](/reference/services/SoftLayer_Network_Vlan/getPrimarySubnetVersion6)
Retrieve a VLAN's primary IPv6 subnet. Some VLAN's may not have a primary IPv6 subnet.

#### [getPrimarySubnets](/reference/services/SoftLayer_Network_Vlan/getPrimarySubnets)


#### [getPrivateNetworkGateways](/reference/services/SoftLayer_Network_Vlan/getPrivateNetworkGateways)
Retrieve the gateways this VLAN is the private VLAN of.

#### [getPrivateVlan](/reference/services/SoftLayer_Network_Vlan/getPrivateVlan)
Retrieve a VLAN's associated private network VLAN.

#### [getPrivateVlanByIpAddress](/reference/services/SoftLayer_Network_Vlan/getPrivateVlanByIpAddress)
Retrieve the private network VLAN associated with an IP address.

#### [getProtectedIpAddresses](/reference/services/SoftLayer_Network_Vlan/getProtectedIpAddresses)


#### [getPublicNetworkGateways](/reference/services/SoftLayer_Network_Vlan/getPublicNetworkGateways)
Retrieve the gateways this VLAN is the public VLAN of.

#### [getPublicVlanByFqdn](/reference/services/SoftLayer_Network_Vlan/getPublicVlanByFqdn)
Retrieve a server's public VLAN based on it's fully-qualified domain name

#### [getReverseDomainRecords](/reference/services/SoftLayer_Network_Vlan/getReverseDomainRecords)
Retrieve all reverse DNS records associated with a VLAN.

#### [getSanStorageCapabilityFlag](/reference/services/SoftLayer_Network_Vlan/getSanStorageCapabilityFlag)
Retrieve a flag indicating that a vlan can be assigned to a host that has SAN disk functionality.

#### [getScaleVlans](/reference/services/SoftLayer_Network_Vlan/getScaleVlans)
Retrieve collection of scale VLANs this VLAN applies to.

#### [getSecondaryRouter](/reference/services/SoftLayer_Network_Vlan/getSecondaryRouter)
Retrieve the secondary router that a VLAN is associated with. Every SoftLayer VLAN is connected to more than one router for greater network redundancy.

#### [getSecondarySubnets](/reference/services/SoftLayer_Network_Vlan/getSecondarySubnets)
Retrieve the subnets that exist as secondary interfaces on a VLAN

#### [getSubnets](/reference/services/SoftLayer_Network_Vlan/getSubnets)
Retrieve all of the subnets that exist as VLAN interfaces.

#### [getTagReferences](/reference/services/SoftLayer_Network_Vlan/getTagReferences)
Retrieve references to all tags for this VLAN.

#### [getTotalPrimaryIpAddressCount](/reference/services/SoftLayer_Network_Vlan/getTotalPrimaryIpAddressCount)
Retrieve the number of primary IP addresses in a VLAN.

#### [getType](/reference/services/SoftLayer_Network_Vlan/getType)
Retrieve the type of this VLAN.

#### [getVirtualGuests](/reference/services/SoftLayer_Network_Vlan/getVirtualGuests)
Retrieve all of the Virtual Servers that are connected to a VLAN.

#### [getVlanForIpAddress](/reference/services/SoftLayer_Network_Vlan/getVlanForIpAddress)
Retrieve an IP addresses's associated VLAN.

#### [setTags](/reference/services/SoftLayer_Network_Vlan/setTags)


#### [updateFirewallIntraVlanCommunication](/reference/services/SoftLayer_Network_Vlan/updateFirewallIntraVlanCommunication)
Update a VLAN's firewall to allow or disallow intra-VLAN communication.

#### [upgrade](/reference/services/SoftLayer_Network_Vlan/upgrade)
Convert the VLAN to a paid resource. That is, from an Automatic to a Premium VLAN.

</div>

