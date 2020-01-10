---
title: "SoftLayer_Security_Certificate_Entry"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Certificate_Entry"
---

# SoftLayer_Security_Certificate_Entry
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Security_Certificate_Entry' >Datatype</a></li>
    </ul>
</div>

## Description 






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
[certificateId]: #certificateid
#### [certificateId]
The ID of the certificate record.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[commonName]: #commonname
#### [commonName]
The common name (usually a domain name) encoded within the certificate.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[keySize]: #keysize
#### [keySize]
The size (number of bits) of the public key represented by the certificate.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[organizationName]: #organizationname
#### [organizationName]
The organizational name encoded in the certificate.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[validityBegin]: #validitybegin
#### [validityBegin]
The UTC timestamp representing the beginning of the certificate's validity   
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[validityDays]: #validitydays
#### [validityDays]
The number of days remaining in the validity period for the certificate.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[validityEnd]: #validityend
#### [validityEnd]
The UTC timestamp representing the end of the certificate's validity period.   
<span class="type-label">Type: </span>**dateTime**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


