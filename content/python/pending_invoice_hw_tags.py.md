---
title: "Gets pending invoice with hardware tags"
description: "An example that gets the pending invoice along with all the hardware tags."
date: "2019-06-14"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Tag_Reference"
    - "SoftLayer_Tag"
    - "SoftLayer_Hardware"
tags:
    - "invoice"
    - "hardware"
    - "tag"
---


```python
import SoftLayer
import json


class PendingInvoice:

    def __init__(self):
        self.client = SoftLayer.create_client_from_env()

    def gather_hardware_tags(self, tags=None):
        """Retrieves hardware with tags references"""
        object_mask = "mask[id,hostname,tagReferences[id,tag]]"
        if tags is None:
            return self.client['SoftLayer_Account'].getHardware(mask=object_mask)
        object_filter = {
            'hardware': {
                'tagReferences': {
                    'tag': {
                        'name': {
                            'operation': 'in', 'options': [{
                                'name': 'data', 'value': tags
                            }]
                        }
                    }
                }
            }
        }

        return self.client['SoftLayer_Account'].getHardware(mask=object_mask, filter=object_filter)

    def gather_invoice_top_level_items(self):
        """Retrieves currently pending invoice with top-level invoice items on account """
        object_mask = "mask[invoiceTopLevelItems]"
        return self.client['SoftLayer_Account'].getPendingInvoice(mask=object_mask)

    def invoice_with_tags(self, tags=None):
        """Adds tags to invoiceTopLevelItems"""
        hardware_invoices = self.gather_invoice_top_level_items()
        hardware_tagged = self.gather_hardware_tags(tags=tags)
        for invoice_item in hardware_invoices['invoiceTopLevelItems']:
            for hardware in hardware_tagged:
                if invoice_item['resourceTableId'] == hardware['id']:
                    invoice_item['tagReferences'] = hardware['tagReferences']
                    print(json.dumps(invoice_item, indent=2))


if __name__ == "__main__":
    main = PendingInvoice()

    # Gets the pending invoice with hardware tags.
    main.invoice_with_tags()

    # Gets the pending invoice  with matching hardware tags.
    hardware_tags = ['tag1', 'tag2']
    main.invoice_with_tags(tags=hardware_tags)

```
