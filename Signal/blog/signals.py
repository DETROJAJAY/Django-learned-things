from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver,Signal
from django.db.models.signals import pre_init,pre_save,pre_delete ,post_init,post_save,post_delete,pre_migrate,post_migrate
from django.core.signals import request_finished,request_started,got_request_exception
from django.db.backends.signals import connection_created

# @receiver(user_logged_in , sender=User)
# def login_success(sender, request, user, **kwargs):
#     print("........----------_________")
#     print("Logged in singnl...Run Inro...")
#     print("sender: " , sender)
#     print("Request: " , request)
#     print("User: ", user)
#     print("User Pass: ", user.password)
#     print(f"KWargs: {kwargs}")
# #user_logged_in.connect(login_success,sender=User)


# @receiver(user_logged_out , sender=User)
# def log_out(sender, request, user, **kwargs):
#     print("........----------_________")
#     print("Logged out singnl...Run Inro...")
#     print("sender: " , sender)
#     print("Request: " , request)
#     print("User: ", user)
#     print("User Pass: ", user.password)
#     print(f"KWargs: {kwargs}")
# #user_logged_out.connect(log_out,sender=User)


# @receiver(user_login_failed)
# def login_faild(sender, credentials, request, **kwargs):
#     print("........----------_________")
#     print("Login faild singnl...Run Inro...")
#     print("sender: " , sender)
#     print("Request: " , request)
#     print("Credential: ", credentials)
#     print(f"KWargs: {kwargs}")
# #use_login_failed.connect(login_faild)

# @receiver(pre_save,sender = User)
# def at_beginning_save(sender , instance,**kwargs):
#     print("___________________________")
#     print("ppre save signal....")
#     print("sender: " , sender)
#     print("Instance: ", instance)
#     print(f"KWargs: {kwargs}")

# @receiver(post_save,sender = User)
# def at_ending_save(sender , instance,created , **kwargs):
#     if created:
#         print("___________________________")
#         print("post save signal....")
#         print("New Record")
#         print("sender: " , sender)
#         print("Instance: ", instance)
#         print("created: " ,created)
#         print(f"KWargs: {kwargs}")
#     else:
#         print("___________________________")
#         print("post save signal....")
#         print("Updated")
#         print("sender: " , sender)
#         print("Instance: ", instance)
#         print("Created: ",created)
#         print(f"KWargs: {kwargs}")

# @receiver(pre_delete,sender = User)
# def at_beginning_delete(sender , instance,**kwargs):
#     print("___________________________")
#     print("ppre delete signal....")
#     print("sender: " , sender)
#     print("Instance: ", instance)
#     print(f"KWargs: {kwargs}")

# @receiver(post_delete,sender = User)
# def at_ending_delete(sender , instance , **kwargs):
#     print("___________________________")
#     print("post delete signal....")
#     print("New Record")
#     print("sender: " , sender)
#     print("Instance: ", instance)
#     print(f"KWargs: {kwargs}")

# @receiver(pre_init , sender=User)
# def at_bignin_init(sender,*args,**kwargs):
#     print("___________________________")
#     print("pre init signal......")
#     print("sender: " , sender)
#     print("Args: ", *args)
#     print(f"KWargs: {kwargs}")

# @receiver(post_init , sender=User)
# def at_ending_init(sender,*args,**kwargs):
#     print("___________________________")
#     print("post init signal......")
#     print("sender: " , sender)
#     print("Args: ", *args)
#     print(f"KWargs: {kwargs}")


# @receiver(request_started)
# def At_bigning_request(sender , environ , **kwargs):
#     print("___________________________")
#     print("At bigning request......")
#     print("sender: " , sender)
#     print("Environ: ", environ)
#     print(f"KWargs: {kwargs}")

# @receiver(request_finished)
# def At_ending_request(sender  , **kwargs):
#     print("___________________________")
#     print("At ending request......")
#     print("sender: " , sender)
#     print(f"KWargs: {kwargs}")

# @receiver(got_request_exception)
# def Got_request_ex(sender , request , **kwargs):
#     print("___________________________")
#     print("At exeption request......")
#     print("sender: " , sender)
#     print("Request: ", request)
#     print(f"KWargs: {kwargs}")


# @receiver(pre_migrate)
# def before_install_app(sender , app_config , verbosity , interactive , using ,plan , apps ,**kwargs):
#     print("___________________________")
#     print("before install APP......")
#     print("sender: " , sender)
#     print("APP_config: ", app_config)
#     print("Verbosity: ",verbosity)
#     print("Interative: ", interactive)
#     print("Using ", using)
#     print("Plan: ",plan)
#     print("App: ",apps)
#     print(f"KWargs: {kwargs}")

# @receiver(post_migrate)
# def at_end_migrate_flush(sender , app_config , verbosity , interactive , using ,plan , apps ,**kwargs):
#     print("___________________________")
#     print("at_end_migrate_flush......")
#     print("sender: " , sender)
#     print("APP_config: ", app_config)
#     print("Verbosity: ",verbosity)
#     print("Interative: ", interactive)
#     print("Using ", using)
#     print("Plan: ",plan)
#     print("App: ",apps)
#     print(f"KWargs: {kwargs}")


# @receiver(connection_created)
# def conn_db(sender , connection, **kwargs):
#     print(">.....................")
#     print("Initial connection to the database .......")
#     print("Sender: ", sender)
#     print("Connecton: ",connection)
#     print(f"kwangs: {kwargs}")





#Create a coustom signal by our hand
notification = Signal()

#now create function for our signal which called reciver funcation
@receiver(notification)
def sgn(sender , **kwargs):
    print("______________________")
    print(sender)
    print(F' kwags: {kwargs}')
    print("Notificathion")