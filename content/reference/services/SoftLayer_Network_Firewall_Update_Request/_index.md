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
### external links
        Array
(
    [url] => http://en.wikipedia.org/wiki/Firewall_(networking)
    [description] => Firewall at Wikipedia
)
1        
### seeAlso
        SoftLayer_Network_Component_Firewall1        SoftLayer_Network_Firewall_Template1        SoftLayer_Network_Component_Firewall1        SoftLayer_Network_Firewall_Template1                
        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Firewall_Update_Request/createObject'> createObject</a> </span>
            <div class='views-field-body'>Create a new firewall update request.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Firewall_Update_Request/getAuthorizingUser'> getAuthorizingUser</a> </span>
            <div class='views-field-body'>Retrieve the user that authorized this firewall update request.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Firewall_Update_Request/getFirewallUpdateRequestRuleAttributes'> getFirewallUpdateRequestRuleAttributes</a> </span>
            <div class='views-field-body'>Get the possible attribute values for a firewall update request rule.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Firewall_Update_Request/getGuest'> getGuest</a> </span>
            <div class='views-field-body'>Retrieve the downstream virtual server that the rule set will be applied to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Firewall_Update_Request/getHardware'> getHardware</a> </span>
            <div class='views-field-body'>Retrieve the downstream server that the rule set will be applied to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Firewall_Update_Request/getNetworkComponentFirewall'> getNetworkComponentFirewall</a> </span>
            <div class='views-field-body'>Retrieve the network component firewall that the rule set will be applied to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Firewall_Update_Request/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_Firewall_Update_Request record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Firewall_Update_Request/getRules'> getRules</a> </span>
            <div class='views-field-body'>Retrieve the group of rules contained within the update request.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Firewall_Update_Request/updateRuleNote'> updateRuleNote</a> </span>
            <div class='views-field-body'></div>
        </div>
        </div>
</div>

