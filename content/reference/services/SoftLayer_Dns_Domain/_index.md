---
title: "SoftLayer_Dns_Domain"
description: "SoftLayer customers have the option of hosting DNS domains on the SoftLayer name servers. Individual domains hosted on t... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain"
---
# SoftLayer_Dns_Domain
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Dns_Domain' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Dns_Domain' >Datatype</a></li>
    </ul>
</div>

## Description
SoftLayer customers have the option of hosting DNS domains on the SoftLayer name servers. Individual domains hosted on the SoftLayer name servers are handled through the SoftLayer_Dns_Domain service. 

Domain changes are applied automatically by our nameservers, but changes may not be received by the other name servers on the Internet for 72 hours after your change. The SoftLayer_Dns_Domain service does not apply to customers who run their own nameservers on servers purchased from SoftLayer. 

SoftLayer provides secondary DNS hosting services if you wish to maintain DNS records on your name server, but have records replicated on SoftLayer's name servers. Use the [SoftLayer_Dns_Secondary]({{<ref "reference/datatypes/SoftLayer_Dns_Secondary">}}) service to manage secondary DNS zones and transfers. 

### External Links


* [Domain Name System at Wikipedia](http://en.wikipedia.org/wiki/Domain_name_system)


* [RFC1035: Domain Names - Implementation and Specification at ietf.org](http://tools.ietf.org/html/rfc1035)




### seeAlso

* [SoftLayer_Dns_Domain_ResourceRecord](/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord )


* [SoftLayer_Dns_Domain_Reverse](/reference/datatypes/SoftLayer_Dns_Domain_Reverse )


* [SoftLayer_Dns_Secondary](/reference/datatypes/SoftLayer_Dns_Secondary )


        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [createARecord](/reference/services/SoftLayer_Dns_Domain/createARecord)
Create an A record on a domain.

#### [createAaaaRecord](/reference/services/SoftLayer_Dns_Domain/createAaaaRecord)
Create an AAAA record on a domain.

#### [createCnameRecord](/reference/services/SoftLayer_Dns_Domain/createCnameRecord)
Create a CNAME record on a domain.

#### [createMxRecord](/reference/services/SoftLayer_Dns_Domain/createMxRecord)
Create an MX record on a domain.

#### [createNsRecord](/reference/services/SoftLayer_Dns_Domain/createNsRecord)
Create an NS record on a domain.

#### [createObject](/reference/services/SoftLayer_Dns_Domain/createObject)
Create a new domain.

#### [createObjects](/reference/services/SoftLayer_Dns_Domain/createObjects)
Create multiple domains at once.

#### [createPtrRecord](/reference/services/SoftLayer_Dns_Domain/createPtrRecord)
Edit the PTR record for a single IP address.

#### [createSpfRecord](/reference/services/SoftLayer_Dns_Domain/createSpfRecord)
Create an SPF record on a domain.

#### [createTxtRecord](/reference/services/SoftLayer_Dns_Domain/createTxtRecord)
Create a TXT record on a domain.

#### [deleteObject](/reference/services/SoftLayer_Dns_Domain/deleteObject)
Remove a domain.

#### [getAccount](/reference/services/SoftLayer_Dns_Domain/getAccount)
Retrieve the SoftLayer customer account that owns a domain.

#### [getByDomainName](/reference/services/SoftLayer_Dns_Domain/getByDomainName)
Search for domains by name.

#### [getManagedResourceFlag](/reference/services/SoftLayer_Dns_Domain/getManagedResourceFlag)
Retrieve a flag indicating that the dns domain record is a managed resource.

#### [getObject](/reference/services/SoftLayer_Dns_Domain/getObject)
Retrieve a SoftLayer_Dns_Domain record.

#### [getResourceRecords](/reference/services/SoftLayer_Dns_Domain/getResourceRecords)
Retrieve the individual records contained within a domain record. These include but are not limited to A, AAAA, MX, CTYPE, SPF and TXT records.

#### [getSecondary](/reference/services/SoftLayer_Dns_Domain/getSecondary)
Retrieve the secondary DNS record that defines this domain as being managed through zone transfers.

#### [getSoaResourceRecord](/reference/services/SoftLayer_Dns_Domain/getSoaResourceRecord)
Retrieve the start of authority (SOA) record contains authoritative and propagation details for a DNS zone. This property is not considered in requests to createObject and editObject.

#### [getZoneFileContents](/reference/services/SoftLayer_Dns_Domain/getZoneFileContents)
Return a domain's data formatted as zone file text.

</div>

