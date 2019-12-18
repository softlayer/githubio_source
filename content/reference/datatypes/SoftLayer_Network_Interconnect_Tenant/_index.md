---
title: "SoftLayer_Network_Interconnect_Tenant"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Interconnect_Tenant"
---

# SoftLayer_Network_Interconnect_Tenant
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Interconnect_Tenant' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Interconnect_Tenant' >Datatype</a></li>
    </ul>
</div>

## Description 






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
[accountId]: #accountid
#### [accountId]
  
<span class="type-label">Type: </span>**integer**

-----
[bgpAsn]: #bgpasn
#### [bgpAsn]
Specifies ASN used for BGP.  
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[errorMessage]: #errormessage
#### [errorMessage]
  
<span class="type-label">Type: </span>**string**

-----
[globalRoutingFlag]: #globalroutingflag
#### [globalRoutingFlag]
The Direct Link connectivity to all SoftLayer data centers if globalRoutingFlag = 1 and local connectivity if globalRoutingFlag = 0.   
<span class="type-label">Type: </span>**boolean**

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**

-----
[interconnectType]: #interconnecttype
#### [interconnectType]
  
<span class="type-label">Type: </span>**string**

-----
[linkSpeed]: #linkspeed
#### [linkSpeed]
Link speed of a Direct Link connection.  
<span class="type-label">Type: </span>**integer**

-----
[localIpAddress]: #localipaddress
#### [localIpAddress]
IP address (v4 or v6) of "near" router serial interface. No check/update of IP Address table.   
<span class="type-label">Type: </span>**string**

-----
[location]: #location
#### [location]
  
<span class="type-label">Type: </span>**string**

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
Specifies the Interconnect connection name.  
<span class="type-label">Type: </span>**string**

-----
[newLinkSpeed]: #newlinkspeed
#### [newLinkSpeed]
Updated Link speed of a Direct Link connection.  
<span class="type-label">Type: </span>**integer**

-----
[note]: #note
#### [note]
This field will have the ticket id if the tenant workflow fails   
<span class="type-label">Type: </span>**string**

-----
[peerLinkSpeed]: #peerlinkspeed
#### [peerLinkSpeed]
Link speed of a Direct Link connection on Equinix Side.  
<span class="type-label">Type: </span>**integer**

-----
[port]: #port
#### [port]
  
<span class="type-label">Type: </span>**string**

-----
[provider]: #provider
#### [provider]
  
<span class="type-label">Type: </span>**string**

-----
[providerAccountId]: #provideraccountid
#### [providerAccountId]
  
<span class="type-label">Type: </span>**integer**

-----
[redundancyFlag]: #redundancyflag
#### [redundancyFlag]
Specifies redundant connection is available if 1.  
<span class="type-label">Type: </span>**boolean**

-----
[remoteIpAddress]: #remoteipaddress
#### [remoteIpAddress]
  
<span class="type-label">Type: </span>**string**

-----
[serviceKey]: #servicekey
#### [serviceKey]
Service key for Interconnect connection.  
<span class="type-label">Type: </span>**string**

-----
[serviceTypeId]: #servicetypeid
#### [serviceTypeId]
  
<span class="type-label">Type: </span>**integer**

-----
[status]: #status
#### [status]
The direct link connection status. IN_PROGRESS, PROVISIONING, CONNECTION_UP, CONNECTION_DOWN   
<span class="type-label">Type: </span>**string**

-----
[vlanId]: #vlanid
#### [vlanId]
  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[billingItem]: #billingitem
#### [billingItem]
The active billing item for a network interconnect.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Network_Interconnect'>SoftLayer_Billing_Item_Network_Interconnect </a>**

-----
[datacenterName]: #datacentername
#### [datacenterName]
  
<span class="type-label">Type: </span>**string**

-----
[portLabel]: #portlabel
#### [portLabel]
  
<span class="type-label">Type: </span>**string**

-----
[serviceType]: #servicetype
#### [serviceType]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_DirectLink_ServiceType'>SoftLayer_Network_DirectLink_ServiceType </a>**

-----
[vendorName]: #vendorname
#### [vendorName]
  
<span class="type-label">Type: </span>**string**

-----
[zoneName]: #zonename
#### [zoneName]
  
<span class="type-label">Type: </span>**string**


## Count
</div>


