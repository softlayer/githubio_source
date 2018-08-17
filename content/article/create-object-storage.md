---
title: "Creating an Object Storage instance"
description: "An example of how to order an Object Storage instance and interact via the API."
date: "2018-08-10"
tags:
    - "article"
    - "sldn"
---


## Create an Object Storage Instance

This tutorial walks you through creating a IBM Cloud Object Storage instance.

## Objectives

* Create an object storage instance.

## Services used

This tutorial uses the following technologies:
* [ibmcloud](https://console.bluemix.net/docs/cli/index.html#overview) IBM Cloud CLI

This tutorial may incur costs. Use the [Pricing Calculator](https://console.bluemix.net/pricing/) to generate a cost estimate based on your projected usage.

## Install IBM Cloud CLI
To install the toolset, you can run the relevant command to start the installer. This installs the following recommended tools for {{site.data.keyword.Bluemix_notm}} development (if not already installed): Homebrew (Mac only), Git, Docker, Helm, kubectl, curl, {{site.data.keyword.Bluemix_notm}} CLI, {{site.data.keyword.dev_cli_notm}} plug-in, Cloud Functions plug-in, Container Registry plug-in, Container Service plug-in, and sdk-gen plug-in.

Mac and Linux:
```
curl -sL https://ibm.biz/idt-installer | bash
```

Windows 10:
    Note: Open Windows PowerShell by right-clicking the PowerShell icon and selecting "Run as Administrator".
```
Set-ExecutionPolicy Unrestricted; iex(New-Object Net.WebClient).DownloadString('http://ibm.biz/idt-win-installer')
```

Verify Installation

To verify installation, run the help command:
```
ibmcloud dev help
```

If installation was successful, the output should list usage instructions, the current version, and supported commands.

## Authenticate


```
ibmcloud login
```


## Create Cloud Object Storage instance
(https://console.bluemix.net/docs/services/cloud-object-storage/basics/developers.html#for-developers)
```
> ibmcloud resource service-instance-create <instance-name> cloud-object-storage <plan> global
```

## Check for the newly provisioned service
You should now see the new object storage instance.
```
ibmcloud resource service-instances
```

## Create a bucket
Now that you have a service instance up and running, you can create a new bucket to store all future files to be uploaded to.
```
curl -X PUT "https://s3-api.us-geo.objectstorage.softlayer.net/<bucketname>" -H "Authorization: Bearer <token>" -H "ibm-service-instance-id: <instance-id>"
```

## List buckets
You should now see the newly added bucket listed using the command below.
```
curl "https://s3-api.us-geo.objectstorage.softlayer.net" -H "Authorization: Bearer <token>" -H "ibm-service-instance-id: <instance-id>"
```

## Further documentation for more expanded use of object storage commands
[](https://console.bluemix.net/docs/services/cloud-object-storage/cli/curl.html)

