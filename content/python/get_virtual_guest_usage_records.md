---
title: "CPU and Memory usage in Virtual servers"
description: "How the portal page retrieves the memory and cpu usage"
date: "2019-04-10"
classes:
    - "SoftLayer_Account"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Metric_Tracking_Object"
tags:
    - "account"
    - "metric"
    - "virtualguest"
---

This example will print out the average memory and CPU usage for a given time period for all virtual guests on your account. 

### Time Format
Use the following time format for any requests. `YYYY-MM-DDTHH:MM:SS` or Epoch Time will work. These times are all tracked in CST, and the response will be in your users local timezone. When requesting data on day boundaries, your start time should be `00:00` and end time should be `23:59`

### Notes

The metric tracking api can be a bit slow, depending on how much data you are requesting, so if your request times out, try lowering how much time you are asking for.

Not all virtual guests will have a metric tracking object, for example any suspended virtual guest, or VMWare guest will not be tracked. 
 

```py
import SoftLayer
import sys
from pprint import pprint as pp 

class Virtual:
    def __init__(self):
        self.client = SoftLayer.create_client_from_env()

    def get_virtual_guest(self):
        """This method gets the basic data for each virtual guest on an account

        The mask is a minimal mask to make the request quicker.
        """
        mask = "mask[id, hostname, domain, metricTrackingObjectId, startCpus]"
        return self.client.call('Account', 'getVirtualGuests', mask=mask)

    def _calculate_averages(self, records):
        """Calculates the average for metric tracking object entries over their time period

        basicaly sum(items) / count(items)
        """
        total = {}
        for item in records:
            counter, date_time, item_type = item.values()
            total[item_type] = [x + y for x, y in zip(total.get(item_type, [0, 0]), [counter, 1])]

        # average of each item_type
        averages = {}
        for item, value in total.items():
            average = round(value[0] / value[1], 2)
            averages[item] = average

        return averages

    def get_cpu_usage(self, guest, start_date, end_date):
        """Formats and executes an API call to get CPU usage data for a guest

        Each CPU is tracked individually so its required to know how many CPUs a guest has
        returns cpu_records, which is the raw data returned from the API
        returns averages, which is the averaged data in a simple dictionary
        """
        valid_types = []
        # it sets the valid types list according number of cpu items in the virtual server
        for i in range(guest['startCpus']):
            valid_type = {"keyName": "CPU" + str(i), "name": "cpu" + str(i), "summaryType": "average"}
            valid_types.append(valid_type)

        cpu_records = self.client.call('Metric_Tracking_Object', 'getSummaryData',
                                        start_date, end_date, valid_types, 86400,
                                        id=guest['metricTrackingObjectId'])

        return cpu_records, self._calculate_averages(cpu_records)

    def get_cpu_usage_per_cpu(self, guest, start_date, end_date):
        """Formats and executes an API call to get CPU usage data for a guest

        Making 1 API call per CPU is usually faster than getting all CPUs in 1 API call.
        Each CPU is tracked individually so its required to know how many CPUs a guest has
        returns cpu_records, which is the raw data returned from the API
        returns averages, which is the averaged data in a simple dictionary
        """
        
        cpu_records = []
        # it sets the valid types list according number of cpu items in the virtual server
        for i in range(guest['startCpus']):
            valid_types = [{"keyName": "CPU" + str(i), "name": "cpu" + str(i), "summaryType": "average"}]


            result  = self.client.call('Metric_Tracking_Object', 'getSummaryData',
                                            start_date, end_date, valid_types, 86400,
                                            id=guest['metricTrackingObjectId'])

            # Need to add each datapoint to the cpu_records list
            for entry in result:
                cpu_records.append(entry)

        return cpu_records, self._calculate_averages(cpu_records)

    def get_memory_usage(self, guest, start_date, end_date):
        """Formats and executes an API call to get memory usage data for a guest

        returns memory_records, which is the raw data returned from the API
        returns averages, which is the averaged data in a simple dictionary
        """
        valid_types = [{"keyName": "MEMORY_USAGE", "summaryType": "average", "unit": "GB"}]

        memory_records = self.client.call('Metric_Tracking_Object', 'getSummaryData',
                                          start_date, end_date, valid_types, 86400,
                                          id=guest['metricTrackingObjectId'])

        return memory_records, self._calculate_averages(memory_records)


if __name__ == "__main__":

    start_date = '2021-05-01T00:00:00'
    end_date = '2021-05-31T23:59:59'

    virtual = Virtual()
    # Get all virtual guests on our account
    virtuals = virtual.get_virtual_guest()
    for guest in virtuals:
        # Make sure the guest object has a tracking ID.
        if guest.get('metricTrackingObjectId', None):
            try:
                cpu_records, cpu_averages = virtual.get_cpu_usage_per_cpu(guest, start_date, end_date)
                memory_records, memory_averages = virtual.get_memory_usage(guest, start_date, end_date)
                # Check to make sure we actually have data for the time period
                if len(memory_records) < 1  or len(cpu_records) < 1 :
                    mem_avg = "No Data"
                    cpu_avg = ["No Data"]
                else:
                    # Convert memory to GB
                    mem_avg = round(memory_averages['memory_usage']/(2**30),2)
                    cpu_avg = []
                    # Convert CPU averages to a nice string format.
                    for cpu in cpu_averages.keys():
                        cpu_avg.append("{}: {}".format(cpu, cpu_averages[cpu]))
                print("{}.{}, {}, {}".format(guest['hostname'], guest['domain'], mem_avg, ", ".join(cpu_avg)))
            # In case of an API error, just print the error and continue.
            except Exception as e:
                print("{}.{}, {}".format(guest['hostname'], guest['domain'], e))
        else:
            print("{}.{} (id={}) No Metric Tracking Object found".format(guest['hostname'], guest['domain'], guest['id']))
        # This script can take a long time to run, this forces output to print immediately
        sys.stdout.flush()

```

