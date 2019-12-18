---
title: "SoftLayer_Container_Account_Historical_Summary_Detail_Uptime"
description: "Historical Summary Details Container for a host resource uptime"
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Account_Historical_Summary_Detail_Uptime"
---

# SoftLayer_Container_Account_Historical_Summary_Detail_Uptime
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Account_Historical_Summary_Detail_Uptime' >Datatype</a></li>
    </ul>
</div>

## Description 
Historical Summary Details Container for a host resource uptime 





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

## Local
-----
[cloudComputingInstance]: #cloudcomputinginstance
#### [cloudComputingInstance]
The hardware for uptime details.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**

-----
[configurationValue]: #configurationvalue
#### [configurationValue]
The configuration value for the detail's resource.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Value'>SoftLayer_Monitoring_Agent_Configuration_Value </a>**

-----
[data]: #data
#### [data]
The data associated with a host uptime details.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Data'>SoftLayer_Metric_Tracking_Object_Data[] </a>**

-----
[endDate]: #enddate
#### [endDate]
The maximum date included in the detail.  
<span class="type-label">Type: </span>**dateTime**

-----
[hardware]: #hardware
#### [hardware]
The hardware for uptime details.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**

-----
[startDate]: #startdate
#### [startDate]
The minimum date included in the detail.  
<span class="type-label">Type: </span>**dateTime**

</div>
<!-- LOCAL PROPERTY END -->

</div>


