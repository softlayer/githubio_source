---
title: "SoftLayer_Location"
description: "Every piece of hardware and network connection owned by SoftLayer is tracked physically by location and stored in the So... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location"
---

# SoftLayer_Location
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Location' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Location' >Datatype</a></li>
    </ul>
</div>

## Description 
Every piece of hardware and network connection owned by SoftLayer is tracked physically by location and stored in the SoftLayer_Location data type. SoftLayer locations exist in parent/child relationships, a convenient way to track equipment from it's city, datacenter, server room, rack, then slot. Network backbones are tied to datacenters only, not to a room, rack, or slot. 


### associatedMethods

*  [SoftLayer_Hardware::getLocation](/reference/services/SoftLayer_Hardware/getLocation )
*  [SoftLayer_Hardware::getDatacenter](/reference/services/SoftLayer_Hardware/getDatacenter )
*  [SoftLayer_Network_Backbone::getLocation](/reference/services/SoftLayer_Network_Backbone/getLocation )





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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The unique identifier of a specific location. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#longName" name=longName>longName</a>
            </span>
            <div class='views-field-body'>A longer location description. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#name" name=name>name</a>
            </span>
            <div class='views-field-body'>A short location description. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#statusId" name=statusId>statusId</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#activePresaleEvents" name=activePresaleEvents>activePresaleEvents</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Sales_Presale_Event'>SoftLayer_Sales_Presale_Event[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#backboneDependents" name=backboneDependents>backboneDependents</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Backbone_Location_Dependent'>SoftLayer_Network_Backbone_Location_Dependent[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#euCompliantFlag" name=euCompliantFlag>euCompliantFlag</a>
            </span>
            <div class='views-field-body'>A flag indicating whether or not the datacenter/location is EU compliant. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#groups" name=groups>groups</a>
            </span>
            <div class='views-field-body'>A location can be a member of 1 or more groups. This will show which groups to which a location belongs. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Location_Group'>SoftLayer_Location_Group[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hardwareFirewalls" name=hardwareFirewalls>hardwareFirewalls</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#locationAddress" name=locationAddress>locationAddress</a>
            </span>
            <div class='views-field-body'>A location's physical address. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account_Address'>SoftLayer_Account_Address </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#locationAddresses" name=locationAddresses>locationAddresses</a>
            </span>
            <div class='views-field-body'>A location's physical addresses. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account_Address'>SoftLayer_Account_Address[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#locationReservationMember" name=locationReservationMember>locationReservationMember</a>
            </span>
            <div class='views-field-body'>A location's Dedicated Rack member </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Location_Reservation_Rack_Member'>SoftLayer_Location_Reservation_Rack_Member </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#locationStatus" name=locationStatus>locationStatus</a>
            </span>
            <div class='views-field-body'>The current locations status. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Location_Status'>SoftLayer_Location_Status </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#networkConfigurationAttribute" name=networkConfigurationAttribute>networkConfigurationAttribute</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Hardware_Attribute'>SoftLayer_Hardware_Attribute </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#onlinePptpVpnUserCount" name=onlinePptpVpnUserCount>onlinePptpVpnUserCount</a>
            </span>
            <div class='views-field-body'>The total number of users online using SoftLayer's PPTP VPN service for a location. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#onlineSslVpnUserCount" name=onlineSslVpnUserCount>onlineSslVpnUserCount</a>
            </span>
            <div class='views-field-body'>The total number of users online using SoftLayer's SSL VPN service for a location. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#pathString" name=pathString>pathString</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#priceGroups" name=priceGroups>priceGroups</a>
            </span>
            <div class='views-field-body'>A location can be a member of 1 or more Price Groups. This will show which groups to which a location belongs. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Location_Group'>SoftLayer_Location_Group[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#regions" name=regions>regions</a>
            </span>
            <div class='views-field-body'>A location can be a member of 1 or more regions. This will show which regions to which a location belongs. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Location_Region'>SoftLayer_Location_Region[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#timezone" name=timezone>timezone</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Locale_Timezone'>SoftLayer_Locale_Timezone </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#vdrGroup" name=vdrGroup>vdrGroup</a>
            </span>
            <div class='views-field-body'>A location can be a member of 1 Bandwidth Pooling Group. This will show which group to which a location belongs. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Location_Group_Location_CrossReference'>SoftLayer_Location_Group_Location_CrossReference </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#activePresaleEventCount" name=activePresaleEventCount>activePresaleEventCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#backboneDependentCount" name=backboneDependentCount>backboneDependentCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#groupCount" name=groupCount>groupCount</a>
            </span>
            <div class='views-field-body'>A count of a location can be a member of 1 or more groups. This will show which groups to which a location belongs. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hardwareFirewallCount" name=hardwareFirewallCount>hardwareFirewallCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#locationAddressCount" name=locationAddressCount>locationAddressCount</a>
            </span>
            <div class='views-field-body'>A count of a location's physical addresses. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#priceGroupCount" name=priceGroupCount>priceGroupCount</a>
            </span>
            <div class='views-field-body'>A count of a location can be a member of 1 or more Price Groups. This will show which groups to which a location belongs. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#regionCount" name=regionCount>regionCount</a>
            </span>
            <div class='views-field-body'>A count of a location can be a member of 1 or more regions. This will show which regions to which a location belongs. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


