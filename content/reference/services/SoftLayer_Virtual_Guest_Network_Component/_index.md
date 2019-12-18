---
title: "SoftLayer_Virtual_Guest_Network_Component"
description: "The virtual guest network component service provides a common interface to a [SoftLayer_Virtual_Guest]({{<ref 'reference... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Network_Component"
---
# SoftLayer_Virtual_Guest_Network_Component
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Virtual_Guest_Network_Component' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component' >Datatype</a></li>
    </ul>
</div>

## Description
The virtual guest network component service provides a common interface to a [SoftLayer_Virtual_Guest]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest">}}) network component. Interaction with various third party APIs is not needed when implementing this service to administer your computing instances. 



        
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

#### [disable](/reference/services/SoftLayer_Virtual_Guest_Network_Component/disable)
Disable a network component to restrict network traffic

#### [enable](/reference/services/SoftLayer_Virtual_Guest_Network_Component/enable)
Enable a network component to allow network traffic

#### [getGuest](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getGuest)
Retrieve the computing instance that this network component exists on.

#### [getHighAvailabilityFirewallFlag](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getHighAvailabilityFirewallFlag)


#### [getIcpBinding](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getIcpBinding)


#### [getIpAddressBindings](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getIpAddressBindings)
Retrieve the records of all IP addresses bound to a computing instance's network component.

#### [getNetworkComponentFirewall](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getNetworkComponentFirewall)
Retrieve the upstream network component firewall.

#### [getNetworkVlan](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getNetworkVlan)
Retrieve the VLAN that a computing instance network component's subnet is associated with.

#### [getObject](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getObject)
Retrieve a SoftLayer_Virtual_Guest_Network_Component record.

#### [getPrimaryIpAddress](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getPrimaryIpAddress)
Retrieve a computing instance network component's primary IP address.

#### [getPrimaryIpAddressRecord](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getPrimaryIpAddressRecord)


#### [getPrimarySubnet](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getPrimarySubnet)
Retrieve a network component's subnet for its primary IP address

#### [getPrimaryVersion6IpAddressRecord](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getPrimaryVersion6IpAddressRecord)
Retrieve a network component's primary IPv6 IP address record.

#### [getRouter](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getRouter)
Retrieve a network component's routers.

#### [getSecurityGroupBindings](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getSecurityGroupBindings)
Retrieve the bindings associating security groups to this network component

#### [getSubnets](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getSubnets)
Retrieve a network component's subnets. A subnet is a group of IP addresses

#### [isPingable](/reference/services/SoftLayer_Virtual_Guest_Network_Component/isPingable)
Verifies if network component is pingable.

#### [securityGroupsReady](/reference/services/SoftLayer_Virtual_Guest_Network_Component/securityGroupsReady)


</div>

