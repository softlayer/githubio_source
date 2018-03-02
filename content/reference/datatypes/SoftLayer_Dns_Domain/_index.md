---
title: "SoftLayer_Dns_Domain"
description: "The SoftLayer_Dns_Domain data type represents a single DNS domain record hosted on the SoftLayer nameservers. Domains co... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain"
---

# SoftLayer_Dns_Domain
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Dns_Domain' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Dns_Domain data type represents a single DNS domain record hosted on the SoftLayer nameservers. Domains contain general information about the domain name such as name and serial. Individual records such as A, AAAA, CTYPE, and MX records are stored in the domain's associated [[SoftLayer_Dns_Domain_ResourceRecord (type)|SoftLayer_Dns_Domain_ResourceRecord]] records. 


### associatedMethods

*  [SoftLayer_Account::getDomains](/reference/services/SoftLayer_Account/getDomains )
*  [SoftLayer_Dns_Domain::getObject](/reference/services/SoftLayer_Dns_Domain/getObject )
*  [SoftLayer_Dns_Domain_ResourceRecord::getDomain](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/getDomain )



### seeAlso

* [SoftLayer_Dns_Domain_ResourceRecord (type)](/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord (type) )


* [SoftLayer_Dns_Secondary (type)](/reference/datatypes/SoftLayer_Dns_Secondary (type) )




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
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A domain record's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>A domain's name including top-level domain, for example "example.com". </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#serial" name=serial>serial</a></span>
            <div class='views-field-body'>A unique number denoting the latest revision of a domain. Whenever a domain is changed its corresponding serial number is also changed. Serial numbers typically follow the format yyyymmdd## where yyyy is the current year, mm is the current month, dd is the current day of the month, and ## is the number of the revision for that day. A domain's serial number is automatically updated when edited via the API.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#updateDate" name=updateDate>updateDate</a></span>
            <div class='views-field-body'>The date that this domain record was last updated. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'>The SoftLayer customer account that owns a domain. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#managedResourceFlag" name=managedResourceFlag>managedResourceFlag</a></span>
            <div class='views-field-body'>A flag indicating that the dns domain record is a managed resource. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#resourceRecords" name=resourceRecords>resourceRecords</a></span>
            <div class='views-field-body'>The individual records contained within a domain record. These include but are not limited to A, AAAA, MX, CTYPE, SPF and TXT records. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord'>SoftLayer_Dns_Domain_ResourceRecord[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#secondary" name=secondary>secondary</a></span>
            <div class='views-field-body'>The secondary DNS record that defines this domain as being managed through zone transfers. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Dns_Secondary'>SoftLayer_Dns_Secondary </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#soaResourceRecord" name=soaResourceRecord>soaResourceRecord</a></span>
            <div class='views-field-body'>The start of authority (SOA) record contains authoritative and propagation details for a DNS zone. This property is not considered in requests to createObject and editObject. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_SoaType'>SoftLayer_Dns_Domain_ResourceRecord_SoaType </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#resourceRecordCount" name=resourceRecordCount>resourceRecordCount</a></span>
            <div class='views-field-body'>A count of the individual records contained within a domain record. These include but are not limited to A, AAAA, MX, CTYPE, SPF and TXT records. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


