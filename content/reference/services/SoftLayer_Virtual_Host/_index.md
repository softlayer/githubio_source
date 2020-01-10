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

#### [getAccount](/reference/services/SoftLayer_Virtual_Host/getAccount)
Retrieve the account which a virtual host belongs to.
</div>

<div class="method-row">

#### [getBilledPerGuestFlag](/reference/services/SoftLayer_Virtual_Host/getBilledPerGuestFlag)
Retrieve boolean flag indicating whether this virtualization platform gets billed per guest rather than at a fixed rate.
</div>

<div class="method-row">

#### [getBilledPerMemoryUsageFlag](/reference/services/SoftLayer_Virtual_Host/getBilledPerMemoryUsageFlag)
Retrieve boolean flag indicating whether this virtualization platform gets billed per memory usage rather than at a fixed rate.
</div>

<div class="method-row">

#### [getGuests](/reference/services/SoftLayer_Virtual_Host/getGuests)
Retrieve the guests associated with a virtual host.
</div>

<div class="method-row">

#### [getHardware](/reference/services/SoftLayer_Virtual_Host/getHardware)
Retrieve the hardware record which a virtual host resides on.
</div>

<div class="method-row">

#### [getLiveGuestByUuid](/reference/services/SoftLayer_Virtual_Host/getLiveGuestByUuid)
Query a virtualization platform directly to retrieve details regarding a guest. 
</div>

<div class="method-row">

#### [getLiveGuestList](/reference/services/SoftLayer_Virtual_Host/getLiveGuestList)
Query a virtualization platform directly to retrieve a list of known guests. 
</div>

<div class="method-row">

#### [getLiveGuestRecentMetricData](/reference/services/SoftLayer_Virtual_Host/getLiveGuestRecentMetricData)
Query a virtualization platform directly to retrieve recent metric data for a guest. 
</div>

<div class="method-row">

#### [getMetricTrackingObject](/reference/services/SoftLayer_Virtual_Host/getMetricTrackingObject)
Retrieve the metric tracking object for this virtual host.
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Virtual_Host/getObject)
Retrieve a SoftLayer_Virtual_Host record.
</div>

<div class="method-row">

#### [getPciDevices](/reference/services/SoftLayer_Virtual_Host/getPciDevices)

</div>

<div class="method-row">

#### [pauseLiveGuest](/reference/services/SoftLayer_Virtual_Host/pauseLiveGuest)
Pause a guest.
</div>

<div class="method-row">

#### [powerCycleLiveGuest](/reference/services/SoftLayer_Virtual_Host/powerCycleLiveGuest)
Power cycle a guest.
</div>

<div class="method-row">

#### [powerOffLiveGuest](/reference/services/SoftLayer_Virtual_Host/powerOffLiveGuest)
Power off a guest.
</div>

<div class="method-row">

#### [powerOnLiveGuest](/reference/services/SoftLayer_Virtual_Host/powerOnLiveGuest)
Power on a guest.
</div>

<div class="method-row">

#### [rebootSoftLiveGuest](/reference/services/SoftLayer_Virtual_Host/rebootSoftLiveGuest)
Attempt to complete a soft reboot of a guest by shutting down the operating system.
</div>

<div class="method-row">

#### [resumeLiveGuest](/reference/services/SoftLayer_Virtual_Host/resumeLiveGuest)
Resume a guest.
</div>
</div>

</div>

