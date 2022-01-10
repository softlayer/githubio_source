---
title: "SoftLayer_Location_Server_Room"
description: "SoftLayer_Location_Server_Room extends the [SoftLayer_Location]({{<ref 'reference/datatypes/SoftLayer_Location'>}}) data... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Server_Room"
---

# SoftLayer_Location_Server_Room
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Location_Server_Room' >Datatype</a></li>
    </ul>
</div>

## Description 


SoftLayer_Location_Server_Room extends the [SoftLayer_Location]({{<ref "reference/datatypes/SoftLayer_Location">}}) data type to include server room-specific properties. 



### seeAlso

* [SoftLayer_Location (type)](/reference/datatypes/SoftLayer_Location (type) )




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
[id]: #id
#### [id]
The unique identifier of a specific location.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[longName]: #longname
#### [longName]
A longer location description.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A short location description.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[statusId]: #statusid
#### [statusId]
  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[activePresaleEvents]: #activepresaleevents
#### [activePresaleEvents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Sales_Presale_Event'>SoftLayer_Sales_Presale_Event[] </a>**  



</div>
<div class="prop-row">

-----
[backboneDependents]: #backbonedependents
#### [backboneDependents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Backbone_Location_Dependent'>SoftLayer_Network_Backbone_Location_Dependent[] </a>**  



</div>
<div class="prop-row">

-----
[bnppCompliantFlag]: #bnppcompliantflag
#### [bnppCompliantFlag]
A flag indicating whether or not the datacenter/location is BNPP compliant.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[euCompliantFlag]: #eucompliantflag
#### [euCompliantFlag]
A flag indicating whether or not the datacenter/location is EU compliant.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[groups]: #groups
#### [groups]
A location can be a member of 1 or more groups. This will show which groups to which a location belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Group'>SoftLayer_Location_Group[] </a>**  



</div>
<div class="prop-row">

-----
[hardwareFirewalls]: #hardwarefirewalls
#### [hardwareFirewalls]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**  



</div>
<div class="prop-row">

-----
[locationAddress]: #locationaddress
#### [locationAddress]
A location's physical address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Address'>SoftLayer_Account_Address </a>**  



</div>
<div class="prop-row">

-----
[locationAddresses]: #locationaddresses
#### [locationAddresses]
A location's physical addresses.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Address'>SoftLayer_Account_Address[] </a>**  



</div>
<div class="prop-row">

-----
[locationReservationMember]: #locationreservationmember
#### [locationReservationMember]
A location's Dedicated Rack member  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Reservation_Rack_Member'>SoftLayer_Location_Reservation_Rack_Member </a>**  



</div>
<div class="prop-row">

-----
[locationStatus]: #locationstatus
#### [locationStatus]
The current locations status.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Status'>SoftLayer_Location_Status </a>**  



</div>
<div class="prop-row">

-----
[networkConfigurationAttribute]: #networkconfigurationattribute
#### [networkConfigurationAttribute]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Attribute'>SoftLayer_Hardware_Attribute </a>**  



</div>
<div class="prop-row">

-----
[onlineSslVpnUserCount]: #onlinesslvpnusercount
#### [onlineSslVpnUserCount]
The total number of users online using SoftLayer's SSL VPN service for a location.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[pathString]: #pathstring
#### [pathString]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[priceGroups]: #pricegroups
#### [priceGroups]
A location can be a member of 1 or more Price Groups. This will show which groups to which a location belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Group'>SoftLayer_Location_Group[] </a>**  



</div>
<div class="prop-row">

-----
[regions]: #regions
#### [regions]
A location can be a member of 1 or more regions. This will show which regions to which a location belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Region'>SoftLayer_Location_Region[] </a>**  



</div>
<div class="prop-row">

-----
[timezone]: #timezone
#### [timezone]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Locale_Timezone'>SoftLayer_Locale_Timezone </a>**  



</div>
<div class="prop-row">

-----
[vdrGroup]: #vdrgroup
#### [vdrGroup]
A location can be a member of 1 Bandwidth Pooling Group. This will show which group to which a location belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Group_Location_CrossReference'>SoftLayer_Location_Group_Location_CrossReference </a>**  



</div>

## Count
<div class="prop-row">

-----
[activePresaleEventCount]: #activepresaleeventcount
#### [activePresaleEventCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[backboneDependentCount]: #backbonedependentcount
#### [backboneDependentCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[groupCount]: #groupcount
#### [groupCount]
A count of a location can be a member of 1 or more groups. This will show which groups to which a location belongs.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[hardwareFirewallCount]: #hardwarefirewallcount
#### [hardwareFirewallCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[locationAddressCount]: #locationaddresscount
#### [locationAddressCount]
A count of a location's physical addresses.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[priceGroupCount]: #pricegroupcount
#### [priceGroupCount]
A count of a location can be a member of 1 or more Price Groups. This will show which groups to which a location belongs.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[regionCount]: #regioncount
#### [regionCount]
A count of a location can be a member of 1 or more regions. This will show which regions to which a location belongs.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


