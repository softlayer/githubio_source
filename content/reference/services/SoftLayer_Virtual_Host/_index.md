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
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [getAccount](/reference/services/SoftLayer_Virtual_Host/getAccount)
Retrieve the account which a virtual host belongs to.

#### [getBilledPerGuestFlag](/reference/services/SoftLayer_Virtual_Host/getBilledPerGuestFlag)
Retrieve boolean flag indicating whether this virtualization platform gets billed per guest rather than at a fixed rate.

#### [getBilledPerMemoryUsageFlag](/reference/services/SoftLayer_Virtual_Host/getBilledPerMemoryUsageFlag)
Retrieve boolean flag indicating whether this virtualization platform gets billed per memory usage rather than at a fixed rate.

#### [getGuests](/reference/services/SoftLayer_Virtual_Host/getGuests)
Retrieve the guests associated with a virtual host.

#### [getHardware](/reference/services/SoftLayer_Virtual_Host/getHardware)
Retrieve the hardware record which a virtual host resides on.

#### [getLiveGuestByUuid](/reference/services/SoftLayer_Virtual_Host/getLiveGuestByUuid)
Query a virtualization platform directly to retrieve details regarding a guest. 

#### [getLiveGuestList](/reference/services/SoftLayer_Virtual_Host/getLiveGuestList)
Query a virtualization platform directly to retrieve a list of known guests. 

#### [getLiveGuestRecentMetricData](/reference/services/SoftLayer_Virtual_Host/getLiveGuestRecentMetricData)
Query a virtualization platform directly to retrieve recent metric data for a guest. 

#### [getMetricTrackingObject](/reference/services/SoftLayer_Virtual_Host/getMetricTrackingObject)
Retrieve the metric tracking object for this virtual host.

#### [getObject](/reference/services/SoftLayer_Virtual_Host/getObject)
Retrieve a SoftLayer_Virtual_Host record.

#### [getPciDevices](/reference/services/SoftLayer_Virtual_Host/getPciDevices)


#### [pauseLiveGuest](/reference/services/SoftLayer_Virtual_Host/pauseLiveGuest)
Pause a guest.

#### [powerCycleLiveGuest](/reference/services/SoftLayer_Virtual_Host/powerCycleLiveGuest)
Power cycle a guest.

#### [powerOffLiveGuest](/reference/services/SoftLayer_Virtual_Host/powerOffLiveGuest)
Power off a guest.

#### [powerOnLiveGuest](/reference/services/SoftLayer_Virtual_Host/powerOnLiveGuest)
Power on a guest.

#### [rebootSoftLiveGuest](/reference/services/SoftLayer_Virtual_Host/rebootSoftLiveGuest)
Attempt to complete a soft reboot of a guest by shutting down the operating system.

#### [resumeLiveGuest](/reference/services/SoftLayer_Virtual_Host/resumeLiveGuest)
Resume a guest.

</div>

