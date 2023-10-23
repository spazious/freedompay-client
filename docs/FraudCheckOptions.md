# FraudCheckOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**kount** | [**KountOptions**](KountOptions.md) |  | [optional] 

## Example

```python
from freedompay_client.models.fraud_check_options import FraudCheckOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FraudCheckOptions from a JSON string
fraud_check_options_instance = FraudCheckOptions.from_json(json)
# print the JSON string representation of the object
print FraudCheckOptions.to_json()

# convert the object into a dict
fraud_check_options_dict = fraud_check_options_instance.to_dict()
# create an instance of FraudCheckOptions from a dict
fraud_check_options_form_dict = fraud_check_options.from_dict(fraud_check_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


