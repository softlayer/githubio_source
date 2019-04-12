---
title: "SoftLayer_Network"
description: "Provides services oriented to network-centric discovery and manipulation."
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network"
---
# SoftLayer_Network
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network' >Datatype</a></li>
    </ul>
</div>

## Description
Provides services oriented to network-centric discovery and manipulation. 



        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network/connectPrivateEndpointService'> connectPrivateEndpointService</a> </span>
            <div class='views-field-body'>Establishes a connection between the account and Service Endpoint networks.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network/disconnectPrivateEndpointService'> disconnectPrivateEndpointService</a> </span>
            <div class='views-field-body'>Terminates the connection between the account and Service Endpoint networks.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network/getCidr'> getCidr</a> </span>
            <div class='views-field-body'>Retrieve the size of the Network specified in CIDR notation. Specified in conjunction with the ``networkIdentifier`` to describe the bounding subnet size for the Network. Required for creation. See [[SoftLayer_Network/createObject]] documentation for creation details.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network/getName'> getName</a> </span>
            <div class='views-field-body'>Retrieve a name for the Network. This is required during creation of a Network and is entirely user defined.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network/getNetworkIdentifier'> getNetworkIdentifier</a> </span>
            <div class='views-field-body'>Retrieve the starting IP address of the Network. Specified in conjunction with the ``cidr`` property to specify the bounding IP address space for the Network. Required for creation. See [[SoftLayer_Network/createObject]] documentation for creation details.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network/getNotes'> getNotes</a> </span>
            <div class='views-field-body'>Retrieve notes, or a description of the Network. This is entirely user defined.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network/getSubnets'> getSubnets</a> </span>
            <div class='views-field-body'>Retrieve the Subnets within the Network. These represent the realized segments of the Network and reside within a [[SoftLayer_Network_Pod|Pod]]. A Subnet must be specified when provisioning a compute resource within a Network.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network/isConnectedToPrivateEndpointService'> isConnectedToPrivateEndpointService</a> </span>
            <div class='views-field-body'>Checks the current Service Endpoint network connection status.</div>
        </div>
        </div>
</div>

