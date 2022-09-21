from django.shortcuts import render
from mywatchlist.models import mywatchlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_barang_watchlist = mywatchlist.objects.all()
    context = {
    'list_barang': data_barang_watchlist,
    'nama': 'Caroline Esther U. P.',
    'id': '2106751915'
}
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = mywatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = mywatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = mywatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = mywatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
