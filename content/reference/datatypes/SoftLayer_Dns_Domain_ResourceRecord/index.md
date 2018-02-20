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
* '''"a"''' for [[SoftLayer_Dns_Domain_ResourceRecord_AType|address]] records
* '''"aaaa"''' for [[SoftLayer_Dns_Domain_ResourceRecord_AaaaType|address]] records
* '''"cname"''' for [[SoftLayer_Dns_Domain_ResourceRecord_CnameType|canonical name]] records
* '''"mx"''' for [[SoftLayer_Dns_Domain_ResourceRecord_MxType|mail exchanger]] records
* '''"ns"''' for [[SoftLayer_Dns_Domain_ResourceRecord_NsType|name server]] records
* '''"ptr"''' for [[SoftLayer_Dns_Domain_ResourceRecord_PtrType|pointer]] records in reverse domains
* '''"soa"''' for a domain's [[SoftLayer_Dns_Domain_ResourceRecord_SoaType|start of authority]] record
* '''"spf"''' for [[SoftLayer_Dns_Domain_ResourceRecord_SpfType|sender policy framework]] records
* '''"srv"''' for [[SoftLayer_Dns_Domain_ResourceRecord_SrvType|service]] records
* '''"txt"''' for [[SoftLayer_Dns_Domain_ResourceRecord_TxtType|text]] records


As ''SoftLayer_Dns_Domain_ResourceRecord'' objects are created and loaded, the API verifies the ''type'' property and casts the object as the appropriate type. 
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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#data" name=data>data</a></span>
            <div class='views-field-body'>The value of a domain's resource record. This can be an IP address or a hostname. Fully qualified host and domain name data must end with the "." character.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#domainId" name=domainId>domainId</a></span>
            <div class='views-field-body'>An identifier belonging to the domain that a resource record is associated with. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#expire" name=expire>expire</a></span>
            <div class='views-field-body'>The amount of time in seconds that a secondary name server (or servers) will hold a zone before it is no longer considered authoritative.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#host" name=host>host</a></span>
            <div class='views-field-body'>The host defined by a resource record. A value of "@" denotes a wildcard. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A domain resource record's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#minimum" name=minimum>minimum</a></span>
            <div class='views-field-body'>The amount of time in seconds that a domain's resource records are valid. This is also known as a minimum TTL, and can be overridden by an individual resource record's TTL.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#mxPriority" name=mxPriority>mxPriority</a></span>
            <div class='views-field-body'>Useful in cases where a domain has more than one mail exchanger, the priority property is the priority of the MTA that delivers mail for a domain. A lower number denotes a higher priority, and mail will attempt to deliver through that MTA before moving to lower priority mail servers. Priority is defaulted to 10 upon resource record creation.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#refresh" name=refresh>refresh</a></span>
            <div class='views-field-body'>The amount of time in seconds that a secondary name server should wait to check for a new copy of a DNS zone from the domain's primary name server. If a zone file has changed then the secondary DNS server will update it's copy of the zone to match the primary DNS server's zone.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#responsiblePerson" name=responsiblePerson>responsiblePerson</a></span>
            <div class='views-field-body'>The email address of the person responsible for a domain, with the "@" replaced with a ".". For instance, if root@example.org is responsible for example.org, then example.org's SOA responsibility is "root.example.org.".  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#retry" name=retry>retry</a></span>
            <div class='views-field-body'>The amount of time in seconds that a domain's primary name server (or servers) should wait if an attempt to refresh by a secondary name server failed before attempting to refresh a domain's zone with that secondary name server again.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ttl" name=ttl>ttl</a></span>
            <div class='views-field-body'>The Time To Live value of a resource record, measured in seconds. TTL is used by a name server to determine how long to cache a resource record. An SOA record's TTL value defines the domain's overall TTL.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#type" name=type>type</a></span>
            <div class='views-field-body'>A domain resource record's type. A value of "a" denotes an A (address) record, "aaaa" denotes an AAAA (IPv6 address) record, "cname" denotes a CNAME (canonical name) record, "mx" denotes an MX (mail exchanger) record, "ns" denotes an NS (nameserver) record, "ptr" denotes a PTR (pointer/reverse) record, "soa" denotes the SOA (start of authority) record, "spf" denotes a SPF (sender policy framework) record, and "txt" denotes a TXT (text) record. A domain record's type also denotes which class in the SoftLayer API is a best match for extending a resource record.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#domain" name=domain>domain</a></span>
            <div class='views-field-body'>The domain that a resource record belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Dns_Domain'>SoftLayer_Dns_Domain </a></p></div>
        </div>
            </div>
</div>


