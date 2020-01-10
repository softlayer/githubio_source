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
[certificate]: #certificate
#### [certificate]
The certificate provided publicly to clients requesting identity credentials. This certificate is usually signed by a source trusted by the client or a signature chain can be established between this certificate and the truested certificate. 

This property may only be modified when no services are associated. See associatedServiceCount.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[certificateSigningRequest]: #certificatesigningrequest
#### [certificateSigningRequest]
The signing request used to request a certificate authority generate a signed certificate. 

This property may only be modified when no services are associated. See associatedServiceCount.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[commonName]: #commonname
#### [commonName]
The common name (usually a domain name) encoded within the certificate. 

This property is read only. Changes made will be silently ignored.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date the certificate _record_ was created. The contents of the certificate may of changed since the record was created, so this does not represent anything about the certificate itself. 

This property is read only. Changes made will be silently ignored.   
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The ID of the certificate record.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[intermediateCertificate]: #intermediatecertificate
#### [intermediateCertificate]
The intermediate certificate authorities certificate that completes the certificate chain for the issued certificate. Required when clients will only trust the root certificate. 

This property may only be modified when no services are associated. See associatedServiceCount.   
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
[modifyDate]: #modifydate
#### [modifyDate]
The date the certificate _record_ was last modified.The contents of the certificate may of changed since the record was created, so this does not represent anything about the certificate itself. 

This property is read only. Changes made will be silently ignored.   
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[notes]: #notes
#### [notes]
A note to help describe the certificate.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[organizationName]: #organizationname
#### [organizationName]
The organizational name encoded in the certificate. 

This property is read only. Changes made will be silently ignored.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[privateKey]: #privatekey
#### [privateKey]
The private key in the key/certificate pair. 

This property may only be modified when no services are associated. See associatedServiceCount.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[validityBegin]: #validitybegin
#### [validityBegin]
The UTC timestamp representing the beginning of the certificate's validity 

This property is read only. Changes made will be silently ignored.   
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[validityDays]: #validitydays
#### [validityDays]
The number of days remaining in the validity period for the certificate. 

This property is read only. Changes made will be silently ignored.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[validityEnd]: #validityend
#### [validityEnd]
The UTC timestamp representing the end of the certificate's validity period. 

This property is read only. Changes made will be silently ignored.   
<span class="type-label">Type: </span>**dateTime**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[associatedServiceCount]: #associatedservicecount
#### [associatedServiceCount]
The number of services currently associated with the certificate.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[loadBalancerVirtualIpAddresses]: #loadbalancervirtualipaddresses
#### [loadBalancerVirtualIpAddresses]
The load balancers virtual IP addresses currently associated with the certificate.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress[] </a>**


</div>

## Count
<div class="prop-row">

-----
[loadBalancerVirtualIpAddressCount]: #loadbalancervirtualipaddresscount
#### [loadBalancerVirtualIpAddressCount]
A count of the load balancers virtual IP addresses currently associated with the certificate.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


