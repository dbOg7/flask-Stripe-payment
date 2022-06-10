from os import environ
import stripe
from flask import Flask, redirect

stripe.api_key = environ.get('stripe.api_key')

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

YOUR_DOMAIN = 'http://localhost:5000'

@app.route('/', methods=['GET','POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'eur',
                    'product_data': {
                    'name': 'site vitrine',
                    },
                    'unit_amount': 100000,
                },
                'quantity': 1,
            }],
            mode='payment',
            
            success_url = YOUR_DOMAIN + '/success.html', #bug
            cancel_url = YOUR_DOMAIN + '/cancel.html', #bug
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)
