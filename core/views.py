from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def home(request):
    # ഡാറ്റാബേസിലുള്ള എല്ലാ ബ്ലോഗ് പോസ്റ്റുകളും എടുക്കുന്നു
    all_posts = BlogPost.objects.all().order_by('-created_at')

    # സ്ലൈഡറിലേക്ക് എപ്പോഴും ഏറ്റവും പുതിയ 2 പോസ്റ്റുകൾ തന്നെ കാണിക്കുന്നു
    slider_posts = all_posts[:2]

    # താഴെ കാണിക്കേണ്ട ബാക്കി പോസ്റ്റുകൾ എടുക്കുന്നു
    posts = all_posts[2:]

    # 👈 ഇവിടെ നമ്മൾ കാറ്റഗറി ഫിൽട്ടറിംഗ് ലോജിക് ചേർത്തു!
    # യുആർഎല്ലിൽ ?category=... ഉണ്ടോ എന്ന് നോക്കുന്നു (ഉദാഹരണത്തിന്: ?category=information)
    category_query = request.GET.get('category')

    if category_query:
        # യൂസർ ക്ലിക്ക് ചെയ്ത കാറ്റഗറിയിലുള്ള പോസ്റ്റുകൾ മാത്രം ഫിൽട്ടർ ചെയ്ത് എടുക്കുന്നു
        posts = all_posts.filter(category__iexact=category_query)

    # നിലവിലുള്ള കാറ്റഗറി ഏതാണെന്ന് അറിയാൻ ഇതും കൂടി ടെംപ്ലേറ്റിലേക്ക് അയക്കുന്നു (ബട്ടൺ ആക്റ്റീവ് ആക്കാൻ)
    context = {
        'slider_posts': slider_posts,
        'posts': posts,
        'selected_category': category_query
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'detail.html', {'post': post})