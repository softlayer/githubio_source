---
title: "SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Plugin"
description: "This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. This datatype has every... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Plugin"
---

# SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Plugin
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Plugin' >Datatype</a></li>
    </ul>
</div>

## Description 
This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. This datatype has everything required to place an order for additional Evault plugins. 


### associatedMethods

*  [SoftLayer_Product_Order::verifyOrder](/reference/services/SoftLayer_Product_Order/verifyOrder )
*  [SoftLayer_Product_Order::placeOrder](/reference/services/SoftLayer_Product_Order/placeOrder )





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
[bigDataOrderFlag]: #bigdataorderflag
#### [bigDataOrderFlag]
Flag for identifying an order for Big Data Deployment.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[billingInformation]: #billinginformation
#### [billingInformation]
Billing Information associated with an order. For existing customers this information is completely ignored. Do not send this information for existing customers.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Product_Order_Billing_Information'>SoftLayer_Container_Product_Order_Billing_Information </a>**


</div>
<div class="prop-row">

-----
[billingOrderItemId]: #billingorderitemid
#### [billingOrderItemId]
This is the ID of the [SoftLayer_Billing_Order_Item]({{<ref "reference/datatypes/SoftLayer_Billing_Order_Item">}}) of this configuration/container. It is used for rebuilding an order container from a quote and is set automatically.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[cancelUrl]: #cancelurl
#### [cancelUrl]
The URL to which PayPal redirects browser after checkout has been canceled before completion of a payment.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[containerIdentifier]: #containeridentifier
#### [containerIdentifier]
User-specified description to identify a particular order container. This is useful if you have a multi-configuration order (multiple <code>orderContainers</code>) and you want to be able to easily determine one from another. Populating this value may be helpful if an exception is thrown when placing an order and it's tied to a specific order container.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[containerSplHash]: #containersplhash
#### [containerSplHash]
This hash is internally-generated and is used to for tracking order containers.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[currencyShortName]: #currencyshortname
#### [currencyShortName]
The currency type chosen at checkout.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[deviceFingerprintId]: #devicefingerprintid
#### [deviceFingerprintId]
Device Fingerprint Identifier - Optional.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[displayLayerSessionId]: #displaylayersessionid
#### [displayLayerSessionId]
This is the configuration identifier for tracking orders on the HTML order forms.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[extendedHardwareTesting]: #extendedhardwaretesting
#### [extendedHardwareTesting]
  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[flexibleCreditProgramPrice]: #flexiblecreditprogramprice
#### [flexibleCreditProgramPrice]
The [SoftLayer_Product_Item_Price]({{<ref "reference/datatypes/SoftLayer_Product_Item_Price">}}) for the Flexible Credit Program discount.  The <code>oneTimeFee</code> field contains the calculated discount being applied to the order.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price </a>**


</div>
<div class="prop-row">

-----
[gdprConsentFlag]: #gdprconsentflag
#### [gdprConsentFlag]
This flag indicates that the customer consented to the GDPR terms for the quote.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
For orders that contain servers (bare metal, virtual server, big data, etc.), the hardware property is required. This property is an array of [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) objects. The <code>hostname</code> and <code>domain</code> properties are required for each hardware object. Note that virtual server ([SoftLayer_Container_Product_Order_Virtual_Guest]({{<ref "reference/datatypes/SoftLayer_Container_Product_Order_Virtual_Guest">}})) orders may populate this field instead of the <code>virtualGuests</code> property.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[imageTemplateGlobalIdentifier]: #imagetemplateglobalidentifier
#### [imageTemplateGlobalIdentifier]
An optional virtual disk image template identifier to be used as an installation base for a computing instance order  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[imageTemplateId]: #imagetemplateid
#### [imageTemplateId]
An optional virtual disk image template identifier to be used as an installation base for a computing instance order  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[isManagedOrder]: #ismanagedorder
#### [isManagedOrder]
Flag to identify a "managed" order. This value is set internally.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[itemCategoryQuestionAnswers]: #itemcategoryquestionanswers
#### [itemCategoryQuestionAnswers]
The collection of [SoftLayer_Container_Product_Item_Category_Question_Answer]({{<ref "reference/datatypes/SoftLayer_Container_Product_Item_Category_Question_Answer">}}) for any product category that has additional questions requiring user input.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Product_Item_Category_Question_Answer'>SoftLayer_Container_Product_Item_Category_Question_Answer[] </a>**


</div>
<div class="prop-row">

-----
[location]: #location
#### [location]
The [SoftLayer_Location_Region]({{<ref "reference/datatypes/SoftLayer_Location_Region">}}) keyname or specific [SoftLayer_Location_Datacenter]({{<ref "reference/datatypes/SoftLayer_Location_Datacenter">}}) id where the order should be provisioned. If this value is provided and the <code>regionalGroup</code> property is also specified, an exception will be thrown indicating that only 1 is allowed.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[locationObject]: #locationobject
#### [locationObject]
This [SoftLayer_Location]({{<ref "reference/datatypes/SoftLayer_Location">}}) object will be determined from the <code>location</code> property and will be returned in the order verification or placement response. Any value specified here will get overwritten by the verification process.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


</div>
<div class="prop-row">

-----
[message]: #message
#### [message]
A generic message about the order. Does not need to be sent in with any orders.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[orderContainers]: #ordercontainers
#### [orderContainers]
Orders may contain an array of configurations. Populating this property allows you to purchase multiple configurations within a single order. Each order container will have its own individual settings independent of the other order containers. For example, it is possible to order a bare metal server in one configuration and a virtual server in another. 

If <code>orderContainers</code> is populated on the base order container, most of the configuration-specific properties are ignored on the base container. For example, <code>prices</code>, <code>location</code> and <code>packageId</code> will be ignored on the base container, but since the <code>billingInformation</code> is a property that's not specific to a single order container (but the order as a whole) it must be populated on the base container.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order[] </a>**


</div>
<div class="prop-row">

-----
[orderHostnames]: #orderhostnames
#### [orderHostnames]
This is deprecated and does not do anything.   
<span class="type-label">Type: </span>**array of strings**


</div>
<div class="prop-row">

-----
[orderVerificationExceptions]: #orderverificationexceptions
#### [orderVerificationExceptions]
Collection of exceptions resulting from the verification of the order. This value is set internally and is not required for end users when placing an order. When placing API orders, users can use this value to determine the container-specific exception that was thrown.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Exception'>SoftLayer_Container_Exception[] </a>**


</div>
<div class="prop-row">

-----
[packageId]: #packageid
#### [packageId]
The [SoftLayer_Product_Package]({{<ref "reference/datatypes/SoftLayer_Product_Package">}}) id for an order container. This is required to place an order.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[paymentType]: #paymenttype
#### [paymentType]
The Payment Type is Optional. If nothing is sent in, then the normal method of payment will be used. For paypal customers, this means a paypalToken will be returned in the receipt. This token is to be used on the paypal website to complete the order. For Credit Card customers, the card on file in our system will be used to make an initial authorization. To force the order to use a payment type, use one of the following: CARD_ON_FILE or PAYPAL   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[postTaxRecurring]: #posttaxrecurring
#### [postTaxRecurring]
The post-tax recurring charge for the order. This is the sum of preTaxRecurring + totalRecurringTax.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[postTaxRecurringHourly]: #posttaxrecurringhourly
#### [postTaxRecurringHourly]
The post-tax recurring hourly charge for the order. Since taxes are not calculated for hourly orders, this value will be the same as preTaxRecurringHourly.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[postTaxRecurringMonthly]: #posttaxrecurringmonthly
#### [postTaxRecurringMonthly]
The post-tax recurring monthly charge for the order. This is the sum of preTaxRecurringMonthly + totalRecurringTax.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[postTaxSetup]: #posttaxsetup
#### [postTaxSetup]
The post-tax setup fees of the order. This is the sum of preTaxSetup + totalSetupTax;  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[preTaxRecurring]: #pretaxrecurring
#### [preTaxRecurring]
The pre-tax recurring total of the order. If there are mixed monthly and hourly prices on the order, this will be the sum of preTaxRecurringHourly and preTaxRecurringMonthly.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[preTaxRecurringHourly]: #pretaxrecurringhourly
#### [preTaxRecurringHourly]
The pre-tax hourly recurring total of the order. If there are only monthly prices on the order, this value will be 0.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[preTaxRecurringMonthly]: #pretaxrecurringmonthly
#### [preTaxRecurringMonthly]
The pre-tax monthly recurring total of the order. If there are only hourly prices on the order, this value will be 0.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[preTaxSetup]: #pretaxsetup
#### [preTaxSetup]
The pre-tax setup fee total of the order.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[presaleEvent]: #presaleevent
#### [presaleEvent]
If there are any presale events available for an order, this value will be populated. It is set internally and is not required for end users when placing an order. See [SoftLayer_Sales_Presale_Event]({{<ref "reference/datatypes/SoftLayer_Sales_Presale_Event">}}) for more info.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Sales_Presale_Event'>SoftLayer_Sales_Presale_Event </a>**


</div>
<div class="prop-row">

-----
[presetId]: #presetid
#### [presetId]
A preset configuration id for the package. Is required if not submitting any prices.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[prices]: #prices
#### [prices]
This is a collection of [SoftLayer_Product_Item_Price]({{<ref "reference/datatypes/SoftLayer_Product_Item_Price">}}) objects. The only required property to populate for an item price object when ordering is its <code>id</code> - all other supplied information about the price (e.g., recurringFee, setupFee, etc.) will be ignored. Unless the [SoftLayer_Product_Package]({{<ref "reference/datatypes/SoftLayer_Product_Package">}}) associated with the order allows for preset prices, this property is required to place an order.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>**


</div>
<div class="prop-row">

-----
[primaryDiskPartitionId]: #primarydiskpartitionid
#### [primaryDiskPartitionId]
The id of a [SoftLayer_Hardware_Component_Partition_Template]({{<ref "reference/datatypes/SoftLayer_Hardware_Component_Partition_Template">}}). This property is optional. If no partition template is provided, a default will be used according to the operating system chosen with the order. Using the [SoftLayer_Hardware_Component_Partition_OperatingSystem]({{<ref "reference/datatypes/SoftLayer_Hardware_Component_Partition_OperatingSystem">}}) service, getPartitionTemplates will return those available for the particular operating system.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[priorities]: #priorities
#### [priorities]
Priorities to set on replication set servers.  
<span class="type-label">Type: </span>**array of strings**


</div>
<div class="prop-row">

-----
[privateCloudOrderFlag]: #privatecloudorderflag
#### [privateCloudOrderFlag]
Flag for identifying a container as Virtual Server (Private Node).  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[privateCloudOrderType]: #privatecloudordertype
#### [privateCloudOrderType]
Type of Virtual Server (Private Node) order. Potential values: INITIAL, ADDHOST, ADDIPS, ADDZONE   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[promotionCode]: #promotioncode
#### [promotionCode]
Optional promotion code for an order.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[properties]: #properties
#### [properties]
Generic properties.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Product_Order_Property'>SoftLayer_Container_Product_Order_Property[] </a>**


</div>
<div class="prop-row">

-----
[proratedInitialCharge]: #proratedinitialcharge
#### [proratedInitialCharge]
The Prorated Initial Charge plus the balance on the account. Only the recurring fees are prorated. Here's how the calculation works: We take the postTaxRecurring value and we prorate it based on the time between now and the next bill date for this account. After this, we add in the setup fee since this is not prorated. Then, if there is a balance on the account, we add that to the account. In the event that there is a credit balance on the account, we will subtract this amount from the order total. If the credit balance on the account is greater than the prorated initial charge, the order will go through without a charge to the credit card on the account or requiring a paypal payment. The credit on the account will be reduced by the order total, and the order will await approval from sales, as normal. If there is a pending order already in the system, We will ignore the balance on the account completely, in the calculation of the initial charge. This is to protect against two orders coming into the system and getting the benefit of a credit balance, or worse, both orders being charged the order amount + the balance on the account.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[proratedOrderTotal]: #proratedordertotal
#### [proratedOrderTotal]
This is the same as the proratedInitialCharge, except the balance on the account is ignored. This is the prorated total amount of the order.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[provisionScripts]: #provisionscripts
#### [provisionScripts]
The URLs for scripts to execute on their respective servers after they have been provisioned. Provision scripts are not available for Microsoft Windows servers.  
<span class="type-label">Type: </span>**array of strings**


</div>
<div class="prop-row">

-----
[quantity]: #quantity
#### [quantity]
The quantity of the item being ordered  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[quoteName]: #quotename
#### [quoteName]
A custom name to be assigned to the quote.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[regionalGroup]: #regionalgroup
#### [regionalGroup]
Specifying a regional group name allows you to not worry about placing your server or service at a specific datacenter, but to any datacenter within that regional group. See [SoftLayer_Location_Group_Regional]({{<ref "reference/datatypes/SoftLayer_Location_Group_Regional">}}) to get a list of available regional group names. 

<code>location</code> and <code>regionalGroup</code> are mutually exclusive on an order container. If both location and regionalGroup are provided, an exception will be thrown indicating that only 1 is allowed. 

If a regional group is provided and VLANs are specified (within the <code>hardware</code> or <code>virtualGuests</code> properties), we will use the datacenter where the VLANs are located. If no VLANs are specified, we will use the preferred datacenter on the regional group object.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[resourceGroupId]: #resourcegroupid
#### [resourceGroupId]
An optional resource group identifier specifying the resource group to attach the order to  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[resourceGroupName]: #resourcegroupname
#### [resourceGroupName]
This variable specifies the name of the resource group the server configuration belongs to. For MongoDB Replica sets, it would be the replica set name.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[resourceGroupTemplateId]: #resourcegrouptemplateid
#### [resourceGroupTemplateId]
An optional resource group template identifier to be used as a deployment base for a Virtual Server (Private Node) order.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[returnUrl]: #returnurl
#### [returnUrl]
The URL to which PayPal redirects browser after a payment is completed.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[sendQuoteEmailFlag]: #sendquoteemailflag
#### [sendQuoteEmailFlag]
This flag indicates that the quote should be sent to the email address associated with the account or order.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[serverCoreCount]: #servercorecount
#### [serverCoreCount]
The number of cores for the server being ordered. This value is set internally.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[serviceToken]: #servicetoken
#### [serviceToken]
The token of a requesting service. Do not set.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[sourceVirtualGuestId]: #sourcevirtualguestid
#### [sourceVirtualGuestId]
An optional computing instance identifier to be used as an installation base for a computing instance order  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[sshKeys]: #sshkeys
#### [sshKeys]
The containers which hold SoftLayer_Security_Ssh_Key IDs to add to their respective servers. The order of containers passed in needs to match the order they are assigned to either hardware or virtualGuests. SSH Keys will not be assigned for servers with Microsoft Windows.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Product_Order_SshKeys'>SoftLayer_Container_Product_Order_SshKeys[] </a>**


</div>
<div class="prop-row">

-----
[stepId]: #stepid
#### [stepId]
An optional parameter for step-based order processing.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[storageGroups]: #storagegroups
#### [storageGroups]


For orders that want to add storage groups such as RAID across multiple disks, simply add [SoftLayer_Container_Product_Order_Storage_Group]({{<ref "reference/datatypes/SoftLayer_Container_Product_Order_Storage_Group">}}) objects to this array. Storage groups will only be used if the 'RAID' disk controller price is selected. Any other disk controller types will ignore the storage groups set here. 

The first storage group in this array will be considered the primary storage group, which is used for the OS. Any other storage groups will act as data storage. 

  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Product_Order_Storage_Group'>SoftLayer_Container_Product_Order_Storage_Group[] </a>**


</div>
<div class="prop-row">

-----
[taxCacheHash]: #taxcachehash
#### [taxCacheHash]
The order container may not contain the final tax rates when it is returned from [SoftLayer_Product_Order::verifyOrder]({{<ref "reference/services/SoftLayer_Product_Order/verifyOrder">}}). This hash will facilitate checking if the tax rates have finished being calculated and retrieving the accurate tax rate values.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[taxCompletedFlag]: #taxcompletedflag
#### [taxCompletedFlag]
Flag to indicate if the order container has the final tax rates for the order. Some tax rates are calculated in the background because they take longer, and they might not be finished when the container is returned from [SoftLayer_Product_Order::verifyOrder]({{<ref "reference/services/SoftLayer_Product_Order/verifyOrder">}}).   
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[techIncubatorItemPrice]: #techincubatoritemprice
#### [techIncubatorItemPrice]
The SoftLayer_Product_Item_Price for the Tech Incubator discount.  The oneTimeFee field contain the calculated discount being applied to the order.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price </a>**


</div>
<div class="prop-row">

-----
[totalRecurringTax]: #totalrecurringtax
#### [totalRecurringTax]
The total tax portion of the recurring fees.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[totalSetupTax]: #totalsetuptax
#### [totalSetupTax]
The tax amount of the setup fees.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[usagePrices]: #usageprices
#### [usagePrices]
This is a collection of [SoftLayer_Product_Item_Price]({{<ref "reference/datatypes/SoftLayer_Product_Item_Price">}}) objects which will be used when the service offering being ordered generates usage. This is a read-only property. Setting this property will not change the order.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>**


</div>
<div class="prop-row">

-----
[useHourlyPricing]: #usehourlypricing
#### [useHourlyPricing]
An optional flag to use hourly pricing instead of standard monthly pricing.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[virtualGuests]: #virtualguests
#### [virtualGuests]
For virtual guest (virtual server) orders, this property is required if you did not specify data in the <code>hardware</code> property. This is an array of [SoftLayer_Virtual_Guest]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest">}}) objects. The <code>hostname</code> and <code>domain</code> properties are required for each virtual guest object. There is no need to specify data in this property and the <code>hardware</code> property - only one is required for virtual server orders.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


