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
```py
import SoftLayer

class Virtual:
    def __init__(self):
        client = SoftLayer.create_client_from_env()
        self.virtual_service = client['Account']
        self.virtual_service = client['Virtual_Guest']
        self.metric_service = client['Metric_Tracking_Object']

    def _get_metric_tracking_object(self, guest_id):
        return self.virtual_service.getMetricTrackingObjectId(id=guest_id)

    def _get_virtual_guest(self):
        return self.account_service.getVirtualGuests(mask='id'

    def _calculate_averages(self, records):
        # total usage and how many records per item type
        total = {}
        for item in records:
            counter, date_time, item_type = item.values()
            total[item_type] = [x + y for x, y in zip(total.get(item_type, [0, 0]), [counter, 1])]

        # average of each item_type
        averages = {}
        for item, value in total.items():
            average = value[0] / value[1]
            averages[item] = average

        return averages

    def get_cpu_usage(self, guest_id, start_date, end_date):
        metric_object_id = self._get_metric_tracking_object(guest_id)
        guest = self.virtual_service.getObject(mask='id,startCpus', id=guest_id)

        # build the SoftLayer_Container_Metric_Data_Type array
        valid_types = []
        # it sets the valid types list according number of cpu items in the virtual server
        for i in range(guest['startCpus']):
            valid_type = {"keyName": "CPU" + str(i), "name": "cpu" + str(i), "summaryType": "max"}
            valid_types.append(valid_type)

        cpu_records = self.metric_service.getSummaryData(start_date, end_date,
                                                         valid_types, 3600,
                                                         id=metric_object_id)

        return cpu_records, self._calculate_averages(cpu_records)

    def get_memory_usage(self, guest_id, start_date, end_date):
        metric_object_id = self._get_metric_tracking_object(guest_id)

        # build the SoftLayer_Container_Metric_Data_Type array
        valid_types = [{"keyName": "MEMORY_USAGE", "summaryType": "max", "unit": "GB"}]

        memory_records = self.metric_service.getSummaryData(start_date, end_date,
                                                            valid_types, 3600,
                                                            id=metric_object_id)

        return memory_records, self._calculate_averages(memory_records)


if __name__ == "__main__":

    guest_id = 55984279
    start_date = '2019-02-04T00:00:00'
    end_date = '2019-04-09T23:59:59'

    virtual = Virtual()
    cpu_records, cpu_averages = virtual.get_cpu_usage(guest_id, start_date, end_date)
    memory_records, memory_averages = virtual.get_memory_usage(guest_id, start_date, end_date)

    # print records and cpu usage
    print("CPU USAGE RECORDS:")
    for record in cpu_records: print(record)

    print("\nCPU AVERAGES:")
    for cpu in cpu_averages: print(cpu + ": " + str(cpu_averages[cpu]))

    # print records and memory usage
    print("\nMEMORY USAGE RECORDS:")
    for record in memory_records: print(record)

    # there is only 1 memory and its value must be divided by 2^30 to convert it to GB
    print("\nMEMORY AVERAGE: " + str(memory_averages['memory_usage']/(2**30)) + " GB")

    virtuals = virtual.get_virtual_guest()
    for guest in virtuals:
        if virtual.get_metric_tracking_object(guest['id']) != '':
            guest_id = guest['id']
            cpu_records, cpu_averages = virtual.get_cpu_usage(guest_id,
                                                              start_date, end_date)
            memory_records, memory_averages = virtual.get_memory_usage(guest_id,
                                                                       start_date, end_date)


            if memory_averages.keys().__contains__('memory_usage'):
                print("\nTHE VIRTUAL GUEST: " + str(guest['id']))
                print("MEMORY AVERAGE: " + str(memory_averages['memory_usage']/(2**30)) 
                 print("CPU AVERAGE: " + str(cpu_averages['cpu0']) + " GB")
```

