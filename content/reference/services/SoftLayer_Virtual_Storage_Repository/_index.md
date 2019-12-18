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
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [getAccount](/reference/services/SoftLayer_Virtual_Storage_Repository/getAccount)
Retrieve the [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) that a storage repository belongs to.

#### [getArchiveDiskUsageRatePerGb](/reference/services/SoftLayer_Virtual_Storage_Repository/getArchiveDiskUsageRatePerGb)
The rate that is charged for archiving every 1 gigabyte of data for a computing instance 

#### [getAverageDiskUsageMetricDataFromInfluxByDate](/reference/services/SoftLayer_Virtual_Storage_Repository/getAverageDiskUsageMetricDataFromInfluxByDate)
Returns the average disk usage for the timeframe based on the parameters provided. 

#### [getAverageUsageMetricDataByDate](/reference/services/SoftLayer_Virtual_Storage_Repository/getAverageUsageMetricDataByDate)
Returns the average disk usage for the timeframe based on the parameters provided. 

#### [getBillingItem](/reference/services/SoftLayer_Virtual_Storage_Repository/getBillingItem)
Retrieve the current billing item for a storage repository.

#### [getDatacenter](/reference/services/SoftLayer_Virtual_Storage_Repository/getDatacenter)
Retrieve the datacenter that a virtual storage repository resides in.

#### [getDiskImages](/reference/services/SoftLayer_Virtual_Storage_Repository/getDiskImages)
Retrieve the [SoftLayer_Virtual_Disk_Image]({{<ref "reference/datatypes/SoftLayer_Virtual_Disk_Image">}}) that are in a storage repository. Disk images are the virtual hard drives for a virtual guest.

#### [getGuests](/reference/services/SoftLayer_Virtual_Storage_Repository/getGuests)
Retrieve the computing instances that have disk images in a storage repository.

#### [getMetricTrackingObject](/reference/services/SoftLayer_Virtual_Storage_Repository/getMetricTrackingObject)


#### [getObject](/reference/services/SoftLayer_Virtual_Storage_Repository/getObject)
Retrieve a SoftLayer_Virtual_Storage_Repository record.

#### [getPublicImageBillingItem](/reference/services/SoftLayer_Virtual_Storage_Repository/getPublicImageBillingItem)
Retrieve the current billing item for a public storage repository.

#### [getPublicImageDiskUsageRatePerGb](/reference/services/SoftLayer_Virtual_Storage_Repository/getPublicImageDiskUsageRatePerGb)
The rate that is charged for publishing every 1 gigabyte of data for an image template 

#### [getStorageLocations](/reference/services/SoftLayer_Virtual_Storage_Repository/getStorageLocations)
The available locations for public image storage. 

#### [getType](/reference/services/SoftLayer_Virtual_Storage_Repository/getType)
Retrieve a storage repository's [SoftLayer_Virtual_Storage_Repository_Type]({{<ref "reference/datatypes/SoftLayer_Virtual_Storage_Repository_Type">}}).

#### [getUsageMetricDataByDate](/reference/services/SoftLayer_Virtual_Storage_Repository/getUsageMetricDataByDate)
Retrieve the metric data for disk space usage for a storage repository. 

#### [getUsageMetricImageByDate](/reference/services/SoftLayer_Virtual_Storage_Repository/getUsageMetricImageByDate)
Retrieve an image of the disk usage data on a [SoftLayer_Virtual_Guest]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest">}}) image for the time range you provide. 

</div>

