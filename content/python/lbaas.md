---
title: "LBaaS Examples"
description: "A variety of examples on how to interact with the Load Balancer as a Service offering"
date: "2018-07-25"
classes: 
    - "SoftLayer_Network_LBaaS_LoadBalancer"
    - "SoftLayer_Network_LBaaS_Member"
    - "SoftLayer_Network_LBaaS_Listener"
tags:
    - "lbaas"
    - "loadbalancers"
---

This example covers a variety of API calls that you might want to use when interacting with the Load Balancer as a Service offering. General information about this service can be found on the [Load Balancer as a Service Documentation](https://console.bluemix.net/docs/infrastructure/loadbalancer-service/getting-started.html#getting-started)

```python
"""
Manages LBaaS instances.

This sample shows how to use a variety of the common methods when working with LBaaS instances. This example is more a proof of concept to show basically how it all works, and not really intended to be used as is.
"""

import SoftLayer
import json

class lbaas():
    GREEN = '\033[92m'    
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    def __init__(self):
        self.client = SoftLayer.Client()
        self.orderData = {}

    def getLBaaSByName(self, name):
        """Finds a LBaaS instance uuid based on its name """
        filter = {"name":{"operation": name}}
        lbaas_items = self.client['Network_LBaaS_LoadBalancer'].getAllObjects(filter=filter)
        if not lbaas_items:
            print("The LBaaS name '%s' doesn't exists." % name)
        else:
            return lbaas_items[0]['uuid']

    def getLBaaSById(self, lbaasId):
        """Finds a LBaaS instance based uuid on its Id"""
        lbaas = self.client['Network_LBaaS_LoadBalancer'].getObject(id=lbaasId)
        return lbaas['uuid']

    def cancelLBaaS(self, uuid):
        """ Cancel a Load Balancer as a Service """
        try:
            response = self.client['Network_LBaaS_LoadBalancer'].cancelLoadBalancer(uuid)

            if response:
                print("The LBaaS was successfuly canceled")

        except (SoftLayer.SoftLayerAPIError, Exception) as e:            
            print("Unable to cancel the LBaaS: %s, %s" % (e.faultCode, e.faultString))

    def addProtocols(self, uuid, protocolConfig):
        """ This sample shows how to add protocols to the LBaaS.
            https://softlayer.github.io/reference/services/SoftLayer_Network_LBaaS_Listener/updateLoadBalancerProtocols/
            https://softlayer.github.io/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancerProtocolConfiguration
        """
        try:
            # Create the service and add the protocols
            lbaasListenerService = self.client['Network_LBaaS_Listener']
            response = lbaasListenerService.updateLoadBalancerProtocols(uuid, protocolConfig)

            print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))

        except (SoftLayer.SoftLayerAPIError, Exception) as e:            
            print("Unable to add protocols: %s, %s" % (e.faultCode, e.faultString))


    def addServerInstances(self, uuid, serverInstances):
        """ This sample shows how to add server instances to the LBaaS.
            https://softlayer.github.io/reference/services/SoftLayer_Network_LBaaS_Member/addLoadBalancerMembers/
            https://softlayer.github.io/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancerServerInstanceInfo/
        """
        try:
            # Create the service and add new members (server instances)
            lbaasMemberService = self.client['Network_LBaaS_Member']
            response = lbaasMemberService.addLoadBalancerMembers(uuid, serverInstances)

            print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))

        except (SoftLayer.SoftLayerAPIError, Exception) as e:            
            print("Unable to add members (server instances): %s, %s" % (e.faultCode, e.faultString))

    def removeServerInstances(self, uuid, members=None):
        """ This sample shows how to remove LBaaS servers (members).
        https://softlayer.github.io/reference/services/SoftLayer_Network_LBaaS_LoadBalancer/getLoadBalancer
        https://softlayer.github.io/reference/services/SoftLayer_Network_LBaaS_Member/deleteLoadBalancerMembers/
        https://softlayer.github.io/reference/services/SoftLayer_Network_LBaaS_LoadBalancer/getMembers/
        """
        try:
            # Create the service and delete selected server instances
            lbaasMemberService = self.client['Network_LBaaS_Member']
            response = lbaasMemberService.deleteLoadBalancerMembers(uuid, members)

            print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))

        except (SoftLayer.SoftLayerAPIError, Exception) as e:            
            print("Unable to remove instances: %s, %s" % (e.faultCode, e.faultString)) 

    def title(self, text):
        """Prints out a pretty colored title"""
        return self.GREEN + self.UNDERLINE + "\n" + text + self.END + "\n"

    def convertToMB(self, value):    
        """quick math"""
        return "{0:.2f}".format(float(value)/(10**6))
   
    def printOverview(self, uuid, listeners):
        """Prints out some general info about a LBaaS"""
        statusTable = PrettyTable(['Instances Up','Instances Down'])
        metricsTable = PrettyTable(['Throughput (bps)','Data Processed (MB)', 
                                    'Conection Rate (cps)', 'Active Connections'])
        healthTable = PrettyTable(['Front-End Protocol','Front-End Port', 
                                   'Back-End Protocol', 'Back-End Port', 'Is Healthy'])

        statusTable.title = "SERVER STATUS"
        metricsTable.title = "METRICS"
        healthTable.title = "HEALTH STATUS"
                        
        try:  
            # Following retrieves statistics anmd members which are used to print 
            # information about status and metrics         
            statics = self.client['Network_LBaaS_LoadBalancer'].getLoadBalancerStatistics(uuid)
            members = self.client['Network_LBaaS_LoadBalancer'].getLoadBalancerMemberHealth(uuid)

            # Adding data about status and metrics
            statusTable.add_row([statics['numberOfMembersUp'], statics['numberOfMembersDown']])
            metricsTable.add_row([statics['throughput'], self.convertToMB(statics['dataProcessedByMonth']), 
                                  statics['connectionRate'], statics['totalConnections']])
            # Adding data about health status if there are members
            if members:
                for listener in listeners:
                    for member in members:
                        if listener['defaultPool']['uuid'] == member['poolUuid']:
                            healthy = all(m['status'] == "UP" for m in member['membersHealth'])

                    healthTable.add_row([listener['protocol'], listener['protocolPort'], 
                                         listener['defaultPool']['protocol'], 
                                         listener['defaultPool']['protocolPort'], healthy])

            print (self.title("OVERVIEW:"))
            print (statusTable)
            print (metricsTable)
            print (healthTable)

        except SoftLayer.SoftLayerAPIError as e:            
            print("Unable to retrieve LBaaS overview:: %s, %s" % (e.faultCode, e.faultString))
    
    def printServerInstances(self, dc, members):
        """Prints out some details about the servers on a LB"""
        instancesTable = PrettyTable(['Id','Name','Type','Private Ip', 'Weight'])

        # Filters in order to retrieve only instances in the same datacenter
        guestFilter = {"virtualGuests":{"datacenter":{"name":{"operation": dc}}}}
        hardwareFilter = {"hardware":{"datacenter":{"name":{"operation": dc}}}}
        mask = "mask[id,fullyQualifiedDomainName,primaryBackendIpAddress]"
        # Retrieve instances
        guests = self.client['Account'].getVirtualGuests(filter=guestFilter, mask=mask)
        servers = self.client['Account'].getHardware(filter=hardwareFilter, mask=mask)

        # Adding data to the table about the instances  
        for m in members:
            for g in guests:
                if g['primaryBackendIpAddress'] == m['address']:
                    instancesTable.add_row([g['id'], g['fullyQualifiedDomainName'],
                                            "Virtual Server",m['address'], m['weight']])
            
            for s in servers:
                if s['primaryBackendIpAddress'] == m['address']:
                    instancesTable.add_row([s['id'], s['fullyQualifiedDomainName'],
                                            "Hardware Server",m['address'], m['weight']])

        print (self.title("SERVER INSTANCES:"))
        print (instancesTable)
    
    def printHealthChecks(self, listeners, healthMonitors):
        healthMTable = PrettyTable(['Protocol','Port','Interval (sec)',
                                   'Timeout (sec)', 'Max Trials'])
        # Adding data to the table
        for hm in healthMonitors:
            for l in listeners:
                if l['defaultPool']['healthMonitor']['uuid'] == hm['uuid']:
                    healthMTable.add_row([hm['monitorType'], l['defaultPool']['protocolPort'], 
                                          hm['interval'], hm['timeout'], hm['maxRetries']])

        print (self.title("HEALTH CHECKS:"))
        print (healthMTable)

    def printDetails(self, uuid, servers=False, checks=False):
        """Prints out details of a LBaaS"""
        table = PrettyTable(['ID','UUID','Description', 
                             'Address', 'Type', 'Location', 'Status'])
                        
        try:
            # Retrieve needed LBaaS information by using masks in the getLoadBalancer method
            mask = "mask[members,listeners[defaultPool[healthMonitor]],healthMonitors]"
            lbaas = self.client['Network_LBaaS_LoadBalancer'].getLoadBalancer(uuid, mask=mask)
            
            isPublic = "Public" if lbaas['isPublic'] == 1 else "Private"
            # Adding data to the table
            table.title = "LBaaS Name: " + lbaas['name']
            table.add_row([lbaas['id'], lbaas['uuid'], lbaas['description'], lbaas['address'],
                              isPublic,lbaas['datacenter']['longName'],lbaas['operatingStatus']])

            print (self.title("DETAILS:"))
            print (table)

            self.printOverview(uuid, lbaas['listeners'])

            if servers:
                self.printServerInstances(lbaas['datacenter']['name'], lbaas['members'])
            
            if checks:
                self.printHealthChecks(lbaas['listeners'], lbaas['healthMonitors'])
            
        except SoftLayer.SoftLayerAPIError as e:            
            print("Unable to retrieve LBaaS details: %s, %s" % (e.faultCode, e.faultString))

    def selectProtocol(self, uuid):
        """It prints a table and waits until an option is selected"""
        protocolTable = PrettyTable(['Option','UUID','Front-End Protocol','Front-End Port', 
                                     'Back-End Protocol', 'Back-End Port'])
        protocolTable.title = "PROTOCOLS"
        
        # Retrieve the listeners in LBaaS using masks
        mask = "mask[members,listeners[defaultPool]]"
        lbaas = self.client['Network_LBaaS_LoadBalancer'].getLoadBalancer(uuid, mask=mask)
        listeners = lbaas['listeners']

        # Adding data about health status if there are members
        for l in listeners:
            protocolTable.add_row([str(listeners.index(l)), l['uuid'],
                                   l['protocol'], l['protocolPort'], 
                                   l['defaultPool']['protocol'], 
                                   l['defaultPool']['protocolPort']])

        print (protocolTable)
        var = int(input("\n\nSelect the protocol you want to remove (0 to " + str(len(listeners) - 1) + ") : "))

        return [str(protocolTable._rows[var][1])]

    def removeProtocols(self, uuid, listeners=None):
        """Removes the selected protocols from a LBaaS"""
        if not listeners:
            listeners = self.selectProtocol(uuid)

        try:
            # Create the service and delete selected protocols
            lbaasListenerService = self.client['Network_LBaaS_Listener']
            response = lbaasListenerService.deleteLoadBalancerProtocols(uuid, listeners)

            print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))

        except (SoftLayer.SoftLayerAPIError, Exception) as e:            
            print("Unable to remove the protocols: %s, %s" % (e.faultCode, e.faultString))

    def listLBaaSItems(self, dc=None):
        """ List all LBaaS items in the account. """
        filter = None
        table = PrettyTable(['ID','UUID','Name', 'Description', 
                             'Address', 'Type', 'Location', 'Status'])
        
        if dc:
            filter = {"datacenter":{"name":{"operation": dc}}}
        
        try:
            # Retrieves all LBaaS in the account
            items = self.client['Network_LBaaS_LoadBalancer'].getAllObjects(filter=filter)
            # Add data to the table and print the list
            for i in items:
                isPublic = "Public" if i['isPublic'] == 1 else "Private"
                table.add_row([i['id'], i['uuid'], i['name'], i['description'], i['address'],
                              isPublic,i['datacenter']['longName'],i['operatingStatus']])

            print (table)

        except SoftLayer.SoftLayerAPIError as e:            
            print("Unable to list all LBaaS in the account: %s, %s" % (e.faultCode, e.faultString))

    def getPackageId(self, pkg):
        """Finds the packageId for the LBaaS"""
        filter = {"keyName":{"operation":pkg}}
        pkg_list = self.client['Product_Package'].getAllObjects(filter=filter)
        return pkg_list[0]['id']

    def getStandardPrices(self,pkg_id):
        """Gets price IDs needed to order a LBaaS"""
        key_names = ["LOAD_BALANCER_BANDWIDTH", "LOAD_BALANCER_DATA_PROCESSED", "LOAD_BALANCER_UPTIME", "LOAD_BALANCER_AS_A_SERVICE"]
                
        items = self.client['Product_Package'].getItems(id=pkg_id)
        prices = []

        for item_keyname in key_names:
            matching_item = [i for i in items
                                 if i['keyName'] == item_keyname][0]
            
            price_id = [p['id'] for p in matching_item['prices']
                            if not p['locationGroupId']][0]
            prices.append(price_id)
        
        return prices

    def setPlan(self, dc=None, pkg="LBAAS"):
        """Sets basic order information"""
        # Retrieve the package id
        pkg_id = self.getPackageId(pkg)
        # We'll retrieve generic prices according to the package
        prices = self.getStandardPrices(pkg_id)
        # Starting building the orderData
        self.orderData['complexType'] = "SoftLayer_Container_Product_Order_Network_LoadBalancer_AsAService"
        self.orderData['location'] = dc
        self.orderData['packageId'] = pkg_id
        self.orderData['useHourlyPricing'] = True            # LBaaS service is only available as an hourly service
        self.orderData['prices'] = [{'id': price_id} for price_id in prices]
    
    def setNetworkSettings(self, is_public=True, ibm_allocation=True, subnet=None):
        """Sets the basic network settings for a LBaaS order"""
        self.orderData['isPublic'] = is_public
        if is_public:            
            self.orderData['useSystemPublicIpPool'] = ibm_allocation
        
        self.orderData['subnets'] = [{"id": subnet}]

    def setBasicAndHealthChecks(self, name=None, desc=None, protocolConfigs=None, health_checks=None):
        """Sets healthchecks for a LBaaS order"""
        self.orderData['name'] = name
        self.orderData['description'] = desc
        self.orderData['protocolConfigurations'] = protocolConfigs
        self.orderData['healthMonitorConfigurations'] = health_checks
    
    def setServerInstances(self, server_instances=None):
        """Sets server instances for a LBaaS order"""
        self.orderData['serverInstancesInformation'] = server_instances
    
    def orderLBaaS(self, placeOrder):
        """Orders a LBaaS instance"""
        try:
            # verifyOrder() will check your order for errors.
            # placeOrder() when you're ready to order. 
            if not placeOrder:
                response = self.client['Product_Order'].verifyOrder(self.orderData)
            else:
                response = self.client['Product_Order'].placeOrder(self.orderData)
            
            print("\nDetailed information below about the order:\n")
            print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
        except SoftLayer.SoftLayerAPIError as e:            
            print("Unable to place the order: %s, %s" % (e.faultCode, e.faultString))        

if __name__ == "__main__":
    # Set Name, ID, or UUID for LBaaS
    # lbaasName = "My-LBaaS-Name"
    # lbaasId = 12345
    lbaasUUID = "1f454229-a7b0-4182-8953-975c0a045f79"
    main = lbaas()


    # Set the datacener location where you want to order
    package = "LBAAS"
    datacenter = "MEXICO"

    lbass_name = "My-LBaaS-name"
    description = "A description sample"
    
    # Set False for private network
    isPublic = True
    # Set False if you want to allocate from a Public Subnet, please ensure 
    # that TCP port 56501 is not blocked by a firewall or any other services.
    ibmAllocation = True
    # The private subnet id you want to place the load balancer
    subnetId = 830460                      

    # Protocol Configuration sample
    protocolConfigurations = [{
        "frontendProtocol":"HTTP",
        "frontendPort":80,
        "backendProtocol":"HTTP",
        "backendPort":8080,
        "sslCertificate": 0,                    # ID of SSL Certificate if you have one
        "loadBalancingMethod":"ROUNDROBIN",     # ROUNDROBIN, LEASTCONNECTION, WEIGHTED_RR
        "maxConn":10000
    }]

    # It must have the same number of objects than protocolConfigurations. 
    # LBaaS will be ordered with default values if it is not set.
    healthChecks=[{
        "protocol": "HTTP",
        "port": 80,
        "interval": 5,
        "timeout": 2,
        "maxTrials": 2,
        "path": ""
    }]

    serverInstances = [
        { "privateIpAddress": "10.148.92.136", "weight": 50 },
        { "privateIpAddress": "10.190.112.133", "weight": 100 }
    ]

    main.setPlan(dc=datacenter, pkg=package)    
    main.setNetworkSettings(is_public=isPublic, ibm_allocation=ibmAllocation, subnet=subnetId)
    
    main.setBasicAndHealthChecks(name=lbass_name, desc=description, 
                                 protocolConfigs=protocolConfigurations,
                                 health_checks=healthChecks)
    # Set server instances if you want to assign baremetals and virtual guests
    # during the order
    main.setServerInstances(server_instances=servers)
    main.orderLBaaS(True)

    main.addServerInstances(uuid, serverInstances)

    protocolConfigurations = [
        {
            "backendPort": 1350,
            "backendProtocol": "TCP",
            "frontendPort": 1450,
            "frontendProtocol": "TCP",
            "loadBalancingMethod": "WEIGHTED_RR",    # ROUNDROBIN, LEASTCONNECTION, WEIGHTED_RR
            "maxConn": 500,
            "sessionType": "SOURCE_IP"
        },
        {
            "backendPort": 1200,
            "backendProtocol": "HTTP",
            "frontendPort": 1150,
            "frontendProtocol": "HTTP",
            "loadBalancingMethod": "ROUNDROBIN",    # ROUNDROBIN, LEASTCONNECTION, WEIGHTED_RR
            "maxConn": 500,
            "sessionType": "SOURCE_IP"
        }
    ]
    main.addProtocols(uuid, protocolConfigurations)
    main.printDetails(uuid, servers=True, checks=True)
    listenerUuids = ["1d72f3cc-7903-484e-b5c0-507fd81ab852",
                     "a1908b08-1ef2-4fe4-bac3-f433589ba3cb"]
    main.removeProtocols(uuid, listeners=listenerUuids)

    # Use SoftLayer_Network_LBaaS_LoadBalancer::getMembers or
    # SoftLayer_Network_LBaaS_LoadBalancer::getLoadBalancer with masks
    # to retrive member uuid values
    memberUuids = ["ed25c408-4b26-4f22-ba1f-32b6af7e36da",
                   "ba9d6df6-c4e6-46a3-9a11-1e901de37932"]
    main.removeServerInstances(uuid, members=memberUuids)
    main.cancelLBaaS(lbaasUUID)
    
    # With following you can cancel it through the its name or id
    # main.cancelLBaaSById(lbaasId)
    # main.cancelLBaaSByName(lbaasName)
```