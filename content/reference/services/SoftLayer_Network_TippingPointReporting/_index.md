---
title: "SoftLayer_Network_TippingPointReporting"
description: "This general purpose class is used to retrieve intrusion protection statistics from the tipping point hardware located o... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_TippingPointReporting"
---
# SoftLayer_Network_TippingPointReporting
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_TippingPointReporting' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_TippingPointReporting' >Datatype</a></li>
    </ul>
</div>

## Description
This general purpose class is used to retrieve intrusion protection statistics from the tipping point hardware located on the softlayer network. 

Every customer has access to the global intrusion protection statistics, as well as the detailed statistics for that user's account. 

No actions can be taken using this system, it is for statistical reporting purposes only. If an attacking IP is identified using this system, please use the firewall system to take any actions that are appropriate. 

This system reports attacks on all SoftLayer data centers. 



        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_TippingPointReporting/drillDownAttack'> drillDownAttack</a> </span>
            <div class='views-field-body'>Allows for attack-specific drill downs.  Available only in ascending time order.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_TippingPointReporting/getMainStatistics'> getMainStatistics</a> </span>
            <div class='views-field-body'>Returns the main statistics for the entire SoftLayer network, as well as your particular account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_TippingPointReporting/getReportForIpAddressOrSubnet'> getReportForIpAddressOrSubnet</a> </span>
            <div class='views-field-body'>Returns a point-by-point breakdown of all attacks on a particular IP or subnet in the given time period.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_TippingPointReporting/getSubnetReportForEntireAccount'> getSubnetReportForEntireAccount</a> </span>
            <div class='views-field-body'>Returns a breakdown of all attacks on all subnets owned by this account.</div>
        </div>
        </div>
</div>

