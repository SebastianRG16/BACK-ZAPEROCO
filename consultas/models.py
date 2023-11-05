from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class Donation(models.Model):

    DONATION_CHOICES = [
        ('urna', 'Urna'),
        ('electrónico', 'Electrónico'),
    ]

    USER_CHOICES = [
        ('asisitente', 'Asistente'),
        ('especial', 'Invitado especial'),
    ]

    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    card = models.CharField(max_length=50)
    celphone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    tipe_donation = models.CharField(max_length=20 , choices=DONATION_CHOICES)
    tipe_user = models.CharField(max_length=50, choices=USER_CHOICES)

    def __str__(self):
        return self.name

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