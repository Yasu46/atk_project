# models.py

from django.db import models
from accounts.models import Account

class ATKResult(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    result = models.CharField(max_length=10, choices=(('negative', 'Negative'), ('positive', 'Positive')))
    image = models.ImageField(upload_to='atk_results/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ATK Result for {self.user.username}: {self.result}"
