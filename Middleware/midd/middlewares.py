from django.shortcuts import HttpResponse

# #Fucton based middleware
# def my_middlware(get_responce):
#     print("One time initialization")
#     def my_function(re):
#         print("this is before view")
#         response = get_responce(re)
#         print("this is after  view")
#         return response
#     return my_function



# #Class based middleware
# class mymiddleware:
#     #Run only one time when server starts
#     def __init__(self , get_response):
#         self.get_response = get_response
#         print("One time initializathion")
#     #Run with every request
#     def __call__(self,re):
#         print("This is before view2")
#         #response = self.get_response(re)
#         response = HttpResponse("NIkl chal nikal")      #jyare request ne aagad na vadhva devi hoi OR view pase na jva devi hoi tyare and aahi thi j teno replay aapay 
#         print("This is after middlewarre")
#         return response








#First middlware hook
# class MyProcessMiddleware:
#     def __init__(self, get_reaponse):
#         self.get_reaponse = get_reaponse
    
#     def __call__(self , re):
#         response  = self.get_reaponse(re)
#         return response

#     def process_view(re, *args, **kwargs):
#         print("This is process view before view")
#         return HttpResponse("this isbefore view")



# #Second middlware hook
# class MyExceptionMiddleware:
#     def __init__(self, get_reaponse):
#         self.get_reaponse = get_reaponse
    
#     def __call__(self , re):
#         response  = self.get_reaponse(re)
#         return response

#     def process_exception(self, re, exception):
#         print("This is process view before view")
#         msg = exception
#         class_name = exception.__class__.__name__
#         print(msg)
#         print(class_name)
#         return HttpResponse("there is a Exeption in the view")



#Third middlware hook
class MyTemplateResponseMiddleware:
    def __init__(self, get_reaponse):
        self.get_reaponse = get_reaponse
    
    def __call__(self , re):
        response  = self.get_reaponse(re)
        return response

    def process_template_response(self , re, response):
        print("Process Template Response From Middleview")
        response.context_data["name"]='i change jay'
        return response
