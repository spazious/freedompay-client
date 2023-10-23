# FraudCheckService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_id** | **str** |  | [optional] 
**option** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 
**device_identifier** | **str** |  | [optional] 
**commerce_indicator** | **str** |  | [optional] 
**site_identifier** | **str** |  | [optional] 
**customer_since_date** | **str** |  | [optional] 
**estimated_total_amount** | **str** |  | [optional] 
**properties** | [**List[UserDefinedField]**](UserDefinedField.md) |  | [optional] 
**run_risk_model** | **str** |  | [optional] 
**order** | **str** |  | [optional] 
**void_threshold** | **str** |  | [optional] 
**auth_data** | **str** |  | [optional] 
**captcha_data** | **str** |  | [optional] 
**fail_count** | **str** |  | [optional] 
**failed_requests** | **List[str]** |  | [optional] 
**run** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.fraud_check_service import FraudCheckService

# TODO update the JSON string below
json = "{}"
# create an instance of FraudCheckService from a JSON string
fraud_check_service_instance = FraudCheckService.from_json(json)
# print the JSON string representation of the object
print FraudCheckService.to_json()

# convert the object into a dict
fraud_check_service_dict = fraud_check_service_instance.to_dict()
# create an instance of FraudCheckService from a dict
fraud_check_service_form_dict = fraud_check_service.from_dict(fraud_check_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


