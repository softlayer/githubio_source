---
title: "SoftLayer_Network_ContentDelivery_Authentication_Address"
description: "For more details on CDN's content authentication service, see [[SoftLayer_Network_ContentDelivery_Authentication_Token|A... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Authentication_Address"
---
# SoftLayer_Network_ContentDelivery_Authentication_Address
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_ContentDelivery_Authentication_Address' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_ContentDelivery_Authentication_Address' >Datatype</a></li>
    </ul>
</div>

## Description
For more details on CDN's content authentication service, see [[SoftLayer_Network_ContentDelivery_Authentication_Token|Authentication Token]]. 

You can restrict or grant access to your content by configuring an authentication IP address or an IP block. . This configuration will affect the entire secure content of your CDN account. Configuring an authentication IP Address does not mean all of your content will be secured. You must place your content in the right directories (/media/securehttp, /media/secureflash, /media/securewm) and you have to use an authentication token. Authentication IP address validation occurs before a token is validated. Consider authentication IP as an additional way to secure your content. You can have up to 20 IP address records. If you want to block access from IP 211.37.0.0/16, you can enter "211.37." instead. IP blocks can be specified in the manner of "8bit times n". 

{| cellspacing="5" style="width: 40%; border: 0px; margin-left: auto; margin-right: auto; padding: 10px;" 
|-
|style="background: #d2d2d2; padding: 10px; text-align: center;"|'''IP range'''
|style="background: #d2d2d2; padding: 10px; text-align: center;"|'''value you will pass to API'''
|-
|style="background: #e7e7e7"|123.0.0.0/8
|style="background: #e7e7e7"|123.
|-
|style="background: #f5f5f5"|123.123.0.0/16
|style="background: #f5f5f5"|123.123.
|-
|style="background: #e7e7e7"|123.123.123.0/24
|style="background: #e7e7e7"|123.123.123.
|-
|style="background: #e7e7e7"|123.123.123.123
|style="background: #e7e7e7"|123.123.123.123 (Allow or Deny a single IP)
|-
|}




IP match starts from higher priority IP to lower and if there is a match, it will stop the process. 

You can also set an authentication IP with an * (asterisk). This can be helpful if you want to deny all IP addresses. The example below shows that requests from 199.7.0.0/16 are allowed and requests from any other IP ranges are blocked. 

{| cellspacing="5" style="width: 60%; border: 0px; margin-left: auto; margin-right: auto; padding: 10px;" 
|-
|style="background: #d2d2d2; padding: 10px; text-align: center;"|'''Name'''
|style="background: #d2d2d2; padding: 10px; text-align: center;"|'''IP Address'''
|style="background: #d2d2d2; padding: 10px; text-align: center;"|'''Access Type'''
|style="background: #d2d2d2; padding: 10px; text-align: center;"|'''Priority'''
|-
|style="background: #e7e7e7"|Allow from Netherlands
|style="background: #e7e7e7"|199.7.
|style="background: #e7e7e7"|ALLOW
|style="background: #e7e7e7"|10
|-
|style="background: #e7e7e7"|Deny all
|style="background: #e7e7e7"|*
|style="background: #e7e7e7"|DENY
|style="background: #e7e7e7"|20
|-
|}



        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Authentication_Address/createObject'> createObject</a> </span>
            <div class='views-field-body'>Creates an authentication IP record</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Authentication_Address/deleteObject'> deleteObject</a> </span>
            <div class='views-field-body'>Deletes an authentication IP address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Authentication_Address/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edits an authentication IP</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Authentication_Address/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_ContentDelivery_Authentication_Address record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Authentication_Address/rearrangeAuthenticationIp'> rearrangeAuthenticationIp</a> </span>
            <div class='views-field-body'>rearranges authentication IPs</div>
        </div>
        </div>
</div>

