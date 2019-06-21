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
        <h2>Local</h2>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hardware" name=hardware>hardware</a>
            </span>
            <div class='views-field-body'>A network component uplink's connected [[SoftLayer_Hardware|Hardware]]. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#networkComponent" name=networkComponent>networkComponent</a>
            </span>
            <div class='views-field-body'>The [[SoftLayer_Network_Component|Network Component]] that a uplink connection belongs to.. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


