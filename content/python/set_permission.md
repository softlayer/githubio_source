---
title: "Set user permissions"
description: "Adds the TICKET_ADD permission to a user"
date: "2015-09-16"
classes: 
    - "SoftLayer_User_Customer"
tags:
    - "permissions"
    - "users"

---

```python
import SoftLayer
from pprint import pprint as pp

class setPermissions():

    def __init__(self):

        self.client = SoftLayer.Client()

    def main(self, user_id):
        permissions = self.client['User_Customer'].getPermissions(id=user_id)
        print("=== OLD PERMISSIONS ===")
        self.printPermissions(permissions)
        setperm = {'keyName': "TICKET_ADD"}
        self.client['User_Customer'].addPortalPermission(setperm, id=user_id)
        permissions = self.client['User_Customer'].getPermissions(id=user_id)
        print("=== NEW PERMISSIONS ===")
        self.printPermissions(permissions)

    def getUsers(self):
        users = self.client['Account'].getUsers()
        print("ID - USERNAME - E-MAIL")
        for user in users:
            print("%s - %s - %s " % (user['id'], user['username'], user['email']))

    def printPermissions(sefl, permissions):
        for permission in permissions:
            print("%s" % permission['keyName'])

if __name__ == "__main__":
    main = setPermissions()
    # CHANGE ME
    my_user = 439723
    main.getUsers()
    main.main(my_user)
```
