---
title: "SoftLayer_Notification_Occurrence_Resource_Network_Storage_NetApp_Volume_Replicant_Nas"
description: "This type contains general information related to a [[SoftLayer_Network_Storage_NetApp_Volume_Replicant_Nas]] resource t... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_Occurrence_Resource_Network_Storage_NetApp_Volume_Replicant_Nas"
---

# SoftLayer_Notification_Occurrence_Resource_Network_Storage_NetApp_Volume_Replicant_Nas
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Resource_Network_Storage_NetApp_Volume_Replicant_Nas' >Datatype</a></li>
    </ul>
</div>

## Description 
This type contains general information related to a [[SoftLayer_Network_Storage_NetApp_Volume_Replicant_Nas]] resource that is impacted by a [[SoftLayer_Notification_Occurrence_Event]]. 





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
            <span class='views-field-title'>
                <a href="#active" name=active>active</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#filterLabel" name=filterLabel>filterLabel</a>
            </span>
            <div class='views-field-body'><<< EOT A label which gives some background as to what piece of </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hostname" name=hostname>hostname</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#notificationOccurrenceEventId" name=notificationOccurrenceEventId>notificationOccurrenceEventId</a>
            </span>
            <div class='views-field-body'><<< EOT The unique identifier for the associated </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#privateIp" name=privateIp>privateIp</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#resourceAccountId" name=resourceAccountId>resourceAccountId</a>
            </span>
            <div class='views-field-body'><<< EOT The unique identifier for the [[SoftLayer_Account]] associated with </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#resourceName" name=resourceName>resourceName</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#resourceTableId" name=resourceTableId>resourceTableId</a>
            </span>
            <div class='views-field-body'><<< EOT The unique identifier for the physical resource that is associated </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#resourceType" name=resourceType>resourceType</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#notificationOccurrenceEvent" name=notificationOccurrenceEvent>notificationOccurrenceEvent</a>
            </span>
            <div class='views-field-body'>The associated event. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Event'>SoftLayer_Notification_Occurrence_Event </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#resource" name=resource>resource</a>
            </span>
            <div class='views-field-body'>The physical resource. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Entity'>SoftLayer_Entity </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


