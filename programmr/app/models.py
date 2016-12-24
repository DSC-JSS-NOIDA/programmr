from django.conf import settings

from django.db import models

# Create your models here.

class Users(models.Model):
	name=models.CharField(max_length=120)
	email_ID=models.EmailField(max_length=200)
	avatar=models.URLField(max_length=120)
	year=models.CharField(max_length=120)
	branch=models.CharField(max_length=120)
	mobile_no=models.CharField(max_length=120)
	timestamp=models.DateTimeField(auto_now=True,auto_now_add=False)
	total_score=models.CharField(max_length=120)

def __unicode__(self):
		return self.name

class Questions(models.Model):
	title=models.CharField(max_length=120)
	detail=models.TextField()
	constraint=models.CharField(max_length=120)
	input_format=models.TextField()
	output_format=models.TextField()
	sample_testcase=models.TextField()
	testcase_input=models.TextField()
	testcase_output=models.TextField()

def __unicode__(self):
		return self.title


class Submission(models.Model):
	user_ID=models.CharField(max_length=120)
	question_ID=models.CharField(max_length=120)
	status=models.CharField(max_length=120)
	source_code_URL=models.URLField(max_length=120)
	date=models.DateTimeField(auto_now=True,auto_now_add=False)

def __unicode__(self):
		return self.status

