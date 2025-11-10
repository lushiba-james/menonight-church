from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title= models.CharField(max_length=255)
    content=models.TextField()
    image= models.ImageField(upload_to= 'blog_images/', blank=True, null= True)
    author= models.CharField( max_length=50, default="Admin")
    created_at= models.TimeField(auto_now_add=True)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})
    
    
    # ministries
    

class Ministry(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='ministries/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


# gallery model
class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('church_events', 'Church Events'),
        ('youth', 'Youth'),
        ('outreach', 'Outreach'),
    ]
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='church_events')
    uploaded_at = models.DateTimeField(auto_now_add=True)  # ✅ add this line

    def __str__(self):
        return f"{self.category} - {self.image.name}"