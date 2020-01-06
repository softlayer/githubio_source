---
title: "DNS management"
description: "How to manage DNS zones and records on SoftLayer's DNS system."
date: "2017-11-23"
classes: 
    - "SoftLayer_Dns_Domain"
tags:
    - "dns"
    - "rest"

---

This article will cover how to use the API to manage DNS zones and records. For a higher level documentation on how that all works, check out [DNS Management](https://cloud.ibm.com/docs/infrastructure/dns)


### Setup
All the functions defined in this article will be part of this `dnsManager` class. Which only sets up the SoftLayer Client, and configures the debugger, which allows you to see the exact API calls being made.

```
import SoftLayer
from pprint import pprint as pp

class dnsManager():

    def __init__(self):
        self.client = SoftLayer.Client()
        debugger = SoftLayer.DebugTransport(self.client.transport)
        self.client.transport = debugger

    def debug(self):
        for call in self.client.transport.get_last_calls():
            print(self.client.transport.print_reproduceable(call))

if __name__ == "__main__":
    main = dnsManager()
    main.main()
    main.debug()
```

### Creating a zone
A Zone here can either be a top level domain (domain.com) or a sub-domain (company.domain.com). The NS records for the zone will need to point so ns1.softlayer.com and ns2.softlayer.com.

To create a zone, we use [SoftLayer_Dns_Domain::createObject()](https://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/createObject/) and pass in a structure of type [SoftLayer_Dns_Domain](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Dns_Domain/). You can pass in a list of resourceRecords during domain creating for them to be added as well. You can not however change the SOA record at creation, but can do so by editing the SOA record after it has been created.

```
    def createZone(self):
        """Creates a DNS zone"""

        zoneTemplate = {
            'name': 'mydomain.com',
            'resourceRecords': [
                {'data': '127.0.0.1', 'host': '@', 'type': 'a' },
                {'data': '1.2.3.4', 'host': 'zed', 'type': 'a' },
                {'data': 'zed', 'host': '@', 'type': 'MX' }
            ]
        }

        result = self.client.call('SoftLayer_Dns_Domain', 'createObject', zoneTemplate)
        pp(result)
```

In Rest:
```
curl -u $SL_USER:$SL_APIKEY -X POST -d \
'{"parameters": [{"name": "mydomain.com", "resourceRecords": [{"type": "a", "host": "@", "data": "127.0.0.1"}, {"type": "a", "host": "zed", "data": "1.2.3.4"}, {"type": "MX", "host": "@", "data": "zed"}]}]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain/createObject.json'
```


### Creating Records
A record will be any entry under the zone you just created, so you will need to know the ID of the zone, and use that for the `domainId` in the record template.

Much like creating a zone, creating a record is done with a createObject call, but this time in the [SoftLayer_Dns_Domain_ResourceRecord::createObject](https://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain_ResourceRecord/createObject/) method. Use the [SoftLayer_Dns_Domain_ResourceRecord](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord/) datatype to define exactly how you want the record itself to look. The example below only uses a few of the fields.


```
    def addRecord(self, zone_id, record):
        """Adds record to zone_id"""
        recordTemplate = {
            'domainId': zone_id,  # id of the zone this record will belong to.
            'data': record['data'],
            'host': record['host'],
            'type': record['type']
        }
        result = self.client.call('SoftLayer_Dns_Domain_ResourceRecord', 'createObject', recordTemplate)
        pp(result)

if __name__ == "__main__":
    main = dnsManager()
    my_zone_id = 2986181
    record = {'data': '4.4.4.4', 'host': 'testa', 'type': 'a'}
    main.addRecord(my_zone_id, record)
```

REST:
```
curl -u $SL_USER:$SL_APIKEY -X POST  -d \
'{"parameters": [{"type": "a", "host": "testa", "domainId": 2986181, "data": "4.4.4.4"}]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain_ResourceRecord/createObject.json'
```

The SoftLayer_Dns_Domain service has methods like [SoftLayer_Dns_Domain::createARecord](https://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/createARecord/) which can make creating records easier, but this approach is a little more flexible. They are both capable of creating the same records though, so feel free to use either approach.

### Viewing
There are two main ways of getting information about the domain and its records. If you know the Id of the zone, simply use [SoftLayer_Dns_Domain::getObject()](https://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/getObject/), otherwise use [SoftLayer_Dns_Domain::getByDomainName](https://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/getByDomainName/) as shown here.

```
    def getZone(self, domain_name=None, zone_id=None):
        if (domain_name is None) and (zone_id is None):
            raise Exception("domain_name or zone_id is required")
        mask = "mask[resourceRecords]"
        if zone_id:
            domain = self.client.call('SoftLayer_Dns_Domain', 'getObject', id=zone_id, mask=mask)
        else:
            domain = self.client.call('SoftLayer_Dns_Domain', 'getByDomainName', domain_name, mask=mask)
        pp(domain)

if __name__ == "__main__":
    main = dnsManager()
    main.getZone(domain_name='mydomain.com')
```

REST:
```
curl -u $SL_USER:$SL_APIKEY \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain/2986181/getObject.json?objectMask=mask%5BresourceRecords%5D'

curl -u $SL_USER:$SL_APIKEY -X POST  -d \
'{"parameters": ["mydomainzzzzzzzzzzzzzz.com"]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain/getByDomainName.json?objectMask=mask%5BresourceRecords%5D'
```

You can also get the BIND format zone file with [getZoneFileContents](https://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/getZoneFileContents) if you need it.

```
curl -u $SL_USER:$SL_APIKEY \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain/2986181/getZoneFileContents.json'

$ORIGIN mydomain.com.
$TTL 86400
@ IN SOA ns1.softlayer.com. root.mydomain.com. (
                       2020010601        ; Serial
                       7200              ; Refresh
                       600               ; Retry
                       1728000           ; Expire
                       3600)             ; Minimum

@                      86400    IN NS    ns1.softlayer.com.
@                      86400    IN NS    ns2.softlayer.com.
@                      86400    IN A     127.0.0.1
testa                  86400    IN A     5.5.5.5
```


### Editing records.

Editing an existing record uses [SoftLayer_Dns_Domain_ResourceRecord::editObject()](https://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain_ResourceRecord/editObject/). You will need to know the Id of the Record (not the zone) for this.

```
    def editRecord(self, record_id, new_data):
        """Edits a record with new_data

        Will return True on success, and exception otherwise.
        new_data should be a structure that has fields that match the local properties of
        https://sldn.softlayer.com/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord/
        Only properties sent in will be updated.
        new_data = {'data':'1.2.3.4', 'ttl':600}
        """

        return self.client.call('SoftLayer_Dns_Domain_ResourceRecord', 'editObject', new_data, id=record_id)

if __name__ == "__main__":
    main = example()
    my_record_id = 118152560
    my_new_record = {'data': '5.5.5.5'}
    main.editRecord(my_record_id, my_new_record)
```

REST:
```
curl -u $SL_USER:$SL_APIKEY -X -d  \
'{"parameters": [{"data": "5.5.5.5"}]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain_ResourceRecord/118152560/editObject.json'
```


#### Editing SOA
The SOA for every zone will get set to something like this:

```
curl -u $SL_USER:$SL_APIKEY \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain/2986181/getSoaResourceRecord.json'
{
    "domainId": 2986181,
    "responsiblePerson": "root.mydomain.com.",
    "data": "ns1.softlayer.com.",
    "refresh": 7200,
    "mxPriority": null,
    "host": "@",
    "minimum": 3600,
    "retry": 600,
    "expire": 1728000,
    "ttl": 86400,
    "type": "soa",
    "id": 118151300
}
```

Which is usually fine, but if you need to change it, you can do the following. You will need to use the editRecords method mentioned above.

```
    def getSoa(self, zone_id):
        return self.client.call('SoftLayer_Dns_Domain', 'getSoaResourceRecord', id=zone_id)

if __name__ == "__main__":
    main = example()
    my_zone_id = 2986181

    soa = main.getSoa(my_zone_id)
    new_soa = {
        'data' : 'ns1.mydomain.com.',  # ending '.' is important.
        'type' : 'soa',
        'responsiblePerson' : 'root.mydomain.com.'  # ending '.' is important.
    }
    main.editRecord(soa.get('id'), new_soa)
    pp(main.getSoa(my_zone_id))
```

### Delete Records and Zones

Deleting a zone or record can be done with deleteObject.

```
    def deleteZone(self, zone_id):
        self.client.call('SoftLayer_Dns_Domain', 'deleteObject', id=zone_id)
    def deleteRecord(self, record_id):
        self.client.call('SoftLayer_Dns_Domain_ResourceRecord', 'deleteObject', id=record_id)

if __name__ == "__main__":
    main = example()
    my_zone_id = 2986181
    my_record_id = 118152560
    main.deleteRecord(my_record_id)
    main.deleteZone(my_zone_id)
```

REST:

You can either user a GET request and specify the deleteObject method, like below.
```
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain_ResourceRecord/118152560/deleteObject.json'
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain/2986181/deleteObject.json'
```

Or use a DELETE request, and omit the method, like below.
```
curl -u $SL_USER:$SL_APIKEY -X DELETE \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain_ResourceRecord/118152560'

curl -u $SL_USER:$SL_APIKEY -X DELETE \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain/2986181'
```

Both will return True on success, and an exception otherwise.

### Reverse Records
Reverse PTR records are a special type of DNS zone, as they can't be retrieved from a SoftLayer_Dns_Domain record exactly. Reverse PTR records link a Server or Virtual Guest with an IP. Generally setting this is very important for hosts that send out email (so spam filters can do some checking on the validity of your host).


```
dig -x 169.48.5.100
; <<>> DiG 9.10.6 <<>> -x 169.48.5.100

;; QUESTION SECTION:
;100.5.48.169.in-addr.arpa. IN  PTR

;; ANSWER SECTION:
100.5.48.169.in-addr.arpa. 86371 IN PTR 64.05.30a9.ip4.static.sl-reverse.com.

```


Each server and virtual guest will have a reverse PTR record associated with its primary IP address. You can get those with [SoftLayer_Hardware_Server::getReverseDomainRecords()](https://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getReverseDomainRecords/) and [SoftLayer_Virtual_Guest::getReverseDomainRecords()](https://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getReverseDomainRecords)

```
records = self.client.call('SoftLayer_Virtual_Guest', 'getReverseDomainRecords', id=record_id)
records = self.client.call('SoftLayer_Hardware_Server', 'getReverseDomainRecords', id=record_id)
```

Once you have the Id of the record, you can use [SoftLayer_Dns_Domain_ResourceRecord::editObject](https://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain_ResourceRecord/editObject/) to make changes to it.

REST:
In this example 1111111 is the id of the virtual guest, and 222222 is the resulting id from getReverseDomainRecords.

```
curl -u $SL_USER:$SL_APIKEY \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/1111111/getReverseDomainRecords.json' | python -m json.tool

[
    {
        "id": 88847,
        "name": "184.193.173.in-addr.arpa",
        "networkAddress": "173.193.184.0",
        "resourceRecords": [
            {
                "data": "pg-test-01.mydomain.com.",
                "domainId": 88847,
                "expire": null,
                "host": "164",
                "id": 222222,
                "isGatewayAddress": false,
                "minimum": null,
                "mxPriority": null,
                "refresh": null,
                "retry": null,
                "ttl": 7200,
                "type": "ptr"
            }
        ],
        "serial": 2020010600,
        "updateDate": "2020-01-06T17:03:27-06:00"
    }
]



curl -u $SL_USER:$SL_APIKEY -X POST  -d \
'{"parameters": [{"data": "pg-test-01.mydomain.com"}]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain_ResourceRecord/222222/editObject.json'
```

The SLCLI has `dns-sync` commands for both [virtual](https://softlayer-python.readthedocs.io/en/latest/cli/vs/#vs-dns-sync) and [hardware](https://softlayer-python.readthedocs.io/en/latest/cli/hardware/#hw-dns-sync) servers.
