from django.db import models

# Create your models here.
class EmailVerification(models.Model):
    email = models.EmailField(unique=True)
    confirmation_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email
    class Meta:
        db_table = 'email'
