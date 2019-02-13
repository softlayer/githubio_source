---
title: "Bandwidth Usage Reports"
description: "Lists each server and virtual guest on an account, and their bandwidth usage throughout the given time period."
date: "2019-02-13"
classes: 
    - "SoftLayer_Metric_Tracking_Object"
tags:
    - "bandwidth"
---

### Data Time Alignment 

The [SoftLayer_Metric_TrackingObject](reference/services/SoftLayer_Metric_Tracking_Object/) class will auto-align your requested time to its nearest data collection boundary. 

For example, if you wanted bandwidth data from `2019-02-03T00:30:00` to `2019-02-04T00:30:01` with a 3600s rollup, you would get data back from `2019-02-03T01:00:00` to `2019-02-04T00:00:00`

This is especially problematic when requesting rollups for 12 and 24 hour periods. For these, the collection boundary starts at 00:00 UTC. So if you are in CST timezone for example, your request of data from `2019-02-03T00:00:00` to `2019-02-04T00:00:00` will get aligned to `2019-02-03T18:00:00-06:00` and `2019-02-03T18:00:00-06:00`

So if you are interested in daily values of your bandwidth, make sure to understand you should send in your requests in UTC so everything aligns to what you requested. This script does this for you, which should hopefully help.


```python
"""
 Softlayer Stores in octets (bytes), sizes printed are in Giga Bytes (octets / 1024^3)
Sum values are a running total for the time period requested.
"""
 
import SoftLayer
from pprint import pprint as pp
import logging
import datetime
import calendar
import  click
 
def dateToEpoch(ctx, param, value):
    """A handy function to take a 'YYYY-MM-DD' date and return a datetime object
    """
    try:
        datetime_object = datetime.datetime.strptime(value, '%Y-%m-%d')
        datetime_object.replace(tzinfo=datetime.timezone.utc)
        return datetime_object
    except ValueError:
        raise click.BadParameter('Unable to parse date: %s' % value)
 
class example():
 
    def __init__(self, start, end):
        """
       :param int start: epoch time to start at. Should align to 00:00 UTC
       :param int end: epoch time to end at. Should align to 00:00 UTC
       """
        self.client = SoftLayer.Client()
        debugger = SoftLayer.DebugTransport(self.client.transport)
        self.client.transport = debugger
        self.start = start
        self.end = end
 
        # logger = logging.getLogger()
        # logger.addHandler(logging.StreamHandler())
   
    def debug(self):
        """
        Useful for printing out the exact API calls that were used. If using the rest transport, will print cure-able commands.
        """
        for call in self.client.transport.get_last_calls():
            print(self.client.transport.print_reproduceable(call))
 
    def main(self):
        """
        Goes through the server and virtualGuest list of servers. Uses pagination to step through large server lists.
        """
        print("Getting reports from %s -> %s" % (self.start, self.end))
        mask = """mask[id,hostname,fullyQualifiedDomainName,metricTrackingObject[id]]"""
        servers = self.client.call('Account', 'getHardware', mask=mask, iter=True, limit=100)
        for server in servers:
            print("%s" % server['fullyQualifiedDomainName'])
            data = self.getBWReport(server['metricTrackingObject']['id'])
            self.detailedReport(server, data)
 
        guests = self.client.call('Account', 'getVirtualGuests', mask=mask, iter=True, limit=100)
        for server in guests:
            print("%s" % server['fullyQualifiedDomainName'])
            data = self.getBWReport(server['metricTrackingObject']['id'])
            self.detailedReport(server, data)
 
    def detailedReport(self, server, data):
        """Prints out the collected data, does sime date formatting to make it look nice. 

        This bit only works in py3.7 because it supports the -06:00 TZ format (part of %z). If you are not using py3.7, you could just print out the date as is, which would be in your local timezone.
        """
        print("Start Date             , End Data               , In , Out, In Sum, Out Sum")
        bw_data = {}
        total_in = 0
        total_out = 0
        for point in data:
            start_date = point['dateTime']
            counter = self.convert(point['counter'])
            if point['type'] == 'publicIn_net_octet':
                bw_data[start_date] = {'in': counter}
            elif point['type'] == 'publicOut_net_octet':
                bw_data[start_date]['out'] = counter
        for point in bw_data:
            # make a datetime object out of the date SL gave us, convert it BACK to UTC
            start_date = datetime.datetime.strptime(point, '%Y-%m-%dT%H:%M:%S%z').astimezone(datetime.timezone.utc)
            # since our rollup is 86400, our end date is + 86400 sceonds
            end_date = start_date + datetime.timedelta(seconds=86400)
            total_in = round(total_in + float(bw_data[point]['in']),4)
            total_out = round(total_out + float(bw_data[point]['out']),4)
            print("%s, %s, %s, %s, %s, %s" % (
                start_date.strftime("%Y-%m-%d %H:%M:%S %Z"),
                end_date.strftime("%Y-%m-%d %H:%M:%S %Z"),
                bw_data[point]['in'],
                bw_data[point]['out'],
                total_in,
                total_out)
            )
 
 
    def getBWReport(self, tracking_id):
        """
        start and end here are getting converted to epoch time so we don't have to worry about properly specifying a timezone. 
        """
        print("getBWReport")
        start = calendar.timegm(self.start.timetuple())
        end = calendar.timegm(self.end.timetuple())
        data = self.client.call('Metric_Tracking_Object', 'getBandwidthData', start, end, 'public', 86400, id=tracking_id)
        # pp(data)
        return data
 
 
    def convert(self, bytes):
        return  round(int(bytes) / (1024 **3 ),2)
 
@click.command()
@click.option('--start', default='2019-01-01', help='Start date, YYYY-MM-DD', callback=dateToEpoch)
@click.option('--end', default='2019-02-01', help='End Date, YYYY-MM-DD', callback=dateToEpoch)
def main(start, end):
    main = example(start, end)
    main.main()
 
if __name__ == "__main__":
    main()
    # Uncomment this to print out the API calls made.
    #main.debug()
```
