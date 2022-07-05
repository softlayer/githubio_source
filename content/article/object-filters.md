---
title: "Object-Filters"
description: "How Object Filters work"
date: "2015-06-02"
tags:
    - "article"
    - "sldn"
    - "objectfilter"
---





## Overview

<iframe width="100%" height="630" src="https://www.youtube.com/embed/LUSzSZSv_Fw"  frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Object filters can be used to limit the results returned by the API. They differ from objectMasks in that they determine which objects are returned while objectMasks define what properties to retrieve from the returned objects.

## Structure
An object filter is created by defining a property hierarchy through the relational and local properties. The property to be filtered will be a structure that represents the object filters conditional.

Each filter object will have at least an 'operation' property and may contain one or more 'options'. 

To pull a list of all virtual machines in the Dallas 5 datacenter we would start with SoftLayer_Account::getVirtualGuests. We will augment this call with an Object Filter to limit the objects returned to those in the Dallas 5 datacenter.

```python
object_filter = {
    # https://softlayer.github.io/reference/datatypes/SoftLayer_Account/#virtualGuests
    'virtualGuests': { 
        # https://softlayer.github.io/reference/datatypes/SoftLayer_Virtual_Guest/#datacenter
        'datacenter': { 
            # https://softlayer.github.io/reference/datatypes/SoftLayer_Location/#name
            'name': {'operation': 'dal05'} 
        }
    }
}
```

*NOTE* objectFilters generally start at the Service's datatype, which is why the SoftLayer_Account::getVirtualGuests's objectFilter starts with the 'virtualGuests' property, and not the datacenter property.

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


An objectFilter can have multiple operations as well.

```python
object_filter = {
    'virtualGuests': {
        'datacenter': {
            'name': {'operation': '!=dal05'}
        }, 
        'domain': {
            'operation': 'test.com'
        }
    }
}
```

## Operations
An operation is the conditional added to the Object Filter to define what Data Type objects will be returned by the API. 

## Literal Operators
+ `value` - Checks that the column matches value
+ `!= value` - Checks that the column does not match value
+ `> value` - Checks that the column is greater than value
+ `>= value` - Checks that the column is greater than or equal to value
+ `< value` - Checks that the column is less than value
+ `<= value` - Checks that the column is less than or equal to value
+ `^= value` - Checks that the column starts with value
+ `!^= value` - Checks that the column does not start with value
+ `$= value` - Checks that the column ends with value
+ `!$= value` - Checks that the column does not end with value
+ `*= value` - Checks that the column contains value
+ `!*= value` - Checks that the column does not contain with value
+ `_= value` - Checks that the lowercased column equals value
+ `~ value` - Checks that the column matches the regular expression value
+ `!~ value` - Checks that the column does not match the regular expression value
+ `not null` - Checks that the column is not null
+ `is null` - Checks that the column is null


## Advanced Operators
Some Object Filters require `options` to be passed in addition the operation. Options are passed as an array of json objects.

*WARNING* If you don't properly define these operators, the API tends to just ignore the filter and return the normal results. 

### IN, NOT IN
The in operation can be used to require the column to match only one of the values. For example:

```python
object_filter = {
    'virtualGuests': {
        'datacenter': {
            'name': {
                'operation': 'in', 
                'options': [{
                    'name': 'data',
                    'value': ['dal09', 'tor01']
                }]
            }
        }
    }
}
```

### OR
There is also an or operation but the in version is recommended when it can be used. Unlike the in operation, the or operation supports literal operators in the values and should therefore be used when needing more than just normal equality. For example

```python
_filter = {
    'virtualGuests': {
        'datacenter': {
            'name': {
                'operation': 'or', 
                'options': [{
                    'name': 'data',
                    'value': ['^= tor', '^= sjc']
                }]
            }
        }
    }
}
```


### AND
The and operation lets a column match multiple possibilities. For example this will get all virtualGuests with maxMemory between 1G and 16G

```python
_filter = {
    'virtualGuests': {
        'maxMemory': {
            'operation': 'and', 
            'options': [{
                'name': 'data',
                'value': ['>= 1024', '<= 16384']
            }]
        }
    }
}
```


## Date filters
Date filters need to be used on fields that contain a date object. Usually the date string format is in the `MM/DD/YYYY HH24:MI:SS` form (using Oracle notation here), usually. If your filter isn't working, try matching the date format to the format returned by the API.

### X days past
A simple way to get dates a few days in the past is this format.

    operation = '>= currentDate - 30'

alternatively 

    'operation': '> sysdate - 30'

```python
_filter = {
    'virtualGuests': {
        'provisionDate': {
            'operation': '> sysdate - 30'
        }
    }
}
```

### Exact Date
    operation = 'isDate'
    options = [{
        'name': 'date',
        'value': ['01/01/01']
        }
    ]

### Date Before Value
    operation = 'lessThanDate'
    options = [{
        'name': 'date',
        'value: ['01/01/01']
        }
    ]

### Date After Value
    operation = 'greaterThanDate'
    options = [{
        'name': 'date',
        'value: ['01/01/01']
        }
    ]

### Between Dates
    operation = 'betweenDate'
    options = [{
        'name': 'startDate',
        'value: ['01/01/2015']
        },
        {
        'name': 'endDate',
        'value': ['01/31/2015]
        }
    ]


## Sorting
The sort option accepts an array. ASC or DESC can be provided to set the sort direction. Since a query can contain many orderBy options, the API allows the developer to set the precedence with a sortOrder option which takes a single-value array of an integer. The lower integer has higher sort priority.  This example will sort the virtual guests by `maxMemory` ASC, then by `provisionDate` DESC.

It is not possible to SORT and SEARCH on the same property.

```python
_filter = {
    'virtualGuests': {
        'provisionDate': {
            'operation': 'orderBy',
            'options': [{
                'name': 'sort',
                'value': ['DESC']
            }, {
                'name': 'sortOrder',
                'value': [1]
            }]
        },
        'maxMemory': {
            'operation': 'orderBy',
            'options': [{
                'name': 'sort',
                'value': ['ASC']
            }, {
                'name': 'sortOrder',
                'value': [0]
            }]
        },
    }
}
```

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