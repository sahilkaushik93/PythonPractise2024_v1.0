from django.contrib import admin
from .models import Form

# Register your models here.
class FormAdmin(admin.ModelAdmin):
    # It will display all these names on admin page in "Forms"
    list_display = ("first_name", "last_name", "email", 
                    "date", "occupation")
    # Adding a search bar
    search_fields = ("first_name", "last_name", "email")
    # Adding Filter
    list_filter = ("date", "occupation")
    # Ordering Data
    ordering = ("first_name",)
    # Making few fields "read only"
    readonly_fields = ("occupation", )


admin.site.register(Form, FormAdmin)