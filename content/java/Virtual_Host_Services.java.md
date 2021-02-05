---
title: "Managing Virtual_Host"
description: "How to interact with the SoftLayer_Virtual_Host services, manage mappings and other related functions"
date: "2021-05-02"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Virtual_Host"
tags:
    - "Virtual_Host"    
---

```java
import com.google.gson.*;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Account;
import com.softlayer.api.service.Hardware;
import com.softlayer.api.service.hardware.Server;
import com.softlayer.api.service.metric.tracking.Object;
import com.softlayer.api.service.virtual.Guest;
import com.softlayer.api.service.virtual.Host;
import com.softlayer.api.service.virtual.host.PciDevice;

import java.util.ArrayList;
import java.util.List;

public class VirtualHostService {

    Account.Service account;
    Host.Service host;
    ApiClient client;

    public VirtualHostService() {
        String user = "set - me";
        String apiKey = "set - me";
        client = (new RestApiClient()).withCredentials(user, apiKey);
        account = Account.service(client);
    }

    /*
    * getAllVirtualHost method
     */
    public List<String> getVirtualHost() {
        List<String> hostList = new ArrayList<String>();

        account.setMask("mask[id,virtualHost[id]]");
        List<Hardware> listHW = account.getHardware();
        for (Hardware hd : listHW) {
            Gson gson = (new GsonBuilder()).setPrettyPrinting().create();
            JsonParser jsonParser = new JsonParser();
            JsonObject paramObject = (JsonObject) jsonParser.parse(gson.toJson(hd));

            try {
                JsonElement virtualHost = ((JsonObject) paramObject.get("virtualHost")).get("id");
                hostList.add(String.valueOf(virtualHost));
            } catch (NullPointerException ex) {
                hostList.add("empty");
            }

        }
        return hostList;
    }

    /**
     * getBilledPerGuestFlag method
     *
     * @param hostId - Virtual host Id
     * @return boolean
     */
    public boolean getBilledPerGuestFlag(int hostId) {
        host = Host.service(client, (long) hostId);
        return host.getBilledPerGuestFlag();
    }

    /**
     * getBilledPerMemoryUsageFlag method
     *
     * @param hostId - Virtual host Id
     * @return boolean
     */
    public boolean getBilledPerMemoryUsageFlag(int hostId) {
        host = Host.service(client, (long) hostId);
        return host.getBilledPerGuestFlag();
    }

    /**
     * getGuest method
     *
     * @param hostId - Virtual host Id
     * @return List<Virtual_Guest>
     */
    public List<Guest> getGuests(int hostId) {
        host = Host.service(client, (long) hostId);
        return host.getGuests();
    }

    /**
     * getHardware method
     *
     * @param hostId - Virtual host Id
     * @return hardware instance
     */
    public Server getHardware(int hostId) {
        host = Host.service(client, (long) hostId);
        return host.getHardware();
    }

    /**
     * getLiveGuestByUuid
     *
     * @param hostId - Virtual host Id
     * @param uuid   - Virtual guest uuid
     * @return Virtual guest Id
     */
    public Guest getLiveGuestByUuid(int hostId, String uuid) {
        host = Host.service(client, (long) hostId);
        return host.getLiveGuestByUuid(uuid);
    }

    /**
     * getLiveGuestByUuid
     *
     * @param hostId - Virtual host Id
     * @return List<Virtual_guest>
     */
    public List<Guest> getLiveGuestList(int hostId) {
        host = Host.service(client, (long) hostId);
        return host.getLiveGuestList();
    }

    /**
     * getLiveGuestByUuid
     *
     * @param hostId   - Virtual host Id
     * @param uuid     - Virtual guest uuid
     * @param interval - interval value
     * @param limit    - limit value
     * @param time     - time value
     * @return Virtual guest Id
     */
    public List<Object> getLiveGuestRecentMetricData(int hostId, String uuid,
                                                     int time, int limit, int interval) {
        host = Host.service(client, (long) hostId);
        return host.getLiveGuestRecentMetricData(uuid, (long) time,
                (long) limit, (long) interval);
    }

    /**
     * getMetricTrackingObject method
     *
     * @param hostId - Virtual host Id
     * @return Metric_Tracking_Object instance
     */
    public Object getMetricTrackingObject(int hostId) {
        host = Host.service(client, (long) hostId);
        return host.getMetricTrackingObject();
    }

    /**
     * getObject method
     *
     * @param hostId -  Virtual host Id
     * @return Virtual host Instance
     */
    public Host getObject(int hostId) {
        host = Host.service(client, (long) hostId);
        return host.getObject();
    }

    /**
     * getPciDevices  method
     *
     * @param hostId - Virtual host Id
     * @return List<PciDevice>
     */
    public List<PciDevice> getPciDevices(int hostId) {
        host = Host.service(client, (long) hostId);
        return host.getPciDevices();
    }

    /**
     * pauseLiveGuest method
     *
     * @param hostId - Virtual host Id
     * @param uuid   - Virtual guest uuid
     * @return boolean
     */
    public boolean pauseLiveGuest(int hostId, String uuid) {
        host = Host.service(client, (long) hostId);
        return host.pauseLiveGuest(uuid);
    }

    /**
     * powerCycleLiveGuest method
     *
     * @param hostId - Virtual host Id
     * @return List<PciDevice>
     */
    public List<PciDevice> powerCycleLiveGuest(int hostId) {
        host = Host.service(client, (long) hostId);
        return host.getPciDevices();
    }

    /**
     * powerOffLiveGuest method
     *
     * @param hostId - Virtual host Id
     * @param uuid   - Virtual guest uuid
     * @return boolean
     */
    public boolean powerOffLiveGuest(int hostId, String uuid) {
        host = Host.service(client, (long) hostId);
        return host.powerOffLiveGuest(uuid);
    }

    /**
     * powerOnLiveGuest method
     *
     * @param hostId - Virtual host Id
     * @param uuid   - Virtual guest uuid
     * @return boolean
     */
    public boolean powerOnLiveGuest(int hostId, String uuid) {
        host = Host.service(client, (long) hostId);
        return host.powerOnLiveGuest(uuid);
    }

    /**
     * rebootSoftLiveGuest method
     *
     * @param hostId - Virtual host Id
     * @param uuid   - Virtual guest uuid
     * @return boolean
     */
    public boolean rebootSoftLiveGuest(int hostId, String uuid) {
        host = Host.service(client, (long) hostId);
        return host.rebootSoftLiveGuest(uuid);
    }

    /**
     * resumeLiveGuest method
     *
     * @param hostId - Virtual host Id
     * @param uuid   - Virtual guest uuid
     * @return boolean
     */
    public boolean resumeLiveGuest(int hostId, String uuid) {
        host = Host.service(client, (long) hostId);
        return host.resumeLiveGuest(uuid);
    }

    public static void main(String[] args) {
        VirtualHostService virtualHostService = new VirtualHostService();
        virtualHostService.getVirtualHost();
    }
}


```