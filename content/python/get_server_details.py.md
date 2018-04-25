---
title: "get_server_details.py"
description: "get_server_details.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
"""
Get Bare Metal details.

Retrieve a list of bare metal servers in the account and print
a report with server hostname, domain, login info, network, CPU,
and RAM details.
This script makes a single call to the getHardware() method in the
SoftLayer_Account API service  and uses an object mask to retrieve
related information.
See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server/

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

"""
Your SoftLayer API username and key.

Generate an API key at the SoftLayer Customer Portal:
https://manage.softlayer.com/Administrative/apiKeychain
"""
# Your SoftLayer API username and key.
API_USERNAME = 'set-me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set-me'

"""
Add an object mask to retrieve our hardwares' related items such as its
operating system, hardware components, and network components. Object masks
can retrieve any information related to your object. See
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
# for a list of the relational properties you can retrieve along with hardware.
"""
objectMask = 'processors, processorCount, memory, memoryCount, networkComponents, ' \
             'primaryIpAddress, operatingSystem.passwords'


# Declare a new API service object.
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

try:
    # Make the call to retrieve our bare metal servers.`
    hardwareList = accountService.getHardware(mask=objectMask)
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to retrieve the bare metal list. \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

for hardware in hardwareList:
    passwords = {}
    passwords['username'] = "no username"
    passwords['password'] = "no password"
    if len(hardware['operatingSystem']['passwords']) >= 1:
        passwords = hardware['operatingSystem']['passwords'][0]
        """
    private network ports. Save MAC addresses.
    Go through the hardware's network components to get it's public and
    """
        networks = hardware['networkComponents']
    publicMacAddress = 'not found'
    privateMacAddress = 'not found'
    for network in networks:
        """
        SoftLayer uses eth0 on the private network and eth1 on the public
        network.
        """
        if network['name'] == 'eth' and network['port'] == 0:
            privateMacAddress = network['macAddress']
        elif network['name'] == 'eth' and network['port'] == 1:
            publicMacAddress = network['macAddress']

    """
    Hardware can only have like processors in them, so use the first item in
    the processors array to get the type of processor in the server.
    """
    processorType = hardware['processors'][0]['hardwareComponentModel']['hardwareGenericComponentModel']['capacity'] +\
                    hardware['processors'][0]['hardwareComponentModel']['hardwareGenericComponentModel']['units'] + " " +\
                    hardware['processors'][0]['hardwareComponentModel']['hardwareGenericComponentModel']['description']

    # Treat memory the same way we did processors.
    memoryType = hardware['memory'][0]['hardwareComponentModel']['hardwareGenericComponentModel']['capacity'] +\
                 hardware['memory'][0]['hardwareComponentModel']['hardwareGenericComponentModel']['units'] + " " +\
                 hardware['memory'][0]['hardwareComponentModel']['hardwareGenericComponentModel']['description']

    # All done! Print hardware info.
    print("Hostname: " + hardware['hostname'])
    print("Domain: " + hardware['domain'])
    print("Login: " + passwords['username'] + "/" + passwords['password'])

    # Check if Server was ordered with public & private network
    # or just Private network only.
    if 'primaryIpAddress' in hardware:
        print("Public IP Address: " + hardware['primaryIpAddress'])
    else:
        print("** Private Network Only server **")

    print("Public MAC Address: " + publicMacAddress)
    print("Private IP Address: " + hardware['privateIpAddress'])
    print("Private MAC Address: " + privateMacAddress)
    print("CPUs: " + str(hardware['processorCount']) + "x " + processorType)
    print("RAM: " + str(hardware['memoryCount']) + "x " + memoryType)
    print(" ")

```
