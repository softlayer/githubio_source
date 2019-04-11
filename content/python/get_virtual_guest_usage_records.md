---
title: "CPU and Memory usage in Virtual servers"
description: "How the portal page retrieves the memory and cpu usage"
date: "2019-04-10"
classes:
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Metric_Tracking_Object"
tags:
    - "metric"
    - "metrics"
    - "virtual server"
    - "virtualguest"
---
```py
import SoftLayer

class Virtual:
    def __init__(self):
        client = SoftLayer.create_client_from_env()
        self.virtual_service = client['Virtual_Guest']
        self.metric_service = client['Metric_Tracking_Object']

    def _get_metric_tracking_object(self, guest_id):
        return self.virtual_service.getMetricTrackingObjectId(id=guest_id)

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

        # build the SoftLayer_Container_Metric_Data_Type array
        valid_types = []
        # set range according number of cpu items you want to retrieve the metric data
        for i in range(16):
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
    print(cpu_averages)

    # print records and memory usage
    print("\nMEMORY USAGE RECORDS:")
    for record in memory_records: print(record)
    
    # there is only 1 memory and its value must be divided by 2 to convert it to GB
    print("\nMEMORY AVERAGE: " + str(memory_averages['memory_usage']/(2**30)) + " GB")
```

