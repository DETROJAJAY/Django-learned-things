from .models import page
from django.db.models.signals import post_delete
from django.dispatch import receiver


#User delete thai tyare tenu create krelu page pn delete thai jase aana thi
@receiver(post_delete, sender=page)                         
def delete_releted_user(sender, instance, **kwargs):
    print("page post_Delete")
    instance.user_name.delete()
