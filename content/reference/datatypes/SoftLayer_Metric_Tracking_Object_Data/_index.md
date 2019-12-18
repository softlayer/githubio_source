---
title: "SoftLayer_Metric_Tracking_Object_Data"
description: "SoftLayer_Metric_Tracking_Object_Data models an individual unit of data tracked by a SoftLayer tracking object, includin... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Metric"
classes:
    - "SoftLayer_Metric_Tracking_Object_Data"
---

# SoftLayer_Metric_Tracking_Object_Data
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Data' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Metric_Tracking_Object_Data models an individual unit of data tracked by a SoftLayer tracking object, including the type of data polled, the date it was polled at, and the counter value that was measured at polling time. 


### associatedMethods

*  [SoftLayer_Metric_Tracking_Object::getBandwidthData](/reference/services/SoftLayer_Metric_Tracking_Object/getBandwidthData )



### seeAlso

* [SoftLayer_Metric_Tracking_Object](/reference/services/SoftLayer_Metric_Tracking_Object )




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
[counter]: #counter
#### [counter]
The value stored for a data record.   
<span class="type-label">Type: </span>**float**

-----
[dateTime]: #datetime
#### [dateTime]
The time a data record was stored.   
<span class="type-label">Type: </span>**dateTime**

-----
[type]: #type
#### [type]
The type of data held in a record.   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

</div>


