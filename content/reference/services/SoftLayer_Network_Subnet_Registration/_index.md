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


Subnet registration objects are used to request and track registration of the subnet with the appropriate Regional Internet Registry (RIR). Registration for public subnets can be requested any time after assignment of the subnet. 

Subnet Registration objects can be updated any time after they are created. This will result in the information being submitted to the RIR and the records on their end being refreshed. 



        
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

#### [clearRegistration](/reference/services/SoftLayer_Network_Subnet_Registration/clearRegistration)
Clear an existing registration

</div>

<div class="method-row">

#### [createObject](/reference/services/SoftLayer_Network_Subnet_Registration/createObject)
Create a new subnet registration

</div>

<div class="method-row">

#### [createObjects](/reference/services/SoftLayer_Network_Subnet_Registration/createObjects)
Create registrations for multiple subnets

</div>

<div class="method-row">

#### [editObject](/reference/services/SoftLayer_Network_Subnet_Registration/editObject)
Edit an existing registration object

</div>

<div class="method-row">

#### [editRegistrationAttachedDetails](/reference/services/SoftLayer_Network_Subnet_Registration/editRegistrationAttachedDetails)
Modify the link between a [SoftLayer_Network_Subnet_Registration]({{<ref "reference/datatypes/SoftLayer_Network_Subnet_Registration">}}) object and two [SoftLayer_Account_Regional_Registry_Detail]({{<ref "reference/datatypes/SoftLayer_Account_Regional_Registry_Detail">}}) objects simultaneously. 

</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Network_Subnet_Registration/getAccount)
Retrieve the account that this registration belongs to.

</div>

<div class="method-row">

#### [getDetailReferences](/reference/services/SoftLayer_Network_Subnet_Registration/getDetailReferences)
Retrieve the cross-reference records that tie the [SoftLayer_Account_Regional_Registry_Detail]({{<ref "reference/datatypes/SoftLayer_Account_Regional_Registry_Detail">}}) objects to the registration object.

</div>

<div class="method-row">

#### [getEvents](/reference/services/SoftLayer_Network_Subnet_Registration/getEvents)
Retrieve the related registration events.

</div>

<div class="method-row">

#### [getNetworkDetail](/reference/services/SoftLayer_Network_Subnet_Registration/getNetworkDetail)
Retrieve the "network" detail object.

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_Subnet_Registration/getObject)
Retrieve a SoftLayer_Network_Subnet_Registration record.

</div>

<div class="method-row">

#### [getPersonDetail](/reference/services/SoftLayer_Network_Subnet_Registration/getPersonDetail)
Retrieve the "person" detail object.

</div>

<div class="method-row">

#### [getRegionalInternetRegistry](/reference/services/SoftLayer_Network_Subnet_Registration/getRegionalInternetRegistry)
Retrieve the related Regional Internet Registry.

</div>

<div class="method-row">

#### [getRegionalInternetRegistryHandle](/reference/services/SoftLayer_Network_Subnet_Registration/getRegionalInternetRegistryHandle)
Retrieve the RIR handle that this registration object belongs to. This field may not be populated until the registration is complete.

</div>

<div class="method-row">

#### [getStatus](/reference/services/SoftLayer_Network_Subnet_Registration/getStatus)
Retrieve the status of this registration.

</div>

<div class="method-row">

#### [getSubnet](/reference/services/SoftLayer_Network_Subnet_Registration/getSubnet)
Retrieve the subnet that this registration pertains to.

</div>
</div>

</div>

