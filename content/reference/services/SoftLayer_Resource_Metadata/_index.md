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
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [getAccountId](/reference/services/SoftLayer_Resource_Metadata/getAccountId)
The id for the account which the resource is in

</div>

<div class="method-row">

#### [getBackendMacAddresses](/reference/services/SoftLayer_Resource_Metadata/getBackendMacAddresses)
A list of backend MAC addresses

</div>

<div class="method-row">

#### [getDatacenter](/reference/services/SoftLayer_Resource_Metadata/getDatacenter)
The name for the datacenter which the resource is in

</div>

<div class="method-row">

#### [getDatacenterId](/reference/services/SoftLayer_Resource_Metadata/getDatacenterId)
The id for the datacenter which the resource is in

</div>

<div class="method-row">

#### [getDomain](/reference/services/SoftLayer_Resource_Metadata/getDomain)
A resource's domain

</div>

<div class="method-row">

#### [getFrontendMacAddresses](/reference/services/SoftLayer_Resource_Metadata/getFrontendMacAddresses)
A list of frontend MAC addresses

</div>

<div class="method-row">

#### [getFullyQualifiedDomainName](/reference/services/SoftLayer_Resource_Metadata/getFullyQualifiedDomainName)
A resource's fully qualified domain name

</div>

<div class="method-row">

#### [getGlobalIdentifier](/reference/services/SoftLayer_Resource_Metadata/getGlobalIdentifier)
A resource's globalIdentifier

</div>

<div class="method-row">

#### [getHostname](/reference/services/SoftLayer_Resource_Metadata/getHostname)
A resource's hostname

</div>

<div class="method-row">

#### [getId](/reference/services/SoftLayer_Resource_Metadata/getId)
A resource's id

</div>

<div class="method-row">

#### [getPrimaryBackendIpAddress](/reference/services/SoftLayer_Resource_Metadata/getPrimaryBackendIpAddress)
The primary backend IP address for the resource

</div>

<div class="method-row">

#### [getPrimaryIpAddress](/reference/services/SoftLayer_Resource_Metadata/getPrimaryIpAddress)
The primary IP address for the resource

</div>

<div class="method-row">

#### [getProvisionState](/reference/services/SoftLayer_Resource_Metadata/getProvisionState)
Obtain the provision state for a resource

</div>

<div class="method-row">

#### [getRouter](/reference/services/SoftLayer_Resource_Metadata/getRouter)
The router associated with a network component

</div>

<div class="method-row">

#### [getServiceResource](/reference/services/SoftLayer_Resource_Metadata/getServiceResource)
Obtain a specific service resource associated with the resource

</div>

<div class="method-row">

#### [getServiceResources](/reference/services/SoftLayer_Resource_Metadata/getServiceResources)
Obtain service resources associated with the resource

</div>

<div class="method-row">

#### [getTags](/reference/services/SoftLayer_Resource_Metadata/getTags)
Obtain tags associated with the resource

</div>

<div class="method-row">

#### [getUserMetadata](/reference/services/SoftLayer_Resource_Metadata/getUserMetadata)
Obtain user data associated with the resource

</div>

<div class="method-row">

#### [getVlanIds](/reference/services/SoftLayer_Resource_Metadata/getVlanIds)
A list of VLAN ids for a network component

</div>

<div class="method-row">

#### [getVlans](/reference/services/SoftLayer_Resource_Metadata/getVlans)
A list of VLAN numbers for a network component

</div>
</div>

</div>

