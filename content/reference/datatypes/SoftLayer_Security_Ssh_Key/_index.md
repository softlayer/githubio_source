---
title: "SoftLayer_Security_Ssh_Key"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Ssh_Key"
---

# SoftLayer_Security_Ssh_Key
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Security_Ssh_Key' >Datatype</a></li>
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
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The date a ssh key was added. 

This property is read only. Changes made will be silently ignored.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#fingerprint" name=fingerprint>fingerprint</a></span>
            <div class='views-field-body'>A short sequence of bytes used to authenticate or lookup a longer ssh key. This will automatically be generated upon adding or modifying the ssh key. 

This property is read only. Changes made will be silently ignored.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The ID of the ssh key record.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#key" name=key>key</a></span>
            <div class='views-field-body'>The ssh key.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#label" name=label>label</a></span>
            <div class='views-field-body'>A descriptive name used to identify a ssh key.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>The date a ssh key was last modified. 

This property is read only. Changes made will be silently ignored.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#notes" name=notes>notes</a></span>
            <div class='views-field-body'>A small note about a ssh key to use at your discretion.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#blockDeviceTemplateGroups" name=blockDeviceTemplateGroups>blockDeviceTemplateGroups</a></span>
            <div class='views-field-body'>The image template groups that are linked to an SSH key. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group'>SoftLayer_Virtual_Guest_Block_Device_Template_Group[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#softwarePasswords" name=softwarePasswords>softwarePasswords</a></span>
            <div class='views-field-body'>The OS root users that are linked to an SSH key. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Software_Component_Password'>SoftLayer_Software_Component_Password[] </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#blockDeviceTemplateGroupCount" name=blockDeviceTemplateGroupCount>blockDeviceTemplateGroupCount</a></span>
            <div class='views-field-body'>A count of the image template groups that are linked to an SSH key. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#softwarePasswordCount" name=softwarePasswordCount>softwarePasswordCount</a></span>
            <div class='views-field-body'>A count of the OS root users that are linked to an SSH key. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


