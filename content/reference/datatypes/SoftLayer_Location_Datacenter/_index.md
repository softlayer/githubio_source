---
title: "SoftLayer_Location_Datacenter"
description: "SoftLayer_Location_Datacenter extends the [SoftLayer_Location]({{<ref 'reference/datatypes/SoftLayer_Location'>}}) data... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Datacenter"
---

# SoftLayer_Location_Datacenter
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Location_Datacenter' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Location_Datacenter' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Location_Datacenter extends the [SoftLayer_Location]({{<ref "reference/datatypes/SoftLayer_Location">}}) data type to include datacenter-specific properties. 


### associatedMethods

*  [SoftLayer_Hardware::getDatacenter](/reference/services/SoftLayer_Hardware/getDatacenter )
*  [SoftLayer_Location::getDatacenters](/reference/services/SoftLayer_Location/getDatacenters )



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
[activeItemPresaleEvents]: #activeitempresaleevents
#### [activeItemPresaleEvents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Sales_Presale_Event'>SoftLayer_Sales_Presale_Event[] </a>**

-----
[activePresaleEvents]: #activepresaleevents
#### [activePresaleEvents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Sales_Presale_Event'>SoftLayer_Sales_Presale_Event[] </a>**

-----
[backboneDependents]: #backbonedependents
#### [backboneDependents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Backbone_Location_Dependent'>SoftLayer_Network_Backbone_Location_Dependent[] </a>**

-----
[backendHardwareRouters]: #backendhardwarerouters
#### [backendHardwareRouters]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[boundSubnets]: #boundsubnets
#### [boundSubnets]
Subnets which are directly bound to one or more routers in a given datacenter, and currently allow routing.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**

-----
[brandCountryRestrictions]: #brandcountryrestrictions
#### [brandCountryRestrictions]
This references relationship between brands, locations and countries associated with a user's account that are ineligible when ordering products. For example, the India datacenter may not be available on this brand for customers that live in Great Britain.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand_Restriction_Location_CustomerCountry'>SoftLayer_Brand_Restriction_Location_CustomerCountry[] </a>**

-----
[euCompliantFlag]: #eucompliantflag
#### [euCompliantFlag]
A flag indicating whether or not the datacenter/location is EU compliant.  
<span class="type-label">Type: </span>**boolean**

-----
[frontendHardwareRouters]: #frontendhardwarerouters
#### [frontendHardwareRouters]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

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
[hardwareRouters]: #hardwarerouters
#### [hardwareRouters]
  
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
[presaleEvents]: #presaleevents
#### [presaleEvents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Sales_Presale_Event'>SoftLayer_Sales_Presale_Event[] </a>**

-----
[priceGroups]: #pricegroups
#### [priceGroups]
A location can be a member of 1 or more Price Groups. This will show which groups to which a location belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Group'>SoftLayer_Location_Group[] </a>**

-----
[regionalGroup]: #regionalgroup
#### [regionalGroup]
The regional group this datacenter belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Group_Regional'>SoftLayer_Location_Group_Regional </a>**

-----
[regionalInternetRegistry]: #regionalinternetregistry
#### [regionalInternetRegistry]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Regional_Internet_Registry'>SoftLayer_Network_Regional_Internet_Registry </a>**

-----
[regions]: #regions
#### [regions]
A location can be a member of 1 or more regions. This will show which regions to which a location belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Region'>SoftLayer_Location_Region[] </a>**

-----
[routableBoundSubnets]: #routableboundsubnets
#### [routableBoundSubnets]
Retrieve all subnets that are eligible to be routed; those which the account has permission to associate with a vlan.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**

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
[activeItemPresaleEventCount]: #activeitempresaleeventcount
#### [activeItemPresaleEventCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


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
[backendHardwareRouterCount]: #backendhardwareroutercount
#### [backendHardwareRouterCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[boundSubnetCount]: #boundsubnetcount
#### [boundSubnetCount]
A count of subnets which are directly bound to one or more routers in a given datacenter, and currently allow routing.   
<span class="type-label">Type: </span>**unsigned long**


-----
[brandCountryRestrictionCount]: #brandcountryrestrictioncount
#### [brandCountryRestrictionCount]
A count of this references relationship between brands, locations and countries associated with a user's account that are ineligible when ordering products. For example, the India datacenter may not be available on this brand for customers that live in Great Britain.   
<span class="type-label">Type: </span>**unsigned long**


-----
[frontendHardwareRouterCount]: #frontendhardwareroutercount
#### [frontendHardwareRouterCount]
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
[hardwareRouterCount]: #hardwareroutercount
#### [hardwareRouterCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[locationAddressCount]: #locationaddresscount
#### [locationAddressCount]
A count of a location's physical addresses.   
<span class="type-label">Type: </span>**unsigned long**


-----
[presaleEventCount]: #presaleeventcount
#### [presaleEventCount]
A count of    
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


-----
[routableBoundSubnetCount]: #routableboundsubnetcount
#### [routableBoundSubnetCount]
A count of retrieve all subnets that are eligible to be routed; those which the account has permission to associate with a vlan.   
<span class="type-label">Type: </span>**unsigned long**

</div>


