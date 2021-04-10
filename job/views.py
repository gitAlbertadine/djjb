from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Job
# Create your views here.

#def job_list(request):
#    job_list=Job.objects.all()
#    context={'jobs':job_list}
#    return render(request,'job/job_list.html',context)
#def job_detail(request,id):\
#    job_detail=Job.objects.get(id=id)
#    context={'job':job_detail}
#    return render(request,'job/job_detail.html',context)
class JobList(ListView): 
    model = Job
    #context_object_name = 'jobs'
    def get_queryset(self):
        return Job.objects.filter(active=False)
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['myname'] = 'Said ed drief'
        return context
class JobDetail(DetailView):
    model = Job
class JobCreate():
    pass
class JobDelete():
    pass
class JobUpdate():
    pass
