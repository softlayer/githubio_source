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


        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/findMyTransactions'> findMyTransactions</a> </span>
            <div class='views-field-body'>returns SWIP transaction objects that are currently in transaction with ARIN.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the Account whose RWHOIS data was used to SWIP this subnet</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_Subnet_Swip_Transaction record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/getSubnet'> getSubnet</a> </span>
            <div class='views-field-body'>Retrieve the subnet that this SWIP transaction was created for.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/removeAllSubnetSwips'> removeAllSubnetSwips</a> </span>
            <div class='views-field-body'>Removes registration information from ARIN for all your subnets</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/removeSwipData'> removeSwipData</a> </span>
            <div class='views-field-body'>Deletes registration information from ARIN for a single subnet</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/resendSwipData'> resendSwipData</a> </span>
            <div class='views-field-body'>Sends updated RWHOIS information to ARIN for a single subnet.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/swipAllSubnets'> swipAllSubnets</a> </span>
            <div class='views-field-body'>create SWIP transactions for all subnets that do not already have a SWIP transaction in progress.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_Swip_Transaction/updateAllSubnetSwips'> updateAllSubnetSwips</a> </span>
            <div class='views-field-body'>Update all subnets on the account with an "OK" status.</div>
        </div>
        </div>
</div>

