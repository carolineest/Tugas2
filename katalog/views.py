from django.shortcuts import render
from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
    'list_barang': data_barang_katalog,
    'nama': 'Caroline Esther U. P.',
    'id': '2106751915'
}
    return render(request, "katalog.html", context)