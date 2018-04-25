---
title: "get_agent_configuration.py"
description: "get_agent_configuration.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Monitoring_Agent"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Hardware_Server"
tags:
    - "monitoring"
---


```
"""
Get the configuration of the monitoring agent in a server or VSI.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Monitoring_Agent/
http://sldn.softlayer.com/article/Object-Masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

ipAddres = "5.153.59.197"

USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.Client(username=USERNAME,
                          api_key=API_KEY)
vsiService = client['SoftLayer_Virtual_Guest']
hardwareService = client['SoftLayer_Hardware_Server']

try:
    objectMask = 'mask[monitoringAgents[configurationTemplate[configurationSections[subSections]],' \
                 'configurationValues[id, value, profileId, agentId, configurationDefinitionId,' \
                 'profile, definition[attributes, section, valueType]]]]'
    server = vsiService.findByIpAddress(ipAddres, mask=objectMask)
    if not 'id' in server:
        server = hardwareService.findByIpAddress(ipAddres, mask=objectMask)
        if not 'id' in server:
            print("There is no a Server or VSI with the IP address: " + ipAddres)
            exit(1)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the server: faultCode=%s, faultString=%s"        
          % (e.faultCode, e.faultString))
    exit(1)

# We will get the configuration of the active agents
agents = [agent for agent in server['monitoringAgents'] if agent['statusName'] == "Active"]
server['monitoringAgents'] = agents

configs = []
for agent in server['monitoringAgents']:
    config = {}
    config['agent'] = agent['name']
    config['id'] = agent['id']
    sections = []
    for section in agent['configurationTemplate']['configurationSections']:
        sect = {}
        subsects = []
        hasProfile = False
        profileIds = []
        confs = []
        for subsection in section['subSections']:
            values = [value for value in agent['configurationValues'] if
                      value['definition']['sectionId'] == subsection['id']]
            for value in values:
                conf = {}
                if value['profileId'] == "":
                    conf[value['definition']['name']] = value['value']
                    confs.append(conf)
                else:
                    hasProfile = True
                    profileIds.append(value['profileId'])      
        sect['name'] = section['name']
        if not hasProfile:
            sect['configuration'] = confs
            sections.append(sect)
        else:
            profileIds = list(set(profileIds))
            profiles = []
            for profileId in profileIds:
                profile = {}
                valueConfs = []
                valueProfiles = [value for value in agent['configurationValues'] if
                                 value['profileId'] == profileId]
                profile['name'] = valueProfiles[0]['profile']['name']
                for valueProfile in valueProfiles:
                    value = {}
                    value[valueProfile['definition']['name']] = valueProfile['value']
                    valueConfs.append(value)
                profile['configuration'] = valueConfs
                profiles.append(profile)
            sect['profiles'] = profiles
            sections.append(sect)
    config['sections'] = sections
    configs.append(config)
print(json.dumps(configs, sort_keys=True, indent=2, separators=(',', ': ')))

```
