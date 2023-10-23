# EodService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** |  | [optional] 
**group_code** | **str** |  | [optional] 
**run** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.eod_service import EodService

# TODO update the JSON string below
json = "{}"
# create an instance of EodService from a JSON string
eod_service_instance = EodService.from_json(json)
# print the JSON string representation of the object
print EodService.to_json()

# convert the object into a dict
eod_service_dict = eod_service_instance.to_dict()
# create an instance of EodService from a dict
eod_service_form_dict = eod_service.from_dict(eod_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


