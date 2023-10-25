from django.db import models


class FAQEntry(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
