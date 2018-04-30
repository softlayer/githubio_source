---
title: "objectStoragetest.php"
description: "objectStoragetest.php"
date: "2018-04-25"
classes: 
tags:
    - "objectstorage"
---


```
<?php

require_once ('softlayer-object-storage-php-master/lib/ObjectStorage/Util.php');


 # Configuring the object storage
 $options = array('adapter' => ObjectStorage_Http_Client::SOCKET, 'timeout' => 10);
 $host = 'https://dal05.objectstorage.service.networklayer.com/auth/v1.0/'; // the SoftLayer Object Storage API host
 $username = 'SLOS207819-16:SL207819'; // user name and password is display at https://manage.softlayer.com/ObjectStorage/index
 $password = 'apikey_goes_here';
 $objectStorage = new ObjectStorage($host, $username, $password, $options);
 
 # the name of your container, this container will be used to add a new file
 $containerName = 'test';
        #$newCdnContainerName = $containerName;
 # the path for the new file to add
 # in this case we are going to add the file "object.txt"
 # to the container "testContainer"
 $newObjectName = $containerName . '/objectTest1.txt';
 # setting the metadata key value for the new file
 $metaKey = 'Description';
 # setting the metadata value for the new file
 $metaData = 'META DATA TO TEST FOR CDN CONTAINER';
 # setting the ttl value for the new file
 #$ttl = 12345;

 # Adding the new file to the container       
 $newObject = $objectStorage->with($newObjectName)
                        ->setBody('Test file to test') # the boby of the file
                        ->setMeta($metaKey,$metaData)
                        ->create();
        
var_dump($newObject);
# how to create a container        
#$newContainer = $objectStorage->with($newCdnContainerName)
#                            ->setMeta($metaKey, $metaData)
#                            ->enableCdn()
#                            ->setTtl($ttl)
#                            ->create();


#var_dump($newContainer);
#$objectStorage->with('containerTestRaul/'.$videoFileName)->purgeCache(); //$videFileName is the file name of the video.
#$objectStorage->with('containerTestRaul/'.$videoFileName)->loadCache(); //$videFileName is the file name of the video.
#$videoObject = $objectStorage->with('containerTestRaul/'.$videoFileName)->setContext('cdn')->setLocalFile($fileFullPath)->create(); ////$fileFullPath is the path of the file of temp folder

?>
```
