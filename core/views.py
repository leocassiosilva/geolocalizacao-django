from django.shortcuts import render

from django.views.generic import View

from .utils import yelp_seach, get_client_city_data


class IndexView(View):

    def get(self, request, *args, **kwargs):

        items = []

        city = None

        while not city:
            ret = get_client_city_data()
            city = ret['city']

        q = request.Get.get('key', None)
        loc = request.Get.get('loc', None)
        location = city

        contex = {
            'city': city,
            'busca': False
        }

        if loc:
            location = loc
        if q:
            items = yelp_seach(keyword=q, location=location)
            contex = {
                'items': items,
                'city': location,
                'busca': True
            }
        return render(request, 'index.html', contex)
