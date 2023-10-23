# Card


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**account_type** | **str** |  | [optional] 
**card_type** | **str** |  | [optional] 
**token_subtype** | **str** |  | [optional] 
**subtype** | **str** |  | [optional] 
**issuer** | **str** |  | [optional] 
**cv_indicator** | **str** |  | [optional] 
**cv_number** | **str** |  | [optional] 
**expiration_month** | **str** |  | [optional] 
**expiration_year** | **str** |  | [optional] 
**issue_number** | **str** |  | [optional] 
**name_on_card** | **str** |  | [optional] 
**start_month** | **str** |  | [optional] 
**start_year** | **str** |  | [optional] 
**service_restriction_code** | **str** |  | [optional] 
**pin_ksn** | **str** |  | [optional] 
**pin_block** | **str** |  | [optional] 
**voucher_number** | **str** |  | [optional] 
**expected_brand** | **str** |  | [optional] 
**pl_data1** | **str** |  | [optional] 
**pl_data2** | **str** |  | [optional] 
**var_pass** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.card import Card

# TODO update the JSON string below
json = "{}"
# create an instance of Card from a JSON string
card_instance = Card.from_json(json)
# print the JSON string representation of the object
print Card.to_json()

# convert the object into a dict
card_dict = card_instance.to_dict()
# create an instance of Card from a dict
card_form_dict = card.from_dict(card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


