---
title: "SoftLayer_Network_Firewall_Update_Request"
description: "The SoftLayer_Network_Firewall_Update_Request service can be used to create SoftLayer network component firewall rules u... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_Update_Request"
---
# SoftLayer_Network_Firewall_Update_Request
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Firewall_Update_Request' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Firewall_Update_Request' >Datatype</a></li>
    </ul>
</div>

## Description
The SoftLayer_Network_Firewall_Update_Request service can be used to create SoftLayer network component firewall rules update requests.  Update requests are added to a transaction queue and are typically posted in about 60 seconds.  After they are posted, they are listed as current rules via the [[SoftLayer Network Component Firewall]] service. Use the [[SoftLayer Network Component Firewall]] service to view current rules. Use the [[SoftLayer Network Firewall Template]] service to pull SoftLayer recommended rule set templates. 

### External Links


* [Firewall at Wikipedia](http://en.wikipedia.org/wiki/Firewall_(networking))




### seeAlso

* [SoftLayer_Network_Component_Firewall](/reference/services/SoftLayer_Network_Component_Firewall )


* [SoftLayer_Network_Firewall_Template](/reference/services/SoftLayer_Network_Firewall_Template )


* [SoftLayer_Network_Component_Firewall](/reference/services/SoftLayer_Network_Component_Firewall )


* [SoftLayer_Network_Firewall_Template](/reference/services/SoftLayer_Network_Firewall_Template )


        
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

#### [createObject](/reference/services/SoftLayer_Network_Firewall_Update_Request/createObject)
Create a new firewall update request.
</div>

<div class="method-row">

#### [getAuthorizingUser](/reference/services/SoftLayer_Network_Firewall_Update_Request/getAuthorizingUser)
Retrieve the user that authorized this firewall update request.
</div>

<div class="method-row">

#### [getFirewallUpdateRequestRuleAttributes](/reference/services/SoftLayer_Network_Firewall_Update_Request/getFirewallUpdateRequestRuleAttributes)
Get the possible attribute values for a firewall update request rule.
</div>

<div class="method-row">

#### [getGuest](/reference/services/SoftLayer_Network_Firewall_Update_Request/getGuest)
Retrieve the downstream virtual server that the rule set will be applied to.
</div>

<div class="method-row">

#### [getHardware](/reference/services/SoftLayer_Network_Firewall_Update_Request/getHardware)
Retrieve the downstream server that the rule set will be applied to.
</div>

<div class="method-row">

#### [getNetworkComponentFirewall](/reference/services/SoftLayer_Network_Firewall_Update_Request/getNetworkComponentFirewall)
Retrieve the network component firewall that the rule set will be applied to.
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_Firewall_Update_Request/getObject)
Retrieve a SoftLayer_Network_Firewall_Update_Request record.
</div>

<div class="method-row">

#### [getRules](/reference/services/SoftLayer_Network_Firewall_Update_Request/getRules)
Retrieve the group of rules contained within the update request.
</div>

<div class="method-row">

#### [updateRuleNote](/reference/services/SoftLayer_Network_Firewall_Update_Request/updateRuleNote)

</div>
</div>

</div>

