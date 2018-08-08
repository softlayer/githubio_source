---
title: "Sub-Organization Billing Detail"
description: "This tutorial walks you through accessing the steps required to access detailed billing data across sub-organization accounts using a specified date and time range."
date: "2018-07-23"
tags:
    - "article"
    - "sldn"
    - "python"
---


# Sub-org Billing Detail

This tutorial walks you through accessing the steps required to access detailed billing data across sub-organization accounts using a specified date and time range.

## Objectives

Understand how to use multiple API services and methods to access detailed billing data for all sub organization accounts for a specified time and date range.

## Services used

This tutorial uses the following technologies:
* [SoftLayer Python Library](http://softlayer-python.readthedocs.io/en/latest/)
* [Account Service](https://softlayer.github.io/reference/services/SoftLayer_Account)
* [Billing_Invoice Service](https://softlayer.github.io/reference/services/SoftLayer_Billing_Invoice/)
* [Billing_Invoice_Item Service](https://softlayer.github.io/reference/services/SoftLayer_Billing_Invoice_Item/)
* [Billing_item Service](https://softlayer.github.io/reference/services/SoftLayer_Billing_Item/)

## Architecture

Accounts (refered to in this document as a sub account) can be owned by a Brand Account, which is the top level
account type for an organization which can enable sub-organizational level billing.  The API Key for a Brand Account
has access billing data for it's sub accounts. This tutorial demonstrates how to leverage Account, Invoice and Billing 
API's to identify invoices accross the multiple sub accounts owned by an organization for a specific range of
dates.  For each invoice, a list of top level billing items are  retreived, such as the billing data for a single
virtual machine.   These top level items, often have detailed sub-billing items such as memory, disk, or cpu which
are also retreived.  

## Install SoftLayer Python Library
* [SoftLayer API Python Client Installation](https://github.com/softlayer/softlayer-python/blob/master/README.rst)


## Obtain a list of invoices for all owned Sub Accounts

Using the [getObject](https://softlayer.github.io/reference/services/SoftLayer_Account/getObject) method of 
the [Account](https://softlayer.github.io/reference/services/SoftLayer_Account) class and a nested account mask you can return a list of invoices for all brands owned accounts.

```python
ownedBrands = client['Account'].getObject(mask="ownedBrands.allOwnedAccounts.invoices")
```

There are several types of invoices which will be returned, for this example the typical invoice type that would be of interest
 is the "RECURRING" type, which includes all the monthly recurring and hourly usage charges incurred on that invoice.

Invoice Types:
* "NEW" typeCode signifies an invoice for new service. 
* "RECURRING" invoices are generated on an accounts anniversary billing date for monthly services.
* "ONE-TIME-CHARGE" invoices are generated when one-time charges are applied to an account.
* "CREDIT" invoices are generated whenever IBM applies a credit against an account's balance. 

The list of invoices should then be filtered to include just the specific type of invoices and dates ranges to be
evaluated.

```python
ownedBrands = client['Account'].getObject(mask="ownedBrands.allOwnedAccounts.invoices")

startDate =  "2018-04-01T00:00:00-06:00"
endDate =  "2018-05-01T11:59:59-06:00"

invoiceType = "RECURRING"
invoiceList=[]

for brand in ownedBrands['ownedBrands']:
    for account in brand['allOwnedAccounts']:
        for invoice in account['invoices']:
            invoiceCreateDate = invoice['createDate']
            if (invoice['typeCode'] == invoiceType) \
                    and (dateutil.parser.parse(invoiceCreateDate) > dateutil.parser.parse(startDate)
                         and dateutil.parser.parse(invoiceCreateDate) < dateutil.parser.parse(endDate)):
                invoiceInfo = client['Billing_Invoice'].getObject(id=invoice['id'],
                    mask="id,createDate,typeCode,invoiceTotalAmount,invoiceTotalRecurringAmount,invoiceTopLevelItemCount")
                invoiceList.append(invoiceInfo)

print (invoiceList)
```

## Access invoice detail
Using the list of invoices returned, use the [getInvoiceTopLevelItems](https://softlayer.github.io/reference/services/SoftLayer_Billing_Invoice/getInvoiceTopLevelItems/)
method from the [Billing_Invoice](https://softlayer.github.io/reference/services/SoftLayer_Billing_Invoice) class to obtain the list of top level items being billed on the invoice specified.

```python
for invoice in InvoiceList:
    topLevelItems = client['Billing_Invoice'].getInvoiceTopLevelItems(id=invoice['id'])    
    print (topLevelItems)
```

## Access sub item details

If additional billing detail is desired for topLevelItems, many items have associated children which have billing details
that make up to the top level item such as memory, storage, or disk.   To access, the details use  [getNonZeroAssociatedChildren](https://softlayer.github.io/reference/services/SoftLayer_Billing_Invoice_Item/getNonZeroAssociatedChildren) method in the [Billing_Invoice_Item](https://softlayer.github.io/reference/services/SoftLayer_Billing_Invoice_Item)
class, by passing the id received from the getInvoiceTopLevelItems call.  The method only returns those associated children with a non-zero cost.

```python
nonZeroAssociatedChildren = client['Billing_Invoice_Item'].getNonZeroAssociatedChildren(id=topLevelItemId)
```
## Sample script

The following sample script creates a .csv file of all the billing level detail for each owned sub account for the dates specified.

```python
import SoftLayer, argparse, csv,logging,time
from datetime import datetime
import dateutil.parser

def getDescription(categoryCode, detail):
    for item in detail:
        if 'categoryCode' in item:
            if item['categoryCode']==categoryCode:
                return item['description']
    return "Not Found"

client = SoftLayer.Client()

startDate = '2018-07-01T00:00:00'
endDate = '2018-07-31T23:59:59'
outputname = 'billing-export.csv'


## OPEN CSV FILE FOR OUTPUT
outfile = open(outputname, 'w')
csvwriter = csv.writer(outfile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

fieldnames = ['Invoice_Date', 'Account_Id', 'Invoice_Number', 'BillingItemId', 'InstanceType', 'hostName', 'Category', 'Description',
             'Hours', 'Hourly_Rate', 'RecurringCharge', 'InvoiceTotal', 'InvoiceRecurring', 'Type']
csvwriter = csv.DictWriter(outfile, delimiter=',', fieldnames=fieldnames)
csvwriter.writerow(dict((fn, fn) for fn in fieldnames))


#
# GET LIST OF INVOICES FOR ALL BRAND OWNED ACCOUNTS
#
print("Looking up invoices for brand....")
ownedBrands = client['Account'].getObject(mask="ownedBrands.allOwnedAccounts.invoices")

# FILTER INVOICES FOR INVOICETYPE AND DATE RANGE REQUESTED

invoiceType = "RECURRING"
invoiceList=[]

for brand in ownedBrands['ownedBrands']:
    for account in brand['allOwnedAccounts']:
        for invoice in account['invoices']:
            invoiceCreateDate = invoice['createDate']
            if (invoice['typeCode'] == invoiceType) \
                    and (dateutil.parser.parse(invoiceCreateDate) > dateutil.parser.parse(startDate)
                         and dateutil.parser.parse(invoiceCreateDate) < dateutil.parser.parse(endDate)):
                invoiceInfo = client['Billing_Invoice'].getObject(id=invoice['id'],
                    mask="id,createDate,typeCode,invoiceTotalAmount,invoiceTotalRecurringAmount,invoiceTopLevelItemCount")
                invoiceList.append(invoiceInfo)


## OBTAIN TOP LEVEL DETAIL FROM EACH INVOICE

print ()
print ('{:<35} {:<15} {:<15} {:>8} {:>16} {:>16} {:>16} {:<15}'.format("Invoice Date /", "Account", "Invoice", " ", "Items", "Recurring Charge",  "Invoice Amount", "Type"))
print ('{:<35} {:<15} {:<15} {:>8} {:>16} {:>16} {:>16} {:<15}'.format("==============", "=======", "=======", " ", "=====", "================",  "==============", "===="))
for invoice in invoiceList:
    invoiceId = invoice['id']
    invoiceInfo = client['Billing_Invoice'].getObject(id=invoiceId,mask="accountId, id,createDate,typeCode,invoiceTotalAmount,invoiceTotalRecurringAmount,invoiceTopLevelItemCount")
    accountId = invoiceInfo['accountId']
    invoiceDate = invoiceInfo['createDate'][0:10]
    invoiceTotalAmount = float(invoiceInfo['invoiceTotalAmount'])
    invoiceTotalRecurringAmount = float(invoiceInfo['invoiceTotalRecurringAmount'])
    invoiceType = invoiceInfo['typeCode']
    totalItems=invoiceInfo['invoiceTopLevelItemCount']

    # PRINT INVOICE SUMMARY LINE
    print('{:35} {:<15} {:<15} {:>8} {:>16} {:>16,.2f} {:>16,.2f} {:<15}'.format(invoiceDate,
                                                                          accountId, invoiceId, " ",
                                                                          totalItems,
                                                                          invoiceTotalAmount,
                                                                          invoiceTotalRecurringAmount, invoiceType))

    limit = 10 ## set limit of record t
    for offset in range(0,totalItems,limit):
        #print ("Lookup at Offset %s" % offset)
        time.sleep(1)
        Billing_Invoice = client['Billing_Invoice'].getInvoiceTopLevelItems(id=invoiceId, limit=limit, offset=offset,
                                mask='id, billingItemId, categoryCode, hostName, domainName, description, createDate, totalRecurringAmount,hourlyRecurringFee')
        count=0
        # ITERATE THROUGH DETAIL
        for item in Billing_Invoice:
            billingItemId = item['billingItemId']
            category = item["categoryCode"]

            if 'hostName' in item:
                hostName = item['hostName']+"."+item['domainName']
            else:
                hostName = "Unnamed Device"

            recurringFee = float(item['totalRecurringAmount'])

            #IF Monthly calculate hourly rate and total hours
            if 'hourlyRecurringFee' in item:
                instanceType = "Hourly"
                associated_children=""
                while associated_children is "":
                    try:
                        time.sleep(0.5)
                        associated_children = client['Billing_Invoice_Item'].getNonZeroAssociatedChildren(id=item['id'],mask="hourlyRecurringFee")
                    except SoftLayer.SoftLayerAPIError as e:
                        logging.warning("getNonZeroAssociatedChildren(): %s, %s" % (e.faultCode, e.faultString))
                        time.sleep(5)
                #calculate total hourlyRecurringFree from associated childrent

                hourlyRecurringFee = float(item['hourlyRecurringFee']) + sum(float(child['hourlyRecurringFee']) for child in associated_children)
                if hourlyRecurringFee > 0:
                    hours = round(float(recurringFee) / hourlyRecurringFee)
                else:
                    hours=0
            else:
                instanceType = "Monthly/Other"
                hourlyRecurringFee = 0
                hours = 0

            if category=="storage_service_enterprise" or category=="performance_storage_iscsi":
                billing_detail=""
                while billing_detail is "":
                    try:
                        time.sleep(1)
                        billing_detail = client['Billing_Invoice_Item'].getChildren(id=item['id'], mask="description,categoryCode,product")
                    except SoftLayer.SoftLayerAPIError as e:
                        logging.warning("%s, %s" % (e.faultCode, e.faultString))

                if category=="storage_service_enterprise":
                    iops=getDescription("storage_tier_level", billing_detail)
                    storage=getDescription("performance_storage_space",billing_detail)
                    snapshot=getDescription("storage_snapshot_space", billing_detail)
                    if snapshot=="Not Found":
                        description=storage+" "+iops+" "
                    else:
                        description=storage+" "+iops+" with "+snapshot
                else:
                    iops=getDescription("performance_storage_iops", billing_detail)
                    storage=getDescription("performance_storage_space", billing_detail)
                    description=storage+" "+iops
            else:
                description=item['description']
                description = description.replace('\n', " ")
            # BUILD CSV OUTPUT & WRITE ROW
            row = {'Invoice_Date': invoiceDate,
                   'Account_Id': accountId,
                   'Invoice_Number': invoiceId,
                   'BillingItemId': billingItemId,
                   'InstanceType': instanceType,
                   'hostName': hostName,
                   'Category': category,
                   'Description': description,
                   'Hours': hours,
                   'Hourly_Rate': round(hourlyRecurringFee,3),
                   'RecurringCharge': round(recurringFee,2),
                   'InvoiceTotal': invoiceTotalAmount,
                   'InvoiceRecurring': invoiceTotalRecurringAmount,
                   'Type': invoiceType
                    }
            csvwriter.writerow(row)
            #print(row)
##close CSV File
outfile.close()
```