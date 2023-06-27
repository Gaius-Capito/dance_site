from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.files.storage import default_storage
from content.models import Images


@receiver(pre_save, sender=Images)
def delete_old_image(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Images.objects.get(pk=instance.pk)
        if old_instance.image_about_us != instance.image_about_us:
            if default_storage.exists(str(old_instance.image_about_us)):
                default_storage.delete(str(old_instance.image_about_us))
        if old_instance.image_about_them != instance.image_about_them:
            if default_storage.exists(str(old_instance.image_about_them)):
                default_storage.delete(str(old_instance.image_about_them))
