---
title: "SoftLayer_Network_Component_Firewall"
description: "The SoftLayer_Network_Component_Firewall service accesses general information relating to a single SoftLayer network com... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component_Firewall"
---
# SoftLayer_Network_Component_Firewall
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Component_Firewall' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Component_Firewall' >Datatype</a></li>
    </ul>
</div>

## Description
The SoftLayer_Network_Component_Firewall service accesses general information relating to a single SoftLayer network component firewall.  This is the object which ties the running rules to a specific downstream server. The current running rule set can be pulled from this service. Use the [[SoftLayer Network Firewall Template]] service to pull SoftLayer recommended rule set templates. Use the [[SoftLayer Network Firewall Update Request]] service to submit a firewall update request. 

### External Links


* [Firewall at Wikipedia](http://en.wikipedia.org/wiki/Firewall_(networking))




### seeAlso

* [SoftLayer_Network_Firewall_Template](/reference/services/SoftLayer_Network_Firewall_Template )


* [SoftLayer_Network_Firewall_Update_Request](/reference/services/SoftLayer_Network_Firewall_Update_Request )


        
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

#### [getApplyServerRuleSubnets](/reference/services/SoftLayer_Network_Component_Firewall/getApplyServerRuleSubnets)
Retrieve the additional subnets linked to this network component firewall, that inherit rules from the host that the context slot is attached to.
</div>

<div class="method-row">

#### [getBillingItem](/reference/services/SoftLayer_Network_Component_Firewall/getBillingItem)
Retrieve the billing item for a Hardware Firewall (Dedicated).
</div>

<div class="method-row">

#### [getGuestNetworkComponent](/reference/services/SoftLayer_Network_Component_Firewall/getGuestNetworkComponent)
Retrieve the network component of the guest virtual server that this network component firewall belongs to.
</div>

<div class="method-row">

#### [getNetworkComponent](/reference/services/SoftLayer_Network_Component_Firewall/getNetworkComponent)
Retrieve the network component of the switch interface that this network component firewall belongs to.
</div>

<div class="method-row">

#### [getNetworkFirewallUpdateRequest](/reference/services/SoftLayer_Network_Component_Firewall/getNetworkFirewallUpdateRequest)
Retrieve the update requests made for this firewall.
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_Component_Firewall/getObject)
Retrieve a SoftLayer_Network_Component_Firewall record.
</div>

<div class="method-row">

#### [getRules](/reference/services/SoftLayer_Network_Component_Firewall/getRules)
Retrieve the currently running rule set of this network component firewall.
</div>

<div class="method-row">

#### [getSubnets](/reference/services/SoftLayer_Network_Component_Firewall/getSubnets)
Retrieve the additional subnets linked to this network component firewall.
</div>

<div class="method-row">

#### [hasActiveTransactions](/reference/services/SoftLayer_Network_Component_Firewall/hasActiveTransactions)

</div>
</div>

</div>

