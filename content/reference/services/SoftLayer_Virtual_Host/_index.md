---
title: "SoftLayer_Virtual_Host"
description: "The virtual host service provides a common interface to any virtualization platform supported by SoftLayer. Interaction... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Host"
---
# SoftLayer_Virtual_Host
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Virtual_Host' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Host' >Datatype</a></li>
    </ul>
</div>

## Description
The virtual host service provides a common interface to any virtualization platform supported by SoftLayer. Interaction with various third party APIs is not needed when implementing this service to administer your hosts. 



        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Host/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the account which a virtual host belongs to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Host/getBilledPerGuestFlag'> getBilledPerGuestFlag</a> </span>
            <div class='views-field-body'>Retrieve boolean flag indicating whether this virtualization platform gets billed per guest rather than at a fixed rate.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Host/getBilledPerMemoryUsageFlag'> getBilledPerMemoryUsageFlag</a> </span>
            <div class='views-field-body'>Retrieve boolean flag indicating whether this virtualization platform gets billed per memory usage rather than at a fixed rate.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Host/getGuests'> getGuests</a> </span>
            <div class='views-field-body'>Retrieve the guests associated with a virtual host.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Host/getHardware'> getHardware</a> </span>
            <div class='views-field-body'>Retrieve the hardware record which a virtual host resides on.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Host/getLiveGuestByUuid'> getLiveGuestByUuid</a> </span>
            <div class='views-field-body'>Query a virtualization platform directly to retrieve details regarding a guest. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Host/getLiveGuestList'> getLiveGuestList</a> </span>
            <div class='views-field-body'>Query a virtualization platform directly to retrieve a list of known guests. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Host/getLiveGuestRecentMetricData'> getLiveGuestRecentMetricData</a> </span>
            <div class='views-field-body'>Query a virtualization platform directly to retrieve recent metric data for a guest. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Host/getMetricTrackingObject'> getMetricTrackingObject</a> </span>
            <div class='views-field-body'>Retrieve the metric tracking object for this virtual host.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Host/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Virtual_Host record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Host/pauseLiveGuest'> pauseLiveGuest</a> </span>
            <div class='views-field-body'>Pause a guest.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Host/powerCycleLiveGuest'> powerCycleLiveGuest</a> </span>
            <div class='views-field-body'>Power cycle a guest.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Host/powerOffLiveGuest'> powerOffLiveGuest</a> </span>
            <div class='views-field-body'>Power off a guest.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Host/powerOnLiveGuest'> powerOnLiveGuest</a> </span>
            <div class='views-field-body'>Power on a guest.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Host/rebootSoftLiveGuest'> rebootSoftLiveGuest</a> </span>
            <div class='views-field-body'>Attempt to complete a soft reboot of a guest by shutting down the operating system.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Host/resumeLiveGuest'> resumeLiveGuest</a> </span>
            <div class='views-field-body'>Resume a guest.</div>
        </div>
        </div>
</div>

