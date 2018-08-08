---
title: "Single Account Billing Detail"
description: "This tutorial walks you through accessing detailed billing data for a single specified account using a specified time and date range"
date: "2018-08-08"
tags:
    - "article"
    - "sldn"
    - "python"
---

# Account Level Billing

This tutorial walks you through accessing detailed billing data for a single specified account using a specified time and date range.

## Objectives

* Understand how to use multiple API services and methods to access detailed billing data for a specified account using a specified time and date range.

## Services used

This tutorial uses the following technologies:
* [SoftLayer Python Library](http://softlayer-python.readthedocs.io/en/latest/)
* [Billing_Invoice Service](https://softlayer.github.io/reference/services/SoftLayer_Billing_Invoice/)
* [Billing_Invoice_Item Service](https://softlayer.github.io/reference/services/SoftLayer_Billing_Invoice_Item/)
* [Billing_item Service](https://softlayer.github.io/reference/services/SoftLayer_Billing_Item/)

## Architecture

This tutorial will leverage account Invoice and Billing Item API's to collect and display detailed billing detail for a specified time and date range.

## Install SoftLayer Python Library
* [SoftLayer API Python Client Installation](https://github.com/softlayer/softlayer-python/blob/master/README.rst)

## Identify and access invoices for specified date range
Start by accessing invoices using the [getInvoices](https://softlayer.github.io/reference/services/SoftLayer_Account/getInvoices/) method for specified account using the invoice type and date range filter. 

Their are several types of invoices which can be requested, for this example the typical type would be the "RECURRING" type, which includes all the monthly recurring and hourly usage charges incurred by the specified account.

* "NEW" typeCode signifies an invoice for new service. 
* "RECURRING" invoices are generated on an accounts anniversary billing date for monthly services.
* "ONE-TIME-CHARGE" invoices are generated when one-time charges are applied to an account.
* "CREDIT" invoices are generated whenever IBM applies a credit against an account's balance. 

The date and time range is specified using the format of "YYYY/MM/DD HH:MM:SS".

```python
InvoiceList = client['Account'].getInvoices(filter={
        'invoices': {
            'createDate': {
                'operation': 'betweenDate',
                'options': [
                     {'name': 'startDate', 'value': [startdate+" 0:0:0"]},
                     {'name': 'endDate', 'value': [enddate+" 23:59:59"]}
                ]
            },
            'typeCode': {
                'operation': 'in',
                'options': [
                    {'name': 'data', 'value': ['RECURRING']}
                ]
            },
            }})  
```


## Access invoice detail
Using the list of invoices returned, use the [getInvoiceTopLevelItems](https://softlayer.github.io/reference/services/SoftLayer_Billing_Invoice/getInvoiceTopLevelItems/) method from the [Billing_Invoice](https://softlayer.github.io/reference/services/SoftLayer_Billing_Invoice) class to obtain the list of top level items being billed on the invoice specified.

```python
topLevelItems = client['Billing_Invoice'].getInvoiceTopLevelItems(id=invoiceId)
```

## Access sub item details

If additional billing detail is desired, many items have associated children which have billing details associated with them such as memory, storage, or disk.   To access, the [getNonZeroAssociatedChildren](https://softlayer.github.io/reference/services/SoftLayer_Billing_Invoice_Item/getNonZeroAssociatedChildren) method in the [Billing_Invoice_Item](https://softlayer.github.io/reference/services/SoftLayer_Billing_Invoice_Item) class is used by passing the id received from the getInvoiceTopLevelItems call.

```python
nonZeroAssociatedChildren = client['Billing_Invoice_Item'].getNonZeroAssociatedChildren(id=topLevelItemId)
```
## Sample script

The following sample script creates a .csv file of all the billing level detail for an account.

```python
import SoftLayer, configparser, argparse, csv,logging,time

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

#
# GET LIST OF INVOICES
#

outfile = open(outputname, 'w')
csvwriter = csv.writer(outfile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

fieldnames = ['Invoice_Date', 'Invoice_Number', 'BillingItemId', 'InstanceType', 'hostName', 'Category', 'Description',
             'Hours', 'Hourly_Rate', 'RecurringCharge', 'InvoiceTotal', 'InvoiceRecurring', 'Type']
csvwriter = csv.DictWriter(outfile, delimiter=',', fieldnames=fieldnames)
csvwriter.writerow(dict((fn, fn) for fn in fieldnames))

## OPEN CSV FILE FOR OUTPUT
print("Looking up invoices....")

# Build Filter for Invoices
InvoiceList = client['Account'].getInvoices(filter={
        'invoices': {
            'createDate': {
                'operation': 'betweenDate',
                'options': [
                     {'name': 'startDate', 'value': [startdate+" 0:0:0"]},
                     {'name': 'endDate', 'value': [enddate+" 23:59:59"]}

                ]
            },
            'typeCode': {
                'operation': 'in',
                'options': [
                    {'name': 'data', 'value': ['RECURRING']}
                ]
                },
                    }
        })


print ()
print ('{:<35} {:<30} {:>8} {:>16} {:>16} {:>16} {:<15}'.format("Invoice Date /", "Invoice Number /", " ", "Items", "Recurring Charge",  "Invoice Amount", "Type"))
print ('{:<35} {:<30} {:>8} {:>16} {:>16} {:>16} {:<15}'.format("==============", "================", " ", "=====", "================",  "==============", "===="))
for invoice in InvoiceList:
    invoiceID = invoice['id']
    invoiceInfo = client['Billing_Invoice'].getObject(id=invoiceID,mask="id,createDate,typeCode,invoiceTotalAmount,invoiceTotalRecurringAmount,invoiceTopLevelItemCount")
    invoiceDate = invoiceInfo['createDate'][0:10]
    invoiceTotalAmount = float(invoiceInfo['invoiceTotalAmount'])
    invoiceTotalRecurringAmount = float(invoiceInfo['invoiceTotalRecurringAmount'])
    invoiceType = invoiceInfo['typeCode']
    totalItems=invoiceInfo['invoiceTopLevelItemCount']

    # PRINT INVOICE SUMMARY LINE
    print('{:35} {:<30} {:>8} {:>16} {:>16,.2f} {:>16,.2f} {:<15}'.format(invoiceDate,
                                                                          invoiceInfo['id'], " ",
                                                                          totalItems,
                                                                          invoiceTotalAmount,
                                                                          invoiceTotalRecurringAmount, invoiceType))

    limit = 10 ## set limit of record t
    for offset in range(0,totalItems,limit):
        print ("Lookup at Offset %s" % offset)
        time.sleep(1)
        Billing_Invoice = client['Billing_Invoice'].getInvoiceTopLevelItems(id=invoiceID, limit=limit, offset=offset,
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
                   'Invoice_Number': invoiceID,
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
            print(row)
##close CSV File
outfile.close()
```