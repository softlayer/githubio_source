---
title: "SoftLayer_Brand"
description: "The SoftLayer_Brand data type contains brand information relating to the single SoftLayer customer account. 

IBM Cloud... "
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

IBM Cloud Infrastructure customers are unable to change their brand information in the portal or the API. 





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
[catalogId]: #catalogid
#### [catalogId]
ID of the Catalog used by this Brand  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[keyName]: #keyname
#### [keyName]
The brand key name.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[longName]: #longname
#### [longName]
The brand long name.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The brand name.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[allOwnedAccounts]: #allownedaccounts
#### [allOwnedAccounts]
All accounts owned by the brand.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account[] </a>**  



</div>
<div class="prop-row">

-----
[allowAccountCreationFlag]: #allowaccountcreationflag
#### [allowAccountCreationFlag]
This flag indicates if creation of accounts is allowed.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[businessPartner]: #businesspartner
#### [businessPartner]
Business Partner details for the brand. Country Enterprise Code, Channel, Segment, Reseller Level.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand_Business_Partner'>SoftLayer_Brand_Business_Partner </a>**  



</div>
<div class="prop-row">

-----
[businessPartnerFlag]: #businesspartnerflag
#### [businessPartnerFlag]
Flag indicating if the brand is a business partner.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[catalog]: #catalog
#### [catalog]
The Product Catalog for the Brand  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Catalog'>SoftLayer_Product_Catalog </a>**  



</div>
<div class="prop-row">

-----
[contacts]: #contacts
#### [contacts]
The contacts for the brand.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand_Contact'>SoftLayer_Brand_Contact[] </a>**  



</div>
<div class="prop-row">

-----
[customerCountryLocationRestrictions]: #customercountrylocationrestrictions
#### [customerCountryLocationRestrictions]
This references relationship between brands, locations and countries associated with a user's account that are ineligible when ordering products. For example, the India datacenter may not be available on this brand for customers that live in Great Britain.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand_Restriction_Location_CustomerCountry'>SoftLayer_Brand_Restriction_Location_CustomerCountry[] </a>**  



</div>
<div class="prop-row">

-----
[distributor]: #distributor
#### [distributor]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand'>SoftLayer_Brand </a>**  



</div>
<div class="prop-row">

-----
[distributorChildFlag]: #distributorchildflag
#### [distributorChildFlag]
  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[distributorFlag]: #distributorflag
#### [distributorFlag]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
An account's associated hardware objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**  



</div>
<div class="prop-row">

-----
[hasAgentAdvancedSupportFlag]: #hasagentadvancedsupportflag
#### [hasAgentAdvancedSupportFlag]
  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[hasAgentSupportFlag]: #hasagentsupportflag
#### [hasAgentSupportFlag]
  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[openTickets]: #opentickets
#### [openTickets]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**  



</div>
<div class="prop-row">

-----
[ownedAccounts]: #ownedaccounts
#### [ownedAccounts]
Active accounts owned by the brand.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account[] </a>**  



</div>
<div class="prop-row">

-----
[securityLevel]: #securitylevel
#### [securityLevel]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Level'>SoftLayer_Security_Level </a>**  



</div>
<div class="prop-row">

-----
[ticketGroups]: #ticketgroups
#### [ticketGroups]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Group'>SoftLayer_Ticket_Group[] </a>**  



</div>
<div class="prop-row">

-----
[tickets]: #tickets
#### [tickets]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**  



</div>
<div class="prop-row">

-----
[users]: #users
#### [users]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer[] </a>**  



</div>
<div class="prop-row">

-----
[virtualGuests]: #virtualguests
#### [virtualGuests]
An account's associated virtual guest objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[allOwnedAccountCount]: #allownedaccountcount
#### [allOwnedAccountCount]
A count of all accounts owned by the brand.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[contactCount]: #contactcount
#### [contactCount]
A count of the contacts for the brand.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[customerCountryLocationRestrictionCount]: #customercountrylocationrestrictioncount
#### [customerCountryLocationRestrictionCount]
A count of this references relationship between brands, locations and countries associated with a user's account that are ineligible when ordering products. For example, the India datacenter may not be available on this brand for customers that live in Great Britain.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[hardwareCount]: #hardwarecount
#### [hardwareCount]
A count of an account's associated hardware objects.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[openTicketCount]: #openticketcount
#### [openTicketCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[ownedAccountCount]: #ownedaccountcount
#### [ownedAccountCount]
A count of active accounts owned by the brand.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[ticketCount]: #ticketcount
#### [ticketCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[ticketGroupCount]: #ticketgroupcount
#### [ticketGroupCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[userCount]: #usercount
#### [userCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[virtualGuestCount]: #virtualguestcount
#### [virtualGuestCount]
A count of an account's associated virtual guest objects.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


