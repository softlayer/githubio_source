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
[accountId]: #accountid
#### [accountId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[bgpAsn]: #bgpasn
#### [bgpAsn]
Specifies ASN used for BGP.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[errorMessage]: #errormessage
#### [errorMessage]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[globalRoutingFlag]: #globalroutingflag
#### [globalRoutingFlag]
The Direct Link connectivity to all SoftLayer data centers if globalRoutingFlag = 1 and local connectivity if globalRoutingFlag = 0.   
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[interconnectType]: #interconnecttype
#### [interconnectType]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[linkSpeed]: #linkspeed
#### [linkSpeed]
Link speed of a Direct Link connection.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[localIpAddress]: #localipaddress
#### [localIpAddress]
IP address (v4 or v6) of "near" router serial interface. No check/update of IP Address table.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[location]: #location
#### [location]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
Specifies the Interconnect connection name.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[newGlobalRoutingFlag]: #newglobalroutingflag
#### [newGlobalRoutingFlag]
Direct Link provider can request change to existing routing, Customer can approve the change. newGlobalRoutingFlag = 1 gives connectivity to all IBM data centers, and if newGlobalRoutingFlag = 0, it gives local connectivity.   
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[newLinkSpeed]: #newlinkspeed
#### [newLinkSpeed]
Updated Link speed of a Direct Link connection.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[note]: #note
#### [note]
This field will have the ticket id if the tenant workflow fails   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[peerLinkSpeed]: #peerlinkspeed
#### [peerLinkSpeed]
Link speed of a Direct Link connection on Equinix Side.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[port]: #port
#### [port]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[provider]: #provider
#### [provider]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[providerAccountId]: #provideraccountid
#### [providerAccountId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[redundancyFlag]: #redundancyflag
#### [redundancyFlag]
Specifies redundant connection is available if 1.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[remoteIpAddress]: #remoteipaddress
#### [remoteIpAddress]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[serviceKey]: #servicekey
#### [serviceKey]
Service key for Interconnect connection.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[serviceTypeId]: #servicetypeid
#### [serviceTypeId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
The direct link connection status. IN_PROGRESS, PROVISIONING, CONNECTION_UP, CONNECTION_DOWN   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[vlanId]: #vlanid
#### [vlanId]
  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
The active billing item for a network interconnect.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Network_Interconnect'>SoftLayer_Billing_Item_Network_Interconnect </a>**  



</div>
<div class="prop-row">

-----
[datacenterName]: #datacentername
#### [datacenterName]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[portLabel]: #portlabel
#### [portLabel]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[serviceType]: #servicetype
#### [serviceType]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_DirectLink_ServiceType'>SoftLayer_Network_DirectLink_ServiceType </a>**  



</div>
<div class="prop-row">

-----
[vendorName]: #vendorname
#### [vendorName]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[zoneName]: #zonename
#### [zoneName]
  
<span class="type-label">Type: </span>**string**  



</div>

## Count
</div>


