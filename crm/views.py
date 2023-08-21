from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceTable, PriceCard
from telebot.sendmessage import sendTelegram

def first_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()

    form = OrderForm()

    dict_obj = {'slider_list': slider_list,
                'pc_1': pc_1,
                'pc_2': pc_2,
                'pc_3': pc_3,
                'price_table': price_table,
                'form': form}

    return render(request, './index.html', dict_obj)

def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    el = Order(order_name=name, order_phone=phone).save()
    sendTelegram(tg_n = name, tg_p = phone)

    return render(request, './thanks.html', {'name': name})