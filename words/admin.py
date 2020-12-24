from django.contrib import admin
from .models.wordamazigh import Word
from .models.translations import translations
from .models.languages import Languages
from .models.types_trans import Types_translations
from .models.types import Types

# Register your models here.

class TypeInline(admin.StackedInline):
    model = Types_translations
    extra = 3

class Typeadmin(admin.ModelAdmin):
    inlines=[TypeInline]

admin.site.register(Word)
admin.site.register(translations)
admin.site.register(Languages)
admin.site.register(Types,Typeadmin)
