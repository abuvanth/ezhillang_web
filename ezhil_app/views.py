from django.shortcuts import render
from .forms import CodeForm
import time,os,subprocess
def index(request):
   if request.method == "GET":
      return render(request,'index.html')
   #assert( request.method == "POST" )
   if request.method=='POST':
      form = CodeForm(request.POST)
      timestr = time.strftime("%Y%m%d-%H%M%S")
      if form.is_valid():
         text_input=form.cleaned_data['code'] 
         print(text_input)
         tmp_file=open(os.path.join(os.path.dirname(__file__),timestr+'.n'),'wb')
         tmp_file.write(text_input.encode('utf-8'))
         tmp_file.close()
         print(text_input)
         output=subprocess.run(['ezhili',os.path.join(os.path.dirname(__file__),timestr+'.n')],stdout=subprocess.PIPE)
         output=output.stdout.decode('utf-8')
         print(output)
         title = u"எழில் வெளியீடு"
         return render(request,u'index.html',{'text_input':text_input,"output":output,"title":title})

