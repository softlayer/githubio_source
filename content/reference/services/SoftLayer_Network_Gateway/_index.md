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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Gateway/bypassAllVlans'> bypassAllVlans</a> </span>
            <div class='views-field-body'>Bypass All VLANs</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Gateway/bypassVlans'> bypassVlans</a> </span>
            <div class='views-field-body'>Bypass VLANs</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Gateway/createObject'> createObject</a> </span>
            <div class='views-field-body'>Create a new server gateway</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Gateway/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit Gateway</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Gateway/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the account for this gateway.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Gateway/getCapacity'> getCapacity</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Gateway/getInsideVlans'> getInsideVlans</a> </span>
            <div class='views-field-body'>Retrieve all VLANs trunked to this gateway.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Gateway/getManufacturer'> getManufacturer</a> </span>
            <div class='views-field-body'>manufacturer name</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Gateway/getMembers'> getMembers</a> </span>
            <div class='views-field-body'>Retrieve the members for this gateway.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Gateway/getNetworkFirewall'> getNetworkFirewall</a> </span>
            <div class='views-field-body'>Retrieve the firewall associated with this gateway, if any.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Gateway/getNetworkFirewallFlag'> getNetworkFirewallFlag</a> </span>
            <div class='views-field-body'>Retrieve whether or not there is a firewall associated with this gateway.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Gateway/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_Gateway record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Gateway/getPossibleInsideVlans'> getPossibleInsideVlans</a> </span>
            <div class='views-field-body'>Get Possible Inside VLANs</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Gateway/getPrivateIpAddress'> getPrivateIpAddress</a> </span>
            <div class='views-field-body'>Retrieve the private gateway IP address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Gateway/getPrivateVlan'> getPrivateVlan</a> </span>
            <div class='views-field-body'>Retrieve the private VLAN for accessing this gateway.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Gateway/getPublicIpAddress'> getPublicIpAddress</a> </span>
            <div class='views-field-body'>Retrieve the public gateway IP address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Gateway/getPublicIpv6Address'> getPublicIpv6Address</a> </span>
            <div class='views-field-body'>Retrieve the public gateway IPv6 address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Gateway/getPublicVlan'> getPublicVlan</a> </span>
            <div class='views-field-body'>Retrieve the public VLAN for accessing this gateway.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Gateway/getStatus'> getStatus</a> </span>
            <div class='views-field-body'>Retrieve the current status of the gateway.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Gateway/unbypassAllVlans'> unbypassAllVlans</a> </span>
            <div class='views-field-body'>Bypass All VLANs</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Gateway/unbypassVlans'> unbypassVlans</a> </span>
            <div class='views-field-body'>Bypass VLANs</div>
        </div>
        </div>
</div>

