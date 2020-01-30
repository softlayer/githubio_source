---
title: "SoftLayer_Account"
description: "The SoftLayer_Account data type contains general information relating to a single SoftLayer customer account. Personal i... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
---

# SoftLayer_Account
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Account data type contains general information relating to a single SoftLayer customer account. Personal information in this type such as names, addresses, and phone numbers are assigned to the account only and not to users belonging to the account. The SoftLayer_Account data type contains a number of relational properties that are used by the SoftLayer customer portal to quickly present a variety of account related services to it's users. 

SoftLayer customers are unable to change their company account information in the portal or the API. If you need to change this information please open a sales ticket in our customer portal and our account management staff will assist you. 


### associatedMethods

*  [SoftLayer_Account::getObject](/reference/services/SoftLayer_Account/getObject )
*  [SoftLayer_Billing_Invoice::getAccount](/reference/services/SoftLayer_Billing_Invoice/getAccount )





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
[accountManagedResourcesFlag]: #accountmanagedresourcesflag
#### [accountManagedResourcesFlag]
A flag indicating that the account has a managed resource.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[accountStatusId]: #accountstatusid
#### [accountStatusId]
A number reflecting the state of an account.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[address1]: #address1
#### [address1]
The first line of the mailing address belonging to an account.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[address2]: #address2
#### [address2]
The second line of the mailing address belonging to an account.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[allowedPptpVpnQuantity]: #allowedpptpvpnquantity
#### [allowedPptpVpnQuantity]
The number of PPTP VPN users allowed on an account.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[alternatePhone]: #alternatephone
#### [alternatePhone]
A secondary phone number assigned to an account.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[brandId]: #brandid
#### [brandId]
The Brand tied to an account.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[city]: #city
#### [city]
The city of the mailing address belonging to an account.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[claimedTaxExemptTxFlag]: #claimedtaxexempttxflag
#### [claimedTaxExemptTxFlag]
Whether an account is exempt from taxes on their invoices.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[companyName]: #companyname
#### [companyName]
The company name associated with an account.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[country]: #country
#### [country]
A two-letter abbreviation of the country in the mailing address belonging to an account.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date an account was created.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[deviceFingerprintId]: #devicefingerprintid
#### [deviceFingerprintId]
Device Fingerprint Identifier - Used internally and can safely be ignored.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[email]: #email
#### [email]
A general email address assigned to an account.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[faxPhone]: #faxphone
#### [faxPhone]
A fax phone number assigned to an account.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[firstName]: #firstname
#### [firstName]
Each customer account is listed under a single individual. This is that individual's first name.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A customer account's internal identifier. Account numbers are typically preceded by the string "SL" in the customer portal. Every SoftLayer account has at least one portal user whose username follows the "SL" + account number naming scheme.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[isReseller]: #isreseller
#### [isReseller]
A flag indicating if an account belongs to a reseller or not.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[lastName]: #lastname
#### [lastName]
Each customer account is listed under a single individual. This is that individual's last name.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[lateFeeProtectionFlag]: #latefeeprotectionflag
#### [lateFeeProtectionFlag]
Whether an account has late fee protection.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date an account was last modified.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[officePhone]: #officephone
#### [officePhone]
An office phone number assigned to an account.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[postalCode]: #postalcode
#### [postalCode]
The postal code of the mailing address belonging to an account.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[resellerLevel]: #resellerlevel
#### [resellerLevel]
The Reseller level of the account.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[state]: #state
#### [state]
A two-letter abbreviation of the state in the mailing address belonging to an account. If an account does not reside in a province then this is typically blank.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[statusDate]: #statusdate
#### [statusDate]
The date of an account's last status change.  
<span class="type-label">Type: </span>**dateTime**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[abuseEmail]: #abuseemail
#### [abuseEmail]
An email address that is responsible for abuse and legal inquiries on behalf of an account. For instance, new legal and abuse tickets are sent to this address.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[abuseEmails]: #abuseemails
#### [abuseEmails]
Email addresses that are responsible for abuse and legal inquiries on behalf of an account. For instance, new legal and abuse tickets are sent to these addresses.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_AbuseEmail'>SoftLayer_Account_AbuseEmail[] </a>**


</div>
<div class="prop-row">

-----
[accountContacts]: #accountcontacts
#### [accountContacts]
The account contacts on an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Contact'>SoftLayer_Account_Contact[] </a>**


</div>
<div class="prop-row">

-----
[accountLicenses]: #accountlicenses
#### [accountLicenses]
The account software licenses owned by an account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_AccountLicense'>SoftLayer_Software_AccountLicense[] </a>**


</div>
<div class="prop-row">

-----
[accountLinks]: #accountlinks
#### [accountLinks]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Link'>SoftLayer_Account_Link[] </a>**


</div>
<div class="prop-row">

-----
[accountStatus]: #accountstatus
#### [accountStatus]
An account's status presented in a more detailed data type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Status'>SoftLayer_Account_Status </a>**


</div>
<div class="prop-row">

-----
[activeAccountDiscountBillingItem]: #activeaccountdiscountbillingitem
#### [activeAccountDiscountBillingItem]
The billing item associated with an account's monthly discount.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**


</div>
<div class="prop-row">

-----
[activeAccountLicenses]: #activeaccountlicenses
#### [activeAccountLicenses]
The active account software licenses owned by an account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_AccountLicense'>SoftLayer_Software_AccountLicense[] </a>**


</div>
<div class="prop-row">

-----
[activeAddresses]: #activeaddresses
#### [activeAddresses]
The active address(es) that belong to an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Address'>SoftLayer_Account_Address[] </a>**


</div>
<div class="prop-row">

-----
[activeAgreements]: #activeagreements
#### [activeAgreements]
All active agreements for an account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Agreement'>SoftLayer_Account_Agreement[] </a>**


</div>
<div class="prop-row">

-----
[activeBillingAgreements]: #activebillingagreements
#### [activeBillingAgreements]
All billing agreements for an account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Agreement'>SoftLayer_Account_Agreement[] </a>**


</div>
<div class="prop-row">

-----
[activeCatalystEnrollment]: #activecatalystenrollment
#### [activeCatalystEnrollment]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Catalyst_Enrollment'>SoftLayer_Catalyst_Enrollment </a>**


</div>
<div class="prop-row">

-----
[activeColocationContainers]: #activecolocationcontainers
#### [activeColocationContainers]
The account's active top level colocation containers.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[activeFlexibleCreditEnrollment]: #activeflexiblecreditenrollment
#### [activeFlexibleCreditEnrollment]
[Deprecated] Please use SoftLayer_Account::activeFlexibleCreditEnrollments.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_FlexibleCredit_Enrollment'>SoftLayer_FlexibleCredit_Enrollment </a>**


</div>
<div class="prop-row">

-----
[activeFlexibleCreditEnrollments]: #activeflexiblecreditenrollments
#### [activeFlexibleCreditEnrollments]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_FlexibleCredit_Enrollment'>SoftLayer_FlexibleCredit_Enrollment[] </a>**


</div>
<div class="prop-row">

-----
[activeNotificationSubscribers]: #activenotificationsubscribers
#### [activeNotificationSubscribers]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Subscriber'>SoftLayer_Notification_Subscriber[] </a>**


</div>
<div class="prop-row">

-----
[activeQuotes]: #activequotes
#### [activeQuotes]
An account's non-expired quotes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Quote'>SoftLayer_Billing_Order_Quote[] </a>**


</div>
<div class="prop-row">

-----
[activeReservedCapacityAgreements]: #activereservedcapacityagreements
#### [activeReservedCapacityAgreements]
Active reserved capacity agreements for an account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Agreement'>SoftLayer_Account_Agreement[] </a>**


</div>
<div class="prop-row">

-----
[activeVirtualLicenses]: #activevirtuallicenses
#### [activeVirtualLicenses]
The virtual software licenses controlled by an account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_VirtualLicense'>SoftLayer_Software_VirtualLicense[] </a>**


</div>
<div class="prop-row">

-----
[adcLoadBalancers]: #adcloadbalancers
#### [adcLoadBalancers]
An account's associated load balancers.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress[] </a>**


</div>
<div class="prop-row">

-----
[addresses]: #addresses
#### [addresses]
All the address(es) that belong to an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Address'>SoftLayer_Account_Address[] </a>**


</div>
<div class="prop-row">

-----
[affiliateId]: #affiliateid
#### [affiliateId]
An affiliate identifier associated with the customer account.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[allBillingItems]: #allbillingitems
#### [allBillingItems]
The billing items that will be on an account's next invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[allCommissionBillingItems]: #allcommissionbillingitems
#### [allCommissionBillingItems]
The billing items that will be on an account's next invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[allRecurringTopLevelBillingItems]: #allrecurringtoplevelbillingitems
#### [allRecurringTopLevelBillingItems]
The billing items that will be on an account's next invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[allRecurringTopLevelBillingItemsUnfiltered]: #allrecurringtoplevelbillingitemsunfiltered
#### [allRecurringTopLevelBillingItemsUnfiltered]
The billing items that will be on an account's next invoice. Does not consider associated items.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[allSubnetBillingItems]: #allsubnetbillingitems
#### [allSubnetBillingItems]
The billing items that will be on an account's next invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[allTopLevelBillingItems]: #alltoplevelbillingitems
#### [allTopLevelBillingItems]
All billing items of an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[allTopLevelBillingItemsUnfiltered]: #alltoplevelbillingitemsunfiltered
#### [allTopLevelBillingItemsUnfiltered]
The billing items that will be on an account's next invoice. Does not consider associated items.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[allowIbmIdSilentMigrationFlag]: #allowibmidsilentmigrationflag
#### [allowIbmIdSilentMigrationFlag]
Indicates whether this account is allowed to silently migrate to use IBMid Authentication.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[allowsBluemixAccountLinkingFlag]: #allowsbluemixaccountlinkingflag
#### [allowsBluemixAccountLinkingFlag]
Flag indicating if this account can be linked with Bluemix.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[applicationDeliveryControllers]: #applicationdeliverycontrollers
#### [applicationDeliveryControllers]
An account's associated application delivery controller records.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller'>SoftLayer_Network_Application_Delivery_Controller[] </a>**


</div>
<div class="prop-row">

-----
[attributes]: #attributes
#### [attributes]
The account attribute values for a SoftLayer customer account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Attribute'>SoftLayer_Account_Attribute[] </a>**


</div>
<div class="prop-row">

-----
[availablePublicNetworkVlans]: #availablepublicnetworkvlans
#### [availablePublicNetworkVlans]
The public network VLANs assigned to an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a>**


</div>
<div class="prop-row">

-----
[balance]: #balance
#### [balance]
The account balance of a SoftLayer customer account. An account's balance is the amount of money owed to SoftLayer by the account holder, returned as a floating point number with two decimal places, measured in US Dollars ($USD). A negative account balance means the account holder has overpaid and is owed money by SoftLayer.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[bandwidthAllotments]: #bandwidthallotments
#### [bandwidthAllotments]
The bandwidth allotments for an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment[] </a>**


</div>
<div class="prop-row">

-----
[bandwidthAllotmentsOverAllocation]: #bandwidthallotmentsoverallocation
#### [bandwidthAllotmentsOverAllocation]
The bandwidth allotments for an account currently over allocation.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment[] </a>**


</div>
<div class="prop-row">

-----
[bandwidthAllotmentsProjectedOverAllocation]: #bandwidthallotmentsprojectedoverallocation
#### [bandwidthAllotmentsProjectedOverAllocation]
The bandwidth allotments for an account projected to go over allocation.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment[] </a>**


</div>
<div class="prop-row">

-----
[bareMetalInstances]: #baremetalinstances
#### [bareMetalInstances]
An account's associated bare metal server objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[billingAgreements]: #billingagreements
#### [billingAgreements]
All billing agreements for an account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Agreement'>SoftLayer_Account_Agreement[] </a>**


</div>
<div class="prop-row">

-----
[billingInfo]: #billinginfo
#### [billingInfo]
An account's billing information.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Info'>SoftLayer_Billing_Info </a>**


</div>
<div class="prop-row">

-----
[blockDeviceTemplateGroups]: #blockdevicetemplategroups
#### [blockDeviceTemplateGroups]
Private template group objects (parent and children) and the shared template group objects (parent only) for an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group'>SoftLayer_Virtual_Guest_Block_Device_Template_Group[] </a>**


</div>
<div class="prop-row">

-----
[bluemixAccountLink]: #bluemixaccountlink
#### [bluemixAccountLink]
The Bluemix account link associated with this SoftLayer account, if one exists.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Link_Bluemix'>SoftLayer_Account_Link_Bluemix </a>**


</div>
<div class="prop-row">

-----
[bluemixLinkedFlag]: #bluemixlinkedflag
#### [bluemixLinkedFlag]
Returns true if this account is linked to IBM Bluemix, false if not.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[brand]: #brand
#### [brand]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand'>SoftLayer_Brand </a>**


</div>
<div class="prop-row">

-----
[brandAccountFlag]: #brandaccountflag
#### [brandAccountFlag]
  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[brandKeyName]: #brandkeyname
#### [brandKeyName]
The brand keyName.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[businessPartner]: #businesspartner
#### [businessPartner]
The Business Partner details for the account. Country Enterprise Code, Channel, Segment, Reseller Level.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Business_Partner'>SoftLayer_Account_Business_Partner </a>**


</div>
<div class="prop-row">

-----
[canOrderAdditionalVlansFlag]: #canorderadditionalvlansflag
#### [canOrderAdditionalVlansFlag]
[DEPRECATED] All accounts may order VLANs.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[carts]: #carts
#### [carts]
An account's active carts.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Quote'>SoftLayer_Billing_Order_Quote[] </a>**


</div>
<div class="prop-row">

-----
[catalystEnrollments]: #catalystenrollments
#### [catalystEnrollments]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Catalyst_Enrollment'>SoftLayer_Catalyst_Enrollment[] </a>**


</div>
<div class="prop-row">

-----
[closedTickets]: #closedtickets
#### [closedTickets]
All closed tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[datacentersWithSubnetAllocations]: #datacenterswithsubnetallocations
#### [datacentersWithSubnetAllocations]
Datacenters which contain subnets that the account has access to route.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location[] </a>**


</div>
<div class="prop-row">

-----
[dedicatedHosts]: #dedicatedhosts
#### [dedicatedHosts]
An account's associated virtual dedicated host objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_DedicatedHost'>SoftLayer_Virtual_DedicatedHost[] </a>**


</div>
<div class="prop-row">

-----
[disablePaymentProcessingFlag]: #disablepaymentprocessingflag
#### [disablePaymentProcessingFlag]
A flag indicating whether payments are processed for this account.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[displaySupportRepresentativeAssignments]: #displaysupportrepresentativeassignments
#### [displaySupportRepresentativeAssignments]
The SoftLayer employees that an account is assigned to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Attachment_Employee'>SoftLayer_Account_Attachment_Employee[] </a>**


</div>
<div class="prop-row">

-----
[domainRegistrations]: #domainregistrations
#### [domainRegistrations]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Domain_Registration'>SoftLayer_Dns_Domain_Registration[] </a>**


</div>
<div class="prop-row">

-----
[domains]: #domains
#### [domains]
The DNS domains associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Domain'>SoftLayer_Dns_Domain[] </a>**


</div>
<div class="prop-row">

-----
[domainsWithoutSecondaryDnsRecords]: #domainswithoutsecondarydnsrecords
#### [domainsWithoutSecondaryDnsRecords]
The DNS domains associated with an account that were not created as a result of a secondary DNS zone transfer.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Domain'>SoftLayer_Dns_Domain[] </a>**


</div>
<div class="prop-row">

-----
[euSupportedFlag]: #eusupportedflag
#### [euSupportedFlag]
Boolean flag dictating whether or not this account has the EU Supported flag. This flag indicates that this account uses IBM Cloud services to process EU citizen's personal data.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[evaultCapacityGB]: #evaultcapacitygb
#### [evaultCapacityGB]
The total capacity of Legacy EVault Volumes on an account, in GB.  
<span class="type-label">Type: </span>**unsigned integer**


</div>
<div class="prop-row">

-----
[evaultMasterUsers]: #evaultmasterusers
#### [evaultMasterUsers]
An account's master EVault user. This is only used when an account has EVault service.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Password'>SoftLayer_Account_Password[] </a>**


</div>
<div class="prop-row">

-----
[evaultNetworkStorage]: #evaultnetworkstorage
#### [evaultNetworkStorage]
An account's associated EVault storage volumes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[expiredSecurityCertificates]: #expiredsecuritycertificates
#### [expiredSecurityCertificates]
Stored security certificates that are expired (ie. SSL)  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Certificate'>SoftLayer_Security_Certificate[] </a>**


</div>
<div class="prop-row">

-----
[facilityLogs]: #facilitylogs
#### [facilityLogs]
Logs of who entered a colocation area which is assigned to this account, or when a user under this account enters a datacenter.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Access_Facility_Log'>SoftLayer_User_Access_Facility_Log[] </a>**


</div>
<div class="prop-row">

-----
[fileBlockBetaAccessFlag]: #fileblockbetaaccessflag
#### [fileBlockBetaAccessFlag]
  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[flexibleCreditEnrollments]: #flexiblecreditenrollments
#### [flexibleCreditEnrollments]
All of the account's current and former Flexible Credit enrollments.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_FlexibleCredit_Enrollment'>SoftLayer_FlexibleCredit_Enrollment[] </a>**


</div>
<div class="prop-row">

-----
[forcePaasAccountLinkDate]: #forcepaasaccountlinkdate
#### [forcePaasAccountLinkDate]
Timestamp representing the point in time when an account is required to link with PaaS.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[globalIpRecords]: #globaliprecords
#### [globalIpRecords]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress_Global'>SoftLayer_Network_Subnet_IpAddress_Global[] </a>**


</div>
<div class="prop-row">

-----
[globalIpv4Records]: #globalipv4records
#### [globalIpv4Records]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress_Global'>SoftLayer_Network_Subnet_IpAddress_Global[] </a>**


</div>
<div class="prop-row">

-----
[globalIpv6Records]: #globalipv6records
#### [globalIpv6Records]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress_Global'>SoftLayer_Network_Subnet_IpAddress_Global[] </a>**


</div>
<div class="prop-row">

-----
[globalLoadBalancerAccounts]: #globalloadbalanceraccounts
#### [globalLoadBalancerAccounts]
The global load balancer accounts for a softlayer customer account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Global_Account'>SoftLayer_Network_LoadBalancer_Global_Account[] </a>**


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
[hardwareOverBandwidthAllocation]: #hardwareoverbandwidthallocation
#### [hardwareOverBandwidthAllocation]
An account's associated hardware objects currently over bandwidth allocation.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[hardwareProjectedOverBandwidthAllocation]: #hardwareprojectedoverbandwidthallocation
#### [hardwareProjectedOverBandwidthAllocation]
An account's associated hardware objects projected to go over bandwidth allocation.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[hardwareWithCpanel]: #hardwarewithcpanel
#### [hardwareWithCpanel]
All hardware associated with an account that has the cPanel web hosting control panel installed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[hardwareWithHelm]: #hardwarewithhelm
#### [hardwareWithHelm]
All hardware associated with an account that has the Helm web hosting control panel installed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[hardwareWithMcafee]: #hardwarewithmcafee
#### [hardwareWithMcafee]
All hardware associated with an account that has McAfee Secure software components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[hardwareWithMcafeeAntivirusRedhat]: #hardwarewithmcafeeantivirusredhat
#### [hardwareWithMcafeeAntivirusRedhat]
All hardware associated with an account that has McAfee Secure AntiVirus for Redhat software components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[hardwareWithMcafeeAntivirusWindows]: #hardwarewithmcafeeantiviruswindows
#### [hardwareWithMcafeeAntivirusWindows]
All hardware associated with an account that has McAfee Secure AntiVirus for Windows software components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[hardwareWithMcafeeIntrusionDetectionSystem]: #hardwarewithmcafeeintrusiondetectionsystem
#### [hardwareWithMcafeeIntrusionDetectionSystem]
All hardware associated with an account that has McAfee Secure Intrusion Detection System software components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[hardwareWithPlesk]: #hardwarewithplesk
#### [hardwareWithPlesk]
All hardware associated with an account that has the Plesk web hosting control panel installed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[hardwareWithQuantastor]: #hardwarewithquantastor
#### [hardwareWithQuantastor]
All hardware associated with an account that has the QuantaStor storage system installed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[hardwareWithUrchin]: #hardwarewithurchin
#### [hardwareWithUrchin]
All hardware associated with an account that has the Urchin web traffic analytics package installed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[hardwareWithWindows]: #hardwarewithwindows
#### [hardwareWithWindows]
All hardware associated with an account that is running a version of the Microsoft Windows operating system.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[hasEvaultBareMetalRestorePluginFlag]: #hasevaultbaremetalrestorepluginflag
#### [hasEvaultBareMetalRestorePluginFlag]
Return 1 if one of the account's hardware has the EVault Bare Metal Server Restore Plugin otherwise 0.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[hasIderaBareMetalRestorePluginFlag]: #hasiderabaremetalrestorepluginflag
#### [hasIderaBareMetalRestorePluginFlag]
Return 1 if one of the account's hardware has an installation of Idera Server Backup otherwise 0.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[hasPendingOrder]: #haspendingorder
#### [hasPendingOrder]
The number of orders in a PENDING status for a SoftLayer customer account.  
<span class="type-label">Type: </span>**unsigned integer**


</div>
<div class="prop-row">

-----
[hasR1softBareMetalRestorePluginFlag]: #hasr1softbaremetalrestorepluginflag
#### [hasR1softBareMetalRestorePluginFlag]
Return 1 if one of the account's hardware has an installation of R1Soft CDP otherwise 0.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[hourlyBareMetalInstances]: #hourlybaremetalinstances
#### [hourlyBareMetalInstances]
An account's associated hourly bare metal server objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[hourlyServiceBillingItems]: #hourlyservicebillingitems
#### [hourlyServiceBillingItems]
Hourly service billing items that will be on an account's next invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[hourlyVirtualGuests]: #hourlyvirtualguests
#### [hourlyVirtualGuests]
An account's associated hourly virtual guest objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[hubNetworkStorage]: #hubnetworkstorage
#### [hubNetworkStorage]
An account's associated Virtual Storage volumes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[ibmCustomerNumber]: #ibmcustomernumber
#### [ibmCustomerNumber]
Unique identifier for a customer used throughout IBM.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[ibmIdAuthenticationRequiredFlag]: #ibmidauthenticationrequiredflag
#### [ibmIdAuthenticationRequiredFlag]
Indicates whether this account requires IBMid authentication.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[ibmIdMigrationExpirationTimestamp]: #ibmidmigrationexpirationtimestamp
#### [ibmIdMigrationExpirationTimestamp]
This key is deprecated and should not be used.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[inProgressExternalAccountSetup]: #inprogressexternalaccountsetup
#### [inProgressExternalAccountSetup]
An in progress request to switch billing systems.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_External_Setup'>SoftLayer_Account_External_Setup </a>**


</div>
<div class="prop-row">

-----
[internalNotes]: #internalnotes
#### [internalNotes]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Note'>SoftLayer_Account_Note[] </a>**


</div>
<div class="prop-row">

-----
[invoices]: #invoices
#### [invoices]
An account's associated billing invoices.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice[] </a>**


</div>
<div class="prop-row">

-----
[ipAddresses]: #ipaddresses
#### [ipAddresses]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>**


</div>
<div class="prop-row">

-----
[iscsiIsolationDisabled]: #iscsiisolationdisabled
#### [iscsiIsolationDisabled]
  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[iscsiNetworkStorage]: #iscsinetworkstorage
#### [iscsiNetworkStorage]
An account's associated iSCSI storage volumes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[lastCanceledBillingItem]: #lastcanceledbillingitem
#### [lastCanceledBillingItem]
The most recently canceled billing item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**


</div>
<div class="prop-row">

-----
[lastCancelledServerBillingItem]: #lastcancelledserverbillingitem
#### [lastCancelledServerBillingItem]
The most recent cancelled server billing item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**


</div>
<div class="prop-row">

-----
[lastFiveClosedAbuseTickets]: #lastfiveclosedabusetickets
#### [lastFiveClosedAbuseTickets]
The five most recently closed abuse tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[lastFiveClosedAccountingTickets]: #lastfiveclosedaccountingtickets
#### [lastFiveClosedAccountingTickets]
The five most recently closed accounting tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[lastFiveClosedOtherTickets]: #lastfiveclosedothertickets
#### [lastFiveClosedOtherTickets]
The five most recently closed tickets that do not belong to the abuse, accounting, sales, or support groups associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[lastFiveClosedSalesTickets]: #lastfiveclosedsalestickets
#### [lastFiveClosedSalesTickets]
The five most recently closed sales tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[lastFiveClosedSupportTickets]: #lastfiveclosedsupporttickets
#### [lastFiveClosedSupportTickets]
The five most recently closed support tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[lastFiveClosedTickets]: #lastfiveclosedtickets
#### [lastFiveClosedTickets]
The five most recently closed tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[latestBillDate]: #latestbilldate
#### [latestBillDate]
An account's most recent billing date.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[latestRecurringInvoice]: #latestrecurringinvoice
#### [latestRecurringInvoice]
An account's latest recurring invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice </a>**


</div>
<div class="prop-row">

-----
[latestRecurringPendingInvoice]: #latestrecurringpendinginvoice
#### [latestRecurringPendingInvoice]
An account's latest recurring pending invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice </a>**


</div>
<div class="prop-row">

-----
[legacyBandwidthAllotments]: #legacybandwidthallotments
#### [legacyBandwidthAllotments]
The legacy bandwidth allotments for an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment[] </a>**


</div>
<div class="prop-row">

-----
[legacyIscsiCapacityGB]: #legacyiscsicapacitygb
#### [legacyIscsiCapacityGB]
The total capacity of Legacy iSCSI Volumes on an account, in GB.  
<span class="type-label">Type: </span>**unsigned integer**


</div>
<div class="prop-row">

-----
[loadBalancers]: #loadbalancers
#### [loadBalancers]
An account's associated load balancers.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_LoadBalancer_VirtualIpAddress[] </a>**


</div>
<div class="prop-row">

-----
[lockboxCapacityGB]: #lockboxcapacitygb
#### [lockboxCapacityGB]
The total capacity of Legacy lockbox Volumes on an account, in GB.  
<span class="type-label">Type: </span>**unsigned integer**


</div>
<div class="prop-row">

-----
[lockboxNetworkStorage]: #lockboxnetworkstorage
#### [lockboxNetworkStorage]
An account's associated Lockbox storage volumes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[manualPaymentsUnderReview]: #manualpaymentsunderreview
#### [manualPaymentsUnderReview]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Payment_Card_ManualPayment'>SoftLayer_Billing_Payment_Card_ManualPayment[] </a>**


</div>
<div class="prop-row">

-----
[masterUser]: #masteruser
#### [masterUser]
An account's master user.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**


</div>
<div class="prop-row">

-----
[mediaDataTransferRequests]: #mediadatatransferrequests
#### [mediaDataTransferRequests]
An account's media transfer service requests.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Media_Data_Transfer_Request'>SoftLayer_Account_Media_Data_Transfer_Request[] </a>**


</div>
<div class="prop-row">

-----
[migratedToIbmCloudPortalFlag]: #migratedtoibmcloudportalflag
#### [migratedToIbmCloudPortalFlag]
Flag indicating whether this account is restricted to the IBM Cloud portal.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[monthlyBareMetalInstances]: #monthlybaremetalinstances
#### [monthlyBareMetalInstances]
An account's associated monthly bare metal server objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[monthlyVirtualGuests]: #monthlyvirtualguests
#### [monthlyVirtualGuests]
An account's associated monthly virtual guest objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[nasNetworkStorage]: #nasnetworkstorage
#### [nasNetworkStorage]
An account's associated NAS storage volumes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[networkCreationFlag]: #networkcreationflag
#### [networkCreationFlag]
[Deprecated] Whether or not this account can define their own networks.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[networkGateways]: #networkgateways
#### [networkGateways]
All network gateway devices on this account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway[] </a>**


</div>
<div class="prop-row">

-----
[networkHardware]: #networkhardware
#### [networkHardware]
An account's associated network hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[networkMessageDeliveryAccounts]: #networkmessagedeliveryaccounts
#### [networkMessageDeliveryAccounts]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Message_Delivery'>SoftLayer_Network_Message_Delivery[] </a>**


</div>
<div class="prop-row">

-----
[networkMonitorDownHardware]: #networkmonitordownhardware
#### [networkMonitorDownHardware]
Hardware which is currently experiencing a service failure.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[networkMonitorDownVirtualGuests]: #networkmonitordownvirtualguests
#### [networkMonitorDownVirtualGuests]
Virtual guest which is currently experiencing a service failure.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[networkMonitorRecoveringHardware]: #networkmonitorrecoveringhardware
#### [networkMonitorRecoveringHardware]
Hardware which is currently recovering from a service failure.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[networkMonitorRecoveringVirtualGuests]: #networkmonitorrecoveringvirtualguests
#### [networkMonitorRecoveringVirtualGuests]
Virtual guest which is currently recovering from a service failure.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[networkMonitorUpHardware]: #networkmonitoruphardware
#### [networkMonitorUpHardware]
Hardware which is currently online.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[networkMonitorUpVirtualGuests]: #networkmonitorupvirtualguests
#### [networkMonitorUpVirtualGuests]
Virtual guest which is currently online.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[networkStorage]: #networkstorage
#### [networkStorage]
An account's associated storage volumes. This includes Lockbox, NAS, EVault, and iSCSI volumes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[networkStorageGroups]: #networkstoragegroups
#### [networkStorageGroups]
An account's Network Storage groups.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Group'>SoftLayer_Network_Storage_Group[] </a>**


</div>
<div class="prop-row">

-----
[networkTunnelContexts]: #networktunnelcontexts
#### [networkTunnelContexts]
IPSec network tunnels for an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context'>SoftLayer_Network_Tunnel_Module_Context[] </a>**


</div>
<div class="prop-row">

-----
[networkVlanSpan]: #networkvlanspan
#### [networkVlanSpan]
Whether or not an account has automatic private VLAN spanning enabled.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Network_Vlan_Span'>SoftLayer_Account_Network_Vlan_Span </a>**


</div>
<div class="prop-row">

-----
[networkVlans]: #networkvlans
#### [networkVlans]
All network VLANs assigned to an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a>**


</div>
<div class="prop-row">

-----
[nextBillingPublicAllotmentHardwareBandwidthDetails]: #nextbillingpublicallotmenthardwarebandwidthdetails
#### [nextBillingPublicAllotmentHardwareBandwidthDetails]
DEPRECATED - This information can be pulled directly through tapping keys now - DEPRECATED. The allotments for this account and their servers for the next billing cycle. The public inbound and outbound bandwidth is calculated for each server in addition to the daily average network traffic since the last billing date.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment[] </a>**


</div>
<div class="prop-row">

-----
[nextInvoiceIncubatorExemptTotal]: #nextinvoiceincubatorexempttotal
#### [nextInvoiceIncubatorExemptTotal]
The pre-tax total amount exempt from incubator credit for the account's next invoice. This field is now deprecated and will soon be removed. Please update all references to instead use nextInvoiceTotalAmount  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[nextInvoiceRecurringAmountEligibleForAccountDiscount]: #nextinvoicerecurringamounteligibleforaccountdiscount
#### [nextInvoiceRecurringAmountEligibleForAccountDiscount]
The total recurring charge amount of an account's next invoice eligible for account discount measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[nextInvoiceTopLevelBillingItems]: #nextinvoicetoplevelbillingitems
#### [nextInvoiceTopLevelBillingItems]
The billing items that will be on an account's next invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[nextInvoiceTotalAmount]: #nextinvoicetotalamount
#### [nextInvoiceTotalAmount]
The pre-tax total amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[nextInvoiceTotalOneTimeAmount]: #nextinvoicetotalonetimeamount
#### [nextInvoiceTotalOneTimeAmount]
The total one-time charge amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[nextInvoiceTotalOneTimeTaxAmount]: #nextinvoicetotalonetimetaxamount
#### [nextInvoiceTotalOneTimeTaxAmount]
The total one-time tax amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[nextInvoiceTotalRecurringAmount]: #nextinvoicetotalrecurringamount
#### [nextInvoiceTotalRecurringAmount]
The total recurring charge amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[nextInvoiceTotalRecurringAmountBeforeAccountDiscount]: #nextinvoicetotalrecurringamountbeforeaccountdiscount
#### [nextInvoiceTotalRecurringAmountBeforeAccountDiscount]
The total recurring charge amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[nextInvoiceTotalRecurringTaxAmount]: #nextinvoicetotalrecurringtaxamount
#### [nextInvoiceTotalRecurringTaxAmount]
The total recurring tax amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[nextInvoiceTotalTaxableRecurringAmount]: #nextinvoicetotaltaxablerecurringamount
#### [nextInvoiceTotalTaxableRecurringAmount]
The total recurring charge amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[notificationSubscribers]: #notificationsubscribers
#### [notificationSubscribers]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Subscriber'>SoftLayer_Notification_Subscriber[] </a>**


</div>
<div class="prop-row">

-----
[openAbuseTickets]: #openabusetickets
#### [openAbuseTickets]
The open abuse tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[openAccountingTickets]: #openaccountingtickets
#### [openAccountingTickets]
The open accounting tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[openBillingTickets]: #openbillingtickets
#### [openBillingTickets]
The open billing tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[openCancellationRequests]: #opencancellationrequests
#### [openCancellationRequests]
An open ticket requesting cancellation of this server, if one exists.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request'>SoftLayer_Billing_Item_Cancellation_Request[] </a>**


</div>
<div class="prop-row">

-----
[openOtherTickets]: #openothertickets
#### [openOtherTickets]
The open tickets that do not belong to the abuse, accounting, sales, or support groups associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[openRecurringInvoices]: #openrecurringinvoices
#### [openRecurringInvoices]
An account's recurring invoices.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice[] </a>**


</div>
<div class="prop-row">

-----
[openSalesTickets]: #opensalestickets
#### [openSalesTickets]
The open sales tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[openStackAccountLinks]: #openstackaccountlinks
#### [openStackAccountLinks]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Link'>SoftLayer_Account_Link[] </a>**


</div>
<div class="prop-row">

-----
[openStackObjectStorage]: #openstackobjectstorage
#### [openStackObjectStorage]
An account's associated Openstack related Object Storage accounts.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[openSupportTickets]: #opensupporttickets
#### [openSupportTickets]
The open support tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[openTickets]: #opentickets
#### [openTickets]
All open tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[openTicketsWaitingOnCustomer]: #openticketswaitingoncustomer
#### [openTicketsWaitingOnCustomer]
All open tickets associated with an account last edited by an employee.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[orders]: #orders
#### [orders]
An account's associated billing orders excluding upgrades.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order'>SoftLayer_Billing_Order[] </a>**


</div>
<div class="prop-row">

-----
[orphanBillingItems]: #orphanbillingitems
#### [orphanBillingItems]
The billing items that have no parent billing item. These are items that don't necessarily belong to a single server.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[ownedBrands]: #ownedbrands
#### [ownedBrands]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand'>SoftLayer_Brand[] </a>**


</div>
<div class="prop-row">

-----
[ownedHardwareGenericComponentModels]: #ownedhardwaregenericcomponentmodels
#### [ownedHardwareGenericComponentModels]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Generic'>SoftLayer_Hardware_Component_Model_Generic[] </a>**


</div>
<div class="prop-row">

-----
[paymentProcessors]: #paymentprocessors
#### [paymentProcessors]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Payment_Processor'>SoftLayer_Billing_Payment_Processor[] </a>**


</div>
<div class="prop-row">

-----
[pendingEvents]: #pendingevents
#### [pendingEvents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Event'>SoftLayer_Notification_Occurrence_Event[] </a>**


</div>
<div class="prop-row">

-----
[pendingInvoice]: #pendinginvoice
#### [pendingInvoice]
An account's latest open (pending) invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice </a>**


</div>
<div class="prop-row">

-----
[pendingInvoiceTopLevelItems]: #pendinginvoicetoplevelitems
#### [pendingInvoiceTopLevelItems]
A list of top-level invoice items that are on an account's currently pending invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item[] </a>**


</div>
<div class="prop-row">

-----
[pendingInvoiceTotalAmount]: #pendinginvoicetotalamount
#### [pendingInvoiceTotalAmount]
The total amount of an account's pending invoice, if one exists.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[pendingInvoiceTotalOneTimeAmount]: #pendinginvoicetotalonetimeamount
#### [pendingInvoiceTotalOneTimeAmount]
The total one-time charges for an account's pending invoice, if one exists. In other words, it is the sum of one-time charges, setup fees, and labor fees. It does not include taxes.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[pendingInvoiceTotalOneTimeTaxAmount]: #pendinginvoicetotalonetimetaxamount
#### [pendingInvoiceTotalOneTimeTaxAmount]
The sum of all the taxes related to one time charges for an account's pending invoice, if one exists.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[pendingInvoiceTotalRecurringAmount]: #pendinginvoicetotalrecurringamount
#### [pendingInvoiceTotalRecurringAmount]
The total recurring amount of an account's pending invoice, if one exists.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[pendingInvoiceTotalRecurringTaxAmount]: #pendinginvoicetotalrecurringtaxamount
#### [pendingInvoiceTotalRecurringTaxAmount]
The total amount of the recurring taxes on an account's pending invoice, if one exists.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[permissionGroups]: #permissiongroups
#### [permissionGroups]
An account's permission groups.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Permission_Group'>SoftLayer_User_Permission_Group[] </a>**


</div>
<div class="prop-row">

-----
[permissionRoles]: #permissionroles
#### [permissionRoles]
An account's user roles.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Permission_Role'>SoftLayer_User_Permission_Role[] </a>**


</div>
<div class="prop-row">

-----
[placementGroups]: #placementgroups
#### [placementGroups]
An account's associated virtual placement groups.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_PlacementGroup'>SoftLayer_Virtual_PlacementGroup[] </a>**


</div>
<div class="prop-row">

-----
[portableStorageVolumes]: #portablestoragevolumes
#### [portableStorageVolumes]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image'>SoftLayer_Virtual_Disk_Image[] </a>**


</div>
<div class="prop-row">

-----
[postProvisioningHooks]: #postprovisioninghooks
#### [postProvisioningHooks]
Customer specified URIs that are downloaded onto a newly provisioned or reloaded server. If the URI is sent over https it will be executed directly on the server.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Hook'>SoftLayer_Provisioning_Hook[] </a>**


</div>
<div class="prop-row">

-----
[pptpVpnAllowedFlag]: #pptpvpnallowedflag
#### [pptpVpnAllowedFlag]
Boolean flag dictating whether or not this account supports PPTP VPN Access.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[pptpVpnUsers]: #pptpvpnusers
#### [pptpVpnUsers]
An account's associated portal users with PPTP VPN access. (Deprecated)  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer[] </a>**


</div>
<div class="prop-row">

-----
[previousRecurringRevenue]: #previousrecurringrevenue
#### [previousRecurringRevenue]
The total recurring amount for an accounts previous revenue.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[priceRestrictions]: #pricerestrictions
#### [priceRestrictions]
The item price that an account is restricted to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price_Account_Restriction'>SoftLayer_Product_Item_Price_Account_Restriction[] </a>**


</div>
<div class="prop-row">

-----
[priorityOneTickets]: #priorityonetickets
#### [priorityOneTickets]
All priority one tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[privateAllotmentHardwareBandwidthDetails]: #privateallotmenthardwarebandwidthdetails
#### [privateAllotmentHardwareBandwidthDetails]
DEPRECATED - This information can be pulled directly through tapping keys now - DEPRECATED. The allotments for this account and their servers. The private inbound and outbound bandwidth is calculated for each server in addition to the daily average network traffic since the last billing date.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment[] </a>**


</div>
<div class="prop-row">

-----
[privateBlockDeviceTemplateGroups]: #privateblockdevicetemplategroups
#### [privateBlockDeviceTemplateGroups]
Private and shared template group objects (parent only) for an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group'>SoftLayer_Virtual_Guest_Block_Device_Template_Group[] </a>**


</div>
<div class="prop-row">

-----
[privateIpAddresses]: #privateipaddresses
#### [privateIpAddresses]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>**


</div>
<div class="prop-row">

-----
[privateNetworkVlans]: #privatenetworkvlans
#### [privateNetworkVlans]
The private network VLANs assigned to an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a>**


</div>
<div class="prop-row">

-----
[privateSubnets]: #privatesubnets
#### [privateSubnets]
All private subnets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**


</div>
<div class="prop-row">

-----
[proofOfConceptAccountFlag]: #proofofconceptaccountflag
#### [proofOfConceptAccountFlag]
Boolean flag indicating whether or not this account is a Proof of Concept account.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[publicAllotmentHardwareBandwidthDetails]: #publicallotmenthardwarebandwidthdetails
#### [publicAllotmentHardwareBandwidthDetails]
DEPRECATED - This information can be pulled directly through tapping keys now - DEPRECATED. The allotments for this account and their servers. The public inbound and outbound bandwidth is calculated for each server in addition to the daily average network traffic since the last billing date.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment[] </a>**


</div>
<div class="prop-row">

-----
[publicIpAddresses]: #publicipaddresses
#### [publicIpAddresses]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>**


</div>
<div class="prop-row">

-----
[publicNetworkVlans]: #publicnetworkvlans
#### [publicNetworkVlans]
The public network VLANs assigned to an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a>**


</div>
<div class="prop-row">

-----
[publicSubnets]: #publicsubnets
#### [publicSubnets]
All public network subnets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**


</div>
<div class="prop-row">

-----
[quotes]: #quotes
#### [quotes]
An account's quotes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Quote'>SoftLayer_Billing_Order_Quote[] </a>**


</div>
<div class="prop-row">

-----
[recentEvents]: #recentevents
#### [recentEvents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Event'>SoftLayer_Notification_Occurrence_Event[] </a>**


</div>
<div class="prop-row">

-----
[referralPartner]: #referralpartner
#### [referralPartner]
The Referral Partner for this account, if any.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[referredAccounts]: #referredaccounts
#### [referredAccounts]
If this is a account is a referral partner, the accounts this referral partner has referred  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account[] </a>**


</div>
<div class="prop-row">

-----
[regulatedWorkloads]: #regulatedworkloads
#### [regulatedWorkloads]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Legal_RegulatedWorkload'>SoftLayer_Legal_RegulatedWorkload[] </a>**


</div>
<div class="prop-row">

-----
[remoteManagementCommandRequests]: #remotemanagementcommandrequests
#### [remoteManagementCommandRequests]
Remote management command requests for an account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_Command_Request'>SoftLayer_Hardware_Component_RemoteManagement_Command_Request[] </a>**


</div>
<div class="prop-row">

-----
[replicationEvents]: #replicationevents
#### [replicationEvents]
The Replication events for all Network Storage volumes on an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Event'>SoftLayer_Network_Storage_Event[] </a>**


</div>
<div class="prop-row">

-----
[requireSilentIBMidUserCreation]: #requiresilentibmidusercreation
#### [requireSilentIBMidUserCreation]
Indicates whether newly created users under this account will be associated with IBMid via an email requiring a response, or not.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[reservedCapacityAgreements]: #reservedcapacityagreements
#### [reservedCapacityAgreements]
All reserved capacity agreements for an account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Agreement'>SoftLayer_Account_Agreement[] </a>**


</div>
<div class="prop-row">

-----
[reservedCapacityGroups]: #reservedcapacitygroups
#### [reservedCapacityGroups]
The reserved capacity groups owned by this account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_ReservedCapacityGroup'>SoftLayer_Virtual_ReservedCapacityGroup[] </a>**


</div>
<div class="prop-row">

-----
[resourceGroups]: #resourcegroups
#### [resourceGroups]
An account's associated top-level resource groups.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group'>SoftLayer_Resource_Group[] </a>**


</div>
<div class="prop-row">

-----
[routers]: #routers
#### [routers]
All Routers that an accounts VLANs reside on  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[rwhoisData]: #rwhoisdata
#### [rwhoisData]
An account's reverse WHOIS data. This data is used when making SWIP requests.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_Rwhois_Data'>SoftLayer_Network_Subnet_Rwhois_Data </a>**


</div>
<div class="prop-row">

-----
[samlAuthentication]: #samlauthentication
#### [samlAuthentication]
The SAML configuration for this account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Authentication_Saml'>SoftLayer_Account_Authentication_Saml </a>**


</div>
<div class="prop-row">

-----
[scaleGroups]: #scalegroups
#### [scaleGroups]
All scale groups on this account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Group'>SoftLayer_Scale_Group[] </a>**


</div>
<div class="prop-row">

-----
[secondaryDomains]: #secondarydomains
#### [secondaryDomains]
The secondary DNS records for a SoftLayer customer account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Secondary'>SoftLayer_Dns_Secondary[] </a>**


</div>
<div class="prop-row">

-----
[securityCertificates]: #securitycertificates
#### [securityCertificates]
Stored security certificates (ie. SSL)  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Certificate'>SoftLayer_Security_Certificate[] </a>**


</div>
<div class="prop-row">

-----
[securityGroups]: #securitygroups
#### [securityGroups]
The security groups belonging to this account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_SecurityGroup'>SoftLayer_Network_SecurityGroup[] </a>**


</div>
<div class="prop-row">

-----
[securityLevel]: #securitylevel
#### [securityLevel]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Level'>SoftLayer_Security_Level </a>**


</div>
<div class="prop-row">

-----
[securityScanRequests]: #securityscanrequests
#### [securityScanRequests]
An account's vulnerability scan requests.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Security_Scanner_Request'>SoftLayer_Network_Security_Scanner_Request[] </a>**


</div>
<div class="prop-row">

-----
[serviceBillingItems]: #servicebillingitems
#### [serviceBillingItems]
The service billing items that will be on an account's next invoice.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[shipments]: #shipments
#### [shipments]
Shipments that belong to the customer's account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Shipment'>SoftLayer_Account_Shipment[] </a>**


</div>
<div class="prop-row">

-----
[sshKeys]: #sshkeys
#### [sshKeys]
Customer specified SSH keys that can be implemented onto a newly provisioned or reloaded server.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Ssh_Key'>SoftLayer_Security_Ssh_Key[] </a>**


</div>
<div class="prop-row">

-----
[sslVpnUsers]: #sslvpnusers
#### [sslVpnUsers]
An account's associated portal users with SSL VPN access.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer[] </a>**


</div>
<div class="prop-row">

-----
[standardPoolVirtualGuests]: #standardpoolvirtualguests
#### [standardPoolVirtualGuests]
An account's virtual guest objects that are hosted on a user provisioned hypervisor.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[subnetRegistrationDetails]: #subnetregistrationdetails
#### [subnetRegistrationDetails]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail'>SoftLayer_Account_Regional_Registry_Detail[] </a>**


</div>
<div class="prop-row">

-----
[subnetRegistrations]: #subnetregistrations
#### [subnetRegistrations]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration'>SoftLayer_Network_Subnet_Registration[] </a>**


</div>
<div class="prop-row">

-----
[subnets]: #subnets
#### [subnets]
All network subnets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**


</div>
<div class="prop-row">

-----
[supportRepresentatives]: #supportrepresentatives
#### [supportRepresentatives]
The SoftLayer employees that an account is assigned to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee[] </a>**


</div>
<div class="prop-row">

-----
[supportSubscriptions]: #supportsubscriptions
#### [supportSubscriptions]
The active support subscriptions for this account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[supportTier]: #supporttier
#### [supportTier]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[suppressInvoicesFlag]: #suppressinvoicesflag
#### [suppressInvoicesFlag]
A flag indicating to suppress invoices.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[tags]: #tags
#### [tags]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Tag'>SoftLayer_Tag[] </a>**


</div>
<div class="prop-row">

-----
[tickets]: #tickets
#### [tickets]
An account's associated tickets.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[ticketsClosedInTheLastThreeDays]: #ticketsclosedinthelastthreedays
#### [ticketsClosedInTheLastThreeDays]
Tickets closed within the last 72 hours or last 10 tickets, whichever is less, associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[ticketsClosedToday]: #ticketsclosedtoday
#### [ticketsClosedToday]
Tickets closed today associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[transcodeAccounts]: #transcodeaccounts
#### [transcodeAccounts]
An account's associated Transcode account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Media_Transcode_Account'>SoftLayer_Network_Media_Transcode_Account[] </a>**


</div>
<div class="prop-row">

-----
[upgradeRequests]: #upgraderequests
#### [upgradeRequests]
An account's associated upgrade requests.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Upgrade_Request'>SoftLayer_Product_Upgrade_Request[] </a>**


</div>
<div class="prop-row">

-----
[users]: #users
#### [users]
An account's portal users.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer[] </a>**


</div>
<div class="prop-row">

-----
[validSecurityCertificates]: #validsecuritycertificates
#### [validSecurityCertificates]
Stored security certificates that are not expired (ie. SSL)  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Certificate'>SoftLayer_Security_Certificate[] </a>**


</div>
<div class="prop-row">

-----
[vdrUpdatesInProgressFlag]: #vdrupdatesinprogressflag
#### [vdrUpdatesInProgressFlag]
Return 0 if vpn updates are currently in progress on this account otherwise 1.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[virtualDedicatedRacks]: #virtualdedicatedracks
#### [virtualDedicatedRacks]
The bandwidth pooling for this account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment[] </a>**


</div>
<div class="prop-row">

-----
[virtualDiskImages]: #virtualdiskimages
#### [virtualDiskImages]
An account's associated virtual server virtual disk images.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image'>SoftLayer_Virtual_Disk_Image[] </a>**


</div>
<div class="prop-row">

-----
[virtualGuests]: #virtualguests
#### [virtualGuests]
An account's associated virtual guest objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[virtualGuestsOverBandwidthAllocation]: #virtualguestsoverbandwidthallocation
#### [virtualGuestsOverBandwidthAllocation]
An account's associated virtual guest objects currently over bandwidth allocation.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[virtualGuestsProjectedOverBandwidthAllocation]: #virtualguestsprojectedoverbandwidthallocation
#### [virtualGuestsProjectedOverBandwidthAllocation]
An account's associated virtual guest objects currently over bandwidth allocation.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[virtualGuestsWithCpanel]: #virtualguestswithcpanel
#### [virtualGuestsWithCpanel]
All virtual guests associated with an account that has the cPanel web hosting control panel installed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[virtualGuestsWithMcafee]: #virtualguestswithmcafee
#### [virtualGuestsWithMcafee]
All virtual guests associated with an account that have McAfee Secure software components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[virtualGuestsWithMcafeeAntivirusRedhat]: #virtualguestswithmcafeeantivirusredhat
#### [virtualGuestsWithMcafeeAntivirusRedhat]
All virtual guests associated with an account that have McAfee Secure AntiVirus for Redhat software components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[virtualGuestsWithMcafeeAntivirusWindows]: #virtualguestswithmcafeeantiviruswindows
#### [virtualGuestsWithMcafeeAntivirusWindows]
All virtual guests associated with an account that has McAfee Secure AntiVirus for Windows software components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[virtualGuestsWithMcafeeIntrusionDetectionSystem]: #virtualguestswithmcafeeintrusiondetectionsystem
#### [virtualGuestsWithMcafeeIntrusionDetectionSystem]
All virtual guests associated with an account that has McAfee Secure Intrusion Detection System software components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[virtualGuestsWithPlesk]: #virtualguestswithplesk
#### [virtualGuestsWithPlesk]
All virtual guests associated with an account that has the Plesk web hosting control panel installed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[virtualGuestsWithQuantastor]: #virtualguestswithquantastor
#### [virtualGuestsWithQuantastor]
All virtual guests associated with an account that have the QuantaStor storage system installed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[virtualGuestsWithUrchin]: #virtualguestswithurchin
#### [virtualGuestsWithUrchin]
All virtual guests associated with an account that has the Urchin web traffic analytics package installed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[virtualPrivateRack]: #virtualprivaterack
#### [virtualPrivateRack]
The bandwidth pooling for this account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment </a>**


</div>
<div class="prop-row">

-----
[virtualStorageArchiveRepositories]: #virtualstoragearchiverepositories
#### [virtualStorageArchiveRepositories]
An account's associated virtual server archived storage repositories.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Storage_Repository'>SoftLayer_Virtual_Storage_Repository[] </a>**


</div>
<div class="prop-row">

-----
[virtualStoragePublicRepositories]: #virtualstoragepublicrepositories
#### [virtualStoragePublicRepositories]
An account's associated virtual server public storage repositories.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Storage_Repository'>SoftLayer_Virtual_Storage_Repository[] </a>**


</div>
<div class="prop-row">

-----
[vpcVirtualGuests]: #vpcvirtualguests
#### [vpcVirtualGuests]
An account's associated VPC configured virtual guest objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>

## Count
<div class="prop-row">

-----
[abuseEmailCount]: #abuseemailcount
#### [abuseEmailCount]
A count of email addresses that are responsible for abuse and legal inquiries on behalf of an account. For instance, new legal and abuse tickets are sent to these addresses.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[accountContactCount]: #accountcontactcount
#### [accountContactCount]
A count of the account contacts on an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[accountLicenseCount]: #accountlicensecount
#### [accountLicenseCount]
A count of the account software licenses owned by an account   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[accountLinkCount]: #accountlinkcount
#### [accountLinkCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[activeAccountLicenseCount]: #activeaccountlicensecount
#### [activeAccountLicenseCount]
A count of the active account software licenses owned by an account   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[activeAddressCount]: #activeaddresscount
#### [activeAddressCount]
A count of the active address(es) that belong to an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[activeAgreementCount]: #activeagreementcount
#### [activeAgreementCount]
A count of all active agreements for an account   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[activeBillingAgreementCount]: #activebillingagreementcount
#### [activeBillingAgreementCount]
A count of all billing agreements for an account   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[activeColocationContainerCount]: #activecolocationcontainercount
#### [activeColocationContainerCount]
A count of the account's active top level colocation containers.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[activeFlexibleCreditEnrollmentCount]: #activeflexiblecreditenrollmentcount
#### [activeFlexibleCreditEnrollmentCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[activeNotificationSubscriberCount]: #activenotificationsubscribercount
#### [activeNotificationSubscriberCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[activeQuoteCount]: #activequotecount
#### [activeQuoteCount]
A count of an account's non-expired quotes.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[activeReservedCapacityAgreementCount]: #activereservedcapacityagreementcount
#### [activeReservedCapacityAgreementCount]
A count of active reserved capacity agreements for an account   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[activeVirtualLicenseCount]: #activevirtuallicensecount
#### [activeVirtualLicenseCount]
A count of the virtual software licenses controlled by an account   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[adcLoadBalancerCount]: #adcloadbalancercount
#### [adcLoadBalancerCount]
A count of an account's associated load balancers.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[addressCount]: #addresscount
#### [addressCount]
A count of all the address(es) that belong to an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[allCommissionBillingItemCount]: #allcommissionbillingitemcount
#### [allCommissionBillingItemCount]
A count of the billing items that will be on an account's next invoice.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[allRecurringTopLevelBillingItemCount]: #allrecurringtoplevelbillingitemcount
#### [allRecurringTopLevelBillingItemCount]
A count of the billing items that will be on an account's next invoice.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[allRecurringTopLevelBillingItemsUnfilteredCount]: #allrecurringtoplevelbillingitemsunfilteredcount
#### [allRecurringTopLevelBillingItemsUnfilteredCount]
A count of the billing items that will be on an account's next invoice. Does not consider associated items.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[allSubnetBillingItemCount]: #allsubnetbillingitemcount
#### [allSubnetBillingItemCount]
A count of the billing items that will be on an account's next invoice.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[allTopLevelBillingItemCount]: #alltoplevelbillingitemcount
#### [allTopLevelBillingItemCount]
A count of all billing items of an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[allTopLevelBillingItemsUnfilteredCount]: #alltoplevelbillingitemsunfilteredcount
#### [allTopLevelBillingItemsUnfilteredCount]
A count of the billing items that will be on an account's next invoice. Does not consider associated items.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[applicationDeliveryControllerCount]: #applicationdeliverycontrollercount
#### [applicationDeliveryControllerCount]
A count of an account's associated application delivery controller records.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of the account attribute values for a SoftLayer customer account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[availablePublicNetworkVlanCount]: #availablepublicnetworkvlancount
#### [availablePublicNetworkVlanCount]
A count of the public network VLANs assigned to an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[bandwidthAllotmentCount]: #bandwidthallotmentcount
#### [bandwidthAllotmentCount]
A count of the bandwidth allotments for an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[bandwidthAllotmentsOverAllocationCount]: #bandwidthallotmentsoverallocationcount
#### [bandwidthAllotmentsOverAllocationCount]
A count of the bandwidth allotments for an account currently over allocation.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[bandwidthAllotmentsProjectedOverAllocationCount]: #bandwidthallotmentsprojectedoverallocationcount
#### [bandwidthAllotmentsProjectedOverAllocationCount]
A count of the bandwidth allotments for an account projected to go over allocation.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[bareMetalInstanceCount]: #baremetalinstancecount
#### [bareMetalInstanceCount]
A count of an account's associated bare metal server objects.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[billingAgreementCount]: #billingagreementcount
#### [billingAgreementCount]
A count of all billing agreements for an account   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[blockDeviceTemplateGroupCount]: #blockdevicetemplategroupcount
#### [blockDeviceTemplateGroupCount]
A count of private template group objects (parent and children) and the shared template group objects (parent only) for an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[cartCount]: #cartcount
#### [cartCount]
A count of an account's active carts.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[catalystEnrollmentCount]: #catalystenrollmentcount
#### [catalystEnrollmentCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[closedTicketCount]: #closedticketcount
#### [closedTicketCount]
A count of all closed tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[datacentersWithSubnetAllocationCount]: #datacenterswithsubnetallocationcount
#### [datacentersWithSubnetAllocationCount]
A count of datacenters which contain subnets that the account has access to route.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[dedicatedHostCount]: #dedicatedhostcount
#### [dedicatedHostCount]
A count of an account's associated virtual dedicated host objects.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[displaySupportRepresentativeAssignmentCount]: #displaysupportrepresentativeassignmentcount
#### [displaySupportRepresentativeAssignmentCount]
A count of the SoftLayer employees that an account is assigned to.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[domainCount]: #domaincount
#### [domainCount]
A count of the DNS domains associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[domainRegistrationCount]: #domainregistrationcount
#### [domainRegistrationCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[domainsWithoutSecondaryDnsRecordCount]: #domainswithoutsecondarydnsrecordcount
#### [domainsWithoutSecondaryDnsRecordCount]
A count of the DNS domains associated with an account that were not created as a result of a secondary DNS zone transfer.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[evaultMasterUserCount]: #evaultmasterusercount
#### [evaultMasterUserCount]
A count of an account's master EVault user. This is only used when an account has EVault service.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[evaultNetworkStorageCount]: #evaultnetworkstoragecount
#### [evaultNetworkStorageCount]
A count of an account's associated EVault storage volumes.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[expiredSecurityCertificateCount]: #expiredsecuritycertificatecount
#### [expiredSecurityCertificateCount]
A count of stored security certificates that are expired (ie. SSL)   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[facilityLogCount]: #facilitylogcount
#### [facilityLogCount]
A count of logs of who entered a colocation area which is assigned to this account, or when a user under this account enters a datacenter.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[flexibleCreditEnrollmentCount]: #flexiblecreditenrollmentcount
#### [flexibleCreditEnrollmentCount]
A count of all of the account's current and former Flexible Credit enrollments.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[globalIpRecordCount]: #globaliprecordcount
#### [globalIpRecordCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[globalIpv4RecordCount]: #globalipv4recordcount
#### [globalIpv4RecordCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[globalIpv6RecordCount]: #globalipv6recordcount
#### [globalIpv6RecordCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[globalLoadBalancerAccountCount]: #globalloadbalanceraccountcount
#### [globalLoadBalancerAccountCount]
A count of the global load balancer accounts for a softlayer customer account.   
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
[hardwareOverBandwidthAllocationCount]: #hardwareoverbandwidthallocationcount
#### [hardwareOverBandwidthAllocationCount]
A count of an account's associated hardware objects currently over bandwidth allocation.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[hardwareProjectedOverBandwidthAllocationCount]: #hardwareprojectedoverbandwidthallocationcount
#### [hardwareProjectedOverBandwidthAllocationCount]
A count of an account's associated hardware objects projected to go over bandwidth allocation.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[hardwareWithCpanelCount]: #hardwarewithcpanelcount
#### [hardwareWithCpanelCount]
A count of all hardware associated with an account that has the cPanel web hosting control panel installed.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[hardwareWithHelmCount]: #hardwarewithhelmcount
#### [hardwareWithHelmCount]
A count of all hardware associated with an account that has the Helm web hosting control panel installed.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[hardwareWithMcafeeAntivirusRedhatCount]: #hardwarewithmcafeeantivirusredhatcount
#### [hardwareWithMcafeeAntivirusRedhatCount]
A count of all hardware associated with an account that has McAfee Secure AntiVirus for Redhat software components.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[hardwareWithMcafeeAntivirusWindowCount]: #hardwarewithmcafeeantiviruswindowcount
#### [hardwareWithMcafeeAntivirusWindowCount]
A count of all hardware associated with an account that has McAfee Secure AntiVirus for Windows software components.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[hardwareWithMcafeeCount]: #hardwarewithmcafeecount
#### [hardwareWithMcafeeCount]
A count of all hardware associated with an account that has McAfee Secure software components.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[hardwareWithMcafeeIntrusionDetectionSystemCount]: #hardwarewithmcafeeintrusiondetectionsystemcount
#### [hardwareWithMcafeeIntrusionDetectionSystemCount]
A count of all hardware associated with an account that has McAfee Secure Intrusion Detection System software components.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[hardwareWithPleskCount]: #hardwarewithpleskcount
#### [hardwareWithPleskCount]
A count of all hardware associated with an account that has the Plesk web hosting control panel installed.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[hardwareWithQuantastorCount]: #hardwarewithquantastorcount
#### [hardwareWithQuantastorCount]
A count of all hardware associated with an account that has the QuantaStor storage system installed.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[hardwareWithUrchinCount]: #hardwarewithurchincount
#### [hardwareWithUrchinCount]
A count of all hardware associated with an account that has the Urchin web traffic analytics package installed.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[hardwareWithWindowCount]: #hardwarewithwindowcount
#### [hardwareWithWindowCount]
A count of all hardware associated with an account that is running a version of the Microsoft Windows operating system.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[hourlyBareMetalInstanceCount]: #hourlybaremetalinstancecount
#### [hourlyBareMetalInstanceCount]
A count of an account's associated hourly bare metal server objects.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[hourlyServiceBillingItemCount]: #hourlyservicebillingitemcount
#### [hourlyServiceBillingItemCount]
A count of hourly service billing items that will be on an account's next invoice.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[hourlyVirtualGuestCount]: #hourlyvirtualguestcount
#### [hourlyVirtualGuestCount]
A count of an account's associated hourly virtual guest objects.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[hubNetworkStorageCount]: #hubnetworkstoragecount
#### [hubNetworkStorageCount]
A count of an account's associated Virtual Storage volumes.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[internalNoteCount]: #internalnotecount
#### [internalNoteCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[invoiceCount]: #invoicecount
#### [invoiceCount]
A count of an account's associated billing invoices.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[ipAddressCount]: #ipaddresscount
#### [ipAddressCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[iscsiNetworkStorageCount]: #iscsinetworkstoragecount
#### [iscsiNetworkStorageCount]
A count of an account's associated iSCSI storage volumes.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[lastFiveClosedAbuseTicketCount]: #lastfiveclosedabuseticketcount
#### [lastFiveClosedAbuseTicketCount]
A count of the five most recently closed abuse tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[lastFiveClosedAccountingTicketCount]: #lastfiveclosedaccountingticketcount
#### [lastFiveClosedAccountingTicketCount]
A count of the five most recently closed accounting tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[lastFiveClosedOtherTicketCount]: #lastfiveclosedotherticketcount
#### [lastFiveClosedOtherTicketCount]
A count of the five most recently closed tickets that do not belong to the abuse, accounting, sales, or support groups associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[lastFiveClosedSalesTicketCount]: #lastfiveclosedsalesticketcount
#### [lastFiveClosedSalesTicketCount]
A count of the five most recently closed sales tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[lastFiveClosedSupportTicketCount]: #lastfiveclosedsupportticketcount
#### [lastFiveClosedSupportTicketCount]
A count of the five most recently closed support tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[lastFiveClosedTicketCount]: #lastfiveclosedticketcount
#### [lastFiveClosedTicketCount]
A count of the five most recently closed tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[legacyBandwidthAllotmentCount]: #legacybandwidthallotmentcount
#### [legacyBandwidthAllotmentCount]
A count of the legacy bandwidth allotments for an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[loadBalancerCount]: #loadbalancercount
#### [loadBalancerCount]
A count of an account's associated load balancers.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[lockboxNetworkStorageCount]: #lockboxnetworkstoragecount
#### [lockboxNetworkStorageCount]
A count of an account's associated Lockbox storage volumes.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[manualPaymentsUnderReviewCount]: #manualpaymentsunderreviewcount
#### [manualPaymentsUnderReviewCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[mediaDataTransferRequestCount]: #mediadatatransferrequestcount
#### [mediaDataTransferRequestCount]
A count of an account's media transfer service requests.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[monthlyBareMetalInstanceCount]: #monthlybaremetalinstancecount
#### [monthlyBareMetalInstanceCount]
A count of an account's associated monthly bare metal server objects.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[monthlyVirtualGuestCount]: #monthlyvirtualguestcount
#### [monthlyVirtualGuestCount]
A count of an account's associated monthly virtual guest objects.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[nasNetworkStorageCount]: #nasnetworkstoragecount
#### [nasNetworkStorageCount]
A count of an account's associated NAS storage volumes.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkGatewayCount]: #networkgatewaycount
#### [networkGatewayCount]
A count of all network gateway devices on this account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkHardwareCount]: #networkhardwarecount
#### [networkHardwareCount]
A count of an account's associated network hardware.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkMessageDeliveryAccountCount]: #networkmessagedeliveryaccountcount
#### [networkMessageDeliveryAccountCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkMonitorDownHardwareCount]: #networkmonitordownhardwarecount
#### [networkMonitorDownHardwareCount]
A count of hardware which is currently experiencing a service failure.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkMonitorDownVirtualGuestCount]: #networkmonitordownvirtualguestcount
#### [networkMonitorDownVirtualGuestCount]
A count of virtual guest which is currently experiencing a service failure.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkMonitorRecoveringHardwareCount]: #networkmonitorrecoveringhardwarecount
#### [networkMonitorRecoveringHardwareCount]
A count of hardware which is currently recovering from a service failure.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkMonitorRecoveringVirtualGuestCount]: #networkmonitorrecoveringvirtualguestcount
#### [networkMonitorRecoveringVirtualGuestCount]
A count of virtual guest which is currently recovering from a service failure.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkMonitorUpHardwareCount]: #networkmonitoruphardwarecount
#### [networkMonitorUpHardwareCount]
A count of hardware which is currently online.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkMonitorUpVirtualGuestCount]: #networkmonitorupvirtualguestcount
#### [networkMonitorUpVirtualGuestCount]
A count of virtual guest which is currently online.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkStorageCount]: #networkstoragecount
#### [networkStorageCount]
A count of an account's associated storage volumes. This includes Lockbox, NAS, EVault, and iSCSI volumes.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkStorageGroupCount]: #networkstoragegroupcount
#### [networkStorageGroupCount]
A count of an account's Network Storage groups.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkTunnelContextCount]: #networktunnelcontextcount
#### [networkTunnelContextCount]
A count of iPSec network tunnels for an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkVlanCount]: #networkvlancount
#### [networkVlanCount]
A count of all network VLANs assigned to an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[nextBillingPublicAllotmentHardwareBandwidthDetailCount]: #nextbillingpublicallotmenthardwarebandwidthdetailcount
#### [nextBillingPublicAllotmentHardwareBandwidthDetailCount]
A count of dEPRECATED - This information can be pulled directly through tapping keys now - DEPRECATED. The allotments for this account and their servers for the next billing cycle. The public inbound and outbound bandwidth is calculated for each server in addition to the daily average network traffic since the last billing date.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[nextInvoiceTopLevelBillingItemCount]: #nextinvoicetoplevelbillingitemcount
#### [nextInvoiceTopLevelBillingItemCount]
A count of the billing items that will be on an account's next invoice.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[notificationSubscriberCount]: #notificationsubscribercount
#### [notificationSubscriberCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[openAbuseTicketCount]: #openabuseticketcount
#### [openAbuseTicketCount]
A count of the open abuse tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[openAccountingTicketCount]: #openaccountingticketcount
#### [openAccountingTicketCount]
A count of the open accounting tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[openBillingTicketCount]: #openbillingticketcount
#### [openBillingTicketCount]
A count of the open billing tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[openCancellationRequestCount]: #opencancellationrequestcount
#### [openCancellationRequestCount]
A count of an open ticket requesting cancellation of this server, if one exists.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[openOtherTicketCount]: #openotherticketcount
#### [openOtherTicketCount]
A count of the open tickets that do not belong to the abuse, accounting, sales, or support groups associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[openRecurringInvoiceCount]: #openrecurringinvoicecount
#### [openRecurringInvoiceCount]
A count of an account's recurring invoices.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[openSalesTicketCount]: #opensalesticketcount
#### [openSalesTicketCount]
A count of the open sales tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[openStackAccountLinkCount]: #openstackaccountlinkcount
#### [openStackAccountLinkCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[openStackObjectStorageCount]: #openstackobjectstoragecount
#### [openStackObjectStorageCount]
A count of an account's associated Openstack related Object Storage accounts.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[openSupportTicketCount]: #opensupportticketcount
#### [openSupportTicketCount]
A count of the open support tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[openTicketCount]: #openticketcount
#### [openTicketCount]
A count of all open tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[openTicketsWaitingOnCustomerCount]: #openticketswaitingoncustomercount
#### [openTicketsWaitingOnCustomerCount]
A count of all open tickets associated with an account last edited by an employee.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[orderCount]: #ordercount
#### [orderCount]
A count of an account's associated billing orders excluding upgrades.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[orphanBillingItemCount]: #orphanbillingitemcount
#### [orphanBillingItemCount]
A count of the billing items that have no parent billing item. These are items that don't necessarily belong to a single server.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[ownedBrandCount]: #ownedbrandcount
#### [ownedBrandCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[ownedHardwareGenericComponentModelCount]: #ownedhardwaregenericcomponentmodelcount
#### [ownedHardwareGenericComponentModelCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[paymentProcessorCount]: #paymentprocessorcount
#### [paymentProcessorCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[pendingEventCount]: #pendingeventcount
#### [pendingEventCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[pendingInvoiceTopLevelItemCount]: #pendinginvoicetoplevelitemcount
#### [pendingInvoiceTopLevelItemCount]
A count of a list of top-level invoice items that are on an account's currently pending invoice.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[permissionGroupCount]: #permissiongroupcount
#### [permissionGroupCount]
A count of an account's permission groups.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[permissionRoleCount]: #permissionrolecount
#### [permissionRoleCount]
A count of an account's user roles.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[placementGroupCount]: #placementgroupcount
#### [placementGroupCount]
A count of an account's associated virtual placement groups.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[portableStorageVolumeCount]: #portablestoragevolumecount
#### [portableStorageVolumeCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[postProvisioningHookCount]: #postprovisioninghookcount
#### [postProvisioningHookCount]
A count of customer specified URIs that are downloaded onto a newly provisioned or reloaded server. If the URI is sent over https it will be executed directly on the server.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[pptpVpnUserCount]: #pptpvpnusercount
#### [pptpVpnUserCount]
A count of an account's associated portal users with PPTP VPN access. (Deprecated)   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[priceRestrictionCount]: #pricerestrictioncount
#### [priceRestrictionCount]
A count of the item price that an account is restricted to.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[priorityOneTicketCount]: #priorityoneticketcount
#### [priorityOneTicketCount]
A count of all priority one tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[privateAllotmentHardwareBandwidthDetailCount]: #privateallotmenthardwarebandwidthdetailcount
#### [privateAllotmentHardwareBandwidthDetailCount]
A count of dEPRECATED - This information can be pulled directly through tapping keys now - DEPRECATED. The allotments for this account and their servers. The private inbound and outbound bandwidth is calculated for each server in addition to the daily average network traffic since the last billing date.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[privateBlockDeviceTemplateGroupCount]: #privateblockdevicetemplategroupcount
#### [privateBlockDeviceTemplateGroupCount]
A count of private and shared template group objects (parent only) for an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[privateIpAddressCount]: #privateipaddresscount
#### [privateIpAddressCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[privateNetworkVlanCount]: #privatenetworkvlancount
#### [privateNetworkVlanCount]
A count of the private network VLANs assigned to an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[privateSubnetCount]: #privatesubnetcount
#### [privateSubnetCount]
A count of all private subnets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[publicAllotmentHardwareBandwidthDetailCount]: #publicallotmenthardwarebandwidthdetailcount
#### [publicAllotmentHardwareBandwidthDetailCount]
A count of dEPRECATED - This information can be pulled directly through tapping keys now - DEPRECATED. The allotments for this account and their servers. The public inbound and outbound bandwidth is calculated for each server in addition to the daily average network traffic since the last billing date.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[publicIpAddressCount]: #publicipaddresscount
#### [publicIpAddressCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[publicNetworkVlanCount]: #publicnetworkvlancount
#### [publicNetworkVlanCount]
A count of the public network VLANs assigned to an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[publicSubnetCount]: #publicsubnetcount
#### [publicSubnetCount]
A count of all public network subnets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[quoteCount]: #quotecount
#### [quoteCount]
A count of an account's quotes.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[recentEventCount]: #recenteventcount
#### [recentEventCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[referredAccountCount]: #referredaccountcount
#### [referredAccountCount]
A count of if this is a account is a referral partner, the accounts this referral partner has referred   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[regulatedWorkloadCount]: #regulatedworkloadcount
#### [regulatedWorkloadCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[remoteManagementCommandRequestCount]: #remotemanagementcommandrequestcount
#### [remoteManagementCommandRequestCount]
A count of remote management command requests for an account   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[replicationEventCount]: #replicationeventcount
#### [replicationEventCount]
A count of the Replication events for all Network Storage volumes on an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[reservedCapacityAgreementCount]: #reservedcapacityagreementcount
#### [reservedCapacityAgreementCount]
A count of all reserved capacity agreements for an account   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[reservedCapacityGroupCount]: #reservedcapacitygroupcount
#### [reservedCapacityGroupCount]
A count of the reserved capacity groups owned by this account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[resourceGroupCount]: #resourcegroupcount
#### [resourceGroupCount]
A count of an account's associated top-level resource groups.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[routerCount]: #routercount
#### [routerCount]
A count of all Routers that an accounts VLANs reside on   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[scaleGroupCount]: #scalegroupcount
#### [scaleGroupCount]
A count of all scale groups on this account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[secondaryDomainCount]: #secondarydomaincount
#### [secondaryDomainCount]
A count of the secondary DNS records for a SoftLayer customer account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[securityCertificateCount]: #securitycertificatecount
#### [securityCertificateCount]
A count of stored security certificates (ie. SSL)   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[securityGroupCount]: #securitygroupcount
#### [securityGroupCount]
A count of the security groups belonging to this account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[securityScanRequestCount]: #securityscanrequestcount
#### [securityScanRequestCount]
A count of an account's vulnerability scan requests.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[serviceBillingItemCount]: #servicebillingitemcount
#### [serviceBillingItemCount]
A count of the service billing items that will be on an account's next invoice.    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[shipmentCount]: #shipmentcount
#### [shipmentCount]
A count of shipments that belong to the customer's account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[sshKeyCount]: #sshkeycount
#### [sshKeyCount]
A count of customer specified SSH keys that can be implemented onto a newly provisioned or reloaded server.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[sslVpnUserCount]: #sslvpnusercount
#### [sslVpnUserCount]
A count of an account's associated portal users with SSL VPN access.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[standardPoolVirtualGuestCount]: #standardpoolvirtualguestcount
#### [standardPoolVirtualGuestCount]
A count of an account's virtual guest objects that are hosted on a user provisioned hypervisor.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[subnetCount]: #subnetcount
#### [subnetCount]
A count of all network subnets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[subnetRegistrationCount]: #subnetregistrationcount
#### [subnetRegistrationCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[subnetRegistrationDetailCount]: #subnetregistrationdetailcount
#### [subnetRegistrationDetailCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[supportRepresentativeCount]: #supportrepresentativecount
#### [supportRepresentativeCount]
A count of the SoftLayer employees that an account is assigned to.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[supportSubscriptionCount]: #supportsubscriptioncount
#### [supportSubscriptionCount]
A count of the active support subscriptions for this account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[tagCount]: #tagcount
#### [tagCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[ticketCount]: #ticketcount
#### [ticketCount]
A count of an account's associated tickets.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[ticketsClosedInTheLastThreeDaysCount]: #ticketsclosedinthelastthreedayscount
#### [ticketsClosedInTheLastThreeDaysCount]
A count of tickets closed within the last 72 hours or last 10 tickets, whichever is less, associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[ticketsClosedTodayCount]: #ticketsclosedtodaycount
#### [ticketsClosedTodayCount]
A count of tickets closed today associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[transcodeAccountCount]: #transcodeaccountcount
#### [transcodeAccountCount]
A count of an account's associated Transcode account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[upgradeRequestCount]: #upgraderequestcount
#### [upgradeRequestCount]
A count of an account's associated upgrade requests.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[userCount]: #usercount
#### [userCount]
A count of an account's portal users.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[validSecurityCertificateCount]: #validsecuritycertificatecount
#### [validSecurityCertificateCount]
A count of stored security certificates that are not expired (ie. SSL)   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[virtualDedicatedRackCount]: #virtualdedicatedrackcount
#### [virtualDedicatedRackCount]
A count of the bandwidth pooling for this account.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[virtualDiskImageCount]: #virtualdiskimagecount
#### [virtualDiskImageCount]
A count of an account's associated virtual server virtual disk images.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[virtualGuestCount]: #virtualguestcount
#### [virtualGuestCount]
A count of an account's associated virtual guest objects.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[virtualGuestsOverBandwidthAllocationCount]: #virtualguestsoverbandwidthallocationcount
#### [virtualGuestsOverBandwidthAllocationCount]
A count of an account's associated virtual guest objects currently over bandwidth allocation.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[virtualGuestsProjectedOverBandwidthAllocationCount]: #virtualguestsprojectedoverbandwidthallocationcount
#### [virtualGuestsProjectedOverBandwidthAllocationCount]
A count of an account's associated virtual guest objects currently over bandwidth allocation.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[virtualGuestsWithCpanelCount]: #virtualguestswithcpanelcount
#### [virtualGuestsWithCpanelCount]
A count of all virtual guests associated with an account that has the cPanel web hosting control panel installed.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[virtualGuestsWithMcafeeAntivirusRedhatCount]: #virtualguestswithmcafeeantivirusredhatcount
#### [virtualGuestsWithMcafeeAntivirusRedhatCount]
A count of all virtual guests associated with an account that have McAfee Secure AntiVirus for Redhat software components.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[virtualGuestsWithMcafeeAntivirusWindowCount]: #virtualguestswithmcafeeantiviruswindowcount
#### [virtualGuestsWithMcafeeAntivirusWindowCount]
A count of all virtual guests associated with an account that has McAfee Secure AntiVirus for Windows software components.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[virtualGuestsWithMcafeeCount]: #virtualguestswithmcafeecount
#### [virtualGuestsWithMcafeeCount]
A count of all virtual guests associated with an account that have McAfee Secure software components.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[virtualGuestsWithMcafeeIntrusionDetectionSystemCount]: #virtualguestswithmcafeeintrusiondetectionsystemcount
#### [virtualGuestsWithMcafeeIntrusionDetectionSystemCount]
A count of all virtual guests associated with an account that has McAfee Secure Intrusion Detection System software components.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[virtualGuestsWithPleskCount]: #virtualguestswithpleskcount
#### [virtualGuestsWithPleskCount]
A count of all virtual guests associated with an account that has the Plesk web hosting control panel installed.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[virtualGuestsWithQuantastorCount]: #virtualguestswithquantastorcount
#### [virtualGuestsWithQuantastorCount]
A count of all virtual guests associated with an account that have the QuantaStor storage system installed.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[virtualGuestsWithUrchinCount]: #virtualguestswithurchincount
#### [virtualGuestsWithUrchinCount]
A count of all virtual guests associated with an account that has the Urchin web traffic analytics package installed.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[virtualStorageArchiveRepositoryCount]: #virtualstoragearchiverepositorycount
#### [virtualStorageArchiveRepositoryCount]
A count of an account's associated virtual server archived storage repositories.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[virtualStoragePublicRepositoryCount]: #virtualstoragepublicrepositorycount
#### [virtualStoragePublicRepositoryCount]
A count of an account's associated virtual server public storage repositories.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[vpcVirtualGuestCount]: #vpcvirtualguestcount
#### [vpcVirtualGuestCount]
A count of an account's associated VPC configured virtual guest objects.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


