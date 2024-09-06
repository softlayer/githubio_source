---
title: "Billing and Invoices"
description: "Some examples of how to get billing and invoicing data from the API."
date: "2019-08-22"
tags:
    - "article"
    - "sldn"
    - "invoice"
    - "billing"
---


## Getting Invoices

Everything that will be charged to your total balance will appear on an invoice, of which there are three main type.

To get the total balance on your account, simply use [SoftLayer_Account::getBalance](/reference/services/SoftLayer_Account/getBalance/). 

```
curl -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getBalance.json'
```

#### NEW
Anything that is newly ordered will appear as a `NEW` type invoice. After the billing cycle ends, these will roll into the `RECURRING` type of invoice.

#### RECURRING
Usually each month you will have one recurring invoice, containing everything that was billed to the account, outside of any charges that appear on `NEW` and `ONE-TIME-CHARGE` invoices. 

>*NOTE*:  
>Recurring invoices may still have `ITEMS` that are billed as a one-time-charge, which are different than  `ONE-TIME-CHARGE` Invoices. Items that show up on recurring invoices that are one-time-charge include consumption based billing item, like bandwidth overages for example.

#### ONE-TIME-CHARGE
These will usually be related to upgrade charges or similar. They are incurred once and don't roll into a `RECURRING` invoice. 

There are several ways to get invoice data from the API.

-----------------------------

#### [SoftLayer_Account::getInvoices](/reference/services/SoftLayer_Account/getInvoices/)

This method will return all invoices your account has ever had, which can be quite a lot if your account has been around for a while. By default, these will be returned Oldest first, which is usually not ideal, so to fix that we use an objectFilter to sort them. This API call will also set a resultLimit of 50.

```shell
# Calling: SoftLayer_Account::getInvoices(id=None, mask='mask[invoiceTotalAmount, itemCount]', filter='{'invoices': {'createDate': {'operation': 'orderBy', 'options': [{'name': 'sort', 'value': ['DESC']}]}}}', args=(), limit=50, offset=0))

curl -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getInvoices.json?objectMask=mask[invoiceTotalAmount,itemCount]&resultLimit=0,50&objectFilter={"invoices":{"createDate":{"operation":"orderBy","options":[{"name":"sort","value":["DESC"]}]}}}'
```

To filter between a certain set of dates, use this:
```shell
slcli --format=json -vvv call-api SoftLayer_Account getInvoices --mask="mask[id,createDate,invoiceTotalAmount,itemCount]" --json-filter='{"invoices":{"createDate":{"operation":"betweenDate","options":[{"name":"startDate","value":["12/01/2020"]},{"name":"endDate","value":["02/01/2021"]}]}}}'

curl -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getInvoices.json?objectMask=mask[id,createDate,invoiceTotalAmount,itemCount]&objectFilter={"invoices":{"createDate":{"operation":"betweenDate","options":[{"name":"startDate","value":["12/01/2020"]},{"name":"endDate","value":["02/01/2021"]}]}}}'
```

#### [SoftLayer_Account::getLatestRecurringInvoice](/reference/services/SoftLayer_Account/getLatestRecurringInvoice/)

`getLatestRecurringInvoice` will only return the latest recurring invoice, as the name suggests. This invoice will generally be for the current billing period which needs to be paid. 

```
curl -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getLatestRecurringInvoice.json'
```

There also exists the [SoftLayer_Account::getLatestRecurringPendingInvoice](/reference/services/SoftLayer_Account/getLatestRecurringPendingInvoice/) method, which will only return the latest recurring invoice if it's status is `OPEN`, meaning it has yet to be paid off fully yet. If the latest invoice is open, these will return the same invoice.

-----------------------------


## The [Billing_Invoice](/reference/datatypes/SoftLayer_Billing_Invoice/) Itself

Some key fields in the Billing_Invoice datatype.

#### invoiceTotalAmount
This is the amount that will be added to the SoftLayer_Account::balance from this invoice. It is broken down into a few other amounts like `invoiceTotalOneTimeAmount`, `invoiceTotalOneTimeTaxAmount`, `invoiceTotalPreTaxAmount`, `invoiceTotalRecurringAmount`, `invoiceTotalRecurringTaxAmount`.

#### payments

Payments that made it into the invoice will show up here.

#### invoiceTopLevelItems
Top Level items that are included on this invoice. This will be things like your servers, virtual guests, any bandwidth charges and things like that.

#### items
Everything billed to this invoice, including top level items and their children.

#### PDF / Excel

The invoice can also be retrieved in Excel or PDF format directly from the API.
Of note though, is the data returned from the API is going to be base64 Encoded, so you will need to decode it first before that data is usable.

+ [SoftLayer_Billing_Invoice::getPdf](/reference/services/SoftLayer_Billing_Invoice/getPdf/)
+ [SoftLayer_Billing_Invoice::getPdfDetailed](/reference/services/SoftLayer_Billing_Invoice/getPdfDetailed/)
+ [SoftLayer_Billing_Invoice::getExcel](/reference/services/SoftLayer_Billing_Invoice/getExcel/)

> The API result is encapsulated in "", and escapes the `/` characters, both of which are invalid and need to removed, which is why the `tr` command is used below. Otherwise `base64` will return the error `Invalid character in input stream.` 

```
curl -s -u $SL_USER:$SL_APIKEY  'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Invoice/<INVOICE_ID>/getPdf.json' | tr -d '"\' > invoice.base64
base64 -D  -i invoice.base64 -o invoice.pdf
```

-----------------------------

## Your Next Invoice
[SoftLayer_Account::getNextInvoiceTopLevelBillingItems()](https://sldn.softlayer.com/reference/services/SoftLayer_Account/getNextInvoiceTopLevelBillingItems/) will return all of the billing items that will show up on the next invoice, assuming nothing changes between now and the next invoice creation.

```shell
slcli --format=json -vvv call-api SoftLayer_Account getNextInvoiceTopLevelBillingItems --limit=10
curl -u $SL_USER:$SL_APIKEY  'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getNextInvoiceTopLevelBillingItems.json?resultLimit=0%2C10'
```

## [Billing_Invoice_Item](/reference/datatypes/SoftLayer_Billing_Invoice_Item/)

Each[SoftLayer_Billing_Item](/reference/datatypes/SoftLayer_Billing_Item/) on an account will generate a Billing_INVOICE_Item. The Billing_INVOICE_Item itself will have a link to its generating Billing_Item in the `billingItem` relation. There is also a variety of information about the Item being billed here, unfortunately there isn't going to be a direct link back to the actual resource (such as the Hardware_Server or Virtual_Guest).

The `resourceTableId` property will contain the Id of the actual resource being billed, but there is no programmatic way to translating that id to the appropriate service directly. You would need to use the `category->categoryCode` to determine which type of resource this Item represents.

-----------------------------

## [Billing_Item](/reference/datatypes/SoftLayer_Billing_Item/)

Every resource will have a Billing_Item that lets you know how much the resource will cost as either an hourly cost (`hourlyRecurringFee`),  monthly cost (`recurringFee`) or one-time cost (`oneTimeFee`). There are a few other fee types (like taxes and setup fees) on the Billing_Item datatype as well that may need to be taken into account, depending on the resource. 

#### children
Some Billing_Items will have children that may account for some of the total cost of the resource, but might not be reflected directly on this item. For example Hardware_Server resources will usually have several child items that represent the cost of RAM/Disks/Port Speed and such. The `recurringFee` of the parent item will not be the full cost of the server, but only the cost of the chassis itself. To find the full cost of a server, you would need to add up the child `recurringFee` with the parent's `recurringFee`, or simply refer to the `nextInvoiceTotal` relations.

#### filteredNextInvoiceChildren
Handy for finding the true cost of an item with all its children. Excludes any item that has no cost.

#### nextInvoiceTotalRecurringAmount
This property will reflect the true recurring cost of the resource that will show up on the invoice, includes child items. The other related `nextInvoiceTotal*` properties are useful as well.

#### orderItem
A link to the [SoftLayer_Billing_Order_Item](/reference/datatypes/SoftLayer_Billing_Order_Item/), which can link to the actual [SoftLayer_Billing_Order](/reference/datatypes/SoftLayer_Billing_Order/), which will contain information about who ordered the resource, and when.
 
#### resourceTableId
This is the `id` of the actual resource being billed for. There is not programatic way to relate this `id` with a specific service, but here is a partial mapping for reference.

|Item CategoryCode | Service |
| ---------------  | ------- |
| guest_core | SoftLayer_Virtual_Guest | 
| load_balancer_as_a_service | SoftLayer_Network_LBaaS_LoadBalancer |
| network_vlan | SoftLayer_Network_Vlan | 
| server | SoftLayer_Hardware_Server | 
| vlan_firewall | SoftLayer_Network_Firewall | 
| storage_as_a_service | SoftLayer_Network_Storage |


-----------------------------

## Resource Billing

While the invoice is a great way to get a high level view of what you are being billed for, it can be cumbersome to use that to find out how much a specific resource is costing you.  To do that, we will start at the resource's service, and go to its billingItem.


+ [Hardware_Firewall](/reference/datatypes/SoftLayer_Hardware_Firewall/#billingItem)
+ [Network_Application_Delivery_Controller](/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller/#billingItem)
+ [Network_CdnMarketplace_Account](/reference/datatypes/SoftLayer_Network_CdnMarketplace_Account/#billingItem)
+ [Hardware_Server](/reference/datatypes/SoftLayer_Hardware_Server/#billingItem)
+ [Network_Storage](/reference/datatypes/SoftLayer_Network_Storage/#billingItem)
+ [Network_Subnet](/reference/datatypes/SoftLayer_Network_Subnet/#billingItem)
+ [Network_Vlan](/reference/datatypes/SoftLayer_Network_Vlan/#billingItem)
+ [Network_Vlan_Firewall](/reference/datatypes/SoftLayer_Network_Vlan_Firewall/#billingItem)
+ [Virtual_Guest](/reference/datatypes/SoftLayer_Virtual_Guest/#billingItem)

-----------------------------

## IBM Cloud Documentation

+ [IBM Billing Documentation](https://cloud.ibm.com/docs/billing-usage)
