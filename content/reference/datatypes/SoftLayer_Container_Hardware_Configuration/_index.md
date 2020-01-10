---
title: "SoftLayer_Container_Hardware_Configuration"
description: "The hardware configuration container is used to provide configuration options for servers. 

Each configuration option w... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Hardware_Configuration"
---

# SoftLayer_Container_Hardware_Configuration
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Hardware_Configuration' >Datatype</a></li>
    </ul>
</div>

## Description 
The hardware configuration container is used to provide configuration options for servers. 

Each configuration option will include both an <code>itemPrice</code> and a <code>template</code>. 

The <code>itemPrice</code> value will provide hourly and monthly costs (if either are applicable), and a description of the option. 

The <code>template</code> will provide a fragment of the request with the properties and values that must be sent when creating a server with the option. 

The [SoftLayer_Hardware::getCreateObjectOptions]({{<ref "reference/services/SoftLayer_Hardware/getCreateObjectOptions">}}) method returns this data structure. 

<style type="text/css">#properties .views-field-body p { margin-top: 1.5em; };</style> 


### associatedMethods

*  [SoftLayer_Hardware::getCreateObjectOptions](/reference/services/SoftLayer_Hardware/getCreateObjectOptions )





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[datacenters]: #datacenters
#### [datacenters]

<div style="width: 200%"> 
Available datacenter options. 


The <code>datacenter.name</code> value in the template represents which datacenter the server will be provisioned in. 
</div>   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Hardware_Configuration_Option'>SoftLayer_Container_Hardware_Configuration_Option[] </a>**


</div>
<div class="prop-row">

-----
[fixedConfigurationPresets]: #fixedconfigurationpresets
#### [fixedConfigurationPresets]

<div style="width: 200%"> 
Available fixed configuration preset options. 


The <code>fixedConfigurationPreset.keyName</code> value in the template is an identifier for a particular fixed configuration. When provided exactly as shown in the template, that fixed configuration will be used. 


When providing a <code>fixedConfigurationPreset.keyName</code> while ordering a server the <code>processors</code> and <code>hardDrives</code> configuration options cannot be used. 
</div>   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Hardware_Configuration_Option'>SoftLayer_Container_Hardware_Configuration_Option[] </a>**


</div>
<div class="prop-row">

-----
[hardDrives]: #harddrives
#### [hardDrives]

<div style="width: 200%"> 
Available hard drive options. 


A server will have at least one hard drive. 


The <code>hardDrives.capacity</code> value in the template represents the size, in gigabytes, of the disk. 
</div>   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Hardware_Configuration_Option'>SoftLayer_Container_Hardware_Configuration_Option[] </a>**


</div>
<div class="prop-row">

-----
[networkComponents]: #networkcomponents
#### [networkComponents]

<div style="width: 200%"> 
Available network component options. 


The <code>networkComponent.maxSpeed</code> value in the template represents the link speed, in megabits per second, of the network connections for a server. 
</div>   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Hardware_Configuration_Option'>SoftLayer_Container_Hardware_Configuration_Option[] </a>**


</div>
<div class="prop-row">

-----
[operatingSystems]: #operatingsystems
#### [operatingSystems]

<div style="width: 200%"> 
Available operating system options. 


The <code>operatingSystemReferenceCode</code> value in the template is an identifier for a particular operating system. When provided exactly as shown in the template, that operating system will be used. 


A reference code is structured as three tokens separated by underscores. The first token represents the product, the second is the version of the product, and the third is whether the OS is 32 or 64bit. 


When providing an <code>operatingSystemReferenceCode</code> while ordering a server the only token required to match exactly is the product. The version token may be given as 'LATEST', else it will require an exact match as well. When the bits token is not provided, 64 bits will be assumed. 


Providing the value of 'LATEST' for a version will select the latest release of that product for the operating system. As this may change over time, you should be sure that the release version is irrelevant for your applications. 


For Windows based operating systems the version will represent both the release version (2008, 2012, etc) and the edition (Standard, Enterprise, etc). For all other operating systems the version will represent the major version (Centos 6, Ubuntu 12, etc) of that operating system, minor versions are represented in few reference codes where they are significant. 
</div>   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Hardware_Configuration_Option'>SoftLayer_Container_Hardware_Configuration_Option[] </a>**


</div>
<div class="prop-row">

-----
[processors]: #processors
#### [processors]

<div style="width: 200%"> 
Available processor options. 


The <code>processorCoreAmount</code> value in the template represents the number of cores allocated to the server. 
The <code>memoryCapacity</code> value in the template represents the amount of memory, in gigabytes, allocated to the server. 
</div>   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Hardware_Configuration_Option'>SoftLayer_Container_Hardware_Configuration_Option[] </a>**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


