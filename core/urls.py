from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),  # www.site.com/about/
    path('contact/', views.contact, name='contact'),  # www.site.com/contact/

    # 👈 ദാ ഈ പുതിയ ലിങ്ക് ഇവിടെ ചേർത്തിട്ടുണ്ട് (ഓരോ ബ്ലോഗിന്റെയും ID വെച്ച് ഓപ്പൺ ചെയ്യാൻ)
    path('post/<int:post_id>/', views.blog_detail, name='blog_detail'),
]