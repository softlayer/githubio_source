---
title: "SoftLayer_Network_Service_Health"
description: "Many general services that SoftLayer provides are tracked on the customer portal with a quick status message. These stat... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Service_Health"
---

# SoftLayer_Network_Service_Health
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Service_Health' >Datatype</a></li>
    </ul>
</div>

## Description 
Many general services that SoftLayer provides are tracked on the customer portal with a quick status message. These status message provide users with a quick reference to the health of a service, whether it's up or down. These services include SoftLayer's Internet backbone connections, VPN entry points, and router networks. The SoftLayer_Network_Service_Health data type provides the relationship between these services and their health status. 



### seeAlso

* [SoftLayer_Network_Service_Health_Status](/reference/datatypes/SoftLayer_Network_Service_Health_Status )




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
[createDate]: #createdate
#### [createDate]
The date that a service's status was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[locationId]: #locationid
#### [locationId]
A service's location identifier.  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date that a service's status was last changed.  
<span class="type-label">Type: </span>**dateTime**

-----
[statusId]: #statusid
#### [statusId]
A service's status identifier.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[location]: #location
#### [location]
A service's location.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[status]: #status
#### [status]
The status portion of a service/status relationship.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Service_Health_Status'>SoftLayer_Network_Service_Health_Status </a>**


## Count
</div>


