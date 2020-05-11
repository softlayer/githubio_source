---
title: "Capture an Image Template"
description: "An example for capturing an Image Template"
date: "2020-05-08"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Virtual_Guest_Block_Device"
    - "SoftLayer_Account"
tags:
    - "template"
    - "virtualguest"
---

Capture Image Template

```java
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.virtual.Guest;
import com.softlayer.api.service.virtual.guest.block.Device;
import java.util.ArrayList;
import java.util.List;


public class CaptureImageTemplate {

  private ApiClient client;
  private long virtualGuestId;

  public CaptureImageTemplate(long guestId) {
    String username = "set-me";
    String apiKey = "set-me";
    client = new RestApiClient().withCredentials(username, apiKey);
    virtualGuestId = guestId;
  }

  public void capture(String name, String note) {
    Guest.Service guestService = Guest.service(client, virtualGuestId);
    guestService.withMask().blockDevices().diskImage();
    Guest virtualGuest = guestService.getObject();

    List<Device> blockDevices = gatherDevices(virtualGuest.getBlockDevices());
    try {
      Gson gson = new GsonBuilder().setPrettyPrinting().create();
      String json;
      guestService = Guest.service(client, virtualGuestId);
      Object result = guestService.createArchiveTransaction(name, blockDevices, note);
      json = gson.toJson(result);
      System.out.println(json);

    } catch (Exception e) {
      System.out.println("Unable to create image. "
          + e.getMessage());
    }
  }

  private List<Device> gatherDevices(List<Device> blockDevices) {
    List<Device> devices = new ArrayList<>();
    for (Device blockDevice : blockDevices) {
      String imageDescription = blockDevice.getDiskImage().getDescription();
      // We never want metadata disks or swap devices
      if (!imageDescription.contains("SWAP") && !imageDescription.contains("Metadata")) {
        devices.add(blockDevice);
      }
    }
    return devices;
  }

  public static void main(String args[]) {
    long virtualGuestId = 100123456L;
    String imageName = "test-image";
    String imageNotes = "Only for testing purposes";
    CaptureImageTemplate image = new CaptureImageTemplate(virtualGuestId);
    image.capture(
        imageName,
        imageNotes);
  }
}

```
