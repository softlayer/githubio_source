---
title: "Working with Brands"
description: "Details on how to work with a Brand account."
date: "2020-07-23"
classes:
    - "SoftLayer_Brand"
    - "SoftLayer_Billing_Invoice"
tags:
    - "brand"
    - "bap"
---


A Brand account is a special type of account at SoftLayer that allows the owner to manage sub-accounts. These sub accounts are separate and individual like any other SoftLayer account, with the exception being that the Brand Master account has access to them.


For these examples, all API calls will be made by a user under the brand master account.

## Owned Brands

To use the [SoftLayer_Brand](/reference/services/SoftLayer_Brand) you first need to find out the BrandId that the account owns. This can be done with the [SoftLayer_Account::getOwnedBrands()](/reference/services/SoftLayer_Account/getOwnedBrands/) API call.

```
$ curl -s -u $SL_BAP_USER:$SL_BAP_KEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getOwnedBrands' |  python -m json.tool
[
    {
        "catalogId": 14,
        "id": 16762,
        "keyName": "SLD_SL_DIST_DEMO_VAR01",
        "longName": "SoftLayer Distributor Demo - VAR 01",
        "name": "SoftLayer Distributor Demo - VAR 01"
    }
]
```


## Owned Accounts

Now that we have a brandId (16762 in the above example), we can use the Brand service to get our owned accounts with [SoftLayer_Brand::getOwnedAccounts()](/reference/services/SoftLayer_Brand/getOwnedAccounts/)

>-g in the curl command lets you use un-escaped brackets

```
$ curl -g -s -u $SL_BAP_USER:$SL_BAP_KEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Brand/16762/getOwnedAccounts?objectMask=mask[id,companyName,createDate]' |  python -m json.tool
[
    {
        "companyName": "SoftLayer Distributor Demo - VAR 01 - Child Account",
        "createDate": "2014-06-11T11:40:18-05:00",
        "id": 345582
    },
    {
        "companyName": "Partner Ecosystem Test ",
        "createDate": "2020-05-19T11:07:37-05:00",
        "id": 2088582
    }
]
```

## Current Useage by Account

To see what your accounts are currently using and being billed for, we need to look at each accounts [nextInvoiceTopLevelBillingItems](/reference/datatypes/SoftLayer_Account/#nextinvoicetoplevelbillingitems)


```
$ curl -g -s -u $SL_BAP_USER:$SL_BAP_KEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Brand/16762/getOwnedAccounts?objectMask=mask[id,companyName,createDate,nextInvoiceTopLevelBillingItems]&resultLimit=0,1' |  python -m json.tool         
[
    {
        "companyName": "SoftLayer Distributor Demo - VAR 01 - Child Account",
        "createDate": "2014-06-11T11:40:18-05:00",
        "id": 345582,
        "nextInvoiceTopLevelBillingItems": [
            {
                "categoryCode": "hub",
                "createDate": "2014-06-13T08:29:04-05:00",
                "cycleStartDate": "2020-07-11T00:51:36-05:00",
                "description": "Object Storage - Pay as you go",
                "id": 28184354,
                "lastBillDate": "2020-07-11T00:51:36-05:00",
                "modifyDate": "2020-07-11T00:51:36-05:00",
                "nextBillDate": "2020-08-11T00:00:00-05:00",
                "orderItemId": 36760662,
                "parentId": null,
                "recurringFee": "0",
                "recurringFeeTaxRate": "0",
                "recurringMonths": 1,
            },
    }
]
```

There may be quite a lot of these items, so it is a good idea to use a [resultLimit](/article/using-result-limits-softlayer-api/) to page through the accounts. It is also a good idea to use a restrictive [objectMask](/article/object-masks/), and only select the fields you need access to.

> Selecting a local property of in an objectMask will deselect all the default properties not in the object mask for that level. In this example id,companyName,createDate are local to the Account datatype, but since no properties were defined in nextInvoiceTopLevelBillingItems, all the defaults are returned.


## Getting Invoices

Invoices can contain a lot of data, so it is best to use the `Brand` service to get some basic information about the invoice (`id` and `createDate` specifically) and then use the `Billing_Invoice` service to get further information about the items on each invoice.

- [latestRecurringInvoice](/reference/datatypes/SoftLayer_Account/#latestrecurringinvoice) is used to get the accounts most current invoice.
- [latestRecurringPendingInvoice](/reference/datatypes/SoftLayer_Account/#latestrecurringpendinginvoice) is used to get the accounts most current invoice that is NOT closed. Invoices are usually closed once the balance has been paid.
- [invoices](/datatypes/SoftLayer_Account/#invoices) will list ALL of the accounts invoices

```
$ curl -g -s -u $SL_BAP_USER:$SL_BAP_KEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Brand/16762/getOwnedAccounts?objectMask=mask[id,companyName,createDate,latestRecurringInvoice]&resultLimit=0,2' |  python -m json.tool 

```


### The Invoice

[Billing and Invoices](/article/billing/) goes into detail on how invoices work at SoftLayer, and should be very helpful.

Once you have the invoice id, you will likely be most concerned with the [invoiceTopLevelItems](/reference/services/SoftLayer_Billing_Invoice/getInvoiceTopLevelItems/)


```
$ curl -g -s -u $SL_BAP_USER:$SL_BAP_KEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Invoice/56409210/getInvoiceTopLevelItems?objectMask=mask[children,invoice[id]]&resultLimit=0,200' | python -m json.tool
```

> the invoice[id] is included in the mask otherwise the whole invoice data will be included in each of the children, generating a lot of returned data. Selecting other local properties from either invoiceTopLevelItems or children would also work.

### Filtering Invoice Items

Each invoice will contain items from the cloud.ibm.com portal, which you may or may not want to parse through. To filter those out, use the following [objectFilter](/article/object-filters/)

This will limit the items returned to only those that are not in the paas categories.

```
$ curl -g -s -u $SL_BAP_USER:$SL_BAP_KEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Invoice/56409210/getInvoiceTopLevelItems?objectMask=mask[invoice[id]]&objectFilter={"invoiceTopLevelItems":{"categoryCode":{"operation":"!^=paas_"}}}&resultLimit=0,200'  | python -m json.tool
```


### Filtering Invoices on a date range

You may want to only get invoices in a certain date range, which is possible with a `filteredMask`.

```
$ curl -g -s -u $SL_BAP_USER:$SL_BAP_KEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/OwnedBrands?objectMask=filteredMask.allOwnedAccounts[id,accountStatusId,invoices[invoiceTotalAmount]]&objectFilter={"ownedBrands":{"allOwnedAccounts":{"invoices":{"createDate":{"operation":"betweenDate","options":[{"name":"startDate","value":["06/01/2020"]},{"name":"endDate","value":["07/15/2020 23:59:59"]}]}}}}}
```

or for a specific brand's accounts

```
curl -g -s -u $SL_BAP_USER:$SL_BAP_KEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Brand/16762/getOwnedAccounts?objectMask=filteredMask[id,accountStatusId,invoices[id,createDate,invoiceTotalAmount]]&objectFilter={"ownedAccounts":{"invoices":{"createDate":{"operation":"betweenDate","options":[{"name":"startDate","value":["07/01/2020"]},{"name":"endDate","value":["07/15/2020"]}]}}}}' | python -m json.tool
```

## Sub-Account Master Users

Sometimes as a brand account, it can be easier to use the API as a "normal" user. For this it is easy enough to get the master user of each sub-account and its API key, and make API calls that way.


```
curl -g -s -u $SL_BAP_USER:$SL_BAP_KEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Brand/16762/getOwnedAccounts?objectMask=mask[id,companyName,createDate,masterUser[id,username,apiAuthenticationKeys[authenticationKey]]]&resultLimit=0,2' |  python -m json.tool 
```

While it is not required, I recommend retaining control over the master account for each sub-account, and creating new user accounts for any other users.