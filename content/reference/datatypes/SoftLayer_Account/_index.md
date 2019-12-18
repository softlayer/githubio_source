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
[accountManagedResourcesFlag]: #accountmanagedresourcesflag
#### [accountManagedResourcesFlag]
A flag indicating that the account has a managed resource.  
<span class="type-label">Type: </span>**boolean**

-----
[accountStatusId]: #accountstatusid
#### [accountStatusId]
A number reflecting the state of an account.  
<span class="type-label">Type: </span>**integer**

-----
[address1]: #address1
#### [address1]
The first line of the mailing address belonging to an account.  
<span class="type-label">Type: </span>**string**

-----
[address2]: #address2
#### [address2]
The second line of the mailing address belonging to an account.  
<span class="type-label">Type: </span>**string**

-----
[allowedPptpVpnQuantity]: #allowedpptpvpnquantity
#### [allowedPptpVpnQuantity]
The number of PPTP VPN users allowed on an account.  
<span class="type-label">Type: </span>**integer**

-----
[alternatePhone]: #alternatephone
#### [alternatePhone]
A secondary phone number assigned to an account.  
<span class="type-label">Type: </span>**string**

-----
[brandId]: #brandid
#### [brandId]
The Brand tied to an account.  
<span class="type-label">Type: </span>**integer**

-----
[city]: #city
#### [city]
The city of the mailing address belonging to an account.  
<span class="type-label">Type: </span>**string**

-----
[claimedTaxExemptTxFlag]: #claimedtaxexempttxflag
#### [claimedTaxExemptTxFlag]
Whether an account is exempt from taxes on their invoices.  
<span class="type-label">Type: </span>**boolean**

-----
[companyName]: #companyname
#### [companyName]
The company name associated with an account.  
<span class="type-label">Type: </span>**string**

-----
[country]: #country
#### [country]
A two-letter abbreviation of the country in the mailing address belonging to an account.  
<span class="type-label">Type: </span>**string**

-----
[createDate]: #createdate
#### [createDate]
The date an account was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[deviceFingerprintId]: #devicefingerprintid
#### [deviceFingerprintId]
Device Fingerprint Identifier - Used internally and can safely be ignored.  
<span class="type-label">Type: </span>**string**

-----
[email]: #email
#### [email]
A general email address assigned to an account.  
<span class="type-label">Type: </span>**string**

-----
[faxPhone]: #faxphone
#### [faxPhone]
A fax phone number assigned to an account.  
<span class="type-label">Type: </span>**string**

-----
[firstName]: #firstname
#### [firstName]
Each customer account is listed under a single individual. This is that individual's first name.  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
A customer account's internal identifier. Account numbers are typically preceded by the string "SL" in the customer portal. Every SoftLayer account has at least one portal user whose username follows the "SL" + account number naming scheme.   
<span class="type-label">Type: </span>**integer**

-----
[isReseller]: #isreseller
#### [isReseller]
A flag indicating if an account belongs to a reseller or not.  
<span class="type-label">Type: </span>**integer**

-----
[lastName]: #lastname
#### [lastName]
Each customer account is listed under a single individual. This is that individual's last name.  
<span class="type-label">Type: </span>**string**

-----
[lateFeeProtectionFlag]: #latefeeprotectionflag
#### [lateFeeProtectionFlag]
Whether an account has late fee protection.  
<span class="type-label">Type: </span>**boolean**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date an account was last modified.  
<span class="type-label">Type: </span>**dateTime**

-----
[officePhone]: #officephone
#### [officePhone]
An office phone number assigned to an account.  
<span class="type-label">Type: </span>**string**

-----
[postalCode]: #postalcode
#### [postalCode]
The postal code of the mailing address belonging to an account.  
<span class="type-label">Type: </span>**string**

-----
[resellerLevel]: #resellerlevel
#### [resellerLevel]
The Reseller level of the account.  
<span class="type-label">Type: </span>**integer**

-----
[state]: #state
#### [state]
A two-letter abbreviation of the state in the mailing address belonging to an account. If an account does not reside in a province then this is typically blank.  
<span class="type-label">Type: </span>**string**

-----
[statusDate]: #statusdate
#### [statusDate]
The date of an account's last status change.  
<span class="type-label">Type: </span>**dateTime**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[abuseEmail]: #abuseemail
#### [abuseEmail]
An email address that is responsible for abuse and legal inquiries on behalf of an account. For instance, new legal and abuse tickets are sent to this address.  
<span class="type-label">Type: </span>**string**

-----
[abuseEmails]: #abuseemails
#### [abuseEmails]
Email addresses that are responsible for abuse and legal inquiries on behalf of an account. For instance, new legal and abuse tickets are sent to these addresses.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_AbuseEmail'>SoftLayer_Account_AbuseEmail[] </a>**

-----
[accountContacts]: #accountcontacts
#### [accountContacts]
The account contacts on an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Contact'>SoftLayer_Account_Contact[] </a>**

-----
[accountLicenses]: #accountlicenses
#### [accountLicenses]
The account software licenses owned by an account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_AccountLicense'>SoftLayer_Software_AccountLicense[] </a>**

-----
[accountLinks]: #accountlinks
#### [accountLinks]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Link'>SoftLayer_Account_Link[] </a>**

-----
[accountStatus]: #accountstatus
#### [accountStatus]
An account's status presented in a more detailed data type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Status'>SoftLayer_Account_Status </a>**

-----
[activeAccountDiscountBillingItem]: #activeaccountdiscountbillingitem
#### [activeAccountDiscountBillingItem]
The billing item associated with an account's monthly discount.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**

-----
[activeAccountLicenses]: #activeaccountlicenses
#### [activeAccountLicenses]
The active account software licenses owned by an account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_AccountLicense'>SoftLayer_Software_AccountLicense[] </a>**

-----
[activeAddresses]: #activeaddresses
#### [activeAddresses]
The active address(es) that belong to an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Address'>SoftLayer_Account_Address[] </a>**

-----
[activeAgreements]: #activeagreements
#### [activeAgreements]
All active agreements for an account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Agreement'>SoftLayer_Account_Agreement[] </a>**

-----
[activeBillingAgreements]: #activebillingagreements
#### [activeBillingAgreements]
All billing agreements for an account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Agreement'>SoftLayer_Account_Agreement[] </a>**

-----
[activeCatalystEnrollment]: #activecatalystenrollment
#### [activeCatalystEnrollment]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Catalyst_Enrollment'>SoftLayer_Catalyst_Enrollment </a>**

-----
[activeColocationContainers]: #activecolocationcontainers
#### [activeColocationContainers]
The account's active top level colocation containers.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**

-----
[activeFlexibleCreditEnrollment]: #activeflexiblecreditenrollment
#### [activeFlexibleCreditEnrollment]
[Deprecated] Please use SoftLayer_Account::activeFlexibleCreditEnrollments.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_FlexibleCredit_Enrollment'>SoftLayer_FlexibleCredit_Enrollment </a>**

-----
[activeFlexibleCreditEnrollments]: #activeflexiblecreditenrollments
#### [activeFlexibleCreditEnrollments]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_FlexibleCredit_Enrollment'>SoftLayer_FlexibleCredit_Enrollment[] </a>**

-----
[activeNotificationSubscribers]: #activenotificationsubscribers
#### [activeNotificationSubscribers]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Subscriber'>SoftLayer_Notification_Subscriber[] </a>**

-----
[activeQuotes]: #activequotes
#### [activeQuotes]
An account's non-expired quotes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Quote'>SoftLayer_Billing_Order_Quote[] </a>**

-----
[activeReservedCapacityAgreements]: #activereservedcapacityagreements
#### [activeReservedCapacityAgreements]
Active reserved capacity agreements for an account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Agreement'>SoftLayer_Account_Agreement[] </a>**

-----
[activeVirtualLicenses]: #activevirtuallicenses
#### [activeVirtualLicenses]
The virtual software licenses controlled by an account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_VirtualLicense'>SoftLayer_Software_VirtualLicense[] </a>**

-----
[adcLoadBalancers]: #adcloadbalancers
#### [adcLoadBalancers]
An account's associated load balancers.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress[] </a>**

-----
[addresses]: #addresses
#### [addresses]
All the address(es) that belong to an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Address'>SoftLayer_Account_Address[] </a>**

-----
[affiliateId]: #affiliateid
#### [affiliateId]
An affiliate identifier associated with the customer account.   
<span class="type-label">Type: </span>**string**

-----
[allBillingItems]: #allbillingitems
#### [allBillingItems]
The billing items that will be on an account's next invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**

-----
[allCommissionBillingItems]: #allcommissionbillingitems
#### [allCommissionBillingItems]
The billing items that will be on an account's next invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**

-----
[allRecurringTopLevelBillingItems]: #allrecurringtoplevelbillingitems
#### [allRecurringTopLevelBillingItems]
The billing items that will be on an account's next invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**

-----
[allRecurringTopLevelBillingItemsUnfiltered]: #allrecurringtoplevelbillingitemsunfiltered
#### [allRecurringTopLevelBillingItemsUnfiltered]
The billing items that will be on an account's next invoice. Does not consider associated items.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**

-----
[allSubnetBillingItems]: #allsubnetbillingitems
#### [allSubnetBillingItems]
The billing items that will be on an account's next invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**

-----
[allTopLevelBillingItems]: #alltoplevelbillingitems
#### [allTopLevelBillingItems]
All billing items of an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**

-----
[allTopLevelBillingItemsUnfiltered]: #alltoplevelbillingitemsunfiltered
#### [allTopLevelBillingItemsUnfiltered]
The billing items that will be on an account's next invoice. Does not consider associated items.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**

-----
[allowIbmIdSilentMigrationFlag]: #allowibmidsilentmigrationflag
#### [allowIbmIdSilentMigrationFlag]
Indicates whether this account is allowed to silently migrate to use IBMid Authentication.  
<span class="type-label">Type: </span>**boolean**

-----
[allowsBluemixAccountLinkingFlag]: #allowsbluemixaccountlinkingflag
#### [allowsBluemixAccountLinkingFlag]
Flag indicating if this account can be linked with Bluemix.  
<span class="type-label">Type: </span>**boolean**

-----
[applicationDeliveryControllers]: #applicationdeliverycontrollers
#### [applicationDeliveryControllers]
An account's associated application delivery controller records.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller'>SoftLayer_Network_Application_Delivery_Controller[] </a>**

-----
[attributes]: #attributes
#### [attributes]
The account attribute values for a SoftLayer customer account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Attribute'>SoftLayer_Account_Attribute[] </a>**

-----
[availablePublicNetworkVlans]: #availablepublicnetworkvlans
#### [availablePublicNetworkVlans]
The public network VLANs assigned to an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a>**

-----
[balance]: #balance
#### [balance]
The account balance of a SoftLayer customer account. An account's balance is the amount of money owed to SoftLayer by the account holder, returned as a floating point number with two decimal places, measured in US Dollars ($USD). A negative account balance means the account holder has overpaid and is owed money by SoftLayer.  
<span class="type-label">Type: </span>**decimal**

-----
[bandwidthAllotments]: #bandwidthallotments
#### [bandwidthAllotments]
The bandwidth allotments for an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment[] </a>**

-----
[bandwidthAllotmentsOverAllocation]: #bandwidthallotmentsoverallocation
#### [bandwidthAllotmentsOverAllocation]
The bandwidth allotments for an account currently over allocation.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment[] </a>**

-----
[bandwidthAllotmentsProjectedOverAllocation]: #bandwidthallotmentsprojectedoverallocation
#### [bandwidthAllotmentsProjectedOverAllocation]
The bandwidth allotments for an account projected to go over allocation.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment[] </a>**

-----
[bareMetalInstances]: #baremetalinstances
#### [bareMetalInstances]
An account's associated bare metal server objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[billingAgreements]: #billingagreements
#### [billingAgreements]
All billing agreements for an account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Agreement'>SoftLayer_Account_Agreement[] </a>**

-----
[billingInfo]: #billinginfo
#### [billingInfo]
An account's billing information.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Info'>SoftLayer_Billing_Info </a>**

-----
[blockDeviceTemplateGroups]: #blockdevicetemplategroups
#### [blockDeviceTemplateGroups]
Private template group objects (parent and children) and the shared template group objects (parent only) for an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group'>SoftLayer_Virtual_Guest_Block_Device_Template_Group[] </a>**

-----
[bluemixAccountLink]: #bluemixaccountlink
#### [bluemixAccountLink]
The Bluemix account link associated with this SoftLayer account, if one exists.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Link_Bluemix'>SoftLayer_Account_Link_Bluemix </a>**

-----
[bluemixLinkedFlag]: #bluemixlinkedflag
#### [bluemixLinkedFlag]
Returns true if this account is linked to IBM Bluemix, false if not.  
<span class="type-label">Type: </span>**boolean**

-----
[brand]: #brand
#### [brand]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand'>SoftLayer_Brand </a>**

-----
[brandAccountFlag]: #brandaccountflag
#### [brandAccountFlag]
  
<span class="type-label">Type: </span>**boolean**

-----
[brandKeyName]: #brandkeyname
#### [brandKeyName]
The brand keyName.  
<span class="type-label">Type: </span>**string**

-----
[businessPartner]: #businesspartner
#### [businessPartner]
The Business Partner details for the account. Country Enterprise Code, Channel, Segment, Reseller Level.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Business_Partner'>SoftLayer_Account_Business_Partner </a>**

-----
[canOrderAdditionalVlansFlag]: #canorderadditionalvlansflag
#### [canOrderAdditionalVlansFlag]
[DEPRECATED] All accounts may order VLANs.  
<span class="type-label">Type: </span>**boolean**

-----
[carts]: #carts
#### [carts]
An account's active carts.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Quote'>SoftLayer_Billing_Order_Quote[] </a>**

-----
[catalystEnrollments]: #catalystenrollments
#### [catalystEnrollments]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Catalyst_Enrollment'>SoftLayer_Catalyst_Enrollment[] </a>**

-----
[closedTickets]: #closedtickets
#### [closedTickets]
All closed tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**

-----
[datacentersWithSubnetAllocations]: #datacenterswithsubnetallocations
#### [datacentersWithSubnetAllocations]
Datacenters which contain subnets that the account has access to route.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location[] </a>**

-----
[dedicatedHosts]: #dedicatedhosts
#### [dedicatedHosts]
An account's associated virtual dedicated host objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_DedicatedHost'>SoftLayer_Virtual_DedicatedHost[] </a>**

-----
[disablePaymentProcessingFlag]: #disablepaymentprocessingflag
#### [disablePaymentProcessingFlag]
A flag indicating whether payments are processed for this account.  
<span class="type-label">Type: </span>**boolean**

-----
[displaySupportRepresentativeAssignments]: #displaysupportrepresentativeassignments
#### [displaySupportRepresentativeAssignments]
The SoftLayer employees that an account is assigned to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Attachment_Employee'>SoftLayer_Account_Attachment_Employee[] </a>**

-----
[domainRegistrations]: #domainregistrations
#### [domainRegistrations]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Domain_Registration'>SoftLayer_Dns_Domain_Registration[] </a>**

-----
[domains]: #domains
#### [domains]
The DNS domains associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Domain'>SoftLayer_Dns_Domain[] </a>**

-----
[domainsWithoutSecondaryDnsRecords]: #domainswithoutsecondarydnsrecords
#### [domainsWithoutSecondaryDnsRecords]
The DNS domains associated with an account that were not created as a result of a secondary DNS zone transfer.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Domain'>SoftLayer_Dns_Domain[] </a>**

-----
[euSupportedFlag]: #eusupportedflag
#### [euSupportedFlag]
Boolean flag dictating whether or not this account has the EU Supported flag. This flag indicates that this account uses IBM Cloud services to process EU citizen's personal data.  
<span class="type-label">Type: </span>**boolean**

-----
[evaultCapacityGB]: #evaultcapacitygb
#### [evaultCapacityGB]
The total capacity of Legacy EVault Volumes on an account, in GB.  
<span class="type-label">Type: </span>**unsigned integer**

-----
[evaultMasterUsers]: #evaultmasterusers
#### [evaultMasterUsers]
An account's master EVault user. This is only used when an account has EVault service.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Password'>SoftLayer_Account_Password[] </a>**

-----
[evaultNetworkStorage]: #evaultnetworkstorage
#### [evaultNetworkStorage]
An account's associated EVault storage volumes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[expiredSecurityCertificates]: #expiredsecuritycertificates
#### [expiredSecurityCertificates]
Stored security certificates that are expired (ie. SSL)  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Certificate'>SoftLayer_Security_Certificate[] </a>**

-----
[facilityLogs]: #facilitylogs
#### [facilityLogs]
Logs of who entered a colocation area which is assigned to this account, or when a user under this account enters a datacenter.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Access_Facility_Log'>SoftLayer_User_Access_Facility_Log[] </a>**

-----
[fileBlockBetaAccessFlag]: #fileblockbetaaccessflag
#### [fileBlockBetaAccessFlag]
  
<span class="type-label">Type: </span>**boolean**

-----
[flexibleCreditEnrollments]: #flexiblecreditenrollments
#### [flexibleCreditEnrollments]
All of the account's current and former Flexible Credit enrollments.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_FlexibleCredit_Enrollment'>SoftLayer_FlexibleCredit_Enrollment[] </a>**

-----
[forcePaasAccountLinkDate]: #forcepaasaccountlinkdate
#### [forcePaasAccountLinkDate]
Timestamp representing the point in time when an account is required to link with PaaS.  
<span class="type-label">Type: </span>**string**

-----
[globalIpRecords]: #globaliprecords
#### [globalIpRecords]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress_Global'>SoftLayer_Network_Subnet_IpAddress_Global[] </a>**

-----
[globalIpv4Records]: #globalipv4records
#### [globalIpv4Records]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress_Global'>SoftLayer_Network_Subnet_IpAddress_Global[] </a>**

-----
[globalIpv6Records]: #globalipv6records
#### [globalIpv6Records]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress_Global'>SoftLayer_Network_Subnet_IpAddress_Global[] </a>**

-----
[globalLoadBalancerAccounts]: #globalloadbalanceraccounts
#### [globalLoadBalancerAccounts]
The global load balancer accounts for a softlayer customer account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Global_Account'>SoftLayer_Network_LoadBalancer_Global_Account[] </a>**

-----
[hardware]: #hardware
#### [hardware]
An account's associated hardware objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[hardwareOverBandwidthAllocation]: #hardwareoverbandwidthallocation
#### [hardwareOverBandwidthAllocation]
An account's associated hardware objects currently over bandwidth allocation.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[hardwareProjectedOverBandwidthAllocation]: #hardwareprojectedoverbandwidthallocation
#### [hardwareProjectedOverBandwidthAllocation]
An account's associated hardware objects projected to go over bandwidth allocation.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[hardwareWithCpanel]: #hardwarewithcpanel
#### [hardwareWithCpanel]
All hardware associated with an account that has the cPanel web hosting control panel installed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[hardwareWithHelm]: #hardwarewithhelm
#### [hardwareWithHelm]
All hardware associated with an account that has the Helm web hosting control panel installed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[hardwareWithMcafee]: #hardwarewithmcafee
#### [hardwareWithMcafee]
All hardware associated with an account that has McAfee Secure software components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[hardwareWithMcafeeAntivirusRedhat]: #hardwarewithmcafeeantivirusredhat
#### [hardwareWithMcafeeAntivirusRedhat]
All hardware associated with an account that has McAfee Secure AntiVirus for Redhat software components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[hardwareWithMcafeeAntivirusWindows]: #hardwarewithmcafeeantiviruswindows
#### [hardwareWithMcafeeAntivirusWindows]
All hardware associated with an account that has McAfee Secure AntiVirus for Windows software components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[hardwareWithMcafeeIntrusionDetectionSystem]: #hardwarewithmcafeeintrusiondetectionsystem
#### [hardwareWithMcafeeIntrusionDetectionSystem]
All hardware associated with an account that has McAfee Secure Intrusion Detection System software components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[hardwareWithPlesk]: #hardwarewithplesk
#### [hardwareWithPlesk]
All hardware associated with an account that has the Plesk web hosting control panel installed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[hardwareWithQuantastor]: #hardwarewithquantastor
#### [hardwareWithQuantastor]
All hardware associated with an account that has the QuantaStor storage system installed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[hardwareWithUrchin]: #hardwarewithurchin
#### [hardwareWithUrchin]
All hardware associated with an account that has the Urchin web traffic analytics package installed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[hardwareWithWindows]: #hardwarewithwindows
#### [hardwareWithWindows]
All hardware associated with an account that is running a version of the Microsoft Windows operating system.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[hasEvaultBareMetalRestorePluginFlag]: #hasevaultbaremetalrestorepluginflag
#### [hasEvaultBareMetalRestorePluginFlag]
Return 1 if one of the account's hardware has the EVault Bare Metal Server Restore Plugin otherwise 0.  
<span class="type-label">Type: </span>**boolean**

-----
[hasIderaBareMetalRestorePluginFlag]: #hasiderabaremetalrestorepluginflag
#### [hasIderaBareMetalRestorePluginFlag]
Return 1 if one of the account's hardware has an installation of Idera Server Backup otherwise 0.  
<span class="type-label">Type: </span>**boolean**

-----
[hasPendingOrder]: #haspendingorder
#### [hasPendingOrder]
The number of orders in a PENDING status for a SoftLayer customer account.  
<span class="type-label">Type: </span>**unsigned integer**

-----
[hasR1softBareMetalRestorePluginFlag]: #hasr1softbaremetalrestorepluginflag
#### [hasR1softBareMetalRestorePluginFlag]
Return 1 if one of the account's hardware has an installation of R1Soft CDP otherwise 0.  
<span class="type-label">Type: </span>**boolean**

-----
[hourlyBareMetalInstances]: #hourlybaremetalinstances
#### [hourlyBareMetalInstances]
An account's associated hourly bare metal server objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[hourlyServiceBillingItems]: #hourlyservicebillingitems
#### [hourlyServiceBillingItems]
Hourly service billing items that will be on an account's next invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**

-----
[hourlyVirtualGuests]: #hourlyvirtualguests
#### [hourlyVirtualGuests]
An account's associated hourly virtual guest objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[hubNetworkStorage]: #hubnetworkstorage
#### [hubNetworkStorage]
An account's associated Virtual Storage volumes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[ibmCustomerNumber]: #ibmcustomernumber
#### [ibmCustomerNumber]
Unique identifier for a customer used throughout IBM.  
<span class="type-label">Type: </span>**string**

-----
[ibmIdAuthenticationRequiredFlag]: #ibmidauthenticationrequiredflag
#### [ibmIdAuthenticationRequiredFlag]
Indicates whether this account requires IBMid authentication.  
<span class="type-label">Type: </span>**boolean**

-----
[ibmIdMigrationExpirationTimestamp]: #ibmidmigrationexpirationtimestamp
#### [ibmIdMigrationExpirationTimestamp]
This key is deprecated and should not be used.  
<span class="type-label">Type: </span>**string**

-----
[inProgressExternalAccountSetup]: #inprogressexternalaccountsetup
#### [inProgressExternalAccountSetup]
An in progress request to switch billing systems.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_External_Setup'>SoftLayer_Account_External_Setup </a>**

-----
[internalNotes]: #internalnotes
#### [internalNotes]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Note'>SoftLayer_Account_Note[] </a>**

-----
[invoices]: #invoices
#### [invoices]
An account's associated billing invoices.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice[] </a>**

-----
[ipAddresses]: #ipaddresses
#### [ipAddresses]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>**

-----
[iscsiIsolationDisabled]: #iscsiisolationdisabled
#### [iscsiIsolationDisabled]
  
<span class="type-label">Type: </span>**boolean**

-----
[iscsiNetworkStorage]: #iscsinetworkstorage
#### [iscsiNetworkStorage]
An account's associated iSCSI storage volumes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[lastCanceledBillingItem]: #lastcanceledbillingitem
#### [lastCanceledBillingItem]
The most recently canceled billing item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**

-----
[lastCancelledServerBillingItem]: #lastcancelledserverbillingitem
#### [lastCancelledServerBillingItem]
The most recent cancelled server billing item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**

-----
[lastFiveClosedAbuseTickets]: #lastfiveclosedabusetickets
#### [lastFiveClosedAbuseTickets]
The five most recently closed abuse tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**

-----
[lastFiveClosedAccountingTickets]: #lastfiveclosedaccountingtickets
#### [lastFiveClosedAccountingTickets]
The five most recently closed accounting tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**

-----
[lastFiveClosedOtherTickets]: #lastfiveclosedothertickets
#### [lastFiveClosedOtherTickets]
The five most recently closed tickets that do not belong to the abuse, accounting, sales, or support groups associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**

-----
[lastFiveClosedSalesTickets]: #lastfiveclosedsalestickets
#### [lastFiveClosedSalesTickets]
The five most recently closed sales tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**

-----
[lastFiveClosedSupportTickets]: #lastfiveclosedsupporttickets
#### [lastFiveClosedSupportTickets]
The five most recently closed support tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**

-----
[lastFiveClosedTickets]: #lastfiveclosedtickets
#### [lastFiveClosedTickets]
The five most recently closed tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**

-----
[latestBillDate]: #latestbilldate
#### [latestBillDate]
An account's most recent billing date.  
<span class="type-label">Type: </span>**dateTime**

-----
[latestRecurringInvoice]: #latestrecurringinvoice
#### [latestRecurringInvoice]
An account's latest recurring invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice </a>**

-----
[latestRecurringPendingInvoice]: #latestrecurringpendinginvoice
#### [latestRecurringPendingInvoice]
An account's latest recurring pending invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice </a>**

-----
[legacyBandwidthAllotments]: #legacybandwidthallotments
#### [legacyBandwidthAllotments]
The legacy bandwidth allotments for an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment[] </a>**

-----
[legacyIscsiCapacityGB]: #legacyiscsicapacitygb
#### [legacyIscsiCapacityGB]
The total capacity of Legacy iSCSI Volumes on an account, in GB.  
<span class="type-label">Type: </span>**unsigned integer**

-----
[loadBalancers]: #loadbalancers
#### [loadBalancers]
An account's associated load balancers.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_LoadBalancer_VirtualIpAddress[] </a>**

-----
[lockboxCapacityGB]: #lockboxcapacitygb
#### [lockboxCapacityGB]
The total capacity of Legacy lockbox Volumes on an account, in GB.  
<span class="type-label">Type: </span>**unsigned integer**

-----
[lockboxNetworkStorage]: #lockboxnetworkstorage
#### [lockboxNetworkStorage]
An account's associated Lockbox storage volumes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[manualPaymentsUnderReview]: #manualpaymentsunderreview
#### [manualPaymentsUnderReview]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Payment_Card_ManualPayment'>SoftLayer_Billing_Payment_Card_ManualPayment[] </a>**

-----
[masterUser]: #masteruser
#### [masterUser]
An account's master user.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**

-----
[mediaDataTransferRequests]: #mediadatatransferrequests
#### [mediaDataTransferRequests]
An account's media transfer service requests.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Media_Data_Transfer_Request'>SoftLayer_Account_Media_Data_Transfer_Request[] </a>**

-----
[migratedToIbmCloudPortalFlag]: #migratedtoibmcloudportalflag
#### [migratedToIbmCloudPortalFlag]
Flag indicating whether this account is restricted to the IBM Cloud portal.  
<span class="type-label">Type: </span>**boolean**

-----
[monthlyBareMetalInstances]: #monthlybaremetalinstances
#### [monthlyBareMetalInstances]
An account's associated monthly bare metal server objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[monthlyVirtualGuests]: #monthlyvirtualguests
#### [monthlyVirtualGuests]
An account's associated monthly virtual guest objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[nasNetworkStorage]: #nasnetworkstorage
#### [nasNetworkStorage]
An account's associated NAS storage volumes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[networkCreationFlag]: #networkcreationflag
#### [networkCreationFlag]
Whether or not this account can define their own networks.  
<span class="type-label">Type: </span>**boolean**

-----
[networkGateways]: #networkgateways
#### [networkGateways]
All network gateway devices on this account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway[] </a>**

-----
[networkHardware]: #networkhardware
#### [networkHardware]
An account's associated network hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[networkMessageDeliveryAccounts]: #networkmessagedeliveryaccounts
#### [networkMessageDeliveryAccounts]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Message_Delivery'>SoftLayer_Network_Message_Delivery[] </a>**

-----
[networkMonitorDownHardware]: #networkmonitordownhardware
#### [networkMonitorDownHardware]
Hardware which is currently experiencing a service failure.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[networkMonitorDownVirtualGuests]: #networkmonitordownvirtualguests
#### [networkMonitorDownVirtualGuests]
Virtual guest which is currently experiencing a service failure.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[networkMonitorRecoveringHardware]: #networkmonitorrecoveringhardware
#### [networkMonitorRecoveringHardware]
Hardware which is currently recovering from a service failure.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[networkMonitorRecoveringVirtualGuests]: #networkmonitorrecoveringvirtualguests
#### [networkMonitorRecoveringVirtualGuests]
Virtual guest which is currently recovering from a service failure.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[networkMonitorUpHardware]: #networkmonitoruphardware
#### [networkMonitorUpHardware]
Hardware which is currently online.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[networkMonitorUpVirtualGuests]: #networkmonitorupvirtualguests
#### [networkMonitorUpVirtualGuests]
Virtual guest which is currently online.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[networkStorage]: #networkstorage
#### [networkStorage]
An account's associated storage volumes. This includes Lockbox, NAS, EVault, and iSCSI volumes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[networkStorageGroups]: #networkstoragegroups
#### [networkStorageGroups]
An account's Network Storage groups.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Group'>SoftLayer_Network_Storage_Group[] </a>**

-----
[networkTunnelContexts]: #networktunnelcontexts
#### [networkTunnelContexts]
IPSec network tunnels for an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context'>SoftLayer_Network_Tunnel_Module_Context[] </a>**

-----
[networkVlanSpan]: #networkvlanspan
#### [networkVlanSpan]
Whether or not an account has automatic private VLAN spanning enabled.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Network_Vlan_Span'>SoftLayer_Account_Network_Vlan_Span </a>**

-----
[networkVlans]: #networkvlans
#### [networkVlans]
All network VLANs assigned to an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a>**

-----
[nextBillingPublicAllotmentHardwareBandwidthDetails]: #nextbillingpublicallotmenthardwarebandwidthdetails
#### [nextBillingPublicAllotmentHardwareBandwidthDetails]
DEPRECATED - This information can be pulled directly through tapping keys now - DEPRECATED. The allotments for this account and their servers for the next billing cycle. The public inbound and outbound bandwidth is calculated for each server in addition to the daily average network traffic since the last billing date.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment[] </a>**

-----
[nextInvoiceIncubatorExemptTotal]: #nextinvoiceincubatorexempttotal
#### [nextInvoiceIncubatorExemptTotal]
The pre-tax total amount exempt from incubator credit for the account's next invoice. This field is now deprecated and will soon be removed. Please update all references to instead use nextInvoiceTotalAmount  
<span class="type-label">Type: </span>**decimal**

-----
[nextInvoiceRecurringAmountEligibleForAccountDiscount]: #nextinvoicerecurringamounteligibleforaccountdiscount
#### [nextInvoiceRecurringAmountEligibleForAccountDiscount]
The total recurring charge amount of an account's next invoice eligible for account discount measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.  
<span class="type-label">Type: </span>**decimal**

-----
[nextInvoiceTopLevelBillingItems]: #nextinvoicetoplevelbillingitems
#### [nextInvoiceTopLevelBillingItems]
The billing items that will be on an account's next invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**

-----
[nextInvoiceTotalAmount]: #nextinvoicetotalamount
#### [nextInvoiceTotalAmount]
The pre-tax total amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.  
<span class="type-label">Type: </span>**float**

-----
[nextInvoiceTotalOneTimeAmount]: #nextinvoicetotalonetimeamount
#### [nextInvoiceTotalOneTimeAmount]
The total one-time charge amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.  
<span class="type-label">Type: </span>**decimal**

-----
[nextInvoiceTotalOneTimeTaxAmount]: #nextinvoicetotalonetimetaxamount
#### [nextInvoiceTotalOneTimeTaxAmount]
The total one-time tax amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.  
<span class="type-label">Type: </span>**decimal**

-----
[nextInvoiceTotalRecurringAmount]: #nextinvoicetotalrecurringamount
#### [nextInvoiceTotalRecurringAmount]
The total recurring charge amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.  
<span class="type-label">Type: </span>**decimal**

-----
[nextInvoiceTotalRecurringAmountBeforeAccountDiscount]: #nextinvoicetotalrecurringamountbeforeaccountdiscount
#### [nextInvoiceTotalRecurringAmountBeforeAccountDiscount]
The total recurring charge amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.  
<span class="type-label">Type: </span>**decimal**

-----
[nextInvoiceTotalRecurringTaxAmount]: #nextinvoicetotalrecurringtaxamount
#### [nextInvoiceTotalRecurringTaxAmount]
The total recurring tax amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.  
<span class="type-label">Type: </span>**float**

-----
[nextInvoiceTotalTaxableRecurringAmount]: #nextinvoicetotaltaxablerecurringamount
#### [nextInvoiceTotalTaxableRecurringAmount]
The total recurring charge amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.  
<span class="type-label">Type: </span>**decimal**

-----
[notificationSubscribers]: #notificationsubscribers
#### [notificationSubscribers]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Subscriber'>SoftLayer_Notification_Subscriber[] </a>**

-----
[openAbuseTickets]: #openabusetickets
#### [openAbuseTickets]
The open abuse tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**

-----
[openAccountingTickets]: #openaccountingtickets
#### [openAccountingTickets]
The open accounting tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**

-----
[openBillingTickets]: #openbillingtickets
#### [openBillingTickets]
The open billing tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**

-----
[openCancellationRequests]: #opencancellationrequests
#### [openCancellationRequests]
An open ticket requesting cancellation of this server, if one exists.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request'>SoftLayer_Billing_Item_Cancellation_Request[] </a>**

-----
[openOtherTickets]: #openothertickets
#### [openOtherTickets]
The open tickets that do not belong to the abuse, accounting, sales, or support groups associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**

-----
[openRecurringInvoices]: #openrecurringinvoices
#### [openRecurringInvoices]
An account's recurring invoices.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice[] </a>**

-----
[openSalesTickets]: #opensalestickets
#### [openSalesTickets]
The open sales tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**

-----
[openStackAccountLinks]: #openstackaccountlinks
#### [openStackAccountLinks]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Link'>SoftLayer_Account_Link[] </a>**

-----
[openStackObjectStorage]: #openstackobjectstorage
#### [openStackObjectStorage]
An account's associated Openstack related Object Storage accounts.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[openSupportTickets]: #opensupporttickets
#### [openSupportTickets]
The open support tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**

-----
[openTickets]: #opentickets
#### [openTickets]
All open tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**

-----
[openTicketsWaitingOnCustomer]: #openticketswaitingoncustomer
#### [openTicketsWaitingOnCustomer]
All open tickets associated with an account last edited by an employee.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**

-----
[orders]: #orders
#### [orders]
An account's associated billing orders excluding upgrades.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order'>SoftLayer_Billing_Order[] </a>**

-----
[orphanBillingItems]: #orphanbillingitems
#### [orphanBillingItems]
The billing items that have no parent billing item. These are items that don't necessarily belong to a single server.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**

-----
[ownedBrands]: #ownedbrands
#### [ownedBrands]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand'>SoftLayer_Brand[] </a>**

-----
[ownedHardwareGenericComponentModels]: #ownedhardwaregenericcomponentmodels
#### [ownedHardwareGenericComponentModels]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Generic'>SoftLayer_Hardware_Component_Model_Generic[] </a>**

-----
[paymentProcessors]: #paymentprocessors
#### [paymentProcessors]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Payment_Processor'>SoftLayer_Billing_Payment_Processor[] </a>**

-----
[pendingEvents]: #pendingevents
#### [pendingEvents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Event'>SoftLayer_Notification_Occurrence_Event[] </a>**

-----
[pendingInvoice]: #pendinginvoice
#### [pendingInvoice]
An account's latest open (pending) invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice </a>**

-----
[pendingInvoiceTopLevelItems]: #pendinginvoicetoplevelitems
#### [pendingInvoiceTopLevelItems]
A list of top-level invoice items that are on an account's currently pending invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item[] </a>**

-----
[pendingInvoiceTotalAmount]: #pendinginvoicetotalamount
#### [pendingInvoiceTotalAmount]
The total amount of an account's pending invoice, if one exists.  
<span class="type-label">Type: </span>**decimal**

-----
[pendingInvoiceTotalOneTimeAmount]: #pendinginvoicetotalonetimeamount
#### [pendingInvoiceTotalOneTimeAmount]
The total one-time charges for an account's pending invoice, if one exists. In other words, it is the sum of one-time charges, setup fees, and labor fees. It does not include taxes.  
<span class="type-label">Type: </span>**decimal**

-----
[pendingInvoiceTotalOneTimeTaxAmount]: #pendinginvoicetotalonetimetaxamount
#### [pendingInvoiceTotalOneTimeTaxAmount]
The sum of all the taxes related to one time charges for an account's pending invoice, if one exists.  
<span class="type-label">Type: </span>**decimal**

-----
[pendingInvoiceTotalRecurringAmount]: #pendinginvoicetotalrecurringamount
#### [pendingInvoiceTotalRecurringAmount]
The total recurring amount of an account's pending invoice, if one exists.  
<span class="type-label">Type: </span>**decimal**

-----
[pendingInvoiceTotalRecurringTaxAmount]: #pendinginvoicetotalrecurringtaxamount
#### [pendingInvoiceTotalRecurringTaxAmount]
The total amount of the recurring taxes on an account's pending invoice, if one exists.  
<span class="type-label">Type: </span>**decimal**

-----
[permissionGroups]: #permissiongroups
#### [permissionGroups]
An account's permission groups.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Permission_Group'>SoftLayer_User_Permission_Group[] </a>**

-----
[permissionRoles]: #permissionroles
#### [permissionRoles]
An account's user roles.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Permission_Role'>SoftLayer_User_Permission_Role[] </a>**

-----
[placementGroups]: #placementgroups
#### [placementGroups]
An account's associated virtual placement groups.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_PlacementGroup'>SoftLayer_Virtual_PlacementGroup[] </a>**

-----
[portableStorageVolumes]: #portablestoragevolumes
#### [portableStorageVolumes]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image'>SoftLayer_Virtual_Disk_Image[] </a>**

-----
[postProvisioningHooks]: #postprovisioninghooks
#### [postProvisioningHooks]
Customer specified URIs that are downloaded onto a newly provisioned or reloaded server. If the URI is sent over https it will be executed directly on the server.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Hook'>SoftLayer_Provisioning_Hook[] </a>**

-----
[pptpVpnAllowedFlag]: #pptpvpnallowedflag
#### [pptpVpnAllowedFlag]
Boolean flag dictating whether or not this account supports PPTP VPN Access.  
<span class="type-label">Type: </span>**boolean**

-----
[pptpVpnUsers]: #pptpvpnusers
#### [pptpVpnUsers]
An account's associated portal users with PPTP VPN access. (Deprecated)  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer[] </a>**

-----
[previousRecurringRevenue]: #previousrecurringrevenue
#### [previousRecurringRevenue]
The total recurring amount for an accounts previous revenue.  
<span class="type-label">Type: </span>**decimal**

-----
[priceRestrictions]: #pricerestrictions
#### [priceRestrictions]
The item price that an account is restricted to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price_Account_Restriction'>SoftLayer_Product_Item_Price_Account_Restriction[] </a>**

-----
[priorityOneTickets]: #priorityonetickets
#### [priorityOneTickets]
All priority one tickets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**

-----
[privateAllotmentHardwareBandwidthDetails]: #privateallotmenthardwarebandwidthdetails
#### [privateAllotmentHardwareBandwidthDetails]
DEPRECATED - This information can be pulled directly through tapping keys now - DEPRECATED. The allotments for this account and their servers. The private inbound and outbound bandwidth is calculated for each server in addition to the daily average network traffic since the last billing date.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment[] </a>**

-----
[privateBlockDeviceTemplateGroups]: #privateblockdevicetemplategroups
#### [privateBlockDeviceTemplateGroups]
Private and shared template group objects (parent only) for an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group'>SoftLayer_Virtual_Guest_Block_Device_Template_Group[] </a>**

-----
[privateIpAddresses]: #privateipaddresses
#### [privateIpAddresses]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>**

-----
[privateNetworkVlans]: #privatenetworkvlans
#### [privateNetworkVlans]
The private network VLANs assigned to an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a>**

-----
[privateSubnets]: #privatesubnets
#### [privateSubnets]
All private subnets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**

-----
[proofOfConceptAccountFlag]: #proofofconceptaccountflag
#### [proofOfConceptAccountFlag]
Boolean flag indicating whether or not this account is a Proof of Concept account.  
<span class="type-label">Type: </span>**boolean**

-----
[publicAllotmentHardwareBandwidthDetails]: #publicallotmenthardwarebandwidthdetails
#### [publicAllotmentHardwareBandwidthDetails]
DEPRECATED - This information can be pulled directly through tapping keys now - DEPRECATED. The allotments for this account and their servers. The public inbound and outbound bandwidth is calculated for each server in addition to the daily average network traffic since the last billing date.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment[] </a>**

-----
[publicIpAddresses]: #publicipaddresses
#### [publicIpAddresses]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>**

-----
[publicNetworkVlans]: #publicnetworkvlans
#### [publicNetworkVlans]
The public network VLANs assigned to an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a>**

-----
[publicSubnets]: #publicsubnets
#### [publicSubnets]
All public network subnets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**

-----
[quotes]: #quotes
#### [quotes]
An account's quotes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Quote'>SoftLayer_Billing_Order_Quote[] </a>**

-----
[recentEvents]: #recentevents
#### [recentEvents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Event'>SoftLayer_Notification_Occurrence_Event[] </a>**

-----
[referralPartner]: #referralpartner
#### [referralPartner]
The Referral Partner for this account, if any.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[referredAccounts]: #referredaccounts
#### [referredAccounts]
If this is a account is a referral partner, the accounts this referral partner has referred  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account[] </a>**

-----
[regulatedWorkloads]: #regulatedworkloads
#### [regulatedWorkloads]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Legal_RegulatedWorkload'>SoftLayer_Legal_RegulatedWorkload[] </a>**

-----
[remoteManagementCommandRequests]: #remotemanagementcommandrequests
#### [remoteManagementCommandRequests]
Remote management command requests for an account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_Command_Request'>SoftLayer_Hardware_Component_RemoteManagement_Command_Request[] </a>**

-----
[replicationEvents]: #replicationevents
#### [replicationEvents]
The Replication events for all Network Storage volumes on an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Event'>SoftLayer_Network_Storage_Event[] </a>**

-----
[requireSilentIBMidUserCreation]: #requiresilentibmidusercreation
#### [requireSilentIBMidUserCreation]
Indicates whether newly created users under this account will be associated with IBMid via an email requiring a response, or not.  
<span class="type-label">Type: </span>**boolean**

-----
[reservedCapacityAgreements]: #reservedcapacityagreements
#### [reservedCapacityAgreements]
All reserved capacity agreements for an account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Agreement'>SoftLayer_Account_Agreement[] </a>**

-----
[reservedCapacityGroups]: #reservedcapacitygroups
#### [reservedCapacityGroups]
The reserved capacity groups owned by this account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_ReservedCapacityGroup'>SoftLayer_Virtual_ReservedCapacityGroup[] </a>**

-----
[resourceGroups]: #resourcegroups
#### [resourceGroups]
An account's associated top-level resource groups.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group'>SoftLayer_Resource_Group[] </a>**

-----
[routers]: #routers
#### [routers]
All Routers that an accounts VLANs reside on  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[rwhoisData]: #rwhoisdata
#### [rwhoisData]
An account's reverse WHOIS data. This data is used when making SWIP requests.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_Rwhois_Data'>SoftLayer_Network_Subnet_Rwhois_Data </a>**

-----
[samlAuthentication]: #samlauthentication
#### [samlAuthentication]
The SAML configuration for this account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Authentication_Saml'>SoftLayer_Account_Authentication_Saml </a>**

-----
[scaleGroups]: #scalegroups
#### [scaleGroups]
All scale groups on this account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Group'>SoftLayer_Scale_Group[] </a>**

-----
[secondaryDomains]: #secondarydomains
#### [secondaryDomains]
The secondary DNS records for a SoftLayer customer account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Dns_Secondary'>SoftLayer_Dns_Secondary[] </a>**

-----
[securityCertificates]: #securitycertificates
#### [securityCertificates]
Stored security certificates (ie. SSL)  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Certificate'>SoftLayer_Security_Certificate[] </a>**

-----
[securityGroups]: #securitygroups
#### [securityGroups]
The security groups belonging to this account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_SecurityGroup'>SoftLayer_Network_SecurityGroup[] </a>**

-----
[securityLevel]: #securitylevel
#### [securityLevel]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Level'>SoftLayer_Security_Level </a>**

-----
[securityScanRequests]: #securityscanrequests
#### [securityScanRequests]
An account's vulnerability scan requests.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Security_Scanner_Request'>SoftLayer_Network_Security_Scanner_Request[] </a>**

-----
[serviceBillingItems]: #servicebillingitems
#### [serviceBillingItems]
The service billing items that will be on an account's next invoice.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**

-----
[shipments]: #shipments
#### [shipments]
Shipments that belong to the customer's account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Shipment'>SoftLayer_Account_Shipment[] </a>**

-----
[sshKeys]: #sshkeys
#### [sshKeys]
Customer specified SSH keys that can be implemented onto a newly provisioned or reloaded server.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Ssh_Key'>SoftLayer_Security_Ssh_Key[] </a>**

-----
[sslVpnUsers]: #sslvpnusers
#### [sslVpnUsers]
An account's associated portal users with SSL VPN access.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer[] </a>**

-----
[standardPoolVirtualGuests]: #standardpoolvirtualguests
#### [standardPoolVirtualGuests]
An account's virtual guest objects that are hosted on a user provisioned hypervisor.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[subnetRegistrationDetails]: #subnetregistrationdetails
#### [subnetRegistrationDetails]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail'>SoftLayer_Account_Regional_Registry_Detail[] </a>**

-----
[subnetRegistrations]: #subnetregistrations
#### [subnetRegistrations]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration'>SoftLayer_Network_Subnet_Registration[] </a>**

-----
[subnets]: #subnets
#### [subnets]
All network subnets associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**

-----
[supportRepresentatives]: #supportrepresentatives
#### [supportRepresentatives]
The SoftLayer employees that an account is assigned to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee[] </a>**

-----
[supportSubscriptions]: #supportsubscriptions
#### [supportSubscriptions]
The active support subscriptions for this account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**

-----
[supportTier]: #supporttier
#### [supportTier]
  
<span class="type-label">Type: </span>**string**

-----
[suppressInvoicesFlag]: #suppressinvoicesflag
#### [suppressInvoicesFlag]
A flag indicating to suppress invoices.  
<span class="type-label">Type: </span>**boolean**

-----
[tags]: #tags
#### [tags]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Tag'>SoftLayer_Tag[] </a>**

-----
[tickets]: #tickets
#### [tickets]
An account's associated tickets.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**

-----
[ticketsClosedInTheLastThreeDays]: #ticketsclosedinthelastthreedays
#### [ticketsClosedInTheLastThreeDays]
Tickets closed within the last 72 hours or last 10 tickets, whichever is less, associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**

-----
[ticketsClosedToday]: #ticketsclosedtoday
#### [ticketsClosedToday]
Tickets closed today associated with an account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**

-----
[transcodeAccounts]: #transcodeaccounts
#### [transcodeAccounts]
An account's associated Transcode account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Media_Transcode_Account'>SoftLayer_Network_Media_Transcode_Account[] </a>**

-----
[upgradeRequests]: #upgraderequests
#### [upgradeRequests]
An account's associated upgrade requests.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Upgrade_Request'>SoftLayer_Product_Upgrade_Request[] </a>**

-----
[users]: #users
#### [users]
An account's portal users.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer[] </a>**

-----
[validSecurityCertificates]: #validsecuritycertificates
#### [validSecurityCertificates]
Stored security certificates that are not expired (ie. SSL)  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Certificate'>SoftLayer_Security_Certificate[] </a>**

-----
[vdrUpdatesInProgressFlag]: #vdrupdatesinprogressflag
#### [vdrUpdatesInProgressFlag]
Return 0 if vpn updates are currently in progress on this account otherwise 1.  
<span class="type-label">Type: </span>**boolean**

-----
[virtualDedicatedRacks]: #virtualdedicatedracks
#### [virtualDedicatedRacks]
The bandwidth pooling for this account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment[] </a>**

-----
[virtualDiskImages]: #virtualdiskimages
#### [virtualDiskImages]
An account's associated virtual server virtual disk images.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image'>SoftLayer_Virtual_Disk_Image[] </a>**

-----
[virtualGuests]: #virtualguests
#### [virtualGuests]
An account's associated virtual guest objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[virtualGuestsOverBandwidthAllocation]: #virtualguestsoverbandwidthallocation
#### [virtualGuestsOverBandwidthAllocation]
An account's associated virtual guest objects currently over bandwidth allocation.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[virtualGuestsProjectedOverBandwidthAllocation]: #virtualguestsprojectedoverbandwidthallocation
#### [virtualGuestsProjectedOverBandwidthAllocation]
An account's associated virtual guest objects currently over bandwidth allocation.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[virtualGuestsWithCpanel]: #virtualguestswithcpanel
#### [virtualGuestsWithCpanel]
All virtual guests associated with an account that has the cPanel web hosting control panel installed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[virtualGuestsWithMcafee]: #virtualguestswithmcafee
#### [virtualGuestsWithMcafee]
All virtual guests associated with an account that have McAfee Secure software components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[virtualGuestsWithMcafeeAntivirusRedhat]: #virtualguestswithmcafeeantivirusredhat
#### [virtualGuestsWithMcafeeAntivirusRedhat]
All virtual guests associated with an account that have McAfee Secure AntiVirus for Redhat software components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[virtualGuestsWithMcafeeAntivirusWindows]: #virtualguestswithmcafeeantiviruswindows
#### [virtualGuestsWithMcafeeAntivirusWindows]
All virtual guests associated with an account that has McAfee Secure AntiVirus for Windows software components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[virtualGuestsWithMcafeeIntrusionDetectionSystem]: #virtualguestswithmcafeeintrusiondetectionsystem
#### [virtualGuestsWithMcafeeIntrusionDetectionSystem]
All virtual guests associated with an account that has McAfee Secure Intrusion Detection System software components.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[virtualGuestsWithPlesk]: #virtualguestswithplesk
#### [virtualGuestsWithPlesk]
All virtual guests associated with an account that has the Plesk web hosting control panel installed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[virtualGuestsWithQuantastor]: #virtualguestswithquantastor
#### [virtualGuestsWithQuantastor]
All virtual guests associated with an account that have the QuantaStor storage system installed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[virtualGuestsWithUrchin]: #virtualguestswithurchin
#### [virtualGuestsWithUrchin]
All virtual guests associated with an account that has the Urchin web traffic analytics package installed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[virtualPrivateRack]: #virtualprivaterack
#### [virtualPrivateRack]
The bandwidth pooling for this account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment </a>**

-----
[virtualStorageArchiveRepositories]: #virtualstoragearchiverepositories
#### [virtualStorageArchiveRepositories]
An account's associated virtual server archived storage repositories.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Storage_Repository'>SoftLayer_Virtual_Storage_Repository[] </a>**

-----
[virtualStoragePublicRepositories]: #virtualstoragepublicrepositories
#### [virtualStoragePublicRepositories]
An account's associated virtual server public storage repositories.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Storage_Repository'>SoftLayer_Virtual_Storage_Repository[] </a>**

-----
[vpcVirtualGuests]: #vpcvirtualguests
#### [vpcVirtualGuests]
An account's associated VPC configured virtual guest objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


## Count

-----
[abuseEmailCount]: #abuseemailcount
#### [abuseEmailCount]
A count of email addresses that are responsible for abuse and legal inquiries on behalf of an account. For instance, new legal and abuse tickets are sent to these addresses.   
<span class="type-label">Type: </span>**unsigned long**


-----
[accountContactCount]: #accountcontactcount
#### [accountContactCount]
A count of the account contacts on an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[accountLicenseCount]: #accountlicensecount
#### [accountLicenseCount]
A count of the account software licenses owned by an account   
<span class="type-label">Type: </span>**unsigned long**


-----
[accountLinkCount]: #accountlinkcount
#### [accountLinkCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[activeAccountLicenseCount]: #activeaccountlicensecount
#### [activeAccountLicenseCount]
A count of the active account software licenses owned by an account   
<span class="type-label">Type: </span>**unsigned long**


-----
[activeAddressCount]: #activeaddresscount
#### [activeAddressCount]
A count of the active address(es) that belong to an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[activeAgreementCount]: #activeagreementcount
#### [activeAgreementCount]
A count of all active agreements for an account   
<span class="type-label">Type: </span>**unsigned long**


-----
[activeBillingAgreementCount]: #activebillingagreementcount
#### [activeBillingAgreementCount]
A count of all billing agreements for an account   
<span class="type-label">Type: </span>**unsigned long**


-----
[activeColocationContainerCount]: #activecolocationcontainercount
#### [activeColocationContainerCount]
A count of the account's active top level colocation containers.   
<span class="type-label">Type: </span>**unsigned long**


-----
[activeFlexibleCreditEnrollmentCount]: #activeflexiblecreditenrollmentcount
#### [activeFlexibleCreditEnrollmentCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[activeNotificationSubscriberCount]: #activenotificationsubscribercount
#### [activeNotificationSubscriberCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[activeQuoteCount]: #activequotecount
#### [activeQuoteCount]
A count of an account's non-expired quotes.   
<span class="type-label">Type: </span>**unsigned long**


-----
[activeReservedCapacityAgreementCount]: #activereservedcapacityagreementcount
#### [activeReservedCapacityAgreementCount]
A count of active reserved capacity agreements for an account   
<span class="type-label">Type: </span>**unsigned long**


-----
[activeVirtualLicenseCount]: #activevirtuallicensecount
#### [activeVirtualLicenseCount]
A count of the virtual software licenses controlled by an account   
<span class="type-label">Type: </span>**unsigned long**


-----
[adcLoadBalancerCount]: #adcloadbalancercount
#### [adcLoadBalancerCount]
A count of an account's associated load balancers.   
<span class="type-label">Type: </span>**unsigned long**


-----
[addressCount]: #addresscount
#### [addressCount]
A count of all the address(es) that belong to an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[allCommissionBillingItemCount]: #allcommissionbillingitemcount
#### [allCommissionBillingItemCount]
A count of the billing items that will be on an account's next invoice.   
<span class="type-label">Type: </span>**unsigned long**


-----
[allRecurringTopLevelBillingItemCount]: #allrecurringtoplevelbillingitemcount
#### [allRecurringTopLevelBillingItemCount]
A count of the billing items that will be on an account's next invoice.   
<span class="type-label">Type: </span>**unsigned long**


-----
[allRecurringTopLevelBillingItemsUnfilteredCount]: #allrecurringtoplevelbillingitemsunfilteredcount
#### [allRecurringTopLevelBillingItemsUnfilteredCount]
A count of the billing items that will be on an account's next invoice. Does not consider associated items.   
<span class="type-label">Type: </span>**unsigned long**


-----
[allSubnetBillingItemCount]: #allsubnetbillingitemcount
#### [allSubnetBillingItemCount]
A count of the billing items that will be on an account's next invoice.   
<span class="type-label">Type: </span>**unsigned long**


-----
[allTopLevelBillingItemCount]: #alltoplevelbillingitemcount
#### [allTopLevelBillingItemCount]
A count of all billing items of an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[allTopLevelBillingItemsUnfilteredCount]: #alltoplevelbillingitemsunfilteredcount
#### [allTopLevelBillingItemsUnfilteredCount]
A count of the billing items that will be on an account's next invoice. Does not consider associated items.   
<span class="type-label">Type: </span>**unsigned long**


-----
[applicationDeliveryControllerCount]: #applicationdeliverycontrollercount
#### [applicationDeliveryControllerCount]
A count of an account's associated application delivery controller records.   
<span class="type-label">Type: </span>**unsigned long**


-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of the account attribute values for a SoftLayer customer account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[availablePublicNetworkVlanCount]: #availablepublicnetworkvlancount
#### [availablePublicNetworkVlanCount]
A count of the public network VLANs assigned to an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[bandwidthAllotmentCount]: #bandwidthallotmentcount
#### [bandwidthAllotmentCount]
A count of the bandwidth allotments for an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[bandwidthAllotmentsOverAllocationCount]: #bandwidthallotmentsoverallocationcount
#### [bandwidthAllotmentsOverAllocationCount]
A count of the bandwidth allotments for an account currently over allocation.   
<span class="type-label">Type: </span>**unsigned long**


-----
[bandwidthAllotmentsProjectedOverAllocationCount]: #bandwidthallotmentsprojectedoverallocationcount
#### [bandwidthAllotmentsProjectedOverAllocationCount]
A count of the bandwidth allotments for an account projected to go over allocation.   
<span class="type-label">Type: </span>**unsigned long**


-----
[bareMetalInstanceCount]: #baremetalinstancecount
#### [bareMetalInstanceCount]
A count of an account's associated bare metal server objects.   
<span class="type-label">Type: </span>**unsigned long**


-----
[billingAgreementCount]: #billingagreementcount
#### [billingAgreementCount]
A count of all billing agreements for an account   
<span class="type-label">Type: </span>**unsigned long**


-----
[blockDeviceTemplateGroupCount]: #blockdevicetemplategroupcount
#### [blockDeviceTemplateGroupCount]
A count of private template group objects (parent and children) and the shared template group objects (parent only) for an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[cartCount]: #cartcount
#### [cartCount]
A count of an account's active carts.   
<span class="type-label">Type: </span>**unsigned long**


-----
[catalystEnrollmentCount]: #catalystenrollmentcount
#### [catalystEnrollmentCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[closedTicketCount]: #closedticketcount
#### [closedTicketCount]
A count of all closed tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[datacentersWithSubnetAllocationCount]: #datacenterswithsubnetallocationcount
#### [datacentersWithSubnetAllocationCount]
A count of datacenters which contain subnets that the account has access to route.   
<span class="type-label">Type: </span>**unsigned long**


-----
[dedicatedHostCount]: #dedicatedhostcount
#### [dedicatedHostCount]
A count of an account's associated virtual dedicated host objects.   
<span class="type-label">Type: </span>**unsigned long**


-----
[displaySupportRepresentativeAssignmentCount]: #displaysupportrepresentativeassignmentcount
#### [displaySupportRepresentativeAssignmentCount]
A count of the SoftLayer employees that an account is assigned to.   
<span class="type-label">Type: </span>**unsigned long**


-----
[domainCount]: #domaincount
#### [domainCount]
A count of the DNS domains associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[domainRegistrationCount]: #domainregistrationcount
#### [domainRegistrationCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[domainsWithoutSecondaryDnsRecordCount]: #domainswithoutsecondarydnsrecordcount
#### [domainsWithoutSecondaryDnsRecordCount]
A count of the DNS domains associated with an account that were not created as a result of a secondary DNS zone transfer.   
<span class="type-label">Type: </span>**unsigned long**


-----
[evaultMasterUserCount]: #evaultmasterusercount
#### [evaultMasterUserCount]
A count of an account's master EVault user. This is only used when an account has EVault service.   
<span class="type-label">Type: </span>**unsigned long**


-----
[evaultNetworkStorageCount]: #evaultnetworkstoragecount
#### [evaultNetworkStorageCount]
A count of an account's associated EVault storage volumes.   
<span class="type-label">Type: </span>**unsigned long**


-----
[expiredSecurityCertificateCount]: #expiredsecuritycertificatecount
#### [expiredSecurityCertificateCount]
A count of stored security certificates that are expired (ie. SSL)   
<span class="type-label">Type: </span>**unsigned long**


-----
[facilityLogCount]: #facilitylogcount
#### [facilityLogCount]
A count of logs of who entered a colocation area which is assigned to this account, or when a user under this account enters a datacenter.   
<span class="type-label">Type: </span>**unsigned long**


-----
[flexibleCreditEnrollmentCount]: #flexiblecreditenrollmentcount
#### [flexibleCreditEnrollmentCount]
A count of all of the account's current and former Flexible Credit enrollments.   
<span class="type-label">Type: </span>**unsigned long**


-----
[globalIpRecordCount]: #globaliprecordcount
#### [globalIpRecordCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[globalIpv4RecordCount]: #globalipv4recordcount
#### [globalIpv4RecordCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[globalIpv6RecordCount]: #globalipv6recordcount
#### [globalIpv6RecordCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[globalLoadBalancerAccountCount]: #globalloadbalanceraccountcount
#### [globalLoadBalancerAccountCount]
A count of the global load balancer accounts for a softlayer customer account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hardwareCount]: #hardwarecount
#### [hardwareCount]
A count of an account's associated hardware objects.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hardwareOverBandwidthAllocationCount]: #hardwareoverbandwidthallocationcount
#### [hardwareOverBandwidthAllocationCount]
A count of an account's associated hardware objects currently over bandwidth allocation.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hardwareProjectedOverBandwidthAllocationCount]: #hardwareprojectedoverbandwidthallocationcount
#### [hardwareProjectedOverBandwidthAllocationCount]
A count of an account's associated hardware objects projected to go over bandwidth allocation.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hardwareWithCpanelCount]: #hardwarewithcpanelcount
#### [hardwareWithCpanelCount]
A count of all hardware associated with an account that has the cPanel web hosting control panel installed.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hardwareWithHelmCount]: #hardwarewithhelmcount
#### [hardwareWithHelmCount]
A count of all hardware associated with an account that has the Helm web hosting control panel installed.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hardwareWithMcafeeAntivirusRedhatCount]: #hardwarewithmcafeeantivirusredhatcount
#### [hardwareWithMcafeeAntivirusRedhatCount]
A count of all hardware associated with an account that has McAfee Secure AntiVirus for Redhat software components.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hardwareWithMcafeeAntivirusWindowCount]: #hardwarewithmcafeeantiviruswindowcount
#### [hardwareWithMcafeeAntivirusWindowCount]
A count of all hardware associated with an account that has McAfee Secure AntiVirus for Windows software components.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hardwareWithMcafeeCount]: #hardwarewithmcafeecount
#### [hardwareWithMcafeeCount]
A count of all hardware associated with an account that has McAfee Secure software components.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hardwareWithMcafeeIntrusionDetectionSystemCount]: #hardwarewithmcafeeintrusiondetectionsystemcount
#### [hardwareWithMcafeeIntrusionDetectionSystemCount]
A count of all hardware associated with an account that has McAfee Secure Intrusion Detection System software components.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hardwareWithPleskCount]: #hardwarewithpleskcount
#### [hardwareWithPleskCount]
A count of all hardware associated with an account that has the Plesk web hosting control panel installed.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hardwareWithQuantastorCount]: #hardwarewithquantastorcount
#### [hardwareWithQuantastorCount]
A count of all hardware associated with an account that has the QuantaStor storage system installed.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hardwareWithUrchinCount]: #hardwarewithurchincount
#### [hardwareWithUrchinCount]
A count of all hardware associated with an account that has the Urchin web traffic analytics package installed.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hardwareWithWindowCount]: #hardwarewithwindowcount
#### [hardwareWithWindowCount]
A count of all hardware associated with an account that is running a version of the Microsoft Windows operating system.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hourlyBareMetalInstanceCount]: #hourlybaremetalinstancecount
#### [hourlyBareMetalInstanceCount]
A count of an account's associated hourly bare metal server objects.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hourlyServiceBillingItemCount]: #hourlyservicebillingitemcount
#### [hourlyServiceBillingItemCount]
A count of hourly service billing items that will be on an account's next invoice.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hourlyVirtualGuestCount]: #hourlyvirtualguestcount
#### [hourlyVirtualGuestCount]
A count of an account's associated hourly virtual guest objects.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hubNetworkStorageCount]: #hubnetworkstoragecount
#### [hubNetworkStorageCount]
A count of an account's associated Virtual Storage volumes.   
<span class="type-label">Type: </span>**unsigned long**


-----
[internalNoteCount]: #internalnotecount
#### [internalNoteCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[invoiceCount]: #invoicecount
#### [invoiceCount]
A count of an account's associated billing invoices.   
<span class="type-label">Type: </span>**unsigned long**


-----
[ipAddressCount]: #ipaddresscount
#### [ipAddressCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[iscsiNetworkStorageCount]: #iscsinetworkstoragecount
#### [iscsiNetworkStorageCount]
A count of an account's associated iSCSI storage volumes.   
<span class="type-label">Type: </span>**unsigned long**


-----
[lastFiveClosedAbuseTicketCount]: #lastfiveclosedabuseticketcount
#### [lastFiveClosedAbuseTicketCount]
A count of the five most recently closed abuse tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[lastFiveClosedAccountingTicketCount]: #lastfiveclosedaccountingticketcount
#### [lastFiveClosedAccountingTicketCount]
A count of the five most recently closed accounting tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[lastFiveClosedOtherTicketCount]: #lastfiveclosedotherticketcount
#### [lastFiveClosedOtherTicketCount]
A count of the five most recently closed tickets that do not belong to the abuse, accounting, sales, or support groups associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[lastFiveClosedSalesTicketCount]: #lastfiveclosedsalesticketcount
#### [lastFiveClosedSalesTicketCount]
A count of the five most recently closed sales tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[lastFiveClosedSupportTicketCount]: #lastfiveclosedsupportticketcount
#### [lastFiveClosedSupportTicketCount]
A count of the five most recently closed support tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[lastFiveClosedTicketCount]: #lastfiveclosedticketcount
#### [lastFiveClosedTicketCount]
A count of the five most recently closed tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[legacyBandwidthAllotmentCount]: #legacybandwidthallotmentcount
#### [legacyBandwidthAllotmentCount]
A count of the legacy bandwidth allotments for an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[loadBalancerCount]: #loadbalancercount
#### [loadBalancerCount]
A count of an account's associated load balancers.   
<span class="type-label">Type: </span>**unsigned long**


-----
[lockboxNetworkStorageCount]: #lockboxnetworkstoragecount
#### [lockboxNetworkStorageCount]
A count of an account's associated Lockbox storage volumes.   
<span class="type-label">Type: </span>**unsigned long**


-----
[manualPaymentsUnderReviewCount]: #manualpaymentsunderreviewcount
#### [manualPaymentsUnderReviewCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[mediaDataTransferRequestCount]: #mediadatatransferrequestcount
#### [mediaDataTransferRequestCount]
A count of an account's media transfer service requests.   
<span class="type-label">Type: </span>**unsigned long**


-----
[monthlyBareMetalInstanceCount]: #monthlybaremetalinstancecount
#### [monthlyBareMetalInstanceCount]
A count of an account's associated monthly bare metal server objects.   
<span class="type-label">Type: </span>**unsigned long**


-----
[monthlyVirtualGuestCount]: #monthlyvirtualguestcount
#### [monthlyVirtualGuestCount]
A count of an account's associated monthly virtual guest objects.   
<span class="type-label">Type: </span>**unsigned long**


-----
[nasNetworkStorageCount]: #nasnetworkstoragecount
#### [nasNetworkStorageCount]
A count of an account's associated NAS storage volumes.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkGatewayCount]: #networkgatewaycount
#### [networkGatewayCount]
A count of all network gateway devices on this account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkHardwareCount]: #networkhardwarecount
#### [networkHardwareCount]
A count of an account's associated network hardware.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkMessageDeliveryAccountCount]: #networkmessagedeliveryaccountcount
#### [networkMessageDeliveryAccountCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[networkMonitorDownHardwareCount]: #networkmonitordownhardwarecount
#### [networkMonitorDownHardwareCount]
A count of hardware which is currently experiencing a service failure.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkMonitorDownVirtualGuestCount]: #networkmonitordownvirtualguestcount
#### [networkMonitorDownVirtualGuestCount]
A count of virtual guest which is currently experiencing a service failure.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkMonitorRecoveringHardwareCount]: #networkmonitorrecoveringhardwarecount
#### [networkMonitorRecoveringHardwareCount]
A count of hardware which is currently recovering from a service failure.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkMonitorRecoveringVirtualGuestCount]: #networkmonitorrecoveringvirtualguestcount
#### [networkMonitorRecoveringVirtualGuestCount]
A count of virtual guest which is currently recovering from a service failure.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkMonitorUpHardwareCount]: #networkmonitoruphardwarecount
#### [networkMonitorUpHardwareCount]
A count of hardware which is currently online.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkMonitorUpVirtualGuestCount]: #networkmonitorupvirtualguestcount
#### [networkMonitorUpVirtualGuestCount]
A count of virtual guest which is currently online.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkStorageCount]: #networkstoragecount
#### [networkStorageCount]
A count of an account's associated storage volumes. This includes Lockbox, NAS, EVault, and iSCSI volumes.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkStorageGroupCount]: #networkstoragegroupcount
#### [networkStorageGroupCount]
A count of an account's Network Storage groups.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkTunnelContextCount]: #networktunnelcontextcount
#### [networkTunnelContextCount]
A count of iPSec network tunnels for an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkVlanCount]: #networkvlancount
#### [networkVlanCount]
A count of all network VLANs assigned to an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[nextBillingPublicAllotmentHardwareBandwidthDetailCount]: #nextbillingpublicallotmenthardwarebandwidthdetailcount
#### [nextBillingPublicAllotmentHardwareBandwidthDetailCount]
A count of dEPRECATED - This information can be pulled directly through tapping keys now - DEPRECATED. The allotments for this account and their servers for the next billing cycle. The public inbound and outbound bandwidth is calculated for each server in addition to the daily average network traffic since the last billing date.   
<span class="type-label">Type: </span>**unsigned long**


-----
[nextInvoiceTopLevelBillingItemCount]: #nextinvoicetoplevelbillingitemcount
#### [nextInvoiceTopLevelBillingItemCount]
A count of the billing items that will be on an account's next invoice.   
<span class="type-label">Type: </span>**unsigned long**


-----
[notificationSubscriberCount]: #notificationsubscribercount
#### [notificationSubscriberCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[openAbuseTicketCount]: #openabuseticketcount
#### [openAbuseTicketCount]
A count of the open abuse tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[openAccountingTicketCount]: #openaccountingticketcount
#### [openAccountingTicketCount]
A count of the open accounting tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[openBillingTicketCount]: #openbillingticketcount
#### [openBillingTicketCount]
A count of the open billing tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[openCancellationRequestCount]: #opencancellationrequestcount
#### [openCancellationRequestCount]
A count of an open ticket requesting cancellation of this server, if one exists.   
<span class="type-label">Type: </span>**unsigned long**


-----
[openOtherTicketCount]: #openotherticketcount
#### [openOtherTicketCount]
A count of the open tickets that do not belong to the abuse, accounting, sales, or support groups associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[openRecurringInvoiceCount]: #openrecurringinvoicecount
#### [openRecurringInvoiceCount]
A count of an account's recurring invoices.   
<span class="type-label">Type: </span>**unsigned long**


-----
[openSalesTicketCount]: #opensalesticketcount
#### [openSalesTicketCount]
A count of the open sales tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[openStackAccountLinkCount]: #openstackaccountlinkcount
#### [openStackAccountLinkCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[openStackObjectStorageCount]: #openstackobjectstoragecount
#### [openStackObjectStorageCount]
A count of an account's associated Openstack related Object Storage accounts.   
<span class="type-label">Type: </span>**unsigned long**


-----
[openSupportTicketCount]: #opensupportticketcount
#### [openSupportTicketCount]
A count of the open support tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[openTicketCount]: #openticketcount
#### [openTicketCount]
A count of all open tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[openTicketsWaitingOnCustomerCount]: #openticketswaitingoncustomercount
#### [openTicketsWaitingOnCustomerCount]
A count of all open tickets associated with an account last edited by an employee.   
<span class="type-label">Type: </span>**unsigned long**


-----
[orderCount]: #ordercount
#### [orderCount]
A count of an account's associated billing orders excluding upgrades.   
<span class="type-label">Type: </span>**unsigned long**


-----
[orphanBillingItemCount]: #orphanbillingitemcount
#### [orphanBillingItemCount]
A count of the billing items that have no parent billing item. These are items that don't necessarily belong to a single server.   
<span class="type-label">Type: </span>**unsigned long**


-----
[ownedBrandCount]: #ownedbrandcount
#### [ownedBrandCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[ownedHardwareGenericComponentModelCount]: #ownedhardwaregenericcomponentmodelcount
#### [ownedHardwareGenericComponentModelCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[paymentProcessorCount]: #paymentprocessorcount
#### [paymentProcessorCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[pendingEventCount]: #pendingeventcount
#### [pendingEventCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[pendingInvoiceTopLevelItemCount]: #pendinginvoicetoplevelitemcount
#### [pendingInvoiceTopLevelItemCount]
A count of a list of top-level invoice items that are on an account's currently pending invoice.   
<span class="type-label">Type: </span>**unsigned long**


-----
[permissionGroupCount]: #permissiongroupcount
#### [permissionGroupCount]
A count of an account's permission groups.   
<span class="type-label">Type: </span>**unsigned long**


-----
[permissionRoleCount]: #permissionrolecount
#### [permissionRoleCount]
A count of an account's user roles.   
<span class="type-label">Type: </span>**unsigned long**


-----
[placementGroupCount]: #placementgroupcount
#### [placementGroupCount]
A count of an account's associated virtual placement groups.   
<span class="type-label">Type: </span>**unsigned long**


-----
[portableStorageVolumeCount]: #portablestoragevolumecount
#### [portableStorageVolumeCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[postProvisioningHookCount]: #postprovisioninghookcount
#### [postProvisioningHookCount]
A count of customer specified URIs that are downloaded onto a newly provisioned or reloaded server. If the URI is sent over https it will be executed directly on the server.   
<span class="type-label">Type: </span>**unsigned long**


-----
[pptpVpnUserCount]: #pptpvpnusercount
#### [pptpVpnUserCount]
A count of an account's associated portal users with PPTP VPN access. (Deprecated)   
<span class="type-label">Type: </span>**unsigned long**


-----
[priceRestrictionCount]: #pricerestrictioncount
#### [priceRestrictionCount]
A count of the item price that an account is restricted to.   
<span class="type-label">Type: </span>**unsigned long**


-----
[priorityOneTicketCount]: #priorityoneticketcount
#### [priorityOneTicketCount]
A count of all priority one tickets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[privateAllotmentHardwareBandwidthDetailCount]: #privateallotmenthardwarebandwidthdetailcount
#### [privateAllotmentHardwareBandwidthDetailCount]
A count of dEPRECATED - This information can be pulled directly through tapping keys now - DEPRECATED. The allotments for this account and their servers. The private inbound and outbound bandwidth is calculated for each server in addition to the daily average network traffic since the last billing date.   
<span class="type-label">Type: </span>**unsigned long**


-----
[privateBlockDeviceTemplateGroupCount]: #privateblockdevicetemplategroupcount
#### [privateBlockDeviceTemplateGroupCount]
A count of private and shared template group objects (parent only) for an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[privateIpAddressCount]: #privateipaddresscount
#### [privateIpAddressCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[privateNetworkVlanCount]: #privatenetworkvlancount
#### [privateNetworkVlanCount]
A count of the private network VLANs assigned to an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[privateSubnetCount]: #privatesubnetcount
#### [privateSubnetCount]
A count of all private subnets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[publicAllotmentHardwareBandwidthDetailCount]: #publicallotmenthardwarebandwidthdetailcount
#### [publicAllotmentHardwareBandwidthDetailCount]
A count of dEPRECATED - This information can be pulled directly through tapping keys now - DEPRECATED. The allotments for this account and their servers. The public inbound and outbound bandwidth is calculated for each server in addition to the daily average network traffic since the last billing date.   
<span class="type-label">Type: </span>**unsigned long**


-----
[publicIpAddressCount]: #publicipaddresscount
#### [publicIpAddressCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[publicNetworkVlanCount]: #publicnetworkvlancount
#### [publicNetworkVlanCount]
A count of the public network VLANs assigned to an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[publicSubnetCount]: #publicsubnetcount
#### [publicSubnetCount]
A count of all public network subnets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[quoteCount]: #quotecount
#### [quoteCount]
A count of an account's quotes.   
<span class="type-label">Type: </span>**unsigned long**


-----
[recentEventCount]: #recenteventcount
#### [recentEventCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[referredAccountCount]: #referredaccountcount
#### [referredAccountCount]
A count of if this is a account is a referral partner, the accounts this referral partner has referred   
<span class="type-label">Type: </span>**unsigned long**


-----
[regulatedWorkloadCount]: #regulatedworkloadcount
#### [regulatedWorkloadCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[remoteManagementCommandRequestCount]: #remotemanagementcommandrequestcount
#### [remoteManagementCommandRequestCount]
A count of remote management command requests for an account   
<span class="type-label">Type: </span>**unsigned long**


-----
[replicationEventCount]: #replicationeventcount
#### [replicationEventCount]
A count of the Replication events for all Network Storage volumes on an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[reservedCapacityAgreementCount]: #reservedcapacityagreementcount
#### [reservedCapacityAgreementCount]
A count of all reserved capacity agreements for an account   
<span class="type-label">Type: </span>**unsigned long**


-----
[reservedCapacityGroupCount]: #reservedcapacitygroupcount
#### [reservedCapacityGroupCount]
A count of the reserved capacity groups owned by this account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[resourceGroupCount]: #resourcegroupcount
#### [resourceGroupCount]
A count of an account's associated top-level resource groups.   
<span class="type-label">Type: </span>**unsigned long**


-----
[routerCount]: #routercount
#### [routerCount]
A count of all Routers that an accounts VLANs reside on   
<span class="type-label">Type: </span>**unsigned long**


-----
[scaleGroupCount]: #scalegroupcount
#### [scaleGroupCount]
A count of all scale groups on this account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[secondaryDomainCount]: #secondarydomaincount
#### [secondaryDomainCount]
A count of the secondary DNS records for a SoftLayer customer account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[securityCertificateCount]: #securitycertificatecount
#### [securityCertificateCount]
A count of stored security certificates (ie. SSL)   
<span class="type-label">Type: </span>**unsigned long**


-----
[securityGroupCount]: #securitygroupcount
#### [securityGroupCount]
A count of the security groups belonging to this account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[securityScanRequestCount]: #securityscanrequestcount
#### [securityScanRequestCount]
A count of an account's vulnerability scan requests.   
<span class="type-label">Type: </span>**unsigned long**


-----
[serviceBillingItemCount]: #servicebillingitemcount
#### [serviceBillingItemCount]
A count of the service billing items that will be on an account's next invoice.    
<span class="type-label">Type: </span>**unsigned long**


-----
[shipmentCount]: #shipmentcount
#### [shipmentCount]
A count of shipments that belong to the customer's account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[sshKeyCount]: #sshkeycount
#### [sshKeyCount]
A count of customer specified SSH keys that can be implemented onto a newly provisioned or reloaded server.   
<span class="type-label">Type: </span>**unsigned long**


-----
[sslVpnUserCount]: #sslvpnusercount
#### [sslVpnUserCount]
A count of an account's associated portal users with SSL VPN access.   
<span class="type-label">Type: </span>**unsigned long**


-----
[standardPoolVirtualGuestCount]: #standardpoolvirtualguestcount
#### [standardPoolVirtualGuestCount]
A count of an account's virtual guest objects that are hosted on a user provisioned hypervisor.   
<span class="type-label">Type: </span>**unsigned long**


-----
[subnetCount]: #subnetcount
#### [subnetCount]
A count of all network subnets associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[subnetRegistrationCount]: #subnetregistrationcount
#### [subnetRegistrationCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[subnetRegistrationDetailCount]: #subnetregistrationdetailcount
#### [subnetRegistrationDetailCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[supportRepresentativeCount]: #supportrepresentativecount
#### [supportRepresentativeCount]
A count of the SoftLayer employees that an account is assigned to.   
<span class="type-label">Type: </span>**unsigned long**


-----
[supportSubscriptionCount]: #supportsubscriptioncount
#### [supportSubscriptionCount]
A count of the active support subscriptions for this account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[tagCount]: #tagcount
#### [tagCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[ticketCount]: #ticketcount
#### [ticketCount]
A count of an account's associated tickets.   
<span class="type-label">Type: </span>**unsigned long**


-----
[ticketsClosedInTheLastThreeDaysCount]: #ticketsclosedinthelastthreedayscount
#### [ticketsClosedInTheLastThreeDaysCount]
A count of tickets closed within the last 72 hours or last 10 tickets, whichever is less, associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[ticketsClosedTodayCount]: #ticketsclosedtodaycount
#### [ticketsClosedTodayCount]
A count of tickets closed today associated with an account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[transcodeAccountCount]: #transcodeaccountcount
#### [transcodeAccountCount]
A count of an account's associated Transcode account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[upgradeRequestCount]: #upgraderequestcount
#### [upgradeRequestCount]
A count of an account's associated upgrade requests.   
<span class="type-label">Type: </span>**unsigned long**


-----
[userCount]: #usercount
#### [userCount]
A count of an account's portal users.   
<span class="type-label">Type: </span>**unsigned long**


-----
[validSecurityCertificateCount]: #validsecuritycertificatecount
#### [validSecurityCertificateCount]
A count of stored security certificates that are not expired (ie. SSL)   
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualDedicatedRackCount]: #virtualdedicatedrackcount
#### [virtualDedicatedRackCount]
A count of the bandwidth pooling for this account.   
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualDiskImageCount]: #virtualdiskimagecount
#### [virtualDiskImageCount]
A count of an account's associated virtual server virtual disk images.   
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualGuestCount]: #virtualguestcount
#### [virtualGuestCount]
A count of an account's associated virtual guest objects.   
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualGuestsOverBandwidthAllocationCount]: #virtualguestsoverbandwidthallocationcount
#### [virtualGuestsOverBandwidthAllocationCount]
A count of an account's associated virtual guest objects currently over bandwidth allocation.   
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualGuestsProjectedOverBandwidthAllocationCount]: #virtualguestsprojectedoverbandwidthallocationcount
#### [virtualGuestsProjectedOverBandwidthAllocationCount]
A count of an account's associated virtual guest objects currently over bandwidth allocation.   
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualGuestsWithCpanelCount]: #virtualguestswithcpanelcount
#### [virtualGuestsWithCpanelCount]
A count of all virtual guests associated with an account that has the cPanel web hosting control panel installed.   
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualGuestsWithMcafeeAntivirusRedhatCount]: #virtualguestswithmcafeeantivirusredhatcount
#### [virtualGuestsWithMcafeeAntivirusRedhatCount]
A count of all virtual guests associated with an account that have McAfee Secure AntiVirus for Redhat software components.   
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualGuestsWithMcafeeAntivirusWindowCount]: #virtualguestswithmcafeeantiviruswindowcount
#### [virtualGuestsWithMcafeeAntivirusWindowCount]
A count of all virtual guests associated with an account that has McAfee Secure AntiVirus for Windows software components.   
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualGuestsWithMcafeeCount]: #virtualguestswithmcafeecount
#### [virtualGuestsWithMcafeeCount]
A count of all virtual guests associated with an account that have McAfee Secure software components.   
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualGuestsWithMcafeeIntrusionDetectionSystemCount]: #virtualguestswithmcafeeintrusiondetectionsystemcount
#### [virtualGuestsWithMcafeeIntrusionDetectionSystemCount]
A count of all virtual guests associated with an account that has McAfee Secure Intrusion Detection System software components.   
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualGuestsWithPleskCount]: #virtualguestswithpleskcount
#### [virtualGuestsWithPleskCount]
A count of all virtual guests associated with an account that has the Plesk web hosting control panel installed.   
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualGuestsWithQuantastorCount]: #virtualguestswithquantastorcount
#### [virtualGuestsWithQuantastorCount]
A count of all virtual guests associated with an account that have the QuantaStor storage system installed.   
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualGuestsWithUrchinCount]: #virtualguestswithurchincount
#### [virtualGuestsWithUrchinCount]
A count of all virtual guests associated with an account that has the Urchin web traffic analytics package installed.   
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualStorageArchiveRepositoryCount]: #virtualstoragearchiverepositorycount
#### [virtualStorageArchiveRepositoryCount]
A count of an account's associated virtual server archived storage repositories.   
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualStoragePublicRepositoryCount]: #virtualstoragepublicrepositorycount
#### [virtualStoragePublicRepositoryCount]
A count of an account's associated virtual server public storage repositories.   
<span class="type-label">Type: </span>**unsigned long**


-----
[vpcVirtualGuestCount]: #vpcvirtualguestcount
#### [vpcVirtualGuestCount]
A count of an account's associated VPC configured virtual guest objects.   
<span class="type-label">Type: </span>**unsigned long**

</div>


