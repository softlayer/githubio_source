---
title: "SoftLayer_Dns_Domain_Reverse_Version4"
description: "The SoftLayer_Dns_Domain_Reverse_Version4 data type represents a reverse IPv4 address record."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_Reverse_Version4"
---

# SoftLayer_Dns_Domain_Reverse_Version4
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Dns_Domain_Reverse_Version4' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Dns_Domain_Reverse_Version4 data type represents a reverse IPv4 address record. 

### External Links


* [Reverse DNS lookup at Wikipedia](http://en.wikipedia.org/wiki/Reverse_DNS_lookup)



### associatedMethods

*  [SoftLayer_Network_Vlan::getReverseDomainRecords](/reference/services/SoftLayer_Network_Vlan/getReverseDomainRecords )
*  [SoftLayer_Network_Subnet::getReverseDomainRecords](/reference/services/SoftLayer_Network_Subnet/getReverseDomainRecords )
*  [SoftLayer_Hardware_Server::getReverseDomainRecords](/reference/services/SoftLayer_Hardware_Server/getReverseDomainRecords )



### seeAlso

* [SoftLayer_Dns_Domain](/reference/services/SoftLayer_Dns_Domain )


* [SoftLayer_Dns_Domain_ResourceRecord](/reference/services/SoftLayer_Dns_Domain_ResourceRecord )


* [SoftLayer_Dns_Domain_ResourceRecord_PtrType](/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_PtrType )




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
[networkAddress]: #networkaddress
#### [networkAddress]
Network address the domain is associated with.  
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
The SoftLayer customer account that owns a domain.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[managedResourceFlag]: #managedresourceflag
#### [managedResourceFlag]
A flag indicating that the dns domain record is a managed resource.  
<span class="type-label">Type: </span>**boolean**

-----
[resourceRecords]: #resourcerecords
#### [resourceRecords]
The pointer type records for a reverse domain.  
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
A count of the pointer type records for a reverse domain.   
<span class="type-label">Type: </span>**unsigned long**

</div>


