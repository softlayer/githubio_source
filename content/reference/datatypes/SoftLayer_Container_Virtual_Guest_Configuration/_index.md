---
title: "SoftLayer_Container_Virtual_Guest_Configuration"
description: "The guest configuration container is used to provide configuration options for creating computing instances. 

Each conf... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Virtual_Guest_Configuration"
---

# SoftLayer_Container_Virtual_Guest_Configuration
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Virtual_Guest_Configuration' >Datatype</a></li>
    </ul>
</div>

## Description 
The guest configuration container is used to provide configuration options for creating computing instances. 

Each configuration option will include both an <code>itemPrice</code> and a <code>template</code>. 

The <code>itemPrice</code> value will provide hourly and monthly costs (if either are applicable), and a description of the option. 

The <code>template</code> will provide a fragment of the request with the properties and values that must be sent when creating a computing instance with the option. 

The [SoftLayer_Virtual_Guest::getCreateObjectOptions]({{<ref "reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions">}}) method returns this data structure. 

<style type="text/css">#properties .views-field-body p { margin-top: 1.5em; };</style> 


### associatedMethods

*  [SoftLayer_Virtual_Guest::getCreateObjectOptions](/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions )





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
[blockDevices]: #blockdevices
#### [blockDevices]

<div style="width: 200%"> 
Available block device options. 


A computing instance will have at least one block device represented by a <code>device</code> number of <code>'0'</code>. 


The <code>blockDevices.device</code> value in the template represents which device the option is for. 
The <code>blockDevices.diskImage.capacity</code> value in the template represents the size, in gigabytes, of the disk. 
The <code>localDiskFlag</code> value in the template represents whether the option is a local or SAN based disk. 


Note: The block device number <code>'1'</code> is reserved for the SWAP disk attached to the computing instance. 
</div>   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Virtual_Guest_Configuration_Option'>SoftLayer_Container_Virtual_Guest_Configuration_Option[] </a>**


</div>
<div class="prop-row">

-----
[datacenters]: #datacenters
#### [datacenters]

<div style="width: 200%"> 
Available datacenter options. 


The <code>datacenter.name</code> value in the template represents which datacenter the computing instance will be provisioned in. 
</div>   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Virtual_Guest_Configuration_Option'>SoftLayer_Container_Virtual_Guest_Configuration_Option[] </a>**


</div>
<div class="prop-row">

-----
[flavors]: #flavors
#### [flavors]

<div style="width: 200%"> 


Available flavor options. 


The <code>supplementalCreateObjectOptions.flavorKeyName</code> value in the template is an identifier for a particular core, ram, and primary disk configuration. 


When providing a <code>supplementalCreateObjectOptions.flavorKeyName</code> option the core, ram, and primary disk options are not needed. If those options are provided they are validated against the flavor. 
</div>   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Virtual_Guest_Configuration_Option'>SoftLayer_Container_Virtual_Guest_Configuration_Option[] </a>**


</div>
<div class="prop-row">

-----
[memory]: #memory
#### [memory]

<div style="width: 200%"> 
Available memory options. 


The <code>maxMemory</code> value in the template represents the amount of memory, in megabytes, allocated to the computing instance. 
</div>   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Virtual_Guest_Configuration_Option'>SoftLayer_Container_Virtual_Guest_Configuration_Option[] </a>**


</div>
<div class="prop-row">

-----
[networkComponents]: #networkcomponents
#### [networkComponents]

<div style="width: 200%"> 
Available network component options. 


The <code>networkComponent.maxSpeed</code> value in the template represents the link speed, in megabits per second, of the network connections for a computing instance. 
</div>   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Virtual_Guest_Configuration_Option'>SoftLayer_Container_Virtual_Guest_Configuration_Option[] </a>**


</div>
<div class="prop-row">

-----
[operatingSystems]: #operatingsystems
#### [operatingSystems]

<div style="width: 200%"> 
Available operating system options. 


The <code>operatingSystemReferenceCode</code> value in the template is an identifier for a particular operating system. When provided exactly as shown in the template, that operating system will be used. 


A reference code is structured as three tokens separated by underscores. The first token represents the product, the second is the version of the product, and the third is whether the OS is 32 or 64bit. 


When providing an <code>operatingSystemReferenceCode</code> while ordering a computing instance the only token required to match exactly is the product. The version token may be given as 'LATEST', else it will require an exact match as well. When the bits token is not provided, 64 bits will be assumed. 


Providing the value of 'LATEST' for a version will select the latest release of that product for the operating system. As this may change over time, you should be sure that the release version is irrelevant for your applications. 


For Windows based operating systems the version will represent both the release version (2008, 2012, etc) and the edition (Standard, Enterprise, etc). For all other operating systems the version will represent the major version (Centos 6, Ubuntu 12, etc) of that operating system, minor versions are not represented in a reference code. 


<b>Notice</b> - Some operating systems are charged based on the value specified in <code>startCpus</code>. The price which is used can be determined by calling [SoftLayer_Virtual_Guest::generateOrderTemplate]({{<ref "reference/services/SoftLayer_Virtual_Guest/generateOrderTemplate">}}) with your desired device specifications. 
</div>   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Virtual_Guest_Configuration_Option'>SoftLayer_Container_Virtual_Guest_Configuration_Option[] </a>**


</div>
<div class="prop-row">

-----
[processors]: #processors
#### [processors]

<div style="width: 200%"> 
Available processor options. 


The <code>startCpus</code> value in the template represents the number of cores allocated to the computing instance. 
The <code>dedicatedAccountHostOnlyFlag</code> value in the template represents whether the instance will run on hosts with instances belonging to other accounts. 
</div>   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Virtual_Guest_Configuration_Option'>SoftLayer_Container_Virtual_Guest_Configuration_Option[] </a>**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


