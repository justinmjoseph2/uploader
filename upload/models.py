from django.db import models

# Create your models here.


from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    uploaded_file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
