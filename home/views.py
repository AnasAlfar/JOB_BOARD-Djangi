from django.shortcuts import render, redirect
from jobb.models import Job, Category
from django.db.models import Count
from accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Testimonial
from .forms import TestimonialForm



# Create your views here.


def home(request):
    numOfjob = Job.objects.count()
    category = Category.objects.all()
    categories_with_job_counts = Category.objects.annotate(job_count=Count('jobs'))
    combined_data = [{'category': cat, 'job_count': count} for cat, count in zip(category, categories_with_job_counts)]
    first_four_jobs = Job.objects.all()[:4]
    
    context = {'numOfjob':numOfjob,'combined_data':combined_data,'first_four_jobs':first_four_jobs}
    
    return render(request,"home/home.html",context)


def testimonial(request):
    #imageuser = request.user.profile.image.url
    
    testimonials = Testimonial.objects.filter(accepted=True)
    context = {'testimonials':testimonials}
    
    return render(request,'home/testimonial.html',context)



@login_required
def create_testimonial(request):
    
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.accepted = False  
            testimonial.save()
            return redirect('home:testimonial')
    else:
        form = TestimonialForm()
    
    return render(request,'home/create_testimonial.html',{'form':form})