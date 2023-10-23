# AdminService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_type** | **str** |  | [optional] 
**term_caps** | **str** |  | [optional] 
**run** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.admin_service import AdminService

# TODO update the JSON string below
json = "{}"
# create an instance of AdminService from a JSON string
admin_service_instance = AdminService.from_json(json)
# print the JSON string representation of the object
print AdminService.to_json()

# convert the object into a dict
admin_service_dict = admin_service_instance.to_dict()
# create an instance of AdminService from a dict
admin_service_form_dict = admin_service.from_dict(admin_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


