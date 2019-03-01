---
title: "SoftLayer_Location"
description: "The SoftLayer_Location API service queries SoftLayer's location tree to find locations for all softlayer resources inclu... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location"
---
# SoftLayer_Location
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Location' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Location' >Datatype</a></li>
    </ul>
</div>

## Description
The SoftLayer_Location API service queries SoftLayer's location tree to find locations for all softlayer resources including bare metal servers, virtual servers, storage repositories, datacenters, points of presence, network backbones, and many more. 



        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getActivePresaleEvents'> getActivePresaleEvents</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getAvailableObjectStorageDatacenters'> getAvailableObjectStorageDatacenters</a> </span>
            <div class='views-field-body'>Get the datacenters where object storage is available</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getBackboneDependents'> getBackboneDependents</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getDatacenters'> getDatacenters</a> </span>
            <div class='views-field-body'>Retrieve all datacenter locations</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getDatacentersWithVirtualImageStoreServiceResourceRecord'> getDatacentersWithVirtualImageStoreServiceResourceRecord</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getEuCompliantFlag'> getEuCompliantFlag</a> </span>
            <div class='views-field-body'>Retrieve a flag indicating whether or not the datacenter/location is EU compliant.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getGroups'> getGroups</a> </span>
            <div class='views-field-body'>Retrieve a location can be a member of 1 or more groups. This will show which groups to which a location belongs.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getHardwareFirewalls'> getHardwareFirewalls</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getLocationAddress'> getLocationAddress</a> </span>
            <div class='views-field-body'>Retrieve a location's physical address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getLocationAddresses'> getLocationAddresses</a> </span>
            <div class='views-field-body'>Retrieve a location's physical addresses.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getLocationReservationMember'> getLocationReservationMember</a> </span>
            <div class='views-field-body'>Retrieve a location's Dedicated Rack member</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getLocationStatus'> getLocationStatus</a> </span>
            <div class='views-field-body'>Retrieve the current locations status.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getNetworkConfigurationAttribute'> getNetworkConfigurationAttribute</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Location record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getOnlinePptpVpnUserCount'> getOnlinePptpVpnUserCount</a> </span>
            <div class='views-field-body'>Retrieve the total number of users online using SoftLayer's PPTP VPN service for a location.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getOnlineSslVpnUserCount'> getOnlineSslVpnUserCount</a> </span>
            <div class='views-field-body'>Retrieve the total number of users online using SoftLayer's SSL VPN service for a location.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getPathString'> getPathString</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getPriceGroups'> getPriceGroups</a> </span>
            <div class='views-field-body'>Retrieve a location can be a member of 1 or more Price Groups. This will show which groups to which a location belongs.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getRegions'> getRegions</a> </span>
            <div class='views-field-body'>Retrieve a location can be a member of 1 or more regions. This will show which regions to which a location belongs.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getTimezone'> getTimezone</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getVdrGroup'> getVdrGroup</a> </span>
            <div class='views-field-body'>Retrieve a location can be a member of 1 Bandwidth Pooling Group. This will show which group to which a location belongs.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getViewableDatacenters'> getViewableDatacenters</a> </span>
            <div class='views-field-body'>Retrieve all datacenter locations</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getViewablePopsAndDataCenters'> getViewablePopsAndDataCenters</a> </span>
            <div class='views-field-body'>Retrieve viewable pops and datacenters in a combined list.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getViewablepointOfPresence'> getViewablepointOfPresence</a> </span>
            <div class='views-field-body'>Retrieve viewable network locations</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Location/getpointOfPresence'> getpointOfPresence</a> </span>
            <div class='views-field-body'>Retrieve all points of presence locations</div>
        </div>
        </div>
</div>

