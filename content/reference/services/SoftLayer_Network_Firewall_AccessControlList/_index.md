---
title: "SoftLayer_Network_Firewall_AccessControlList"
description: "The SoftLayer_Network_Firewall_AccessControlList service accesses general information relating to a single SoftLayer fir... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_AccessControlList"
---
# SoftLayer_Network_Firewall_AccessControlList
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Firewall_AccessControlList' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Firewall_AccessControlList' >Datatype</a></li>
    </ul>
</div>

## Description
The SoftLayer_Network_Firewall_AccessControlList service accesses general information relating to a single SoftLayer firewall access control list.  This is the object which ties the running rules to a specific context. The current running rule set can be pulled from this service. Use the [[SoftLayer Network Firewall Template]] service to pull SoftLayer recommended rule set templates. Use the [[SoftLayer Network Firewall Update Request]] service to submit a firewall update request. 

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

#### [getNetworkFirewallUpdateRequests](/reference/services/SoftLayer_Network_Firewall_AccessControlList/getNetworkFirewallUpdateRequests)
Retrieve the update requests made for this firewall.
</div>

<div class="method-row">

#### [getNetworkVlan](/reference/services/SoftLayer_Network_Firewall_AccessControlList/getNetworkVlan)

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_Firewall_AccessControlList/getObject)
Retrieve a SoftLayer_Network_Firewall_AccessControlList record.
</div>

<div class="method-row">

#### [getRules](/reference/services/SoftLayer_Network_Firewall_AccessControlList/getRules)
Retrieve the currently running rule set of this context access control list firewall.
</div>
</div>

</div>

