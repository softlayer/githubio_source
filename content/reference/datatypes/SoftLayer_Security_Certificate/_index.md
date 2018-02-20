---
title: "SoftLayer_Security_Certificate"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Certificate"
---

# SoftLayer_Security_Certificate
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Security_Certificate' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Security_Certificate' >Datatype</a></li>
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
            <span class='views-field-title'><a href="#certificate" name=certificate>certificate</a></span>
            <div class='views-field-body'>The certificate provided publicly to clients requesting identity credentials. This certificate is usually signed by a source trusted by the client or a signature chain can be established between this certificate and the truested certificate. 

This property may only be modified when no services are associated. See associatedServiceCount.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#certificateSigningRequest" name=certificateSigningRequest>certificateSigningRequest</a></span>
            <div class='views-field-body'>The signing request used to request a certificate authority generate a signed certificate. 

This property may only be modified when no services are associated. See associatedServiceCount.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#commonName" name=commonName>commonName</a></span>
            <div class='views-field-body'>The common name (usually a domain name) encoded within the certificate. 

This property is read only. Changes made will be silently ignored.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The date the certificate _record_ was created. The contents of the certificate may of changed since the record was created, so this does not represent anything about the certificate itself. 

This property is read only. Changes made will be silently ignored.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The ID of the certificate record.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#intermediateCertificate" name=intermediateCertificate>intermediateCertificate</a></span>
            <div class='views-field-body'>The intermediate certificate authorities certificate that completes the certificate chain for the issued certificate. Required when clients will only trust the root certificate. 

This property may only be modified when no services are associated. See associatedServiceCount.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#keySize" name=keySize>keySize</a></span>
            <div class='views-field-body'>The size (number of bits) of the public key represented by the certificate.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>The date the certificate _record_ was last modified.The contents of the certificate may of changed since the record was created, so this does not represent anything about the certificate itself. 

This property is read only. Changes made will be silently ignored.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#notes" name=notes>notes</a></span>
            <div class='views-field-body'>A note to help describe the certificate.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#organizationName" name=organizationName>organizationName</a></span>
            <div class='views-field-body'>The organizational name encoded in the certificate. 

This property is read only. Changes made will be silently ignored.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#privateKey" name=privateKey>privateKey</a></span>
            <div class='views-field-body'>The private key in the key/certificate pair. 

This property may only be modified when no services are associated. See associatedServiceCount.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#validityBegin" name=validityBegin>validityBegin</a></span>
            <div class='views-field-body'>The UTC timestamp representing the beginning of the certificate's validity 

This property is read only. Changes made will be silently ignored.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#validityDays" name=validityDays>validityDays</a></span>
            <div class='views-field-body'>The number of days remaining in the validity period for the certificate. 

This property is read only. Changes made will be silently ignored.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#validityEnd" name=validityEnd>validityEnd</a></span>
            <div class='views-field-body'>The UTC timestamp representing the end of the certificate's validity period. 

This property is read only. Changes made will be silently ignored.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#associatedServiceCount" name=associatedServiceCount>associatedServiceCount</a></span>
            <div class='views-field-body'>The number of services currently associated with the certificate. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#loadBalancerVirtualIpAddresses" name=loadBalancerVirtualIpAddresses>loadBalancerVirtualIpAddresses</a></span>
            <div class='views-field-body'>The load balancers virtual IP addresses currently associated with the certificate. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress[] </a></p></div>
        </div>
            </div>
</div>


