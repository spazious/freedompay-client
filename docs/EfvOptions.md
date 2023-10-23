# EfvOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | **str** |  | [optional] 
**force** | **str** |  | [optional] 
**force_code** | **str** |  | [optional] 
**force_message** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.efv_options import EfvOptions

# TODO update the JSON string below
json = "{}"
# create an instance of EfvOptions from a JSON string
efv_options_instance = EfvOptions.from_json(json)
# print the JSON string representation of the object
print EfvOptions.to_json()

# convert the object into a dict
efv_options_dict = efv_options_instance.to_dict()
# create an instance of EfvOptions from a dict
efv_options_form_dict = efv_options.from_dict(efv_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


