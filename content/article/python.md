---
title: "The SoftLayer Python Library"
description: "Covers using the softlayer-python project to interact with the SoftLayer API, along with how to use the `slcli`, a command line tool, which is bundled with the softlayer-python library"
date: "2021-08-10"
tags:
    - "tools"
    - "slcli"
    - "article"
    - "python"
---


## The Basics

- [softlayer-python](https://github.com/softlayer/softlayer-python) project homepage. For source code and submitting issues.
- [Documentation](https://softlayer-python.readthedocs.io/en/latest/) Covers both the SLCLI and softlayer-python library.
- [PyPi project](https://pypi.org/project/SoftLayer/) For latest information about the softlayer-python package, which is kept updated on PyPi.


#### <font color=red>Python 2.7 Support</font>
As of version 5.8.0 SoftLayer-Python will no longer support python2.7, which is [End Of Life as of 2020](https://www.python.org/dev/peps/pep-0373/) . If you cannot install python 3.6+ for some reason, you will need to use a version of softlayer-python <= 5.7.2

--------------

## Authentication

When making API calls in python, you will first create an instance of the [SoftLayer Client class](https://github.com/softlayer/softlayer-python/blob/master/SoftLayer/API.py#L155). This client object is responsible for all the communication with the SoftLayer API server. 

The first step for setting up a client is getting authentication information, and there are several ways to do this.

To get started, we will assume you are setting up your code something like this:

```python
import SoftLayer
# This is nice for printing out results from the API as raw JSON
from pprint import pprint as pp 

client = SoftLayer.create_client_from_env()
```

#### [The ~/.softlayer config](#softlayer-config) {#softlayer-config .anchor-link}

By default,  [`SoftLayer.create_client_from_env()`](https://github.com/softlayer/softlayer-python/blob/master/SoftLayer/API.py#L50) will read in the configuration from a file in your home directory called `~/.softlayer` ( and `~/AppData/Roaming/softlayer` on Windows)

This file can be setup manually with the `slcli config setup` command, or if you already know what the config should be, this file can be set up by copying over a known good configuration.

Listed below is an example config file, with comments and optional settings.

```bash
$ cat ~/.softlayer
[softlayer]
username = SLUserName
api_key = 64CharacterLongApiKeyGoesHere

# For IBMCloud ApiKeys
# https://sldn.softlayer.com/article/authenticating-softlayer-api/#cloud-api
# username = apikey
# api_key = 32CharacterLongKey

# Both rest and xmlrpc will work with this client
# however the format of the request, and output of any logging/debugging 
# information will change based on this.
endpoint_url = https://api.softlayer.com/rest/v3.1
#endpoint_url = https://api.softlayer.com/xmlrpc/v3.1

# Set to a number to stop waiting after that many seconds
timeout = 0

# If you need to proxy requests through something
# proxy = 'http://somehost'
```


#### [Environment Variables](#softlayer-environment) {#softlayer-environment .anchor-link}

You can also use the following environment variables to control authentication.

- `https_proxy`: For anyone needing to proxy requests through a middle server
- `SL_USERNAME`: `username` in the config
- `SL_API_KEY`: `api_key` in the config


#### Setting during client creation

You can of course set these variables when you are creating the client itself as well.

```python
client = SoftLayer.create_client_from_env(
    username='SL_USERNAME', api_key="64CharacterLongAPiKey"
)
```

See [SoftLayer.create_client_from_env()](https://softlayer-python.readthedocs.io/en/latest/api/client/#SoftLayer.create_client_from_env) for a full list of parameters. 

The only ones that are not checked for in the config are 

- `config_file`: which will just tell the client to read from a non-default location
- `user_agent`: Make API calls with a non-standard user_agent. Can be somewhat useful if you want your API calls to have some style in our API logs.
- `transport `: Useful if you want to use a debugging transport, or maybe some special modified transport.
- `verify`: which will prevent SSL verification checks. Don't turn this off unless you mean to.

--------------

## [Making API Calls](#making-api-calls) {#making-api-calls .anchor-link}

Now that the client is setup, we are able to make API calls and get data back.


#### [client.call](#client-call) {#client-call .anchor-link}

`client.call()` is generally what you should use to interact with the API. The [client.call() documentation](https://softlayer-python.readthedocs.io/en/latest/api/client/#SoftLayer.BaseClient.call) has a full listing of all the supported parameters, but the basic syntax is as follows:

```python
result = client.call('SoftLayer_Account', 'getObject')
pp(result)
```
[Making API Calls](https://softlayer-python.readthedocs.io/en/latest/api/client/#making-api-calls) has some more examples of how to use this method if needed.

#### [client.iter_call](#client-itercall) {#client-itercall .anchor-link}

[client.iter_call()](https://softlayer-python.readthedocs.io/en/latest/api/client/#SoftLayer.BaseClient.iter_call) is useful if you want to iterate over a large return set from the API. It takes the same arguments as `client.call()`, however this method will return a [Python Generator](https://wiki.python.org/moin/Generators) and only make API calls to get more data when you read the end of the current data set.

For example, the following code will first get all virtual guests on the account, THEN lookup information on each of them in turn.

```python

virtualGuests = client.call('SoftLayer_Account', 'getVirtualGuests', mask="mask[id]", iter=True)
for guest in virtualGuest:
    guestInfo = client.call('SoftLayer_Virtual_Guest', 'getObject', id=guest.get('id'))
    pp(guestInfo)
```

However the following code will get virtual guests in batches of 10, get the info on each, then get the next batch of 10. This will continue until the client gets less than 10 results back

```python
virtualGuests = client.iter_call('SoftLayer_Account', 'getVirtualGuests', mask="mask[id]", limit=10)
for guest in virtualGuest:
    guestInfo = client.call('SoftLayer_Virtual_Guest', 'getObject', id=guest.get('id'))
    pp(guestInfo)
```
This is mostly useful when getting all the results back from the API might take a very long time, and you want to do something in between API calls.

#### Service.call()

This is an older form of making API calls and you may see it in some examples occasionally. It is supported, but if you are writing new code you should use `client.call()`

The basic format for this type is like this:

```python
client['SoftLayer_Account'].getObject()
```

The parameters you pass into that method are the same as `client.call()`, it is basically just formatted different.

#### [Method Parameters](#method-parameters) (#method-parameters .anchor-link)

If a specific method takes input parameters, for example [SoftLayer_Dns_Domain::createARecord()](/reference/services/SoftLayer_Dns_Domain/createARecord/) takes 3 parameters (host, data, ttl). You specify these parameters as function parameters to `client.call()`. 

><font color=red>NOTE: </font> Parameters are specified in the order they appear in the documentation. They are NOT specified by name.

```python
domain_id = 123456
try:
    new_record = client.call('SoftLayer_Dns_Domain', 'createARecord', 'newHost', '1.2.3.4', '6000', id=domain_id)
    pp(new_record)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to create domain\nError: {}".format(e))
```

#### [Object Masks](#object-masks) {#object-masks .anchor-link}

[Object Masks](https://sldn.softlayer.com/article/object-masks/) are a complex concept of the API, but setting them is straightforward.

The basics is that it should be a string, starting with `mask[` and ending with `]`, and between should be the list of properties you want to get back from the API. If you want to select propertyX of a property1, propertyX needs to be enclosed in `[]` and the end of property1, like this:

```python
mask = "mask[id, hostname, backendRouters[hostname]]"
guests = client.call('SoftLayer_Account', 'getVirtualGuests', mask=mask)
for guest in guests:
    pp(guest)
```

#### [Object Filters](#object-filters) {#object-filters .anchor-link}

[Object Filters](https://sldn.softlayer.com/article/object-filters/) are another critical API concept. In this case you would specify them as a Python nested dictionary.

```python
_filter = {"virtualGuests": {"hostname": {"operation": "testHost"}}}
guests = client.call('SoftLayer_Account', 'getVirtualGuests', filter=_filter)
for guest in guests:
    pp(guest)
```

#### [Result Limits and Pagination](#result-limits) {#result-limits .anchor-link}

You can automatically paginate API requests by using the `iter=True` parameter of `client.call()`, or by using `client.iter_call()` directly.  If you want to control pagination yourself you can use the `offset` and `limit` paramters.

> API results are not guaranteed to be in order from one API call to another, so if you do pagination, make sure to use an OrderBy Object Filter on some unique property

```python
from SoftLayer import utils

_filter = {"virtualGuests": {"id": utils.query_filter_orderby()}
guests = client.call('SoftLayer_Account', 'getVirtualGuests', filter=_filter, limit=10, offset=0)
for guest in guests:
    pp(guest)
```

#### [Error Handling](#error-handling) {#error-handling .anchor-link}

[SoftLayer.Exceptions](https://github.com/softlayer/softlayer-python/blob/master/SoftLayer/exceptions.py) has a few defined Exceptions for handling API related errors.

```python
try:
    account = client.call('SoftLayer_Account', 'getObject')
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve account information faultCode={}, faultString={}".format(e.faultCode, e.faultString)

```

--------------

## [Advanced Usage](#advanced-usage) {#advanced-usage .anchor-link}

#### Retry Decorator
The [Retry Decorator](https://github.com/softlayer/softlayer-python/blob/master/SoftLayer/decoration.py#L21) is a [Python Decorator](https://www.python.org/dev/peps/pep-0318/) that will automatically retry an API call based on a few types of API issues.

The [virtual guest manager](https://github.com/softlayer/softlayer-python/blob/master/SoftLayer/managers/vs.py) has a few good examples of this in practice

```python
import logging
from SoftLayer.decoration import retry

LOGGER = logging.getLogger(__name__)


@retry(logger=LOGGER)
def listGuests():
    return client.call('Account', 'getVirtualGuests')
```

If during this API call we get one of the following exceptions, the code will automatically retry after waiting a little bit.
```python
    exceptions.ServerError,
    exceptions.ApplicationError,
    exceptions.RemoteSystemError,
```

#### Debugging

The Client object keeps track of all API calls made, and has a handy feature to be able to print them out in a raw format that doesn't rely on the SoftLayer library.

If you are using the XMLRPC endpoint, this will result it a bit of python code that will directly use the requests library to send in the API call and show the payload it is sending.

The REST endpoint though will print out a nice CURL command that is nice and copy-pasteable.

[Debugging Documentation](https://softlayer-python.readthedocs.io/en/latest/api/client/#debugging) has the steps needed to set up the debugger and print out the API calls.

--------------

## [Managers](#managers) {#managers .anchor-link}

The [Managers](https://softlayer-python.readthedocs.io/en/latest/api/client/#managers) are a collection of helper classes to make dealing with some of the more complex portions of the API a lot easier. 

While it is not required to use them, they can serve as a good example to build off from. Most of the managers were designed for use with the CLI, but of note is the [Ordering Manager](https://softlayer-python.readthedocs.io/en/latest/api/managers/ordering/) which can help take a lot of the complexity out of creating orders.


```python
from SoftLayer.managers import ordering

manager = ordering.OrderingManager(client)
# This just excludes all non-classic infrastructure packages
_filter = {'type': {'keyName': {'operation': '!= BLUEMIX_SERVICE'}}}
packages = manager.list_packages(filter = _filter)
print("Id, KeyName")
for package in packages:
    print("{}, {}".format(package.get('id'),package.get('keyName'))
```

--------------

## [Utilities](#utilities) {#utilities .anchor-link}

The [SoftLayer.utils](https://github.com/softlayer/softlayer-python/blob/master/SoftLayer/utils.py) section has a variety of functions that can make your life easier as well. Noteably the `query_filter` type functions can help format Object Filters properly and take a lot of the guess working out of the more complex filters.


```python
from SoftLayer import utils

_filter = {"virtualGuests": {"hostname": utils.query_filter_orderby()}
guestsByHostname = client.call('SoftLayer_Account', 'getVirtualGuests', filter=_filter)
for guest in guestsByHostname:
    pp(guest)
```

--------------

## [SLCLI](#slcli) {#slcli .anchor-link}

The [slcli](https://softlayer-python.readthedocs.io/en/latest/cli_directory/) command is included as part of the softlayer-python package. It contains a lot of prebuilt functionality that you can also find in the web portal, although some formats and outputs will be different of course. 

It is a sister program of the [`ibmcloud sl`](https://cloud.ibm.com/docs/cli?topic=cli-sl-all-api) command, but a different code base. The two strive to have the same functionality, but some differences do exist, so be aware of which one you are using.

--------------

## Further Reading

- [SLDN Python Library](https://sldn.softlayer.com/python/)
- [SoftLayer-Python Project Homepage](https://github.com/softlayer/softlayer-python)
- [IBMCloud CLI](https://cloud.ibm.com/docs/cli?topic=cli-getting-started)
- [SLCLI Command Directory](https://softlayer-python.readthedocs.io/en/latest/cli_directory/)
- [SLCLI Change Log](https://github.com/softlayer/softlayer-python/blob/master/CHANGELOG.md)
- [softlayer-python Versions](https://github.com/softlayer/softlayer-python/releases)
