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
### external links
        Array
(
    [url] => http://en.wikipedia.org/wiki/Virtual_LAN
    [description] => Virtual LAN at Wikipedia
)
1        
### seeAlso
        SoftLayer_Network_Subnet1        SoftLayer_Network_Subnet_IpAddress1                
        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit a VLAN's properties</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer customer account associated with a VLAN.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getAdditionalPrimarySubnets'> getAdditionalPrimarySubnets</a> </span>
            <div class='views-field-body'>Retrieve a VLAN's additional primary subnets. These are used to extend the number of servers attached to the VLAN by adding more ip addresses to the primary IP address pool.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getAttachedNetworkGateway'> getAttachedNetworkGateway</a> </span>
            <div class='views-field-body'>Retrieve the gateway this VLAN is inside of.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getAttachedNetworkGatewayFlag'> getAttachedNetworkGatewayFlag</a> </span>
            <div class='views-field-body'>Retrieve whether or not this VLAN is inside a gateway.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getAttachedNetworkGatewayVlan'> getAttachedNetworkGatewayVlan</a> </span>
            <div class='views-field-body'>Retrieve the inside VLAN record if this VLAN is inside a network gateway.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getBillingItem'> getBillingItem</a> </span>
            <div class='views-field-body'>Retrieve the billing item for a network vlan.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getCancelFailureReasons'> getCancelFailureReasons</a> </span>
            <div class='views-field-body'>Get a set of reasons why this VLAN may not be cancelled.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getDedicatedFirewallFlag'> getDedicatedFirewallFlag</a> </span>
            <div class='views-field-body'>Retrieve a flag indicating that a network vlan is on a Hardware Firewall (Dedicated).</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getExtensionRouter'> getExtensionRouter</a> </span>
            <div class='views-field-body'>Retrieve the extension router that a VLAN is associated with.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getFirewallGuestNetworkComponents'> getFirewallGuestNetworkComponents</a> </span>
            <div class='views-field-body'>Retrieve a firewalled Vlan's network components.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getFirewallInterfaces'> getFirewallInterfaces</a> </span>
            <div class='views-field-body'>Retrieve a firewalled vlan's inbound/outbound interfaces.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getFirewallNetworkComponents'> getFirewallNetworkComponents</a> </span>
            <div class='views-field-body'>Retrieve a firewalled Vlan's network components.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getFirewallProtectableIpAddresses'> getFirewallProtectableIpAddresses</a> </span>
            <div class='views-field-body'>Get the IP addresses associated with this server that are protectable by a network component firewall.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getFirewallProtectableSubnets'> getFirewallProtectableSubnets</a> </span>
            <div class='views-field-body'>Get the subnets associated with this server that are protectable by a network component firewall.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getFirewallRules'> getFirewallRules</a> </span>
            <div class='views-field-body'>Retrieve the currently running rule set of a firewalled VLAN.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getGuestNetworkComponents'> getGuestNetworkComponents</a> </span>
            <div class='views-field-body'>Retrieve the networking components that are connected to a VLAN.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getHardware'> getHardware</a> </span>
            <div class='views-field-body'>Retrieve all of the hardware that exists on a VLAN. Hardware is associated with a VLAN by its networking components.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getHighAvailabilityFirewallFlag'> getHighAvailabilityFirewallFlag</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getLocalDiskStorageCapabilityFlag'> getLocalDiskStorageCapabilityFlag</a> </span>
            <div class='views-field-body'>Retrieve a flag indicating that a vlan can be assigned to a host that has local disk functionality.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getNetwork'> getNetwork</a> </span>
            <div class='views-field-body'>Retrieve the network in which this VLAN resides.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getNetworkComponentTrunks'> getNetworkComponentTrunks</a> </span>
            <div class='views-field-body'>Retrieve the network components that are connected to this VLAN through a trunk.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getNetworkComponents'> getNetworkComponents</a> </span>
            <div class='views-field-body'>Retrieve the networking components that are connected to a VLAN.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getNetworkSpace'> getNetworkSpace</a> </span>
            <div class='views-field-body'>Retrieve identifier to denote whether a VLAN is used for public or private connectivity.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getNetworkVlanFirewall'> getNetworkVlanFirewall</a> </span>
            <div class='views-field-body'>Retrieve the Hardware Firewall (Dedicated) for a network vlan.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_Vlan record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getPrimaryRouter'> getPrimaryRouter</a> </span>
            <div class='views-field-body'>Retrieve the primary router that a VLAN is associated with. Every SoftLayer VLAN is connected to more than one router for greater network redundancy.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getPrimarySubnet'> getPrimarySubnet</a> </span>
            <div class='views-field-body'>Retrieve a VLAN's primary subnet. Each VLAN has at least one subnet, usually the subnet that is assigned to a server or new IP address block when it's purchased.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getPrimarySubnetVersion6'> getPrimarySubnetVersion6</a> </span>
            <div class='views-field-body'>Retrieve a VLAN's primary IPv6 subnet. Some VLAN's may not have a primary IPv6 subnet.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getPrimarySubnets'> getPrimarySubnets</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getPrivateNetworkGateways'> getPrivateNetworkGateways</a> </span>
            <div class='views-field-body'>Retrieve the gateways this VLAN is the private VLAN of.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getPrivateVlan'> getPrivateVlan</a> </span>
            <div class='views-field-body'>Retrieve a VLAN's associated private network VLAN.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getPrivateVlanByIpAddress'> getPrivateVlanByIpAddress</a> </span>
            <div class='views-field-body'>Retrieve the private network VLAN associated with an IP address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getProtectedIpAddresses'> getProtectedIpAddresses</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getPublicNetworkGateways'> getPublicNetworkGateways</a> </span>
            <div class='views-field-body'>Retrieve the gateways this VLAN is the public VLAN of.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getPublicVlanByFqdn'> getPublicVlanByFqdn</a> </span>
            <div class='views-field-body'>Retrieve a server's public VLAN based on it's fully-qualified domain name</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getReverseDomainRecords'> getReverseDomainRecords</a> </span>
            <div class='views-field-body'>Retrieve all reverse DNS records associated with a VLAN.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getSanStorageCapabilityFlag'> getSanStorageCapabilityFlag</a> </span>
            <div class='views-field-body'>Retrieve a flag indicating that a vlan can be assigned to a host that has SAN disk functionality.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getScaleVlans'> getScaleVlans</a> </span>
            <div class='views-field-body'>Retrieve collection of scale VLANs this VLAN applies to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getSecondaryRouter'> getSecondaryRouter</a> </span>
            <div class='views-field-body'>Retrieve the secondary router that a VLAN is associated with. Every SoftLayer VLAN is connected to more than one router for greater network redundancy.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getSecondarySubnets'> getSecondarySubnets</a> </span>
            <div class='views-field-body'>Retrieve the subnets that exist as secondary interfaces on a VLAN</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getSubnets'> getSubnets</a> </span>
            <div class='views-field-body'>Retrieve all of the subnets that exist as VLAN interfaces.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getTagReferences'> getTagReferences</a> </span>
            <div class='views-field-body'>Retrieve references to all tags for this VLAN.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getTotalPrimaryIpAddressCount'> getTotalPrimaryIpAddressCount</a> </span>
            <div class='views-field-body'>Retrieve the number of primary IP addresses in a VLAN.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getType'> getType</a> </span>
            <div class='views-field-body'>Retrieve the type of this VLAN.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getVirtualGuests'> getVirtualGuests</a> </span>
            <div class='views-field-body'>Retrieve all of the Virtual Servers that are connected to a VLAN.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/getVlanForIpAddress'> getVlanForIpAddress</a> </span>
            <div class='views-field-body'>Retrieve an IP addresses's associated VLAN.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/setTags'> setTags</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan/updateFirewallIntraVlanCommunication'> updateFirewallIntraVlanCommunication</a> </span>
            <div class='views-field-body'>Update a VLAN's firewall to allow or disallow intra-VLAN communication.</div>
        </div>
        </div>
</div>

