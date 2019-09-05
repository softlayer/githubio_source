---
title: "Bandwidth Usage Reports"
description: "Lists each server and virtual guest on an account, and their bandwidth usage throughout the given time period."
date: "2019-02-13"
classes: 
    - "SoftLayer_Metric_Tracking_Object"
    - "SoftLayer_Container_Bandwidth_GraphOutputs"
tags:
    - "bandwidth"
---

### Data Time Alignment 

The [SoftLayer_Metric_TrackingObject](/reference/services/SoftLayer_Metric_Tracking_Object/) class will auto-align your requested time to its nearest data collection boundary. 

For example, if you wanted bandwidth data from `2019-02-03T00:30:00` to `2019-02-04T00:30:01` with a 3600s rollup, you would get data back from `2019-02-03T01:00:00` to `2019-02-04T00:00:00`

This is especially problematic when requesting rollups for 12 and 24 hour periods. For these, the collection boundary starts at 00:00 UTC. So if you are in CST timezone for example, your request of data from `2019-02-03T00:00:00` to `2019-02-04T00:00:00` will get aligned to `2019-02-03T18:00:00-06:00` and `2019-02-03T18:00:00-06:00`

So if you are interested in daily values of your bandwidth, make sure to understand you should send in your requests in UTC so everything aligns to what you requested. This script does this for you, which should hopefully help.


*NOTE* Bandwidth from the Metric_TrackingObject is going to be in `octets`, or bytes. 

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
    # Uncomment this to print out the API calls made.
    #main.debug()
 
if __name__ == "__main__":
    main()

```


### REST Calls made
Get server list, with tracking object Ids
```
curl -u $SL_USER:$SL_APIKEY -X GET 'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getHardware.json?objectMask=mask%5Bid%2Chostname%2CfullyQualifiedDomainName%2CmetricTrackingObject%5Bid%5D%5D&resultLimit=0%2C2'
```

Get bandwidth data
```
curl -u $SL_USER:$SL_APIKEY -X POST  -d '{"parameters": [1546300800, 1548979200, "public", 86400]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Metric_Tracking_Object/26570093/getBandwidthData.json'
```

### Summary Reports

Possible values for [Metric_Data_Type](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Metric_Data_Type/). All summaryTypes must be the same for each request.

#### KeyName
* PUBLICIN
* PUBLICOUT
* PRIVATEIN
* PRIVATEOUT

#### summaryType
* items
* min
* max
* average
* sum
* timeaverage

*NOTE* When sending in a string time to the API, it is assumed the time is in CST/CDT. Use epoch time if you specifically want the data from a different timezone. 

```python
import SoftLayer
from pprint import pprint as pp
import datetime

class example():
    def __init__(self):
        self.client = SoftLayer.Client()

    def getSummaryReport(self, tracking_id, start_date, end_date, types=None, summaryPeriod=3600):
        """Gets a nice summary bandwidth report"""
        if types is None:
            types = [{
                'keyName': 'PUBLICIN',
                'summaryType': 'sum'
            }]
        data = self.client.call('SoftLayer_Metric_Tracking_Object', 'getSummaryData', start_date, end_date, types, summaryPeriod, id=tracking_id)
        return data

    def getHardwareTrackingId(self, hardware_id):
        return self.client.call('Hardware_Server', 'getMetricTrackingObject', id=hardware_id)
    def getVirtualTrackingId(self, vsi_id):
        return self.client.call('Virtual_Guest', 'getMetricTrackingObject', id=vsi_id)
    def convert(self, bytes):
        return  round(int(bytes) / (1024 **3 ),2)

if __name__ == "__main__":
    vsi_id = 75764043
    main = example()
    trackingObject = main.getVirtualTrackingId(vsi_id)
    print("Tracking ID is {}".format(trackingObject.get('id')))

    start_date = datetime.datetime.today()
    end_date = start_date + datetime.timedelta(days=1)
    time_format = "%Y-%m-%d"
    # image = main.getGraph(trackingObject.get('id'), start_date.strftime(time_format), end_date.strftime(time_format))

    # print("Graph Title: {}".format(image.get('graphTitle')))
    # main.saveImage(image)
    summary_types = [
        {"keyName": "PUBLICIN", "summaryType": "sum"},
        {"keyName": "PUBLICOUT", "summaryType": "sum"}
    ]
    summary = main.getSummaryReport(trackingObject.get('id'), start_date.strftime(time_format), end_date.strftime(time_format), summary_types)

    # Print out a daily summary of the summary...
    i = 0
    while i < len(summary):
        # Get the time, convert to UTC to avoid confusion.
        # %z only works in py3.7+. You may have to mangle the TZ data otherwise.
        the_date = datetime.datetime.strptime(summary[i]['dateTime'], '%Y-%m-%dT%H:%M:%S%z').astimezone(datetime.timezone.utc)
        print(the_date.strftime("%Y-%m-%d %H:%M"))
        output = []
        for sum_type in summary_types:
            text = "{}: {} MB".format(sum_type['keyName'], main.convert(summary[i]['counter']))
            output.append(text)
            i = i + 1
        print(", ".join(output))

```

### Simple Server Bandwidth
This example just gets the current billing cycle usage for a given server.

```python
import SoftLayer
import pprint

class example():

    def __init__(self):
        self.client = SoftLayer.Client()

    def main(self):
        pp = pprint.PrettyPrinter(indent=2)
        theMask = "mask[inboundPrivateBandwidthUsage,inboundPublicBandwidthUsage,outboundPrivateBandwidthUsage,outboundPublicBandwidthUsage]"
        result = self.client['SoftLayer_Account'].getHardware()
        print "server_name,public_in,public_out,private_in,private_out"
        
        for server in result:
            #getHardware() only returns SoftLayer_Hardware, which doesn't have the private bw usage metrics, for some reason.
            # So we just use SoftLayer_Hardware_Server here, which has more detailed information
            serverInfo = self.client['SoftLayer_Hardware_Server'].getObject(id=server['id'],mask=theMask)

            # use .get() to avoid exceptions
            pubin = serverInfo.get('inboundPublicBandwidthUsage', '--')
            pubout = serverInfo.get('outboundPublicBandwidthUsage', '--')
            privin =serverInfo.get('inboundPrivateBandwidthUsage', '--')
            privout = serverInfo.get('outboundPrivateBandwidthUsage', '--')

            print(serverInfo['fullyQualifiedDomainName'] + ","),
            print(pubin + ","),
            print(pubout + ","),
            print(privin + ","),
            print(privout)


if __name__ == "__main__":
    main = example()
    main.main()
```


### Virtual Guest getCurrentBandwidthSummary and getBandwidthDataByDate

[getBandwidthDataByDate](https://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getBandwidthDataByDate/)
[getCurrentBandwidthSummary](http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getCurrentBandwidthSummary)

```python
import SoftLayer
import datetime

from pprint import pprint as pp
class example():

    def __init__(self):
        self.client = SoftLayer.Client()

    def getCurrentBandwidthSummary(self, vsi_id):
        summary = self.client.call('Virtual_Guest', 'getCurrentBandwidthSummary', id=serverId)
        return summary

    def getBandwidthDataByDate(self, vsi_id, start_date, end_date, direction)
        """direction should be 'public', 'private', 'both'"""
        template = {
            'startDateTime': start_date,
            'endDateTime': end_date,
            'networkType': direction
        }
        bandwidth = self.client.call('Virtual_Guest').getBandwidthDataByDate(template, id=vsi_id)
        return bandwidth


if __name__ == "__main__":
    vsi_id = 12345667
    main = example()
    summary = main.getCurrentBandwidthSummary(vsi_id)
    print("Summary")
    pp(summary)

    start_date = datetime.datetime.today()
    end_date = start_date + datetime.timedelta(days=1)
    bw_by_date = main.getBandwidthDataByDate(vsi_id, start_date, end_date)
    print("Bandwidth By Date")
    pp(bw_by_date)
```


### Get the Bandwidth Graph

[getBandwidthGraph](https://sldn.softlayer.com/reference/services/SoftLayer_Metric_Tracking_Object/getBandwidthGraph/)

```python
import SoftLayer
from pprint import pprint as pp
import datetime
import base64

class example():

    def __init__(self):
        self.client = SoftLayer.Client()

    def getGraph(self, tracking_id, startDateTime, endDateTime, graphType='public',
                 fontSize=8, graphWidth=800, graphHeight=300, doNotShowTimeZone=False):
        """Returns a bandwidth graph"""
        image = self.client.call('SoftLayer_Metric_Tracking_Object', 'getBandwidthGraph',
                                 startDateTime, endDateTime, graphType, fontSize, graphWidth,
                                 graphHeight, doNotShowTimeZone, id=tracking_id)
        # pp(image)
        return image

    def saveImage(self, image):
        """image should be data returned from getBandwidthGraph"""
        # Graph title will usually be the FQDN of the server
        path = '{}.png'.format(image.get('graphTitle'))
        # open the file in write+binary mode
        file = open(path, 'wb')
        image_data = image.get('graphImage')

        # REST API returns a '' encapsulated string, so we need to remove those, and then base64decode
        if isinstance(image_data, str):
            png = base64.b64decode(image_data.replace("'",""))
        # XML-RPC returns raw binary, so we just need to get its data out.
        else:
            png = image_data.data

        file.write(png)
        file.close()

    def getHardwareTrackingId(self, hardware_id):
        return self.client.call('Hardware_Server', 'getMetricTrackingObject', id=hardware_id)
    def getVirtualTrackingId(self, vsi_id):
        return self.client.call('Virtual_Guest', 'getMetricTrackingObject', id=vsi_id)

if __name__ == "__main__":
    vsi_id = 75764043
    main = example()
    trackingObject = main.getVirtualTrackingId(vsi_id)
    print("Tracking ID is {}".format(trackingObject.get('id')))

    start_date = datetime.datetime.today()
    end_date = start_date + datetime.timedelta(days=1)
    time_format = "%Y-%m-%d"
    image = main.getGraph(trackingObject.get('id'), start_date.strftime(time_format), end_date.strftime(time_format))

    print("Graph Title: {}".format(image.get('graphTitle')))
    main.saveImage(image)
```