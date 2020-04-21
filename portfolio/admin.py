from django.contrib import admin
from .models import Project
from .models import WorkExperience
from .models import Education
from .models import Skill
from .models import OtherSkill



admin.site.register(Project)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(OtherSkill)
