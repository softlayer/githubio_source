---
title: "SoftLayer_Dns_Domain_ResourceRecord_TxtType"
description: "SoftLayer_Dns_Domain_ResourceRecord_TxtType is a SoftLayer_Dns_Domain_ResourceRecord object whose ''type'' property is s... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord_TxtType"
---

# SoftLayer_Dns_Domain_ResourceRecord_TxtType
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_TxtType' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Dns_Domain_ResourceRecord_TxtType is a SoftLayer_Dns_Domain_ResourceRecord object whose ''type'' property is set to "txt" and defines a DNS TXT record on a SoftLayer hosted domain. A TXT record provides a text description for a host. For instance, if defining the TXT record "My test host" for "host.example.org". then the ''host'' property equals "host" and the ''data'' property equals "My test host". 

TXT records are commonly used in email verification methods such as Sender Policy Framework. 

### External Links


* [List of DNS record types at Wikipedia](http://en.wikipedia.org/wiki/List_of_DNS_record_types)


* [Sender Policy Framework](http://www.openspf.org/Project_Overview)



### associatedMethods

*  [SoftLayer_Dns_Domain::createTxtRecord](/reference/services/SoftLayer_Dns_Domain/createTxtRecord )



### seeAlso

* [SoftLayer_Dns_Domain](/reference/services/SoftLayer_Dns_Domain )


* [SoftLayer_Dns_Domain_ResourceRecord](/reference/services/SoftLayer_Dns_Domain_ResourceRecord )




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
The string "txt" which defines a resource record as a TXT record.  
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


