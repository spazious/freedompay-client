# InvoiceService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trans_type** | **str** |  | [optional] 
**run** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.invoice_service import InvoiceService

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceService from a JSON string
invoice_service_instance = InvoiceService.from_json(json)
# print the JSON string representation of the object
print InvoiceService.to_json()

# convert the object into a dict
invoice_service_dict = invoice_service_instance.to_dict()
# create an instance of InvoiceService from a dict
invoice_service_form_dict = invoice_service.from_dict(invoice_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


