import json
from json import JSONEncoder

import simplejson
from django.core import serializers
from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
from .models import Post
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.

def index(request):
    return HttpResponse("欢迎访问我的博客首页！")

def json2(request):
    post_list = Post.objects.all().order_by('-created_time')
    response_data = {}
    response_data['code'] = 1
    #response_data['post_list'] = serializers.serialize('json', post_list)

    data = [item.to_dict() for item in post_list]
    response_data['post_list'] = data

    return JsonResponse(response_data)

# def index(request):
#     post_list = Post.objects.all().order_by('-created_time')
#     return render(request, 'blog/index.html', context={'post_list': post_list})

    # response_data = {}
    # response_data['code'] = 0
    # response_data['post_list'] = post_list
    # return HttpResponse(json.dumps(response_data), content_type="application/json")