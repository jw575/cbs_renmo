from django.shortcuts import render
import cbs_renmo
import cbs_renmo.app_logic


def home(request):
    context = dict()
    context['options'] = [
        ['bankInfo', 'Enter your bank information'],
        ['loginFunction', 'Login'],
    ]
    return render(request, "home.html", context)
    # renders home.html using whatever inside the context dictionary


def get_bank(request):
    context = dict()
    return render(request, "bankInfo.html", context)


def login(request):
    context = dict()
    return render(request, "loginFunction.html", context)


def receiver(request):
    context = dict()
    try:
        if request.POST:
            token = request.POST['token']
            id = request.POST['id']
            plaid_access_token = cbs_renmo.app_logic.process_bank_info(token, id)[0]
            stripe_tokenID = cbs_renmo.app_logic.process_bank_info(token, id)[1]
            # print(plaid_access_token)
            # print(stripe_tokenID)
            account_data = cbs_renmo.app_logic.account_data(plaid_access_token)
            # print("exited account_data()")
            print(account_data)
            context = {'plaid_token': plaid_access_token,
                       'stripe_token': stripe_tokenID,
                       'account_data': account_data}
        else:
            pass
    except:
        print("Exception Occured")
    return render(request, "management.html", context)
