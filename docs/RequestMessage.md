# RequestMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**store_id** | **str** |  | [optional] 
**terminal_id** | **str** |  | [optional] 
**es_key** | **str** |  | [optional] 
**admin_service** | [**AdminService**](AdminService.md) |  | [optional] 
**auto_rental_data** | [**AutoRentalData**](AutoRentalData.md) |  | [optional] 
**healthcare_data** | [**HealthcareDataWeb**](HealthcareDataWeb.md) |  | [optional] 
**bill_to** | [**BillTo**](BillTo.md) |  | [optional] 
**card** | [**Card**](Card.md) |  | [optional] 
**cc_auth_service** | [**CCAuthService**](CCAuthService.md) |  | [optional] 
**cc_capture_service** | [**CCCaptureService**](CCCaptureService.md) |  | [optional] 
**cc_credit_service** | [**CCCreditService**](CCCreditService.md) |  | [optional] 
**cc_followup_service** | [**CCFollowupService**](CCFollowupService.md) |  | [optional] 
**dcc_service** | [**DccService**](DccService.md) |  | [optional] 
**dcc** | [**DccInfo**](DccInfo.md) |  | [optional] 
**check** | [**Check**](Check.md) |  | [optional] 
**clerk_id** | **str** |  | [optional] 
**client_metadata** | [**ClientMetadata**](ClientMetadata.md) |  | [optional] 
**comments** | **str** |  | [optional] 
**discount_service** | [**DiscountService**](DiscountService.md) |  | [optional] 
**efv_options** | [**EfvOptions**](EfvOptions.md) |  | [optional] 
**fleet_data** | [**FleetData**](FleetData.md) |  | [optional] 
**fraud_check_service** | [**FraudCheckService**](FraudCheckService.md) |  | [optional] 
**inquiry_service** | [**InquiryService**](InquiryService.md) |  | [optional] 
**hotel_data** | [**HotelData**](HotelData.md) |  | [optional] 
**invoice_discount_detail** | [**List[EIDDetail]**](EIDDetail.md) |  | [optional] 
**invoice_service** | [**InvoiceService**](InvoiceService.md) |  | [optional] 
**invoice_header** | [**InvoiceHeader**](InvoiceHeader.md) |  | [optional] 
**items** | [**List[Item]**](Item.md) |  | [optional] 
**payments** | [**List[Payment]**](Payment.md) |  | [optional] 
**language** | **str** |  | [optional] 
**loyalty_service** | [**LoyaltyService**](LoyaltyService.md) |  | [optional] 
**request_incentives** | [**RequestIncentives**](RequestIncentives.md) |  | [optional] 
**merchant_defined_data** | [**MerchantDefinedData**](MerchantDefinedData.md) |  | [optional] 
**magic_cookie** | **str** |  | [optional] 
**merchant_reference_code** | **str** |  | [optional] 
**merchant_batch_id** | **str** |  | [optional] 
**message_service** | [**MessageService**](MessageService.md) |  | [optional] 
**mobile_service** | [**MobileService**](MobileService.md) |  | [optional] 
**network_data** | [**NetworkData**](NetworkData.md) |  | [optional] 
**offline_control** | [**OfflineControl**](OfflineControl.md) |  | [optional] 
**order_request_id** | **str** |  | [optional] 
**order_request_token** | **str** |  | [optional] 
**pos** | [**Pos**](Pos.md) |  | [optional] 
**promo_service** | [**PromoService**](PromoService.md) |  | [optional] 
**purchase_totals** | [**PurchaseTotals**](PurchaseTotals.md) |  | [optional] 
**restaurant_data** | [**RestaurantData**](RestaurantData.md) |  | [optional] 
**response_flags** | **str** |  | [optional] 
**session_key** | **str** |  | [optional] 
**session_service** | [**SessionService**](SessionService.md) |  | [optional] 
**ship_from** | [**ShipFrom**](ShipFrom.md) |  | [optional] 
**ship_to** | [**ShipTo**](ShipTo.md) |  | [optional] 
**token_create_service** | [**TokenCreateService**](TokenCreateService.md) |  | [optional] 
**vend_control_service** | [**VendControlService**](VendControlService.md) |  | [optional] 
**void_service** | [**VoidService**](VoidService.md) |  | [optional] 
**tor_service** | [**TORService**](TORService.md) |  | [optional] 
**eod_service** | [**EodService**](EodService.md) |  | [optional] 
**incentive_service** | [**IncentiveService**](IncentiveService.md) |  | [optional] 
**member_data** | [**MemberData**](MemberData.md) |  | [optional] 

## Example

```python
from freedompay_client.models.request_message import RequestMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RequestMessage from a JSON string
request_message_instance = RequestMessage.from_json(json)
# print the JSON string representation of the object
print RequestMessage.to_json()

# convert the object into a dict
request_message_dict = request_message_instance.to_dict()
# create an instance of RequestMessage from a dict
request_message_form_dict = request_message.from_dict(request_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


