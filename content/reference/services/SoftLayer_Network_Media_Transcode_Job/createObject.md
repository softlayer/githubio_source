---
title: "createObject"
description: "With this method, you can create a transcode job. 

The very first step of creating a transcode job is to upload your me... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Media_Transcode_Job"
---
# SoftLayer_Network_Media_Transcode_Job::createObject
## Overview 
With this method, you can create a transcode job. 

The very first step of creating a transcode job is to upload your media files to the /in directory on your Transcode FTP space. Then, you have to pass a [[SoftLayer_Network_Media_Transcode_Job|Transcode job]] object as a parameter for this method. 

There are 4 required properties of SoftLayer_Network_Media_Transcode_Job object: transcodePresetName, transcodePresetGuid, inputFile, and outputFile. A transcode preset is a configuration that defines a certain media output.  You can retrieve all the supported presets with the [[SoftLayer_Network_Media_Transcode_Account::getPresets|getPresets]] method. You can also use [[SoftLayer_Network_Media_Transcode_Account::getPresetDetail|getPresetDetail]] method to get more information on a preset. Use these two methods to determine appropriate values for "transcodePresetName" and "transcodePresetGuid" properties. For an "inputFile", you must specify a file that exists in the /in directory of your Transcode FTP space. An "outputFile" name will be used by the Transcode server for naming a transcoded file.  An output file name must be in /out directory. If your outputFile name already exists in the /out directory, the Transcode server will append a file name with _n (an underscore and the total number of files with the identical name plus 1). 

The "name" property is optional and it can help you keep track of transcode jobs easily. "autoDeleteDuration" is another optional property that you can specify.  It determines how soon your input file will be deleted. If autoDeleteDuration is set to zero, your input file will be removed immediately after the last transcode job running on it is completed. A value for autoDeleteDuration property is in seconds and the maximum value is 259200 which is 3 days. 

An example SoftLayer_Network_Media_Transcode_Job parameter looks like this: 


* name: My transcoding
* transcodePresetName: F4V 896kbps 640x352 16x9 29.97fps
* transcodePresetGuid: {87E01268-C3E3-4A85-9701-052C9AC42BD4}
* inputFile: /in/my_birthday.wmv
* outputFile: /out/my_birthday_flash


Notice that an output file does not have a file extension.  The Transcode server will append a file extension based on an output format. A newly created transcode job will be in "Pending" status and it will be added to the Transcoding queue. You will receive a notification email whenever there is a status change on your transcode job.  For example, the Transcode server starts to process your transcode job, you will be notified via an email. 

You can add up to 3 pending jobs at a time. Transcode jobs with any other status such as "Complete" or "Error" will not be counted toward your pending jobs. 

Once a job is complete, the Transcode server will place the output file into the /out directory along with a notification email. The files in the /out directory will be removed 3 days after they were created.  You will need to use an FTP client to download transcoded files. 



### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Network_Media_Transcode_Job'>SoftLayer_Network_Media_Transcode_Job </a>| The SoftLayer_Network_Media_Transcode_Job object that you wish to create.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_Media_Transcode_JobObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Media_Transcode_Job'>SoftLayer_Network_Media_Transcode_Job </a>
