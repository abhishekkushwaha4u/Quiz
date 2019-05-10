from django.db import models

class multiple_choice(models.Model):
    question_number = models.IntegerField()
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=10)
    a = models.CharField(max_length=200)
    b = models.CharField(max_length=200)
    c = models.CharField(max_length=200)
    d = models.CharField(max_length=200)
    
    def __str__(self):
           return "{}) {} \n {} \t {} \n {} \t {}".format(self.question_number, self.question,self.a,self.b,self.c,self.d)

class improved_question(models.Model):
    question = models.CharField(max_length=300,blank=True)
    question_img = models.FileField(blank=True, null=True)
    answer = models.CharField(max_length=10,blank=True)
    a = models.CharField(max_length=200,blank=True)
    a_img = models.FileField(blank=True,null=True)
    b = models.CharField(max_length=200,blank=True)
    b_img = models.FileField(blank=True,null=True)
    c = models.CharField(max_length=200,blank=True)
    c_img = models.FileField(blank=True,null=True)
    d = models.CharField(max_length=200,blank=True)
    d_img = models.FileField(blank=True,null=True)
    
    def __str__(self):
           return "{} \n {} \t {} \n {} \t {}".format( self.question,self.a,self.b,self.c,self.d)

 
