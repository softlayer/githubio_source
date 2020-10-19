---
title: "SoftLayer_Dns_Domain_Reverse"
description: "The SoftLayer_Dns_Domain_Reverse data type represents a reverse IP address record."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_Reverse"
---

# SoftLayer_Dns_Domain_Reverse
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Dns_Domain_Reverse' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Dns_Domain_Reverse data type represents a reverse IP address record. 

### External Links


* [Reverse DNS lookup at Wikipedia](http://en.wikipedia.org/wiki/Reverse_DNS_lookup)



### associatedMethods

*  [SoftLayer_Network_Vlan::getReverseDomainRecords](/reference/services/SoftLayer_Network_Vlan/getReverseDomainRecords )
*  [SoftLayer_Network_Subnet::getReverseDomainRecords](/reference/services/SoftLayer_Network_Subnet/getReverseDomainRecords )
*  [SoftLayer_Hardware_Server::getReverseDomainRecords](/reference/services/SoftLayer_Hardware_Server/getReverseDomainRecords )



### seeAlso

* [SoftLayer_Dns_Domain](/reference/datatypes/SoftLayer_Dns_Domain )


* [SoftLayer_Dns_Domain_ResourceRecord](/reference/services/SoftLayer_Dns_Domain_ResourceRecord )


* [SoftLayer_Dns_Domain_ResourceRecord_PtrType](/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_PtrType )




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
A domain record's internal identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A domain's name including top-level domain, for example "example.com".  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[networkAddress]: #networkaddress
#### [networkAddress]
Network address the domain is associated with.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[serial]: #serial
#### [serial]
A unique number denoting the latest revision of a domain. Whenever a domain is changed its corresponding serial number is also changed. Serial numbers typically follow the format yyyymmdd## where yyyy is the current year, mm is the current month, dd is the current day of the month, and ## is the number of the revision for that day. A domain's serial number is automatically updated when edited via the API.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[updateDate]: #updatedate
#### [updateDate]
The date that this domain record was last updated.  
<span class="type-label">Type: </span>**dateTime**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The SoftLayer customer account that owns a domain.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[managedResourceFlag]: #managedresourceflag
#### [managedResourceFlag]
A flag indicating that the dns domain record is a managed resource.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[resourceRecords]: #resourcerecords
#### [resourceRecords]
The pointer type records for a reverse domain.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord'>SoftLayer_Dns_Domain_ResourceRecord[] </a>**


</div>
<div class="prop-row">

-----
[secondary]: #secondary
#### [secondary]
The secondary DNS record that defines this domain as being managed through zone transfers.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Secondary'>SoftLayer_Dns_Secondary </a>**


</div>
<div class="prop-row">

-----
[soaResourceRecord]: #soaresourcerecord
#### [soaResourceRecord]
The start of authority (SOA) record contains authoritative and propagation details for a DNS zone. This property is not considered in requests to createObject and editObject.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_SoaType'>SoftLayer_Dns_Domain_ResourceRecord_SoaType </a>**


</div>

## Count
<div class="prop-row">

-----
[resourceRecordCount]: #resourcerecordcount
#### [resourceRecordCount]
A count of the pointer type records for a reverse domain.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


