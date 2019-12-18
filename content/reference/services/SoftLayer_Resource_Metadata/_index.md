---
title: "SoftLayer_Resource_Metadata"
description: "The Resource Metadata service enables the user to obtain information regarding the resource from which the request origi... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Resource"
classes:
    - "SoftLayer_Resource_Metadata"
---
# SoftLayer_Resource_Metadata
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Resource_Metadata' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Resource_Metadata' >Datatype</a></li>
    </ul>
</div>

## Description
The Resource Metadata service enables the user to obtain information regarding the resource from which the request originates. Due to the requirement that the request originate from the backend network of the resource, no API key is necessary to perform the request. 

The primary use of this service is to allow self-discovery for newly provisioned resources, enabling further automated setup by the user. 



        
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

#### [getBackendMacAddresses](/reference/services/SoftLayer_Resource_Metadata/getBackendMacAddresses)
A list of backend MAC addresses

#### [getDatacenter](/reference/services/SoftLayer_Resource_Metadata/getDatacenter)
The name for the datacenter which the resource is in

#### [getDatacenterId](/reference/services/SoftLayer_Resource_Metadata/getDatacenterId)
The id for the datacenter which the resource is in

#### [getDomain](/reference/services/SoftLayer_Resource_Metadata/getDomain)
A resource's domain

#### [getFrontendMacAddresses](/reference/services/SoftLayer_Resource_Metadata/getFrontendMacAddresses)
A list of frontend MAC addresses

#### [getFullyQualifiedDomainName](/reference/services/SoftLayer_Resource_Metadata/getFullyQualifiedDomainName)
A resource's fully qualified domain name

#### [getGlobalIdentifier](/reference/services/SoftLayer_Resource_Metadata/getGlobalIdentifier)
A resource's globalIdentifier

#### [getHostname](/reference/services/SoftLayer_Resource_Metadata/getHostname)
A resource's hostname

#### [getId](/reference/services/SoftLayer_Resource_Metadata/getId)
A resource's id

#### [getPrimaryBackendIpAddress](/reference/services/SoftLayer_Resource_Metadata/getPrimaryBackendIpAddress)
The primary backend IP address for the resource

#### [getPrimaryIpAddress](/reference/services/SoftLayer_Resource_Metadata/getPrimaryIpAddress)
The primary IP address for the resource

#### [getProvisionState](/reference/services/SoftLayer_Resource_Metadata/getProvisionState)
Obtain the provision state for a resource

#### [getRouter](/reference/services/SoftLayer_Resource_Metadata/getRouter)
The router associated with a network component

#### [getServiceResource](/reference/services/SoftLayer_Resource_Metadata/getServiceResource)
Obtain a specific service resource associated with the resource

#### [getServiceResources](/reference/services/SoftLayer_Resource_Metadata/getServiceResources)
Obtain service resources associated with the resource

#### [getTags](/reference/services/SoftLayer_Resource_Metadata/getTags)
Obtain tags associated with the resource

#### [getUserMetadata](/reference/services/SoftLayer_Resource_Metadata/getUserMetadata)
Obtain user data associated with the resource

#### [getVlanIds](/reference/services/SoftLayer_Resource_Metadata/getVlanIds)
A list of VLAN ids for a network component

#### [getVlans](/reference/services/SoftLayer_Resource_Metadata/getVlans)
A list of VLAN numbers for a network component

</div>

