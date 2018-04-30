---
title: "SoftLayer_Network_Subnet_Registration"
description: "Subnet registration objects are used to request and track registration of the subnet with the appropriate Regional Inter... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Registration"
---
# SoftLayer_Network_Subnet_Registration
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Subnet_Registration' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration' >Datatype</a></li>
    </ul>
</div>

## Description
Subnet registration objects are used to request and track registration of the subnet with the appropriate Regional Internet Registry (RIR). Subnet registration is executed automatically for RIRs that require registration upon assignment, but this registration can be modified at any time. 

Subnet Registration objects can be updated after they are created. This will result in the information being submitted to the RIR and the records on their end being refreshed. 



        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Registration/clearRegistration'> clearRegistration</a> </span>
            <div class='views-field-body'>Clear an existing registration</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Registration/createObject'> createObject</a> </span>
            <div class='views-field-body'>Create a new subnet registration object</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Registration/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit an existing registration object</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Registration/editRegistrationAttachedDetails'> editRegistrationAttachedDetails</a> </span>
            <div class='views-field-body'>Modify the link between a [[SoftLayer_Network_Subnet_Registration]] object and two [[SoftLayer_Account_Regional_Registry_Detail]] objects simultaneously. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Registration/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the account that this registration belongs to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Registration/getDetailReferences'> getDetailReferences</a> </span>
            <div class='views-field-body'>Retrieve the cross-reference records that tie the [[SoftLayer_Account_Regional_Registry_Detail]] objects to the registration object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Registration/getEvents'> getEvents</a> </span>
            <div class='views-field-body'>Retrieve the related registration events.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Registration/getNetworkDetail'> getNetworkDetail</a> </span>
            <div class='views-field-body'>Retrieve the "network" detail object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Registration/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_Subnet_Registration record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Registration/getPersonDetail'> getPersonDetail</a> </span>
            <div class='views-field-body'>Retrieve the "person" detail object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Registration/getRegionalInternetRegistry'> getRegionalInternetRegistry</a> </span>
            <div class='views-field-body'>Retrieve the related Regional Internet Registry.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Registration/getRegionalInternetRegistryHandle'> getRegionalInternetRegistryHandle</a> </span>
            <div class='views-field-body'>Retrieve the RIR handle that this registration object belongs to. This field may not be populated until the registration is complete.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Registration/getStatus'> getStatus</a> </span>
            <div class='views-field-body'>Retrieve the status of this registration.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Registration/getSubnet'> getSubnet</a> </span>
            <div class='views-field-body'>Retrieve the subnet that this registration pertains to.</div>
        </div>
        </div>
</div>

