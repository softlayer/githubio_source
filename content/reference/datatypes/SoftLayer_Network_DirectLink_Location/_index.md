---
title: "SoftLayer_Network_DirectLink_Location"
description: "The SoftLayer_Network_DirectLink_Location presents a structure containing attributes of a Direct Link location, and its... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_DirectLink_Location"
---

# SoftLayer_Network_DirectLink_Location
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_DirectLink_Location' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_DirectLink_Location' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_DirectLink_Location presents a structure containing attributes of a Direct Link location, and its related object SoftLayer location. 





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
[buildingColocationOwner]: #buildingcolocationowner
#### [buildingColocationOwner]
The Direct Link specific location owner for POP/DC facilities. Like Equinix, Pacnet, Verizon etc.   
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
The unique identifier of a Direct Link location.  
<span class="type-label">Type: </span>**integer**

-----
[isRedundantXcr]: #isredundantxcr
#### [isRedundantXcr]
Specifies if The Direct Link specific location has Redundancy:secondary XCR availability.   
<span class="type-label">Type: </span>**boolean**

-----
[locationId]: #locationid
#### [locationId]
The Direct Link specific location ie. Data Center & Network POP facility. Refer to location object Like Dallas in US, London in England etc.   
<span class="type-label">Type: </span>**integer**

-----
[marketGeography]: #marketgeography
#### [marketGeography]
The Direct Link Market location used in Direct Link Order. Like Europe, North America, Asia pacific etc.   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[location]: #location
#### [location]
The location of Direct Link facility.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[provider]: #provider
#### [provider]
The Id of Direct Link provider.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_DirectLink_Provider'>SoftLayer_Network_DirectLink_Provider </a>**

-----
[serviceType]: #servicetype
#### [serviceType]
The Id of Direct Link service type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_DirectLink_ServiceType'>SoftLayer_Network_DirectLink_ServiceType </a>**


## Count
</div>


