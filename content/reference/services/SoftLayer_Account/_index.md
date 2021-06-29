---
title: "SoftLayer_Account"
description: "Every SoftLayer customer has an account which is defined in the SoftLayer_Account service. SoftLayer accounts have users... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
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
Every SoftLayer customer has an account which is defined in the SoftLayer_Account service. SoftLayer accounts have users, hardware, and services such as storage and domains associated with them. The SoftLayer_Account service is a convenient way to obtain general information about your SoftLayer account. Use the data returned by these methods with other API services to get more detailed information about your services and to make changes to your servers and services. 

SoftLayer customers are unable to change their company account information in the portal or the API. If you need to change this information please open a sales ticket in our customer portal and our account management staff will assist you. 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [activatePartner](/reference/services/SoftLayer_Account/activatePartner)
This service enables a partner account that has been created but is currently inactive. This restricted service is only available for certain accounts. Please contact support for questions. 
</div>

<div class="method-row">

#### [addAchInformation](/reference/services/SoftLayer_Account/addAchInformation)

</div>

<div class="method-row">

#### [addReferralPartnerPaymentOption](/reference/services/SoftLayer_Account/addReferralPartnerPaymentOption)

</div>

<div class="method-row">

#### [areVdrUpdatesBlockedForBilling](/reference/services/SoftLayer_Account/areVdrUpdatesBlockedForBilling)
This method returns true if Bandwidth Pooling updates are blocked so billing can run for this account.
</div>

<div class="method-row">

#### [cancelPayPalTransaction](/reference/services/SoftLayer_Account/cancelPayPalTransaction)
Cancel the PayPal Payment Request process.
</div>

<div class="method-row">

#### [completePayPalTransaction](/reference/services/SoftLayer_Account/completePayPalTransaction)
Complete the PayPal Payment Request process and receive confirmation message.
</div>

<div class="method-row">

#### [countHourlyInstances](/reference/services/SoftLayer_Account/countHourlyInstances)
Retrieve the number of hourly services on an account that are active, plus any pending orders with hourly services attached. 
</div>

<div class="method-row">

#### [createUser](/reference/services/SoftLayer_Account/createUser)
Create a new user record, optionally skipping the IBMid email ("silently").
</div>

<div class="method-row">

#### [disableEuSupport](/reference/services/SoftLayer_Account/disableEuSupport)
Turn off the EU Supported account flag.
</div>

<div class="method-row">

#### [disableVpnConfigRequiresVpnManageAttribute](/reference/services/SoftLayer_Account/disableVpnConfigRequiresVpnManageAttribute)
Disable the VPN Config Requires VPN Manage attribute, creating it if necessary.
</div>

<div class="method-row">

#### [editAccount](/reference/services/SoftLayer_Account/editAccount)
Edit an account's information.
</div>

<div class="method-row">

#### [enableEuSupport](/reference/services/SoftLayer_Account/enableEuSupport)
Turn on the EU Supported account flag.
</div>

<div class="method-row">

#### [enableVpnConfigRequiresVpnManageAttribute](/reference/services/SoftLayer_Account/enableVpnConfigRequiresVpnManageAttribute)
Enable the VPN Config Requires VPN Manage attribute, creating it if necessary.
</div>

<div class="method-row">

#### [getAbuseEmail](/reference/services/SoftLayer_Account/getAbuseEmail)
Retrieve an email address that is responsible for abuse and legal inquiries on behalf of an account. For instance, new legal and abuse tickets are sent to this address.
</div>

<div class="method-row">

#### [getAbuseEmails](/reference/services/SoftLayer_Account/getAbuseEmails)
Retrieve email addresses that are responsible for abuse and legal inquiries on behalf of an account. For instance, new legal and abuse tickets are sent to these addresses.
</div>

<div class="method-row">

#### [getAccountBackupHistory](/reference/services/SoftLayer_Account/getAccountBackupHistory)
This method provides a history of account backups.
</div>

<div class="method-row">

#### [getAccountContacts](/reference/services/SoftLayer_Account/getAccountContacts)
Retrieve the account contacts on an account.
</div>

<div class="method-row">

#### [getAccountLicenses](/reference/services/SoftLayer_Account/getAccountLicenses)
Retrieve the account software licenses owned by an account
</div>

<div class="method-row">

#### [getAccountLinks](/reference/services/SoftLayer_Account/getAccountLinks)

</div>

<div class="method-row">

#### [getAccountStatus](/reference/services/SoftLayer_Account/getAccountStatus)
Retrieve an account's status presented in a more detailed data type.
</div>

<div class="method-row">

#### [getAccountTraitValue](/reference/services/SoftLayer_Account/getAccountTraitValue)
Get the specific trait by its key
</div>

<div class="method-row">

#### [getActiveAccountDiscountBillingItem](/reference/services/SoftLayer_Account/getActiveAccountDiscountBillingItem)
Retrieve the billing item associated with an account's monthly discount.
</div>

<div class="method-row">

#### [getActiveAccountLicenses](/reference/services/SoftLayer_Account/getActiveAccountLicenses)
Retrieve the active account software licenses owned by an account
</div>

<div class="method-row">

#### [getActiveAddresses](/reference/services/SoftLayer_Account/getActiveAddresses)
Retrieve the active address(es) that belong to an account.
</div>

<div class="method-row">

#### [getActiveAgreements](/reference/services/SoftLayer_Account/getActiveAgreements)
Retrieve all active agreements for an account
</div>

<div class="method-row">

#### [getActiveBillingAgreements](/reference/services/SoftLayer_Account/getActiveBillingAgreements)
Retrieve all billing agreements for an account
</div>

<div class="method-row">

#### [getActiveCatalystEnrollment](/reference/services/SoftLayer_Account/getActiveCatalystEnrollment)

</div>

<div class="method-row">

#### [getActiveColocationContainers](/reference/services/SoftLayer_Account/getActiveColocationContainers)
Retrieve the account's active top level colocation containers.
</div>

<div class="method-row">

#### [getActiveFlexibleCreditEnrollment](/reference/services/SoftLayer_Account/getActiveFlexibleCreditEnrollment)
Retrieve [Deprecated] Please use SoftLayer_Account::activeFlexibleCreditEnrollments.
</div>

<div class="method-row">

#### [getActiveFlexibleCreditEnrollments](/reference/services/SoftLayer_Account/getActiveFlexibleCreditEnrollments)

</div>

<div class="method-row">

#### [getActiveNotificationSubscribers](/reference/services/SoftLayer_Account/getActiveNotificationSubscribers)

</div>

<div class="method-row">

#### [getActiveOutletPackages](/reference/services/SoftLayer_Account/getActiveOutletPackages)
DEPRECATED. This method will return nothing.
</div>

<div class="method-row">

#### [getActivePackages](/reference/services/SoftLayer_Account/getActivePackages)
Retrieve the active [SoftLayer_Product_Package]({{<ref "reference/datatypes/SoftLayer_Product_Package">}}) objects from which you can order a server, service or software. 
</div>

<div class="method-row">

#### [getActivePackagesByAttribute](/reference/services/SoftLayer_Account/getActivePackagesByAttribute)
[<strong>DEPRECATED</strong>] Retrieve the active [SoftLayer_Product_Package]({{<ref "reference/datatypes/SoftLayer_Product_Package">}}) objects from which you can order a server, service or software filtered by an attribute type ([SoftLayer_Product_Package_Attribute_Type]({{<ref "reference/datatypes/SoftLayer_Product_Package_Attribute_Type">}})) on the package. 
</div>

<div class="method-row">

#### [getActivePrivateHostedCloudPackages](/reference/services/SoftLayer_Account/getActivePrivateHostedCloudPackages)

</div>

<div class="method-row">

#### [getActiveQuotes](/reference/services/SoftLayer_Account/getActiveQuotes)
Retrieve an account's non-expired quotes.
</div>

<div class="method-row">

#### [getActiveReservedCapacityAgreements](/reference/services/SoftLayer_Account/getActiveReservedCapacityAgreements)
Retrieve active reserved capacity agreements for an account
</div>

<div class="method-row">

#### [getActiveVirtualLicenses](/reference/services/SoftLayer_Account/getActiveVirtualLicenses)
Retrieve the virtual software licenses controlled by an account
</div>

<div class="method-row">

#### [getAdcLoadBalancers](/reference/services/SoftLayer_Account/getAdcLoadBalancers)
Retrieve an account's associated load balancers.
</div>

<div class="method-row">

#### [getAddresses](/reference/services/SoftLayer_Account/getAddresses)
Retrieve all the address(es) that belong to an account.
</div>

<div class="method-row">

#### [getAffiliateId](/reference/services/SoftLayer_Account/getAffiliateId)
Retrieve an affiliate identifier associated with the customer account. 
</div>

<div class="method-row">

#### [getAggregatedUptimeGraph](/reference/services/SoftLayer_Account/getAggregatedUptimeGraph)
Returns URL uptime data for your account
</div>

<div class="method-row">

#### [getAllBillingItems](/reference/services/SoftLayer_Account/getAllBillingItems)
Retrieve the billing items that will be on an account's next invoice.
</div>

<div class="method-row">

#### [getAllCommissionBillingItems](/reference/services/SoftLayer_Account/getAllCommissionBillingItems)
Retrieve the billing items that will be on an account's next invoice.
</div>

<div class="method-row">

#### [getAllRecurringTopLevelBillingItems](/reference/services/SoftLayer_Account/getAllRecurringTopLevelBillingItems)
Retrieve the billing items that will be on an account's next invoice.
</div>

<div class="method-row">

#### [getAllRecurringTopLevelBillingItemsUnfiltered](/reference/services/SoftLayer_Account/getAllRecurringTopLevelBillingItemsUnfiltered)
Retrieve the billing items that will be on an account's next invoice. Does not consider associated items.
</div>

<div class="method-row">

#### [getAllSubnetBillingItems](/reference/services/SoftLayer_Account/getAllSubnetBillingItems)
Retrieve the billing items that will be on an account's next invoice.
</div>

<div class="method-row">

#### [getAllTopLevelBillingItems](/reference/services/SoftLayer_Account/getAllTopLevelBillingItems)
Retrieve all billing items of an account.
</div>

<div class="method-row">

#### [getAllTopLevelBillingItemsUnfiltered](/reference/services/SoftLayer_Account/getAllTopLevelBillingItemsUnfiltered)
Retrieve the billing items that will be on an account's next invoice. Does not consider associated items.
</div>

<div class="method-row">

#### [getAllowIbmIdSilentMigrationFlag](/reference/services/SoftLayer_Account/getAllowIbmIdSilentMigrationFlag)
Retrieve indicates whether this account is allowed to silently migrate to use IBMid Authentication.
</div>

<div class="method-row">

#### [getAllowsBluemixAccountLinkingFlag](/reference/services/SoftLayer_Account/getAllowsBluemixAccountLinkingFlag)
Retrieve flag indicating if this account can be linked with Bluemix.
</div>

<div class="method-row">

#### [getAlternateCreditCardData](/reference/services/SoftLayer_Account/getAlternateCreditCardData)

</div>

<div class="method-row">

#### [getApplicationDeliveryControllers](/reference/services/SoftLayer_Account/getApplicationDeliveryControllers)
Retrieve an account's associated application delivery controller records.
</div>

<div class="method-row">

#### [getAttributeByType](/reference/services/SoftLayer_Account/getAttributeByType)
Retrieve an account attribute by type key name.
</div>

<div class="method-row">

#### [getAttributes](/reference/services/SoftLayer_Account/getAttributes)
Retrieve the account attribute values for a SoftLayer customer account.
</div>

<div class="method-row">

#### [getAuxiliaryNotifications](/reference/services/SoftLayer_Account/getAuxiliaryNotifications)

</div>

<div class="method-row">

#### [getAvailablePublicNetworkVlans](/reference/services/SoftLayer_Account/getAvailablePublicNetworkVlans)
Retrieve the public network VLANs assigned to an account.
</div>

<div class="method-row">

#### [getAverageArchiveUsageMetricDataByDate](/reference/services/SoftLayer_Account/getAverageArchiveUsageMetricDataByDate)
Returns the average disk usage for all archive repositories for the timeframe based on the parameters provided. 
</div>

<div class="method-row">

#### [getAveragePublicUsageMetricDataByDate](/reference/services/SoftLayer_Account/getAveragePublicUsageMetricDataByDate)
Returns the average disk usage for all public repositories for the timeframe based on the parameters provided. 
</div>

<div class="method-row">

#### [getBalance](/reference/services/SoftLayer_Account/getBalance)
Retrieve the account balance of a SoftLayer customer account. An account's balance is the amount of money owed to SoftLayer by the account holder, returned as a floating point number with two decimal places, measured in US Dollars ($USD). A negative account balance means the account holder has overpaid and is owed money by SoftLayer.
</div>

<div class="method-row">

#### [getBandwidthAllotments](/reference/services/SoftLayer_Account/getBandwidthAllotments)
Retrieve the bandwidth allotments for an account.
</div>

<div class="method-row">

#### [getBandwidthAllotmentsOverAllocation](/reference/services/SoftLayer_Account/getBandwidthAllotmentsOverAllocation)
Retrieve the bandwidth allotments for an account currently over allocation.
</div>

<div class="method-row">

#### [getBandwidthAllotmentsProjectedOverAllocation](/reference/services/SoftLayer_Account/getBandwidthAllotmentsProjectedOverAllocation)
Retrieve the bandwidth allotments for an account projected to go over allocation.
</div>

<div class="method-row">

#### [getBandwidthList](/reference/services/SoftLayer_Account/getBandwidthList)

</div>

<div class="method-row">

#### [getBareMetalInstances](/reference/services/SoftLayer_Account/getBareMetalInstances)
Retrieve an account's associated bare metal server objects.
</div>

<div class="method-row">

#### [getBillingAgreements](/reference/services/SoftLayer_Account/getBillingAgreements)
Retrieve all billing agreements for an account
</div>

<div class="method-row">

#### [getBillingInfo](/reference/services/SoftLayer_Account/getBillingInfo)
Retrieve an account's billing information.
</div>

<div class="method-row">

#### [getBlockDeviceTemplateGroups](/reference/services/SoftLayer_Account/getBlockDeviceTemplateGroups)
Retrieve private template group objects (parent and children) and the shared template group objects (parent only) for an account.
</div>

<div class="method-row">

#### [getBluemixAccountLink](/reference/services/SoftLayer_Account/getBluemixAccountLink)
Retrieve the Bluemix account link associated with this SoftLayer account, if one exists.
</div>

<div class="method-row">

#### [getBluemixLinkedFlag](/reference/services/SoftLayer_Account/getBluemixLinkedFlag)
Retrieve returns true if this account is linked to IBM Bluemix, false if not.
</div>

<div class="method-row">

#### [getBrand](/reference/services/SoftLayer_Account/getBrand)

</div>

<div class="method-row">

#### [getBrandAccountFlag](/reference/services/SoftLayer_Account/getBrandAccountFlag)

</div>

<div class="method-row">

#### [getBrandKeyName](/reference/services/SoftLayer_Account/getBrandKeyName)
Retrieve the brand keyName.
</div>

<div class="method-row">

#### [getBusinessPartner](/reference/services/SoftLayer_Account/getBusinessPartner)
Retrieve the Business Partner details for the account. Country Enterprise Code, Channel, Segment, Reseller Level.
</div>

<div class="method-row">

#### [getCanOrderAdditionalVlansFlag](/reference/services/SoftLayer_Account/getCanOrderAdditionalVlansFlag)
Retrieve [DEPRECATED] All accounts may order VLANs.
</div>

<div class="method-row">

#### [getCarts](/reference/services/SoftLayer_Account/getCarts)
Retrieve an account's active carts.
</div>

<div class="method-row">

#### [getCatalystEnrollments](/reference/services/SoftLayer_Account/getCatalystEnrollments)

</div>

<div class="method-row">

#### [getClosedTickets](/reference/services/SoftLayer_Account/getClosedTickets)
Retrieve all closed tickets associated with an account.
</div>

<div class="method-row">

#### [getCurrentBackupStatisticsGraph](/reference/services/SoftLayer_Account/getCurrentBackupStatisticsGraph)
This method retrieves a pie chart for today's backup statistics.
</div>

<div class="method-row">

#### [getCurrentTicketStatisticsGraph](/reference/services/SoftLayer_Account/getCurrentTicketStatisticsGraph)
(Deprecated)
</div>

<div class="method-row">

#### [getCurrentUser](/reference/services/SoftLayer_Account/getCurrentUser)
Retrieve the current API user's record.
</div>

<div class="method-row">

#### [getDatacentersWithSubnetAllocations](/reference/services/SoftLayer_Account/getDatacentersWithSubnetAllocations)
Retrieve datacenters which contain subnets that the account has access to route.
</div>

<div class="method-row">

#### [getDedicatedHosts](/reference/services/SoftLayer_Account/getDedicatedHosts)
Retrieve an account's associated virtual dedicated host objects.
</div>

<div class="method-row">

#### [getDedicatedHostsForImageTemplate](/reference/services/SoftLayer_Account/getDedicatedHostsForImageTemplate)
Get a collection of dedicated hosts that are valid for a given image template. 
</div>

<div class="method-row">

#### [getDisablePaymentProcessingFlag](/reference/services/SoftLayer_Account/getDisablePaymentProcessingFlag)
Retrieve a flag indicating whether payments are processed for this account.
</div>

<div class="method-row">

#### [getDiskUsageMetricDataByDate](/reference/services/SoftLayer_Account/getDiskUsageMetricDataByDate)
Retrieve the metric data for disk space usage for a storage repository from the Metric Tracking Object System and the Legacy Data Warehouse. 
</div>

<div class="method-row">

#### [getDiskUsageMetricDataFromLegacyByDate](/reference/services/SoftLayer_Account/getDiskUsageMetricDataFromLegacyByDate)
Retrieve the metric data for disk space usage for a storage repository from the Legacy Data Warehouse. 
</div>

<div class="method-row">

#### [getDiskUsageMetricDataFromMetricTrackingObjectSystemByDate](/reference/services/SoftLayer_Account/getDiskUsageMetricDataFromMetricTrackingObjectSystemByDate)
Retrieve the metric data for disk space usage for a storage repository from the Metric Tracking Object System. 
</div>

<div class="method-row">

#### [getDiskUsageMetricImageByDate](/reference/services/SoftLayer_Account/getDiskUsageMetricImageByDate)
Retrieve an image of the disk usage data on a [SoftLayer_Virtual_Guest]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest">}}) image for the time range you provide. 
</div>

<div class="method-row">

#### [getDisplaySupportRepresentativeAssignments](/reference/services/SoftLayer_Account/getDisplaySupportRepresentativeAssignments)
Retrieve the SoftLayer employees that an account is assigned to.
</div>

<div class="method-row">

#### [getDomainRegistrations](/reference/services/SoftLayer_Account/getDomainRegistrations)

</div>

<div class="method-row">

#### [getDomains](/reference/services/SoftLayer_Account/getDomains)
Retrieve the DNS domains associated with an account.
</div>

<div class="method-row">

#### [getDomainsWithoutSecondaryDnsRecords](/reference/services/SoftLayer_Account/getDomainsWithoutSecondaryDnsRecords)
Retrieve the DNS domains associated with an account that were not created as a result of a secondary DNS zone transfer.
</div>

<div class="method-row">

#### [getEuSupportedFlag](/reference/services/SoftLayer_Account/getEuSupportedFlag)
Retrieve boolean flag dictating whether or not this account has the EU Supported flag. This flag indicates that this account uses IBM Cloud services to process EU citizen's personal data.
</div>

<div class="method-row">

#### [getEvaultCapacityGB](/reference/services/SoftLayer_Account/getEvaultCapacityGB)
Retrieve the total capacity of Legacy EVault Volumes on an account, in GB.
</div>

<div class="method-row">

#### [getEvaultMasterUsers](/reference/services/SoftLayer_Account/getEvaultMasterUsers)
Retrieve an account's master EVault user. This is only used when an account has EVault service.
</div>

<div class="method-row">

#### [getEvaultNetworkStorage](/reference/services/SoftLayer_Account/getEvaultNetworkStorage)
Retrieve an account's associated EVault storage volumes.
</div>

<div class="method-row">

#### [getExecutiveSummaryPdf](/reference/services/SoftLayer_Account/getExecutiveSummaryPdf)
This method provides an executive summary PDF for managed hosting services. 
</div>

<div class="method-row">

#### [getExpiredSecurityCertificates](/reference/services/SoftLayer_Account/getExpiredSecurityCertificates)
Retrieve stored security certificates that are expired (ie. SSL)
</div>

<div class="method-row">

#### [getFacilityLogs](/reference/services/SoftLayer_Account/getFacilityLogs)
Retrieve logs of who entered a colocation area which is assigned to this account, or when a user under this account enters a datacenter.
</div>

<div class="method-row">

#### [getFileBlockBetaAccessFlag](/reference/services/SoftLayer_Account/getFileBlockBetaAccessFlag)

</div>

<div class="method-row">

#### [getFlexibleCreditEnrollments](/reference/services/SoftLayer_Account/getFlexibleCreditEnrollments)
Retrieve all of the account's current and former Flexible Credit enrollments.
</div>

<div class="method-row">

#### [getFlexibleCreditProgramInfo](/reference/services/SoftLayer_Account/getFlexibleCreditProgramInfo)
[DEPRECATED] Please use SoftLayer_Account::getFlexibleCreditProgramsInfo. This is no longer an accurate representation of discounts. 
</div>

<div class="method-row">

#### [getFlexibleCreditProgramsInfo](/reference/services/SoftLayer_Account/getFlexibleCreditProgramsInfo)
This method retrieves information on all of your Flexible Credit Program enrollments for your account. 
</div>

<div class="method-row">

#### [getForcePaasAccountLinkDate](/reference/services/SoftLayer_Account/getForcePaasAccountLinkDate)
Retrieve timestamp representing the point in time when an account is required to link with PaaS.
</div>

<div class="method-row">

#### [getGlobalIpRecords](/reference/services/SoftLayer_Account/getGlobalIpRecords)

</div>

<div class="method-row">

#### [getGlobalIpv4Records](/reference/services/SoftLayer_Account/getGlobalIpv4Records)

</div>

<div class="method-row">

#### [getGlobalIpv6Records](/reference/services/SoftLayer_Account/getGlobalIpv6Records)

</div>

<div class="method-row">

#### [getGlobalLoadBalancerAccounts](/reference/services/SoftLayer_Account/getGlobalLoadBalancerAccounts)
Retrieve [Deprecated] The global load balancer accounts for a softlayer customer account.
</div>

<div class="method-row">

#### [getHardware](/reference/services/SoftLayer_Account/getHardware)
Retrieve an account's associated hardware objects.
</div>

<div class="method-row">

#### [getHardwareOverBandwidthAllocation](/reference/services/SoftLayer_Account/getHardwareOverBandwidthAllocation)
Retrieve an account's associated hardware objects currently over bandwidth allocation.
</div>

<div class="method-row">

#### [getHardwarePools](/reference/services/SoftLayer_Account/getHardwarePools)
Get a collection of managed hardware pools.
</div>

<div class="method-row">

#### [getHardwareProjectedOverBandwidthAllocation](/reference/services/SoftLayer_Account/getHardwareProjectedOverBandwidthAllocation)
Retrieve an account's associated hardware objects projected to go over bandwidth allocation.
</div>

<div class="method-row">

#### [getHardwareWithCpanel](/reference/services/SoftLayer_Account/getHardwareWithCpanel)
Retrieve all hardware associated with an account that has the cPanel web hosting control panel installed.
</div>

<div class="method-row">

#### [getHardwareWithHelm](/reference/services/SoftLayer_Account/getHardwareWithHelm)
Retrieve all hardware associated with an account that has the Helm web hosting control panel installed.
</div>

<div class="method-row">

#### [getHardwareWithMcafee](/reference/services/SoftLayer_Account/getHardwareWithMcafee)
Retrieve all hardware associated with an account that has McAfee Secure software components.
</div>

<div class="method-row">

#### [getHardwareWithMcafeeAntivirusRedhat](/reference/services/SoftLayer_Account/getHardwareWithMcafeeAntivirusRedhat)
Retrieve all hardware associated with an account that has McAfee Secure AntiVirus for Redhat software components.
</div>

<div class="method-row">

#### [getHardwareWithMcafeeAntivirusWindows](/reference/services/SoftLayer_Account/getHardwareWithMcafeeAntivirusWindows)
Retrieve all hardware associated with an account that has McAfee Secure AntiVirus for Windows software components.
</div>

<div class="method-row">

#### [getHardwareWithMcafeeIntrusionDetectionSystem](/reference/services/SoftLayer_Account/getHardwareWithMcafeeIntrusionDetectionSystem)
Retrieve all hardware associated with an account that has McAfee Secure Intrusion Detection System software components.
</div>

<div class="method-row">

#### [getHardwareWithPlesk](/reference/services/SoftLayer_Account/getHardwareWithPlesk)
Retrieve all hardware associated with an account that has the Plesk web hosting control panel installed.
</div>

<div class="method-row">

#### [getHardwareWithQuantastor](/reference/services/SoftLayer_Account/getHardwareWithQuantastor)
Retrieve all hardware associated with an account that has the QuantaStor storage system installed.
</div>

<div class="method-row">

#### [getHardwareWithUrchin](/reference/services/SoftLayer_Account/getHardwareWithUrchin)
Retrieve all hardware associated with an account that has the Urchin web traffic analytics package installed.
</div>

<div class="method-row">

#### [getHardwareWithWindows](/reference/services/SoftLayer_Account/getHardwareWithWindows)
Retrieve all hardware associated with an account that is running a version of the Microsoft Windows operating system.
</div>

<div class="method-row">

#### [getHasEvaultBareMetalRestorePluginFlag](/reference/services/SoftLayer_Account/getHasEvaultBareMetalRestorePluginFlag)
Retrieve return 1 if one of the account's hardware has the EVault Bare Metal Server Restore Plugin otherwise 0.
</div>

<div class="method-row">

#### [getHasIderaBareMetalRestorePluginFlag](/reference/services/SoftLayer_Account/getHasIderaBareMetalRestorePluginFlag)
Retrieve return 1 if one of the account's hardware has an installation of Idera Server Backup otherwise 0.
</div>

<div class="method-row">

#### [getHasPendingOrder](/reference/services/SoftLayer_Account/getHasPendingOrder)
Retrieve the number of orders in a PENDING status for a SoftLayer customer account.
</div>

<div class="method-row">

#### [getHasR1softBareMetalRestorePluginFlag](/reference/services/SoftLayer_Account/getHasR1softBareMetalRestorePluginFlag)
Retrieve return 1 if one of the account's hardware has an installation of R1Soft CDP otherwise 0.
</div>

<div class="method-row">

#### [getHistoricalBackupGraph](/reference/services/SoftLayer_Account/getHistoricalBackupGraph)

</div>

<div class="method-row">

#### [getHistoricalBandwidthGraph](/reference/services/SoftLayer_Account/getHistoricalBandwidthGraph)
[DEPRECATED] This method returns a line graph of bandwidth statistics.
</div>

<div class="method-row">

#### [getHistoricalTicketGraph](/reference/services/SoftLayer_Account/getHistoricalTicketGraph)
This method returns a pie chart of ticket statistics for the given dates.
</div>

<div class="method-row">

#### [getHistoricalUptimeGraph](/reference/services/SoftLayer_Account/getHistoricalUptimeGraph)
This method returns a SoftLayer_Container_Account_Graph_Outputs object for the specified date range. 
</div>

<div class="method-row">

#### [getHourlyBareMetalInstances](/reference/services/SoftLayer_Account/getHourlyBareMetalInstances)
Retrieve an account's associated hourly bare metal server objects.
</div>

<div class="method-row">

#### [getHourlyServiceBillingItems](/reference/services/SoftLayer_Account/getHourlyServiceBillingItems)
Retrieve hourly service billing items that will be on an account's next invoice.
</div>

<div class="method-row">

#### [getHourlyVirtualGuests](/reference/services/SoftLayer_Account/getHourlyVirtualGuests)
Retrieve an account's associated hourly virtual guest objects.
</div>

<div class="method-row">

#### [getHubNetworkStorage](/reference/services/SoftLayer_Account/getHubNetworkStorage)
Retrieve an account's associated Virtual Storage volumes.
</div>

<div class="method-row">

#### [getIbmCustomerNumber](/reference/services/SoftLayer_Account/getIbmCustomerNumber)
Retrieve unique identifier for a customer used throughout IBM.
</div>

<div class="method-row">

#### [getIbmIdAuthenticationRequiredFlag](/reference/services/SoftLayer_Account/getIbmIdAuthenticationRequiredFlag)
Retrieve indicates whether this account requires IBMid authentication.
</div>

<div class="method-row">

#### [getIbmIdMigrationExpirationTimestamp](/reference/services/SoftLayer_Account/getIbmIdMigrationExpirationTimestamp)
Retrieve this key is deprecated and should not be used.
</div>

<div class="method-row">

#### [getInProgressExternalAccountSetup](/reference/services/SoftLayer_Account/getInProgressExternalAccountSetup)
Retrieve an in progress request to switch billing systems.
</div>

<div class="method-row">

#### [getInternalNotes](/reference/services/SoftLayer_Account/getInternalNotes)

</div>

<div class="method-row">

#### [getInvoices](/reference/services/SoftLayer_Account/getInvoices)
Retrieve an account's associated billing invoices.
</div>

<div class="method-row">

#### [getIpAddresses](/reference/services/SoftLayer_Account/getIpAddresses)

</div>

<div class="method-row">

#### [getIscsiIsolationDisabled](/reference/services/SoftLayer_Account/getIscsiIsolationDisabled)

</div>

<div class="method-row">

#### [getIscsiNetworkStorage](/reference/services/SoftLayer_Account/getIscsiNetworkStorage)
Retrieve an account's associated iSCSI storage volumes.
</div>

<div class="method-row">

#### [getLargestAllowedSubnetCidr](/reference/services/SoftLayer_Account/getLargestAllowedSubnetCidr)
Computes the number of available public secondary IP addresses, augmented by the provided number of hosts, before overflow of the allowed host to IP address ratio occurs. The result is aligned to the nearest subnet size that could be accommodated in full. 

0 is returned if an overflow is detected. 

The use of $locationId has been deprecated. 
</div>

<div class="method-row">

#### [getLastCanceledBillingItem](/reference/services/SoftLayer_Account/getLastCanceledBillingItem)
Retrieve the most recently canceled billing item.
</div>

<div class="method-row">

#### [getLastCancelledServerBillingItem](/reference/services/SoftLayer_Account/getLastCancelledServerBillingItem)
Retrieve the most recent cancelled server billing item.
</div>

<div class="method-row">

#### [getLastFiveClosedAbuseTickets](/reference/services/SoftLayer_Account/getLastFiveClosedAbuseTickets)
Retrieve the five most recently closed abuse tickets associated with an account.
</div>

<div class="method-row">

#### [getLastFiveClosedAccountingTickets](/reference/services/SoftLayer_Account/getLastFiveClosedAccountingTickets)
Retrieve the five most recently closed accounting tickets associated with an account.
</div>

<div class="method-row">

#### [getLastFiveClosedOtherTickets](/reference/services/SoftLayer_Account/getLastFiveClosedOtherTickets)
Retrieve the five most recently closed tickets that do not belong to the abuse, accounting, sales, or support groups associated with an account.
</div>

<div class="method-row">

#### [getLastFiveClosedSalesTickets](/reference/services/SoftLayer_Account/getLastFiveClosedSalesTickets)
Retrieve the five most recently closed sales tickets associated with an account.
</div>

<div class="method-row">

#### [getLastFiveClosedSupportTickets](/reference/services/SoftLayer_Account/getLastFiveClosedSupportTickets)
Retrieve the five most recently closed support tickets associated with an account.
</div>

<div class="method-row">

#### [getLastFiveClosedTickets](/reference/services/SoftLayer_Account/getLastFiveClosedTickets)
Retrieve the five most recently closed tickets associated with an account.
</div>

<div class="method-row">

#### [getLatestBillDate](/reference/services/SoftLayer_Account/getLatestBillDate)
Retrieve an account's most recent billing date.
</div>

<div class="method-row">

#### [getLatestRecurringInvoice](/reference/services/SoftLayer_Account/getLatestRecurringInvoice)
Retrieve an account's latest recurring invoice.
</div>

<div class="method-row">

#### [getLatestRecurringPendingInvoice](/reference/services/SoftLayer_Account/getLatestRecurringPendingInvoice)
Retrieve an account's latest recurring pending invoice.
</div>

<div class="method-row">

#### [getLegacyBandwidthAllotments](/reference/services/SoftLayer_Account/getLegacyBandwidthAllotments)
Retrieve the legacy bandwidth allotments for an account.
</div>

<div class="method-row">

#### [getLegacyIscsiCapacityGB](/reference/services/SoftLayer_Account/getLegacyIscsiCapacityGB)
Retrieve the total capacity of Legacy iSCSI Volumes on an account, in GB.
</div>

<div class="method-row">

#### [getLoadBalancers](/reference/services/SoftLayer_Account/getLoadBalancers)
Retrieve an account's associated load balancers.
</div>

<div class="method-row">

#### [getLockboxCapacityGB](/reference/services/SoftLayer_Account/getLockboxCapacityGB)
Retrieve the total capacity of Legacy lockbox Volumes on an account, in GB.
</div>

<div class="method-row">

#### [getLockboxNetworkStorage](/reference/services/SoftLayer_Account/getLockboxNetworkStorage)
Retrieve an account's associated Lockbox storage volumes.
</div>

<div class="method-row">

#### [getManualPaymentsUnderReview](/reference/services/SoftLayer_Account/getManualPaymentsUnderReview)

</div>

<div class="method-row">

#### [getMasterUser](/reference/services/SoftLayer_Account/getMasterUser)
Retrieve an account's master user.
</div>

<div class="method-row">

#### [getMediaDataTransferRequests](/reference/services/SoftLayer_Account/getMediaDataTransferRequests)
Retrieve an account's media transfer service requests.
</div>

<div class="method-row">

#### [getMigratedToIbmCloudPortalFlag](/reference/services/SoftLayer_Account/getMigratedToIbmCloudPortalFlag)
Retrieve flag indicating whether this account is restricted to the IBM Cloud portal.
</div>

<div class="method-row">

#### [getMonthlyBareMetalInstances](/reference/services/SoftLayer_Account/getMonthlyBareMetalInstances)
Retrieve an account's associated monthly bare metal server objects.
</div>

<div class="method-row">

#### [getMonthlyVirtualGuests](/reference/services/SoftLayer_Account/getMonthlyVirtualGuests)
Retrieve an account's associated monthly virtual guest objects.
</div>

<div class="method-row">

#### [getNasNetworkStorage](/reference/services/SoftLayer_Account/getNasNetworkStorage)
Retrieve an account's associated NAS storage volumes.
</div>

<div class="method-row">

#### [getNetAppActiveAccountLicenseKeys](/reference/services/SoftLayer_Account/getNetAppActiveAccountLicenseKeys)
Get a collection of active NetApp software account license keys.
</div>

<div class="method-row">

#### [getNetworkCreationFlag](/reference/services/SoftLayer_Account/getNetworkCreationFlag)
Retrieve [Deprecated] Whether or not this account can define their own networks.
</div>

<div class="method-row">

#### [getNetworkGateways](/reference/services/SoftLayer_Account/getNetworkGateways)
Retrieve all network gateway devices on this account.
</div>

<div class="method-row">

#### [getNetworkHardware](/reference/services/SoftLayer_Account/getNetworkHardware)
Retrieve an account's associated network hardware.
</div>

<div class="method-row">

#### [getNetworkMessageDeliveryAccounts](/reference/services/SoftLayer_Account/getNetworkMessageDeliveryAccounts)

</div>

<div class="method-row">

#### [getNetworkMonitorDownHardware](/reference/services/SoftLayer_Account/getNetworkMonitorDownHardware)
Retrieve hardware which is currently experiencing a service failure.
</div>

<div class="method-row">

#### [getNetworkMonitorDownVirtualGuests](/reference/services/SoftLayer_Account/getNetworkMonitorDownVirtualGuests)
Retrieve virtual guest which is currently experiencing a service failure.
</div>

<div class="method-row">

#### [getNetworkMonitorRecoveringHardware](/reference/services/SoftLayer_Account/getNetworkMonitorRecoveringHardware)
Retrieve hardware which is currently recovering from a service failure.
</div>

<div class="method-row">

#### [getNetworkMonitorRecoveringVirtualGuests](/reference/services/SoftLayer_Account/getNetworkMonitorRecoveringVirtualGuests)
Retrieve virtual guest which is currently recovering from a service failure.
</div>

<div class="method-row">

#### [getNetworkMonitorUpHardware](/reference/services/SoftLayer_Account/getNetworkMonitorUpHardware)
Retrieve hardware which is currently online.
</div>

<div class="method-row">

#### [getNetworkMonitorUpVirtualGuests](/reference/services/SoftLayer_Account/getNetworkMonitorUpVirtualGuests)
Retrieve virtual guest which is currently online.
</div>

<div class="method-row">

#### [getNetworkStorage](/reference/services/SoftLayer_Account/getNetworkStorage)
Retrieve an account's associated storage volumes. This includes Lockbox, NAS, EVault, and iSCSI volumes.
</div>

<div class="method-row">

#### [getNetworkStorageGroups](/reference/services/SoftLayer_Account/getNetworkStorageGroups)
Retrieve an account's Network Storage groups.
</div>

<div class="method-row">

#### [getNetworkTunnelContexts](/reference/services/SoftLayer_Account/getNetworkTunnelContexts)
Retrieve iPSec network tunnels for an account.
</div>

<div class="method-row">

#### [getNetworkVlanSpan](/reference/services/SoftLayer_Account/getNetworkVlanSpan)
Retrieve whether or not an account has automatic private VLAN spanning enabled.
</div>

<div class="method-row">

#### [getNetworkVlans](/reference/services/SoftLayer_Account/getNetworkVlans)
Retrieve all network VLANs assigned to an account.
</div>

<div class="method-row">

#### [getNextBillingPublicAllotmentHardwareBandwidthDetails](/reference/services/SoftLayer_Account/getNextBillingPublicAllotmentHardwareBandwidthDetails)
Retrieval: DEPRECATED - This information can be pulled directly through tapping keys now - DEPRECATED. The allotments for this account and their servers for the next billing cycle. The public inbound and outbound bandwidth is calculated for each server in addition to the daily average network traffic since the last billing date.
</div>

<div class="method-row">

#### [getNextInvoiceExcel](/reference/services/SoftLayer_Account/getNextInvoiceExcel)
Retrieve the next billing period's invoice. Note, this should be considered preliminary as you may add, remove, change billing items on your account.
</div>

<div class="method-row">

#### [getNextInvoiceIncubatorExemptTotal](/reference/services/SoftLayer_Account/getNextInvoiceIncubatorExemptTotal)
Retrieve the pre-tax total amount exempt from incubator credit for the account's next invoice. This field is now deprecated and will soon be removed. Please update all references to instead use nextInvoiceTotalAmount
</div>

<div class="method-row">

#### [getNextInvoicePdf](/reference/services/SoftLayer_Account/getNextInvoicePdf)
Retrieve the next billing period's invoice. Note, this should be considered preliminary as you may add, remove, change billing items on your account.
</div>

<div class="method-row">

#### [getNextInvoicePdfDetailed](/reference/services/SoftLayer_Account/getNextInvoicePdfDetailed)
Retrieve the next billing period's detailed invoice. Note, this should be considered preliminary as you may add, remove, change billing items on your account.
</div>

<div class="method-row">

#### [getNextInvoiceRecurringAmountEligibleForAccountDiscount](/reference/services/SoftLayer_Account/getNextInvoiceRecurringAmountEligibleForAccountDiscount)
Retrieve the total recurring charge amount of an account's next invoice eligible for account discount measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.
</div>

<div class="method-row">

#### [getNextInvoiceTopLevelBillingItems](/reference/services/SoftLayer_Account/getNextInvoiceTopLevelBillingItems)
Retrieve the billing items that will be on an account's next invoice.
</div>

<div class="method-row">

#### [getNextInvoiceTotalAmount](/reference/services/SoftLayer_Account/getNextInvoiceTotalAmount)
Retrieve the pre-tax total amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.
</div>

<div class="method-row">

#### [getNextInvoiceTotalOneTimeAmount](/reference/services/SoftLayer_Account/getNextInvoiceTotalOneTimeAmount)
Retrieve the total one-time charge amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.
</div>

<div class="method-row">

#### [getNextInvoiceTotalOneTimeTaxAmount](/reference/services/SoftLayer_Account/getNextInvoiceTotalOneTimeTaxAmount)
Retrieve the total one-time tax amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.
</div>

<div class="method-row">

#### [getNextInvoiceTotalRecurringAmount](/reference/services/SoftLayer_Account/getNextInvoiceTotalRecurringAmount)
Retrieve the total recurring charge amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.
</div>

<div class="method-row">

#### [getNextInvoiceTotalRecurringAmountBeforeAccountDiscount](/reference/services/SoftLayer_Account/getNextInvoiceTotalRecurringAmountBeforeAccountDiscount)
Retrieve the total recurring charge amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.
</div>

<div class="method-row">

#### [getNextInvoiceTotalRecurringTaxAmount](/reference/services/SoftLayer_Account/getNextInvoiceTotalRecurringTaxAmount)
Retrieve the total recurring tax amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.
</div>

<div class="method-row">

#### [getNextInvoiceTotalTaxableRecurringAmount](/reference/services/SoftLayer_Account/getNextInvoiceTotalTaxableRecurringAmount)
Retrieve the total recurring charge amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.
</div>

<div class="method-row">

#### [getNextInvoiceZeroFeeItemCounts](/reference/services/SoftLayer_Account/getNextInvoiceZeroFeeItemCounts)

</div>

<div class="method-row">

#### [getNotificationSubscribers](/reference/services/SoftLayer_Account/getNotificationSubscribers)

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Account/getObject)
Retrieve a SoftLayer_Account record.
</div>

<div class="method-row">

#### [getOpenAbuseTickets](/reference/services/SoftLayer_Account/getOpenAbuseTickets)
Retrieve the open abuse tickets associated with an account.
</div>

<div class="method-row">

#### [getOpenAccountingTickets](/reference/services/SoftLayer_Account/getOpenAccountingTickets)
Retrieve the open accounting tickets associated with an account.
</div>

<div class="method-row">

#### [getOpenBillingTickets](/reference/services/SoftLayer_Account/getOpenBillingTickets)
Retrieve the open billing tickets associated with an account.
</div>

<div class="method-row">

#### [getOpenCancellationRequests](/reference/services/SoftLayer_Account/getOpenCancellationRequests)
Retrieve an open ticket requesting cancellation of this server, if one exists.
</div>

<div class="method-row">

#### [getOpenOtherTickets](/reference/services/SoftLayer_Account/getOpenOtherTickets)
Retrieve the open tickets that do not belong to the abuse, accounting, sales, or support groups associated with an account.
</div>

<div class="method-row">

#### [getOpenRecurringInvoices](/reference/services/SoftLayer_Account/getOpenRecurringInvoices)
Retrieve an account's recurring invoices.
</div>

<div class="method-row">

#### [getOpenSalesTickets](/reference/services/SoftLayer_Account/getOpenSalesTickets)
Retrieve the open sales tickets associated with an account.
</div>

<div class="method-row">

#### [getOpenStackAccountLinks](/reference/services/SoftLayer_Account/getOpenStackAccountLinks)

</div>

<div class="method-row">

#### [getOpenStackObjectStorage](/reference/services/SoftLayer_Account/getOpenStackObjectStorage)
Retrieve an account's associated Openstack related Object Storage accounts.
</div>

<div class="method-row">

#### [getOpenSupportTickets](/reference/services/SoftLayer_Account/getOpenSupportTickets)
Retrieve the open support tickets associated with an account.
</div>

<div class="method-row">

#### [getOpenTickets](/reference/services/SoftLayer_Account/getOpenTickets)
Retrieve all open tickets associated with an account.
</div>

<div class="method-row">

#### [getOpenTicketsWaitingOnCustomer](/reference/services/SoftLayer_Account/getOpenTicketsWaitingOnCustomer)
Retrieve all open tickets associated with an account last edited by an employee.
</div>

<div class="method-row">

#### [getOrders](/reference/services/SoftLayer_Account/getOrders)
Retrieve an account's associated billing orders excluding upgrades.
</div>

<div class="method-row">

#### [getOrphanBillingItems](/reference/services/SoftLayer_Account/getOrphanBillingItems)
Retrieve the billing items that have no parent billing item. These are items that don't necessarily belong to a single server.
</div>

<div class="method-row">

#### [getOwnedBrands](/reference/services/SoftLayer_Account/getOwnedBrands)

</div>

<div class="method-row">

#### [getOwnedHardwareGenericComponentModels](/reference/services/SoftLayer_Account/getOwnedHardwareGenericComponentModels)

</div>

<div class="method-row">

#### [getPaymentProcessors](/reference/services/SoftLayer_Account/getPaymentProcessors)

</div>

<div class="method-row">

#### [getPendingCreditCardChangeRequestData](/reference/services/SoftLayer_Account/getPendingCreditCardChangeRequestData)
Retrieve details of all credit card change requests which have not been processed by a SoftLayer agent.
</div>

<div class="method-row">

#### [getPendingEvents](/reference/services/SoftLayer_Account/getPendingEvents)

</div>

<div class="method-row">

#### [getPendingInvoice](/reference/services/SoftLayer_Account/getPendingInvoice)
Retrieve an account's latest open (pending) invoice.
</div>

<div class="method-row">

#### [getPendingInvoiceTopLevelItems](/reference/services/SoftLayer_Account/getPendingInvoiceTopLevelItems)
Retrieve a list of top-level invoice items that are on an account's currently pending invoice.
</div>

<div class="method-row">

#### [getPendingInvoiceTotalAmount](/reference/services/SoftLayer_Account/getPendingInvoiceTotalAmount)
Retrieve the total amount of an account's pending invoice, if one exists.
</div>

<div class="method-row">

#### [getPendingInvoiceTotalOneTimeAmount](/reference/services/SoftLayer_Account/getPendingInvoiceTotalOneTimeAmount)
Retrieve the total one-time charges for an account's pending invoice, if one exists. In other words, it is the sum of one-time charges, setup fees, and labor fees. It does not include taxes.
</div>

<div class="method-row">

#### [getPendingInvoiceTotalOneTimeTaxAmount](/reference/services/SoftLayer_Account/getPendingInvoiceTotalOneTimeTaxAmount)
Retrieve the sum of all the taxes related to one time charges for an account's pending invoice, if one exists.
</div>

<div class="method-row">

#### [getPendingInvoiceTotalRecurringAmount](/reference/services/SoftLayer_Account/getPendingInvoiceTotalRecurringAmount)
Retrieve the total recurring amount of an account's pending invoice, if one exists.
</div>

<div class="method-row">

#### [getPendingInvoiceTotalRecurringTaxAmount](/reference/services/SoftLayer_Account/getPendingInvoiceTotalRecurringTaxAmount)
Retrieve the total amount of the recurring taxes on an account's pending invoice, if one exists.
</div>

<div class="method-row">

#### [getPermissionGroups](/reference/services/SoftLayer_Account/getPermissionGroups)
Retrieve an account's permission groups.
</div>

<div class="method-row">

#### [getPermissionRoles](/reference/services/SoftLayer_Account/getPermissionRoles)
Retrieve an account's user roles.
</div>

<div class="method-row">

#### [getPlacementGroups](/reference/services/SoftLayer_Account/getPlacementGroups)
Retrieve an account's associated virtual placement groups.
</div>

<div class="method-row">

#### [getPortableStorageVolumes](/reference/services/SoftLayer_Account/getPortableStorageVolumes)

</div>

<div class="method-row">

#### [getPostProvisioningHooks](/reference/services/SoftLayer_Account/getPostProvisioningHooks)
Retrieve customer specified URIs that are downloaded onto a newly provisioned or reloaded server. If the URI is sent over https it will be executed directly on the server.
</div>

<div class="method-row">

#### [getPptpVpnAllowedFlag](/reference/services/SoftLayer_Account/getPptpVpnAllowedFlag)
Retrieve (Deprecated) Boolean flag dictating whether or not this account supports PPTP VPN Access.
</div>

<div class="method-row">

#### [getPptpVpnUsers](/reference/services/SoftLayer_Account/getPptpVpnUsers)
Retrieve an account's associated portal users with PPTP VPN access. (Deprecated)
</div>

<div class="method-row">

#### [getPreviousRecurringRevenue](/reference/services/SoftLayer_Account/getPreviousRecurringRevenue)
Retrieve the total recurring amount for an accounts previous revenue.
</div>

<div class="method-row">

#### [getPriceRestrictions](/reference/services/SoftLayer_Account/getPriceRestrictions)
Retrieve the item price that an account is restricted to.
</div>

<div class="method-row">

#### [getPriorityOneTickets](/reference/services/SoftLayer_Account/getPriorityOneTickets)
Retrieve all priority one tickets associated with an account.
</div>

<div class="method-row">

#### [getPrivateAllotmentHardwareBandwidthDetails](/reference/services/SoftLayer_Account/getPrivateAllotmentHardwareBandwidthDetails)
Retrieval: DEPRECATED - This information can be pulled directly through tapping keys now - DEPRECATED. The allotments for this account and their servers. The private inbound and outbound bandwidth is calculated for each server in addition to the daily average network traffic since the last billing date.
</div>

<div class="method-row">

#### [getPrivateBlockDeviceTemplateGroups](/reference/services/SoftLayer_Account/getPrivateBlockDeviceTemplateGroups)
Retrieve private and shared template group objects (parent only) for an account.
</div>

<div class="method-row">

#### [getPrivateIpAddresses](/reference/services/SoftLayer_Account/getPrivateIpAddresses)

</div>

<div class="method-row">

#### [getPrivateNetworkVlans](/reference/services/SoftLayer_Account/getPrivateNetworkVlans)
Retrieve the private network VLANs assigned to an account.
</div>

<div class="method-row">

#### [getPrivateSubnets](/reference/services/SoftLayer_Account/getPrivateSubnets)
Retrieve all private subnets associated with an account.
</div>

<div class="method-row">

#### [getProofOfConceptAccountFlag](/reference/services/SoftLayer_Account/getProofOfConceptAccountFlag)
Retrieve boolean flag indicating whether or not this account is a Proof of Concept account.
</div>

<div class="method-row">

#### [getPublicAllotmentHardwareBandwidthDetails](/reference/services/SoftLayer_Account/getPublicAllotmentHardwareBandwidthDetails)
Retrieval: DEPRECATED - This information can be pulled directly through tapping keys now - DEPRECATED. The allotments for this account and their servers. The public inbound and outbound bandwidth is calculated for each server in addition to the daily average network traffic since the last billing date.
</div>

<div class="method-row">

#### [getPublicIpAddresses](/reference/services/SoftLayer_Account/getPublicIpAddresses)

</div>

<div class="method-row">

#### [getPublicNetworkVlans](/reference/services/SoftLayer_Account/getPublicNetworkVlans)
Retrieve the public network VLANs assigned to an account.
</div>

<div class="method-row">

#### [getPublicSubnets](/reference/services/SoftLayer_Account/getPublicSubnets)
Retrieve all public network subnets associated with an account.
</div>

<div class="method-row">

#### [getQuotes](/reference/services/SoftLayer_Account/getQuotes)
Retrieve an account's quotes.
</div>

<div class="method-row">

#### [getRecentEvents](/reference/services/SoftLayer_Account/getRecentEvents)

</div>

<div class="method-row">

#### [getReferralPartner](/reference/services/SoftLayer_Account/getReferralPartner)
Retrieve the Referral Partner for this account, if any.
</div>

<div class="method-row">

#### [getReferralPartnerCommissionForecast](/reference/services/SoftLayer_Account/getReferralPartnerCommissionForecast)

</div>

<div class="method-row">

#### [getReferralPartnerCommissionHistory](/reference/services/SoftLayer_Account/getReferralPartnerCommissionHistory)

</div>

<div class="method-row">

#### [getReferralPartnerCommissionPending](/reference/services/SoftLayer_Account/getReferralPartnerCommissionPending)

</div>

<div class="method-row">

#### [getReferredAccounts](/reference/services/SoftLayer_Account/getReferredAccounts)
Retrieve if this is a account is a referral partner, the accounts this referral partner has referred
</div>

<div class="method-row">

#### [getRegulatedWorkloads](/reference/services/SoftLayer_Account/getRegulatedWorkloads)

</div>

<div class="method-row">

#### [getRemoteManagementCommandRequests](/reference/services/SoftLayer_Account/getRemoteManagementCommandRequests)
Retrieve remote management command requests for an account
</div>

<div class="method-row">

#### [getReplicationEvents](/reference/services/SoftLayer_Account/getReplicationEvents)
Retrieve the Replication events for all Network Storage volumes on an account.
</div>

<div class="method-row">

#### [getRequireSilentIBMidUserCreation](/reference/services/SoftLayer_Account/getRequireSilentIBMidUserCreation)
Retrieve indicates whether newly created users under this account will be associated with IBMid via an email requiring a response, or not.
</div>

<div class="method-row">

#### [getReservedCapacityAgreements](/reference/services/SoftLayer_Account/getReservedCapacityAgreements)
Retrieve all reserved capacity agreements for an account
</div>

<div class="method-row">

#### [getReservedCapacityGroups](/reference/services/SoftLayer_Account/getReservedCapacityGroups)
Retrieve the reserved capacity groups owned by this account.
</div>

<div class="method-row">

#### [getResourceGroups](/reference/services/SoftLayer_Account/getResourceGroups)
Retrieve an account's associated top-level resource groups.
</div>

<div class="method-row">

#### [getRouters](/reference/services/SoftLayer_Account/getRouters)
Retrieve all Routers that an accounts VLANs reside on
</div>

<div class="method-row">

#### [getRwhoisData](/reference/services/SoftLayer_Account/getRwhoisData)
Retrieval: DEPRECATED
</div>

<div class="method-row">

#### [getSamlAuthentication](/reference/services/SoftLayer_Account/getSamlAuthentication)
Retrieve the SAML configuration for this account.
</div>

<div class="method-row">

#### [getScaleGroups](/reference/services/SoftLayer_Account/getScaleGroups)
Retrieve all scale groups on this account.
</div>

<div class="method-row">

#### [getSecondaryDomains](/reference/services/SoftLayer_Account/getSecondaryDomains)
Retrieve the secondary DNS records for a SoftLayer customer account.
</div>

<div class="method-row">

#### [getSecurityCertificates](/reference/services/SoftLayer_Account/getSecurityCertificates)
Retrieve stored security certificates (ie. SSL)
</div>

<div class="method-row">

#### [getSecurityGroups](/reference/services/SoftLayer_Account/getSecurityGroups)
Retrieve the security groups belonging to this account.
</div>

<div class="method-row">

#### [getSecurityLevel](/reference/services/SoftLayer_Account/getSecurityLevel)

</div>

<div class="method-row">

#### [getSecurityScanRequests](/reference/services/SoftLayer_Account/getSecurityScanRequests)
Retrieve an account's vulnerability scan requests.
</div>

<div class="method-row">

#### [getServiceBillingItems](/reference/services/SoftLayer_Account/getServiceBillingItems)
Retrieve the service billing items that will be on an account's next invoice. 
</div>

<div class="method-row">

#### [getSharedBlockDeviceTemplateGroups](/reference/services/SoftLayer_Account/getSharedBlockDeviceTemplateGroups)
Get the collection of template group objects that have been shared with this account.
</div>

<div class="method-row">

#### [getShipments](/reference/services/SoftLayer_Account/getShipments)
Retrieve shipments that belong to the customer's account.
</div>

<div class="method-row">

#### [getSshKeys](/reference/services/SoftLayer_Account/getSshKeys)
Retrieve customer specified SSH keys that can be implemented onto a newly provisioned or reloaded server.
</div>

<div class="method-row">

#### [getSslVpnUsers](/reference/services/SoftLayer_Account/getSslVpnUsers)
Retrieve an account's associated portal users with SSL VPN access.
</div>

<div class="method-row">

#### [getStandardPoolVirtualGuests](/reference/services/SoftLayer_Account/getStandardPoolVirtualGuests)
Retrieve an account's virtual guest objects that are hosted on a user provisioned hypervisor.
</div>

<div class="method-row">

#### [getSubnetRegistrationDetails](/reference/services/SoftLayer_Account/getSubnetRegistrationDetails)

</div>

<div class="method-row">

#### [getSubnetRegistrations](/reference/services/SoftLayer_Account/getSubnetRegistrations)

</div>

<div class="method-row">

#### [getSubnets](/reference/services/SoftLayer_Account/getSubnets)
Retrieve all network subnets associated with an account.
</div>

<div class="method-row">

#### [getSupportRepresentatives](/reference/services/SoftLayer_Account/getSupportRepresentatives)
Retrieve the SoftLayer employees that an account is assigned to.
</div>

<div class="method-row">

#### [getSupportSubscriptions](/reference/services/SoftLayer_Account/getSupportSubscriptions)
Retrieve the active support subscriptions for this account.
</div>

<div class="method-row">

#### [getSupportTier](/reference/services/SoftLayer_Account/getSupportTier)

</div>

<div class="method-row">

#### [getSuppressInvoicesFlag](/reference/services/SoftLayer_Account/getSuppressInvoicesFlag)
Retrieve a flag indicating to suppress invoices.
</div>

<div class="method-row">

#### [getTags](/reference/services/SoftLayer_Account/getTags)

</div>

<div class="method-row">

#### [getTechIncubatorProgramInfo](/reference/services/SoftLayer_Account/getTechIncubatorProgramInfo)
This method retrieves the Technology Incubator Program information for your account. 
</div>

<div class="method-row">

#### [getThirdPartyPoliciesAcceptanceStatus](/reference/services/SoftLayer_Account/getThirdPartyPoliciesAcceptanceStatus)
Get the acceptance status of the applicable third-party policies.
</div>

<div class="method-row">

#### [getTickets](/reference/services/SoftLayer_Account/getTickets)
Retrieve an account's associated tickets.
</div>

<div class="method-row">

#### [getTicketsClosedInTheLastThreeDays](/reference/services/SoftLayer_Account/getTicketsClosedInTheLastThreeDays)
Retrieve tickets closed within the last 72 hours or last 10 tickets, whichever is less, associated with an account.
</div>

<div class="method-row">

#### [getTicketsClosedToday](/reference/services/SoftLayer_Account/getTicketsClosedToday)
Retrieve tickets closed today associated with an account.
</div>

<div class="method-row">

#### [getTranscodeAccounts](/reference/services/SoftLayer_Account/getTranscodeAccounts)
Retrieve an account's associated Transcode account.
</div>

<div class="method-row">

#### [getUpgradeRequests](/reference/services/SoftLayer_Account/getUpgradeRequests)
Retrieve an account's associated upgrade requests.
</div>

<div class="method-row">

#### [getUsers](/reference/services/SoftLayer_Account/getUsers)
Retrieve an account's portal users.
</div>

<div class="method-row">

#### [getValidSecurityCertificateEntries](/reference/services/SoftLayer_Account/getValidSecurityCertificateEntries)

</div>

<div class="method-row">

#### [getValidSecurityCertificates](/reference/services/SoftLayer_Account/getValidSecurityCertificates)
Retrieve stored security certificates that are not expired (ie. SSL)
</div>

<div class="method-row">

#### [getVdrUpdatesInProgressFlag](/reference/services/SoftLayer_Account/getVdrUpdatesInProgressFlag)
Retrieve return 0 if vpn updates are currently in progress on this account otherwise 1.
</div>

<div class="method-row">

#### [getVirtualDedicatedRacks](/reference/services/SoftLayer_Account/getVirtualDedicatedRacks)
Retrieve the bandwidth pooling for this account.
</div>

<div class="method-row">

#### [getVirtualDiskImages](/reference/services/SoftLayer_Account/getVirtualDiskImages)
Retrieve an account's associated virtual server virtual disk images.
</div>

<div class="method-row">

#### [getVirtualGuests](/reference/services/SoftLayer_Account/getVirtualGuests)
Retrieve an account's associated virtual guest objects.
</div>

<div class="method-row">

#### [getVirtualGuestsOverBandwidthAllocation](/reference/services/SoftLayer_Account/getVirtualGuestsOverBandwidthAllocation)
Retrieve an account's associated virtual guest objects currently over bandwidth allocation.
</div>

<div class="method-row">

#### [getVirtualGuestsProjectedOverBandwidthAllocation](/reference/services/SoftLayer_Account/getVirtualGuestsProjectedOverBandwidthAllocation)
Retrieve an account's associated virtual guest objects currently over bandwidth allocation.
</div>

<div class="method-row">

#### [getVirtualGuestsWithCpanel](/reference/services/SoftLayer_Account/getVirtualGuestsWithCpanel)
Retrieve all virtual guests associated with an account that has the cPanel web hosting control panel installed.
</div>

<div class="method-row">

#### [getVirtualGuestsWithMcafee](/reference/services/SoftLayer_Account/getVirtualGuestsWithMcafee)
Retrieve all virtual guests associated with an account that have McAfee Secure software components.
</div>

<div class="method-row">

#### [getVirtualGuestsWithMcafeeAntivirusRedhat](/reference/services/SoftLayer_Account/getVirtualGuestsWithMcafeeAntivirusRedhat)
Retrieve all virtual guests associated with an account that have McAfee Secure AntiVirus for Redhat software components.
</div>

<div class="method-row">

#### [getVirtualGuestsWithMcafeeAntivirusWindows](/reference/services/SoftLayer_Account/getVirtualGuestsWithMcafeeAntivirusWindows)
Retrieve all virtual guests associated with an account that has McAfee Secure AntiVirus for Windows software components.
</div>

<div class="method-row">

#### [getVirtualGuestsWithMcafeeIntrusionDetectionSystem](/reference/services/SoftLayer_Account/getVirtualGuestsWithMcafeeIntrusionDetectionSystem)
Retrieve all virtual guests associated with an account that has McAfee Secure Intrusion Detection System software components.
</div>

<div class="method-row">

#### [getVirtualGuestsWithPlesk](/reference/services/SoftLayer_Account/getVirtualGuestsWithPlesk)
Retrieve all virtual guests associated with an account that has the Plesk web hosting control panel installed.
</div>

<div class="method-row">

#### [getVirtualGuestsWithQuantastor](/reference/services/SoftLayer_Account/getVirtualGuestsWithQuantastor)
Retrieve all virtual guests associated with an account that have the QuantaStor storage system installed.
</div>

<div class="method-row">

#### [getVirtualGuestsWithUrchin](/reference/services/SoftLayer_Account/getVirtualGuestsWithUrchin)
Retrieve all virtual guests associated with an account that has the Urchin web traffic analytics package installed.
</div>

<div class="method-row">

#### [getVirtualPrivateRack](/reference/services/SoftLayer_Account/getVirtualPrivateRack)
Retrieve the bandwidth pooling for this account.
</div>

<div class="method-row">

#### [getVirtualStorageArchiveRepositories](/reference/services/SoftLayer_Account/getVirtualStorageArchiveRepositories)
Retrieve an account's associated virtual server archived storage repositories.
</div>

<div class="method-row">

#### [getVirtualStoragePublicRepositories](/reference/services/SoftLayer_Account/getVirtualStoragePublicRepositories)
Retrieve an account's associated virtual server public storage repositories.
</div>

<div class="method-row">

#### [getVmWareActiveAccountLicenseKeys](/reference/services/SoftLayer_Account/getVmWareActiveAccountLicenseKeys)
Get a collection of active VMware software account license keys.
</div>

<div class="method-row">

#### [getVpcVirtualGuests](/reference/services/SoftLayer_Account/getVpcVirtualGuests)
Retrieve an account's associated VPC configured virtual guest objects.
</div>

<div class="method-row">

#### [getVpnConfigRequiresVPNManageFlag](/reference/services/SoftLayer_Account/getVpnConfigRequiresVPNManageFlag)

</div>

<div class="method-row">

#### [getWindowsUpdateStatus](/reference/services/SoftLayer_Account/getWindowsUpdateStatus)
Retrieve a list of an account's hardware's Windows Update status.
</div>

<div class="method-row">

#### [hasAttribute](/reference/services/SoftLayer_Account/hasAttribute)
Determine if an account has a given attribute.
</div>

<div class="method-row">

#### [hourlyInstanceLimit](/reference/services/SoftLayer_Account/hourlyInstanceLimit)
Retrieve the number of hourly services that an account is allowed to have 
</div>

<div class="method-row">

#### [hourlyServerLimit](/reference/services/SoftLayer_Account/hourlyServerLimit)
Retrieve the number of hourly bare metal servers that an account is allowed to have 
</div>

<div class="method-row">

#### [isActiveVmwareCustomer](/reference/services/SoftLayer_Account/isActiveVmwareCustomer)
Determines if the account is considered an active VMware customer and as such eligible to order VMware restricted products. This result is cached for up to 60 seconds. 
</div>

<div class="method-row">

#### [isEligibleForLocalCurrencyProgram](/reference/services/SoftLayer_Account/isEligibleForLocalCurrencyProgram)

</div>

<div class="method-row">

#### [isEligibleToLinkWithPaas](/reference/services/SoftLayer_Account/isEligibleToLinkWithPaas)
Returns true if this account is eligible to link with PaaS. False otherwise. 
</div>

<div class="method-row">

#### [linkExternalAccount](/reference/services/SoftLayer_Account/linkExternalAccount)
This method will link this SoftLayer account with the provided external account. 
</div>

<div class="method-row">

#### [removeAlternateCreditCard](/reference/services/SoftLayer_Account/removeAlternateCreditCard)

</div>

<div class="method-row">

#### [requestCreditCardChange](/reference/services/SoftLayer_Account/requestCreditCardChange)
Retrieve the record data associated with the submission of a Credit Card Change Request.
</div>

<div class="method-row">

#### [requestManualPayment](/reference/services/SoftLayer_Account/requestManualPayment)
Retrieve the record data associated with the submission of a Manual Payment Request.
</div>

<div class="method-row">

#### [requestManualPaymentUsingCreditCardOnFile](/reference/services/SoftLayer_Account/requestManualPaymentUsingCreditCardOnFile)
Retrieve the record data associated with the submission of a Manual Payment Request which charges the manual payment to a credit card already on file. 
</div>

<div class="method-row">

#### [setAbuseEmails](/reference/services/SoftLayer_Account/setAbuseEmails)
Set this account's abuse emails.
</div>

<div class="method-row">

#### [setManagedPoolQuantity](/reference/services/SoftLayer_Account/setManagedPoolQuantity)
Set the number of desired servers in the pool
</div>

<div class="method-row">

#### [setVlanSpan](/reference/services/SoftLayer_Account/setVlanSpan)
Set the flag that enables or disables automatic private network VLAN spanning for a SoftLayer customer account.
</div>

<div class="method-row">

#### [swapCreditCards](/reference/services/SoftLayer_Account/swapCreditCards)

</div>

<div class="method-row">

#### [syncCurrentUserPopulationWithPaas](/reference/services/SoftLayer_Account/syncCurrentUserPopulationWithPaas)
This method manually starts a synchronize operation for the current IBMid-authenticated user population of a linked account pair. "Manually" means "independent of an account link operation". 
</div>

<div class="method-row">

#### [updateVpnUsersForResource](/reference/services/SoftLayer_Account/updateVpnUsersForResource)
[DEPRECATED] Creates or updates a user VPN access privileges for a server on account.
</div>

<div class="method-row">

#### [validate](/reference/services/SoftLayer_Account/validate)
Validates SoftLayer account information. Will return an error if any field is not valid.
</div>

<div class="method-row">

#### [validateManualPaymentAmount](/reference/services/SoftLayer_Account/validateManualPaymentAmount)
Ensure the amount requested for a manual payment is valid.
</div>
</div>

</div>

