from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse,JsonResponse,FileResponse
from django.template import Template,Context
import os
# Create your views here.


def msgproc(request):
    datalist = []
    if request.method == "POST":
        ur1 = request.POST.get("ur1", None)
        ur2 = request.POST.get("ur2", None)
        msg = request.POST.get("msg",None)
        time = datetime.now()
        with open('msgdata.txt', 'a+') as f:
            f.write("{}++{}++{}++{}++\n".format(ur2,ur1,\
                msg,time.strftime("%Y-%m-%d %H:%M:%S")))

    if request.method == "GET":
        ur3 = request.GET.get("ur3", None)
        if ur3 != None:
            with open("msgdata.txt", "r") as f:
                cnt = 0
                for line in f:
                    linedata = line.split('++')
                    if linedata[0] == ur3:
                        cnt = cnt + 1
                        d = {"ur1":linedata[1],"msg":linedata[2]\
                            ,"time":linedata[3]}
                        datalist.append(d)
                    if cnt >= 10:
                        break   
    return render(request,"MsgSingleWeb.html",{"data_g":datalist})
# msgproc

def homeproc(resquest):
    response = HttpResponse()
    response.write("<h1>这是首页，具体功能请访问<a href='./msggate/'>这里</a></h1>")
    response.write("<h2>这是第二行</h2>")
    
    return response
    #return HttpResponse("<h1>这是首页，具体功能请访问<a href='./msggate/'>这里</a></h1>")
#  homeproc
def homeproc1(resquest):
    response = JsonResponse({'key':'value1'})
    return response
#  homeproc1

def homeproc2(resquest):
    cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    response = FileResponse(open(cwd + "/msgapp/templates/test1.png","rb"))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="test1.png"'
    return response
#  homeproc2

def pgproc(resquest):
    template = Template("<h1>这个程序的名字是{{ name }}</h1>")
    context = Context({"name" : "实验平台"})
    return HttpResponse(template.render(context))

#  pgproc