---
title: "SoftLayer_Brand"
description: "The SoftLayer_Brand data type contains brand information relating to the single SoftLayer customer account. 

SoftLayer... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Brand"
classes:
    - "SoftLayer_Brand"
---

# SoftLayer_Brand
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Brand' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Brand' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Brand data type contains brand information relating to the single SoftLayer customer account. 

SoftLayer customers are unable to change their brand information in the portal or the API. 
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
            <span class='views-field-title'><a href="#catalogId" name=catalogId>catalogId</a></span>
            <div class='views-field-body'>ID of the Catalog used by this Brand </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#keyName" name=keyName>keyName</a></span>
            <div class='views-field-body'>The brand key name. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#longName" name=longName>longName</a></span>
            <div class='views-field-body'>The brand long name. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>The brand name. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#allOwnedAccounts" name=allOwnedAccounts>allOwnedAccounts</a></span>
            <div class='views-field-body'>All accounts owned by the brand. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#allowAccountCreationFlag" name=allowAccountCreationFlag>allowAccountCreationFlag</a></span>
            <div class='views-field-body'>This flag indicates if creation of accounts is allowed. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#businessPartner" name=businessPartner>businessPartner</a></span>
            <div class='views-field-body'>Business Partner details for the brand. Country Enterprise Code, Channel, Segment, Reseller Level. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Brand_Business_Partner'>SoftLayer_Brand_Business_Partner </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#businessPartnerFlag" name=businessPartnerFlag>businessPartnerFlag</a></span>
            <div class='views-field-body'>Flag indicating if the brand is a business partner. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#catalog" name=catalog>catalog</a></span>
            <div class='views-field-body'>The Product Catalog for the Brand </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Catalog'>SoftLayer_Product_Catalog </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#contacts" name=contacts>contacts</a></span>
            <div class='views-field-body'>The contacts for the brand. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Brand_Contact'>SoftLayer_Brand_Contact[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#customerCountryLocationRestrictions" name=customerCountryLocationRestrictions>customerCountryLocationRestrictions</a></span>
            <div class='views-field-body'>This references relationship between brands, locations and countries associated with a user's account that are ineligible when ordering products. For example, the India datacenter may not be available on this brand for customers that live in Great Britain. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Brand_Restriction_Location_CustomerCountry'>SoftLayer_Brand_Restriction_Location_CustomerCountry[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#distributor" name=distributor>distributor</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Brand'>SoftLayer_Brand </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#distributorChildFlag" name=distributorChildFlag>distributorChildFlag</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#distributorFlag" name=distributorFlag>distributorFlag</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardware" name=hardware>hardware</a></span>
            <div class='views-field-body'>An account's associated hardware objects. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hasAgentSupportFlag" name=hasAgentSupportFlag>hasAgentSupportFlag</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#openTickets" name=openTickets>openTickets</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ownedAccounts" name=ownedAccounts>ownedAccounts</a></span>
            <div class='views-field-body'>Active accounts owned by the brand. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ticketGroups" name=ticketGroups>ticketGroups</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Ticket_Group'>SoftLayer_Ticket_Group[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#tickets" name=tickets>tickets</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#users" name=users>users</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#virtualGuests" name=virtualGuests>virtualGuests</a></span>
            <div class='views-field-body'>An account's associated virtual guest objects. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a></p></div>
        </div>
            </div>
</div>


