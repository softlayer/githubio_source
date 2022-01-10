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





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[bootMode]: #bootmode
#### [bootMode]

Optional virtualization boot mode parameter, if set, can mark a template to boot specifically into PV or HVM.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[byol]: #byol
#### [byol]

Specifies if image is using a customer's software license.   
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[cloudInit]: #cloudinit
#### [cloudInit]

Specifies if image requires cloud-init.   
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[crkCrn]: #crkcrn
#### [crkCrn]

CRN to customer root key   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[environmentType]: #environmenttype
#### [environmentType]

For future use; not currently defined.   
<span class="type-label">Type: </span>**array of strings**  



</div>
<div class="prop-row">

-----
[ibmAccessKey]: #ibmaccesskey
#### [ibmAccessKey]

IBM Cloud HMAC Access Key   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[ibmApiKey]: #ibmapikey
#### [ibmApiKey]

IBM Cloud (Bluemix) API Key   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[ibmSecretKey]: #ibmsecretkey
#### [ibmSecretKey]

IBM HMAC Secret Key   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[isEncrypted]: #isencrypted
#### [isEncrypted]

Specifies if image is encrypted or not.   
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The group name to be applied to the imported template  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[note]: #note
#### [note]
The note to be applied to the imported template  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[operatingSystemReferenceCode]: #operatingsystemreferencecode
#### [operatingSystemReferenceCode]

The referenceCode of the operating system software description for the imported VHD   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[rootKeyId]: #rootkeyid
#### [rootKeyId]

Name of the IBM Key Protect Key Name. Required if using an encrypted image.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[supportedBootModes]: #supportedbootmodes
#### [supportedBootModes]

Optional Collection of modes that this template supports booting into.   
<span class="type-label">Type: </span>**array of strings**  



</div>
<div class="prop-row">

-----
[uri]: #uri
#### [uri]

The URI for an object storage object (.vhd/.iso file) 
<code>swift://<ObjectStorageAccountName>@<clusterName>/<containerName>/<fileName.(vhd|iso)></code>   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[wrappedDek]: #wrappeddek
#### [wrappedDek]

Wrapped Decryption Key provided by IBM Key Protect   
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


