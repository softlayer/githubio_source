---
title: "SoftLayer_Network_Vlan_Firewall"
description: "The SoftLayer_Network_Vlan_Firewall data type contains general information relating to a single SoftLayer VLAN firewall.... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan_Firewall"
---

# SoftLayer_Network_Vlan_Firewall
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Vlan_Firewall' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Vlan_Firewall data type contains general information relating to a single SoftLayer VLAN firewall. This is the object which ties the running rules to a specific downstream server. Use the [[SoftLayer Network Firewall Template]] service to pull SoftLayer recommended rule set templates. Use the [[SoftLayer Network Firewall Update Request]] service to submit a firewall update request. 

### External Links


* [Firewall at Wikipedia](http://en.wikipedia.org/wiki/Firewall_(networking))




### seeAlso

* [SoftLayer_Network_Firewall_Template](/reference/datatypes/SoftLayer_Network_Firewall_Template )


* [SoftLayer_Network_Firewall_Update_Request](/reference/datatypes/SoftLayer_Network_Firewall_Update_Request )




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
            <span class='views-field-title'><a href="#administrativeBypassFlag" name=administrativeBypassFlag>administrativeBypassFlag</a></span>
            <div class='views-field-body'>A flag to indicate if the firewall is in administrative bypass mode. In other words, no rules are being applied to the traffic coming through. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#customerManagedFlag" name=customerManagedFlag>customerManagedFlag</a></span>
            <div class='views-field-body'>Whether or not this firewall can be directly logged in to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A firewall's unique identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#primaryIpAddress" name=primaryIpAddress>primaryIpAddress</a></span>
            <div class='views-field-body'>A firewall's primary IP address. This field will be the IP shown when doing network traces and reverse DNS and is a read-only property. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#accountId" name=accountId>accountId</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#bandwidthAllocation" name=bandwidthAllocation>bandwidthAllocation</a></span>
            <div class='views-field-body'>A firewall's allotted bandwidth (measured in GB). </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingCycleBandwidthUsage" name=billingCycleBandwidthUsage>billingCycleBandwidthUsage</a></span>
            <div class='views-field-body'>The raw bandwidth usage data for the current billing cycle. One object will be returned for each network this firewall is attached to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingCyclePrivateBandwidthUsage" name=billingCyclePrivateBandwidthUsage>billingCyclePrivateBandwidthUsage</a></span>
            <div class='views-field-body'>The raw private bandwidth usage data for the current billing cycle. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingCyclePublicBandwidthUsage" name=billingCyclePublicBandwidthUsage>billingCyclePublicBandwidthUsage</a></span>
            <div class='views-field-body'>The raw public bandwidth usage data for the current billing cycle. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingItem" name=billingItem>billingItem</a></span>
            <div class='views-field-body'>The billing item for a Hardware Firewall (Dedicated). </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#bypassRequestStatus" name=bypassRequestStatus>bypassRequestStatus</a></span>
            <div class='views-field-body'>Administrative bypass request status. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#datacenter" name=datacenter>datacenter</a></span>
            <div class='views-field-body'>The datacenter that the firewall resides in. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#firewallType" name=firewallType>firewallType</a></span>
            <div class='views-field-body'>The firewall device type. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#fullyQualifiedDomainName" name=fullyQualifiedDomainName>fullyQualifiedDomainName</a></span>
            <div class='views-field-body'>A name reflecting the hostname and domain of the firewall. This is created from the combined values of the firewall's logical name and vlan number automatically, and thus can not be edited directly. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#managementCredentials" name=managementCredentials>managementCredentials</a></span>
            <div class='views-field-body'>The credentials to log in to a firewall device. This is only present for dedicated appliances. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Software_Component_Password'>SoftLayer_Software_Component_Password </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#metricTrackingObject" name=metricTrackingObject>metricTrackingObject</a></span>
            <div class='views-field-body'>A firewall's metric tracking object. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object'>SoftLayer_Metric_Tracking_Object </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#metricTrackingObjectId" name=metricTrackingObjectId>metricTrackingObjectId</a></span>
            <div class='views-field-body'>The metric tracking object ID for this firewall. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkFirewallUpdateRequests" name=networkFirewallUpdateRequests>networkFirewallUpdateRequests</a></span>
            <div class='views-field-body'>The update requests made for this firewall. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Firewall_Update_Request'>SoftLayer_Network_Firewall_Update_Request[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkGateway" name=networkGateway>networkGateway</a></span>
            <div class='views-field-body'>The gateway associated with this firewall, if any. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkVlan" name=networkVlan>networkVlan</a></span>
            <div class='views-field-body'>The VLAN object that a firewall is associated with and protecting. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkVlans" name=networkVlans>networkVlans</a></span>
            <div class='views-field-body'>The VLAN objects that a firewall is associated with and protecting. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#rules" name=rules>rules</a></span>
            <div class='views-field-body'>The currently running rule set of this network component firewall. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Vlan_Firewall_Rule'>SoftLayer_Network_Vlan_Firewall_Rule[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#tagReferences" name=tagReferences>tagReferences</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Tag_Reference'>SoftLayer_Tag_Reference[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#upgradeRequest" name=upgradeRequest>upgradeRequest</a></span>
            <div class='views-field-body'>A firewall's associated upgrade request object, if any. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Upgrade_Request'>SoftLayer_Product_Upgrade_Request </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingCycleBandwidthUsageCount" name=billingCycleBandwidthUsageCount>billingCycleBandwidthUsageCount</a></span>
            <div class='views-field-body'>A count of the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this firewall is attached to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkFirewallUpdateRequestCount" name=networkFirewallUpdateRequestCount>networkFirewallUpdateRequestCount</a></span>
            <div class='views-field-body'>A count of the update requests made for this firewall. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkVlanCount" name=networkVlanCount>networkVlanCount</a></span>
            <div class='views-field-body'>A count of the VLAN objects that a firewall is associated with and protecting. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ruleCount" name=ruleCount>ruleCount</a></span>
            <div class='views-field-body'>A count of the currently running rule set of this network component firewall. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#tagReferenceCount" name=tagReferenceCount>tagReferenceCount</a></span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


