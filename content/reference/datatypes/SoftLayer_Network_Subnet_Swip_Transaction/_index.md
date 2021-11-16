---
title: "SoftLayer_Network_Subnet_Swip_Transaction"
description: "**DEPRECATED**
The SoftLayer_Network_Subnet_Swip_Transaction data type contains basic information tracked at SoftLayer t... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Swip_Transaction"
---

# SoftLayer_Network_Subnet_Swip_Transaction
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Subnet_Swip_Transaction' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Subnet_Swip_Transaction' >Datatype</a></li>
    </ul>
</div>

## Description 

<div class="deprecated"><span class="deprecation-label">Deprecated  </span></div>


**DEPRECATED**
The SoftLayer_Network_Subnet_Swip_Transaction data type contains basic information tracked at SoftLayer to allow automation of Swip creation, update, and removal requests.  A specific transaction is attached to an accountId and a subnetId. This also contains a "Status Name" which tells the customer what the transaction is doing: 


* REQUEST QUEUED:  Request is queued up to be sent to ARIN
* REQUEST SENT:  The email request has been sent to ARIN
* REQUEST CONFIRMED:  ARIN has confirmed that the request is good, and should be available in 24 hours
* OK:  The subnet has been checked with WHOIS and it the SWIP transaction has completed correctly
* REMOVE QUEUED:  A subnet is queued to be removed from ARIN's systems
* REMOVE SENT:  The removal email request has been sent to ARIN
* REMOVE CONFIRMED:  ARIN has confirmed that the removal request is good, and the subnet should be clear in WHOIS in 24 hours
* DELETED:  This specific SWIP Transaction has been removed from ARIN and is no longer in effect
* SOFTLAYER MANUALLY PROCESSING:  Sometimes a request doesn't go through correctly and has to be manually processed by SoftLayer.  This may take some time.

### External Links


* [Shared Whois Project at Wikipedia](http://en.wikipedia.org/wiki/Shared_Whois_Project)




### seeAlso

* [SoftLayer_Network_Subnet_Rwhois_Data](/reference/services/SoftLayer_Network_Subnet_Rwhois_Data )




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
A SWIP transaction's unique identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[statusName]: #statusname
#### [statusName]
A Name describing which state a SWIP  transaction is in.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[subnetId]: #subnetid
#### [subnetId]
ID Number of the Subnet for this SWIP transaction.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The Account whose RWHOIS data was used to SWIP this subnet  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[subnet]: #subnet
#### [subnet]
The subnet that this SWIP transaction was created for.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a>**  



</div>

## Count
</div>


