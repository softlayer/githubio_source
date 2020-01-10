---
title: "SoftLayer_Network_Backbone"
description: "A SoftLayer_Network_Backbone represents a single backbone connection from SoftLayer to the public Internet, from the Int... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Backbone"
---

# SoftLayer_Network_Backbone
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Backbone' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Backbone' >Datatype</a></li>
    </ul>
</div>

## Description 
A SoftLayer_Network_Backbone represents a single backbone connection from SoftLayer to the public Internet, from the Internet to the SoftLayer private network, or a link that connects the private networks between SoftLayer's datacenters. The SoftLayer_Network_Backbone data type is a collection of data associated with one of those connections. 


### associatedMethods

*  [SoftLayer_Network_Backbone::getObject](/reference/services/SoftLayer_Network_Backbone/getObject )
*  [SoftLayer_Network_Backbone::getAllBackbones](/reference/services/SoftLayer_Network_Backbone/getAllBackbones )





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
[capacity]: #capacity
#### [capacity]
The numeric portion of the bandwidth capacity of a SoftLayer backbone. For instance, if a backbone is rated at "1 GigE" capacity then the capacity property of the backbone is 1.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[capacityUnits]: #capacityunits
#### [capacityUnits]
The unit portion of the bandwidth capacity of a SoftLayer backbone. For instance, if a backbone is rated at "10 G" capacity then the capacityUnits property of the backbone is "G".   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A backbone's internal identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A backbone's name. This is usually the name of the backbone's network provider followed by a number in case SoftLayer uses more than one backbone from a provider. Backbone provider numbers start with the number one and increment from there.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[networkComponentId]: #networkcomponentid
#### [networkComponentId]
The internal identifier of the network component that backbone is connected to.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
Whether a SoftLayer backbone connects to the public Internet, to the private network, or connecting the private networks of SoftLayer's datacenters. Type is either the string "public", "private", or "private-interconnect".   
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[health]: #health
#### [health]
A backbone's status.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[location]: #location
#### [location]
Which of the SoftLayer datacenters a backbone is connected to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


</div>
<div class="prop-row">

-----
[networkComponent]: #networkcomponent
#### [networkComponent]
A backbone's primary network component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a>**


</div>

## Count
</div>


