---
title: "SoftLayer_User_Customer_External_Binding_Verisign"
description: "The SoftLayer_User_Customer_External_Binding_Verisign data type contains information about a single VeriSign external bi... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_External_Binding_Verisign"
---

# SoftLayer_User_Customer_External_Binding_Verisign
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_User_Customer_External_Binding_Verisign' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_External_Binding_Verisign' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_User_Customer_External_Binding_Verisign data type contains information about a single VeriSign external binding.  The external binding information is used when a SoftLayer customer logs into the SoftLayer customer portal to authenticate them against a 3rd party, in this case VeriSign. 

The information provided by the VeriSign external binding data type includes: 
* The type of credential
* The current state of the credential
** Enabled
** Disabled
** Locked
* The credential's expiration date
* The last time the credential was updated


SoftLayer users with an active external binding will be prohibited from using the API for security reasons. 
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
            <span class='views-field-title'><a href="#active" name=active>active</a></span>
            <div class='views-field-body'>The flag that determines whether the external binding is active will be used for authentication or not.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The date that the external authentication binding was created. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#externalId" name=externalId>externalId</a></span>
            <div class='views-field-body'>The identifier used to identify this binding to an external authentication source.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>An external authentication binding's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#password" name=password>password</a></span>
            <div class='views-field-body'>The password used to authenticate the external id at an external authentication source.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#typeId" name=typeId>typeId</a></span>
            <div class='views-field-body'>The [[SoftLayer_User_External_Binding_Type|type]] identifier of an external authentication binding.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#userId" name=userId>userId</a></span>
            <div class='views-field-body'>An external authentication binding's associated [[SoftLayer_User_Customer|user account]] id.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#vendorId" name=vendorId>vendorId</a></span>
            <div class='views-field-body'>The [[SoftLayer_User_External_Binding_Vendor|vendor]] identifier of an external authentication binding.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#attributes" name=attributes>attributes</a></span>
            <div class='views-field-body'>Attributes of an external authentication binding. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_User_External_Binding_Attribute'>SoftLayer_User_External_Binding_Attribute[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingItem" name=billingItem>billingItem</a></span>
            <div class='views-field-body'>The current billing item for an external binding. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#credentialExpirationDate" name=credentialExpirationDate>credentialExpirationDate</a></span>
            <div class='views-field-body'>The date that a VeriSign credential expires. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#credentialLastUpdateDate" name=credentialLastUpdateDate>credentialLastUpdateDate</a></span>
            <div class='views-field-body'>The last time a VeriSign credential was updated. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#credentialState" name=credentialState>credentialState</a></span>
            <div class='views-field-body'>The current state of a VeriSign credential. This can be 'Enabled', 'Disabled', or 'Locked'. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#credentialType" name=credentialType>credentialType</a></span>
            <div class='views-field-body'>The type of VeriSign credential. This can be either 'Hardware' or 'Software'. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#note" name=note>note</a></span>
            <div class='views-field-body'>An optional note for identifying the external binding. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#type" name=type>type</a></span>
            <div class='views-field-body'>The type of external authentication binding. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_User_External_Binding_Type'>SoftLayer_User_External_Binding_Type </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#user" name=user>user</a></span>
            <div class='views-field-body'>The SoftLayer user that the external authentication binding belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#vendor" name=vendor>vendor</a></span>
            <div class='views-field-body'>The vendor of an external authentication binding. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_User_External_Binding_Vendor'>SoftLayer_User_External_Binding_Vendor </a></p></div>
        </div>
            </div>
</div>


