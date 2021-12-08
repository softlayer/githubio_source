---
title: "SoftLayer_Network_Subnet_Swip_Transaction"
description: "**DEPRECATED**
SoftLayer's Automated Swip System is a finite state machine; it works by locally tracking a transaction b... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
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
SoftLayer's Automated Swip System is a finite state machine; it works by locally tracking a transaction between SoftLayer and the relevant Regional Internet Registry (RIR), assigning responsibility of a subnet to a customer. Transactions are dictated by the RIR's processing system, and the nature of the communication medium with each RIR, namely their REST API. 

Using this API, SoftLayer Customers are able to initiate, monitor, update, and remove Swip system transactions with ARIN and RIPE. 

### External Links


* [Shared Whois Project at Wikipedia](http://en.wikipedia.org/wiki/Shared_Whois_Project)




### seeAlso

* [SoftLayer_Network_Subnet_Rwhois_Data](/reference/services/SoftLayer_Network_Subnet_Rwhois_Data )


        
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

<div class="method-row deprecated">

#### [findMyTransactions](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/findMyTransactions)
returns SWIP transaction objects that are currently in transaction with ARIN.

<span class="deprecation-label">Deprecated  </span>


</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/getAccount)
Retrieve the Account whose RWHOIS data was used to SWIP this subnet

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/getObject)
Retrieve a SoftLayer_Network_Subnet_Swip_Transaction record.

</div>

<div class="method-row">

#### [getSubnet](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/getSubnet)
Retrieve the subnet that this SWIP transaction was created for.

</div>

<div class="method-row deprecated">

#### [removeAllSubnetSwips](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/removeAllSubnetSwips)
Removes registration information from ARIN for all your subnets

<span class="deprecation-label">Deprecated  </span>


</div>

<div class="method-row deprecated">

#### [removeSwipData](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/removeSwipData)
Deletes registration information from ARIN for a single subnet

<span class="deprecation-label">Deprecated  </span>


</div>

<div class="method-row deprecated">

#### [resendSwipData](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/resendSwipData)
Sends updated RWHOIS information to ARIN for a single subnet.

<span class="deprecation-label">Deprecated  </span>


</div>

<div class="method-row deprecated">

#### [swipAllSubnets](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/swipAllSubnets)
create SWIP transactions for all subnets that do not already have a SWIP transaction in progress.

<span class="deprecation-label">Deprecated  </span>


</div>

<div class="method-row deprecated">

#### [updateAllSubnetSwips](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/updateAllSubnetSwips)
Update all subnets on the account with an "OK" status.

<span class="deprecation-label">Deprecated  </span>


</div>
</div>

</div>

