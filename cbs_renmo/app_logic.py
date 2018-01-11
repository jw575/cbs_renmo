def process_bank_info(public_token, account_id):
    from plaid import Client

    # Change `sandbox` to `development` to test with live users and change
    # to `production` when you're ready to go live!
    client = Client(client_id='5a54dbbdefe64e49ca4ae233', secret='e46141f14d9a73d68f2dc58a7a9c3b',
                    public_key='cc5eca9a7b42c6fd2dee4ebad4e959', environment='sandbox')

    exchange_token_response = client.Item.public_token.exchange(public_token)
    access_token = exchange_token_response['access_token']

    stripe_response = client.Processor.stripeBankAccountTokenCreate(access_token, account_id)
    bank_account_token = stripe_response['stripe_bank_account_token']

    return [access_token, bank_account_token]


def account_data(plaid_access_token):
    from plaid import Client

    client = Client(client_id='5a54dbbdefe64e49ca4ae233', secret='e46141f14d9a73d68f2dc58a7a9c3b',
                    public_key='cc5eca9a7b42c6fd2dee4ebad4e959', environment='sandbox')

    # Retrieve Auth information for the Item, which includes high-level
    # account information and account numbers for depository accounts.
    auth_response = client.Auth.get(plaid_access_token)
    return auth_response


def get_date():
    import datetime
    current_date = datetime.date.today()
    return (current_date)


def get_fx_rate():
    try:
        url = "http://www.xe.com/currencyconverter/convert/?Amount=1&From=CNY&ToUSD"
        import requests
        from bs4 import BeautifulSoup
        page_data = BeautifulSoup(requests.get(url).content, 'lxml')
        return float(page_data.find('span', class_='uccResultAmount').get_text())
    except:
        return None
