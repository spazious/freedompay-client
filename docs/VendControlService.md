# VendControlService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**VendProductList**](VendProductList.md) |  | [optional] 

## Example

```python
from freedompay_client.models.vend_control_service import VendControlService

# TODO update the JSON string below
json = "{}"
# create an instance of VendControlService from a JSON string
vend_control_service_instance = VendControlService.from_json(json)
# print the JSON string representation of the object
print VendControlService.to_json()

# convert the object into a dict
vend_control_service_dict = vend_control_service_instance.to_dict()
# create an instance of VendControlService from a dict
vend_control_service_form_dict = vend_control_service.from_dict(vend_control_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


