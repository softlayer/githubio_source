---
title: "SoftLayer_Auxiliary_Network_Status"
description: "This service provides a way for a SoftLayer customer to obtain current latency information from around the world to our... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Auxiliary"
classes:
    - "SoftLayer_Auxiliary_Network_Status"
---
# SoftLayer_Auxiliary_Network_Status
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Auxiliary_Network_Status' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Auxiliary_Network_Status' >Datatype</a></li>
    </ul>
</div>

## Description
This service provides a way for a SoftLayer customer to obtain current latency information from around the world to our datacenters, and segments of our network both public and private. There are a few valid targets. Currently the valid targets are as follows: 
* ALL
* NETWORK_DALLAS
* NETWORK_HOUSTON
* NETWORK_SANJOSE
* NETWORK_SEATTLE
* NETWORK_WDC
* NETWORK_PUBLIC
* NETWORK_PUBLIC_DALLAS
* NETWORK_PUBLIC_HOUSTON
* NETWORK_PUBLIC_SANJOSE
* NETWORK_PUBLIC_SEATTLE
* NETWORK_PUBLIC_WDC
* NETWORK_PRIVATE
* NETWORK_PRIVATE_DALLAS
* NETWORK_PRIVATE_HOUSTON
* NETWORK_PRIVATE_SANJOSE
* NETWORK_PRIVATE_SEATTLE
* NETWORK_PRIVATE_WDC
Information 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [getNetworkStatus](/reference/services/SoftLayer_Auxiliary_Network_Status/getNetworkStatus)
return current network status for a given target.
</div>
</div>

</div>

