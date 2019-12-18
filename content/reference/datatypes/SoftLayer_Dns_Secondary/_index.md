---
title: "SoftLayer_Dns_Secondary"
description: "The SoftLayer_Dns_Secondary data type contains information on a single secondary DNS zone which is managed through SoftL... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Secondary"
---

# SoftLayer_Dns_Secondary
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Dns_Secondary' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Dns_Secondary' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Dns_Secondary data type contains information on a single secondary DNS zone which is managed through SoftLayer's zone transfer service. Domains created via zone transfer may not be modified by the SoftLayer portal or API. 

### External Links


* [DNS Zone Transfer at Wikipedia.](http://en.wikipedia.org/wiki/DNS_zone_transfer)


* [Secondary Domains at KnowledgeLayer](http://knowledgelayer.softlayer.com/questions/478)



### associatedMethods

*  [SoftLayer_Dns_Secondary::getObject](/reference/services/SoftLayer_Dns_Secondary/getObject )
*  [SoftLayer_Dns_Domain::getSecondary](/reference/services/SoftLayer_Dns_Domain/getSecondary )
*  [SoftLayer_Account::getSecondaryDomains](/reference/services/SoftLayer_Account/getSecondaryDomains )



### seeAlso

* [SoftLayer_Dns_Domain](/reference/services/SoftLayer_Dns_Domain )




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
[createDate]: #createdate
#### [createDate]
The date a secondary DNS record was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
The internal identifier for a secondary DNS record.  
<span class="type-label">Type: </span>**integer**

-----
[lastUpdate]: #lastupdate
#### [lastUpdate]
The date when the most recent secondary DNS zone transfer took place.  
<span class="type-label">Type: </span>**dateTime**

-----
[masterIpAddress]: #masteripaddress
#### [masterIpAddress]
The IP address of the master name server where a secondary DNS zone is transferred from.  
<span class="type-label">Type: </span>**string**

-----
[statusId]: #statusid
#### [statusId]
The current status of a secondary DNS record.  The status may be one of the following: 
:*'''0''': Disabled
:*'''1''': Active
:*'''2''': Transfer Now
:*'''3''': An error occurred that prevented the zone transfer from being completed.  
<span class="type-label">Type: </span>**integer**

-----
[statusText]: #statustext
#### [statusText]
The textual representation of a secondary DNS zone's status.  
<span class="type-label">Type: </span>**string**

-----
[transferFrequency]: #transferfrequency
#### [transferFrequency]
How often a secondary DNS zone should be transferred in minutes.  
<span class="type-label">Type: </span>**integer**

-----
[zoneName]: #zonename
#### [zoneName]
The name of the zone that is transferred.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The SoftLayer account that owns a secondary DNS record.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[domain]: #domain
#### [domain]
The domain record created by zone transfer from a secondary DNS record.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Domain'>SoftLayer_Dns_Domain </a>**

-----
[errorMessages]: #errormessages
#### [errorMessages]
The error messages created during secondary DNS record transfer.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Message'>SoftLayer_Dns_Message[] </a>**

-----
[status]: #status
#### [status]
The current status of the secondary DNS zone.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Status'>SoftLayer_Dns_Status </a>**


## Count

-----
[errorMessageCount]: #errormessagecount
#### [errorMessageCount]
A count of the error messages created during secondary DNS record transfer.   
<span class="type-label">Type: </span>**unsigned long**

</div>


