from django.db import models


class BlogPost(models.Model):
    # സ്റ്റാറ്റസ് കൊടുക്കാനുള്ള ഓപ്ഷനുകൾ (Draft അല്ലെങ്കിൽ Published)
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    # 👈 ഇവിടെ max_length എന്ന് കറക്റ്റ് ചെയ്തിട്ടുണ്ട്
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100)

    # ഫോട്ടോ യുആർഎൽ, ഒപ്പം ഫയൽ നേരിട്ട് അപ്‌ലോഡ് ചെയ്യാനുള്ള പുതിയ ഫീൽഡ്
    image_url = models.URLField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    # പുതിയ പോസ്റ്റ് സ്റ്റാറ്റസ് ഫീൽഡ്
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    created_at = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ഒരു ഡിഫാൾട്ട് ഇമേജ് സെറ്റ് ചെയ്യുന്നു (ഫോട്ടോയോ യുആർഎല്ലോ ഇല്ലെങ്കിൽ കാണിക്കാൻ)
        if not self.image_url:
            self.image_url = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1200&q=80"

    def __str__(self):
        return self.title