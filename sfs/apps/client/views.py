from django.shortcuts import render
from client import models


from django.views import View

class ShowIndex(View):
    """
    show index
    """

    def get(self,request):
        """展示客户信息界面"""
        # client_list = models.Client.objects.select_related("vip").filter(is_delete=False)

        return render(request,"admin/client/index.html",locals())