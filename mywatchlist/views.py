from django.shortcuts import render
from django.shortcuts import render
from mywatchlist.models import mywatchlist

# Create your views here.
def show_mywatchlist(request):
    data_barang_watchlist = mywatchlist.objects.all()
    context = {
    'list_barang': data_barang_watchlist,
    'nama': 'Caroline Esther U. P.',
    'id': '2106751915'
}
    return render(request, "mywatchlist.html", context)