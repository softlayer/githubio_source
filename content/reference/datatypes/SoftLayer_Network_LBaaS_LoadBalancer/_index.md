---
title: "SoftLayer_Network_LBaaS_LoadBalancer"
description: "The SoftLayer_Network_LBaaS_LoadBalancer type presents a structure containing attributes of a load balancer, and its rel... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_LoadBalancer"
---

# SoftLayer_Network_LBaaS_LoadBalancer
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_LBaaS_LoadBalancer' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancer' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_LBaaS_LoadBalancer type presents a structure containing attributes of a load balancer, and its related objects including listeners, pools and members. 





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
                <a href="#accountId" name=accountId>accountId</a>
            </span>
            <div class='views-field-body'>The account this load balancer belongs to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#address" name=address>address</a>
            </span>
            <div class='views-field-body'>Address (Host name) of a load balancer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'>Specifies when a load balancer was created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#description" name=description>description</a>
            </span>
            <div class='views-field-body'>Description of a load balancer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The unique identifier of a load balancer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#isPublic" name=isPublic>isPublic</a>
            </span>
            <div class='views-field-body'>Specifies whether the load balancer is a public or internal load balancer.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#locationId" name=locationId>locationId</a>
            </span>
            <div class='views-field-body'>This references to location with type datacenter </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'>Specifies when a load balancer was updated last. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#name" name=name>name</a>
            </span>
            <div class='views-field-body'>The load balancer's name. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#operatingStatus" name=operatingStatus>operatingStatus</a>
            </span>
            <div class='views-field-body'>The operation status "ONLINE" or "OFFLINE" of a load balancer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#previousErrorText" name=previousErrorText>previousErrorText</a>
            </span>
            <div class='views-field-body'>Error message of previous API call in case of failure </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#provisioningStatus" name=provisioningStatus>provisioningStatus</a>
            </span>
            <div class='views-field-body'>The provisioning status of a load balancer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#useSystemPublicIpPool" name=useSystemPublicIpPool>useSystemPublicIpPool</a>
            </span>
            <div class='views-field-body'>Applicable for public load balancer only. It specifies whether the public IP addresses are allocated from system public IP pool (1, default) or public subnet (null | 0) from the account ordering the load balancer. For internal load balancer, useSystemPublicIpPool will be ignored, and it always defaults to 1.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#uuid" name=uuid>uuid</a>
            </span>
            <div class='views-field-body'>The UUID of a load balancer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#datacenter" name=datacenter>datacenter</a>
            </span>
            <div class='views-field-body'>Datacenter, where load balancer is located. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#healthMonitors" name=healthMonitors>healthMonitors</a>
            </span>
            <div class='views-field-body'>Health monitors for the backend members. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_LBaaS_HealthMonitor'>SoftLayer_Network_LBaaS_HealthMonitor[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#l7Pools" name=l7Pools>l7Pools</a>
            </span>
            <div class='views-field-body'>L7Pools for load balancer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7Pool'>SoftLayer_Network_LBaaS_L7Pool[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#listeners" name=listeners>listeners</a>
            </span>
            <div class='views-field-body'>Listeners assigned to load balancer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_LBaaS_Listener'>SoftLayer_Network_LBaaS_Listener[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#members" name=members>members</a>
            </span>
            <div class='views-field-body'>Members assigned to load balancer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_LBaaS_Member'>SoftLayer_Network_LBaaS_Member[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#sslCiphers" name=sslCiphers>sslCiphers</a>
            </span>
            <div class='views-field-body'>list of preferred custom ciphers configured for the load balancer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_LBaaS_SSLCipher'>SoftLayer_Network_LBaaS_SSLCipher[] </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#healthMonitorCount" name=healthMonitorCount>healthMonitorCount</a>
            </span>
            <div class='views-field-body'>A count of health monitors for the backend members. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#l7PoolCount" name=l7PoolCount>l7PoolCount</a>
            </span>
            <div class='views-field-body'>A count of l7Pools for load balancer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#listenerCount" name=listenerCount>listenerCount</a>
            </span>
            <div class='views-field-body'>A count of listeners assigned to load balancer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#memberCount" name=memberCount>memberCount</a>
            </span>
            <div class='views-field-body'>A count of members assigned to load balancer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#sslCipherCount" name=sslCipherCount>sslCipherCount</a>
            </span>
            <div class='views-field-body'>A count of list of preferred custom ciphers configured for the load balancer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


