---
title: "SoftLayer_Network_Gateway"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway"
---

# SoftLayer_Network_Gateway
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Gateway' >Datatype</a></li>
    </ul>
</div>

## Description 






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
            <div class='views-field-body'>The internal identifier of the account assigned to this gateway.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#groupNumber" name=groupNumber>groupNumber</a></span>
            <div class='views-field-body'>The VRRP group number for this gateway. This is set internally and cannot be provided on create.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A gateway's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>A gateway's name. This is required on create and can be no more than 255 characters.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkSpace" name=networkSpace>networkSpace</a></span>
            <div class='views-field-body'>A gateway's network space. Currently, only 'private'  or 'both' is allowed. When this value is 'private', it is a backend gateway only. Otherwise, it is a gateway for both frontend and backend traffic.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#privateIpAddressId" name=privateIpAddressId>privateIpAddressId</a></span>
            <div class='views-field-body'>The internal identifier of the private IP address for this gateway.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#privateVlanId" name=privateVlanId>privateVlanId</a></span>
            <div class='views-field-body'>The internal identifier of the private VLAN for this gateway.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#publicIpAddressId" name=publicIpAddressId>publicIpAddressId</a></span>
            <div class='views-field-body'>The internal identifier of the public IP address for this gateway.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#publicIpv6AddressId" name=publicIpv6AddressId>publicIpv6AddressId</a></span>
            <div class='views-field-body'>The internal identifier of the public IPv6 address for this gateway.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#publicVlanId" name=publicVlanId>publicVlanId</a></span>
            <div class='views-field-body'>The internal identifier of the public VLAN for this gateway. This is set internally and cannot be provided on create.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#statusId" name=statusId>statusId</a></span>
            <div class='views-field-body'>The current status of this gateway. This is always active unless there is a process running to change the gateway. This can not be set on creation.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'>The account for this gateway. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#insideVlans" name=insideVlans>insideVlans</a></span>
            <div class='views-field-body'>All VLANs trunked to this gateway. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Gateway_Vlan'>SoftLayer_Network_Gateway_Vlan[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#members" name=members>members</a></span>
            <div class='views-field-body'>The members for this gateway. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Gateway_Member'>SoftLayer_Network_Gateway_Member[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkFirewall" name=networkFirewall>networkFirewall</a></span>
            <div class='views-field-body'>The firewall associated with this gateway, if any. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Vlan_Firewall'>SoftLayer_Network_Vlan_Firewall </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkFirewallFlag" name=networkFirewallFlag>networkFirewallFlag</a></span>
            <div class='views-field-body'>Whether or not there is a firewall associated with this gateway. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#privateIpAddress" name=privateIpAddress>privateIpAddress</a></span>
            <div class='views-field-body'>The private gateway IP address. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#privateVlan" name=privateVlan>privateVlan</a></span>
            <div class='views-field-body'>The private VLAN for accessing this gateway. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#publicIpAddress" name=publicIpAddress>publicIpAddress</a></span>
            <div class='views-field-body'>The public gateway IP address. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#publicIpv6Address" name=publicIpv6Address>publicIpv6Address</a></span>
            <div class='views-field-body'>The public gateway IPv6 address. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#publicVlan" name=publicVlan>publicVlan</a></span>
            <div class='views-field-body'>The public VLAN for accessing this gateway. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#status" name=status>status</a></span>
            <div class='views-field-body'>The current status of the gateway. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Gateway_Status'>SoftLayer_Network_Gateway_Status </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#insideVlanCount" name=insideVlanCount>insideVlanCount</a></span>
            <div class='views-field-body'>A count of all VLANs trunked to this gateway. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#memberCount" name=memberCount>memberCount</a></span>
            <div class='views-field-body'>A count of the members for this gateway. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


