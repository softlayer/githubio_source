---
title: "SoftLayer_Dns_Secondary"
description: "SoftLayer's secondary DNS service allows you to use SoftLayer's name servers as a secondary server to your domain's name... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
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
SoftLayer's secondary DNS service allows you to use SoftLayer's name servers as a secondary server to your domain's name servers. This is accomplished through the use of zone transfers. Each record created within the secondary DNS service defines which zone is transferred, what server it is transferred from, and the frequency that zone transfers occur at. Zone transfers are performed automatically based on the transfer frequency set on the secondary DNS record. Domains created via zone transfer may not be modified by the SoftLayer portal or API. 

The secondary DNS service also provides the ability to manually initiate a zone transfer through the [[SoftLayer_Dns_Secondary::transferNow]] method. The daemon that performs zone transfers runs once a minute, therefore it could take a full minute for the zone transfer to be completed. 

Secondary DNS transfers may periodically generate notification or error messages. Please use the [[SoftLayer_Dns_Message]] service to retrieve these notifications. 

### External Links


* [DNS Zone Transfer at Wikipedia.](http://en.wikipedia.org/wiki/DNS_zone_transfer)


* [Secondary Domains at KnowledgeLayer](http://knowledgelayer.softlayer.com/questions/478)




### seeAlso

* [SoftLayer_Dns_Domain](/reference/services/SoftLayer_Dns_Domain )


* [SoftLayer_Dns_Message](/reference/datatypes/SoftLayer_Dns_Message )


        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Secondary/convertToPrimary'> convertToPrimary</a> </span>
            <div class='views-field-body'>Convert a secondary DNS record into a primary DNS record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Secondary/createObject'> createObject</a> </span>
            <div class='views-field-body'>Create a secondary DNS record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Secondary/createObjects'> createObjects</a> </span>
            <div class='views-field-body'>Create multiple secondary DNS records.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Secondary/deleteObject'> deleteObject</a> </span>
            <div class='views-field-body'>Delete a secondary DNS record</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Secondary/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit a secondary DNS record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Secondary/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer account that owns a secondary DNS record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Secondary/getByDomainName'> getByDomainName</a> </span>
            <div class='views-field-body'>Search for secondary domains by name.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Secondary/getDomain'> getDomain</a> </span>
            <div class='views-field-body'>Retrieve the domain record created by zone transfer from a secondary DNS record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Secondary/getErrorMessages'> getErrorMessages</a> </span>
            <div class='views-field-body'>Retrieve the error messages created during secondary DNS record transfer.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Secondary/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Dns_Secondary record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Secondary/getStatus'> getStatus</a> </span>
            <div class='views-field-body'>Retrieve the current status of the secondary DNS zone.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Dns_Secondary/transferNow'> transferNow</a> </span>
            <div class='views-field-body'>Initiate a zone transfer for a secondary DNS record.</div>
        </div>
        </div>
</div>

