---
title: "SoftLayer_Dns_Domain_Forward"
description: "The SoftLayer_Dns_Domain_Forward data type represents a single DNS domain record hosted on the SoftLayer nameservers. Do... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_Forward"
---

# SoftLayer_Dns_Domain_Forward
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Dns_Domain_Forward' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Dns_Domain_Forward data type represents a single DNS domain record hosted on the SoftLayer nameservers. Domains contain general information about the domain name such as name and serial. Individual records such as A, AAAA, CTYPE, and MX records are stored in the domain's associated [SoftLayer_Dns_Domain_ResourceRecord]({{<ref "reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord">}}) records. 


### associatedMethods

*  [SoftLayer_Account::getDomains](/reference/services/SoftLayer_Account/getDomains )
*  [SoftLayer_Dns_Domain_Forward::getObject](/reference/services/SoftLayer_Dns_Domain_Forward/getObject )





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
[id]: #id
#### [id]
A domain record's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[name]: #name
#### [name]
A domain's name including top-level domain, for example "example.com".  
<span class="type-label">Type: </span>**string**

-----
[serial]: #serial
#### [serial]
A unique number denoting the latest revision of a domain. Whenever a domain is changed its corresponding serial number is also changed. Serial numbers typically follow the format yyyymmdd## where yyyy is the current year, mm is the current month, dd is the current day of the month, and ## is the number of the revision for that day. A domain's serial number is automatically updated when edited via the API.   
<span class="type-label">Type: </span>**integer**

-----
[updateDate]: #updatedate
#### [updateDate]
The date that this domain record was last updated.  
<span class="type-label">Type: </span>**dateTime**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
A domain's associated customer account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[managedResourceFlag]: #managedresourceflag
#### [managedResourceFlag]
A flag indicating that the dns domain record is a managed resource.  
<span class="type-label">Type: </span>**boolean**

-----
[resourceRecords]: #resourcerecords
#### [resourceRecords]
The individual records contained within a domain record. These include but are not limited to A, AAAA, MX, CTYPE, SPF and TXT records.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord'>SoftLayer_Dns_Domain_ResourceRecord[] </a>**

-----
[secondary]: #secondary
#### [secondary]
The secondary DNS record that defines this domain as being managed through zone transfers.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Secondary'>SoftLayer_Dns_Secondary </a>**

-----
[soaResourceRecord]: #soaresourcerecord
#### [soaResourceRecord]
The start of authority (SOA) record contains authoritative and propagation details for a DNS zone. This property is not considered in requests to createObject and editObject.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_SoaType'>SoftLayer_Dns_Domain_ResourceRecord_SoaType </a>**


## Count

-----
[resourceRecordCount]: #resourcerecordcount
#### [resourceRecordCount]
A count of the individual records contained within a domain record. These include but are not limited to A, AAAA, MX, CTYPE, SPF and TXT records.   
<span class="type-label">Type: </span>**unsigned long**

</div>


