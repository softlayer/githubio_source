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
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [disable](/reference/services/SoftLayer_Virtual_Guest_Network_Component/disable)
Disable a network component to restrict network traffic
</div>

<div class="method-row">

#### [enable](/reference/services/SoftLayer_Virtual_Guest_Network_Component/enable)
Enable a network component to allow network traffic
</div>

<div class="method-row">

#### [getGuest](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getGuest)
Retrieve the computing instance that this network component exists on.
</div>

<div class="method-row">

#### [getHighAvailabilityFirewallFlag](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getHighAvailabilityFirewallFlag)

</div>

<div class="method-row">

#### [getIcpBinding](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getIcpBinding)

</div>

<div class="method-row">

#### [getIpAddressBindings](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getIpAddressBindings)
Retrieve the records of all IP addresses bound to a computing instance's network component.
</div>

<div class="method-row">

#### [getNetworkComponentFirewall](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getNetworkComponentFirewall)
Retrieve the upstream network component firewall.
</div>

<div class="method-row">

#### [getNetworkVlan](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getNetworkVlan)
Retrieve the VLAN that a computing instance network component's subnet is associated with.
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getObject)
Retrieve a SoftLayer_Virtual_Guest_Network_Component record.
</div>

<div class="method-row">

#### [getPrimaryIpAddress](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getPrimaryIpAddress)
Retrieve a computing instance network component's primary IP address.
</div>

<div class="method-row">

#### [getPrimaryIpAddressRecord](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getPrimaryIpAddressRecord)

</div>

<div class="method-row">

#### [getPrimarySubnet](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getPrimarySubnet)
Retrieve a network component's subnet for its primary IP address
</div>

<div class="method-row">

#### [getPrimaryVersion6IpAddressRecord](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getPrimaryVersion6IpAddressRecord)
Retrieve a network component's primary IPv6 IP address record.
</div>

<div class="method-row">

#### [getRouter](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getRouter)
Retrieve a network component's routers.
</div>

<div class="method-row">

#### [getSecurityGroupBindings](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getSecurityGroupBindings)
Retrieve the bindings associating security groups to this network component
</div>

<div class="method-row">

#### [getSubnets](/reference/services/SoftLayer_Virtual_Guest_Network_Component/getSubnets)
Retrieve a network component's subnets. A subnet is a group of IP addresses
</div>

<div class="method-row">

#### [isPingable](/reference/services/SoftLayer_Virtual_Guest_Network_Component/isPingable)
Verifies if network component is pingable.
</div>

<div class="method-row">

#### [securityGroupsReady](/reference/services/SoftLayer_Virtual_Guest_Network_Component/securityGroupsReady)

</div>
</div>

</div>

