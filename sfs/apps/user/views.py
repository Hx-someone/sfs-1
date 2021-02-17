import json

from django.shortcuts import render

# Create your views here.
from django.views import View
from utils.code.json_function import to_json_data
from utils.code.res_code import Code,error_map



class LoginView(View):
    def get(self,request):
        return render(request,"user/login.html")

    def post(self,request):
        try:
            data = request.body
            if not data:
                return to_json_data(errno=Code.PARAMERR,errmsg=error_map[Code.PARAMERR])
            data = json.loads(data)
        except Exception as e:
            return to_json_data(errno=Code.UNKOWNERR,errmsg = error_map[Code.UNKOWNERR])



class RegisterView(View):

    def get(self,request):

        return render(request,"user/login.html")
