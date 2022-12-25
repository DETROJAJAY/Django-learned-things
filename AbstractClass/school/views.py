from django.shortcuts import render
from .models import Student,Teacher,Contractor

def Home(re):
    student_data = Student.myQM.all() 
    teacher_data = Teacher.myQM.get_stu_age_range(20,24)        #Use Created Custom Mnager With Custom Query Set
    contractor_data = Contractor.myQM.all() 
    return render(re , 'school/home.html', {'st':student_data , 'th':teacher_data , 'ct':contractor_data})


from .models import Student2,ExamCenter
def Home2(re):
    student2_data = Student2.myown.all()              #Use Custom manager which Also Change Quesry Set
    examcenter_data = ExamCenter.objects.all()        #Here use inbuilt manager
    return render(re , 'school/home.html', {'st':student2_data , 'ex':examcenter_data})


from .models import ExamCenter2,MyExamCenter
def Home3(re):
    examcenter2_data = ExamCenter2.myobj.all()          #use our created Manager "myobj"
    myexam_data = MyExamCenter.myobj.all()              #use our created Manager "myobj"
    return render(re, 'school/home.html', {'ec2':examcenter2_data , 'myex':myexam_data})




#______________________________________Simple Model Inhereturnce mate________________________________________#

# def Home(re):
#     student_data = Student.objects.all()
#     teacher_data = Teacher.objects.all()
#     contractor_data = Contractor.objects.all()
#     return render(re , 'school/home.html', {'st':student_data , 'th':teacher_data , 'ct':contractor_data})


# from .models import Student2,ExamCenter
# def Home2(re):
#     student2_data = Student2.objects.all()
#     examcenter_data = ExamCenter.objects.all()
#     return render(re , 'school/home.html', {'st':student2_data , 'ex':examcenter_data})


# from .models import ExamCenter2,MyExamCenter
# def Home3(re):
#     examcenter2_data = ExamCenter2.objects.all()
#     myexam_data = MyExamCenter.objects.all()
#     return render(re, 'school/home.html', {'ec2':examcenter2_data , 'myex':myexam_data})