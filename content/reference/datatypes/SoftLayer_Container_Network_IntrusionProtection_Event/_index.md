---
title: "SoftLayer_Container_Network_IntrusionProtection_Event"
description: "The IntrusionProtection_Event object stores information about individual intrusion protection events. 

It is a data con... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_IntrusionProtection_Event"
---

# SoftLayer_Container_Network_IntrusionProtection_Event
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_IntrusionProtection_Event' >Datatype</a></li>
    </ul>
</div>

## Description 
The IntrusionProtection_Event object stores information about individual intrusion protection events. 

It is a data container that cannot be edited, deleted, or saved. 

It is returned by many methods in the TippingPointReporting object, but never directly, always as a child of another container object. 





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
            <span class='views-field-title'><a href="#CVEId" name=CVEId>CVEId</a></span>
            <div class='views-field-body'>The CVE ID(s), if any, associated with this attack signature. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#actionTaken" name=actionTaken>actionTaken</a></span>
            <div class='views-field-body'>The action that was taken when this attack was discovered.  Can be either "Block" or "Permit" </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#attackCount" name=attackCount>attackCount</a></span>
            <div class='views-field-body'>The number of attacks in this block.  Attacks are grouped differently based on the query performed on the tippingPointReporting object. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#attackLongDescription" name=attackLongDescription>attackLongDescription</a></span>
            <div class='views-field-body'>Long description of the attack.  May contain links to more information </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#attackName" name=attackName>attackName</a></span>
            <div class='views-field-body'>Name of the attack </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#beginTime" name=beginTime>beginTime</a></span>
            <div class='views-field-body'>The starting timestamp of the attack recorded, in Y-m-d H:i:s format.  May not be set, depending on the type of query performed. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#bugtraqId" name=bugtraqId>bugtraqId</a></span>
            <div class='views-field-body'>The BugTraq ID(s), if any, associated with this attack signature. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#classification" name=classification>classification</a></span>
            <div class='views-field-body'>The human-readable classification of the attack </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#destinationIpAddress" name=destinationIpAddress>destinationIpAddress</a></span>
            <div class='views-field-body'>The IP Address (as a dotted decimal string) of the machine that was the target of the attack </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#destinationPort" name=destinationPort>destinationPort</a></span>
            <div class='views-field-body'>The port the attack was directed at </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#endTime" name=endTime>endTime</a></span>
            <div class='views-field-body'>The ending timestamp of the attack recorded, in Y-m-d H:i:s format.  May not be set, depending on the type of query performed. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#platform" name=platform>platform</a></span>
            <div class='views-field-body'>The platform affected by the attack </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#protocol" name=protocol>protocol</a></span>
            <div class='views-field-body'>The protocol used in the attack </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#severity" name=severity>severity</a></span>
            <div class='views-field-body'>The human-readable severity of this attack, from "Low" to "Critical" </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#signatureId" name=signatureId>signatureId</a></span>
            <div class='views-field-body'>Unique ID of the "Signature" in question.  The signature determines the type of attack recorded.  SignatureId is used in the drillDown() function on the TippingPointReporting service </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#sourceIpAddress" name=sourceIpAddress>sourceIpAddress</a></span>
            <div class='views-field-body'>The IP Address (as a dotted decimal string) of the machine originating the attack </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#sourcePort" name=sourcePort>sourcePort</a></span>
            <div class='views-field-body'>The port the attack originated from </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
    </div>


