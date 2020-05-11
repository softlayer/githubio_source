---
title: "Attach a file to a ticket"
description: "Attach a file to a created ticket"
date: "2020-05-08"
classes: 
    - "SoftLayer_Ticket"
tags:
    - "ticket"
    
---

```java
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Ticket;
import com.softlayer.api.service.container.utility.file.Attachment;
import org.apache.commons.codec.binary.Base64;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

public class AttachFileToTicket {

    public AttachFileToTicket() throws IOException {
        // Declare your SoftLayer username and apiKey
        String username = "set me";
        String apiKey = "set me";

        Long ticketId = 10811111L;

        // Declare the name of the file that will upload to the SoftLayer API and the path where
        // the file is located.
        String filename = "fileTest.txt";
        String path = "C:\\ticketCreated\\ticket.txt";

        // Reading the file in bytes
        File file = new File(path);
        FileInputStream ficheroStream = new FileInputStream(file);
        byte contenido[] = new byte[(int) file.length()];
        ficheroStream.read(contenido);

        String base64String = Base64.encodeBase64String(contenido);
        byte[] backToBytes = Base64.decodeBase64(base64String);

        // Build SoftLayer_Container_Utility_File_Attachment object
        Attachment newFile = new Attachment();
        newFile.setData(backToBytes);
        newFile.setFilename(filename);

        // Get Api Client and SoftLayer_Ticket service
        ApiClient client = new RestApiClient().withCredentials(username, apiKey).withLoggingEnabled();
        Ticket.Service ticketService = Ticket.service(client, ticketId);

        try {

            com.softlayer.api.service.ticket.attachment.File result = ticketService.addAttachedFile(newFile);
            System.out.println(result);

        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }

    public static void main(String[] args) throws IOException {
        new AttachFileToTicket();
    }
}

```