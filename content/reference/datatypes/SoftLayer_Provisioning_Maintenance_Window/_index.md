---
title: "SoftLayer_Provisioning_Maintenance_Window"
description: "The SoftLayer_Provisioning_Maintenance_Window represent a time window that SoftLayer performs a hardware or software mai... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Provisioning"
classes:
    - "SoftLayer_Provisioning_Maintenance_Window"
---

# SoftLayer_Provisioning_Maintenance_Window
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Provisioning_Maintenance_Window' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Provisioning_Maintenance_Window' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Provisioning_Maintenance_Window represent a time window that SoftLayer performs a hardware or software maintenance and upgrades. 


### associatedMethods

*  [SoftLayer_Provisioning_Maintenance_Window::getMaintenanceWindows](/reference/services/SoftLayer_Provisioning_Maintenance_Window/getMaintenanceWindows )



### seeAlso

* [SoftLayer_Product_Order_Upgrade_Request](/reference/datatypes/SoftLayer_Product_Order_Upgrade_Request )




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
[beginDate]: #begindate
#### [beginDate]
The date and time a maintenance window is scheduled to begin.  
<span class="type-label">Type: </span>**dateTime**

-----
[dayOfWeek]: #dayofweek
#### [dayOfWeek]
An ISO-8601 numeric representation of the day of the week that a maintenance window is performed. 1: Monday, 7: Sunday  
<span class="type-label">Type: </span>**integer**

-----
[endDate]: #enddate
#### [endDate]
The date and time a maintenance window is scheduled to end.  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
Id of the maintenance window  
<span class="type-label">Type: </span>**integer**

-----
[locationId]: #locationid
#### [locationId]
An internal identifier of the location (data center) record that a maintenance window takes place in.  
<span class="type-label">Type: </span>**integer**

-----
[portalTzId]: #portaltzid
#### [portalTzId]
An internal identifier of the datacenter timezone.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

</div>


