from django.shortcuts import render
import cbs_renmo
import cbs_renmo.app_logic
from cbs_renmo import app_logic
from cbs_renmo.models import User, Listing


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


def list(request):
    context = dict()
    seller = User.objects.get(id=1)
    context['seller'] = seller
    context['date'] = app_logic.get_date()
    context['fx_rate'] = app_logic.get_fx_rate()
    try:
        request.GET['list']
        sell_amount = request.GET['sell_amount']
        fx_rate = request.GET['fx_rate']
        app_logic.post_listing(seller.id, sell_amount, fx_rate)
        return listingconfirm(request)
    except:
        pass
    return render(request, "list.html", context)


def listingconfirm(request):
    context = dict()
    new_listing = Listing.objects.order_by('-id').first()
    context['listing'] = new_listing
    return render(request, "listingconfirm.html", context)
