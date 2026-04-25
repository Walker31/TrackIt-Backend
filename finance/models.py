from django.db import models
from django.contrib.auth.models import User
from encrypted_fields import fields

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('transport', 'Transport'),
        ('shopping', 'Shopping'),
        ('health', 'Health'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    amount = fields.EncryptedCharField(max_length=100)  # Encrypted Decimal as String
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    timestamp = models.DateTimeField()
    description = fields.EncryptedTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.amount}"

    class Meta:
        ordering = ['-timestamp']
