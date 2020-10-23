---
title: "SoftLayer_Network_Media_Transcode_Account"
description: "Transcoding is a service which allows you to transcode media files to different formats. For example, if you have a Wind... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Media_Transcode_Account"
---
# SoftLayer_Network_Media_Transcode_Account
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Media_Transcode_Account' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Media_Transcode_Account' >Datatype</a></li>
    </ul>
</div>

## Description
Transcoding is a service which allows you to transcode media files to different formats. For example, if you have a Windows Media Video file you wish to stream in Flash Video format, transcoding would be the process to make this change. Individual SoftLayer customer can have a single Transcode account and you need to create a Transcode account to use the service. To create a Transcode account, go to the "Private Network" -> "Transcoding" page in the SoftLayer [https://manage.softlayer.com customer portal] or invoke [SoftLayer_Network_Media_Transcode_Account::createTranscodeAccount]({{<ref "reference/services/SoftLayer_Network_Media_Transcode_Account/createTranscodeAccount">}}) method. 

SoftLayer Transcoding service supports a large number of video and audio codecs. This means you can transcode many different types of movies.  Refer to [http://knowledgelayer.softlayer.com/questions/409/SoftLayer+Transcoding+FAQ Transcode FAQ] for supported codes and media containers. Transcode server also has hundreds of pre-defined output formats that you can choose from. 

A Transcode account object allows you to communicate with the Transcode FTP (transcode.service.softlayer.com server) server and Transcode server. You can retrieve a directory listing, details on a media file, Transcode output presets, and Transcode FTP login credentials. Most importantly, you can create transcode jobs through your Transcode account. 

When a Transcode account is created, it creates an FTP account on the Transcode FTP. You can upload your media files to the /in directory and you can download transcoded media files from the /out directory. You can keep the files 3 days from the creation date. They will be automatically deleted after this point. For more details on the Transcode FTP server, refer to [SoftLayer_Network_Media_Transcode_Account::getFtpAttributes]({{<ref "reference/services/SoftLayer_Network_Media_Transcode_Account/getFtpAttributes">}}) method. 

### External Links


* [Transcode FAQ](http://knowledgelayer.softlayer.com/questions/409/SoftLayer+Transcoding+FAQ)


* [Transcode Wiki](http://en.wikipedia.org/wiki/Transcoding)




### seeAlso

* [SoftLayer_Network_Media_Transcode_Job](/reference/services/SoftLayer_Network_Media_Transcode_Job )


        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [createTranscodeAccount](/reference/services/SoftLayer_Network_Media_Transcode_Account/createTranscodeAccount)
Creates a new transcode account
</div>

<div class="method-row">

#### [createTranscodeJob](/reference/services/SoftLayer_Network_Media_Transcode_Account/createTranscodeJob)
Creates a transcode job
</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Network_Media_Transcode_Account/getAccount)
Retrieve the SoftLayer account information
</div>

<div class="method-row">

#### [getDirectoryInformation](/reference/services/SoftLayer_Network_Media_Transcode_Account/getDirectoryInformation)
Returns a directory listing
</div>

<div class="method-row">

#### [getFileDetail](/reference/services/SoftLayer_Network_Media_Transcode_Account/getFileDetail)
Returns detailed information on a video or audio file
</div>

<div class="method-row">

#### [getFtpAttributes](/reference/services/SoftLayer_Network_Media_Transcode_Account/getFtpAttributes)
Returns Transcode FTP login credentials
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_Media_Transcode_Account/getObject)
Retrieve a SoftLayer_Network_Media_Transcode_Account record.
</div>

<div class="method-row">

#### [getPresetDetail](/reference/services/SoftLayer_Network_Media_Transcode_Account/getPresetDetail)
Returns details on a transcode output preset
</div>

<div class="method-row">

#### [getPresets](/reference/services/SoftLayer_Network_Media_Transcode_Account/getPresets)
Returns an array of transcoding preset objects
</div>

<div class="method-row">

#### [getTranscodeJobs](/reference/services/SoftLayer_Network_Media_Transcode_Account/getTranscodeJobs)
Retrieve transcode jobs
</div>
</div>

</div>

