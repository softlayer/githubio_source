---
title: "SoftLayer_Account_Authentication_Saml"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Authentication_Saml"
---

# SoftLayer_Account_Authentication_Saml
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Authentication_Saml' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Authentication_Saml' >Datatype</a></li>
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
[accountId]: #accountid
#### [accountId]
The saml account id.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[certificate]: #certificate
#### [certificate]
The identity provider x509 certificate.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[certificateFingerprint]: #certificatefingerprint
#### [certificateFingerprint]
The identity provider x509 certificate fingerprint.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[entityId]: #entityid
#### [entityId]
The identity provider entity ID.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The saml internal identifying number.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[serviceProviderCertificate]: #serviceprovidercertificate
#### [serviceProviderCertificate]
The service provider x509 certificate.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[serviceProviderEntityId]: #serviceproviderentityid
#### [serviceProviderEntityId]
The service provider entity IDs.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[serviceProviderPublicKey]: #serviceproviderpublickey
#### [serviceProviderPublicKey]
The service provider public key.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[serviceProviderSingleLogoutEncoding]: #serviceprovidersinglelogoutencoding
#### [serviceProviderSingleLogoutEncoding]
The service provider signle logout encoding.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[serviceProviderSingleLogoutUrl]: #serviceprovidersinglelogouturl
#### [serviceProviderSingleLogoutUrl]
The service provider signle logout address.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[serviceProviderSingleSignOnEncoding]: #serviceprovidersinglesignonencoding
#### [serviceProviderSingleSignOnEncoding]
The service provider signle sign on encoding.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[serviceProviderSingleSignOnUrl]: #serviceprovidersinglesignonurl
#### [serviceProviderSingleSignOnUrl]
The service provider signle sign on address.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[singleLogoutEncoding]: #singlelogoutencoding
#### [singleLogoutEncoding]
The identity provider single logout encoding.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[singleLogoutUrl]: #singlelogouturl
#### [singleLogoutUrl]
The identity provider sigle logout address.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[singleSignOnEncoding]: #singlesignonencoding
#### [singleSignOnEncoding]
The identity provider single sign on encoding.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[singleSignOnUrl]: #singlesignonurl
#### [singleSignOnUrl]
The identity provider signle sign on address.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account associated with this saml configuration.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[attributes]: #attributes
#### [attributes]
The saml attribute values for a SoftLayer customer account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Authentication_Attribute'>SoftLayer_Account_Authentication_Attribute[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of the saml attribute values for a SoftLayer customer account.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


