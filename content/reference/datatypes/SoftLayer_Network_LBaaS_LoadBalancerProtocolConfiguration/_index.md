---
title: "SoftLayer_Network_LBaaS_LoadBalancerProtocolConfiguration"
description: "SoftLayer_Network_LBaaS_LoadBalancerProtocolConfiguration specifies the protocol, port, maximum number of allowed connec... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_LoadBalancerProtocolConfiguration"
---

# SoftLayer_Network_LBaaS_LoadBalancerProtocolConfiguration
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancerProtocolConfiguration' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Network_LBaaS_LoadBalancerProtocolConfiguration specifies the protocol, port, maximum number of allowed connections and session stickiness for load balancer's front- and backend. 





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
                <a href="#backendPort" name=backendPort>backendPort</a>
            </span>
            <div class='views-field-body'>Backends port </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#backendProtocol" name=backendProtocol>backendProtocol</a>
            </span>
            <div class='views-field-body'><<EOT </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#frontendPort" name=frontendPort>frontendPort</a>
            </span>
            <div class='views-field-body'>Frontends port </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#frontendProtocol" name=frontendProtocol>frontendProtocol</a>
            </span>
            <div class='views-field-body'><<EOT </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#listenerUuid" name=listenerUuid>listenerUuid</a>
            </span>
            <div class='views-field-body'>Listeners UUID, required for update only </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#loadBalancingMethod" name=loadBalancingMethod>loadBalancingMethod</a>
            </span>
            <div class='views-field-body'><<EOT </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#maxConn" name=maxConn>maxConn</a>
            </span>
            <div class='views-field-body'>Maximum number of allowed connections </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#sessionCookieName" name=sessionCookieName>sessionCookieName</a>
            </span>
            <div class='views-field-body'>Sessions cookie name </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#sessionType" name=sessionType>sessionType</a>
            </span>
            <div class='views-field-body'>Session stickiness type. Valid values are "SOURCE_IP" "HTTP_COOKIE" </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#tlsCertificateId" name=tlsCertificateId>tlsCertificateId</a>
            </span>
            <div class='views-field-body'>ssl/tls certificate id </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
    </div>


