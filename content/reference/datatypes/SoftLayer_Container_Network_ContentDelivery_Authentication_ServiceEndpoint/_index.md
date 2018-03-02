---
title: "SoftLayer_Container_Network_ContentDelivery_Authentication_ServiceEndpoint"
description: "CDN supports the content authentication service. With the content authentication service, customers can control access t... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_ContentDelivery_Authentication_ServiceEndpoint"
---

# SoftLayer_Container_Network_ContentDelivery_Authentication_ServiceEndpoint
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_ContentDelivery_Authentication_ServiceEndpoint' >Datatype</a></li>
    </ul>
</div>

## Description 
CDN supports the content authentication service. With the content authentication service, customers can control access to their contents. There are several scenarios where this authentication capability could be useful. Websites can prevent other rogue websites from linking to their videos. Content owners can prevent users from passing around http links, thus forcing them to login to view contents. It is also possible to authenticate via the client IP address. Referrer information is also checked if provided by a client's browser. servers will invoke a web service method to validate a content authentication token. 

CDN uses the default authentication web service provided by SoftLayer to validate a token. A customer can use their own implementation of the token authentication web service by using [[SoftLayer_Network_ContentDelivery_Account::setAuthenticationServiceEndpoint|setAuthenticationServiceEndpoint]] method. 

This container class holds the token validation web service endpoint information. CDN supports 3 different protocols: HTTP, RTMP (streaming Flash), and MMS (streaming Windows Media) 

### External Links


* [CDN Services at softlayer.com](http://www.softlayer.com/services_cdnlayer.html)



### associatedMethods

*  [SoftLayer_Network_ContentDelivery_Account::setAuthenticationServiceEndpoint](/reference/services/SoftLayer_Network_ContentDelivery_Account/setAuthenticationServiceEndpoint )



### seeAlso

* [SoftLayer_Network_ContentDelivery_Account](/reference/datatypes/SoftLayer_Network_ContentDelivery_Account )




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
            <span class='views-field-title'><a href="#endpoint" name=endpoint>endpoint</a></span>
            <div class='views-field-body'>The authentication web service endpoint that CDN servers will use to validate a token </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#protocol" name=protocol>protocol</a></span>
            <div class='views-field-body'>The protocol that the WSDL will be used for.  This can be HTTP, WINDOWSMEDIA, or FLASH </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
    </div>


