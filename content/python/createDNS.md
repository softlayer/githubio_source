---
title: "Create A Domain"
description: "Example of how to create a Domain in the SoftLayer DNS, along with how to edit its resource records."
date: "2016-04-29"
classes: 
    - "SoftLayer_Dns_Domain"
    - "SoftLayer_Dns_Domain_ResourceRecord"
tags:
    - "dns"
---



```
import SoftLayer
from pprint import pprint as pp

class example():

    def __init__(self):

        self.client = SoftLayer.Client()

    def main(self):
        zone_name = 'lablayer2.info'
        zone_client = self.client['SoftLayer_Dns_Domain']
        the_zone =  {
            'name' : zone_name,
            'resourceRecords' : [ 
                {
                    'data' : '123.123.123.123',
                    'host' : 'ns1',
                    'type' : 'a',
                },
                {
                    'data' : '123.123.123.123',
                    'host' : 'ns2',
                    'type' : 'a',
                },
                {
                    'data' : '123.123.123.123',
                    'host' : '@',
                    'type' : 'a',
                },
                {
                    'data' : 'ns2.lablayer2.info.',
                    'host' : '@',
                    'type' : 'ns',
                },
                {
                    'data' : 'ns1.lablayer2.info.',
                    'host' : '@',
                    'type' : 'ns',
                }
            ]
        }
        the_soa = {
            'data' : 'ns1.lablayer2.info.',
            'type' : 'soa',
            'responsiblePerson' : 'root.lablayer2.info.'
        }
        # result = zone_client.createObject(the_zone)
        # pp(result)

        mask = "mask[resourceRecords]"
        """
        getByDomainName will do a greedy search, so make sure you are searching for 
        the exact domain you want, otherwise you might get back more than 1 result.
        """
        zone_result = zone_client.getByDomainName(zone_name, mask=mask)
        # pp(zone_result)

        """
        SoftLayer creates each zone with a standard SOA record.
        The SOA record can only be changed after creation. This isn't
        usually needed, but here is how to do it.
        """
        for zone in zone_result[0]['resourceRecords']:
            if zone['type'].lower() is 'soa':
                zone_client.editObject(the_soa, id=zone['id'])


if __name__ == "__main__":
    main = example()
    main.main()

```