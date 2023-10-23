# DccService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bin** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**run** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.dcc_service import DccService

# TODO update the JSON string below
json = "{}"
# create an instance of DccService from a JSON string
dcc_service_instance = DccService.from_json(json)
# print the JSON string representation of the object
print DccService.to_json()

# convert the object into a dict
dcc_service_dict = dcc_service_instance.to_dict()
# create an instance of DccService from a dict
dcc_service_form_dict = dcc_service.from_dict(dcc_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


