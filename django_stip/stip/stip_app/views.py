# from django.shortcuts import render

# Create your views here.
from typing import Any
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound
from django.http import HttpResponseForbidden, HttpResponseBadRequest
from django.http import JsonResponse
from pip._vendor.requests.api import request
from django.core.serializers.json import DjangoJSONEncoder


def index(request):
    bob = Person("Bob", 41)
    return JsonResponse(bob, safe=False, encoder=PersonEncoder)
    #  return JsonResponse({"name": "Tom", "age": 38})


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class PersonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age}
        return super().default(obj)

    # people=["Tom","Bob","Sam"]
    # if id in range(0,len(people)):
    #     return HttpResponse (people[id])
    # else:
    #     return HttpResponseNotFound("Not found")

    # return HttpResponse("<h1>Hello</h1>", content_type="text/plain", charset="utf-8")
    # host=request.META["HTTP_HOST"]
    # user_agent=request.META["HTTP_USER_AGENT"]
    # path=request.path
    # return HttpResponse( f"""
    # <p>Host: {host}</p>
    # <p> User_agent: {user_agent}</p>
    # <p>Path: {path}</p>
    #                     """)


def about(request, name, age):
    return HttpResponse(f"""
       <h2>О пользователе</h2>
       <p>Имя: {name}</p>
       <p>Возраст: {age} </p>

    """)


def contact(request):
    return HttpResponseRedirect("/about")


# def user(request,name,age):
#     return HttpResponse(f"<h2>Имя: {name} Возраст:{age}</h2>")
def user(request):
    age = request.GET.get("age", 0)
    name = request.GET.get("name", "Undefined")
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")


def details(request):
    return HttpResponsePermanentRedirect("/")


def products(request, id):
    return HttpResponse(f"Товар: {id}")


def new(request, id):
    return HttpResponse(f"Товар: {id}")


def top(request):
    return HttpResponse("Популярные товары")


def comments(request, id):
    return HttpResponse(f"Вопрос о товаре {id}")


def questions(request, id):
    return HttpResponse(f"Вопрос о товаре {id} ")


# def access(request, age):
#     if age not in range(1, 111):
#         return HttpResponseBadRequest("Некорректные данные ")
#     if age > 17:
#         return HttpResponse("возраст доступен")
#     else:
#         return HttpResponseForbidden("Доступ заблокирован, мал ишшо  ")
