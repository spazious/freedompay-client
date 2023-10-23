# PurchaseTotals


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_detail** | [**List[TaxDetailItem]**](TaxDetailItem.md) |  | [optional] 
**currency** | **str** |  | [optional] 
**discount_total** | **str** |  | [optional] 
**duty_total** | **str** |  | [optional] 
**freight_total** | **str** |  | [optional] 
**tax_total** | **str** |  | [optional] 
**tip_amount** | **str** |  | [optional] 
**debit_surcharge** | **str** |  | [optional] 
**cash_back_amount** | **str** |  | [optional] 
**overtender** | **str** |  | [optional] 
**invoice_total** | **str** |  | [optional] 
**service_charge** | **str** |  | [optional] 
**eid_amount** | **str** |  | [optional] 
**charge_amount** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.purchase_totals import PurchaseTotals

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseTotals from a JSON string
purchase_totals_instance = PurchaseTotals.from_json(json)
# print the JSON string representation of the object
print PurchaseTotals.to_json()

# convert the object into a dict
purchase_totals_dict = purchase_totals_instance.to_dict()
# create an instance of PurchaseTotals from a dict
purchase_totals_form_dict = purchase_totals.from_dict(purchase_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


