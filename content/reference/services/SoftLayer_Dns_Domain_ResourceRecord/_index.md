---
title: "SoftLayer_Dns_Domain_ResourceRecord"
description: "Every domain record hosted on the SoftLayer name servers is comprised of a series or resource records that control how t... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
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
Every domain record hosted on the SoftLayer name servers is comprised of a series or resource records that control how the domain operates, translates host names, and translates service location. Each of those resource records is controlled by the SoftLayer_Dns_Domain_ResourceRecord service. SoftLayer domains have the following resource records: 
* A single SOA record
* A records
* AAAA records
* Optional CNAME records
* At least one MX record
* NS records for ns1.softlayer.com and ns2.softlayer.com
* Optional TXT records
* Optional SPF records


The SoftLayer_Dns_Domain_ResourceRecords service also controls the records contained in reverse DNS records. SoftLayer_Dns_Domain_Reverse records contain multiple PTR type resource records. 

As with domain changes, resource record changes happen immediately, but may take up to 72 hours to propagate to the rest of the Internet's name servers. The SoftLayer_Dns_Domain_ResourceRecord service only applies to domains hosted on the SoftLayer name servers. 
### external links
        Array
(
    [url] => http://en.wikipedia.org/wiki/List_of_DNS_record_types
    [description] => List of DNS record types at Wikipedia
)
1        
### seeAlso
        SoftLayer_Dns_Domain1        SoftLayer_Dns_Domain_Reverse1        SoftLayer_Dns_Domain_ResourceRecord_AType1        SoftLayer_Dns_Domain_ResourceRecord_AaaaType1        SoftLayer_Dns_Domain_ResourceRecord_CnameType1        SoftLayer_Dns_Domain_ResourceRecord_MxType1        SoftLayer_Dns_Domain_ResourceRecord_NsType1        SoftLayer_Dns_Domain_ResourceRecord_PtrType1        SoftLayer_Dns_Domain_ResourceRecord_SoaType1        SoftLayer_Dns_Domain_ResourceRecord_SpfType1        SoftLayer_Dns_Domain_ResourceRecord_SrvType1        SoftLayer_Dns_Domain_ResourceRecord_TxtType1                
        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain_ResourceRecord/createObject'> createObject</a> </span>
            <div class='views-field-body'>Create a domain's resource record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain_ResourceRecord/createObjects'> createObjects</a> </span>
            <div class='views-field-body'>Create multiple domain resource records.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain_ResourceRecord/deleteObject'> deleteObject</a> </span>
            <div class='views-field-body'>Delete a domain's resource record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain_ResourceRecord/deleteObjects'> deleteObjects</a> </span>
            <div class='views-field-body'>Delete multiple resource records from a domain.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain_ResourceRecord/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit a domain's resource record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain_ResourceRecord/editObjects'> editObjects</a> </span>
            <div class='views-field-body'>Edit multiple domain resource records.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain_ResourceRecord/getDomain'> getDomain</a> </span>
            <div class='views-field-body'>Retrieve the domain that a resource record belongs to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Domain_ResourceRecord/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Dns_Domain_ResourceRecord record.</div>
        </div>
        </div>
</div>

