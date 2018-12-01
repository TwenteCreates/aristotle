from django.contrib import admin
from analytics.models import *


class PupilAdmin(admin.ModelAdmin):
    list_display = [getattr(field, 'name') for field in Pupil._meta.fields]


class ConceptAdmin(admin.ModelAdmin):
    list_display = [getattr(field, 'name') for field in Concept._meta.fields]
    search_fields = ('naam', 'category')


class ConceptRelationAdmin(admin.ModelAdmin):
    list_display = ['from_concept', 'level', 'to_concept']
    search_fields = ('from_concept', 'to_concept')

class PrimarySchoolAdmin(admin.ModelAdmin):
    list_display = ['instellings_naam', 'plaatsnaam', 'provincie', 'brin_nummer', 'internetadres']
    search_fields = ('instellings_naam', 'plaatsnaam', 'provincie', 'brin_nummer', 'internetadres')


admin.site.register(Pupil, PupilAdmin)
admin.site.register(Concept, ConceptAdmin)
admin.site.register(ConceptRelation, ConceptRelationAdmin)
admin.site.register(PrimarySchool, PrimarySchoolAdmin)
