# VoidService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**offline** | **str** |  | [optional] 
**offline_code** | **str** |  | [optional] 
**run** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.void_service import VoidService

# TODO update the JSON string below
json = "{}"
# create an instance of VoidService from a JSON string
void_service_instance = VoidService.from_json(json)
# print the JSON string representation of the object
print VoidService.to_json()

# convert the object into a dict
void_service_dict = void_service_instance.to_dict()
# create an instance of VoidService from a dict
void_service_form_dict = void_service.from_dict(void_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


