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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Resource_Metadata/getBackendMacAddresses'> getBackendMacAddresses</a> </span>
            <div class='views-field-body'>A list of backend MAC addresses</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Resource_Metadata/getDatacenter'> getDatacenter</a> </span>
            <div class='views-field-body'>The name for the datacenter which the resource is in</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Resource_Metadata/getDatacenterId'> getDatacenterId</a> </span>
            <div class='views-field-body'>The id for the datacenter which the resource is in</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Resource_Metadata/getDomain'> getDomain</a> </span>
            <div class='views-field-body'>A resource's domain</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Resource_Metadata/getFrontendMacAddresses'> getFrontendMacAddresses</a> </span>
            <div class='views-field-body'>A list of frontend MAC addresses</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Resource_Metadata/getFullyQualifiedDomainName'> getFullyQualifiedDomainName</a> </span>
            <div class='views-field-body'>A resource's fully qualified domain name</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Resource_Metadata/getGlobalIdentifier'> getGlobalIdentifier</a> </span>
            <div class='views-field-body'>A resource's globalIdentifier</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Resource_Metadata/getHostname'> getHostname</a> </span>
            <div class='views-field-body'>A resource's hostname</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Resource_Metadata/getId'> getId</a> </span>
            <div class='views-field-body'>A resource's id</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Resource_Metadata/getPrimaryBackendIpAddress'> getPrimaryBackendIpAddress</a> </span>
            <div class='views-field-body'>The primary backend IP address for the resource</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Resource_Metadata/getPrimaryIpAddress'> getPrimaryIpAddress</a> </span>
            <div class='views-field-body'>The primary IP address for the resource</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Resource_Metadata/getProvisionState'> getProvisionState</a> </span>
            <div class='views-field-body'>Obtain the provision state for a resource</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Resource_Metadata/getRouter'> getRouter</a> </span>
            <div class='views-field-body'>The router associated with a network component</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Resource_Metadata/getServiceResource'> getServiceResource</a> </span>
            <div class='views-field-body'>Obtain a specific service resource associated with the resource</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Resource_Metadata/getServiceResources'> getServiceResources</a> </span>
            <div class='views-field-body'>Obtain service resources associated with the resource</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Resource_Metadata/getTags'> getTags</a> </span>
            <div class='views-field-body'>Obtain tags associated with the resource</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Resource_Metadata/getUserMetadata'> getUserMetadata</a> </span>
            <div class='views-field-body'>Obtain user data associated with the resource</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Resource_Metadata/getVlanIds'> getVlanIds</a> </span>
            <div class='views-field-body'>A list of VLAN ids for a network component</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Resource_Metadata/getVlans'> getVlans</a> </span>
            <div class='views-field-body'>A list of VLAN numbers for a network component</div>
        </div>
        </div>
</div>

