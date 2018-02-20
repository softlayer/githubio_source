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
Transcoding is a service which allows you to transcode media files to different formats. For example, if you have a Windows Media Video file you wish to stream in Flash Video format, transcoding would be the process to make this change. Individual SoftLayer customer can have a single Transcode account and you need to create a Transcode account to use the service. To create a Transcode account, go to the "Private Network" -> "Transcoding" page in the SoftLayer [https://manage.softlayer.com customer portal] or invoke [[SoftLayer_Network_Media_Transcode_Account::createTranscodeAccount|createTranscodeAccount]] method. 

SoftLayer Transcoding service supports a large number of video and audio codecs. This means you can transcode many different types of movies.  Refer to [http://knowledgelayer.softlayer.com/questions/409/SoftLayer+Transcoding+FAQ Transcode FAQ] for supported codes and media containers. Transcode server also has hundreds of pre-defined output formats that you can choose from. 

A Transcode account object allows you to communicate with the Transcode FTP (transcode.service.softlayer.com server) server and Transcode server. You can retrieve a directory listing, details on a media file, Transcode output presets, and Transcode FTP login credentials. Most importantly, you can create transcode jobs through your Transcode account. 

When a Transcode account is created, it creates an FTP account on the Transcode FTP. You can upload your media files to the /in directory and you can download transcoded media files from the /out directory. You can keep the files 3 days from the creation date. They will be automatically deleted after this point. For more details on the Transcode FTP server, refer to [[SoftLayer_Network_Media_Transcode_Account::getFtpAttributes|getFtpAttributes]] method. 
### external links
        Array
(
    [url] => http://knowledgelayer.softlayer.com/questions/409/SoftLayer+Transcoding+FAQ
    [description] => Transcode FAQ
)
1        Array
(
    [url] => http://en.wikipedia.org/wiki/Transcoding
    [description] => Transcode Wiki
)
1        
### seeAlso
        SoftLayer_Network_Media_Transcode_Job1                
        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Media_Transcode_Account/createTranscodeAccount'> createTranscodeAccount</a> </span>
            <div class='views-field-body'>Creates a new transcode account</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Media_Transcode_Account/createTranscodeJob'> createTranscodeJob</a> </span>
            <div class='views-field-body'>Creates a transcode job</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Media_Transcode_Account/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer account information</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Media_Transcode_Account/getDirectoryInformation'> getDirectoryInformation</a> </span>
            <div class='views-field-body'>Returns a directory listing</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Media_Transcode_Account/getFileDetail'> getFileDetail</a> </span>
            <div class='views-field-body'>Returns detailed information on a video or audio file</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Media_Transcode_Account/getFtpAttributes'> getFtpAttributes</a> </span>
            <div class='views-field-body'>Returns Transcode FTP login credentials</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Media_Transcode_Account/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_Media_Transcode_Account record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Media_Transcode_Account/getPresetDetail'> getPresetDetail</a> </span>
            <div class='views-field-body'>Returns details on a transcode output preset</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Media_Transcode_Account/getPresets'> getPresets</a> </span>
            <div class='views-field-body'>Returns an array of transcoding preset objects</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Media_Transcode_Account/getTranscodeJobs'> getTranscodeJobs</a> </span>
            <div class='views-field-body'>Retrieve transcode jobs</div>
        </div>
        </div>
</div>

