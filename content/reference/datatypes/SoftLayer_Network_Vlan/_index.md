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
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Vlan' >Datatype</a></li>
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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#accountId" name=accountId>accountId</a></span>
            <div class='views-field-body'>The internal identifier of the SoftLayer customer account that a VLAN is associated with. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A VLAN's internal identifier. This should not be confused with the ''vlanNumber'' property, which is used in network configuration. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>The date a VLAN was last modified. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>The optional name for this VLAN </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#note" name=note>note</a></span>
            <div class='views-field-body'>The note for this vlan. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#primarySubnetId" name=primarySubnetId>primarySubnetId</a></span>
            <div class='views-field-body'>The internal identifier of the primary subnet addressed on a VLAN. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#vlanNumber" name=vlanNumber>vlanNumber</a></span>
            <div class='views-field-body'>A VLAN's number as recorded within the SoftLayer network. This is configured directly on SoftLayer's networking equipment and should not be confused with a VLAN's ''id'' property. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'>The SoftLayer customer account associated with a VLAN. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#additionalPrimarySubnets" name=additionalPrimarySubnets>additionalPrimarySubnets</a></span>
            <div class='views-field-body'>A VLAN's additional primary subnets. These are used to extend the number of servers attached to the VLAN by adding more ip addresses to the primary IP address pool. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#attachedNetworkGateway" name=attachedNetworkGateway>attachedNetworkGateway</a></span>
            <div class='views-field-body'>The gateway this VLAN is inside of. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#attachedNetworkGatewayFlag" name=attachedNetworkGatewayFlag>attachedNetworkGatewayFlag</a></span>
            <div class='views-field-body'>Whether or not this VLAN is inside a gateway. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#attachedNetworkGatewayVlan" name=attachedNetworkGatewayVlan>attachedNetworkGatewayVlan</a></span>
            <div class='views-field-body'>The inside VLAN record if this VLAN is inside a network gateway. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Gateway_Vlan'>SoftLayer_Network_Gateway_Vlan </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingItem" name=billingItem>billingItem</a></span>
            <div class='views-field-body'>The billing item for a network vlan. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#dedicatedFirewallFlag" name=dedicatedFirewallFlag>dedicatedFirewallFlag</a></span>
            <div class='views-field-body'>A flag indicating that a network vlan is on a Hardware Firewall (Dedicated). </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#extensionRouter" name=extensionRouter>extensionRouter</a></span>
            <div class='views-field-body'>The extension router that a VLAN is associated with. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Router'>SoftLayer_Hardware_Router </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#firewallGuestNetworkComponents" name=firewallGuestNetworkComponents>firewallGuestNetworkComponents</a></span>
            <div class='views-field-body'>A firewalled Vlan's network components. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Component_Firewall'>SoftLayer_Network_Component_Firewall[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#firewallInterfaces" name=firewallInterfaces>firewallInterfaces</a></span>
            <div class='views-field-body'>A firewalled vlan's inbound/outbound interfaces. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Firewall_Module_Context_Interface'>SoftLayer_Network_Firewall_Module_Context_Interface[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#firewallNetworkComponents" name=firewallNetworkComponents>firewallNetworkComponents</a></span>
            <div class='views-field-body'>A firewalled Vlan's network components. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Component_Firewall'>SoftLayer_Network_Component_Firewall[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#firewallRules" name=firewallRules>firewallRules</a></span>
            <div class='views-field-body'>The currently running rule set of a firewalled VLAN. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Vlan_Firewall_Rule'>SoftLayer_Network_Vlan_Firewall_Rule[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#guestNetworkComponents" name=guestNetworkComponents>guestNetworkComponents</a></span>
            <div class='views-field-body'>The networking components that are connected to a VLAN. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component'>SoftLayer_Virtual_Guest_Network_Component[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardware" name=hardware>hardware</a></span>
            <div class='views-field-body'>All of the hardware that exists on a VLAN. Hardware is associated with a VLAN by its networking components. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#highAvailabilityFirewallFlag" name=highAvailabilityFirewallFlag>highAvailabilityFirewallFlag</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#localDiskStorageCapabilityFlag" name=localDiskStorageCapabilityFlag>localDiskStorageCapabilityFlag</a></span>
            <div class='views-field-body'>A flag indicating that a vlan can be assigned to a host that has local disk functionality. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#network" name=network>network</a></span>
            <div class='views-field-body'>The network in which this VLAN resides. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network'>SoftLayer_Network </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkComponentTrunks" name=networkComponentTrunks>networkComponentTrunks</a></span>
            <div class='views-field-body'>The network components that are connected to this VLAN through a trunk. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Component_Network_Vlan_Trunk'>SoftLayer_Network_Component_Network_Vlan_Trunk[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkComponents" name=networkComponents>networkComponents</a></span>
            <div class='views-field-body'>The networking components that are connected to a VLAN. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkSpace" name=networkSpace>networkSpace</a></span>
            <div class='views-field-body'>Identifier to denote whether a VLAN is used for public or private connectivity. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkVlanFirewall" name=networkVlanFirewall>networkVlanFirewall</a></span>
            <div class='views-field-body'>The Hardware Firewall (Dedicated) for a network vlan. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Vlan_Firewall'>SoftLayer_Network_Vlan_Firewall </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#primaryRouter" name=primaryRouter>primaryRouter</a></span>
            <div class='views-field-body'>The primary router that a VLAN is associated with. Every SoftLayer VLAN is connected to more than one router for greater network redundancy. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Router'>SoftLayer_Hardware_Router </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#primarySubnet" name=primarySubnet>primarySubnet</a></span>
            <div class='views-field-body'>A VLAN's primary subnet. Each VLAN has at least one subnet, usually the subnet that is assigned to a server or new IP address block when it's purchased. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#primarySubnetVersion6" name=primarySubnetVersion6>primarySubnetVersion6</a></span>
            <div class='views-field-body'>A VLAN's primary IPv6 subnet. Some VLAN's may not have a primary IPv6 subnet. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#primarySubnets" name=primarySubnets>primarySubnets</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#privateNetworkGateways" name=privateNetworkGateways>privateNetworkGateways</a></span>
            <div class='views-field-body'>The gateways this VLAN is the private VLAN of. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#protectedIpAddresses" name=protectedIpAddresses>protectedIpAddresses</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#publicNetworkGateways" name=publicNetworkGateways>publicNetworkGateways</a></span>
            <div class='views-field-body'>The gateways this VLAN is the public VLAN of. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#sanStorageCapabilityFlag" name=sanStorageCapabilityFlag>sanStorageCapabilityFlag</a></span>
            <div class='views-field-body'>A flag indicating that a vlan can be assigned to a host that has SAN disk functionality. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#scaleVlans" name=scaleVlans>scaleVlans</a></span>
            <div class='views-field-body'>Collection of scale VLANs this VLAN applies to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Scale_Network_Vlan'>SoftLayer_Scale_Network_Vlan[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#secondaryRouter" name=secondaryRouter>secondaryRouter</a></span>
            <div class='views-field-body'>The secondary router that a VLAN is associated with. Every SoftLayer VLAN is connected to more than one router for greater network redundancy. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#secondarySubnets" name=secondarySubnets>secondarySubnets</a></span>
            <div class='views-field-body'>The subnets that exist as secondary interfaces on a VLAN </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#subnets" name=subnets>subnets</a></span>
            <div class='views-field-body'>All of the subnets that exist as VLAN interfaces. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#tagReferences" name=tagReferences>tagReferences</a></span>
            <div class='views-field-body'>References to all tags for this VLAN. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Tag_Reference'>SoftLayer_Tag_Reference[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#totalPrimaryIpAddressCount" name=totalPrimaryIpAddressCount>totalPrimaryIpAddressCount</a></span>
            <div class='views-field-body'>The number of primary IP addresses in a VLAN. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsigned integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#type" name=type>type</a></span>
            <div class='views-field-body'>The type of this VLAN. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Vlan_Type'>SoftLayer_Network_Vlan_Type </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#virtualGuests" name=virtualGuests>virtualGuests</a></span>
            <div class='views-field-body'>All of the Virtual Servers that are connected to a VLAN. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#additionalPrimarySubnetCount" name=additionalPrimarySubnetCount>additionalPrimarySubnetCount</a></span>
            <div class='views-field-body'>A count of a VLAN's additional primary subnets. These are used to extend the number of servers attached to the VLAN by adding more ip addresses to the primary IP address pool. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#firewallGuestNetworkComponentCount" name=firewallGuestNetworkComponentCount>firewallGuestNetworkComponentCount</a></span>
            <div class='views-field-body'>A count of a firewalled Vlan's network components. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#firewallInterfaceCount" name=firewallInterfaceCount>firewallInterfaceCount</a></span>
            <div class='views-field-body'>A count of a firewalled vlan's inbound/outbound interfaces. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#firewallNetworkComponentCount" name=firewallNetworkComponentCount>firewallNetworkComponentCount</a></span>
            <div class='views-field-body'>A count of a firewalled Vlan's network components. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#firewallRuleCount" name=firewallRuleCount>firewallRuleCount</a></span>
            <div class='views-field-body'>A count of the currently running rule set of a firewalled VLAN. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#guestNetworkComponentCount" name=guestNetworkComponentCount>guestNetworkComponentCount</a></span>
            <div class='views-field-body'>A count of the networking components that are connected to a VLAN. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareCount" name=hardwareCount>hardwareCount</a></span>
            <div class='views-field-body'>A count of all of the hardware that exists on a VLAN. Hardware is associated with a VLAN by its networking components. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkComponentCount" name=networkComponentCount>networkComponentCount</a></span>
            <div class='views-field-body'>A count of the networking components that are connected to a VLAN. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkComponentTrunkCount" name=networkComponentTrunkCount>networkComponentTrunkCount</a></span>
            <div class='views-field-body'>A count of the network components that are connected to this VLAN through a trunk. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#primarySubnetCount" name=primarySubnetCount>primarySubnetCount</a></span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#privateNetworkGatewayCount" name=privateNetworkGatewayCount>privateNetworkGatewayCount</a></span>
            <div class='views-field-body'>A count of the gateways this VLAN is the private VLAN of. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#protectedIpAddressCount" name=protectedIpAddressCount>protectedIpAddressCount</a></span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#publicNetworkGatewayCount" name=publicNetworkGatewayCount>publicNetworkGatewayCount</a></span>
            <div class='views-field-body'>A count of the gateways this VLAN is the public VLAN of. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#scaleVlanCount" name=scaleVlanCount>scaleVlanCount</a></span>
            <div class='views-field-body'>A count of collection of scale VLANs this VLAN applies to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#secondarySubnetCount" name=secondarySubnetCount>secondarySubnetCount</a></span>
            <div class='views-field-body'>A count of the subnets that exist as secondary interfaces on a VLAN </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#subnetCount" name=subnetCount>subnetCount</a></span>
            <div class='views-field-body'>A count of all of the subnets that exist as VLAN interfaces. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#tagReferenceCount" name=tagReferenceCount>tagReferenceCount</a></span>
            <div class='views-field-body'>A count of references to all tags for this VLAN. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#virtualGuestCount" name=virtualGuestCount>virtualGuestCount</a></span>
            <div class='views-field-body'>A count of all of the Virtual Servers that are connected to a VLAN. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


