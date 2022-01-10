---
title: "SoftLayer_Network_Component_Uplink_Hardware"
description: "The SoftLayer_Network_Component_Uplink_Hardware data type abstracts information related to network connections between S... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component_Uplink_Hardware"
---

# SoftLayer_Network_Component_Uplink_Hardware
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Component_Uplink_Hardware' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Network_Component_Uplink_Hardware data type abstracts information related to network connections between SoftLayer hardware and SoftLayer network components. 

It is populated via triggers on the network_connection table (SoftLayer_Network_Connection), so you shouldn't have to delete or insert records into this table, ever. 





### seeAlso

* [SoftLayer_Hardware](/reference/services/SoftLayer_Hardware )


* [SoftLayer_Network_Component](/reference/services/SoftLayer_Network_Component )




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
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
A network component uplink's connected [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**  



</div>
<div class="prop-row">

-----
[networkComponent]: #networkcomponent
#### [networkComponent]
The [SoftLayer_Network_Component]({{<ref "reference/datatypes/SoftLayer_Network_Component">}}) that a uplink connection belongs to..  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a>**  



</div>

## Count
</div>


