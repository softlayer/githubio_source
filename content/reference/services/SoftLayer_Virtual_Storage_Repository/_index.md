---
title: "SoftLayer_Virtual_Storage_Repository"
description: "Storage Repositories are storage systems that are accessible through the internet and can be accessed through many types... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Storage_Repository"
---
# SoftLayer_Virtual_Storage_Repository
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Virtual_Storage_Repository' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Storage_Repository' >Datatype</a></li>
    </ul>
</div>

## Description
Storage Repositories are storage systems that are accessible through the internet and can be accessed through many types of devices, interfaces, and other resources such as NFS (Network File System).  They can contain 1 or more [SoftLayer_Virtual_Disk_Image]({{<ref "reference/datatypes/SoftLayer_Virtual_Disk_Image">}}) and can be attached to more than one [SoftLayer_Virtual_Host]({{<ref "reference/datatypes/SoftLayer_Virtual_Host">}}). 



        
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

#### [getAccount](/reference/services/SoftLayer_Virtual_Storage_Repository/getAccount)
Retrieve the [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) that a storage repository belongs to.
</div>

<div class="method-row">

#### [getArchiveDiskUsageRatePerGb](/reference/services/SoftLayer_Virtual_Storage_Repository/getArchiveDiskUsageRatePerGb)
The rate that is charged for archiving every 1 gigabyte of data for a computing instance 
</div>

<div class="method-row">

#### [getAverageDiskUsageMetricDataFromInfluxByDate](/reference/services/SoftLayer_Virtual_Storage_Repository/getAverageDiskUsageMetricDataFromInfluxByDate)
Returns the average disk usage for the timeframe based on the parameters provided. 
</div>

<div class="method-row">

#### [getAverageUsageMetricDataByDate](/reference/services/SoftLayer_Virtual_Storage_Repository/getAverageUsageMetricDataByDate)
Returns the average disk usage for the timeframe based on the parameters provided. 
</div>

<div class="method-row">

#### [getBillingItem](/reference/services/SoftLayer_Virtual_Storage_Repository/getBillingItem)
Retrieve the current billing item for a storage repository.
</div>

<div class="method-row">

#### [getDatacenter](/reference/services/SoftLayer_Virtual_Storage_Repository/getDatacenter)
Retrieve the datacenter that a virtual storage repository resides in.
</div>

<div class="method-row">

#### [getDiskImages](/reference/services/SoftLayer_Virtual_Storage_Repository/getDiskImages)
Retrieve the [SoftLayer_Virtual_Disk_Image]({{<ref "reference/datatypes/SoftLayer_Virtual_Disk_Image">}}) that are in a storage repository. Disk images are the virtual hard drives for a virtual guest.
</div>

<div class="method-row">

#### [getGuests](/reference/services/SoftLayer_Virtual_Storage_Repository/getGuests)
Retrieve the computing instances that have disk images in a storage repository.
</div>

<div class="method-row">

#### [getMetricTrackingObject](/reference/services/SoftLayer_Virtual_Storage_Repository/getMetricTrackingObject)

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Virtual_Storage_Repository/getObject)
Retrieve a SoftLayer_Virtual_Storage_Repository record.
</div>

<div class="method-row">

#### [getPublicImageBillingItem](/reference/services/SoftLayer_Virtual_Storage_Repository/getPublicImageBillingItem)
Retrieve the current billing item for a public storage repository.
</div>

<div class="method-row">

#### [getPublicImageDiskUsageRatePerGb](/reference/services/SoftLayer_Virtual_Storage_Repository/getPublicImageDiskUsageRatePerGb)
The rate that is charged for publishing every 1 gigabyte of data for an image template 
</div>

<div class="method-row">

#### [getStorageLocations](/reference/services/SoftLayer_Virtual_Storage_Repository/getStorageLocations)
The available locations for public image storage. 
</div>

<div class="method-row">

#### [getType](/reference/services/SoftLayer_Virtual_Storage_Repository/getType)
Retrieve a storage repository's [SoftLayer_Virtual_Storage_Repository_Type]({{<ref "reference/datatypes/SoftLayer_Virtual_Storage_Repository_Type">}}).
</div>

<div class="method-row">

#### [getUsageMetricDataByDate](/reference/services/SoftLayer_Virtual_Storage_Repository/getUsageMetricDataByDate)
Retrieve the metric data for disk space usage for a storage repository. 
</div>

<div class="method-row">

#### [getUsageMetricImageByDate](/reference/services/SoftLayer_Virtual_Storage_Repository/getUsageMetricImageByDate)
Retrieve an image of the disk usage data on a [SoftLayer_Virtual_Guest]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest">}}) image for the time range you provide. 
</div>
</div>

</div>

