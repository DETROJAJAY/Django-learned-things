from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache

@cache_page(15)                                     #------> view base cachee krva mate ni 1st rite
def home(re):                                               
    return render(re , 'enroll/course.html')


def contact(re):
    return render(re , 'enroll/contact.html')

def temcache(re):
    return render(re , 'enroll/cache.html')


#------> Low level cathe API
# def LowApi(re):
#     mv = cache.get('movie','has_expired') #Aya default value set kri 6 jo movie ma kai na hoi to a set thai jai
#     if mv == 'has_expired':
#         cache.set('movie' , 'The maji' ,20)
#         mv = cache.get('movie')
#     return render(re , 'enroll/lowlevel.html' , {'fm':mv})


# def LowApi(re):
#     mv = cache.get_or_set('fees',1000 , 20 , version=2) 
#     return render(re , 'enroll/lowlevel.html' , {'fm':mv})

# def LowApi(re):
#     data = {'name':'heet' , 'roll':709}
#     cache.set_many(data , 30)
#     mv = cache.get_many(data)
#     return render(re , 'enroll/lowlevel.html' , {'fm':mv})

# def LowApi(re):
#     cache.delete('fees' , version=2)
#     return render(re , 'enroll/lowlevel.html' )

# def LowApi(re):
#     cache.set('roll' , 1121 , 30)
#     mv = cache.get('roll')
#     return render(re , 'enroll/lowlevel.html',{'fm':mv})


# def LowApi(re):
#     #cache.set('roll' , 100 , 600)
#     mv = cache.decr('roll' , delta=2)
#     return render(re , 'enroll/lowlevel.html',{'fm':mv})

# def LowApi(re):
#     cache.clear()
#     return render(re , 'enroll/lowlevel.html')