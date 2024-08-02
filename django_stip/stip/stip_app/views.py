from django.shortcuts import render
from django.template.response import TemplateResponse
# Create your views here.
from typing import Any
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound
from django.http import HttpResponseForbidden, HttpResponseBadRequest
from django.http import JsonResponse
from pip._vendor.requests.api import request
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime
from .forms import UserForm


def index(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.changed_data["name"]
            return HttpResponse(f"<h2> Hello, {name}</h2>")
        else:
            return HttpResponse("invalid data")
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})

        # name=request.POST.get("name")
        # age=request.POST.get("age")
        # return HttpResponse(f"<h2> Привет, {name}, твой возраст {age}</h2>")
    # else:
    #     userform = UserForm()
    #     return render(request, "index.html", {"form": userform})

    # userform = UserForm()
    # return render(request, "index.html", {"form": userform})
    # langs=[]
    # data = {"red": "красный", "green": "зеленый", "blue": "синий"}
    # langs = ["Python", "JavaScript", "Java", "C#", "C++"]
    # return render(request, "index.html",  context={"site": "METANIT.COM"})
    # return render(request, "index.html",context={"langs":langs})
    # return render(request, "index.html",context={"data":data})
    # data={"n":5}
    # return render(request, "index.html", context=data)
    # return render(request, "index.html", context={"body": "<h1>Hello ,world</h1>"})
    # header = "Данные  пользователя"
    # langs = ["Python", "Java", "C#"]
    # user = {"name": "Tom", "age": 23}
    # adress=("Абрикосовая", 23, 45)
    # data={"header":header, "langs":langs,"user":user, "adress":adress}
    # return render(request, "index.html", context=data)
    # return TemplateResponse(request, "index.html",data)
    # return render(request, "index.html", context={"person":Person("Tom",22)})
    # data={"header": "Hello Django", "message": "Welcome to Python"}
    # return TemplateResponse(request, "index.html",context=data)
    # return render(request,"index.html")
    # bob = Person("Bob", 41)
    # return JsonResponse(bob, safe=False, encoder=PersonEncoder)
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


def about(request):
    return render(request, "about.html")
# def about(request, name, age):
    # return HttpResponse(f"""
    #    <h2>О пользователе</h2>
    #    <p>Имя: {name}</p>
    #    <p>Возраст: {age} </p>

    # """)


def contact(request):
    return render(request, "contacts.html")
    # return HttpResponseRedirect("/about")


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
def set(request):
    username = request.GET.get("username", "Undefined")
    response = HttpResponse(f"Hello {username}")
    response.set_cookie("username", username)
    return response


def get(request):
    usename = request.COOKIES["username"]
    return HttpResponse(f"Hello {usename}")


def postuser(request):
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    langs = request.POST.getlist("languages", ["python"])
    return HttpResponse(f"""
                        <div>Name: {name} Age: {age} <div>
                        <div>languages: {langs}</div>
                        """)
