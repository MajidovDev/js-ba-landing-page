from django.contrib import admin
from .models import Student, Course, myUserModel, CourseReview, ModuleCourse, IntroductionInfo

admin.site.register(CourseReview)
admin.site.register(myUserModel)

admin.site.register(IntroductionInfo)
admin.site.register(Student)
admin.site.register(Course)

admin.site.register(ModuleCourse)
