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

This sample script is provided as a convienience, you may need to modify some of the data it outputs for your needs.

It should though gather RECURRING invoices from the time specified, and show you all the top level items and their charges.

```python
#!python

import SoftLayer
import csv
import logging
import time
import click
import datetime
from prettytable import PrettyTable


def getDescription(categoryCode, detail):
    for item in detail:
        if 'categoryCode' in item:
            if item['categoryCode']==categoryCode:
                return item['description']
    return "Not Found"

class invoices():

    def __init__(self, start, end):
        """
        :param int start: epoch time to start at. Should align to 00:00 UTC
        :param int end: epoch time to end at. Should align to 00:00 UTC
        """
        self.client = SoftLayer.Client()
        # Uncomment these lines for the debugger to print API calls.
        # This script makes quite a few API calls, so this is commented out to not spam the console.
        # debugger = SoftLayer.DebugTransport(self.client.transport)
        # self.client.transport = debugger
        self.start = start
        self.end = end

    def debug(self):
        """Useful for seeing what actual API calls were being made"""
        for call in self.client.transport.get_last_calls():
            print(self.client.transport.print_reproduceable(call))

    def main(self):
        """Gets invoices, and parses them into a list data structure"""
        invoice_rows = []
        invoices = self.invoices()
        print('{:<35} {:<30} {:>8} {:>16} {:>16} {:>16} {:<15}'.format(
            "Invoice Date /", "Invoice Number /", " ", "Items", "Recurring Charge",  "Invoice Amount", "Type"))
        print('{:<35} {:<30} {:>8} {:>16} {:>16} {:>16} {:<15}'.format(
            "==============", "================", " ", "=====", "================",  "==============", "===="))
        for invoice in invoices:
            invoice_rows.append(self.parse_invoice(invoice))
        return invoice_rows

    def invoices(self):
        """Gets all the RECURRING invoice between the specified start and end dates"""
        _filter = {
            'invoices': {
                'createDate': {
                    'operation': 'betweenDate',
                    'options': [
                         {'name': 'startDate', 'value': [self.start]},
                         {'name': 'endDate', 'value': [self.end]}
                    ]
                },
                'typeCode': {'operation': 'RECURRING'}
            }
        }
        invoiceMask = "mask[id]"
        # As some invoices may have a lot of items, we only get the ID here, and break our API calls up
        invoices = self.client.call('SoftLayer_Account', 'getInvoices', filter=_filter, iter=True, mask=invoiceMask)
        return invoices

    def parse_invoice(self, invoice):
        invoiceMask = "mask[id, createDate, typeCode, invoiceTotalAmount, invoiceTotalRecurringAmount]"
        itemMask = """mask[id, billingItemId, categoryCode, hostName, domainName, description, createDate, 
                           totalRecurringAmount, hourlyRecurringFee]"""
        invoiceID = invoice['id']

        # Gets some basic information about the invoice.
        invoiceInfo = self.client.call('SoftLayer_Billing_Invoice', 'getObject', id=invoiceID, mask=invoiceMask)

        invoiceDate = invoiceInfo['createDate'][0:10] # Just the YYYY-MM-DD part
        invoiceTotalAmount = float(invoiceInfo['invoiceTotalAmount'])
        invoiceTotalRecurringAmount = float(invoiceInfo['invoiceTotalRecurringAmount'])
        invoiceType = invoiceInfo['typeCode']

        # Gets all the actual Items on the invoice. `iter=True` here will automatically page through the items
        items = self.client.call('SoftLayer_Billing_Invoice', 'getInvoiceTopLevelItems', id=invoiceID, 
                                 mask=itemMask, iter=True)
        print('{:35} {:<30} {:>8} {:>16} {:>16,.2f} {:>16,.2f} {:<15}'.format(
            invoiceDate, invoiceInfo['id'], " ", len(items), invoiceTotalAmount, invoiceTotalRecurringAmount, invoiceType))

        invoice_rows = []
        for item in items:
            invoice_rows.append(self.parse_item(item, invoiceInfo))
        return invoice_rows

    def parse_item(self, item, invoiceInfo):
        billingItemId = item['billingItemId']
        category = item["categoryCode"]
        invoiceID = invoiceInfo['id']
        invoiceDate = invoiceInfo['createDate'][0:10] # Just the YYYY-MM-DD part
        invoiceTotalAmount = float(invoiceInfo['invoiceTotalAmount'])
        invoiceTotalRecurringAmount = float(invoiceInfo['invoiceTotalRecurringAmount'])
        invoiceType = invoiceInfo['typeCode']

        childrenMask ="""mask[id, categoryCode, hourlyRecurringFee, recurringFee, description, product]"""
        if 'hostName' in item:
            hostName = item.get('hostName')+"."+item.get('domainName', 'NONE!')
        else:
            hostName = "Unnamed Device"

        recurringFee = float(item['totalRecurringAmount'])

        #IF Monthly calculate hourly rate and total hours
        if 'hourlyRecurringFee' in item:
            instanceType = "Hourly"
            associated_children = []

            try:
                # Check associated children, as the top item might not have all relevant charges
                associated_children = self.client.call('Billing_Invoice_Item', 'getNonZeroAssociatedChildren',
                                                        id=item['id'], mask=childrenMask)
            except SoftLayer.SoftLayerAPIError as e:
                logging.warning("getNonZeroAssociatedChildren(): %s, %s" % (e.faultCode, e.faultString))
            #calculate total hourlyRecurringFree from associated childrent
            # pp(associated_children)
            hourlyRecurringFee = float(item.get('hourlyRecurringFee', 0.0))
            for child in associated_children:
                hourlyRecurringFee = hourlyRecurringFee +  float(child.get('hourlyRecurringFee',0.0) )

            if hourlyRecurringFee > 0:
                hours = round(float(recurringFee) / hourlyRecurringFee)
            else:
                hours=0
        else:
            instanceType = "Monthly"
            hourlyRecurringFee = 0
            hours = 0

        if category=="storage_service_enterprise" or category=="performance_storage_iscsi":
            billing_detail= []
            try:
                # Check children, as the top item might not have all relevant charges
                billing_detail = self.client.call('Billing_Invoice_Item', 'getChildren',
                                                  id=item['id'], mask=childrenMask)
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
        row = {'Date': invoiceDate,
               'Invoice': invoiceID,
               'ItemId': billingItemId,
               'Billing': instanceType,
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
        return row

    def print_rows(self, invoices):
        table = PrettyTable()
        fields = self.get_filed_names()
        table.field_names  = fields
        table.align = "l"
        for invoice in invoices:
            for row in invoice:
                # Maps the row into a table
                table.add_row([row[entry] for entry in fields])
        print(table)

    def write_rows(self, invoices, filename):
        fieldnames = self.get_filed_names()

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for invoice in invoices:
                for row in invoice:
                    writer.writerow(row)

    def get_filed_names(self):
        fieldnames = ['Date', 'Invoice', 'ItemId', 'Billing', 'hostName', 
                     'Category', 'Description', 'Hours', 'Hourly_Rate', 'RecurringCharge',
                     'InvoiceTotal', 'InvoiceRecurring', 'Type']
        return fieldnames


@click.command()
@click.option('--start', default='2019-01-01', help='Start date, MM/DD/YYYY')
@click.option('--end', default='2019-02-01', help='End Date, MM/DD/YYYY')
@click.option('--filename', help="Name of the file you want to output to.")
def main(start, end, filename):
    print("MAIN FUNCTION")
    main = invoices(start, end)
    invoice_rows = main.main()

    main.print_rows(invoice_rows)
    if filename:
        main.write_rows(invoice_rows, filename)


if __name__ == "__main__":
    main()
```