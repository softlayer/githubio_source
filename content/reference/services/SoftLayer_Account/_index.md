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
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [activatePartner](/reference/services/SoftLayer_Account/activatePartner)
This service enables a partner account that has been created but is currently inactive. This restricted service is only available for certain accounts. Please contact support for questions. 

#### [addAchInformation](/reference/services/SoftLayer_Account/addAchInformation)


#### [addReferralPartnerPaymentOption](/reference/services/SoftLayer_Account/addReferralPartnerPaymentOption)


#### [areVdrUpdatesBlockedForBilling](/reference/services/SoftLayer_Account/areVdrUpdatesBlockedForBilling)
This method returns true if Bandwidth Pooling updates are blocked so billing can run for this account.

#### [cancelPayPalTransaction](/reference/services/SoftLayer_Account/cancelPayPalTransaction)
Cancel the PayPal Payment Request process.

#### [completePayPalTransaction](/reference/services/SoftLayer_Account/completePayPalTransaction)
Complete the PayPal Payment Request process and receive confirmation message.

#### [countHourlyInstances](/reference/services/SoftLayer_Account/countHourlyInstances)
Retrieve the number of hourly services on an account that are active, plus any pending orders with hourly services attached. 

#### [createUser](/reference/services/SoftLayer_Account/createUser)
Create a new user record, optionally skipping the IBMid email ("silently").

#### [disableEuSupport](/reference/services/SoftLayer_Account/disableEuSupport)
Turn off the EU Supported account flag.

#### [editAccount](/reference/services/SoftLayer_Account/editAccount)
Edit an account's information.

#### [enableEuSupport](/reference/services/SoftLayer_Account/enableEuSupport)
Turn on the EU Supported account flag.

#### [getAbuseEmail](/reference/services/SoftLayer_Account/getAbuseEmail)
Retrieve an email address that is responsible for abuse and legal inquiries on behalf of an account. For instance, new legal and abuse tickets are sent to this address.

#### [getAbuseEmails](/reference/services/SoftLayer_Account/getAbuseEmails)
Retrieve email addresses that are responsible for abuse and legal inquiries on behalf of an account. For instance, new legal and abuse tickets are sent to these addresses.

#### [getAccountBackupHistory](/reference/services/SoftLayer_Account/getAccountBackupHistory)
This method provides a history of account backups.

#### [getAccountContacts](/reference/services/SoftLayer_Account/getAccountContacts)
Retrieve the account contacts on an account.

#### [getAccountLicenses](/reference/services/SoftLayer_Account/getAccountLicenses)
Retrieve the account software licenses owned by an account

#### [getAccountLinks](/reference/services/SoftLayer_Account/getAccountLinks)


#### [getAccountStatus](/reference/services/SoftLayer_Account/getAccountStatus)
Retrieve an account's status presented in a more detailed data type.

#### [getAccountTraitValue](/reference/services/SoftLayer_Account/getAccountTraitValue)
Get the specific trait by its key

#### [getActiveAccountDiscountBillingItem](/reference/services/SoftLayer_Account/getActiveAccountDiscountBillingItem)
Retrieve the billing item associated with an account's monthly discount.

#### [getActiveAccountLicenses](/reference/services/SoftLayer_Account/getActiveAccountLicenses)
Retrieve the active account software licenses owned by an account

#### [getActiveAddresses](/reference/services/SoftLayer_Account/getActiveAddresses)
Retrieve the active address(es) that belong to an account.

#### [getActiveAgreements](/reference/services/SoftLayer_Account/getActiveAgreements)
Retrieve all active agreements for an account

#### [getActiveAlarms](/reference/services/SoftLayer_Account/getActiveAlarms)
Get all active alarms on this account.

#### [getActiveBillingAgreements](/reference/services/SoftLayer_Account/getActiveBillingAgreements)
Retrieve all billing agreements for an account

#### [getActiveCatalystEnrollment](/reference/services/SoftLayer_Account/getActiveCatalystEnrollment)


#### [getActiveColocationContainers](/reference/services/SoftLayer_Account/getActiveColocationContainers)
Retrieve the account's active top level colocation containers.

#### [getActiveFlexibleCreditEnrollment](/reference/services/SoftLayer_Account/getActiveFlexibleCreditEnrollment)
Retrieve [Deprecated] Please use SoftLayer_Account::activeFlexibleCreditEnrollments.

#### [getActiveFlexibleCreditEnrollments](/reference/services/SoftLayer_Account/getActiveFlexibleCreditEnrollments)


#### [getActiveNotificationSubscribers](/reference/services/SoftLayer_Account/getActiveNotificationSubscribers)


#### [getActiveOutletPackages](/reference/services/SoftLayer_Account/getActiveOutletPackages)
DEPRECATED. This method will return nothing.

#### [getActivePackages](/reference/services/SoftLayer_Account/getActivePackages)
Retrieve the active [SoftLayer_Product_Package]({{<ref "reference/datatypes/SoftLayer_Product_Package">}}) objects from which you can order a server, service or software. 

#### [getActivePackagesByAttribute](/reference/services/SoftLayer_Account/getActivePackagesByAttribute)
[<strong>DEPRECATED</strong>] Retrieve the active [SoftLayer_Product_Package]({{<ref "reference/datatypes/SoftLayer_Product_Package">}}) objects from which you can order a server, service or software filtered by an attribute type ([SoftLayer_Product_Package_Attribute_Type]({{<ref "reference/datatypes/SoftLayer_Product_Package_Attribute_Type">}})) on the package. 

#### [getActivePrivateHostedCloudPackages](/reference/services/SoftLayer_Account/getActivePrivateHostedCloudPackages)


#### [getActiveQuotes](/reference/services/SoftLayer_Account/getActiveQuotes)
Retrieve an account's non-expired quotes.

#### [getActiveReservedCapacityAgreements](/reference/services/SoftLayer_Account/getActiveReservedCapacityAgreements)
Retrieve active reserved capacity agreements for an account

#### [getActiveVirtualLicenses](/reference/services/SoftLayer_Account/getActiveVirtualLicenses)
Retrieve the virtual software licenses controlled by an account

#### [getAdcLoadBalancers](/reference/services/SoftLayer_Account/getAdcLoadBalancers)
Retrieve an account's associated load balancers.

#### [getAddresses](/reference/services/SoftLayer_Account/getAddresses)
Retrieve all the address(es) that belong to an account.

#### [getAffiliateId](/reference/services/SoftLayer_Account/getAffiliateId)
Retrieve an affiliate identifier associated with the customer account. 

#### [getAggregatedUptimeGraph](/reference/services/SoftLayer_Account/getAggregatedUptimeGraph)
Returns URL uptime data for your account

#### [getAllBillingItems](/reference/services/SoftLayer_Account/getAllBillingItems)
Retrieve the billing items that will be on an account's next invoice.

#### [getAllCommissionBillingItems](/reference/services/SoftLayer_Account/getAllCommissionBillingItems)
Retrieve the billing items that will be on an account's next invoice.

#### [getAllRecurringTopLevelBillingItems](/reference/services/SoftLayer_Account/getAllRecurringTopLevelBillingItems)
Retrieve the billing items that will be on an account's next invoice.

#### [getAllRecurringTopLevelBillingItemsUnfiltered](/reference/services/SoftLayer_Account/getAllRecurringTopLevelBillingItemsUnfiltered)
Retrieve the billing items that will be on an account's next invoice. Does not consider associated items.

#### [getAllSubnetBillingItems](/reference/services/SoftLayer_Account/getAllSubnetBillingItems)
Retrieve the billing items that will be on an account's next invoice.

#### [getAllTopLevelBillingItems](/reference/services/SoftLayer_Account/getAllTopLevelBillingItems)
Retrieve all billing items of an account.

#### [getAllTopLevelBillingItemsUnfiltered](/reference/services/SoftLayer_Account/getAllTopLevelBillingItemsUnfiltered)
Retrieve the billing items that will be on an account's next invoice. Does not consider associated items.

#### [getAllowIbmIdSilentMigrationFlag](/reference/services/SoftLayer_Account/getAllowIbmIdSilentMigrationFlag)
Retrieve indicates whether this account is allowed to silently migrate to use IBMid Authentication.

#### [getAllowsBluemixAccountLinkingFlag](/reference/services/SoftLayer_Account/getAllowsBluemixAccountLinkingFlag)
Retrieve flag indicating if this account can be linked with Bluemix.

#### [getAlternateCreditCardData](/reference/services/SoftLayer_Account/getAlternateCreditCardData)


#### [getApplicationDeliveryControllers](/reference/services/SoftLayer_Account/getApplicationDeliveryControllers)
Retrieve an account's associated application delivery controller records.

#### [getAttributeByType](/reference/services/SoftLayer_Account/getAttributeByType)
Retrieve an account attribute by type key name.

#### [getAttributes](/reference/services/SoftLayer_Account/getAttributes)
Retrieve the account attribute values for a SoftLayer customer account.

#### [getAuxiliaryNotifications](/reference/services/SoftLayer_Account/getAuxiliaryNotifications)


#### [getAvailablePublicNetworkVlans](/reference/services/SoftLayer_Account/getAvailablePublicNetworkVlans)
Retrieve the public network VLANs assigned to an account.

#### [getAverageArchiveUsageMetricDataByDate](/reference/services/SoftLayer_Account/getAverageArchiveUsageMetricDataByDate)
Returns the average disk usage for all archive repositories for the timeframe based on the parameters provided. 

#### [getAveragePublicUsageMetricDataByDate](/reference/services/SoftLayer_Account/getAveragePublicUsageMetricDataByDate)
Returns the average disk usage for all public repositories for the timeframe based on the parameters provided. 

#### [getBalance](/reference/services/SoftLayer_Account/getBalance)
Retrieve the account balance of a SoftLayer customer account. An account's balance is the amount of money owed to SoftLayer by the account holder, returned as a floating point number with two decimal places, measured in US Dollars ($USD). A negative account balance means the account holder has overpaid and is owed money by SoftLayer.

#### [getBandwidthAllotments](/reference/services/SoftLayer_Account/getBandwidthAllotments)
Retrieve the bandwidth allotments for an account.

#### [getBandwidthAllotmentsOverAllocation](/reference/services/SoftLayer_Account/getBandwidthAllotmentsOverAllocation)
Retrieve the bandwidth allotments for an account currently over allocation.

#### [getBandwidthAllotmentsProjectedOverAllocation](/reference/services/SoftLayer_Account/getBandwidthAllotmentsProjectedOverAllocation)
Retrieve the bandwidth allotments for an account projected to go over allocation.

#### [getBareMetalInstances](/reference/services/SoftLayer_Account/getBareMetalInstances)
Retrieve an account's associated bare metal server objects.

#### [getBillingAgreements](/reference/services/SoftLayer_Account/getBillingAgreements)
Retrieve all billing agreements for an account

#### [getBillingInfo](/reference/services/SoftLayer_Account/getBillingInfo)
Retrieve an account's billing information.

#### [getBlockDeviceTemplateGroups](/reference/services/SoftLayer_Account/getBlockDeviceTemplateGroups)
Retrieve private template group objects (parent and children) and the shared template group objects (parent only) for an account.

#### [getBluemixAccountLink](/reference/services/SoftLayer_Account/getBluemixAccountLink)
Retrieve the Bluemix account link associated with this SoftLayer account, if one exists.

#### [getBluemixLinkedFlag](/reference/services/SoftLayer_Account/getBluemixLinkedFlag)
Retrieve returns true if this account is linked to IBM Bluemix, false if not.

#### [getBrand](/reference/services/SoftLayer_Account/getBrand)


#### [getBrandAccountFlag](/reference/services/SoftLayer_Account/getBrandAccountFlag)


#### [getBrandKeyName](/reference/services/SoftLayer_Account/getBrandKeyName)
Retrieve the brand keyName.

#### [getBusinessPartner](/reference/services/SoftLayer_Account/getBusinessPartner)
Retrieve the Business Partner details for the account. Country Enterprise Code, Channel, Segment, Reseller Level.

#### [getCanOrderAdditionalVlansFlag](/reference/services/SoftLayer_Account/getCanOrderAdditionalVlansFlag)
Retrieve [DEPRECATED] All accounts may order VLANs.

#### [getCarts](/reference/services/SoftLayer_Account/getCarts)
Retrieve an account's active carts.

#### [getCatalystEnrollments](/reference/services/SoftLayer_Account/getCatalystEnrollments)


#### [getClosedTickets](/reference/services/SoftLayer_Account/getClosedTickets)
Retrieve all closed tickets associated with an account.

#### [getCurrentBackupStatisticsGraph](/reference/services/SoftLayer_Account/getCurrentBackupStatisticsGraph)
This method retrieves a pie chart for today's backup statistics.

#### [getCurrentTicketStatisticsGraph](/reference/services/SoftLayer_Account/getCurrentTicketStatisticsGraph)
(Deprecated)

#### [getCurrentUser](/reference/services/SoftLayer_Account/getCurrentUser)
Retrieve the current API user's record.

#### [getDatacentersWithSubnetAllocations](/reference/services/SoftLayer_Account/getDatacentersWithSubnetAllocations)
Retrieve datacenters which contain subnets that the account has access to route.

#### [getDedicatedHosts](/reference/services/SoftLayer_Account/getDedicatedHosts)
Retrieve an account's associated virtual dedicated host objects.

#### [getDedicatedHostsForImageTemplate](/reference/services/SoftLayer_Account/getDedicatedHostsForImageTemplate)
Get a collection of dedicated hosts that are valid for a given image template. 

#### [getDisablePaymentProcessingFlag](/reference/services/SoftLayer_Account/getDisablePaymentProcessingFlag)
Retrieve a flag indicating whether payments are processed for this account.

#### [getDiskUsageMetricDataByDate](/reference/services/SoftLayer_Account/getDiskUsageMetricDataByDate)
Retrieve the metric data for disk space usage for a storage repository from the Metric Tracking Object System and the Legacy Data Warehouse. 

#### [getDiskUsageMetricDataFromLegacyByDate](/reference/services/SoftLayer_Account/getDiskUsageMetricDataFromLegacyByDate)
Retrieve the metric data for disk space usage for a storage repository from the Legacy Data Warehouse. 

#### [getDiskUsageMetricDataFromMetricTrackingObjectSystemByDate](/reference/services/SoftLayer_Account/getDiskUsageMetricDataFromMetricTrackingObjectSystemByDate)
Retrieve the metric data for disk space usage for a storage repository from the Metric Tracking Object System. 

#### [getDiskUsageMetricImageByDate](/reference/services/SoftLayer_Account/getDiskUsageMetricImageByDate)
Retrieve an image of the disk usage data on a [SoftLayer_Virtual_Guest]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest">}}) image for the time range you provide. 

#### [getDisplaySupportRepresentativeAssignments](/reference/services/SoftLayer_Account/getDisplaySupportRepresentativeAssignments)
Retrieve the SoftLayer employees that an account is assigned to.

#### [getDomainRegistrations](/reference/services/SoftLayer_Account/getDomainRegistrations)


#### [getDomains](/reference/services/SoftLayer_Account/getDomains)
Retrieve the DNS domains associated with an account.

#### [getDomainsWithoutSecondaryDnsRecords](/reference/services/SoftLayer_Account/getDomainsWithoutSecondaryDnsRecords)
Retrieve the DNS domains associated with an account that were not created as a result of a secondary DNS zone transfer.

#### [getEuSupportedFlag](/reference/services/SoftLayer_Account/getEuSupportedFlag)
Retrieve boolean flag dictating whether or not this account has the EU Supported flag. This flag indicates that this account uses IBM Cloud services to process EU citizen's personal data.

#### [getEvaultCapacityGB](/reference/services/SoftLayer_Account/getEvaultCapacityGB)
Retrieve the total capacity of Legacy EVault Volumes on an account, in GB.

#### [getEvaultMasterUsers](/reference/services/SoftLayer_Account/getEvaultMasterUsers)
Retrieve an account's master EVault user. This is only used when an account has EVault service.

#### [getEvaultNetworkStorage](/reference/services/SoftLayer_Account/getEvaultNetworkStorage)
Retrieve an account's associated EVault storage volumes.

#### [getExecutiveSummaryPdf](/reference/services/SoftLayer_Account/getExecutiveSummaryPdf)
This method provides an executive summary PDF for managed hosting services. 

#### [getExpiredSecurityCertificates](/reference/services/SoftLayer_Account/getExpiredSecurityCertificates)
Retrieve stored security certificates that are expired (ie. SSL)

#### [getFacilityLogs](/reference/services/SoftLayer_Account/getFacilityLogs)
Retrieve logs of who entered a colocation area which is assigned to this account, or when a user under this account enters a datacenter.

#### [getFileBlockBetaAccessFlag](/reference/services/SoftLayer_Account/getFileBlockBetaAccessFlag)


#### [getFlexibleCreditEnrollments](/reference/services/SoftLayer_Account/getFlexibleCreditEnrollments)
Retrieve all of the account's current and former Flexible Credit enrollments.

#### [getFlexibleCreditProgramInfo](/reference/services/SoftLayer_Account/getFlexibleCreditProgramInfo)
[DEPRECATED] Please use SoftLayer_Account::getFlexibleCreditProgramsInfo. This is no longer an accurate representation of discounts. 

#### [getFlexibleCreditProgramsInfo](/reference/services/SoftLayer_Account/getFlexibleCreditProgramsInfo)
This method retrieves information on all of your Flexible Credit Program enrollments for your account. 

#### [getForcePaasAccountLinkDate](/reference/services/SoftLayer_Account/getForcePaasAccountLinkDate)
Retrieve timestamp representing the point in time when an account is required to link with PaaS.

#### [getGlobalIpRecords](/reference/services/SoftLayer_Account/getGlobalIpRecords)


#### [getGlobalIpv4Records](/reference/services/SoftLayer_Account/getGlobalIpv4Records)


#### [getGlobalIpv6Records](/reference/services/SoftLayer_Account/getGlobalIpv6Records)


#### [getGlobalLoadBalancerAccounts](/reference/services/SoftLayer_Account/getGlobalLoadBalancerAccounts)
Retrieve the global load balancer accounts for a softlayer customer account.

#### [getHardware](/reference/services/SoftLayer_Account/getHardware)
Retrieve an account's associated hardware objects.

#### [getHardwareOverBandwidthAllocation](/reference/services/SoftLayer_Account/getHardwareOverBandwidthAllocation)
Retrieve an account's associated hardware objects currently over bandwidth allocation.

#### [getHardwarePools](/reference/services/SoftLayer_Account/getHardwarePools)
Get a collection of managed hardware pools.

#### [getHardwareProjectedOverBandwidthAllocation](/reference/services/SoftLayer_Account/getHardwareProjectedOverBandwidthAllocation)
Retrieve an account's associated hardware objects projected to go over bandwidth allocation.

#### [getHardwareWithCpanel](/reference/services/SoftLayer_Account/getHardwareWithCpanel)
Retrieve all hardware associated with an account that has the cPanel web hosting control panel installed.

#### [getHardwareWithHelm](/reference/services/SoftLayer_Account/getHardwareWithHelm)
Retrieve all hardware associated with an account that has the Helm web hosting control panel installed.

#### [getHardwareWithMcafee](/reference/services/SoftLayer_Account/getHardwareWithMcafee)
Retrieve all hardware associated with an account that has McAfee Secure software components.

#### [getHardwareWithMcafeeAntivirusRedhat](/reference/services/SoftLayer_Account/getHardwareWithMcafeeAntivirusRedhat)
Retrieve all hardware associated with an account that has McAfee Secure AntiVirus for Redhat software components.

#### [getHardwareWithMcafeeAntivirusWindows](/reference/services/SoftLayer_Account/getHardwareWithMcafeeAntivirusWindows)
Retrieve all hardware associated with an account that has McAfee Secure AntiVirus for Windows software components.

#### [getHardwareWithMcafeeIntrusionDetectionSystem](/reference/services/SoftLayer_Account/getHardwareWithMcafeeIntrusionDetectionSystem)
Retrieve all hardware associated with an account that has McAfee Secure Intrusion Detection System software components.

#### [getHardwareWithPlesk](/reference/services/SoftLayer_Account/getHardwareWithPlesk)
Retrieve all hardware associated with an account that has the Plesk web hosting control panel installed.

#### [getHardwareWithQuantastor](/reference/services/SoftLayer_Account/getHardwareWithQuantastor)
Retrieve all hardware associated with an account that has the QuantaStor storage system installed.

#### [getHardwareWithUrchin](/reference/services/SoftLayer_Account/getHardwareWithUrchin)
Retrieve all hardware associated with an account that has the Urchin web traffic analytics package installed.

#### [getHardwareWithWindows](/reference/services/SoftLayer_Account/getHardwareWithWindows)
Retrieve all hardware associated with an account that is running a version of the Microsoft Windows operating system.

#### [getHasEvaultBareMetalRestorePluginFlag](/reference/services/SoftLayer_Account/getHasEvaultBareMetalRestorePluginFlag)
Retrieve return 1 if one of the account's hardware has the EVault Bare Metal Server Restore Plugin otherwise 0.

#### [getHasIderaBareMetalRestorePluginFlag](/reference/services/SoftLayer_Account/getHasIderaBareMetalRestorePluginFlag)
Retrieve return 1 if one of the account's hardware has an installation of Idera Server Backup otherwise 0.

#### [getHasPendingOrder](/reference/services/SoftLayer_Account/getHasPendingOrder)
Retrieve the number of orders in a PENDING status for a SoftLayer customer account.

#### [getHasR1softBareMetalRestorePluginFlag](/reference/services/SoftLayer_Account/getHasR1softBareMetalRestorePluginFlag)
Retrieve return 1 if one of the account's hardware has an installation of R1Soft CDP otherwise 0.

#### [getHistoricalBackupGraph](/reference/services/SoftLayer_Account/getHistoricalBackupGraph)


#### [getHistoricalBandwidthGraph](/reference/services/SoftLayer_Account/getHistoricalBandwidthGraph)
This method returns a line graph of bandwidth statistics.

#### [getHistoricalTicketGraph](/reference/services/SoftLayer_Account/getHistoricalTicketGraph)
This method returns a pie chart of ticket statistics for the given dates.

#### [getHistoricalUptimeGraph](/reference/services/SoftLayer_Account/getHistoricalUptimeGraph)
This method returns a SoftLayer_Container_Account_Graph_Outputs object for the specified date range. 

#### [getHourlyBareMetalInstances](/reference/services/SoftLayer_Account/getHourlyBareMetalInstances)
Retrieve an account's associated hourly bare metal server objects.

#### [getHourlyServiceBillingItems](/reference/services/SoftLayer_Account/getHourlyServiceBillingItems)
Retrieve hourly service billing items that will be on an account's next invoice.

#### [getHourlyVirtualGuests](/reference/services/SoftLayer_Account/getHourlyVirtualGuests)
Retrieve an account's associated hourly virtual guest objects.

#### [getHubNetworkStorage](/reference/services/SoftLayer_Account/getHubNetworkStorage)
Retrieve an account's associated Virtual Storage volumes.

#### [getIbmCustomerNumber](/reference/services/SoftLayer_Account/getIbmCustomerNumber)
Retrieve unique identifier for a customer used throughout IBM.

#### [getIbmIdAuthenticationRequiredFlag](/reference/services/SoftLayer_Account/getIbmIdAuthenticationRequiredFlag)
Retrieve indicates whether this account requires IBMid authentication.

#### [getIbmIdMigrationExpirationTimestamp](/reference/services/SoftLayer_Account/getIbmIdMigrationExpirationTimestamp)
Retrieve this key is deprecated and should not be used.

#### [getInProgressExternalAccountSetup](/reference/services/SoftLayer_Account/getInProgressExternalAccountSetup)
Retrieve an in progress request to switch billing systems.

#### [getInternalNotes](/reference/services/SoftLayer_Account/getInternalNotes)


#### [getInvoices](/reference/services/SoftLayer_Account/getInvoices)
Retrieve an account's associated billing invoices.

#### [getIpAddresses](/reference/services/SoftLayer_Account/getIpAddresses)


#### [getIscsiIsolationDisabled](/reference/services/SoftLayer_Account/getIscsiIsolationDisabled)


#### [getIscsiNetworkStorage](/reference/services/SoftLayer_Account/getIscsiNetworkStorage)
Retrieve an account's associated iSCSI storage volumes.

#### [getLargestAllowedSubnetCidr](/reference/services/SoftLayer_Account/getLargestAllowedSubnetCidr)
Computes the number of available public secondary IP addresses, augmented by the provided number of hosts, before overflow of the allowed host to IP address ratio occurs. The result is aligned to the nearest subnet size that could be accommodated in full. 

0 is returned if an overflow is detected. 

The use of $locationId has been deprecated. 

#### [getLastCanceledBillingItem](/reference/services/SoftLayer_Account/getLastCanceledBillingItem)
Retrieve the most recently canceled billing item.

#### [getLastCancelledServerBillingItem](/reference/services/SoftLayer_Account/getLastCancelledServerBillingItem)
Retrieve the most recent cancelled server billing item.

#### [getLastFiveClosedAbuseTickets](/reference/services/SoftLayer_Account/getLastFiveClosedAbuseTickets)
Retrieve the five most recently closed abuse tickets associated with an account.

#### [getLastFiveClosedAccountingTickets](/reference/services/SoftLayer_Account/getLastFiveClosedAccountingTickets)
Retrieve the five most recently closed accounting tickets associated with an account.

#### [getLastFiveClosedOtherTickets](/reference/services/SoftLayer_Account/getLastFiveClosedOtherTickets)
Retrieve the five most recently closed tickets that do not belong to the abuse, accounting, sales, or support groups associated with an account.

#### [getLastFiveClosedSalesTickets](/reference/services/SoftLayer_Account/getLastFiveClosedSalesTickets)
Retrieve the five most recently closed sales tickets associated with an account.

#### [getLastFiveClosedSupportTickets](/reference/services/SoftLayer_Account/getLastFiveClosedSupportTickets)
Retrieve the five most recently closed support tickets associated with an account.

#### [getLastFiveClosedTickets](/reference/services/SoftLayer_Account/getLastFiveClosedTickets)
Retrieve the five most recently closed tickets associated with an account.

#### [getLatestBillDate](/reference/services/SoftLayer_Account/getLatestBillDate)
Retrieve an account's most recent billing date.

#### [getLatestRecurringInvoice](/reference/services/SoftLayer_Account/getLatestRecurringInvoice)
Retrieve an account's latest recurring invoice.

#### [getLatestRecurringPendingInvoice](/reference/services/SoftLayer_Account/getLatestRecurringPendingInvoice)
Retrieve an account's latest recurring pending invoice.

#### [getLegacyBandwidthAllotments](/reference/services/SoftLayer_Account/getLegacyBandwidthAllotments)
Retrieve the legacy bandwidth allotments for an account.

#### [getLegacyIscsiCapacityGB](/reference/services/SoftLayer_Account/getLegacyIscsiCapacityGB)
Retrieve the total capacity of Legacy iSCSI Volumes on an account, in GB.

#### [getLoadBalancers](/reference/services/SoftLayer_Account/getLoadBalancers)
Retrieve an account's associated load balancers.

#### [getLockboxCapacityGB](/reference/services/SoftLayer_Account/getLockboxCapacityGB)
Retrieve the total capacity of Legacy lockbox Volumes on an account, in GB.

#### [getLockboxNetworkStorage](/reference/services/SoftLayer_Account/getLockboxNetworkStorage)
Retrieve an account's associated Lockbox storage volumes.

#### [getManualPaymentsUnderReview](/reference/services/SoftLayer_Account/getManualPaymentsUnderReview)


#### [getMasterUser](/reference/services/SoftLayer_Account/getMasterUser)
Retrieve an account's master user.

#### [getMediaDataTransferRequests](/reference/services/SoftLayer_Account/getMediaDataTransferRequests)
Retrieve an account's media transfer service requests.

#### [getMigratedToIbmCloudPortalFlag](/reference/services/SoftLayer_Account/getMigratedToIbmCloudPortalFlag)
Retrieve flag indicating whether this account is restricted to the IBM Cloud portal.

#### [getMonthlyBareMetalInstances](/reference/services/SoftLayer_Account/getMonthlyBareMetalInstances)
Retrieve an account's associated monthly bare metal server objects.

#### [getMonthlyVirtualGuests](/reference/services/SoftLayer_Account/getMonthlyVirtualGuests)
Retrieve an account's associated monthly virtual guest objects.

#### [getNasNetworkStorage](/reference/services/SoftLayer_Account/getNasNetworkStorage)
Retrieve an account's associated NAS storage volumes.

#### [getNetAppActiveAccountLicenseKeys](/reference/services/SoftLayer_Account/getNetAppActiveAccountLicenseKeys)
Get a collection of active NetApp software account license keys.

#### [getNetworkCreationFlag](/reference/services/SoftLayer_Account/getNetworkCreationFlag)
Retrieve whether or not this account can define their own networks.

#### [getNetworkGateways](/reference/services/SoftLayer_Account/getNetworkGateways)
Retrieve all network gateway devices on this account.

#### [getNetworkHardware](/reference/services/SoftLayer_Account/getNetworkHardware)
Retrieve an account's associated network hardware.

#### [getNetworkMessageDeliveryAccounts](/reference/services/SoftLayer_Account/getNetworkMessageDeliveryAccounts)


#### [getNetworkMonitorDownHardware](/reference/services/SoftLayer_Account/getNetworkMonitorDownHardware)
Retrieve hardware which is currently experiencing a service failure.

#### [getNetworkMonitorDownVirtualGuests](/reference/services/SoftLayer_Account/getNetworkMonitorDownVirtualGuests)
Retrieve virtual guest which is currently experiencing a service failure.

#### [getNetworkMonitorRecoveringHardware](/reference/services/SoftLayer_Account/getNetworkMonitorRecoveringHardware)
Retrieve hardware which is currently recovering from a service failure.

#### [getNetworkMonitorRecoveringVirtualGuests](/reference/services/SoftLayer_Account/getNetworkMonitorRecoveringVirtualGuests)
Retrieve virtual guest which is currently recovering from a service failure.

#### [getNetworkMonitorUpHardware](/reference/services/SoftLayer_Account/getNetworkMonitorUpHardware)
Retrieve hardware which is currently online.

#### [getNetworkMonitorUpVirtualGuests](/reference/services/SoftLayer_Account/getNetworkMonitorUpVirtualGuests)
Retrieve virtual guest which is currently online.

#### [getNetworkStorage](/reference/services/SoftLayer_Account/getNetworkStorage)
Retrieve an account's associated storage volumes. This includes Lockbox, NAS, EVault, and iSCSI volumes.

#### [getNetworkStorageGroups](/reference/services/SoftLayer_Account/getNetworkStorageGroups)
Retrieve an account's Network Storage groups.

#### [getNetworkTunnelContexts](/reference/services/SoftLayer_Account/getNetworkTunnelContexts)
Retrieve iPSec network tunnels for an account.

#### [getNetworkVlanSpan](/reference/services/SoftLayer_Account/getNetworkVlanSpan)
Retrieve whether or not an account has automatic private VLAN spanning enabled.

#### [getNetworkVlans](/reference/services/SoftLayer_Account/getNetworkVlans)
Retrieve all network VLANs assigned to an account.

#### [getNextBillingPublicAllotmentHardwareBandwidthDetails](/reference/services/SoftLayer_Account/getNextBillingPublicAllotmentHardwareBandwidthDetails)
Retrieval: DEPRECATED - This information can be pulled directly through tapping keys now - DEPRECATED. The allotments for this account and their servers for the next billing cycle. The public inbound and outbound bandwidth is calculated for each server in addition to the daily average network traffic since the last billing date.

#### [getNextInvoiceExcel](/reference/services/SoftLayer_Account/getNextInvoiceExcel)
Retrieve the next billing period's invoice. Note, this should be considered preliminary as you may add, remove, change billing items on your account.

#### [getNextInvoiceIncubatorExemptTotal](/reference/services/SoftLayer_Account/getNextInvoiceIncubatorExemptTotal)
Retrieve the pre-tax total amount exempt from incubator credit for the account's next invoice. This field is now deprecated and will soon be removed. Please update all references to instead use nextInvoiceTotalAmount

#### [getNextInvoicePdf](/reference/services/SoftLayer_Account/getNextInvoicePdf)
Retrieve the next billing period's invoice. Note, this should be considered preliminary as you may add, remove, change billing items on your account.

#### [getNextInvoicePdfDetailed](/reference/services/SoftLayer_Account/getNextInvoicePdfDetailed)
Retrieve the next billing period's detailed invoice. Note, this should be considered preliminary as you may add, remove, change billing items on your account.

#### [getNextInvoiceRecurringAmountEligibleForAccountDiscount](/reference/services/SoftLayer_Account/getNextInvoiceRecurringAmountEligibleForAccountDiscount)
Retrieve the total recurring charge amount of an account's next invoice eligible for account discount measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.

#### [getNextInvoiceTopLevelBillingItems](/reference/services/SoftLayer_Account/getNextInvoiceTopLevelBillingItems)
Retrieve the billing items that will be on an account's next invoice.

#### [getNextInvoiceTotalAmount](/reference/services/SoftLayer_Account/getNextInvoiceTotalAmount)
Retrieve the pre-tax total amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.

#### [getNextInvoiceTotalOneTimeAmount](/reference/services/SoftLayer_Account/getNextInvoiceTotalOneTimeAmount)
Retrieve the total one-time charge amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.

#### [getNextInvoiceTotalOneTimeTaxAmount](/reference/services/SoftLayer_Account/getNextInvoiceTotalOneTimeTaxAmount)
Retrieve the total one-time tax amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.

#### [getNextInvoiceTotalRecurringAmount](/reference/services/SoftLayer_Account/getNextInvoiceTotalRecurringAmount)
Retrieve the total recurring charge amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.

#### [getNextInvoiceTotalRecurringAmountBeforeAccountDiscount](/reference/services/SoftLayer_Account/getNextInvoiceTotalRecurringAmountBeforeAccountDiscount)
Retrieve the total recurring charge amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.

#### [getNextInvoiceTotalRecurringTaxAmount](/reference/services/SoftLayer_Account/getNextInvoiceTotalRecurringTaxAmount)
Retrieve the total recurring tax amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.

#### [getNextInvoiceTotalTaxableRecurringAmount](/reference/services/SoftLayer_Account/getNextInvoiceTotalTaxableRecurringAmount)
Retrieve the total recurring charge amount of an account's next invoice measured in US Dollars ($USD), assuming no changes or charges occur between now and time of billing.

#### [getNextInvoiceZeroFeeItemCounts](/reference/services/SoftLayer_Account/getNextInvoiceZeroFeeItemCounts)


#### [getNotificationSubscribers](/reference/services/SoftLayer_Account/getNotificationSubscribers)


#### [getObject](/reference/services/SoftLayer_Account/getObject)
Retrieve a SoftLayer_Account record.

#### [getOpenAbuseTickets](/reference/services/SoftLayer_Account/getOpenAbuseTickets)
Retrieve the open abuse tickets associated with an account.

#### [getOpenAccountingTickets](/reference/services/SoftLayer_Account/getOpenAccountingTickets)
Retrieve the open accounting tickets associated with an account.

#### [getOpenBillingTickets](/reference/services/SoftLayer_Account/getOpenBillingTickets)
Retrieve the open billing tickets associated with an account.

#### [getOpenCancellationRequests](/reference/services/SoftLayer_Account/getOpenCancellationRequests)
Retrieve an open ticket requesting cancellation of this server, if one exists.

#### [getOpenOtherTickets](/reference/services/SoftLayer_Account/getOpenOtherTickets)
Retrieve the open tickets that do not belong to the abuse, accounting, sales, or support groups associated with an account.

#### [getOpenRecurringInvoices](/reference/services/SoftLayer_Account/getOpenRecurringInvoices)
Retrieve an account's recurring invoices.

#### [getOpenSalesTickets](/reference/services/SoftLayer_Account/getOpenSalesTickets)
Retrieve the open sales tickets associated with an account.

#### [getOpenStackAccountLinks](/reference/services/SoftLayer_Account/getOpenStackAccountLinks)


#### [getOpenStackObjectStorage](/reference/services/SoftLayer_Account/getOpenStackObjectStorage)
Retrieve an account's associated Openstack related Object Storage accounts.

#### [getOpenSupportTickets](/reference/services/SoftLayer_Account/getOpenSupportTickets)
Retrieve the open support tickets associated with an account.

#### [getOpenTickets](/reference/services/SoftLayer_Account/getOpenTickets)
Retrieve all open tickets associated with an account.

#### [getOpenTicketsWaitingOnCustomer](/reference/services/SoftLayer_Account/getOpenTicketsWaitingOnCustomer)
Retrieve all open tickets associated with an account last edited by an employee.

#### [getOrders](/reference/services/SoftLayer_Account/getOrders)
Retrieve an account's associated billing orders excluding upgrades.

#### [getOrphanBillingItems](/reference/services/SoftLayer_Account/getOrphanBillingItems)
Retrieve the billing items that have no parent billing item. These are items that don't necessarily belong to a single server.

#### [getOwnedBrands](/reference/services/SoftLayer_Account/getOwnedBrands)


#### [getOwnedHardwareGenericComponentModels](/reference/services/SoftLayer_Account/getOwnedHardwareGenericComponentModels)


#### [getPaymentProcessors](/reference/services/SoftLayer_Account/getPaymentProcessors)


#### [getPendingCreditCardChangeRequestData](/reference/services/SoftLayer_Account/getPendingCreditCardChangeRequestData)
Retrieve details of all credit card change requests which have not been processed by a SoftLayer agent.

#### [getPendingEvents](/reference/services/SoftLayer_Account/getPendingEvents)


#### [getPendingInvoice](/reference/services/SoftLayer_Account/getPendingInvoice)
Retrieve an account's latest open (pending) invoice.

#### [getPendingInvoiceTopLevelItems](/reference/services/SoftLayer_Account/getPendingInvoiceTopLevelItems)
Retrieve a list of top-level invoice items that are on an account's currently pending invoice.

#### [getPendingInvoiceTotalAmount](/reference/services/SoftLayer_Account/getPendingInvoiceTotalAmount)
Retrieve the total amount of an account's pending invoice, if one exists.

#### [getPendingInvoiceTotalOneTimeAmount](/reference/services/SoftLayer_Account/getPendingInvoiceTotalOneTimeAmount)
Retrieve the total one-time charges for an account's pending invoice, if one exists. In other words, it is the sum of one-time charges, setup fees, and labor fees. It does not include taxes.

#### [getPendingInvoiceTotalOneTimeTaxAmount](/reference/services/SoftLayer_Account/getPendingInvoiceTotalOneTimeTaxAmount)
Retrieve the sum of all the taxes related to one time charges for an account's pending invoice, if one exists.

#### [getPendingInvoiceTotalRecurringAmount](/reference/services/SoftLayer_Account/getPendingInvoiceTotalRecurringAmount)
Retrieve the total recurring amount of an account's pending invoice, if one exists.

#### [getPendingInvoiceTotalRecurringTaxAmount](/reference/services/SoftLayer_Account/getPendingInvoiceTotalRecurringTaxAmount)
Retrieve the total amount of the recurring taxes on an account's pending invoice, if one exists.

#### [getPermissionGroups](/reference/services/SoftLayer_Account/getPermissionGroups)
Retrieve an account's permission groups.

#### [getPermissionRoles](/reference/services/SoftLayer_Account/getPermissionRoles)
Retrieve an account's user roles.

#### [getPlacementGroups](/reference/services/SoftLayer_Account/getPlacementGroups)
Retrieve an account's associated virtual placement groups.

#### [getPortableStorageVolumes](/reference/services/SoftLayer_Account/getPortableStorageVolumes)


#### [getPostProvisioningHooks](/reference/services/SoftLayer_Account/getPostProvisioningHooks)
Retrieve customer specified URIs that are downloaded onto a newly provisioned or reloaded server. If the URI is sent over https it will be executed directly on the server.

#### [getPptpVpnAllowedFlag](/reference/services/SoftLayer_Account/getPptpVpnAllowedFlag)
Retrieve boolean flag dictating whether or not this account supports PPTP VPN Access.

#### [getPptpVpnUsers](/reference/services/SoftLayer_Account/getPptpVpnUsers)
Retrieve an account's associated portal users with PPTP VPN access. (Deprecated)

#### [getPreviousRecurringRevenue](/reference/services/SoftLayer_Account/getPreviousRecurringRevenue)
Retrieve the total recurring amount for an accounts previous revenue.

#### [getPriceRestrictions](/reference/services/SoftLayer_Account/getPriceRestrictions)
Retrieve the item price that an account is restricted to.

#### [getPriorityOneTickets](/reference/services/SoftLayer_Account/getPriorityOneTickets)
Retrieve all priority one tickets associated with an account.

#### [getPrivateAllotmentHardwareBandwidthDetails](/reference/services/SoftLayer_Account/getPrivateAllotmentHardwareBandwidthDetails)
Retrieval: DEPRECATED - This information can be pulled directly through tapping keys now - DEPRECATED. The allotments for this account and their servers. The private inbound and outbound bandwidth is calculated for each server in addition to the daily average network traffic since the last billing date.

#### [getPrivateBlockDeviceTemplateGroups](/reference/services/SoftLayer_Account/getPrivateBlockDeviceTemplateGroups)
Retrieve private and shared template group objects (parent only) for an account.

#### [getPrivateIpAddresses](/reference/services/SoftLayer_Account/getPrivateIpAddresses)


#### [getPrivateNetworkVlans](/reference/services/SoftLayer_Account/getPrivateNetworkVlans)
Retrieve the private network VLANs assigned to an account.

#### [getPrivateSubnets](/reference/services/SoftLayer_Account/getPrivateSubnets)
Retrieve all private subnets associated with an account.

#### [getProofOfConceptAccountFlag](/reference/services/SoftLayer_Account/getProofOfConceptAccountFlag)
Retrieve boolean flag indicating whether or not this account is a Proof of Concept account.

#### [getPublicAllotmentHardwareBandwidthDetails](/reference/services/SoftLayer_Account/getPublicAllotmentHardwareBandwidthDetails)
Retrieval: DEPRECATED - This information can be pulled directly through tapping keys now - DEPRECATED. The allotments for this account and their servers. The public inbound and outbound bandwidth is calculated for each server in addition to the daily average network traffic since the last billing date.

#### [getPublicIpAddresses](/reference/services/SoftLayer_Account/getPublicIpAddresses)


#### [getPublicNetworkVlans](/reference/services/SoftLayer_Account/getPublicNetworkVlans)
Retrieve the public network VLANs assigned to an account.

#### [getPublicSubnets](/reference/services/SoftLayer_Account/getPublicSubnets)
Retrieve all public network subnets associated with an account.

#### [getQuotes](/reference/services/SoftLayer_Account/getQuotes)
Retrieve an account's quotes.

#### [getRecentEvents](/reference/services/SoftLayer_Account/getRecentEvents)


#### [getReferralPartner](/reference/services/SoftLayer_Account/getReferralPartner)
Retrieve the Referral Partner for this account, if any.

#### [getReferralPartnerCommissionForecast](/reference/services/SoftLayer_Account/getReferralPartnerCommissionForecast)


#### [getReferralPartnerCommissionHistory](/reference/services/SoftLayer_Account/getReferralPartnerCommissionHistory)


#### [getReferralPartnerCommissionPending](/reference/services/SoftLayer_Account/getReferralPartnerCommissionPending)


#### [getReferredAccounts](/reference/services/SoftLayer_Account/getReferredAccounts)
Retrieve if this is a account is a referral partner, the accounts this referral partner has referred

#### [getRegulatedWorkloads](/reference/services/SoftLayer_Account/getRegulatedWorkloads)


#### [getRemoteManagementCommandRequests](/reference/services/SoftLayer_Account/getRemoteManagementCommandRequests)
Retrieve remote management command requests for an account

#### [getReplicationEvents](/reference/services/SoftLayer_Account/getReplicationEvents)
Retrieve the Replication events for all Network Storage volumes on an account.

#### [getRequireSilentIBMidUserCreation](/reference/services/SoftLayer_Account/getRequireSilentIBMidUserCreation)
Retrieve indicates whether newly created users under this account will be associated with IBMid via an email requiring a response, or not.

#### [getReservedCapacityAgreements](/reference/services/SoftLayer_Account/getReservedCapacityAgreements)
Retrieve all reserved capacity agreements for an account

#### [getReservedCapacityGroups](/reference/services/SoftLayer_Account/getReservedCapacityGroups)
Retrieve the reserved capacity groups owned by this account.

#### [getResourceGroups](/reference/services/SoftLayer_Account/getResourceGroups)
Retrieve an account's associated top-level resource groups.

#### [getRouters](/reference/services/SoftLayer_Account/getRouters)
Retrieve all Routers that an accounts VLANs reside on

#### [getRwhoisData](/reference/services/SoftLayer_Account/getRwhoisData)
Retrieve an account's reverse WHOIS data. This data is used when making SWIP requests.

#### [getSamlAuthentication](/reference/services/SoftLayer_Account/getSamlAuthentication)
Retrieve the SAML configuration for this account.

#### [getScaleGroups](/reference/services/SoftLayer_Account/getScaleGroups)
Retrieve all scale groups on this account.

#### [getSecondaryDomains](/reference/services/SoftLayer_Account/getSecondaryDomains)
Retrieve the secondary DNS records for a SoftLayer customer account.

#### [getSecurityCertificates](/reference/services/SoftLayer_Account/getSecurityCertificates)
Retrieve stored security certificates (ie. SSL)

#### [getSecurityGroups](/reference/services/SoftLayer_Account/getSecurityGroups)
Retrieve the security groups belonging to this account.

#### [getSecurityLevel](/reference/services/SoftLayer_Account/getSecurityLevel)


#### [getSecurityScanRequests](/reference/services/SoftLayer_Account/getSecurityScanRequests)
Retrieve an account's vulnerability scan requests.

#### [getServiceBillingItems](/reference/services/SoftLayer_Account/getServiceBillingItems)
Retrieve the service billing items that will be on an account's next invoice. 

#### [getSharedBlockDeviceTemplateGroups](/reference/services/SoftLayer_Account/getSharedBlockDeviceTemplateGroups)
Get the collection of template group objects that have been shared with this account.

#### [getShipments](/reference/services/SoftLayer_Account/getShipments)
Retrieve shipments that belong to the customer's account.

#### [getSshKeys](/reference/services/SoftLayer_Account/getSshKeys)
Retrieve customer specified SSH keys that can be implemented onto a newly provisioned or reloaded server.

#### [getSslVpnUsers](/reference/services/SoftLayer_Account/getSslVpnUsers)
Retrieve an account's associated portal users with SSL VPN access.

#### [getStandardPoolVirtualGuests](/reference/services/SoftLayer_Account/getStandardPoolVirtualGuests)
Retrieve an account's virtual guest objects that are hosted on a user provisioned hypervisor.

#### [getSubnetRegistrationDetails](/reference/services/SoftLayer_Account/getSubnetRegistrationDetails)


#### [getSubnetRegistrations](/reference/services/SoftLayer_Account/getSubnetRegistrations)


#### [getSubnets](/reference/services/SoftLayer_Account/getSubnets)
Retrieve all network subnets associated with an account.

#### [getSupportRepresentatives](/reference/services/SoftLayer_Account/getSupportRepresentatives)
Retrieve the SoftLayer employees that an account is assigned to.

#### [getSupportSubscriptions](/reference/services/SoftLayer_Account/getSupportSubscriptions)
Retrieve the active support subscriptions for this account.

#### [getSupportTier](/reference/services/SoftLayer_Account/getSupportTier)


#### [getSuppressInvoicesFlag](/reference/services/SoftLayer_Account/getSuppressInvoicesFlag)
Retrieve a flag indicating to suppress invoices.

#### [getTags](/reference/services/SoftLayer_Account/getTags)


#### [getTechIncubatorProgramInfo](/reference/services/SoftLayer_Account/getTechIncubatorProgramInfo)
This method retrieves the Technology Incubator Program information for your account. 

#### [getThirdPartyPoliciesAcceptanceStatus](/reference/services/SoftLayer_Account/getThirdPartyPoliciesAcceptanceStatus)
Get the acceptance status of the applicable third-party policies.

#### [getTickets](/reference/services/SoftLayer_Account/getTickets)
Retrieve an account's associated tickets.

#### [getTicketsClosedInTheLastThreeDays](/reference/services/SoftLayer_Account/getTicketsClosedInTheLastThreeDays)
Retrieve tickets closed within the last 72 hours or last 10 tickets, whichever is less, associated with an account.

#### [getTicketsClosedToday](/reference/services/SoftLayer_Account/getTicketsClosedToday)
Retrieve tickets closed today associated with an account.

#### [getTranscodeAccounts](/reference/services/SoftLayer_Account/getTranscodeAccounts)
Retrieve an account's associated Transcode account.

#### [getUpgradeRequests](/reference/services/SoftLayer_Account/getUpgradeRequests)
Retrieve an account's associated upgrade requests.

#### [getUsers](/reference/services/SoftLayer_Account/getUsers)
Retrieve an account's portal users.

#### [getValidSecurityCertificateEntries](/reference/services/SoftLayer_Account/getValidSecurityCertificateEntries)


#### [getValidSecurityCertificates](/reference/services/SoftLayer_Account/getValidSecurityCertificates)
Retrieve stored security certificates that are not expired (ie. SSL)

#### [getVdrUpdatesInProgressFlag](/reference/services/SoftLayer_Account/getVdrUpdatesInProgressFlag)
Retrieve return 0 if vpn updates are currently in progress on this account otherwise 1.

#### [getVirtualDedicatedRacks](/reference/services/SoftLayer_Account/getVirtualDedicatedRacks)
Retrieve the bandwidth pooling for this account.

#### [getVirtualDiskImages](/reference/services/SoftLayer_Account/getVirtualDiskImages)
Retrieve an account's associated virtual server virtual disk images.

#### [getVirtualGuests](/reference/services/SoftLayer_Account/getVirtualGuests)
Retrieve an account's associated virtual guest objects.

#### [getVirtualGuestsOverBandwidthAllocation](/reference/services/SoftLayer_Account/getVirtualGuestsOverBandwidthAllocation)
Retrieve an account's associated virtual guest objects currently over bandwidth allocation.

#### [getVirtualGuestsProjectedOverBandwidthAllocation](/reference/services/SoftLayer_Account/getVirtualGuestsProjectedOverBandwidthAllocation)
Retrieve an account's associated virtual guest objects currently over bandwidth allocation.

#### [getVirtualGuestsWithCpanel](/reference/services/SoftLayer_Account/getVirtualGuestsWithCpanel)
Retrieve all virtual guests associated with an account that has the cPanel web hosting control panel installed.

#### [getVirtualGuestsWithMcafee](/reference/services/SoftLayer_Account/getVirtualGuestsWithMcafee)
Retrieve all virtual guests associated with an account that have McAfee Secure software components.

#### [getVirtualGuestsWithMcafeeAntivirusRedhat](/reference/services/SoftLayer_Account/getVirtualGuestsWithMcafeeAntivirusRedhat)
Retrieve all virtual guests associated with an account that have McAfee Secure AntiVirus for Redhat software components.

#### [getVirtualGuestsWithMcafeeAntivirusWindows](/reference/services/SoftLayer_Account/getVirtualGuestsWithMcafeeAntivirusWindows)
Retrieve all virtual guests associated with an account that has McAfee Secure AntiVirus for Windows software components.

#### [getVirtualGuestsWithMcafeeIntrusionDetectionSystem](/reference/services/SoftLayer_Account/getVirtualGuestsWithMcafeeIntrusionDetectionSystem)
Retrieve all virtual guests associated with an account that has McAfee Secure Intrusion Detection System software components.

#### [getVirtualGuestsWithPlesk](/reference/services/SoftLayer_Account/getVirtualGuestsWithPlesk)
Retrieve all virtual guests associated with an account that has the Plesk web hosting control panel installed.

#### [getVirtualGuestsWithQuantastor](/reference/services/SoftLayer_Account/getVirtualGuestsWithQuantastor)
Retrieve all virtual guests associated with an account that have the QuantaStor storage system installed.

#### [getVirtualGuestsWithUrchin](/reference/services/SoftLayer_Account/getVirtualGuestsWithUrchin)
Retrieve all virtual guests associated with an account that has the Urchin web traffic analytics package installed.

#### [getVirtualPrivateRack](/reference/services/SoftLayer_Account/getVirtualPrivateRack)
Retrieve the bandwidth pooling for this account.

#### [getVirtualStorageArchiveRepositories](/reference/services/SoftLayer_Account/getVirtualStorageArchiveRepositories)
Retrieve an account's associated virtual server archived storage repositories.

#### [getVirtualStoragePublicRepositories](/reference/services/SoftLayer_Account/getVirtualStoragePublicRepositories)
Retrieve an account's associated virtual server public storage repositories.

#### [getVmWareActiveAccountLicenseKeys](/reference/services/SoftLayer_Account/getVmWareActiveAccountLicenseKeys)
Get a collection of active VMware software account license keys.

#### [getVpcVirtualGuests](/reference/services/SoftLayer_Account/getVpcVirtualGuests)
Retrieve an account's associated VPC configured virtual guest objects.

#### [getWindowsUpdateStatus](/reference/services/SoftLayer_Account/getWindowsUpdateStatus)
Retrieve a list of an account's hardware's Windows Update status.

#### [hasAttribute](/reference/services/SoftLayer_Account/hasAttribute)
Determine if an account has a given attribute.

#### [hourlyInstanceLimit](/reference/services/SoftLayer_Account/hourlyInstanceLimit)
Retrieve the number of hourly services that an account is allowed to have 

#### [hourlyServerLimit](/reference/services/SoftLayer_Account/hourlyServerLimit)
Retrieve the number of hourly bare metal servers that an account is allowed to have 

#### [isActiveVmwareCustomer](/reference/services/SoftLayer_Account/isActiveVmwareCustomer)
Determines if the account is considered an active VMware customer and as such eligible to order VMware restricted products. This result is cached for up to 60 seconds. 

#### [isEligibleForLocalCurrencyProgram](/reference/services/SoftLayer_Account/isEligibleForLocalCurrencyProgram)


#### [isEligibleToLinkWithPaas](/reference/services/SoftLayer_Account/isEligibleToLinkWithPaas)
Returns true if this account is eligible to link with PaaS. False otherwise. 

#### [linkExternalAccount](/reference/services/SoftLayer_Account/linkExternalAccount)
This method will link this SoftLayer account with the provided external account. 

#### [removeAlternateCreditCard](/reference/services/SoftLayer_Account/removeAlternateCreditCard)


#### [requestCreditCardChange](/reference/services/SoftLayer_Account/requestCreditCardChange)
Retrieve the record data associated with the submission of a Credit Card Change Request.

#### [requestManualPayment](/reference/services/SoftLayer_Account/requestManualPayment)
Retrieve the record data associated with the submission of a Manual Payment Request.

#### [requestManualPaymentUsingCreditCardOnFile](/reference/services/SoftLayer_Account/requestManualPaymentUsingCreditCardOnFile)
Retrieve the record data associated with the submission of a Manual Payment Request which charges the manual payment to a credit card already on file. 

#### [setAbuseEmails](/reference/services/SoftLayer_Account/setAbuseEmails)
Set this account's abuse emails.

#### [setManagedPoolQuantity](/reference/services/SoftLayer_Account/setManagedPoolQuantity)
Set the number of desired servers in the pool

#### [setVlanSpan](/reference/services/SoftLayer_Account/setVlanSpan)
Set the flag that enables or disables automatic private network VLAN spanning for a SoftLayer customer account.

#### [swapCreditCards](/reference/services/SoftLayer_Account/swapCreditCards)


#### [syncCurrentUserPopulationWithPaas](/reference/services/SoftLayer_Account/syncCurrentUserPopulationWithPaas)
This method manually starts a synchronize operation for the current IBMid-authenticated user population of a linked account pair. "Manually" means "independent of an account link operation". 

#### [updateVpnUsersForResource](/reference/services/SoftLayer_Account/updateVpnUsersForResource)
Creates or updates a user VPN access privileges for a server on account.

#### [validate](/reference/services/SoftLayer_Account/validate)
Validates SoftLayer account information. Will return an error if any field is not valid.

#### [validateManualPaymentAmount](/reference/services/SoftLayer_Account/validateManualPaymentAmount)
Ensure the amount requested for a manual payment is valid.

</div>

