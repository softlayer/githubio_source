---
title: "SoftLayer_Dns_Domain_ResourceRecord_SrvType"
description: "SoftLayer_Dns_Domain_ResourceRecord_SrvType is a SoftLayer_Dns_Domain_ResourceRecord object whose ''type'' property is s... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord_SrvType"
---

# SoftLayer_Dns_Domain_ResourceRecord_SrvType
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Dns_Domain_ResourceRecord_SrvType' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_SrvType' >Datatype</a></li>
    </ul>
</div>

## Description 


SoftLayer_Dns_Domain_ResourceRecord_SrvType is a SoftLayer_Dns_Domain_ResourceRecord object whose ''type'' property is set to "srv" and defines a DNS SRV record on a SoftLayer hosted domain. 

### External Links


* [SRV Record at Wikipedia](http://en.wikipedia.org/wiki/SRV_record)



### associatedMethods

*  [SoftLayer_Dns_Domain_ResourceRecord_SrvType::createObject](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_SrvType/createObject )



### seeAlso

* [SoftLayer_Dns_Domain](/reference/services/SoftLayer_Dns_Domain )


* [SoftLayer_Dns_Domain_ResourceRecord](/reference/services/SoftLayer_Dns_Domain_ResourceRecord )




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
[data]: #data
#### [data]
The value of a domain's resource record. This can be an IP address or a hostname. Fully qualified host and domain name data must end with the "." character.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[domainId]: #domainid
#### [domainId]
An identifier belonging to the domain that a resource record is associated with.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[expire]: #expire
#### [expire]
The amount of time in seconds that a secondary name server (or servers) will hold a zone before it is no longer considered authoritative.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[host]: #host
#### [host]
The host defined by a resource record. A value of "@" denotes a wildcard.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A domain resource record's internal identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[minimum]: #minimum
#### [minimum]
The amount of time in seconds that a domain's resource records are valid. This is also known as a minimum TTL, and can be overridden by an individual resource record's TTL.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[mxPriority]: #mxpriority
#### [mxPriority]
Useful in cases where a domain has more than one mail exchanger, the priority property is the priority of the MTA that delivers mail for a domain. A lower number denotes a higher priority, and mail will attempt to deliver through that MTA before moving to lower priority mail servers. Priority is defaulted to 10 upon resource record creation.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[port]: #port
#### [port]
The TCP or UDP port on which the service is to be found.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[priority]: #priority
#### [priority]
The priority of the target host, lower value means more preferred.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[protocol]: #protocol
#### [protocol]
The protocol of the desired service; this is usually either TCP or UDP.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[refresh]: #refresh
#### [refresh]
The amount of time in seconds that a secondary name server should wait to check for a new copy of a DNS zone from the domain's primary name server. If a zone file has changed then the secondary DNS server will update it's copy of the zone to match the primary DNS server's zone.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[responsiblePerson]: #responsibleperson
#### [responsiblePerson]
The email address of the person responsible for a domain, with the "@" replaced with a ".". For instance, if root@example.org is responsible for example.org, then example.org's SOA responsibility is "root.example.org.".   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[retry]: #retry
#### [retry]
The amount of time in seconds that a domain's primary name server (or servers) should wait if an attempt to refresh by a secondary name server failed before attempting to refresh a domain's zone with that secondary name server again.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[service]: #service
#### [service]
The symbolic name of the desired service  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[ttl]: #ttl
#### [ttl]
The Time To Live value of a resource record, measured in seconds. TTL is used by a name server to determine how long to cache a resource record. An SOA record's TTL value defines the domain's overall TTL.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The string "srv" which defines a resource record as an SRV record.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[weight]: #weight
#### [weight]
A relative weight for records with the same priority.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[domain]: #domain
#### [domain]
The domain that a resource record belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Domain'>SoftLayer_Dns_Domain </a>**  



</div>

## Count
</div>


