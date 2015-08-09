# from django.shortcuts import render
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from django.views.generic.base import TemplateView

import datetime
# # Create your views here.
# def index(request):
#     return render_to_response('index.html','',context_instance = RequestContext(request))



# Create your views here.
class index(TemplateView):
    template_name = 'index.html'
    def get_context_data(self,**kwargs):
        # today = datetime.datetime.today()
        context_data = super(index,self).get_context_data(**kwargs)
        # context_data['blogcate'] = blogcate
        # context_data['anli'] = anli
        return context_data
