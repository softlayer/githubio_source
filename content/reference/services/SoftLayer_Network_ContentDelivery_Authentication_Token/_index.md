---
title: "SoftLayer_Network_ContentDelivery_Authentication_Token"
description: "CDN's content authentication service is the technology that allows only authorized user to access your content. It perfo... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Authentication_Token"
---
# SoftLayer_Network_ContentDelivery_Authentication_Token
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_ContentDelivery_Authentication_Token' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_ContentDelivery_Authentication_Token' >Datatype</a></li>
    </ul>
</div>

## Description
CDN's content authentication service is the technology that allows only authorized user to access your content. It performs a token based authentication before delivering content. An authentication token can be obtained from the SoftLayer customer portal or API and it needs to be appended to the CDN URL. When an end-user requests a file, CDN server will check the validity of the token passed via HTTP GET string. Then the content will be delivered if the token is validated otherwise the connection will be rejected. 

There are several scenarios where this authentication capability could be useful. If a website doesn't require authentication, it runs the risk of other sites hot-linking to its images. Content owners can prevent others sites from passing HTTP links to images by requiring authentication in order to view a site's contents. Leverage the API to add this additional layer of security through our Content Authentication service. 

To begin using the Content Authentication service, define secure directions using the [[SoftLayer_Network_ContentDelivery_Account::createTokenAuthenticationDirectory|createTokenAuthenticationDirectory]] method. Refer to the table below for examples of token authentication URLs. 

{| cellspacing="5" style="width: 90%; border: 0px; margin-left: auto; margin-right: auto; padding: 10px;" 
|-
|style="background: #d2d2d2; padding: 10px; text-align: center;"|'''Media Type'''
|style="background: #d2d2d2; padding: 10px; text-align: center;"|'''Token Auth Directory'''
|style="background: #d2d2d2; padding: 10px; text-align: center;"|'''CDN URL Type'''
|style="background: #d2d2d2; padding: 10px; text-align: center;"|'''Example URL'''
|-
|style="background: #e7e7e7; text-align: center;"|HTTP
|style="background: #e7e7e7; text-align: center;"|(FTP) /securehttp
|style="background: #e7e7e7; text-align: center;"|Default
|style="background: #e7e7e7"|http://(CDN_NAME).http.cdn.softlayer.net/00(CDN_NAME)/securehttp/example.jpg?ramdomTokenString
|-
|style="background: #e7e7e7; text-align: center;"|HTTP
|style="background: #e7e7e7; text-align: center;"|(Customer Origin) http://myorigin.com/securehttp
|style="background: #e7e7e7; text-align: center;"|Default
|style="background: #e7e7e7"|http://(CDN_NAME).http.cdn.softlayer.net/80(CDN_NAME)/myorigin.com/securehttp/example.jpg?ramdomTokenString
|-
|style="background: #e7e7e7; text-align: center;"|HTTP
|style="background: #e7e7e7; text-align: center;"|(FTP or Custom Origin)
|style="background: #e7e7e7; text-align: center;"|CNAME
|style="background: #e7e7e7"|http://cdn.mydomain.com/example.jpg?ramdomTokenString
|-
|style="background: #e7e7e7; text-align: center;"|Streaming Flash
|style="background: #e7e7e7; text-align: center;"|(FTP) /secureflash
|style="background: #e7e7e7; text-align: center;"|Default
|style="background: #e7e7e7"|rtmp://(CDN_NAME).flash.cdn.softlayer.net/00(CDN_NAME)/secureflash/example.flv?ramdomTokenString
|-
|style="background: #e7e7e7; text-align: center;"|Streaming Flash
|style="background: #e7e7e7; text-align: center;"|(Customer Origin) http://myorigin.com/secureflash
|style="background: #e7e7e7; text-align: center;"|Default
|style="background: #e7e7e7"|rtmp://(CDN_NAME).flash.cdn.softlayer.net/80(CDN_NAME)/myorigin.com/secureflash/example.flv?ramdomTokenString
|-
|style="background: #e7e7e7; text-align: center;"|Streaming Flash
|style="background: #e7e7e7; text-align: center;"|(FTP or Custom Origin)
|style="background: #e7e7e7; text-align: center;"|CNAME
|style="background: #e7e7e7"|rtmp://flash.mydomain.com/example.flv?ramdomTokenString
|-
|style="background: #e7e7e7; text-align: center;"|Streaming Windows Media
|style="background: #e7e7e7; text-align: center;"|(FTP) /securewm
|style="background: #e7e7e7; text-align: center;"|Default
|style="background: #e7e7e7"| mms://(CDN_NAME).flash.cdn.softlayer.net/00(CDN_NAME)/securewm/example.wmv?ramdomTokenString
|-
|}


Note. Windows Media does not support customer origin. Token authentication can be ordered as a CDN add-on item. 

'''Authentication Token''' 

Authentication tokens expire after the specified time (in seconds) has elapsed. Set a token's expiration time by passing the number of seconds the token should remain active to the [[SoftLayer_Network_ContentDelivery_Authentication_Token::getTimedToken|getTimedToken]] method. For example, if you pass 3600 for the token life to the [[SoftLayer_Network_ContentDelivery_Authentication_Token::getTimedToken|getTimedToken]] method, it will return a token that will expire after an hour of its creation. There is no way to revoke a timed token.  To create a timed token, use the [[SoftLayer_Network_ContentDelivery_Authentication_Token::getTimedToken|getTimedToken]] method and it takes 3 parameters: 

<dl> <dt>'''Token Life (required)'''</dt> <dd>This value is defined in seconds and outlines the amount of time a token remains valid. To create a token that expires in an hour, pass a Token Life of 3600. The minimum value for Token Life is 60 seconds and the maximum value is 604800 seconds, or one week.</dd> 

<dt>'''Client IP (optional)'''</dt> <dd>If set, the token validation process will match the client IP address. A valid IP address should be an IPv4 format or an IP block. If you want to block access from IP 211.37.0.0/16, you can enter "211.37." instead. IP blocks can be specified in the manner of "8bit times n".</dd> 

<dt>'''Referring domain (optional)'''</dt> <dd>The referrer or referring page is the URL of the previous webpage from which a link was followed. You can further restrict access to your contents by matching referrer information. Set this value only if you are certain about referrer you're expecting. You can only set a domain or an IP address without a path or a file name in it. This can be a part of your domain. If you want to grant access from any of your subdomains, set the root domain as a referring domain.</dd> </dl> 



        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Authentication_Token/createObject'> createObject</a> </span>
            <div class='views-field-body'>(DEPRECATED) Creates a managed authentication token</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Authentication_Token/getAllManagedTokens'> getAllManagedTokens</a> </span>
            <div class='views-field-body'>(DEPRECATED) Returns all managed tokens for a CDN account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Authentication_Token/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_ContentDelivery_Authentication_Token record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Authentication_Token/getTimedToken'> getTimedToken</a> </span>
            <div class='views-field-body'>Returns an authentication token that expires after a certain amount of time</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Authentication_Token/revokeAllManagedTokens'> revokeAllManagedTokens</a> </span>
            <div class='views-field-body'>(DEPRECATED) Revokes all managed tokens belong to a CDN account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Authentication_Token/revokeAllTokens'> revokeAllTokens</a> </span>
            <div class='views-field-body'>Revokes all tokens belong to a CDN account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Authentication_Token/revokeManagedToken'> revokeManagedToken</a> </span>
            <div class='views-field-body'>(DEPRECATED) Revokes a managed token</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Authentication_Token/revokeManagedTokens'> revokeManagedTokens</a> </span>
            <div class='views-field-body'>(DEPRECATED) Deletes multiple managed tokens</div>
        </div>
        </div>
</div>

