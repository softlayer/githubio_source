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
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [editObject](/reference/services/SoftLayer_Network_Vlan/editObject)
Edit a VLAN's properties

</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Network_Vlan/getAccount)
Retrieve the SoftLayer customer account associated with a VLAN.

</div>

<div class="method-row">

#### [getAdditionalPrimarySubnets](/reference/services/SoftLayer_Network_Vlan/getAdditionalPrimarySubnets)
Retrieve a VLAN's additional primary subnets. These are used to extend the number of servers attached to the VLAN by adding more ip addresses to the primary IP address pool.

</div>

<div class="method-row">

#### [getAttachedNetworkGateway](/reference/services/SoftLayer_Network_Vlan/getAttachedNetworkGateway)
Retrieve the gateway this VLAN is inside of.

</div>

<div class="method-row">

#### [getAttachedNetworkGatewayFlag](/reference/services/SoftLayer_Network_Vlan/getAttachedNetworkGatewayFlag)
Retrieve whether or not this VLAN is inside a gateway.

</div>

<div class="method-row">

#### [getAttachedNetworkGatewayVlan](/reference/services/SoftLayer_Network_Vlan/getAttachedNetworkGatewayVlan)
Retrieve the inside VLAN record if this VLAN is inside a network gateway.

</div>

<div class="method-row">

#### [getBillingItem](/reference/services/SoftLayer_Network_Vlan/getBillingItem)
Retrieve the billing item for a network vlan.

</div>

<div class="method-row">

#### [getCancelFailureReasons](/reference/services/SoftLayer_Network_Vlan/getCancelFailureReasons)
Get a set of reasons why this VLAN may not be cancelled.

</div>

<div class="method-row">

#### [getDedicatedFirewallFlag](/reference/services/SoftLayer_Network_Vlan/getDedicatedFirewallFlag)
Retrieve a flag indicating that a network vlan is on a Hardware Firewall (Dedicated).

</div>

<div class="method-row">

#### [getExtensionRouter](/reference/services/SoftLayer_Network_Vlan/getExtensionRouter)
Retrieve the extension router that a VLAN is associated with.

</div>

<div class="method-row">

#### [getFirewallGuestNetworkComponents](/reference/services/SoftLayer_Network_Vlan/getFirewallGuestNetworkComponents)
Retrieve a firewalled Vlan's network components.

</div>

<div class="method-row">

#### [getFirewallInterfaces](/reference/services/SoftLayer_Network_Vlan/getFirewallInterfaces)
Retrieve a firewalled vlan's inbound/outbound interfaces.

</div>

<div class="method-row">

#### [getFirewallNetworkComponents](/reference/services/SoftLayer_Network_Vlan/getFirewallNetworkComponents)
Retrieve a firewalled Vlan's network components.

</div>

<div class="method-row">

#### [getFirewallProtectableIpAddresses](/reference/services/SoftLayer_Network_Vlan/getFirewallProtectableIpAddresses)
Get the IP addresses associated with this server that are protectable by a network component firewall.

</div>

<div class="method-row">

#### [getFirewallProtectableSubnets](/reference/services/SoftLayer_Network_Vlan/getFirewallProtectableSubnets)
Get the subnets associated with this server that are protectable by a network component firewall.

</div>

<div class="method-row">

#### [getFirewallRules](/reference/services/SoftLayer_Network_Vlan/getFirewallRules)
Retrieve the currently running rule set of a firewalled VLAN.

</div>

<div class="method-row">

#### [getGuestNetworkComponents](/reference/services/SoftLayer_Network_Vlan/getGuestNetworkComponents)
Retrieve the networking components that are connected to a VLAN.

</div>

<div class="method-row">

#### [getHardware](/reference/services/SoftLayer_Network_Vlan/getHardware)
Retrieve all of the hardware that exists on a VLAN. Hardware is associated with a VLAN by its networking components.

</div>

<div class="method-row">

#### [getHighAvailabilityFirewallFlag](/reference/services/SoftLayer_Network_Vlan/getHighAvailabilityFirewallFlag)


</div>

<div class="method-row">

#### [getLocalDiskStorageCapabilityFlag](/reference/services/SoftLayer_Network_Vlan/getLocalDiskStorageCapabilityFlag)
Retrieve a flag indicating that a vlan can be assigned to a host that has local disk functionality.

</div>

<div class="method-row">

#### [getNetwork](/reference/services/SoftLayer_Network_Vlan/getNetwork)
Retrieve the network in which this VLAN resides.

</div>

<div class="method-row">

#### [getNetworkComponentTrunks](/reference/services/SoftLayer_Network_Vlan/getNetworkComponentTrunks)
Retrieve the network components that are connected to this VLAN through a trunk.

</div>

<div class="method-row">

#### [getNetworkComponents](/reference/services/SoftLayer_Network_Vlan/getNetworkComponents)
Retrieve the networking components that are connected to a VLAN.

</div>

<div class="method-row">

#### [getNetworkComponentsTrunkable](/reference/services/SoftLayer_Network_Vlan/getNetworkComponentsTrunkable)
Retrieve the viable trunking targets of this VLAN. Viable targets include accessible components of assigned hardware in the same pod and network as this VLAN, which are not already natively attached nor trunked.

</div>

<div class="method-row">

#### [getNetworkSpace](/reference/services/SoftLayer_Network_Vlan/getNetworkSpace)
Retrieve identifier to denote whether a VLAN is used for public or private connectivity.

</div>

<div class="method-row">

#### [getNetworkVlanFirewall](/reference/services/SoftLayer_Network_Vlan/getNetworkVlanFirewall)
Retrieve the Hardware Firewall (Dedicated) for a network vlan.

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_Vlan/getObject)
Retrieve a SoftLayer_Network_Vlan record.

</div>

<div class="method-row">

#### [getPrimaryRouter](/reference/services/SoftLayer_Network_Vlan/getPrimaryRouter)
Retrieve the primary router that a VLAN is associated with. Every SoftLayer VLAN is connected to more than one router for greater network redundancy.

</div>

<div class="method-row">

#### [getPrimarySubnet](/reference/services/SoftLayer_Network_Vlan/getPrimarySubnet)
Retrieve a VLAN's primary subnet. Each VLAN has at least one subnet, usually the subnet that is assigned to a server or new IP address block when it's purchased.

</div>

<div class="method-row">

#### [getPrimarySubnetVersion6](/reference/services/SoftLayer_Network_Vlan/getPrimarySubnetVersion6)
Retrieve a VLAN's primary IPv6 subnet. Some VLAN's may not have a primary IPv6 subnet.

</div>

<div class="method-row">

#### [getPrimarySubnets](/reference/services/SoftLayer_Network_Vlan/getPrimarySubnets)


</div>

<div class="method-row">

#### [getPrivateNetworkGateways](/reference/services/SoftLayer_Network_Vlan/getPrivateNetworkGateways)
Retrieve the gateways this VLAN is the private VLAN of.

</div>

<div class="method-row">

#### [getPrivateVlan](/reference/services/SoftLayer_Network_Vlan/getPrivateVlan)
Retrieve a VLAN's associated private network VLAN.

</div>

<div class="method-row deprecated">

#### [getPrivateVlanByIpAddress](/reference/services/SoftLayer_Network_Vlan/getPrivateVlanByIpAddress)
Retrieve the private network VLAN associated with an IP address.

<span class="deprecation-label">Deprecated  </span>


</div>

<div class="method-row">

#### [getProtectedIpAddresses](/reference/services/SoftLayer_Network_Vlan/getProtectedIpAddresses)


</div>

<div class="method-row">

#### [getPublicNetworkGateways](/reference/services/SoftLayer_Network_Vlan/getPublicNetworkGateways)
Retrieve the gateways this VLAN is the public VLAN of.

</div>

<div class="method-row">

#### [getPublicVlanByFqdn](/reference/services/SoftLayer_Network_Vlan/getPublicVlanByFqdn)
Retrieve a server's public VLAN based on it's fully-qualified domain name

</div>

<div class="method-row">

#### [getReverseDomainRecords](/reference/services/SoftLayer_Network_Vlan/getReverseDomainRecords)
Retrieve all reverse DNS records associated with a VLAN.

</div>

<div class="method-row">

#### [getSanStorageCapabilityFlag](/reference/services/SoftLayer_Network_Vlan/getSanStorageCapabilityFlag)
Retrieve a flag indicating that a vlan can be assigned to a host that has SAN disk functionality.

</div>

<div class="method-row">

#### [getScaleVlans](/reference/services/SoftLayer_Network_Vlan/getScaleVlans)
Retrieve collection of scale VLANs this VLAN applies to.

</div>

<div class="method-row">

#### [getSecondaryRouter](/reference/services/SoftLayer_Network_Vlan/getSecondaryRouter)
Retrieve the secondary router that a VLAN is associated with. Every SoftLayer VLAN is connected to more than one router for greater network redundancy.

</div>

<div class="method-row">

#### [getSecondarySubnets](/reference/services/SoftLayer_Network_Vlan/getSecondarySubnets)
Retrieve the subnets that exist as secondary interfaces on a VLAN

</div>

<div class="method-row">

#### [getSubnets](/reference/services/SoftLayer_Network_Vlan/getSubnets)
Retrieve all of the subnets that exist as VLAN interfaces.

</div>

<div class="method-row">

#### [getTagReferences](/reference/services/SoftLayer_Network_Vlan/getTagReferences)
Retrieve references to all tags for this VLAN.

</div>

<div class="method-row">

#### [getTotalPrimaryIpAddressCount](/reference/services/SoftLayer_Network_Vlan/getTotalPrimaryIpAddressCount)
Retrieve the number of primary IP addresses in a VLAN.

</div>

<div class="method-row">

#### [getType](/reference/services/SoftLayer_Network_Vlan/getType)
Retrieve the type of this VLAN.

</div>

<div class="method-row">

#### [getVirtualGuests](/reference/services/SoftLayer_Network_Vlan/getVirtualGuests)
Retrieve all of the Virtual Servers that are connected to a VLAN.

</div>

<div class="method-row">

#### [getVlanForIpAddress](/reference/services/SoftLayer_Network_Vlan/getVlanForIpAddress)
Retrieve an IP addresses's associated VLAN.

</div>

<div class="method-row">

#### [setTags](/reference/services/SoftLayer_Network_Vlan/setTags)


</div>

<div class="method-row">

#### [updateFirewallIntraVlanCommunication](/reference/services/SoftLayer_Network_Vlan/updateFirewallIntraVlanCommunication)
Update a VLAN's firewall to allow or disallow intra-VLAN communication.

</div>

<div class="method-row">

#### [upgrade](/reference/services/SoftLayer_Network_Vlan/upgrade)
Convert the VLAN to a paid resource. That is, from an Automatic to a Premium VLAN.

</div>
</div>

</div>

