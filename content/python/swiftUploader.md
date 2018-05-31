---
title: 'Object Storage Uploader'
description: 'Import customer-supplied Virtual Hard Disks (VHDs) to our object storage offering.'
date: '2017-09-13'
author: 'Adam Shaw'
classes:
    - "Swift"
tags:
    - "swift"
    - "tools"
    - "template"
---

## Overview
We’ve recently added the option to import customer-supplied Virtual Hard Disks (VHDs) to our object storage offering. This is a great option for our customers who may have special virtual machines that they have spent hours perfecting. Since learning to import these images can pose a slight challenge, especially for those unfamiliar with object storage (OpenStack Swift), I wrote this blog to share scripts that will streamline the process.

## Object Storage
SoftLayer’s object storage is an enhanced version of OpenStack Swift. Although we’ve added features to it, the API (on the whole) is still the same. Two requirements of particular importance to storing disk images are limitations and requirements on large files. Swift limits all files to be 5GB or less. To support larger files users need to create a manifest file that combines smaller files into one large file.

For example, to upload a 12GB VHD, the user is expected to segment the file into at least three files and then create a manifest that brings them back together.

## Easier Importing
Since many people don’t have the time to learn the inner workings of Swift and would just like to get VHDs running on their servers, I have created a set scripts to simplify the process. They handle the authentication, file segmentation, and dynamic manifest creation for you, so you can get up and running quickly. You can easily access them here .

You can use a Bash script or a Python 3 script. Both do the same thing, but depending on your environment you may prefer one over the other.

But before we jump into the scripts, you’ll need to find your object storage username and password.

To get those, log in to http://control.softlayer.com, go to Storage->Object Storage, select your cluster (I would suggest Dallas 5 for your first tests), and then click “View Credentials” in the top left of the page. You will be presented with a modal window containing your username and API Key (or password) for object storage.

## ObjectStorageUploader.sh - Bash Edition
The idea behind this script is to have as little user interaction as possible. By calling the script with the proper parameters, you are able to walk away and let it do its thing.

Simply place the bash script in your directory of VHDs. Call the script by passing in the image you want to upload, the location to upload it (container/filename), and your Swift username and password.

$ ./ObjectStorageUpload.sh myOS.vhd 'myContainer/myOS.vhd' 'SLOS1234-1:SL1234' 'apikey'

It will begin the process of walking through the segments of the file and building up your object in object storage.

## ObjectStorageUploader.py - Python 3 Edition
Before we begin, make sure you have installed the latest version of Python 3 located here: https://www.python.org/downloads/

Any Python 3 release will work, but I have been using Python 3.4.0 for my testing.

The idea behind this script is to actually walk you through the process of uploading a file to Swift. Use this script via supplied parameters, in “interactive mode,” or a combination of the two. This is particularly handy for Windows users who are newer to scripting. Simply drop the script in the folder containing your VHDs, run it, and let it guide you through uploading the image to object storage.

To execute the script, place it in the directory where you store your VHDs and double click it. It will then prompt you to select the file you want to upload.

After selecting your file, you will be asked for your Swift username and password. Authentication will be attempted and, if successful, the list of containers in your cluster will be presented.

Select the container you want to upload to and the script will begin uploading the VHD to object storage.

If you prefer the command line arguments approach, you can pass in arguments to this script too. The signature is slightly different since all the opinions are optional.

$ python ObjectStorageUpload.py -f myOS.vhd -t 'myContainer/myOS.vhd' -u 'SLOS1234-1:SL1234'

## Importing Uploaded VHD as Image Templates
Now that your image is in object storage you can import your VHD into the SoftLayer template, so you can use it to provision a new virtual server!

Go to your image templates page in the portal and click the “Import Image” tab. Select the Swift account, cluster, container, and file that you uploaded. Give your new template a name and some notes. Make sure to fill out the Operating System information properly as this is used when setting up your new server, and finally click “Import.”

Lastly, you will be emailed after the VHD has been processed by our system.

-Adam Shaw

```python
# ================================================================================
#     ObjectStorageUploader.py
#     © Copyright IBM Corporation 2014.
#     LICENSE: MIT (http://opensource.org/licenses/MIT)    
# ================================================================================

import argparse
import os
import math
import http.client
import time
import datetime
from urllib.parse import urlparse
from urllib.parse import quote



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="file to upload to SWIFT")
    parser.add_argument("-u", "--username", help="SWIFT username")
    parser.add_argument("-p", "--password", help="SWIFT password (SoftLayer API key)")
    parser.add_argument("-c", "--cluster", help="SWIFT cluster to use (default: dal05.objectstorage.softlayer.net)")
    parser.add_argument("-t", "--target", help="location on SWIFT cluster to store file (container/filename.vhd)")
    args = parser.parse_args()

    if not args.file:
        filename = select_file()
    else:
        filename = args.file

    if not args.username:
        swift_user_name, swift_password = get_swift_credentials()
    else:
        swift_user_name = args.username
        swift_password = args.password

    if not args.cluster:
        storage_url, auth_token = authenticate_swift(
            swift_user_name,
            swift_password,
            "dal05.objectstorage.softlayer.net"
        )
    else:
        storage_url, auth_token = authenticate_swift(
            swift_user_name,
            swift_password,
            args.cluster
        )

    if not args.target:
        container = select_container(storage_url, auth_token)
        swift_target_path = "{}/{}".format(container, quote(filename))
    else:
        swift_target_path = args.target

    upload_file(filename, swift_target_path, storage_url, auth_token)


def select_file():
    current_path = (os.path.dirname(os.path.realpath(__file__)))
    print("Files in {}".format(current_path))
    files = get_file_list(current_path)
    return prompt_for_choice(files, "Select file for upload:")


def get_file_list(path):
    files = []
    for file in os.listdir(path):
        if os.path.isfile(file):
            files.append(file)
    return files


def prompt_for_choice(list, prompt_label):
    for i, item in enumerate(list):
        if len(item):
            print("{}) {}".format(i, item))
    selected_index = input(prompt_label)
    if selected_index.isdigit():
        if 0 <= int(selected_index) < len(list):
            print()
            return list[int(selected_index)]

    print("Invalid Input: {}".format(selected_index))
    return prompt_for_choice(list, prompt_label)


def get_swift_credentials():
    swift_user_name = input("Swift Username:")
    swift_password = input("Swift Password:")
    return swift_user_name, swift_password


def authenticate_swift(swift_user_name, swift_password, selected_endpoint=""):
    if selected_endpoint == "":
        swift_endpoints = [
            "dal05.objectstorage.softlayer.net",
            "sng01.objectstorage.softlayer.net",
            "ams01.objectstorage.softlayer.net",
        ]
        selected_endpoint = prompt_for_choice(
            swift_endpoints,
            "Select Object Storage Endpoint:"
        )

    print("Authenticating...")
    headers = {
        "X-Storage-User": swift_user_name,
        "X-Storage-Pass": swift_password
    }
    try:
        response = object_storage_request(
            selected_endpoint,
            "/auth/v1.0/",
            headers
        )
    except Exception:
        swift_user_name, swift_password = get_swift_credentials()
        return authenticate_swift(swift_user_name, swift_password)
    print("Success!")

    storage_url = response.getheader("X-Storage-Url")
    auth_token = response.getheader("X-Auth-Token")

    return storage_url, auth_token


def select_container(storage_url, auth_token):
    url_tuple = urlparse(storage_url)

    headers = {"X-Auth-Token": auth_token}
    try:
        response = object_storage_request(
            url_tuple.netloc,
            url_tuple.path,
            headers
        )
    except Exception:
        swift_user_name, swift_password = get_swift_credentials()
        storage_url, auth_token = authenticate_swift(swift_user_name, swift_password)
        return select_container(storage_url, auth_token)

    containers = response.read().decode("utf-8").split("\n")
    return prompt_for_choice(containers, "Select Container:")


def object_storage_request(server, path, headers, method="GET", data=""):
    connection = http.client.HTTPConnection(server)
    connection.request(method, path, data, headers)
    response = connection.getresponse()

    if 200 <= response.getcode() < 300:
        return response

    print("Error {}: {}".format(response.status, response.reason))
    raise Exception(response.status, response.reason)


def upload_file(filename, swift_target_path, storage_url, auth_token):
    url_tuple = urlparse(storage_url)
    headers = {"X-Auth-Token": auth_token}

    file_size = os.path.getsize(filename)
    block_size = 1048576
    chunk_size = 5 * block_size
    chunks = math.ceil(file_size / chunk_size)

    print("Reading in file")
    file = open(filename, 'rb')
    print("Uploading {} to \"{}\"".format(filename, swift_target_path))
    retry = 0
    i = 0
    while i < chunks:
        try:
            data = file.read(chunk_size)
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            print("Uploading part {} of {} at {}".format(i + 1, chunks, st))
            chunk_name = "chunk-{0:0>5}".format(i)
            object_storage_request(
                url_tuple.netloc,
                "{}/{}/{}".format(url_tuple.path, swift_target_path, chunk_name),
                headers,
                "PUT",
                data)
            i += 1
        except Exception as e:
            print ('failed to upload chunk with exception ' + str(e))
            retry += 1
            if retry == 4:
                return

    try:
        print("Writing manifest file")
        headers = {
            "X-Auth-Token": auth_token,
            "X-Object-Manifest": swift_target_path,
            "Content-Length": 0,
        }
        object_storage_request(
            url_tuple.netloc,
            "{}/{}".format(url_tuple.path, swift_target_path),
            headers,
            "PUT"
        )
    except Exception:
        return

    print("File Uploaded!")

if __name__ == "__main__":
    main()

```


```bash
#!/bin/bash
# ================================================================================
#     ObjectStorageUploader.sh
#     © Copyright IBM Corporation 2014.
#     LICENSE: MIT (http://opensource.org/licenses/MIT)    
# ================================================================================

#./objectstorageupload.sh dsl-4.4.10.iso 'myContainer/file.vhd' 'SLOS1234-1:SL1234' 'apikey'

fileToUpload=$1
swiftTargetPath=$2
swiftUsername=$3
swiftPassword=$4

swiftEndpoint='https://dal05.objectstorage.softlayer.net/auth/v1.0/'

apiResponse=$(curl -X GET -H "X-Storage-User: $swiftUsername" -H "X-Storage-Pass: $swiftPassword" -s -i $swiftEndpoint)
swiftAuthToken=$(echo "$apiResponse" | grep "X-Auth-Token:" | sed 's/X-Auth-Token: //g' | tr -d '\r')
swiftStorageUrl=$(echo "$apiResponse" | grep "X-Storage-Url:" | sed 's/X-Storage-Url: //g' | tr -d '\r')

fileSize=$(wc -c $fileToUpload | awk '{print $1}')
blockSize=1048576
let chunkSize=2048 #2GB chunks
let chunks=($fileSize/$blockSize+$chunkSize-1)/$chunkSize;

for ((i=0; i<chunks; i++))
do
   printf -v chunkName "chunk-%05d" $i
   let skipChunk=$i*chunkSize

   dd if=$fileToUpload bs=$blockSize count=$chunkSize skip=$skipChunk | curl -X PUT -H "X-Auth-Token: $swiftAuthToken" --data-binary @- "$swiftStorageUrl/$swiftTargetPath/$chunkName"
done

curl -X PUT -H "X-Auth-Token: $swiftAuthToken" -H "X-Object-Manifest: $swiftTargetPath" -H "Content-Length: 0" $swiftStorageUrl/$swiftTargetPath
```

Originally from [SLDN](https://sldn.softlayer.com/blog/ashaw/object-storage-uploader)