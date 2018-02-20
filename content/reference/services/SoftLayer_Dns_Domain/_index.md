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

SoftLayer provides secondary DNS hosting services if you wish to maintain DNS records on your name server, but have records replicated on SoftLayer's name servers. Use the [[SoftLayer_Dns_Secondary]] service to manage secondary DNS zones and transfers. 
### external links
        Array
(
    [url] => http://en.wikipedia.org/wiki/Domain_name_system
    [description] => Domain Name System at Wikipedia
)
1        Array
(
    [url] => http://tools.ietf.org/html/rfc1035
    [description] => RFC1035: Domain Names - Implementation and Specification at ietf.org
)
1        
### seeAlso
        SoftLayer_Dns_Domain_ResourceRecord1        SoftLayer_Dns_Domain_Reverse1        SoftLayer_Dns_Secondary1                
        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain/createARecord'> createARecord</a> </span>
            <div class='views-field-body'>Create an A record on a domain.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain/createAaaaRecord'> createAaaaRecord</a> </span>
            <div class='views-field-body'>Create an AAAA record on a domain.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain/createCnameRecord'> createCnameRecord</a> </span>
            <div class='views-field-body'>Create a CNAME record on a domain.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain/createMxRecord'> createMxRecord</a> </span>
            <div class='views-field-body'>Create an MX record on a domain.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain/createNsRecord'> createNsRecord</a> </span>
            <div class='views-field-body'>Create an NS record on a domain.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain/createObject'> createObject</a> </span>
            <div class='views-field-body'>Create a new domain.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain/createObjects'> createObjects</a> </span>
            <div class='views-field-body'>Create multiple domains at once.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain/createPtrRecord'> createPtrRecord</a> </span>
            <div class='views-field-body'>Edit the PTR record for a single IP address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain/createSpfRecord'> createSpfRecord</a> </span>
            <div class='views-field-body'>Create an SPF record on a domain.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain/createTxtRecord'> createTxtRecord</a> </span>
            <div class='views-field-body'>Create a TXT record on a domain.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain/deleteObject'> deleteObject</a> </span>
            <div class='views-field-body'>Remove a domain.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer customer account that owns a domain.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain/getByDomainName'> getByDomainName</a> </span>
            <div class='views-field-body'>Search for domains by name.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain/getManagedResourceFlag'> getManagedResourceFlag</a> </span>
            <div class='views-field-body'>Retrieve a flag indicating that the dns domain record is a managed resource.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Dns_Domain record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain/getResourceRecords'> getResourceRecords</a> </span>
            <div class='views-field-body'>Retrieve the individual records contained within a domain record. These include but are not limited to A, AAAA, MX, CTYPE, SPF and TXT records.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain/getSecondary'> getSecondary</a> </span>
            <div class='views-field-body'>Retrieve the secondary DNS record that defines this domain as being managed through zone transfers.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain/getSoaResourceRecord'> getSoaResourceRecord</a> </span>
            <div class='views-field-body'>Retrieve the start of authority (SOA) record contains authoritative and propagation details for a DNS zone. This property is not considered in requests to createObject and editObject.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain/getZoneFileContents'> getZoneFileContents</a> </span>
            <div class='views-field-body'>Return a domain's data formatted as zone file text.</div>
        </div>
        </div>
</div>

