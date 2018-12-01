from django.db import models

ORIGINS = (
        (0, "Limburg"),
        (1, "Non-Dutch"),
        (2, "(Other) Dutch"),
        )

GENDER = (
        (0, "male"),
        (1, "female"),
        )
LANGUAGES = (
        (0, "Nederlands"),
        (1, "andere taal"),
        (2, "dialect"),
        )

TRACK_LEVELS = (
        (0, 'vmbo bl/kl'),
        (1, 'vmbo gl/tl'),
        (2, 'havo'),
        (3, 'vwo'),
        )

SUPPORT_LEVELS = (
        (0, "no"),
        (1, "some"),
        (2, "a lot"),
        (3, "quite a lot"),
        )

REGIONS = (
        (0, "North of South Limburg (Sittard area)"),
        (1, "South-East Limburg (Heerlen area)"),
        (2, "South-West Limburg (Maastricht area)"),
        (3, "Central Limburg"),
        (4, "North Limburg"),
        )

YESNO = (
        (0, "no"),
        (1, "yes"),
        )

CONCEPT_RELATION_LEVELS = (
        (-1, "lower"),
        (0, "same"),
        (1, "higher")
    )

CATEGORIES = (
        (0, "Engels"),
        (1, "Nederlands"),
        (2, "Wiskunde"),
        (3, "Aardrijkskunde"),
        (4, "Geschiedenis"),
        )

def get_value(choice_tuple, key):
    for k, v in choice_tuple:
        if key == k:
            return v
    raise Exception("key not found")


class Pupil(models.Model):
    student_end_6th_year = models.IntegerField(null=True)
    student_end_9th_year = models.IntegerField(null=True)
    study_track_9th = models.IntegerField(choices=TRACK_LEVELS, null=True)
    exit_school_6th_grade = models.IntegerField(null=True)
    exit_school_6th_recommendation = models.CharField(max_length=30, blank=True)
    correct_math_cito = models.IntegerField(null=True)
    correct_study_skills_cito = models.IntegerField(null=True)
    correct_language_cito = models.IntegerField(null=True)
    gender = models.BooleanField(choices=GENDER, null=True)
    highest_educated_parent_level = models.CharField(max_length=100,blank=True)
    origin = models.IntegerField(choices=ORIGINS,null=True)
    home_language = models.IntegerField(choices=LANGUAGES,null=True)
    student_birth_year = models.IntegerField(null=True)
    student_birth_month = models.IntegerField(null=True)
    primary_school = models.IntegerField(null=True)
    secondary_school = models.IntegerField(null=True)
    secondary_school_location = models.IntegerField(null=True)
    region = models.IntegerField(choices=REGIONS, null=True)
    iq_6th = models.IntegerField(null=True) # sumscore ?
    iq_9th = models.FloatField(null=True) # standardized
    dutch_language_test_9th = models.FloatField(null=True)
    math_test_9th = models.FloatField(null=True)
    school_motivation_score = models.FloatField(null=True)
    social_capital_score = models.FloatField(null=True)
    parent_support_home_lessons = models.IntegerField(choices=SUPPORT_LEVELS, null=True)
    parent_support_homework_help = models.IntegerField(choices=SUPPORT_LEVELS, null=True)
    parent_support_motivation = models.IntegerField(choices=SUPPORT_LEVELS, null=True)
    parent_support_professional = models.IntegerField(choices=SUPPORT_LEVELS, null=True)
    ever_registered_as_school_drop_out = models.BooleanField(choices=YESNO, null=True)
    family_both_parents = models.BooleanField(choices=YESNO, null=True)

class Concept(models.Model):
    name = models.CharField(max_length=200)
    video = models.CharField(max_length=20)
    image = models.URLField()
    summary = models.TextField()
    question = models.CharField(max_length=200)
    answer0 = models.CharField(max_length=200)
    answer1 = models.CharField(max_length=200)
    answer2 = models.CharField(max_length=200)
    answer3 = models.CharField(max_length=200)
    correct_answer = models.IntegerField()
    related = models.ManyToManyField('self', symmetrical=False, through='ConceptRelation')
    category = models.IntegerField(choices=CATEGORIES)

    def get_related_concepts(self):
        return ConceptRelation.objects.filter(to_concept=self)

    def __str__(self):
        return self.name

class ConceptRelation(models.Model):
    """
    How the from concept related to the to concept
    """
    from_concept = models.ForeignKey(Concept, related_name='from_concept', on_delete=models.CASCADE)
    to_concept = models.ForeignKey(Concept, related_name='to_concept', on_delete=models.CASCADE)
    level = models.IntegerField(choices=CONCEPT_RELATION_LEVELS)

    def __str__(self):
        return "%s relation from %s to %s" % (get_value(CONCEPT_RELATION_LEVELS, self.level), self.from_concept, self.to_concept)

