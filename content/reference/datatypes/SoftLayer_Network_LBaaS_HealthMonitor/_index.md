---
title: "SoftLayer_Network_LBaaS_HealthMonitor"
description: "The SoftLayer_Network_LBaaS_HealthMonitor type presents a structure containing attributes of a health monitor object ass... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_HealthMonitor"
---

# SoftLayer_Network_LBaaS_HealthMonitor
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_LBaaS_HealthMonitor' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LBaaS_HealthMonitor' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_LBaaS_HealthMonitor type presents a structure containing attributes of a health monitor object associated with load balancer instance. Note that the relationship between backend (pool) and health monitor is N-to-1, especially that the pools object associated with a health monitor must have the same pair of protocol and port. Example: frontend FA: http, 80   - backend BA: tcp, 3456 - healthmonitor HM_tcp3456 frontend FB: https, 443 - backend BB: tcp, 3456 - healthmonitor HM_tcp3456 In above example both backends BA and BB share the same healthmonitor HM_tcp3456 





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
[createDate]: #createdate
#### [createDate]
Create date of the health monitor instance  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Health monitor's identifier  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[interval]: #interval
#### [interval]
Interval in seconds to perform health check  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[maxRetries]: #maxretries
#### [maxRetries]
Maximum number of health check retries in case of failure  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
Modify date of the health monitor instance  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[monitorType]: #monitortype
#### [monitorType]
Type of health check, valid values are "TCP", "HTTP" and "HTTPS"  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[provisioningStatus]: #provisioningstatus
#### [provisioningStatus]
Provisioning status of the health monitor, supported values are "CREATE_PENDING",  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[timeout]: #timeout
#### [timeout]
Timeout in seconds to wait for health checks response  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[urlPath]: #urlpath
#### [urlPath]
If monitorType is "HTTP" this specifies the whole URL path  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[uuid]: #uuid
#### [uuid]
Health monitor's UUID  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


