---
title: "SoftLayer_Container_Network_Storage_Evault_WebCc_JobDetails"
description: "The SoftLayer_Container_Network_Storage_Evault_WebCc_JobDetails will contain basic details for all backup and restore jo... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_Storage_Evault_WebCc_JobDetails"
---

# SoftLayer_Container_Network_Storage_Evault_WebCc_JobDetails
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_Storage_Evault_WebCc_JobDetails' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_Network_Storage_Evault_WebCc_JobDetails will contain basic details for all backup and restore jobs performed by the StorageLayer EVault service offering. 


### associatedMethods

*  [SoftLayer_Network_Storage_Backup_Evault::getAgentStatuses](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getAgentStatuses )
*  [SoftLayer_Network_Storage_Backup_Evault::getTasks](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getTasks )





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
            <span class='views-field-title'><a href="#bytesUsed" name=bytesUsed>bytesUsed</a></span>
            <div class='views-field-body'>The number of bytes currently used by the backup job. (provided only for backup jobs) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsigned long</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#description" name=description>description</a></span>
            <div class='views-field-body'>Description of the backup/restore job </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareId" name=hardwareId>hardwareId</a></span>
            <div class='views-field-body'>hardware id </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#lastRunDate" name=lastRunDate>lastRunDate</a></span>
            <div class='views-field-body'>Date of the last jobrun. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>Name of the backup/restore job </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#originalSize" name=originalSize>originalSize</a></span>
            <div class='views-field-body'>Size of backup job when it was first run. (provided only for backup jobs) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsigned long</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#percentageOfTotalUsage" name=percentageOfTotalUsage>percentageOfTotalUsage</a></span>
            <div class='views-field-body'>Percentage of overall used space allocated by the job. (provided only for backup jobs) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#result" name=result>result</a></span>
            <div class='views-field-body'>Result of the latest jobrun. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#virtualGuestId" name=virtualGuestId>virtualGuestId</a></span>
            <div class='views-field-body'>virtual guest id </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
    </div>


