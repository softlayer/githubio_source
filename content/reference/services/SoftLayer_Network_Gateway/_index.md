---
title: "SoftLayer_Network_Gateway"
description: "A network gateway is a set of members which have a configurable set of VLANs trunked through them. This is helpful for c... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway"
---
# SoftLayer_Network_Gateway
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Gateway' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Gateway' >Datatype</a></li>
    </ul>
</div>

## Description
A network gateway is a set of members which have a configurable set of VLANs trunked through them. This is helpful for creating proxies. Each network gateway can have a configurable set of hardware and VLANs within the same pod routed to it. Gateways can be bypassed or unbypassed either as a whole or for specific VLANs. They are also provided gateway VLANs for management that are never bypassed. Members cannot be simply removed once attached to a gateway, they must be reclaimed. 



        
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

#### [bypassAllVlans](/reference/services/SoftLayer_Network_Gateway/bypassAllVlans)
Bypass All VLANs
</div>

<div class="method-row">

#### [bypassVlans](/reference/services/SoftLayer_Network_Gateway/bypassVlans)
Bypass VLANs
</div>

<div class="method-row">

#### [changeGatewayVersion](/reference/services/SoftLayer_Network_Gateway/changeGatewayVersion)
Change Juniper vSRX version on a Gateway
</div>

<div class="method-row">

#### [checkAccountWhiteList](/reference/services/SoftLayer_Network_Gateway/checkAccountWhiteList)

</div>

<div class="method-row">

#### [createObject](/reference/services/SoftLayer_Network_Gateway/createObject)
Create a new server gateway
</div>

<div class="method-row">

#### [editObject](/reference/services/SoftLayer_Network_Gateway/editObject)
Edit Gateway
</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Network_Gateway/getAccount)
Retrieve the account for this gateway.
</div>

<div class="method-row">

#### [getAllowedOsPriceIds](/reference/services/SoftLayer_Network_Gateway/getAllowedOsPriceIds)

</div>

<div class="method-row">

#### [getCapacity](/reference/services/SoftLayer_Network_Gateway/getCapacity)

</div>

<div class="method-row">

#### [getInsideVlans](/reference/services/SoftLayer_Network_Gateway/getInsideVlans)
Retrieve all VLANs trunked to this gateway.
</div>

<div class="method-row">

#### [getManufacturer](/reference/services/SoftLayer_Network_Gateway/getManufacturer)
manufacturer name
</div>

<div class="method-row">

#### [getMemberGatewayImagesMatch](/reference/services/SoftLayer_Network_Gateway/getMemberGatewayImagesMatch)

</div>

<div class="method-row">

#### [getMembers](/reference/services/SoftLayer_Network_Gateway/getMembers)
Retrieve the members for this gateway.
</div>

<div class="method-row">

#### [getNetworkFirewall](/reference/services/SoftLayer_Network_Gateway/getNetworkFirewall)
Retrieve the firewall associated with this gateway, if any.
</div>

<div class="method-row">

#### [getNetworkFirewallFlag](/reference/services/SoftLayer_Network_Gateway/getNetworkFirewallFlag)
Retrieve whether or not there is a firewall associated with this gateway.
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_Gateway/getObject)
Retrieve a SoftLayer_Network_Gateway record.
</div>

<div class="method-row">

#### [getPossibleInsideVlans](/reference/services/SoftLayer_Network_Gateway/getPossibleInsideVlans)
Get Possible Inside VLANs
</div>

<div class="method-row">

#### [getPrivateIpAddress](/reference/services/SoftLayer_Network_Gateway/getPrivateIpAddress)
Retrieve the private gateway IP address.
</div>

<div class="method-row">

#### [getPrivateVlan](/reference/services/SoftLayer_Network_Gateway/getPrivateVlan)
Retrieve the private VLAN for accessing this gateway.
</div>

<div class="method-row">

#### [getPublicIpAddress](/reference/services/SoftLayer_Network_Gateway/getPublicIpAddress)
Retrieve the public gateway IP address.
</div>

<div class="method-row">

#### [getPublicIpv6Address](/reference/services/SoftLayer_Network_Gateway/getPublicIpv6Address)
Retrieve the public gateway IPv6 address.
</div>

<div class="method-row">

#### [getPublicVlan](/reference/services/SoftLayer_Network_Gateway/getPublicVlan)
Retrieve the public VLAN for accessing this gateway.
</div>

<div class="method-row">

#### [getRollbackSupport](/reference/services/SoftLayer_Network_Gateway/getRollbackSupport)

</div>

<div class="method-row">

#### [getStatus](/reference/services/SoftLayer_Network_Gateway/getStatus)
Retrieve the current status of the gateway.
</div>

<div class="method-row">

#### [getUpgradeItemPrices](/reference/services/SoftLayer_Network_Gateway/getUpgradeItemPrices)
Retrieve available upgrade prices
</div>

<div class="method-row">

#### [isAccountWhiteListed](/reference/services/SoftLayer_Network_Gateway/isAccountWhiteListed)

</div>

<div class="method-row">

#### [isLicenseServerAllowed](/reference/services/SoftLayer_Network_Gateway/isLicenseServerAllowed)

</div>

<div class="method-row">

#### [isRollbackAllowed](/reference/services/SoftLayer_Network_Gateway/isRollbackAllowed)

</div>

<div class="method-row">

#### [rebuildvSRXHACluster](/reference/services/SoftLayer_Network_Gateway/rebuildvSRXHACluster)
Rebuild Juniper vSRX HA Gateway
</div>

<div class="method-row">

#### [refreshGatewayLicense](/reference/services/SoftLayer_Network_Gateway/refreshGatewayLicense)

</div>

<div class="method-row">

#### [setGatewayPassword](/reference/services/SoftLayer_Network_Gateway/setGatewayPassword)

</div>

<div class="method-row">

#### [unbypassAllVlans](/reference/services/SoftLayer_Network_Gateway/unbypassAllVlans)
Bypass All VLANs
</div>

<div class="method-row">

#### [unbypassVlans](/reference/services/SoftLayer_Network_Gateway/unbypassVlans)
Bypass VLANs
</div>
</div>

</div>

