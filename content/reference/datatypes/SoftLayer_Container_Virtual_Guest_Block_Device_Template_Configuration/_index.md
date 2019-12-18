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

## Local
-----
[bootMode]: #bootmode
#### [bootMode]

Optional virtualization boot mode parameter, if set, can mark a template to boot specifically into PV or HVM.   
<span class="type-label">Type: </span>**string**

-----
[byol]: #byol
#### [byol]

Specifies if image is using a customer's software license.   
<span class="type-label">Type: </span>**boolean**

-----
[cloudInit]: #cloudinit
#### [cloudInit]

Specifies if image requires cloud-init.   
<span class="type-label">Type: </span>**boolean**

-----
[crkCrn]: #crkcrn
#### [crkCrn]

CRN to customer root key   
<span class="type-label">Type: </span>**string**

-----
[environmentType]: #environmenttype
#### [environmentType]

For future use; not currently defined.   
<span class="type-label">Type: </span>**array of strings**

-----
[ibmAccessKey]: #ibmaccesskey
#### [ibmAccessKey]

IBM Cloud HMAC Access Key   
<span class="type-label">Type: </span>**string**

-----
[ibmApiKey]: #ibmapikey
#### [ibmApiKey]

IBM Cloud (Bluemix) API Key   
<span class="type-label">Type: </span>**string**

-----
[ibmSecretKey]: #ibmsecretkey
#### [ibmSecretKey]

IBM HMAC Secret Key   
<span class="type-label">Type: </span>**string**

-----
[isEncrypted]: #isencrypted
#### [isEncrypted]

Specifies if image is encrypted or not.   
<span class="type-label">Type: </span>**boolean**

-----
[name]: #name
#### [name]
The group name to be applied to the imported template  
<span class="type-label">Type: </span>**string**

-----
[note]: #note
#### [note]
The note to be applied to the imported template  
<span class="type-label">Type: </span>**string**

-----
[operatingSystemReferenceCode]: #operatingsystemreferencecode
#### [operatingSystemReferenceCode]

The referenceCode of the operating system software description for the imported VHD   
<span class="type-label">Type: </span>**string**

-----
[rootKeyId]: #rootkeyid
#### [rootKeyId]

Name of the IBM Key Protect Key Name. Required if using an encrypted image.   
<span class="type-label">Type: </span>**string**

-----
[supportedBootModes]: #supportedbootmodes
#### [supportedBootModes]

Optional Collection of modes that this template supports booting into.   
<span class="type-label">Type: </span>**array of strings**

-----
[uri]: #uri
#### [uri]

The URI for an object storage object (.vhd/.iso file) 
<code>swift://<ObjectStorageAccountName>@<clusterName>/<containerName>/<fileName.(vhd|iso)></code>   
<span class="type-label">Type: </span>**string**

-----
[wrappedDek]: #wrappeddek
#### [wrappedDek]

Wrapped Decryption Key provided by IBM Key Protect   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

</div>


