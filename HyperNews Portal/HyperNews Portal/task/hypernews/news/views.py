from django.shortcuts import render
from django.views import View
import json
from django.conf import settings
from django.views.generic.base import TemplateView
from datetime import datetime
from django.http import HttpResponseRedirect


class MyIndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class AllNewsView(View):
    def get(self, request, *args, **kwargs):
        search = request.GET.get('q')
        with open(settings.NEWS_JSON_PATH) as json_file:
            json_string = json_file.read()
            json_object = json.loads(json_string)
            date_dict = {}
            date_lst = []
            for item in json_object:
                dt = datetime.strptime(item['created'], '%Y-%m-%d %H:%M:%S')
                str_date = dt.strftime('%Y-%m-%d')
                date_lst.append(str_date)
            date_lst.sort(reverse=True)
            for date_item in date_lst:
                news_by_date_array = []
                for item in json_object:
                    dt = datetime.strptime(item['created'], '%Y-%m-%d %H:%M:%S')
                    str_date = dt.strftime('%Y-%m-%d')
                    if str_date == date_item:
                        if search is None:
                            news_by_date = {'title': item['title'], 'link': item['link']}
                            news_by_date_array.append(news_by_date)
                        else:
                            if search in item['title']:
                                news_by_date = {'title': item['title'], 'link': item['link']}
                                news_by_date_array.append(news_by_date)
                if len(news_by_date_array) > 0:
                    date_dict[date_item] = news_by_date_array
        return render(request, 'news.html', context={'news': date_dict})


class OneNewsView(TemplateView):
    template_name = 'news_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news_link = kwargs['n_news']
        with open(settings.NEWS_JSON_PATH) as json_file:
            json_string = json_file.read()
            json_object = json.loads(json_string)
            for item in json_object:
                if news_link == str(item['link']):
                    context['text'] = item['text']
                    context['title'] = item['title']
                    context['created'] = item['created']
                    return context


class AddNewsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'news_add.html')

    def post(self, request, *args, **kwargs):
        json_array = None
        news_title = request.POST['title']
        news_text = request.POST['text']
        news_created_date = datetime.now()
        news_created = news_created_date.strftime('%Y-%m-%d %H:%M:%S')
        news_existed_link = []
        with open(settings.NEWS_JSON_PATH) as json_file:
            json_string = json_file.read()
            json_object = json.loads(json_string)
            json_array = json_object
            for item in json_object:
                news_existed_link.append(int(item['link']))
        news_link = max(news_existed_link) + 1
        json_array.append({"created": news_created, "text": news_text, "title": news_title, "link": news_link})
        with open(settings.NEWS_JSON_PATH, 'w') as json_file:
            json.dump(json_array, json_file)
        return HttpResponseRedirect('/news/')

