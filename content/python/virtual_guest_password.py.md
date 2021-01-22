---
title: "Working with virtual guest passwords"
description: "A few examples on interacting with virtual guest credentials."
date: "2019-05-03"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Software_Component_Password"
tags:
    - "managepassword"
---

### Create a Virtual Guest Credential

```python
from pprint import pprint

import SoftLayer
from prettytable import PrettyTable


class Server:
    def __init__(self):
        client = SoftLayer.create_client_from_env()
        self.server_service = client['SoftLayer_Virtual_Guest']
        self.password_service = client['SoftLayer_Software_Component_Password']

    def print_software_components(self, serverId):
        mask = 'mask[softwareLicense[id,softwareDescription[name]]]'
        components_response = self.server_service.getSoftwareComponents(id=serverId, mask=mask)

        table = PrettyTable(["name"])

        for componet in components_response:
            table.add_row([componet["softwareLicense"]["softwareDescription"]["name"]])

        print(table)

    def create_credential(self, server_id, name=None, username=None, password=None, notes=None):
        # Retrieve the software components of a server.
        components_response = self.server_service.getSoftwareComponents(id=server_id, mask='mask[softwareLicense]')

        softwareId = 0
        for component in components_response:
            if name == component['softwareLicense']['softwareDescription']['name']:
                softwareId = component['id']

        # Build a SoftLayer_Software_Component_Password object
        templatePass = {
            "username": username,
            "password": password,
            "notes": notes,
            "softwareId": softwareId
        }
        try:
            result = self.password_service.createObject(templatePass)
            return result
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to create the password. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
            exit(1)


if __name__ == "__main__":
    server = Server()
    server_id = 11111
    server.print_software_components(server_id)

    print("Enter a software description name from above e.g. CentOS")
    software_description_name = input()

    # Set the username and password data.
    print("Enter the username")
    username = input()
    print("Enter the password")
    password = input()

    # optional field
    print("Enter a note(this is an optional field)")
    notes = input()

    # Create server credentials
    receipt = server.create_credential(server_id, name=software_description_name, username=username, password=password,
                                       notes=notes)
    pprint(receipt)

```

### Edit a Virtual Guest Credential

```python
from pprint import pprint

import SoftLayer
from prettytable import PrettyTable


class Server:
    def __init__(self):
        client = SoftLayer.create_client_from_env()
        self.server_service = client['SoftLayer_Virtual_Guest']
        self.password_service = client['SoftLayer_Software_Component_Password']

    def print_software_components_passwords(self, serverId):
        mask = 'mask[id,passwords[id,password,username]]'
        components_response = self.server_service.getSoftwareComponents(id=serverId, mask=mask)

        table = PrettyTable(["SoftwareComponentPasswordId", "password", "username"])

        for component in components_response:
            for password in component['passwords']:
                table.add_row([password['id'], password['password'], password['username']])

        print(table)

    def edit_credential(self, software_password_id, username=None, password=None, notes=None):
        # Build a SoftLayer_Software_Component_Password object
        templatePass = {
            "username": username,
            "password": password,
            "notes": notes
        }
        try:
            result = self.password_service.editObject(templatePass, id=software_password_id)
            return result
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to create the password. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
            exit(1)


if __name__ == "__main__":
    server = Server()
    server_id = 11111
    server.print_software_components_passwords(server_id)

    print("Enter a SoftwareComponentPasswordId you want to edit from above")
    software_password_id = input()

    # Set the username and password data.
    print("Enter the username")
    username = input()
    print("Enter the password")
    password = input()

    # optional field
    print("Enter a note(this is an optional field)")
    notes = input()

    # Edit the server credential
    receipt = server.edit_credential(software_password_id, username=username, password=password, notes=notes)
    pprint(receipt)

```

### Delete a Virtual Guest Credential
```python
from pprint import pprint

import SoftLayer
from prettytable import PrettyTable


class Server:
    def __init__(self):
        client = SoftLayer.create_client_from_env()
        self.server_service = client['SoftLayer_Virtual_Guest']
        self.password_service = client['SoftLayer_Software_Component_Password']

    def print_software_components_passwords(self, serverId):
        mask = 'mask[id,passwords[id,password,username]]'
        components_response = self.server_service.getSoftwareComponents(id=serverId, mask=mask)

        table = PrettyTable(["SoftwareComponentPasswordId", "password", "username"])

        for component in components_response:
            for password in component['passwords']:
                table.add_row([password['id'], password['password'], password['username']])

        print(table)

    def delete_credential(self, software_password_id=None):
        try:
            result = self.password_service.deleteObject(id=software_password_id)
            return result
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to create the password. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
            exit(1)


if __name__ == "__main__":
    server = Server()
    server_id = 11111
    server.print_software_components_passwords(server_id)

    print("Enter a SoftwareComponentPasswordId you want to delete from above")
    software_password_id = input()

    # Delete a server credential.
    receipt = server.delete_credential(software_password_id=software_password_id)
    pprint(receipt)

```
