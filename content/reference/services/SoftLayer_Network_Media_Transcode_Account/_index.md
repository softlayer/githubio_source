---
title: "SoftLayer_Network_Media_Transcode_Account"
description: "Transcoding is a service which allows you to transcode media files to different formats. For example, if you have a Windows Media Video file you wish to stream in Flash Video format, transcoding would be the process to make this change. Individual SoftLayer customer can have a single Transcode account and you need to create a Transcode account to use the service. To create a Transcode account, go to the 'Private Network' -> 'Transcoding' page in the SoftLayer [https://manage.softlayer.com customer portal] or invoke [[SoftLayer_Network_Media_Transcode_Account::createTranscodeAccount|createTranscodeAccount]] method. 

SoftLayer Transcoding service supports a large number of video and audio codecs. This means you can transcode many different types of movies.  Refer to [http://knowledgelayer.softlayer.com/questions/409/SoftLayer+Transcoding+FAQ Transcode FAQ] for supported codes and media containers. Transcode server also has hundreds of pre-defined output formats that you can choose from. 

A Transcode account object allows you to communicate with the Transcode FTP (transcode.service.softlayer.com server) server and Transcode server. You can retrieve a directory listing, details on a media file, Transcode output presets, and Transcode FTP login credentials. Most importantly, you can create transcode jobs through your Transcode account. 

When a Transcode account is created, it creates an FTP account on the Transcode FTP. You can upload your media files to the /in directory and you can download transcoded media files from the /out directory. You can keep the files 3 days from the creation date. They will be automatically deleted after this point. For more details on the Transcode FTP server, refer to [[SoftLayer_Network_Media_Transcode_Account::getFtpAttributes|getFtpAttributes]] method. "
date: "2018-02-12"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Media_Transcode_Account"
type: "reference"
layout: "service"
mainService : "SoftLayer_Network_Media_Transcode_Account"
---
