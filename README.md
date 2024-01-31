# apple-to-stripe-token
Converts Apple Pay tokens to stripe tokens; allowing you to use stripe as payment gateway to charge your customers. (Todo: in progress of creating it's own python package)

The need for this came from the fact that Stripe ONLY supports Apple Pay on mobile or web apps. Previously, if you would've liked to use Stripe with Apple Pay iMessage, or Telegram, (or some other platform that supports w/ Apple Pay) then you wouldve been out of luck. 
This now allows you to use Stripe as your payment processor by converting your apple pay token to stripe v1 token, then charging your customers with a stripe payment intent or charge intent; [like so](https://stripe.com/docs/api/payment_methods/create).

**Again, Stripe does not support this!
This was created by reverse engineering Stripe's swift package for Apple Pay, so I can not confirm if this would be PCI compliant, please use at your own risk :)**

**converter.py** contains all the code you'd need.

### Necessary Documentation
[Apple: Instructions to set up your Apple Pay merchant account](https://register.apple.com/resources/messages/msp-api-tutorial/applepay)

[Apple: Sending test Apple Pay requests](https://register.apple.com/resources/messages/msp-api-tutorial/applepay#exercise-send-an-apple-pay-requestbasic-functionality)

[Stripe: Adding apple pay certs to your Stripe Account](https://support.stripe.com/questions/enable-apple-pay-on-your-stripe-account)
