from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class Donation(models.Model):
    name = models.CharField(max_length=50)
    tipe_donation = models.CharField(max_length=50)
    tipe_user = models.CharField(max_length=50)
    donation = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# Definir un receptor para la señal de creación de Donation
@receiver(post_save, sender=Donation)
def donation_created(sender, instance, created, **kwargs):
    print('creando')
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "donation_updates",
            {
                "type": "donation.update",
                "message": f"Se ha creado una nueva donación: {instance.name}."
            }
        )

# Definir un receptor para la señal de eliminación de Donation
@receiver(post_delete, sender=Donation)
def donation_deleted(sender, instance, **kwargs):
    print('eliminando')
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "donation_updates",
        {
            "type": "donation.update",
            "message": f"Se ha eliminado la donación: {instance.name}."
        }
    )