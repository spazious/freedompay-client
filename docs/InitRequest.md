# InitRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**button** | [**ButtonControl**](ButtonControl.md) |  | [optional] 
**button_type** | **str** |  | [optional] 
**pay_pal** | [**PayPalInitRequest**](PayPalInitRequest.md) |  | [optional] 
**postal_code** | [**PostalCodeControl**](PostalCodeControl.md) |  | [optional] 
**pay_by_bank** | [**PayByBankInitRequest**](PayByBankInitRequest.md) |  | [optional] 
**fraud_check** | [**FraudCheckOptions**](FraudCheckOptions.md) |  | [optional] 
**card_number** | [**CardNumberControl**](CardNumberControl.md) |  | [optional] 
**consumer_authentication** | [**ConsumerAuthentication**](ConsumerAuthentication.md) |  | [optional] 
**dcc** | [**DccOptions**](DccOptions.md) |  | [optional] 
**expiration_date** | [**ExpirationDateControl**](ExpirationDateControl.md) |  | [optional] 
**order_details** | [**OrderDetails**](OrderDetails.md) |  | [optional] 
**security_code** | [**SecurityCodeControl**](SecurityCodeControl.md) |  | [optional] 
**token_information** | [**TokenInformation**](TokenInformation.md) |  | [optional] 
**card_icon_display_type** | **str** |  | [optional] 
**payment_type** | **str** |  | [optional] 
**workflow_type** | **str** |  | [optional] 
**culture_code** | **str** |  | [optional] 
**es_key** | **str** |  | [optional] 
**legal** | [**LegalControl**](LegalControl.md) |  | [optional] 
**store_id** | **str** |  | [optional] 
**styles** | **str** |  | [optional] 
**terminal_id** | **str** |  | [optional] 
**validation_message_type** | **str** |  | [optional] 
**reference_id** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.init_request import InitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InitRequest from a JSON string
init_request_instance = InitRequest.from_json(json)
# print the JSON string representation of the object
print InitRequest.to_json()

# convert the object into a dict
init_request_dict = init_request_instance.to_dict()
# create an instance of InitRequest from a dict
init_request_form_dict = init_request.from_dict(init_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


