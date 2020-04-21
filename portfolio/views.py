from django.shortcuts import render
#from django.http import HttpResponse
from .models import Project
from .models import WorkExperience
from .models import Education
from .models import Skill
from .models import OtherSkill

def home(request):
    projects=Project.objects.all()
    experiences=WorkExperience.objects.all()
    educations=Education.objects.all()
    skills=Skill.objects.all()
    otherskills=OtherSkill.objects.all()



    return render(request,'portfolio/home.html',{'projects':projects, 'experiences':experiences, 'education':educations,
    				'skills': skills, 'otherskills':otherskills} )
