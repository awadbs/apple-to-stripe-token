import json
import stripe


stripe.api_key = "set_your_striple_api_key_here" #grab your stripe api key

#get your apple pay token. Would be sent here when your customer creates an apple pay intent.
# https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypaymenttoken
#  example below of extraction of an apple pay token from Apple hitting my post request endpoint
paymentData = json.loads(event['body'])['payment']['paymentToken']

try:
    stripe_payload = create_stripe_payload(paymentData) #extract parameters for stripe request
    token_response = stripe.Token.create(stripe_payload) # request a stripe token from apple token info.

    #### charge your customer using newly minted stripe token!
    charge = stripe.Charge.create(
            amount=1000,  # amount in cents
            currency="usd",
            source=token_response, 
            description="Charge for product/service"
        )
except stripe.error.StripeError as e:
    print(e)



## Extracts and formats apple pay token object for stripe's token request endpoint
def create_stripe_payload(payment_data):
    payload = {}

    # Add pk_token
    payload['pk_token'] = payment_data.paymentData
    
    # Add billing contact information if available
    # if billing_contact:
    #     payload['card'] = billing_contact  # Replace with actual method to extract address params


    payment_instrument = payment_data.paymentMethod.displayName
    if payment_instrument:
        payload['pk_token_instrument_name'] = payment_instrument

   
    payment_network = payment_data.paymentMethod.network
    if payment_network:
        payload['pk_token_payment_network'] = payment_network

    transaction_identifier = payment_data.transactionIdentifier
    if transaction_identifier:
        payload['pk_token_transaction_id'] = transaction_identifier


    return payload


