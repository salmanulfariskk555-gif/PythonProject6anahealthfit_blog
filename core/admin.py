from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    # 1. അഡ്മിൻ ലിസ്റ്റിൽ കാണിക്കേണ്ട കോളങ്ങൾ (സ്റ്റാറ്റസ് കൂടി ചേർത്തു)
    list_display = ('title', 'category', 'status', 'created_at')

    # 2. അഡ്മിൻ പാനലിൽ നിന്ന് നേരിട്ട് സ്റ്റാറ്റസും കാറ്റഗറിയും മാറ്റാൻ (List Editable)
    list_editable = ('status', 'category')

    # 3. സെർച്ച് ബോക്സ്
    search_fields = ('title', 'content')

    # 4. വലതുവശത്തെ ഫിൽട്ടറുകൾ (സ്റ്റാറ്റസ് വെച്ചും ഫിൽട്ടർ ചെയ്യാം)
    list_filter = ('status', 'category', 'created_at')

    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    # 🚀 എല്ലാ പവർഫുൾ ആക്ഷൻസും ഇവിടെ ചേർത്തിരിക്കുന്നു!
    actions = ['make_published', 'make_draft', 'make_category_health', 'make_category_information']

    # ആക്ഷൻ 1: ഒന്നിച്ച് പബ്ലിഷ് ചെയ്യാൻ
    @admin.action(description="Publish selected posts")
    def make_published(self, request, queryset):
        updated_count = queryset.update(status='published')
        self.message_user(request, f"Successfully published {updated_count} posts.")

    # ആക്ഷൻ 2: ഒന്നിച്ച് ഡ്രാഫ്റ്റിലേക്ക് മാറ്റാൻ
    @admin.action(description="Move selected posts to Draft")
    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='draft')
        self.message_user(request, f"Successfully moved {updated_count} posts to Draft.")

    # ആക്ഷൻ 3: കാറ്റഗറി ഒന്നിച്ച് Health ആക്കാൻ
    @admin.action(description="Change category to Health & Fitness")
    def make_category_health(self, request, queryset):
        updated_count = queryset.update(category='Health & Fitness')
        self.message_user(request, f"Successfully updated {updated_count} posts to Health & Fitness.")

    # ആക്ഷൻ 4: കാറ്റഗറി ഒന്നിച്ച് Information ആക്കാൻ
    @admin.action(description="Change category to Information")
    def make_category_information(self, request, queryset):
        updated_count = queryset.update(category='Information')
        self.message_user(request, f"Successfully updated {updated_count} posts to Information.")