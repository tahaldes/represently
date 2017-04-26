from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.http import HttpResponseRedirect
from .models import Zipcode, District, Rep
from . import calculator
from .forms import ZipcodeForm


def index(request):
    for zips in Zipcode.objects.all():
        if zips.district_set.all() == []:
            zips.delete()
    return render(request, 'zip_to_rep/index.html', {'all_zips': Zipcode.objects.all})


def zip_detail(request, zipcode):
    zipc = get_object_or_404(Zipcode, zip=zipcode)
    for ex in Zipcode.objects.all():
        if zipc == ex:
            zipc.delete()
    info = calculator.get_district_info((zipcode))
    new_zip = (Zipcode(zip=zipcode))
    new_zip.save()
    if new_zip.district_set.all != []:
        for district in info['results']:
            if district['district'] != 0:
                new_district = District(zip_code=new_zip, dist_state=district['state'], dist_num=district['district'])
                new_district.save()
                name = calculator.get_1rep_name(new_district)
                recentbill = calculator.get_bill_name_maybe(new_district)
                #howvoted = calculator.get_positon(new_district)
                new_rep = Rep(dist=new_district, rep_name=name,recent_bill= recentbill,how_voted= 'for')
                new_rep.save()
    return render(request, 'zip_to_rep/zip_detail.html', {'zip': zipc})


class ZipAdd(CreateView):
    model = Zipcode
    fields = ['zip']