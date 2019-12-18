---
title: "SoftLayer_Container_Network_IntrusionProtection_Statistics"
description: "The IntrusionProtection_Statistics Type is used as a container for SoftLayer_Container_Network_IntrusionProtection_Stati... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_IntrusionProtection_Statistics"
---

# SoftLayer_Container_Network_IntrusionProtection_Statistics
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_IntrusionProtection_Statistics' >Datatype</a></li>
    </ul>
</div>

## Description 
The IntrusionProtection_Statistics Type is used as a container for SoftLayer_Container_Network_IntrusionProtection_Statistic objects.  The SoftLayer_Container_Network_IntrusionProtection_Statistics class holds the "header" information, like the item being queried (either account or data center), the time frame, and the grand total of the attacks. 


### associatedMethods

*  [SoftLayer_Network_TippingPointReporting::getMainStatistics](/reference/services/SoftLayer_Network_TippingPointReporting/getMainStatistics )





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
[target]: #target
#### [target]
The actual target, either a datacenter name, an account ID, or a subnet IP  
<span class="type-label">Type: </span>**string**

-----
[targetType]: #targettype
#### [targetType]
The type of the target, right now either "datacenter", "account", or "subnet"  
<span class="type-label">Type: </span>**string**

-----
[timeFrame]: #timeframe
#### [timeFrame]
The time frame of the attack, in string form, like "Last 24 hours"  
<span class="type-label">Type: </span>**string**

-----
[topAttacks]: #topattacks
#### [topAttacks]
The top attacks for this target over this time frame  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Network_IntrusionProtection_Statistic'>SoftLayer_Container_Network_IntrusionProtection_Statistic[] </a>**

-----
[totalAttacks]: #totalattacks
#### [totalAttacks]
Total attacks for this $target over this time frame  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

</div>


