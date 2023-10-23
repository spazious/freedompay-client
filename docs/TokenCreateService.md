# TokenCreateService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**disable_verification** | **str** |  | [optional] 
**pos_data** | **str** |  | [optional] 
**dyn_exp** | **str** |  | [optional] 
**run** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.token_create_service import TokenCreateService

# TODO update the JSON string below
json = "{}"
# create an instance of TokenCreateService from a JSON string
token_create_service_instance = TokenCreateService.from_json(json)
# print the JSON string representation of the object
print TokenCreateService.to_json()

# convert the object into a dict
token_create_service_dict = token_create_service_instance.to_dict()
# create an instance of TokenCreateService from a dict
token_create_service_form_dict = token_create_service.from_dict(token_create_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


