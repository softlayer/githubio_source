---
title: "SoftLayer_Dns_Domain_ResourceRecord"
description: "The SoftLayer_Dns_Domain_ResourceRecord data type represents a single resource record entry in a SoftLayer hosted domain... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord"
---

# SoftLayer_Dns_Domain_ResourceRecord
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Dns_Domain_ResourceRecord' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Dns_Domain_ResourceRecord data type represents a single resource record entry in a SoftLayer hosted domain. Each resource record contains a ''host'' and ''data'' property, defining a resource's name and it's target data. Domains contain multiple types of resource records. The ''type'' property separates out resource records by type. ''Type'' can take one of the following values: 
* '''"a"''' for [SoftLayer_Dns_Domain_ResourceRecord_AType]({{<ref "reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_AType">}}) records
* '''"aaaa"''' for [SoftLayer_Dns_Domain_ResourceRecord_AaaaType]({{<ref "reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_AaaaType">}}) records
* '''"cname"''' for [SoftLayer_Dns_Domain_ResourceRecord_CnameType]({{<ref "reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_CnameType">}}) records
* '''"mx"''' for [SoftLayer_Dns_Domain_ResourceRecord_MxType]({{<ref "reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_MxType">}}) records
* '''"ns"''' for [SoftLayer_Dns_Domain_ResourceRecord_NsType]({{<ref "reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_NsType">}}) records
* '''"ptr"''' for [SoftLayer_Dns_Domain_ResourceRecord_PtrType]({{<ref "reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_PtrType">}}) records in reverse domains
* '''"soa"''' for a domain's [SoftLayer_Dns_Domain_ResourceRecord_SoaType]({{<ref "reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_SoaType">}}) record
* '''"spf"''' for [SoftLayer_Dns_Domain_ResourceRecord_SpfType]({{<ref "reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_SpfType">}}) records
* '''"srv"''' for [SoftLayer_Dns_Domain_ResourceRecord_SrvType]({{<ref "reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_SrvType">}}) records
* '''"txt"''' for [SoftLayer_Dns_Domain_ResourceRecord_TxtType]({{<ref "reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_TxtType">}}) records


As ''SoftLayer_Dns_Domain_ResourceRecord'' objects are created and loaded, the API verifies the ''type'' property and casts the object as the appropriate type. 

### External Links


* [List of DNS record types at Wikipedia](http://en.wikipedia.org/wiki/List_of_DNS_record_types)



### associatedMethods

*  [SoftLayer_Dns_Domain::getResourceRecords](/reference/services/SoftLayer_Dns_Domain/getResourceRecords )
*  [SoftLayer_Dns_Domain::createARecord](/reference/services/SoftLayer_Dns_Domain/createARecord )
*  [SoftLayer_Dns_Domain::createAaaaRecord](/reference/services/SoftLayer_Dns_Domain/createAaaaRecord )
*  [SoftLayer_Dns_Domain::createCnameRecord](/reference/services/SoftLayer_Dns_Domain/createCnameRecord )
*  [SoftLayer_Dns_Domain::createMxRecord](/reference/services/SoftLayer_Dns_Domain/createMxRecord )
*  [SoftLayer_Dns_Domain::createNsRecord](/reference/services/SoftLayer_Dns_Domain/createNsRecord )
*  [SoftLayer_Dns_Domain::createSpfRecord](/reference/services/SoftLayer_Dns_Domain/createSpfRecord )
*  [SoftLayer_Dns_Domain::createTxtRecord](/reference/services/SoftLayer_Dns_Domain/createTxtRecord )
*  [SoftLayer_Dns_Domain_ResourceRecord::getObject](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/getObject )



### seeAlso

* [SoftLayer_Dns_Domain](/reference/services/SoftLayer_Dns_Domain )


* [SoftLayer_Dns_Domain_Reverse](/reference/datatypes/SoftLayer_Dns_Domain_Reverse )


* [SoftLayer_Dns_Domain_ResourceRecord_AType](/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_AType )


* [SoftLayer_Dns_Domain_ResourceRecord_AaaaType](/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_AaaaType )


* [SoftLayer_Dns_Domain_ResourceRecord_CnameType](/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_CnameType )


* [SoftLayer_Dns_Domain_ResourceRecord_MxType](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_MxType )


* [SoftLayer_Dns_Domain_ResourceRecord_NsType](/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_NsType )


* [SoftLayer_Dns_Domain_ResourceRecord_PtrType](/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_PtrType )


* [SoftLayer_Dns_Domain_ResourceRecord_SoaType](/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_SoaType )


* [SoftLayer_Dns_Domain_ResourceRecord_SpfType](/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_SpfType )


* [SoftLayer_Dns_Domain_ResourceRecord_SrvType](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_SrvType )


* [SoftLayer_Dns_Domain_ResourceRecord_TxtType](/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_TxtType )




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
[data]: #data
#### [data]
The value of a domain's resource record. This can be an IP address or a hostname. Fully qualified host and domain name data must end with the "." character.   
<span class="type-label">Type: </span>**string**

-----
[domainId]: #domainid
#### [domainId]
An identifier belonging to the domain that a resource record is associated with.  
<span class="type-label">Type: </span>**integer**

-----
[expire]: #expire
#### [expire]
The amount of time in seconds that a secondary name server (or servers) will hold a zone before it is no longer considered authoritative.   
<span class="type-label">Type: </span>**integer**

-----
[host]: #host
#### [host]
The host defined by a resource record. A value of "@" denotes a wildcard.  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
A domain resource record's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[minimum]: #minimum
#### [minimum]
The amount of time in seconds that a domain's resource records are valid. This is also known as a minimum TTL, and can be overridden by an individual resource record's TTL.   
<span class="type-label">Type: </span>**integer**

-----
[mxPriority]: #mxpriority
#### [mxPriority]
Useful in cases where a domain has more than one mail exchanger, the priority property is the priority of the MTA that delivers mail for a domain. A lower number denotes a higher priority, and mail will attempt to deliver through that MTA before moving to lower priority mail servers. Priority is defaulted to 10 upon resource record creation.   
<span class="type-label">Type: </span>**integer**

-----
[refresh]: #refresh
#### [refresh]
The amount of time in seconds that a secondary name server should wait to check for a new copy of a DNS zone from the domain's primary name server. If a zone file has changed then the secondary DNS server will update it's copy of the zone to match the primary DNS server's zone.   
<span class="type-label">Type: </span>**integer**

-----
[responsiblePerson]: #responsibleperson
#### [responsiblePerson]
The email address of the person responsible for a domain, with the "@" replaced with a ".". For instance, if root@example.org is responsible for example.org, then example.org's SOA responsibility is "root.example.org.".   
<span class="type-label">Type: </span>**string**

-----
[retry]: #retry
#### [retry]
The amount of time in seconds that a domain's primary name server (or servers) should wait if an attempt to refresh by a secondary name server failed before attempting to refresh a domain's zone with that secondary name server again.   
<span class="type-label">Type: </span>**integer**

-----
[ttl]: #ttl
#### [ttl]
The Time To Live value of a resource record, measured in seconds. TTL is used by a name server to determine how long to cache a resource record. An SOA record's TTL value defines the domain's overall TTL.   
<span class="type-label">Type: </span>**integer**

-----
[type]: #type
#### [type]
A domain resource record's type. A value of "a" denotes an A (address) record, "aaaa" denotes an AAAA (IPv6 address) record, "cname" denotes a CNAME (canonical name) record, "mx" denotes an MX (mail exchanger) record, "ns" denotes an NS (nameserver) record, "ptr" denotes a PTR (pointer/reverse) record, "soa" denotes the SOA (start of authority) record, "spf" denotes a SPF (sender policy framework) record, and "txt" denotes a TXT (text) record. A domain record's type also denotes which class in the SoftLayer API is a best match for extending a resource record.   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[domain]: #domain
#### [domain]
The domain that a resource record belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Domain'>SoftLayer_Dns_Domain </a>**


## Count
</div>


