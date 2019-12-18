---
title: "SoftLayer_Location_Storage_Room"
description: "SoftLayer_Location_Storage_Room extends the [SoftLayer_Location]({{<ref 'reference/datatypes/SoftLayer_Location'>}}) dat... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Storage_Room"
---

# SoftLayer_Location_Storage_Room
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Location_Storage_Room' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Location_Storage_Room extends the [SoftLayer_Location]({{<ref "reference/datatypes/SoftLayer_Location">}}) data type to include storage room-specific properties. 



### seeAlso

* [SoftLayer_Location (type)](/reference/datatypes/SoftLayer_Location (type) )




<!-- Service Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Method Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Service Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
-----
[id]: #id
#### [id]
The unique identifier of a specific location.  
<span class="type-label">Type: </span>**integer**

-----
[longName]: #longname
#### [longName]
A longer location description.  
<span class="type-label">Type: </span>**string**

-----
[name]: #name
#### [name]
A short location description.  
<span class="type-label">Type: </span>**string**

-----
[statusId]: #statusid
#### [statusId]
  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[activePresaleEvents]: #activepresaleevents
#### [activePresaleEvents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Sales_Presale_Event'>SoftLayer_Sales_Presale_Event[] </a>**

-----
[backboneDependents]: #backbonedependents
#### [backboneDependents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Backbone_Location_Dependent'>SoftLayer_Network_Backbone_Location_Dependent[] </a>**

-----
[euCompliantFlag]: #eucompliantflag
#### [euCompliantFlag]
A flag indicating whether or not the datacenter/location is EU compliant.  
<span class="type-label">Type: </span>**boolean**

-----
[groups]: #groups
#### [groups]
A location can be a member of 1 or more groups. This will show which groups to which a location belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Group'>SoftLayer_Location_Group[] </a>**

-----
[hardwareFirewalls]: #hardwarefirewalls
#### [hardwareFirewalls]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[locationAddress]: #locationaddress
#### [locationAddress]
A location's physical address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Address'>SoftLayer_Account_Address </a>**

-----
[locationAddresses]: #locationaddresses
#### [locationAddresses]
A location's physical addresses.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Address'>SoftLayer_Account_Address[] </a>**

-----
[locationReservationMember]: #locationreservationmember
#### [locationReservationMember]
A location's Dedicated Rack member  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Reservation_Rack_Member'>SoftLayer_Location_Reservation_Rack_Member </a>**

-----
[locationStatus]: #locationstatus
#### [locationStatus]
The current locations status.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Status'>SoftLayer_Location_Status </a>**

-----
[networkConfigurationAttribute]: #networkconfigurationattribute
#### [networkConfigurationAttribute]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Attribute'>SoftLayer_Hardware_Attribute </a>**

-----
[onlinePptpVpnUserCount]: #onlinepptpvpnusercount
#### [onlinePptpVpnUserCount]
The total number of users online using SoftLayer's PPTP VPN service for a location.  
<span class="type-label">Type: </span>**integer**

-----
[onlineSslVpnUserCount]: #onlinesslvpnusercount
#### [onlineSslVpnUserCount]
The total number of users online using SoftLayer's SSL VPN service for a location.  
<span class="type-label">Type: </span>**integer**

-----
[pathString]: #pathstring
#### [pathString]
  
<span class="type-label">Type: </span>**string**

-----
[priceGroups]: #pricegroups
#### [priceGroups]
A location can be a member of 1 or more Price Groups. This will show which groups to which a location belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Group'>SoftLayer_Location_Group[] </a>**

-----
[regions]: #regions
#### [regions]
A location can be a member of 1 or more regions. This will show which regions to which a location belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Region'>SoftLayer_Location_Region[] </a>**

-----
[timezone]: #timezone
#### [timezone]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Locale_Timezone'>SoftLayer_Locale_Timezone </a>**

-----
[vdrGroup]: #vdrgroup
#### [vdrGroup]
A location can be a member of 1 Bandwidth Pooling Group. This will show which group to which a location belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Group_Location_CrossReference'>SoftLayer_Location_Group_Location_CrossReference </a>**


## Count

-----
[activePresaleEventCount]: #activepresaleeventcount
#### [activePresaleEventCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[backboneDependentCount]: #backbonedependentcount
#### [backboneDependentCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[groupCount]: #groupcount
#### [groupCount]
A count of a location can be a member of 1 or more groups. This will show which groups to which a location belongs.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hardwareFirewallCount]: #hardwarefirewallcount
#### [hardwareFirewallCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[locationAddressCount]: #locationaddresscount
#### [locationAddressCount]
A count of a location's physical addresses.   
<span class="type-label">Type: </span>**unsigned long**


-----
[priceGroupCount]: #pricegroupcount
#### [priceGroupCount]
A count of a location can be a member of 1 or more Price Groups. This will show which groups to which a location belongs.   
<span class="type-label">Type: </span>**unsigned long**


-----
[regionCount]: #regioncount
#### [regionCount]
A count of a location can be a member of 1 or more regions. This will show which regions to which a location belongs.   
<span class="type-label">Type: </span>**unsigned long**

</div>


