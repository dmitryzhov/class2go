from django.core.management.base import BaseCommand, CommandError
from c2g.models import *
from django.contrib.auth.models import User,Group
from django.db import connection, transaction
from courses.reports.generation.course_quizzes import *

class Command(BaseCommand):
    help = "Get quiz stats for the course. Syntax: manage.py gen_course_quizzes_report <course_handle> [save_to_s3 (1 or 0)]\n"
        
    def handle(self, *args, **options):
        if len(args) == 0:
            print "No course handle supplied!"
            
        try:
            course = Course.objects.get(handle= args[0], mode='ready')
        except:
            print "Failed to find course with given handle"
            return
        
        save_to_s3 = False
        if len(args) > 1: save_to_s3 = True if (args[1] == '1') else False
        
        gen_course_quizzes_report(course, save_to_s3)