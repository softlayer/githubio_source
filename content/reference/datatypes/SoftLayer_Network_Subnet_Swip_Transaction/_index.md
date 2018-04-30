---
title: "SoftLayer_Network_Subnet_Swip_Transaction"
description: "The SoftLayer_Network_Subnet_Swip_Transaction data type contains basic information tracked at SoftLayer to allow automat... "
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
            <div class='views-field-body'>A SWIP transaction's unique identifier. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#statusName" name=statusName>statusName</a>
            </span>
            <div class='views-field-body'>A Name describing which state a SWIP  transaction is in. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#subnetId" name=subnetId>subnetId</a>
            </span>
            <div class='views-field-body'>ID Number of the Subnet for this SWIP transaction. </div>
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
                <a href="#account" name=account>account</a>
            </span>
            <div class='views-field-body'>The Account whose RWHOIS data was used to SWIP this subnet </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#subnet" name=subnet>subnet</a>
            </span>
            <div class='views-field-body'>The subnet that this SWIP transaction was created for. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


