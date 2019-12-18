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

## Local
-----
[catalogId]: #catalogid
#### [catalogId]
ID of the Catalog used by this Brand  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**

-----
[keyName]: #keyname
#### [keyName]
The brand key name.  
<span class="type-label">Type: </span>**string**

-----
[longName]: #longname
#### [longName]
The brand long name.  
<span class="type-label">Type: </span>**string**

-----
[name]: #name
#### [name]
The brand name.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[allOwnedAccounts]: #allownedaccounts
#### [allOwnedAccounts]
All accounts owned by the brand.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account[] </a>**

-----
[allowAccountCreationFlag]: #allowaccountcreationflag
#### [allowAccountCreationFlag]
This flag indicates if creation of accounts is allowed.  
<span class="type-label">Type: </span>**boolean**

-----
[businessPartner]: #businesspartner
#### [businessPartner]
Business Partner details for the brand. Country Enterprise Code, Channel, Segment, Reseller Level.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand_Business_Partner'>SoftLayer_Brand_Business_Partner </a>**

-----
[businessPartnerFlag]: #businesspartnerflag
#### [businessPartnerFlag]
Flag indicating if the brand is a business partner.  
<span class="type-label">Type: </span>**boolean**

-----
[catalog]: #catalog
#### [catalog]
The Product Catalog for the Brand  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Catalog'>SoftLayer_Product_Catalog </a>**

-----
[contacts]: #contacts
#### [contacts]
The contacts for the brand.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand_Contact'>SoftLayer_Brand_Contact[] </a>**

-----
[customerCountryLocationRestrictions]: #customercountrylocationrestrictions
#### [customerCountryLocationRestrictions]
This references relationship between brands, locations and countries associated with a user's account that are ineligible when ordering products. For example, the India datacenter may not be available on this brand for customers that live in Great Britain.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand_Restriction_Location_CustomerCountry'>SoftLayer_Brand_Restriction_Location_CustomerCountry[] </a>**

-----
[distributor]: #distributor
#### [distributor]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand'>SoftLayer_Brand </a>**

-----
[distributorChildFlag]: #distributorchildflag
#### [distributorChildFlag]
  
<span class="type-label">Type: </span>**boolean**

-----
[distributorFlag]: #distributorflag
#### [distributorFlag]
  
<span class="type-label">Type: </span>**string**

-----
[hardware]: #hardware
#### [hardware]
An account's associated hardware objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[hasAgentAdvancedSupportFlag]: #hasagentadvancedsupportflag
#### [hasAgentAdvancedSupportFlag]
  
<span class="type-label">Type: </span>**boolean**

-----
[hasAgentSupportFlag]: #hasagentsupportflag
#### [hasAgentSupportFlag]
  
<span class="type-label">Type: </span>**boolean**

-----
[openTickets]: #opentickets
#### [openTickets]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**

-----
[ownedAccounts]: #ownedaccounts
#### [ownedAccounts]
Active accounts owned by the brand.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account[] </a>**

-----
[securityLevel]: #securitylevel
#### [securityLevel]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Level'>SoftLayer_Security_Level </a>**

-----
[ticketGroups]: #ticketgroups
#### [ticketGroups]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Group'>SoftLayer_Ticket_Group[] </a>**

-----
[tickets]: #tickets
#### [tickets]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**

-----
[users]: #users
#### [users]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer[] </a>**

-----
[virtualGuests]: #virtualguests
#### [virtualGuests]
An account's associated virtual guest objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


## Count

-----
[allOwnedAccountCount]: #allownedaccountcount
#### [allOwnedAccountCount]
A count of all accounts owned by the brand.   
<span class="type-label">Type: </span>**unsigned long**


-----
[contactCount]: #contactcount
#### [contactCount]
A count of the contacts for the brand.   
<span class="type-label">Type: </span>**unsigned long**


-----
[customerCountryLocationRestrictionCount]: #customercountrylocationrestrictioncount
#### [customerCountryLocationRestrictionCount]
A count of this references relationship between brands, locations and countries associated with a user's account that are ineligible when ordering products. For example, the India datacenter may not be available on this brand for customers that live in Great Britain.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hardwareCount]: #hardwarecount
#### [hardwareCount]
A count of an account's associated hardware objects.   
<span class="type-label">Type: </span>**unsigned long**


-----
[openTicketCount]: #openticketcount
#### [openTicketCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[ownedAccountCount]: #ownedaccountcount
#### [ownedAccountCount]
A count of active accounts owned by the brand.   
<span class="type-label">Type: </span>**unsigned long**


-----
[ticketCount]: #ticketcount
#### [ticketCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[ticketGroupCount]: #ticketgroupcount
#### [ticketGroupCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[userCount]: #usercount
#### [userCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualGuestCount]: #virtualguestcount
#### [virtualGuestCount]
A count of an account's associated virtual guest objects.   
<span class="type-label">Type: </span>**unsigned long**

</div>


