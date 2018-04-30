---
title: "SoftLayer_Dns_Secondary"
description: "The SoftLayer_Dns_Secondary data type contains information on a single secondary DNS zone which is managed through SoftL... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Secondary"
---

# SoftLayer_Dns_Secondary
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Dns_Secondary' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Dns_Secondary' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Dns_Secondary data type contains information on a single secondary DNS zone which is managed through SoftLayer's zone transfer service. Domains created via zone transfer may not be modified by the SoftLayer portal or API. 

### External Links


* [DNS Zone Transfer at Wikipedia.](http://en.wikipedia.org/wiki/DNS_zone_transfer)


* [Secondary Domains at KnowledgeLayer](http://knowledgelayer.softlayer.com/questions/478)



### associatedMethods

*  [SoftLayer_Dns_Secondary::getObject](/reference/services/SoftLayer_Dns_Secondary/getObject )
*  [SoftLayer_Dns_Domain::getSecondary](/reference/services/SoftLayer_Dns_Domain/getSecondary )
*  [SoftLayer_Account::getSecondaryDomains](/reference/services/SoftLayer_Account/getSecondaryDomains )



### seeAlso

* [SoftLayer_Dns_Domain](/reference/services/SoftLayer_Dns_Domain )




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
            <span class='views-field-title'>
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'>The date a secondary DNS record was created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The internal identifier for a secondary DNS record. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#lastUpdate" name=lastUpdate>lastUpdate</a>
            </span>
            <div class='views-field-body'>The date when the most recent secondary DNS zone transfer took place. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#masterIpAddress" name=masterIpAddress>masterIpAddress</a>
            </span>
            <div class='views-field-body'>The IP address of the master name server where a secondary DNS zone is transferred from. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#statusId" name=statusId>statusId</a>
            </span>
            <div class='views-field-body'>The current status of a secondary DNS record.  The status may be one of the following: 
:*'''0''': Disabled
:*'''1''': Active
:*'''2''': Transfer Now
:*'''3''': An error occurred that prevented the zone transfer from being completed. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#statusText" name=statusText>statusText</a>
            </span>
            <div class='views-field-body'>The textual representation of a secondary DNS zone's status. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#transferFrequency" name=transferFrequency>transferFrequency</a>
            </span>
            <div class='views-field-body'>How often a secondary DNS zone should be transferred in minutes. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#zoneName" name=zoneName>zoneName</a>
            </span>
            <div class='views-field-body'>The name of the zone that is transferred. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#account" name=account>account</a>
            </span>
            <div class='views-field-body'>The SoftLayer account that owns a secondary DNS record. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#domain" name=domain>domain</a>
            </span>
            <div class='views-field-body'>The domain record created by zone transfer from a secondary DNS record. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Dns_Domain'>SoftLayer_Dns_Domain </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#errorMessages" name=errorMessages>errorMessages</a>
            </span>
            <div class='views-field-body'>The error messages created during secondary DNS record transfer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Dns_Message'>SoftLayer_Dns_Message[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#status" name=status>status</a>
            </span>
            <div class='views-field-body'>The current status of the secondary DNS zone. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Dns_Status'>SoftLayer_Dns_Status </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#errorMessageCount" name=errorMessageCount>errorMessageCount</a>
            </span>
            <div class='views-field-body'>A count of the error messages created during secondary DNS record transfer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


