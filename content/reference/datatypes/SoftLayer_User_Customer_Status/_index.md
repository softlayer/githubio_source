---
title: "SoftLayer_User_Customer_Status"
description: "Each SoftLayer User Customer instance is assigned a status code that determines how it's treated in the customer portal.... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Status"
---

# SoftLayer_User_Customer_Status
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_User_Customer_Status' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_Status' >Datatype</a></li>
    </ul>
</div>

## Description 


Each SoftLayer User Customer instance is assigned a status code that determines how it's treated in the customer portal. This status is reflected in the SoftLayer_User_Customer_Status data type. Status differs from user permissions in that user status applies globally to the portal while user permissions are applied to specific portal functions. 

Note that a status of "PENDING" also has been added. This status is specific to users that are configured to use IBMid authentication. This would include some (not all) users on accounts that are linked to Platform Services (PaaS, formerly Bluemix) accounts, but is not limited to users in such accounts. Using IBMid authentication is optional for active users even if it is not required by the account type. PENDING status indicates that a relationship between an IBMid and a user is being set up but is not complete. To be complete, PENDING users need to perform an action ("accepting the invitation") before becoming an active user within IBM Cloud and/or IMS. PENDING is a system state, and can not be administered by users (including the account master user). SoftLayer Commercial is the only environment where IBMid and/or account linking are used. 




### associatedMethods

*  [SoftLayer_User_Customer::getUserStatus](/reference/services/SoftLayer_User_Customer/getUserStatus )
*  [SoftLayer_User_Customer_Status::getObject](/reference/services/SoftLayer_User_Customer_Status/getObject )



### seeAlso

* [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer )




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
A user's status identifying number.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[keyName]: #keyname
#### [keyName]
A user's status keyname  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A user's status. This can be either "Active" for user accounts with portal access, "Inactive" for users disabled by another portal user, "Disabled" for accounts turned off by SoftLayer, or "VPN Only" for user accounts with no access to the customer portal but VPN access to the private network.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


