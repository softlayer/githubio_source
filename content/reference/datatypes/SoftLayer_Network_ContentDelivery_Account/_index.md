---
title: "SoftLayer_Network_ContentDelivery_Account"
description: "The SoftLayer_Network_ContentDelivery_Account data type models an individual CDN account. CDN accounts contain reference... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
---

# SoftLayer_Network_ContentDelivery_Account
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_ContentDelivery_Account' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_ContentDelivery_Account data type models an individual CDN account. CDN accounts contain references to the SoftLayer customer account they belong to, login credentials for upload services, and a CDN account's status. Please contact SoftLayer sales to purchase or cancel a CDN account 

### External Links


* [Content delivery network at Wikipedia](http://en.wikipedia.org/wiki/Content_delivery_network)


* [CDN Services at softlayer.com](http://knowledgelayer.softlayer.com/topic/cdn)



### associatedMethods

*  [SoftLayer_Account::getCdnAccounts](/reference/services/SoftLayer_Account/getCdnAccounts )
*  [SoftLayer_Network_ContentDelivery_Account::getObject](/reference/services/SoftLayer_Network_ContentDelivery_Account/getObject )





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
            <div class='views-field-body'>The internal identifier of the customer account that a CDN account belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The date that a CDN account was created. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A CDN account's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#statusId" name=statusId>statusId</a></span>
            <div class='views-field-body'>The internal identifier of a CDN status </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'>The customer account that a CDN account belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#associatedCdnAccountId" name=associatedCdnAccountId>associatedCdnAccountId</a></span>
            <div class='views-field-body'>The CDN account id that this CDN account is associated with. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#authenticationIpAddresses" name=authenticationIpAddresses>authenticationIpAddresses</a></span>
            <div class='views-field-body'>The IP addresses that are used for the content authentication service. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_ContentDelivery_Authentication_Address'>SoftLayer_Network_ContentDelivery_Authentication_Address[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingItem" name=billingItem>billingItem</a></span>
            <div class='views-field-body'>The current billing item for a CDN account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cdnAccountName" name=cdnAccountName>cdnAccountName</a></span>
            <div class='views-field-body'>The name of a CDN account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cdnAccountNote" name=cdnAccountNote>cdnAccountNote</a></span>
            <div class='views-field-body'>A brief note on a CDN account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cdnSolutionName" name=cdnSolutionName>cdnSolutionName</a></span>
            <div class='views-field-body'>The solution type of a CDN account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#dependantServiceFlag" name=dependantServiceFlag>dependantServiceFlag</a></span>
            <div class='views-field-body'>Indicates if CDN account is dependent on other service. If set, this CDN account is limited to these services: createOriginPullMapping, deleteOriginPullRule, getOriginPullMappingInformation, getCdnUrls, purgeCache, loadContent, manageHttpCompression </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#legacyCdnFlag" name=legacyCdnFlag>legacyCdnFlag</a></span>
            <div class='views-field-body'>Indicates if it is a legacy CDN or not </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#logEnabledFlag" name=logEnabledFlag>logEnabledFlag</a></span>
            <div class='views-field-body'>Indicates if CDN logging is enabled. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#providerPortalAccessFlag" name=providerPortalAccessFlag>providerPortalAccessFlag</a></span>
            <div class='views-field-body'>Indicates if customer is allowed to access the CDN provider's management portal. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#status" name=status>status</a></span>
            <div class='views-field-body'>A CDN account's status presented in a more detailed data type. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_ContentDelivery_Account_Status'>SoftLayer_Network_ContentDelivery_Account_Status </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#tokenAuthenticationEnabledFlag" name=tokenAuthenticationEnabledFlag>tokenAuthenticationEnabledFlag</a></span>
            <div class='views-field-body'>Indicates if the token authentication service is enabled or not. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#authenticationIpAddressCount" name=authenticationIpAddressCount>authenticationIpAddressCount</a></span>
            <div class='views-field-body'>A count of the IP addresses that are used for the content authentication service. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


