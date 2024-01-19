# from django.db import models

# # Create your models here.
# from django.db import models

# # Create your models here.
# from django.db import models

# class Contact(models.Model):
#     # overview = models.TextField()
#     contact_number = models.CharField(max_length=20,null=True)
#     email = models.EmailField(null=True)
#     # email = models.EmailField(null=False)
#     lives_in = models.CharField(max_length=100,null=True)
#     last_studied_in = models.CharField(max_length=100,null=True)
#     gender = models.CharField(max_length=10,null=True)
#     total_experience = models.IntegerField(null=True)
#     relationship_status = models.CharField(max_length=20,null=True)
#     languages = models.CharField(max_length=100,null=True)
#     birthday = models.DateField(null=True)
#     website = models.URLField(null=True)
#     religion = models.CharField(max_length=50,null=True)

#     def __str__(self):
#         return self.contact_number



# class Experience(models.Model):
#     # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     job_title = models.CharField(max_length=100,null=True)
#     company_name = models.CharField(max_length=100,null=True)
#     location = models.CharField(max_length=100,null=True)
#     ex_start_date = models.DateField(null=True)
#     ex_end_date = models.DateField(null=True)
#     ex_des = models.TextField(null=True)
#     # created_at = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.job_title 


# class Skill(models.Model):
    
#     skill = models.CharField(max_length=50)
#     rating = models.FloatField(null=True,blank=True)
    

#     def __str__(self):
#         return self.skill


# # class Education(models.Model):
# #     # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
# #     school_college = models.CharField(max_length=100,null=True,blank=True)
# #     degree = models.CharField(max_length=100,null=True,blank=True)
# #     field_of_study = models.CharField(max_length=100,null=True,blank=True)
# #     university_name = models.CharField(max_length=100,null=True,blank=True)
# #     edu_start_date = models.DateField(null=True,blank=True)
# #     edu_end_date = models.DateField(null=True,blank=True)
# #     edu_des = models.TextField(null=True,blank=True)
# #     # created_at = models.DateTimeField(default=timezone.now)

# #     def __str__(self):
# #         return self.school_college


# class Education(models.Model):
#     # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     school_college = models.CharField(max_length=100)
#     degree = models.CharField(max_length=100,null=True)
#     field_of_study = models.CharField(max_length=100,null=True)
#     university_name = models.CharField(max_length=100,null=True)
#     edu_start_date = models.DateField(null=True)
#     edu_end_date = models.DateField(null=True)
#     edu_des = models.TextField(null=True)
#     # created_at = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.school_college





# class Achievement(models.Model):
#     # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     ach_title = models.CharField(max_length=100)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     ach_des = models.TextField()
#     image = models.ImageField(upload_to='achievements/')
#     # created_at = models.DateTimeField(default=timezone.now)
    

#     def __str__(self):
#         return self.ach_title
    

# # class About(models.Model):
# #     # profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
# #     about_title = models.CharField(max_length=100,null=True,blank=True)
# #     about_des = models.TextField(null=True,blank=True)
# #     # created_at = models.DateTimeField(default=timezone.now)
# #     VISIBILITY_CHOICES = (
# #         ('everyone', 'Everyone'),
# #         ('yourContacts', 'Your Contacts'),
# #         ('onlyMe', 'Only Me'),
# #     )

# #     # Create CharFields to store radio button selections
# #     title_visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='everyone')
# #     def __str__(self):
# #         return self.about_title    


# class About(models.Model):
#     about_title = models.CharField(max_length=255)
#     about_des = models.CharField(max_length=255)
    

#     def __str__(self):
#         return self.about_title






# #-------------------------------------------------------------------------------  


# class WorkPortfolio(models.Model):
#     # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     work_title = models.CharField(max_length=100)
#     work_des = models.TextField()
#     link = models.URLField()
#     # created_at = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.work_title
    
# class PlaceLived(models.Model):
#     # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     place = models.CharField(max_length=100)
#     place_start_date = models.DateField()
#     place_end_date = models.DateField()
#     # currently_living_in = models.BooleanField()
#     # created_at = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.place    
    




# class Relationship(models.Model):
#     # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     relationship_type = models.CharField(max_length=50)
#     # created_at = models.DateTimeField(default=timezone.now)
    
#     def __str__(self):
#         return self.name



from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

class Contact(models.Model):
    # overview = models.TextField()
    contact_number = models.CharField(max_length=20,null=True)
    email = models.EmailField(null=True)
    # email = models.EmailField(null=False)
    lives_in = models.CharField(max_length=100,null=True)
    last_studied_in = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=10,null=True)
    total_experience = models.IntegerField(null=True)
    relationship_status = models.CharField(max_length=20,null=True)
    languages = models.CharField(max_length=100,null=True)
    birthday = models.DateField(null=True)
    website = models.URLField(null=True)
    religion = models.CharField(max_length=50,null=True)
    overview_contact_visibility = models.CharField(max_length=20, default="Public Friends",null=True,blank=True)
   
    def __str__(self):
        return self.contact_number



class Experience(models.Model):
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100,null=True)
    company_name = models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100,null=True)
    ex_start_date = models.DateField(null=True)
    ex_end_date = models.DateField(null=True)
    ex_des = models.TextField(null=True)
    ex_jobtitle_visibility = models.CharField(max_length=20, default="Public Friends",null=True,blank=True)
   
    # created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job_title 


class Skill(models.Model):
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill = models.CharField(max_length=50,null=True,blank=True)
    rating = models.IntegerField()
    skills_name_visibility = models.CharField(max_length=20, default="Public Friends",null=True,blank=True)
    skills_rating_visibility = models.CharField(max_length=20, default="Public Friends",null=True,blank=True)
   

    def __str__(self):
        return self.skill





class Education(models.Model):
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    school_college = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    university_name = models.CharField(max_length=100)
    edu_start_date = models.DateField()
    edu_end_date = models.DateField()
    edu_des = models.TextField()
    edu_title_visibility = models.CharField(max_length=20, default="Public Friends",null=True,blank=True)
   
    # created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.school_college





class Achievement(models.Model):
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ach_title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    ach_des = models.TextField()
    image = models.ImageField(upload_to='achievements/')
    ach_title_visibility = models.CharField(max_length=20, default="Public Friends",null=True,blank=True)
   
    # created_at = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.ach_title
    

# class About(models.Model):
#     # profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
#     about_title = models.CharField(max_length=100,null=True,blank=True)
#     about_des = models.TextField(null=True,blank=True)
#     # created_at = models.DateTimeField(default=timezone.now)
#     VISIBILITY_CHOICES = (
#         ('everyone', 'Everyone'),
#         ('yourContacts', 'Your Contacts'),
#         ('onlyMe', 'Only Me'),
#     )

#     # Create CharFields to store radio button selections
#     title_visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='everyone')
#     def __str__(self):
#         return self.about_title    


class About(models.Model):
    about_title = models.CharField(max_length=255)
    about_des = models.CharField(max_length=255)
    title_visibility = models.CharField(max_length=20, default="Public Friends",null=True,blank=True)
    description_visibility = models.CharField(max_length=20, default="Public Friends",null=True,blank=True)

    def __str__(self):
        return self.about_title






#-------------------------------------------------------------------------------  


class WorkPortfolio(models.Model):
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    work_title = models.CharField(max_length=100,null=True,blank=True)
    work_des = models.TextField(null=True,blank=True)
    link = models.URLField(null=True,blank=True)
    # created_at = models.DateTimeField(default=timezone.now)
    work_title_visibility = models.CharField(max_length=20, default="Public Friends",null=True,blank=True)
    work_des_visibility = models.CharField(max_length=20, default="Public Friends",null=True,blank=True)
    work_link_visibility = models.CharField(max_length=20, default="Public Friends",null=True,blank=True)

    def __str__(self):
        return self.work_title
    
class PlaceLived(models.Model):
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    place = models.CharField(max_length=100,null=True,blank=True)
    place_start_date = models.DateField(null=True,blank=True)
    place_end_date = models.DateField(null=True,blank=True)
    # currently_living_in = models.BooleanField()
    # created_at = models.DateTimeField(default=timezone.now)
    place_visibility = models.CharField(max_length=20, default="Public Friends",null=True,blank=True)
   

    def __str__(self):
        return self.place    
    




class Relationship(models.Model):
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    relationship_type = models.CharField(max_length=50)
    # created_at = models.DateTimeField(default=timezone.now)
    relationship_name_visibility = models.CharField(max_length=20, default="Public Friends",null=True,blank=True)
    relationship_type_visibility = models.CharField(max_length=20, default="Public Friends",null=True,blank=True)
   
    def __str__(self):
        return self.name

