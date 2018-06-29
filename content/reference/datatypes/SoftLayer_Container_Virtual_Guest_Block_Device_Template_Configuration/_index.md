---
title: "SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration"
description: "The SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration data type contains information relating to a t... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration"
---

# SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration data type contains information relating to a template's external location for importing and exporting 


### associatedMethods

*  [SoftLayer_Virtual_Guest_Block_Device_Template_Group::createFromExternalSource](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/createFromExternalSource )





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
                <a href="#bootMode" name=bootMode>bootMode</a>
            </span>
            <div class='views-field-body'>
Optional virtualization boot mode parameter, if set, can mark a template to boot specifically into PV or HVM.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#byol" name=byol>byol</a>
            </span>
            <div class='views-field-body'>
Specifies if image is using a customer's software license.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#cloudInit" name=cloudInit>cloudInit</a>
            </span>
            <div class='views-field-body'>
Specifies if image requires cloud-init.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#ibmApiKey" name=ibmApiKey>ibmApiKey</a>
            </span>
            <div class='views-field-body'>
IBM Cloud (Bluemix) API Key  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#isEncrypted" name=isEncrypted>isEncrypted</a>
            </span>
            <div class='views-field-body'>
Specifies if image is encrypted or not.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#keyProtectId" name=keyProtectId>keyProtectId</a>
            </span>
            <div class='views-field-body'>
ID of the IBM Key Protect Instance  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#name" name=name>name</a>
            </span>
            <div class='views-field-body'>The group name to be applied to the imported template </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#note" name=note>note</a>
            </span>
            <div class='views-field-body'>The note to be applied to the imported template </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#operatingSystemReferenceCode" name=operatingSystemReferenceCode>operatingSystemReferenceCode</a>
            </span>
            <div class='views-field-body'>
The referenceCode of the operating system software description for the imported VHD  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#rootKeyId" name=rootKeyId>rootKeyId</a>
            </span>
            <div class='views-field-body'>
Name of the IBM Key Protect Key Name. Required if using an encrypted image.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#supportedBootModes" name=supportedBootModes>supportedBootModes</a>
            </span>
            <div class='views-field-body'>
Optional Collection of modes that this template supports booting into.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>array of strings</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#uri" name=uri>uri</a>
            </span>
            <div class='views-field-body'>
The URI for an object storage object (.vhd/.iso file) 
<code>swift://<ObjectStorageAccountName>@<clusterName>/<containerName>/<fileName.(vhd|iso)></code>  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#wrappedDek" name=wrappedDek>wrappedDek</a>
            </span>
            <div class='views-field-body'>
Wrapped Decryption Key provided by IBM Key Protect  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
    </div>


