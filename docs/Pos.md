# Pos


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**register_number** | **str** |  | [optional] 
**entry_mode** | **str** |  | [optional] 
**track1** | **str** |  | [optional] 
**track2** | **str** |  | [optional] 
**track3** | **str** |  | [optional] 
**track_ksn** | **str** |  | [optional] 
**sequence_number** | **str** |  | [optional] 
**card_present** | **str** |  | [optional] 
**track1e** | **str** |  | [optional] 
**track2e** | **str** |  | [optional] 
**track1len** | **str** |  | [optional] 
**track2len** | **str** |  | [optional] 
**tracke** | **str** |  | [optional] 
**enc_mode** | **str** |  | [optional] 
**msr_type** | **str** |  | [optional] 
**payment_date** | **str** |  | [optional] 
**chip_data** | **str** |  | [optional] 
**issuer_script_results** | **str** |  | [optional] 
**caps** | **str** |  | [optional] 
**fallback_reason** | **str** |  | [optional] 
**sig_data** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.pos import Pos

# TODO update the JSON string below
json = "{}"
# create an instance of Pos from a JSON string
pos_instance = Pos.from_json(json)
# print the JSON string representation of the object
print Pos.to_json()

# convert the object into a dict
pos_dict = pos_instance.to_dict()
# create an instance of Pos from a dict
pos_form_dict = pos.from_dict(pos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


