---
title: "SoftLayer_Network_Media_Transcode_Job"
description: "The SoftLayer_Network_Media_Transcode_Job contains information regarding a transcode job such as input file, output form... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Media_Transcode_Job"
---

# SoftLayer_Network_Media_Transcode_Job
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Media_Transcode_Job' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Media_Transcode_Job' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Media_Transcode_Job contains information regarding a transcode job such as input file, output format, user id and so on. 





<!-- Service Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Method Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Service Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
-----
[autoDeleteDuration]: #autodeleteduration
#### [autoDeleteDuration]
The auto-deletion duration in seconds.  This value determines how long the input file will be kept on the storage.  
<span class="type-label">Type: </span>**integer**

-----
[byteIn]: #bytein
#### [byteIn]
The size of an input file in byte  
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
The created date  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
The internal identifier of a transcode job  
<span class="type-label">Type: </span>**integer**

-----
[inputFile]: #inputfile
#### [inputFile]
The input file name  
<span class="type-label">Type: </span>**string**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The last modified date  
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
The name of a transcode job  
<span class="type-label">Type: </span>**string**

-----
[outputFile]: #outputfile
#### [outputFile]
The output file name  
<span class="type-label">Type: </span>**string**

-----
[transcodeAccountId]: #transcodeaccountid
#### [transcodeAccountId]
The internal identifier of SoftLayer account  
<span class="type-label">Type: </span>**integer**

-----
[transcodeJobGuid]: #transcodejobguid
#### [transcodeJobGuid]
The unique id of a transcode job  
<span class="type-label">Type: </span>**string**

-----
[transcodePresetGuid]: #transcodepresetguid
#### [transcodePresetGuid]
The unique id of a pre-defined output format  
<span class="type-label">Type: </span>**string**

-----
[transcodePresetName]: #transcodepresetname
#### [transcodePresetName]
The name of a transcode output preset  
<span class="type-label">Type: </span>**string**

-----
[transcodeStatusId]: #transcodestatusid
#### [transcodeStatusId]
The internal identifier of a transcode status  
<span class="type-label">Type: </span>**integer**

-----
[userId]: #userid
#### [userId]
The internal identifier of the user who created a transcode job  
<span class="type-label">Type: </span>**integer**

-----
[watermark]: #watermark
#### [watermark]
Watermark to apply to job  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Network_Media_Transcode_Job_Watermark'>SoftLayer_Container_Network_Media_Transcode_Job_Watermark </a>**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[history]: #history
#### [history]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Media_Transcode_Job_History'>SoftLayer_Network_Media_Transcode_Job_History[] </a>**

-----
[transcodeAccount]: #transcodeaccount
#### [transcodeAccount]
The transcode service account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Media_Transcode_Account'>SoftLayer_Network_Media_Transcode_Account </a>**

-----
[transcodeStatus]: #transcodestatus
#### [transcodeStatus]
The status information of a transcode job  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Media_Transcode_Job_Status'>SoftLayer_Network_Media_Transcode_Job_Status </a>**

-----
[transcodeStatusName]: #transcodestatusname
#### [transcodeStatusName]
The status of a transcode job  
<span class="type-label">Type: </span>**string**

-----
[user]: #user
#### [user]
The SoftLayer user that created the transcode job  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**


## Count

-----
[historyCount]: #historycount
#### [historyCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>


