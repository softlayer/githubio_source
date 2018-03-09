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
                <a href="#certificateId" name=certificateId>certificateId</a>
            </span>
            <div class='views-field-body'>The ID of the certificate record.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#commonName" name=commonName>commonName</a>
            </span>
            <div class='views-field-body'>The common name (usually a domain name) encoded within the certificate.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#keySize" name=keySize>keySize</a>
            </span>
            <div class='views-field-body'>The size (number of bits) of the public key represented by the certificate.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#organizationName" name=organizationName>organizationName</a>
            </span>
            <div class='views-field-body'>The organizational name encoded in the certificate.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#validityBegin" name=validityBegin>validityBegin</a>
            </span>
            <div class='views-field-body'>The UTC timestamp representing the beginning of the certificate's validity  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#validityDays" name=validityDays>validityDays</a>
            </span>
            <div class='views-field-body'>The number of days remaining in the validity period for the certificate.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#validityEnd" name=validityEnd>validityEnd</a>
            </span>
            <div class='views-field-body'>The UTC timestamp representing the end of the certificate's validity period.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
            </div>
    </div>


