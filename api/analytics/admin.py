from django.utils.translation import ugettext_lazy
from django.contrib.admin import AdminSite
from django.contrib import admin
from analytics.models import *


class TeacherAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('Aristotle Teacher')
    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('Aristotle Teacher')
    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Content Management System')


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

teacher_admin = TeacherAdminSite()
teacher_admin.register(Pupil, PupilAdmin)
teacher_admin.register(Concept, ConceptAdmin)
teacher_admin.register(ConceptRelation, ConceptRelationAdmin)
teacher_admin.register(PrimarySchool, PrimarySchoolAdmin)

