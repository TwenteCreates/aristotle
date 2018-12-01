from django.contrib import admin
from analytics.models import Pupil, Concept, ConceptRelation


class PupilAdmin(admin.ModelAdmin):
    list_display = [getattr(field, 'name') for field in Pupil._meta.fields]

class ConceptAdmin(admin.ModelAdmin):
    list_display = [getattr(field, 'name') for field in Concept._meta.fields]

class ConceptRelationAdmin(admin.ModelAdmin):
    list_display = ['from_concept', 'level', 'to_concept']

admin.site.register(Pupil, PupilAdmin)
admin.site.register(Concept, ConceptAdmin)
admin.site.register(ConceptRelation, ConceptRelationAdmin)
