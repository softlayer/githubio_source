---
title: "CPU and Memory usage in Virtual servers"
description: "How the portal page retrieves the memory and cpu usage"
date: "2020-06-10"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Metric_Tracking_Object"
tags:
    - "metric"
    - "virtualguest"
---


```
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.container.bandwidth.GraphOutputs;
import com.softlayer.api.service.container.metric.data.Type;
import com.softlayer.api.service.metric.tracking.Object;
import com.softlayer.api.service.metric.tracking.object.Data;
import com.softlayer.api.service.virtual.Guest;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.util.*;

public class Usage {
    private Guest.Service guestService;
    private Object.Service trakingService;

    public Usage(Guest.Service guestService, Object.Service trakingService) {
        this.guestService = guestService;
        this.trakingService = trakingService;
    }

    public Map<String, Double> calculateAverages(List<Data> records) {
        Map<String, Double> total = new HashMap<>();
        Map<String, Integer> totalCounter = new HashMap<>();
        for (Data item : records) {
            if (!total.containsKey(item.getType())) {
                total.put(item.getType(), item.getCounter().doubleValue());
                totalCounter.put(item.getType(), 1);
            } else {
                double itemCounterTotal = total.get(item.getType()) + item.getCounter().doubleValue();
                total.put(item.getType(), itemCounterTotal);
                totalCounter.put(item.getType(), totalCounter.get(item.getType()) + 1);
            }
        }

        Map<String, Double> average = new HashMap<>();
        for (Map.Entry<String, Double> entry : total.entrySet()) {
            double usageCounter = entry.getValue() / totalCounter.get(entry.getKey());
            average.put(entry.getKey(), usageCounter);
        }
        return average;
    }

    public List<Data> getCpuUsage(String startDate, String endDate) throws ParseException {

        GregorianCalendar start = getDate(startDate);
        GregorianCalendar end = getDate(endDate);

        Guest guestResponse = this.guestService.getObject();

        List<Type> types = new ArrayList<>();
        for (int i = 0; i < guestResponse.getStartCpus(); i++) {
            Type type = new Type();
            type.setKeyName("CPU" + String.valueOf(i));
            type.setName("cpu" + String.valueOf(i));
            type.setSummaryType("max");
            types.add(type);
        }

        return this.trakingService.getSummaryData(start, end, types, 3600L);
    }

    public List<Data> getMemoryUsage(String startDate, String endDate) throws ParseException {

        GregorianCalendar start = getDate(startDate);
        GregorianCalendar end = getDate(endDate);

        //build the SoftLayer_Container_Metric_Data_Type array
        List<Type> types = new ArrayList<>();

        Type type = new Type();
        type.setKeyName("MEMORY_USAGE");
        type.setSummaryType("max");
        type.setUnit("GB");
        types.add(type);

        return this.trakingService.getSummaryData(start, end, types, 3600L);
    }

    public void getCpuGraph(String startDate, String endDate, String filePath, List<String> cpuType) throws ParseException {

        GregorianCalendar start = getDate(startDate);
        GregorianCalendar end = getDate(endDate);

        GraphOutputs cpuGraph = this.trakingService.getGraph(start, end, cpuType);
        byte[] cpuImae = cpuGraph.getGraphImage();

        try {
            ByteArrayInputStream inputStream = new ByteArrayInputStream(cpuImae);
            BufferedImage image = ImageIO.read(inputStream);
            ImageIO.write(image, "jpg", new File(filePath));
            System.out.println("Image created");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void getMemoryGraph(String startDate, String endDate, String filePath) throws ParseException {

        GregorianCalendar start = getDate(startDate);
        GregorianCalendar end = getDate(endDate);

        GraphOutputs cpuGraph = this.guestService.getMemoryMetricImageByDate(start, end);
        byte[] cpuImage = cpuGraph.getGraphImage();

        try {
            ByteArrayInputStream inputStream = new ByteArrayInputStream(cpuImage);
            BufferedImage image = ImageIO.read(inputStream);
            ImageIO.write(image, "jpg", new File(filePath));
            System.out.println("Image created");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public GregorianCalendar getDate(String date) throws ParseException {

        ZoneId defaultZoneId = ZoneId.systemDefault();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss", Locale.ENGLISH);
        LocalDate localDate = LocalDate.parse(date, formatter);
        Date date1 = Date.from(localDate.atStartOfDay(defaultZoneId).toInstant());
        GregorianCalendar dateValue = new GregorianCalendar();
        dateValue.setTime(date1);
        return dateValue;
    }

    public static void main(String[] args) throws ParseException {
        // Declare your SoftLayer username and apiKey
        String username = "set me";
        String apiKey = "set me";
        
        Long serverId = 11111L;
        String startDate = "2020-03-04T00:00:00";
        String endDate = "2020-04-09T23:59:59";

        String filePathCpu = "E:\\file\\cpufile.jpg";
        String filePathMemory = "E:\\file\\memoryfile.jpg";

        // Get Api Client.
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Guest.Service guestService = Guest.service(client, serverId);

        Long trakingId = guestService.getMetricTrackingObjectId();
        Object.Service trakingService = Object.service(client, trakingId);

        Usage usage = new Usage(guestService, trakingService);
        List<Data> cpuRecord = usage.getCpuUsage(startDate, endDate);
        Map<String, Double> cpuAverage = usage.calculateAverages(cpuRecord);
        List<Data> memoryRecord = usage.getMemoryUsage(startDate, endDate);
        Map<String, Double> memoryAverage = usage.calculateAverages(memoryRecord);

        // print records and cpu usage
        System.out.println("CPU USAGE RECORDS:\n");
        for (Data record : cpuRecord) {
            SimpleDateFormat formattedDate = new SimpleDateFormat("dd-MMM-yyyy");
            String dateFormatted = formattedDate.format(record.getDateTime().getTime());
            System.out.println(record.getType() + " - " + dateFormatted + " - " + record.getCounter());
        }

        // print("\nCPU AVERAGES:")
        System.out.println("\nCPU AVERAGES:\n");
        for (Map.Entry<String, Double> average : cpuAverage.entrySet()) {
            System.out.println(average.getKey() + ": " + average.getValue() + "\n");
        }

        // cpu graph
        List<String> cpuTypes = new ArrayList<>();
        for (Map.Entry<String, Double> average : cpuAverage.entrySet()) {
            cpuTypes.add(average.getKey());
        }
        usage.getCpuGraph(startDate, endDate, filePathCpu, cpuTypes);

        // print records and memory usage
        System.out.println("\nMEMORY USAGE RECORDS:\n");
        for (Data record : memoryRecord) {
            SimpleDateFormat formattedDate = new SimpleDateFormat("dd-MMM-yyyy");
            String dateFormatted = formattedDate.format(record.getDateTime().getTime());
            System.out.println(record.getType() + " - " + dateFormatted + " - " + record.getCounter());
        }

        // there is only 1 memory and its value must be divided by 2^30 to convert it to GB
        System.out.println("\nMEMORY AVERAGE: " + memoryAverage.get("memory_usage") / Math.pow(2, 30) + "GB");

        // memory graph
        usage.getMemoryGraph(startDate, endDate, filePathMemory);
    }
}


```
