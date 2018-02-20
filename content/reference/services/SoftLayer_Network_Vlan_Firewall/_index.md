---
title: "SoftLayer_Network_Vlan_Firewall"
description: "The SoftLayer_Network_Vlan_Firewall service accesses general information relating to a single SoftLayer VLAN firewall.... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan_Firewall"
---
# SoftLayer_Network_Vlan_Firewall
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Vlan_Firewall' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Vlan_Firewall' >Datatype</a></li>
    </ul>
</div>

## Description
The SoftLayer_Network_Vlan_Firewall service accesses general information relating to a single SoftLayer VLAN firewall.  This is the object which ties the running rules to a specific downstream server. The current running rule set can be pulled from this service. Use the [[SoftLayer Network Firewall Template]] service to pull SoftLayer recommended rule set templates. Use the [[SoftLayer Network Firewall Update Request]] service to submit a firewall update request. 
### external links
        Array
(
    [url] => http://en.wikipedia.org/wiki/Firewall_(networking)
    [description] => Firewall at Wikipedia
)
1        
### seeAlso
        SoftLayer_Network_Firewall_Template1        SoftLayer_Network_Firewall_Update_Request1                
        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/approveBypassRequest'> approveBypassRequest</a> </span>
            <div class='views-field-body'>Approve a request from technical support to bypass the firewall.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/getAccountId'> getAccountId</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/getBandwidthAllocation'> getBandwidthAllocation</a> </span>
            <div class='views-field-body'>Retrieve a firewall's allotted bandwidth (measured in GB).</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/getBillingCycleBandwidthUsage'> getBillingCycleBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this firewall is attached to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/getBillingCyclePrivateBandwidthUsage'> getBillingCyclePrivateBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the raw private bandwidth usage data for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/getBillingCyclePublicBandwidthUsage'> getBillingCyclePublicBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the raw public bandwidth usage data for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/getBillingItem'> getBillingItem</a> </span>
            <div class='views-field-body'>Retrieve the billing item for a Hardware Firewall (Dedicated).</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/getBypassRequestStatus'> getBypassRequestStatus</a> </span>
            <div class='views-field-body'>Retrieve administrative bypass request status.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/getDatacenter'> getDatacenter</a> </span>
            <div class='views-field-body'>Retrieve the datacenter that the firewall resides in.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/getFirewallType'> getFirewallType</a> </span>
            <div class='views-field-body'>Retrieve the firewall device type.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/getFullyQualifiedDomainName'> getFullyQualifiedDomainName</a> </span>
            <div class='views-field-body'>Retrieve a name reflecting the hostname and domain of the firewall. This is created from the combined values of the firewall's logical name and vlan number automatically, and thus can not be edited directly.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/getManagementCredentials'> getManagementCredentials</a> </span>
            <div class='views-field-body'>Retrieve the credentials to log in to a firewall device. This is only present for dedicated appliances.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/getMetricTrackingObject'> getMetricTrackingObject</a> </span>
            <div class='views-field-body'>Retrieve a firewall's metric tracking object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/getMetricTrackingObjectId'> getMetricTrackingObjectId</a> </span>
            <div class='views-field-body'>Retrieve the metric tracking object ID for this firewall.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/getNetworkFirewallUpdateRequests'> getNetworkFirewallUpdateRequests</a> </span>
            <div class='views-field-body'>Retrieve the update requests made for this firewall.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/getNetworkGateway'> getNetworkGateway</a> </span>
            <div class='views-field-body'>Retrieve the gateway associated with this firewall, if any.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/getNetworkVlan'> getNetworkVlan</a> </span>
            <div class='views-field-body'>Retrieve the VLAN object that a firewall is associated with and protecting.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/getNetworkVlans'> getNetworkVlans</a> </span>
            <div class='views-field-body'>Retrieve the VLAN objects that a firewall is associated with and protecting.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_Vlan_Firewall record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/getRules'> getRules</a> </span>
            <div class='views-field-body'>Retrieve the currently running rule set of this network component firewall.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/getTagReferences'> getTagReferences</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/getUpgradeRequest'> getUpgradeRequest</a> </span>
            <div class='views-field-body'>Retrieve a firewall's associated upgrade request object, if any.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/isHighAvailabilityUpgradeAvailable'> isHighAvailabilityUpgradeAvailable</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/rejectBypassRequest'> rejectBypassRequest</a> </span>
            <div class='views-field-body'>Reject a request from technical support to bypass the firewall.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/restoreDefaults'> restoreDefaults</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/setTags'> setTags</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Vlan_Firewall/updateRouteBypass'> updateRouteBypass</a> </span>
            <div class='views-field-body'></div>
        </div>
        </div>
</div>

