---
title: "SoftLayer_Virtual_Guest_Block_Device_Template_Group_Accounts"
description: "The SoftLayer_Virtual_Guest_Block_Device_Template_Group_Accounts data type represents the SoftLayer customer accounts wh... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group_Accounts"
---

# SoftLayer_Virtual_Guest_Block_Device_Template_Group_Accounts
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group_Accounts' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Virtual_Guest_Block_Device_Template_Group_Accounts data type represents the SoftLayer customer accounts which have access to provision CloudLayer Computing Instances from an image template group. 

All accounts other than the image template group owner have read-only access to that image template group. 

It is important to note that this data type should only exist to give accounts access to the parent template group object, not the child.  All image template sharing between accounts should occur on the parent object. 


### associatedMethods

*  [SoftLayer_Virtual_Guest_Block_Device_Template_Group::getAccountReferences](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getAccountReferences )



### seeAlso

* [SoftLayer_Virtual_Guest_Block_Device_Template_Group](/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group )




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
            <span class='views-field-title'><a href="#accountId" name=accountId>accountId</a></span>
            <div class='views-field-body'>The [[SoftLayer_Account|account]] ID which will have access to an image.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The date access was granted to an account.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#groupId" name=groupId>groupId</a></span>
            <div class='views-field-body'>The [[SoftLayer_Virtual_Guest_Block_Device_Template_Group|group]] ID which access will be granted to.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'>The [[SoftLayer_Account|account]] that an image template group is shared with. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#group" name=group>group</a></span>
            <div class='views-field-body'>The [[SoftLayer_Virtual_Guest_Block_Device_Template_Group|image template group]] that is shared with an account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group'>SoftLayer_Virtual_Guest_Block_Device_Template_Group </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


