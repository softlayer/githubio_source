---
title: "SoftLayer_Network_LBaaS_L7HealthMonitor"
description: "The SoftLayer_Network_LBaaS_L7HealthMonitor type presents a structure containing attributes of a health monitor object a... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7HealthMonitor"
---

# SoftLayer_Network_LBaaS_L7HealthMonitor
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7HealthMonitor' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Network_LBaaS_L7HealthMonitor type presents a structure containing attributes of a health monitor object associated with a L7 pool instance. Note that the relationship between backend (L7 pool) and health monitor is 1-to-1, pools object associated with a health monitor must have the same pair of protocol and port. Example: frontend FA: http, 80   - backend BA: http, 3456 - healthmonitor HM_http3456 frontend FB: https, 443 - backend BB: http, 3456 - healthmonitor HM_http3456 









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
  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[interval]: #interval
#### [interval]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[maxRetries]: #maxretries
#### [maxRetries]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[monitorType]: #monitortype
#### [monitorType]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[provisioningStatus]: #provisioningstatus
#### [provisioningStatus]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[timeout]: #timeout
#### [timeout]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[urlPath]: #urlpath
#### [urlPath]
  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


