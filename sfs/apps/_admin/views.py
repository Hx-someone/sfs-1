from django.shortcuts import render
from django.views import View



class ShowIndex(View):

    def get(self,request):
        return render(request, "admin/base.html")
