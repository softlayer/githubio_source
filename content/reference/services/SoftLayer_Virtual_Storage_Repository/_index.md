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
Storage Repositories are storage systems that are accessible through the internet and can be accessed through many types of devices, interfaces, and other resources such as NFS (Network File System).  They can contain 1 or more [[SoftLayer_Disk_Image|disk images]] and can be attached to more than one [[SoftLayer_Virtual_Host|host]]. 



        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Storage_Repository/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the [[SoftLayer_Account|account]] that a storage repository belongs to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Storage_Repository/getArchiveDiskUsageRatePerGb'> getArchiveDiskUsageRatePerGb</a> </span>
            <div class='views-field-body'>The rate that is charged for archiving every 1 gigabyte of data for a computing instance </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Storage_Repository/getAverageDiskUsageMetricDataFromInfluxByDate'> getAverageDiskUsageMetricDataFromInfluxByDate</a> </span>
            <div class='views-field-body'>Returns the average disk usage for the timeframe based on the parameters provided. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Storage_Repository/getAverageUsageMetricDataByDate'> getAverageUsageMetricDataByDate</a> </span>
            <div class='views-field-body'>Returns the average disk usage for the timeframe based on the parameters provided. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Storage_Repository/getBillingItem'> getBillingItem</a> </span>
            <div class='views-field-body'>Retrieve the current billing item for a storage repository.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Storage_Repository/getDatacenter'> getDatacenter</a> </span>
            <div class='views-field-body'>Retrieve the datacenter that a virtual storage repository resides in.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Storage_Repository/getDiskImages'> getDiskImages</a> </span>
            <div class='views-field-body'>Retrieve the [[SoftLayer_Virtual_Disk_Image|disk images]] that are in a storage repository. Disk images are the virtual hard drives for a virtual guest.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Storage_Repository/getGuests'> getGuests</a> </span>
            <div class='views-field-body'>Retrieve the computing instances that have disk images in a storage repository.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Storage_Repository/getMetricTrackingObject'> getMetricTrackingObject</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Storage_Repository/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Virtual_Storage_Repository record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Storage_Repository/getPublicImageBillingItem'> getPublicImageBillingItem</a> </span>
            <div class='views-field-body'>Retrieve the current billing item for a public storage repository.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Storage_Repository/getPublicImageDiskUsageRatePerGb'> getPublicImageDiskUsageRatePerGb</a> </span>
            <div class='views-field-body'>The rate that is charged for publishing every 1 gigabyte of data for an image template </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Storage_Repository/getStorageLocations'> getStorageLocations</a> </span>
            <div class='views-field-body'>The available locations for public image storage. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Storage_Repository/getType'> getType</a> </span>
            <div class='views-field-body'>Retrieve a storage repository's [[SoftLayer_Virtual_Storage_Repository_Type|type]].</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Storage_Repository/getUsageMetricDataByDate'> getUsageMetricDataByDate</a> </span>
            <div class='views-field-body'>Retrieve the metric data for disk space usage for a storage repository. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Storage_Repository/getUsageMetricImageByDate'> getUsageMetricImageByDate</a> </span>
            <div class='views-field-body'>Retrieve an image of the disk usage data on a [[SoftLayer_Virtual_Guest|Cloud Computing Instance]] image for the time range you provide. </div>
        </div>
        </div>
</div>

