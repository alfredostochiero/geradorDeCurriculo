from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
import os, sys, subprocess, platform



def home(request):
    return render(request, 'home.html')


def form(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = '+'+request.POST.get('phone')
        sumary = request.POST.get('sumary')
        degree = request.POST.get('degree')
        university = request.POST.get('university')
        previous = request.POST.get('previous')
        skills = request.POST.get('skills')

        profile = Profile(name=name,email=email,phone_number=phone,sumary=sumary,degree=degree,university=university,
                          previous_work=previous, skills=skills)
        profile.save()
    return render(request,'form.html')

def resume(request,id):

    if platform.system() == "Windows":
        pdfkit_config = pdfkit.configuration(
            wkhtmltopdf=os.environ.get('WKHTMLTOPDF_BINARY', 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'))
    else:
        os.environ['PATH'] += os.pathsep + os.path.dirname(sys.executable)
        WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf')],
                                           stdout=subprocess.PIPE).communicate()[0].strip()
        pdfkit_config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)

    user_profile = Profile.objects.get(pk=id)
    num = user_profile.phone_number
    user_profile.phone_number = '('+num[0:2]+')'+num[3:]
    template = loader.get_template('resume.html')
    html = template.render({'user_profile':user_profile})
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
    }
    # config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

    pdf = pdfkit.from_string(html,False,options,configuration=pdfkit_config)
    context = {
        'user': user_profile
    }
    response = HttpResponse(pdf, content_type='application/pdf')
    response["Content-Disposition"] = 'attachment'
    filename = 'resumepdf'
    return response

def list(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'list.html', context)




