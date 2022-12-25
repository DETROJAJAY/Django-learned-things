from django.contrib import admin

#__________________________________Abstract Base Class____________________________________#
from .models import Student,Teacher,Contractor

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','age','fees']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','date','salary']

@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','date','payment']



#__________________________________Multi-table Inheritance____________________________________#
from .models import Student2,ExamCenter 

@admin.register(ExamCenter)
class ExamcenterAdmin(admin.ModelAdmin):
    list_display = ['id','cname','city']

@admin.register(Student2)
class Student2Admin(admin.ModelAdmin):
    list_display = ['id','cname','city','name','roll']          #aama 'cname' to show thaityar mate 6 baki add krti vakhte to aama nalakhi to pn batave j


#__________________________________Proxy Model____________________________________#
from .models import ExamCenter2,MyExamCenter

@admin.register(ExamCenter2)
class ExamCenter2Admin(admin.ModelAdmin):
    list_display = ['id','cname','city']

@admin.register(MyExamCenter)
class MyExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id','cname','city'] 