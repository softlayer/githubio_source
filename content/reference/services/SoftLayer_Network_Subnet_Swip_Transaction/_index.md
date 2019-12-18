---
title: "SoftLayer_Network_Subnet_Swip_Transaction"
description: "SoftLayer's Automated Swip System is a finite state machine; it works by locally tracking a transaction between SoftLaye... "
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
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [findMyTransactions](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/findMyTransactions)
returns SWIP transaction objects that are currently in transaction with ARIN.

#### [getAccount](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/getAccount)
Retrieve the Account whose RWHOIS data was used to SWIP this subnet

#### [getObject](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/getObject)
Retrieve a SoftLayer_Network_Subnet_Swip_Transaction record.

#### [getSubnet](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/getSubnet)
Retrieve the subnet that this SWIP transaction was created for.

#### [removeAllSubnetSwips](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/removeAllSubnetSwips)
Removes registration information from ARIN for all your subnets

#### [removeSwipData](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/removeSwipData)
Deletes registration information from ARIN for a single subnet

#### [resendSwipData](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/resendSwipData)
Sends updated RWHOIS information to ARIN for a single subnet.

#### [swipAllSubnets](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/swipAllSubnets)
create SWIP transactions for all subnets that do not already have a SWIP transaction in progress.

#### [updateAllSubnetSwips](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/updateAllSubnetSwips)
Update all subnets on the account with an "OK" status.

</div>

