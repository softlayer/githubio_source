---
title: "SoftLayer_Network_Subnet_Rwhois_Data"
description: "**DEPRECATED**
Use SoftLayer_Account_Regional_Registry_Detail and SoftLayer_Network_Subnet_Registration instead. 

Every... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Rwhois_Data"
---
# SoftLayer_Network_Subnet_Rwhois_Data
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Subnet_Rwhois_Data' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Subnet_Rwhois_Data' >Datatype</a></li>
    </ul>
</div>

## Description

<div class="deprecated"><span class="deprecation-label">Deprecated  </span></div>


**DEPRECATED**
Use SoftLayer_Account_Regional_Registry_Detail and SoftLayer_Network_Subnet_Registration instead. 

Every SoftLayer customer account has a RWHOIS record tied to it.  This RWHOIS record is used by SoftLayer's Reverse Whois system as well as SoftLayer's Automated SWIP system. 

This service allows you to update your stored RWHOIS record.  Changing this record automatically updates the RWHOIS record in 24 hours, but does NOT update SWIP data.  You will need to use the SWIP service to do that. 



### seeAlso

* [SoftLayer_Network_Subnet_Swip_Transaction](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction )


        
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

#### [editObject](/reference/services/SoftLayer_Network_Subnet_Rwhois_Data/editObject)
Edit the RWHOIS record by passing in a modified version of the record object. All fields are editable. The fields are as follows: 
* companyName
* firstName
* lastName
* city
* country
* postalCode
* abuseEmail
* address1

<span class="deprecation-label">Deprecated  </span>


</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Network_Subnet_Rwhois_Data/getAccount)
Retrieve the SoftLayer customer account associated with this reverse WHOIS data.

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_Subnet_Rwhois_Data/getObject)
Retrieve a SoftLayer_Network_Subnet_Rwhois_Data record.

</div>
</div>

</div>

