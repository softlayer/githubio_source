---
title: "Object-Filters"
description: "How Object Filters work"
date: "2015-06-02"
tags:
    - "article"
    - "sldn"
    - "objectfilter"
---



Object filters can be used to limit the results returned by the API. They differ from object masks in that they determine what Data Type objects are returned while Object Masks define what properties to retrieve from the returned objects.

## Structure
An object filter is created by defining a property hierarchy through the relational and local properties. The property to be filtered will be a structure that represents the object filters conditional.

Each filter object will have at least an 'operation' property and may contain one or more 'options'. 

To pull a list of all virtual machines in the Dallas 5 datacenter we would start with SoftLayer_Account::getVirtualGuests. We will augment this call with an Object Filter to limit the objects returned to those in the Dallas 5 datacenter.

```python
    object_filter = {
        'virtualGuests': {
            'datacenter': {
                'name': {'operation': 'dal05'}
            }
        }
    }
```

We have given the target property a value of a json object with one element named `operation`. the operation element has a string value of `dal05`. The value of the operation element determines the conditional that will be used. The above is an example of the `Equals` conditional. 

The inverse of this example, pulling all virtual machines ***not*** in the Dallas 5 datacenter is accomplished by changing to the `NOT EQUAL` conditional.

```python
object_filter = {
    'virtualGuests': {
        'datacenter': {
            'name': {'operation': '!=dal05'}
        }
    }
}
```


## Operations
An operation is the conditional added to the Object Filter to define what Data Type objects will be returned by the API. 

## General Filters
### Equals
***Value can be int or string***

    operation = 'baz'
    operation = 1234

### Not Equal
***Value can be int or string***

    operation = '!= example string'
    operation = '!= 1234'

### Greater Than or Equal to
    operation = '>= 1234'

### Greater Than
    operation = '> 1234'

### Less Than or Equal to
    operation = '<= 1234'

### Less Than
    operation = '< 1234' 

### Not Null
    operation = 'not null'

### Is Null
    operation = 'is null' 

## String Filters
### Contains
    operation = '*= wibble wobble'

### Does not Contain
    operation = '!*= corge'

### Starts With
    operation = '^= qux'

### Ends With
    operation = '$= baz'

## Date filters
Some Object Filters require `options` to be passed in addition the operation. Options are passed as an array of json objects.

### X days past
    operation = '>= currentDate - 01/01/01'

### Exact Date
    operation = 'isDate'
    options = [{
        'name': 'date',
        'value': '01/01/01'
        }
    ]

### Date Before Value
    operation = 'lessThanDate'
    options = [{
        'name': 'date',
        'value: '01/01/01'
        }
    ]

### Date After Value
    operation = 'greaterThanDate'
    options = [{
        'name': 'date',
        'value: '01/01/01'
        }
    ]

### Between Dates
    operation = 'betweenDate'
    options = [{
        'name': 'startDate',
        'value: '01/01/01'
        },
        {
        'name': 'endDate',
        'value': '01/02/01
        }
    ]

## Regex Filters
### Like
    operation = '~ value'
### Not Like
    operation = '!~ value'

## Examples
### REST
#### List the ID and hostname of all servers in dal05

    https://api.softlayer.com/rest/v3/SoftLayer_Account/getVirtualGuests?objectMask=mask[id,hostname]&objectFilter={"datacenter":{"name":{"operation":"dal05"}}}

### Python
#### List all bare metal servers in spare pool

```python
hardware = client.call('Account', 'getHardware', filter={
    'hardware': {
        'sparePoolBillingItem': {
            'id' : {
                'operation': 'not null'
                }
            }
        }
    }
)
pprint.pprint(hardware)
```

### PHP
#### Retrieve the latest non $0 invoice

```php
$accountClient = SoftLayer_SoapClient::getClient('SoftLayer_Account', Null, $apiUser, $key);

$filter = new stdClass();
$filter->invoices = new stdClass();
$filter->invoices->amount = new stdClass();
$filter->invoices->amount->operation = 'not null';
$accountClient->setObjectFilter($filter);

$mask = "mask.id";
$accountClient->setObjectMask($mask);
$accountClient->setResultLimit(1,0);

$invoices = $accountClient->getInvoices();
print_r($invoices);
```

### Pull invoices between two dates
```php
$startDate = new DateTime('2012-04-03T13:05:25-06:00');
$endDate = new DateTime('2012-04-05T09:53:51-06:00');

$accountClient = SoftLayer_SoapClient::getClient('SoftLayer_Account', Null, $apiUser, $key);

$filter = new stdClass();
$filter->invoices = new stdClass();
$filter->invoices->createDate = new stdClass();
$filter->invoices->createDate->operation = 'betweenDate';
$filter->invoices->createDate->options = array();
$filter->invoices->createDate->options[0] = new stdClass();
$filter->invoices->createDate->options[0]->name = 'startDate';
$filter->invoices->createDate->options[0]->value = array($startDate->format('m/d/Y H:i:s'));
$filter->invoices->createDate->options[1] = new stdClass();
$filter->invoices->createDate->options[1]->name = 'endDate';
$filter->invoices->createDate->options[1]->value = array($endDate->format('m/d/Y H:i:s'));
$accountClient->setObjectFilter($filter);
$invoices = $accountClient->getInvoices();
 
print_r($invoices);
```