# models.py

from django.db import models
from django.contrib.auth.models import User

class ATKResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.CharField(max_length=10, choices=(('negative', 'Negative'), ('positive', 'Positive')))
    image = models.ImageField(upload_to='atk_results/')  # ImageField には `Pillow` ライブラリが必要です

    def __str__(self):
        return f"ATK Result for {self.user.username}: {self.result}"
