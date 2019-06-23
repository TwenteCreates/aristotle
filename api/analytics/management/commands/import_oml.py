from django.core.management.base import BaseCommand, CommandError
import csv
from analytics.models import *


def get_key(choice_tuple, value):
    if not value:
        return None
    for k, v in choice_tuple:
        if value == v:
            return k
    raise Exception("value not found")


def int_process(int_string):
    return int(int_string) if int_string else 0


def float_process(float_string):
    return float(float_string) if float_string else 0


def bool_process(bool_string):
    if bool_string == '1':
        return True
    elif bool_string == '0':
        return False
    else:
        return None


class Command(BaseCommand):
    help = 'imports oml data csv to the pupil model'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
        try:
            file = open(options['filename'], 'r')
        except IOError as e:
            raise CommandError('Error opening file', e)
        else:
            reader = csv.reader(file, delimiter=',', quotechar='"')
            first = True
            for row in reader:
                if first:
                    header = row
                    first = False
                else:
                    print(row)
                    Pupil.objects.create(
                            id = int_process(row[0]),
                            student_end_6th_year=int_process(row[1]),
                            student_end_9th_year=int_process(row[2]),
                            study_track_9th=get_key(TRACK_LEVELS, row[3]),
                            exit_school_6th_grade=int_process(row[4]),
                            exit_school_6th_recommendation=row[5],
                            correct_math_cito=int_process(row[6]),
                            correct_study_skills_cito=int_process(row[7]),
                            correct_language_cito=int_process(row[8]),
                            gender=bool_process(row[9]),
                            highest_educated_parent_level=row[10],
                            origin=get_key(ORIGINS, row[11]),
                            home_language=get_key(LANGUAGES, row[12]),
                            student_birth_year=int_process(row[13]),
                            student_birth_month=int_process(row[14]),
                            primary_school=int_process(row[15]),
                            secondary_school=int_process(row[16]),
                            secondary_school_location=int_process(row[17]),
                            region=get_key(REGIONS, row[18]),
                            iq_6th=int_process(row[19]),
                            iq_9th=float_process(row[20]),
                            dutch_language_test_9th=float_process(row[21]),
                            math_test_9th=float_process(row[22]),
                            school_motivation_score=float_process(row[23]),
                            social_capital_score=float_process(row[24]),
                            parent_support_home_lessons=get_key(SUPPORT_LEVELS, row[25]),
                            parent_support_homework_help=get_key(SUPPORT_LEVELS, row[26]),
                            parent_support_motivation=get_key(SUPPORT_LEVELS, row[27]),
                            parent_support_professional=get_key(SUPPORT_LEVELS, row[28]),
                            ever_registered_as_school_drop_out=bool_process(row[29]),
                            family_both_parents=bool_process(row[30]),
                            )
