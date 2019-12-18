---
title: "SoftLayer_Network_Storage_Hub_Cleversafe_Account"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Hub_Cleversafe_Account"
---

# SoftLayer_Network_Storage_Hub_Cleversafe_Account
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Storage_Hub_Cleversafe_Account' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_Hub_Cleversafe_Account' >Datatype</a></li>
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
The ID of the SoftLayer_Account which this IBM Cloud Object Storage account is associated with.   
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
The IMS ID of an IBM Cloud Object Storage account.   
<span class="type-label">Type: </span>**integer**

-----
[notes]: #notes
#### [notes]
A user-defined field of notes.   
<span class="type-label">Type: </span>**string**

-----
[username]: #username
#### [username]
Human readable identifier of IBM Cloud Object Storage accounts.   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
SoftLayer account to which an IBM Cloud Object Storage account belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[billingItem]: #billingitem
#### [billingItem]
An associated parent billing item which is active. Includes billing items which are scheduled to be cancelled in the future.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**

-----
[cancelledBillingItem]: #cancelledbillingitem
#### [cancelledBillingItem]
An associated parent billing item which has been cancelled.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**

-----
[credentials]: #credentials
#### [credentials]
Credentials used for generating an AWS signature. Max of 2.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Credential'>SoftLayer_Network_Storage_Credential[] </a>**

-----
[metricTrackingObject]: #metrictrackingobject
#### [metricTrackingObject]
Provides an interface to various metrics relating to the usage of an IBM Cloud Object Storage account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object'>SoftLayer_Metric_Tracking_Object </a>**

-----
[uuid]: #uuid
#### [uuid]
Unique identifier for an IBM Cloud Object Storage account.  
<span class="type-label">Type: </span>**string**


## Count

-----
[credentialCount]: #credentialcount
#### [credentialCount]
A count of credentials used for generating an AWS signature. Max of 2.   
<span class="type-label">Type: </span>**unsigned long**

</div>


