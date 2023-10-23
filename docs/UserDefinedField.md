# UserDefinedField


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.user_defined_field import UserDefinedField

# TODO update the JSON string below
json = "{}"
# create an instance of UserDefinedField from a JSON string
user_defined_field_instance = UserDefinedField.from_json(json)
# print the JSON string representation of the object
print UserDefinedField.to_json()

# convert the object into a dict
user_defined_field_dict = user_defined_field_instance.to_dict()
# create an instance of UserDefinedField from a dict
user_defined_field_form_dict = user_defined_field.from_dict(user_defined_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


