# HealthcareDataWeb


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_amount** | **str** |  | [optional] 
**rx** | **str** |  | [optional] 
**vision** | **str** |  | [optional] 
**clinic** | **str** |  | [optional] 
**dental** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.healthcare_data_web import HealthcareDataWeb

# TODO update the JSON string below
json = "{}"
# create an instance of HealthcareDataWeb from a JSON string
healthcare_data_web_instance = HealthcareDataWeb.from_json(json)
# print the JSON string representation of the object
print HealthcareDataWeb.to_json()

# convert the object into a dict
healthcare_data_web_dict = healthcare_data_web_instance.to_dict()
# create an instance of HealthcareDataWeb from a dict
healthcare_data_web_form_dict = healthcare_data_web.from_dict(healthcare_data_web_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


