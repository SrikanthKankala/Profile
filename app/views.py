# from django.http import HttpResponse
# from django.http import Http404
# from django.shortcuts import render
# from django.utils.dateparse import parse_date
# from django.core.exceptions import ObjectDoesNotExist
# from django.core.exceptions import ValidationError
# from datetime import datetime
# from django.http import JsonResponse
# from django.http import HttpResponse
# # Create your views here.
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Contact,Experience,Skill,Education,Achievement,About,WorkPortfolio,PlaceLived,Relationship
# from .forms import ContactForm
# import MySQLdb as mysql
# from django.db import connections
# from django.core.exceptions import ObjectDoesNotExist
# from django.db import IntegrityError
# from django.db import transaction
# from django.views.decorators.csrf import csrf_exempt
# from django.core.exceptions import ObjectDoesNotExist
# from django.db import transaction
# from django.db import DatabaseError
# def Insertview(request):  #index html view
#     return render(request,'app/insert.html')

# # ---------------------------------------Contact Total OK---------------------------

# def Insertdata(request):
#  if request.method == 'POST':
    
#     #data come from html too view
#     Contact_number = request.POST['Contact_number']
#     Email = request.POST['Email']
#     Lives_in= request.POST['Lives_in']
#     Last_studied_in = request.POST['Last_studied_in']
#     Gender = request.POST['Gender']
#     Total_experience = request.POST['Total_experience']
#     Relationship_status= request.POST['Relationship_status']
#     Languages = request.POST['Languages']
#     Birthday= request.POST['Birthday']
#     Website= request.POST['Website']
#     Religion= request.POST['Religion']
#     # action=request.POST['action']
    
#     #creating objct of model class
    
#     newusers = Contact.objects.create(
#             contact_number =Contact_number,
#             email =Email,
#             lives_in=Lives_in,
#             last_studied_in =Last_studied_in,
#             gender=Gender,
#             total_experience=Total_experience,
#             relationship_status =Relationship_status,
#             languages =Languages,
#             birthday =Birthday,
#             website =Website,
#             religion =Religion
#         )
#     newusers.save()
    
#     #After insert render on show.html page
#     #return render(request,'app/show.html')
#     return redirect('editpage', pk=newusers.id)
#  else:
#         return render(request, 'app/insert.html')
 



# def displaydata(request):
#     #select  * from tablename
#     all_data= Contact.objects.all()
#     return render(request,'app/show_profile_form.html',{'key1':all_data})  #key1


# #Edit page view
# def Editpage(request,pk):
#     #fetching the data of particular id
#     get_data=Contact.objects.get(id=pk)    #pk - primary key
#     # return render(request,'app/edit.html',{'key2':get_data})

#     return render(request,'app/edit_overview.html',{'key2':get_data})








# def Updatedata(request, pk):
#     udata = Contact.objects.get(id=pk)

#     # Update fields only if they are provided in the POST data
#     udata.contact_number = request.POST.get('Contact_number', udata.contact_number)
#     udata.email = request.POST.get('Email', udata.email)
#     udata.lives_in = request.POST.get('Lives_in', udata.lives_in)
#     udata.last_studied_in = request.POST.get('Last_studied_in', udata.last_studied_in)
#     udata.gender = request.POST.get('Gender', udata.gender)
#     udata.total_experience = request.POST.get('Total_experience', udata.total_experience)
#     udata.relationship_status = request.POST.get('Relationship_status', udata.relationship_status)
#     udata.languages = request.POST.get('Languages', udata.languages)

#     # Handle the date format for 'Birthday' if it's not empty
#     birthday_str = request.POST.get('Birthday', '')
#     if birthday_str:
#         try:
#             # Parse the date in "DD/MM/YYYY" format
#             birthday_obj = datetime.strptime(birthday_str, '%d/%m/%Y')
#             formatted_birthday = birthday_obj.strftime('%Y-%m-%d')
#             udata.birthday = formatted_birthday
#         except ValueError:
#             # Handle invalid date format
#             # You can add a validation message or take appropriate action here
#             pass

#     udata.website = request.POST.get('Website', udata.website)
#     udata.religion = request.POST.get('Religion', udata.religion)
    
#     # Save the data
#     udata.save()
    
#     return redirect('showpage')

# #delete the
# def Deletedata(request,pk):
#     ddata =Contact.objects.get(id=pk)
#     ddata.delete()
#     return redirect('showpage')


# def update_contact_number(request, pk):
#     if request.method == 'POST':
#         Contact_number = request.POST['Contact_number']
#         contact = Contact.objects.get(id=pk)
#         contact.contact_number = Contact_number
#         contact.save()
#         return redirect('showpage')

#     # Handle GET request if needed
#     # ...

# def update_email(request, pk):
#     if request.method == 'POST':
#         Email = request.POST['Email']
#         contact = Contact.objects.get(id=pk)
#         contact.email = Email
#         contact.save()
#         return redirect('showpage')

#     # Handle GET request if needed
#     # ...

# def update_lives_in(request, pk):
#     if request.method == 'POST':
#         Lives_in = request.POST['Lives_in']
#         contact = Contact.objects.get(id=pk)
#         contact.lives_in = Lives_in
#         contact.save()
#         return redirect('showpage')

#     # Handle GET request if needed
#     # ...

# def update_last_studied_in(request, pk):
#     if request.method == 'POST':
#         Last_studied_in = request.POST['Last_studied_in']
#         contact = Contact.objects.get(id=pk)
#         contact.last_studied_in = Last_studied_in
#         contact.save()
#         return redirect('showpage')


# # Update Gender
# def update_gender(request, pk):
#     contact = get_object_or_404(Contact, pk=pk)
#     if request.method == 'POST':
#         contact.gender = request.POST.get('Gender')
#         contact.save()
#         return redirect('showpage')
#     # return render(request, 'update_gende.html', {'contact': contact})

# # Update Total Experience
# def update_total_experience(request, pk):
#     contact = get_object_or_404(Contact, pk=pk)
#     if request.method == 'POST':
#         contact.total_experience = request.POST.get('Total_experience')
#         contact.save()
#         return redirect('showpage')
#     # return render(request, 'update_total_experience.html', {'contact': contact})

# # Update Relationship Status
# def update_relationship_status(request, pk):
#     contact = get_object_or_404(Contact, pk=pk)
#     if request.method == 'POST':
#         contact.relationship_status = request.POST.get('Relationship_status')
#         contact.save()
#         return redirect('showpage')
#     # return render(request, 'update_relationship_status.html', {'contact': contact})

# # # Update Languages
# def update_languages(request, pk):
#     if request.method == 'POST':
#         Languages= request.POST['Languages']
#         contact = Contact.objects.get(id=pk)
#         contact.languages = Languages
#         contact.save()
#         return redirect('showpage')


# def update_birthday(request, pk):
#     contact = get_object_or_404(Contact, pk=pk)
#     if request.method == 'POST':
#         Birthday = request.POST.get('Birthday')
#         try:
#             # Parse the date in "DD/MM/YYYY" format
#             birthday_obj = datetime.strptime(Birthday, '%d/%m/%Y')
#             formatted_birthday = birthday_obj.strftime('%Y-%m-%d')
#             contact.birthday = formatted_birthday
#             contact.save()
#             return redirect('showpage')
#         except ValueError:
#             # Handle invalid date format
#             # You can add a validation message or take appropriate action here
#             pass

#     return render(request, 'app/edit_overview.html', {'contact': contact})    

# # Update Website
# def update_website(request, pk):
#     contact = get_object_or_404(Contact, pk=pk)
#     if request.method == 'POST':
#         contact.website = request.POST.get('Website')
#         contact.save()
#         return redirect('showpage')
#     # return render(request, 'update_website.html', {'contact': contact})

# # Update Religion
# def update_religion(request, pk):
#     contact = get_object_or_404(Contact, pk=pk)
#     if request.method == 'POST':
#         contact.religion = request.POST.get('Religion')
#         contact.save()
#         return redirect('showpage')
#     # return render(request, 'update_religion.html', {'contact': contact})


# #-------------------------------------------------------------------------------------------------


# # ----------------------------------- Experience Total OK -------------------------------------------------

# def experiencedata(request):
#  if request.method == 'POST':
    
#     #data come from html too view
#     Job_title = request.POST['Job_title']
#     Company_name = request.POST['Company_name']
#     Location = request.POST['Location']
#     Start_date = request.POST['Start_date']
#     End_date = request.POST['End_date']
#     Description = request.POST['Description']
#     # action=request.POST['action']
    
#     #creating objct of model class
    
#     newuser=Experience.objects.create(
#             # profile=profile,
#     job_title=Job_title,
#     company_name=Company_name,
#     location=Location,
#     ex_start_date=Start_date,
#     ex_end_date=End_date,
#     ex_des=Description
#     )
#     newuser.save()
    
#     #After insert render on show.html page
#     #return render(request,'app/show.html')
#     return redirect('experienceeditpage', pk=newuser.id)
#  else:
#         return render(request, 'app/insert.html') 






# def ex_update_job_title(request, pk):
#     contact = get_object_or_404(Experience, pk=pk)
#     if request.method == 'POST':
#         contact.job_title = request.POST.get('Job_title')
#         contact.save()
#         return redirect('experienceshowpage')
#     # return render(request, 'update_job_title.html', {'contact': contact})

# # Update Company Name
# def ex_update_company_name(request, pk):
#     contact = get_object_or_404(Experience, pk=pk)
#     if request.method == 'POST':
#         contact.company_name = request.POST.get('Company_name')
#         contact.save()
#         return redirect('experienceshowpage')
#     # return render(request, 'update_company_name.html', {'contact': contact})

# # Update Location
# def ex_update_location(request, pk):
#     contact = get_object_or_404(Experience, pk=pk)
#     if request.method == 'POST':
#         contact.location = request.POST.get('Location')
#         contact.save()
#         return redirect('experienceshowpage')
#     # return render(request, 'update_location.html', {'contact': contact})

# # Update Start Date (You can do the same for End Date, Description, etc.)
# def ex_update_start_date(request, pk):
#     contact = get_object_or_404(Experience, pk=pk)
#     if request.method == 'POST':
#         contact.ex_start_date = request.POST.get('Start_date')
#         contact.save()
#         return redirect('experienceshowpage')

# # Update End Date
# def ex_update_end_date(request, pk):
#     contact = get_object_or_404(Experience, pk=pk)
#     if request.method == 'POST':
#         contact.ex_end_date = request.POST.get('End_date')
#         contact.save()
#         return redirect('experienceshowpage')
#     # return render(request, 'update_end_date.html', {'contact': contact})

# # Update Description
# def ex_update_description(request, pk):
#     contact = get_object_or_404(Experience, pk=pk)
#     if request.method == 'POST':
#         contact.ex_des = request.POST.get('Description')
#         contact.save()
#         return redirect('experienceshowpage')
#     # return render(request, 'update_description.html', {'contact': contact})










# def experiencedisplaydata(request):
#     all_skills = Experience.objects.all()
#     return render(request, 'app/experiencepage.html', {'key1': all_skills}) 


# def experienceEditpage(request,pk):
#     #fetching the data of particular id
#     get_data=Experience.objects.get(id=pk)    #pk - primary key
#     return render(request,'app/edit_experience.html',{'key2':get_data})





# def experienceUpdatedata(request, pk):
#     # Retrieve the Experience object
#     udata = Experience.objects.get(id=pk)

#     # Get the values from the request.POST dictionary, handling missing fields
#     udata.job_title = request.POST.get('Job_title', udata.job_title)
#     udata.company_name = request.POST.get('Company_name', udata.company_name)
#     udata.location = request.POST.get('Location', udata.location)

#     # Parse and format the 'Start_date' and 'End_date' fields
#     start_date_str = request.POST.get('Start_date', '')
#     end_date_str = request.POST.get('End_date', '')

#     if start_date_str:
#         start_date_obj = datetime.strptime(start_date_str, '%Y-%m-%d')
#         udata.ex_start_date = start_date_obj

#     if end_date_str:
#         end_date_obj = datetime.strptime(end_date_str, '%Y-%m-%d')
#         udata.ex_end_date = end_date_obj

#     # Get the description field, using the existing value if not provided
#     udata.ex_des = request.POST.get('Description', udata.ex_des)

#     # Save the data
#     udata.save()
    
#     return redirect('experienceshowpage')




# def experienceDeletedata(request,pk):
#     ddata =Experience.objects.get(id=pk)
#     ddata.delete()
#     return redirect('experienceshowpage')
# #----------------------------------------------------------------------------------------------------

# # ----------------------------------skill NOT (none) OK----------------------------------------------------------





# def skilldata(request):
#     if request.method == 'POST':
#         Select_skills = request.POST.get('Select_skills')
#         Rating = request.POST.get('Rating')
        
#         new_skill = Skill.objects.create(skill=Select_skills, rating=Rating)
#         return redirect('skillseditpage',pk=new_skill.id)

#     return render(request, 'app/insert.html')



# def skills_update_select_skill(request, pk):
#     contact = get_object_or_404(Skill, pk=pk)
#     if request.method == 'POST':
#         contact.skill= request.POST.get('Select_skills')
#         contact.save()
#         return redirect('skillsshowpage')
#     # return render(request, 'update_end_date.html', {'contact': contact})

# # Update Description
# def skills_update_rating(request, pk):
#     contact = get_object_or_404(Skill, pk=pk)
#     if request.method == 'POST':
#         contact.rating = request.POST.get('Rating')
#         contact.save()
#         return redirect('skillsshowpage')






# def skilldisplaydata(request):
#     all_skills = Skill.objects.all()
#     return render(request, 'app/skillspage.html', {'key1': all_skills})

# # Edit page view
# def skillEditpage(request, pk):
#     get_skill = Skill.objects.get(id=pk)
#     return render(request, 'app/edit_skills.html', {'key2': get_skill})


# # def skillUpdatedata(request, pk):
# #     udata = Skill.objects.get(id=pk)
# #     udata.skill = request.POST.get('Select_skills')
# #     udata.rating = request.POST.get('Rating')
   
    
# #     udata.save()
# #     return redirect('skillsshowpage')


# @csrf_exempt
# def skillUpdatedata(request, pk):
#     if request.method == 'POST':
#         try:
#             with transaction.atomic():
#                 udata = Skill.objects.select_for_update().get(id=pk)
#                 if 'rating' in udata.__dict__:
#                     udata.rating =request.POST.get('Rating') 
#                 udata.save()
#                 return JsonResponse({"status": "success"})
#         except ObjectDoesNotExist:
#             return JsonResponse({"status": "error", "error": "User not found"})
#         # except IntegrityError:
#         #     return JsonResponse({"status": "error"})

# # Delete the data
# def skillDeletedata(request, pk):
#     ddata = Skill.objects.get(id=pk)
#     ddata.delete()
#     return redirect('skillsshowpage')




# # ------------------------------  Education NOt (none) OK -----------------------------------------------




# def educationdata(request):
#     if request.method == 'POST':
        
#         # Get the form data directly from request.POST
#         School_college = request.POST['School_college']
#         Degree = request.POST['Degree']
#         Field_of_study = request.POST['Field_of_study']
#         University_name = request.POST['University_name']
#         Start_date = request.POST['Start_date']
#         End_date = request.POST['End_date']
#         Description = request.POST['Description']
        
#         # Create a new education record for the profile
#         newuser=Education.objects.create(
#             # profile=profile,
#             school_college=School_college,
#             degree=Degree,
#             field_of_study=Field_of_study,
#             university_name=University_name,
#             edu_start_date=Start_date,
#             edu_end_date=End_date,
#             edu_des=Description
#         )
#         return redirect('educationeditpage',pk=newuser.id)

#     return render(request, 'app/insert.html')

# def educationdisplaydata(request):
#     all_skills = Education.objects.all()
#     return render(request, 'app/educationpage.html', {'key1': all_skills})

# # Edit page view
# def educationEditpage(request, pk):
#     get_skill = Education.objects.get(id=pk)
#     return render(request, 'app/edit_education.html', {'key2': get_skill})




# def edu_update_school_college(request, pk):
#     education_data = get_object_or_404(Education, pk=pk)

#     if request.method == 'POST':
#         education_data.school_college = request.POST.get('School_college')
#         education_data.save()

#     return redirect('educationshowpage')  # You can redirect to the detail page or wherever you want

# # Update degree
# def edu_update_degree(request, pk):
#     education_data = get_object_or_404(Education, pk=pk)

#     if request.method == 'POST':
#         education_data.degree = request.POST.get('Degree')
#         education_data.save()

#     return redirect('educationshowpage')



# # Update field of study
# def edu_update_field_of_study(request, pk):
#     education_data = get_object_or_404(Education, pk=pk)

#     if request.method == 'POST':
#         education_data.field_of_study = request.POST.get('Field_of_study')
#         education_data.save()

#     return redirect('educationshowpage')  # You can redirect to the detail page or wherever you want

# # Update university name
# def edu_update_university_name(request, pk):
#     education_data = get_object_or_404(Education, pk=pk)

#     if request.method == 'POST':
#         education_data.university_name = request.POST.get('University_name')
#         education_data.save()

#     return redirect('educationshowpage')

# # Update education start date
# def edu_update_start_date(request, pk):
#     education_data = get_object_or_404(Education, pk=pk)

#     if request.method == 'POST':
#         start_date_str = request.POST.get('Start_date')
#         if start_date_str:
#             start_date_obj = datetime.strptime(start_date_str, '%Y-%m-%d')
#             education_data.edu_start_date = start_date_obj
#             education_data.save()

#     return redirect('educationshowpage')

# # Update education end date
# def edu_update_end_date(request, pk):
#     education_data = get_object_or_404(Education, pk=pk)

#     if request.method == 'POST':
#         end_date_str = request.POST.get('End_date')
#         if end_date_str:
#             end_date_obj = datetime.strptime(end_date_str, '%Y-%m-%d')
#             education_data.edu_end_date = end_date_obj
#             education_data.save()

#     return redirect('educationshowpage')

# # Update education description
# def edu_update_des(request, pk):
#     education_data = get_object_or_404(Education, pk=pk)

#     if request.method == 'POST':
#         education_data.edu_des = request.POST.get('Description')
#         education_data.save()

#     return redirect('educationshowpage')






# def educationUpdatedata(request, pk):
#     udata = Education.objects.get(id=pk)
#     udata.school_college = request.POST.get('School_college')
#     udata.degree = request.POST.get('Degree')
#     udata.field_of_study = request.POST.get('Field_of_study')
#     udata.university_name = request.POST.get('University_name')

#     # Parse and format the 'Start_date' and 'End_date' fields
#     start_date_str = request.POST.get('Start_date', '')
#     end_date_str = request.POST.get('End_date', '')

#     if start_date_str:
#         start_date_obj = datetime.strptime(start_date_str, '%Y-%m-%d')
#         udata.edu_start_date = start_date_obj

#     if end_date_str:
#         end_date_obj = datetime.strptime(end_date_str, '%Y-%m-%d')
#         udata.edu_end_date = end_date_obj

#     udata.edu_des = request.POST.get('Description')

#     udata.save()
#     return redirect('educationshowpage')













# # Delete the data
# def educationDeletedata(request, pk):
#     ddata = Education.objects.get(id=pk)
#     ddata.delete()
#     return redirect('educationshowpage')






# # ----------------------------- Achivement NOT (none)  OK-----------------------------------




# def achivementdata(request):
#     if request.method == 'POST':
        
#         # Get the form data directly from request.POST
#         Title = request.POST['Title']
#         Start_date = request.POST['Start_date']
#         End_date= request.POST['End_date']
       
#         Description = request.POST['Description']
#         Image = request.FILES.get('Image')
#         # Create a new education record for the profile
#         newuser=Achievement.objects.create(
#             # profile=profile,
#             ach_title =Title,
            
#             start_date=Start_date,
#             end_date=End_date,
#             ach_des=Description,
#             image=Image
#         )
#         return redirect('achivementeditpage',pk=newuser.id)

#     return render(request, 'app/insert.html')

# def achivementdisplaydata(request):
#     all_skills = Achievement.objects.all()
#     return render(request, 'app/achievementspage.html', {'key1': all_skills})
#     # return render(request, 'app/skillspage.html', {'key1': all_skills})

# # Edit page view
# def achivementEditpage(request, pk):
#     get_skill = Achievement.objects.get(id=pk)
#     return render(request, 'app/edit_achivement.html', {'key2': get_skill})


# # Update Title view


# def ach_update_title(request, pk):
#     achievement = get_object_or_404(Achievement, pk=pk)
#     if request.method == 'POST':
#         Title = request.POST.get('Title')
#         achievement.ach_title = Title
#         achievement.save()
#         return JsonResponse({'success': True})
#     return JsonResponse({'success': False})







# # def ach_update_start_date(request, pk):
# #     ach_data = get_object_or_404(Achievement, pk=pk)

# #     if request.method == 'POST':
# #         start_date_str = request.POST.get('Start_date')
# #         if start_date_str:
# #             start_date_obj = datetime.strptime(start_date_str, '%Y-%m-%d')
# #             ach_data.start_date = start_date_obj
# #             ach_data.save()

# #     return redirect('achivementshowpage')



# def ach_update_start_date(request, pk):
#     achievement = get_object_or_404(Achievement, pk=pk)
#     if request.method == 'POST':
#         start_date = request.POST.get('Start_date')
#         achievement.start_date = start_date
#         achievement.save()
#         return JsonResponse({'success': True})
#     return JsonResponse({'success': False})


# # # Update education end date
# # def ach_update_end_date(request, pk):
# #     ach_data = get_object_or_404(Achievement, pk=pk)

# #     if request.method == 'POST':
# #         end_date_str = request.POST.get('End_date')
# #         if end_date_str:
# #             end_date_obj = datetime.strptime(end_date_str, '%Y-%m-%d')
# #             ach_data.end_date = end_date_obj
# #             ach_data.save()

# #     return redirect('achivementshowpage')


# def ach_update_end_date(request, pk):
#     achievement = get_object_or_404(Achievement, pk=pk)
#     if request.method == 'POST':
#         End_date = request.POST.get('End_date')
#         achievement.end_date = End_date
#         achievement.save()
#         return JsonResponse({'success': True})
#     return JsonResponse({'success': False})





# def ach_update_des(request, pk):
#     achievement = get_object_or_404(Achievement, pk=pk)
#     if request.method == 'POST':
#         Description = request.POST.get('Description')
#         achievement.ach_des = Description
#         achievement.save()
#         return JsonResponse({'success': True})
#     return JsonResponse({'success': False})





# # def ach_update_image(request, pk):
# #     achievement = get_object_or_404(Achievement, pk=pk)
    
# #     if request.method == 'POST':
# #         # Clear the previous image, if any, before saving the new one
# #         if achievement.image:
# #             achievement.image.delete()
        
# #         # Save the new image
# #         achievement.image = request.FILES['Image']
# #         achievement.save()
        
# #         return JsonResponse({'success': True})
    

# def ach_update_image(request, pk):
#     achievement = get_object_or_404(Achievement, pk=pk)
    
#     if request.method == 'POST':
#         # Clear the previous image, if any, before saving the new one
#         if achievement.image:
#             achievement.image.delete()
        
#         # Save the new image
#         image = request.FILES.get('Image')
#         if image:
#             achievement.image = image
        
#         achievement.save()
#         return JsonResponse({'success': True})
    
#     # If the request method is not POST, you should return a GET request response.
#     #return render(request, 'achievement_update_image.html')


# # def achivementUpdatedata(request, pk):
# #     udata = Achievement.objects.get(id=pk)
# #     udata.ach_title = request.POST.get('Title')
# #     udata.start_date = request.POST.get('Start_date')
# #     udata.end_date = request.POST.get('End_date')
# #     udata.ach_des = request.POST.get('Description')

# #     # Handle the uploaded image
# #     image = request.FILES.get('Image')
# #     if image:
# #         udata.image.save(image.name, image)

# #     udata.save()
# #     return redirect('achivementshowpage')

# # def achivementUpdatedata(request, pk):
# #     udata = get_object_or_404(Achievement, id=pk)

# #     if request.method == 'POST':
# #         udata.ach_title = request.POST.get('Title')
# #         udata.start_date = request.POST.get('Start_date')
# #         udata.end_date = request.POST.get('End_date')
# #         udata.ach_des = request.POST.get('Description')

# #         # Handle the uploaded image
# #         image = request.FILES.get('Image')
# #         if image:
# #             udata.image = image

# #         udata.save()
# #         return redirect('achivementshowpage')
# #     else:
# #         return render(request, 'edit.html', {'achievement': udata})

# def achivementUpdatedata(request, pk):
#     udata = get_object_or_404(Achievement, pk=pk)

#     if request.method == 'POST':
#         udata.ach_title = request.POST.get('Title')
#         udata.start_date = request.POST.get('Start_date')
#         udata.end_date = request.POST.get('End_date')
#         udata.ach_des = request.POST.get('Description')

#         # Handle the uploaded image
#         image = request.FILES.get('Image')
#         if image:
#             udata.image = image

#         udata.save()
#         return redirect('achivementshowpage')
#     else:
#         return render(request, 'edit_achivement.html', {'achievement': udata})

# # ...




# # ...
# # Delete the data
# # def achivementDeletedata(request, pk):
# #     ddata = Achievement.objects.get(id=pk)
# #     ddata.delete()
# #     return redirect('achivementshowpage')  # Corrected the URL name
# def achivementDeletedata(request, pk):
#     ddata = get_object_or_404(Achievement, pk=pk)
#     ddata.delete()
#     return redirect('achivementshowpage')


# #--------------------------------about Total OK-------------------------------------------------------


# # def aboutdata(request):
# #  if request.method == 'POST':
    
# #     #data come from html too view
# #     Title= request.POST['Title']
# #     Description = request.POST['Description']
    
# #     # action=request.POST['action']
    
# #     #creating objct of model class
    
# #     newusers = About.objects.create(
# #            about_title=Title,
# #            about_des=Description 
            
# #         )
# #     newusers.save()
    
# #     #After insert render on show.html page
# #     #return render(request,'app/show.html')
# #     return redirect('abouteditpage',pk=newusers.id)
# #  else:
# #         return render(request, 'app/insert.html')

# def aboutdata(request):
#     title_error = None
#     description_error = None

#     if request.method == 'POST':
#         Title = request.POST['Title']
#         Description = request.POST['Description']

#         if not Title:
#             title_error = 'Title is required'

#         if not Description:
#             description_error = 'Description is required'

#         if Title and Description:
#             newusers = About.objects.create(about_title=Title, about_des=Description)
#             newusers.save()
#             return redirect('abouteditpage', pk=newusers.id)

#     return render(request, 'app/insert.html', {
#         'title_error': title_error,
#         'description_error': description_error
#     })
 
# # Update Title view
# def update_title(request, pk):
#     if request.method == 'POST':
#         Title = request.POST['Title']
#         udata = About.objects.get(id=pk)
#         udata.about_title = Title
#         udata.save()
#     return redirect('aboutshowpage')

# # Update Description view
# def update_description(request, pk):
#     if request.method == 'POST':
#         Description = request.POST['Description']
#         udata = About.objects.get(id=pk)
#         udata.about_des = Description
#         udata.save()
#     return redirect('aboutshowpage')

# # Add more views for other fields if needed



# def aboutdisplaydata(request):
#     #select  * from tablename
#     all_data= About.objects.all()
#     return render(request,'app/aboutpage.html',{'key1':all_data})  #key1


# #Edit page view
# def aboutEditpage(request,pk):
#     #fetching the data of particular id
#     get_data=About.objects.get(id=pk)    #pk - primary key
#     return render(request,'app/edit_about.html',{'key2':get_data})


# #update data view

# #don't delete

# # def update_visibility(request, pk):
# #     if request.method == 'POST':
# #         title_visibility = request.POST.get('titleVisibility')
# #         description_visibility = request.POST.get('descriptionVisibility')
        
# #         about_data = About.objects.get(id=pk)
# #         about_data.title_visibility = title_visibility
# #         about_data.description_visibility = description_visibility
# #         about_data.save()
        
# #         return redirect('aboutshowpage')
# #     else:
# #         return redirect('aboutshowpage')

# def aboutUpdatedata(request,pk):
#     udata=About.objects.get(id=pk)
#     udata.about_title = request.POST['Title']
#     udata.about_des = request.POST['Description']
   
#     #udata the data use save()
#     udata.save()
#     return redirect('aboutshowpage')


    
# #delete the
# # def aboutDeletedata(request,pk):
# #     ddata =About.objects.get(id=pk)
# #     ddata.delete()
# #     return redirect('aboutshowpage')

# def aboutDeletedata(request, pk):
#     try:
#         ddata = About.objects.get(id=pk)
#         ddata.delete()
#     except About.DoesNotExist:
#         pass
#     return redirect('aboutshowpage')



# # def save_radio_data(request, pk):
# #     if request.method == 'POST':
# #         title_visibility = request.POST.get('titleVisibility')
# #         description_visibility = request.POST.get('descriptionVisibility')
        
# #         # Assuming you have a model to save this data
# #         about_data = About.objects.get(id=pk)
# #         about_data.title_visibility = title_visibility
# #         about_data.description_visibility = description_visibility
# #         about_data.save()
        
# #         return HttpResponse('Data saved successfully')
# #     else:
# #         return HttpResponse('Invalid request method')


# # -----------------------------Workportfolio NOT ((none)OK------------------------------------------------




# def workportfoliodata(request):
#     if request.method == 'POST':
        
#         # Get the form data directly from request.POST
#         Title = request.POST['Title']
       
       
#         Description = request.POST['Description']
#         Link = request.POST['Link']
#         # Create a new education record for the profile
#         newuser=WorkPortfolio.objects.create(
#                 # profile=profile,
#                 work_title=Title,
#                 work_des=Description,
#                 link=Link
#             )
#         return redirect('workportfolioeditpage',pk=newuser.id)

#     return render(request, 'app/insert.html')


# # Update Title view for Work Portfolio
# def work_update_title(request, pk):
#     if request.method == 'POST':
#         Title = request.POST['Title']
#         work_item = WorkPortfolio.objects.get(id=pk)
#         work_item.work_title = Title
#         work_item.save()
#     return redirect('workportfolioshowpage')  # Redirect to the appropriate page

# # Update Description view for Work Portfolio
# def work_update_description(request, pk):
#     if request.method == 'POST':
#         Description = request.POST['Description']
#         work_item = WorkPortfolio.objects.get(id=pk)
#         work_item.work_des = Description
#         work_item.save()
#     return redirect('workportfolioshowpage')  # Redirect to the appropriate page

# # Update Link view for Work Portfolio
# def work_update_link(request, pk):
#     if request.method == 'POST':
#         Link = request.POST['Link']
#         work_item = WorkPortfolio.objects.get(id=pk)
#         work_item.link = Link
#         work_item.save()
#     return redirect('workportfolioshowpage')  # Redirect to the appropriate page


# def workportfoliodisplaydata(request):
#     #select  * from tablename
#     all_data= WorkPortfolio.objects.all()
#     return render(request,'app/workportfolio.html',{'key1':all_data})  #key1



# def workportfolioEditpage(request,pk):
#     #fetching the data of particular id
#     get_data=WorkPortfolio.objects.get(id=pk)    #pk - primary key
#     return render(request,'app/edit_workportfolio.html',{'key2':get_data})


# def workportfolioUpdatedata(request,pk):
#     udata=WorkPortfolio.objects.get(id=pk)
#     udata.work_title = request.POST.get('Title')
#     udata.work_des = request.POST.get('Description')
#     udata.link = request.POST.get('Link')
#     #udata the data use save()
#     udata.save()
#     return redirect('workportfolioshowpage')



# # Update Work Portfolio
# # def workportfolioUpdatedata(request, pk):
# #     if request.method == 'POST':
# #         # Get the WorkPortfolio instance by its primary key (pk)
# #         udata = WorkPortfolio.objects.get(id=pk)

# #         # Update the fields based on the form input
# #         udata.work_title = request.POST.get('Title')
# #         udata.work_des = request.POST.get('Description')
# #         udata.link = request.POST.get('Link')

# #         # Save the updated WorkPortfolio instance
# #         udata.save()

# #         return redirect('workportfolioshowpage')
    
#     # return render(request, 'app/edit.html', {'key2': udata})



# def workportfolioDeletedata(request,pk):
#     ddata =WorkPortfolio.objects.get(id=pk)
#     ddata.delete()
#     return redirect('workportfolioshowpage')




# #--------------------------------------Place lived Total OK  -----------------------------

# def placesdata(request):
#  if request.method == 'POST':
    
#     #data come from html too view
#     Place = request.POST['Place']
#     Start_date = request.POST['Start_date']
#     End_date = request.POST['End_date']
#     # Currently_living_in = request.POST.get('Currently_living_in') == 'on'
#     # action=request.POST['action']
    
#     #creating objct of model class
    
#     newuser=PlaceLived.objects.create(place=Place,place_start_date=Start_date,
#                                          place_end_date=End_date)#,currently_living_in=Currently_living_in
       
#     newuser.save()
    
#     #After insert render on show.html page
#     #return render(request,'app/show.html')
#     return redirect('placeseditpage',pk=newuser.id)
#  else:
#         return render(request, 'app/insert.html')
 

# def place_update_name(request, pk):
#     place_data = get_object_or_404(PlaceLived, pk=pk)

#     if request.method == 'POST':
#         place_data.place = request.POST.get('Place')
#         place_data.save()

#     return redirect('placesshowpage')

# # Update Place Lived in start date
# def place_update_start_date(request, pk):
#     place_data = get_object_or_404(PlaceLived, pk=pk)

#     if request.method == 'POST':
#         start_date_str = request.POST.get('Start_date')
#         if start_date_str:
#             start_date_obj = datetime.strptime(start_date_str, '%Y-%m-%d')
#             place_data.place_start_date = start_date_obj
#             place_data.save()

#     return redirect('placesshowpage')

# # Update Place Lived in end date
# def place_update_end_date(request, pk):
#     place_data = get_object_or_404(PlaceLived, pk=pk)

#     if request.method == 'POST':
#         end_date_str = request.POST.get('End_date')
#         if end_date_str:
#             end_date_obj = datetime.strptime(end_date_str, '%Y-%m-%d')
#             place_data.place_end_date = end_date_obj
#             place_data.save()

#     return redirect('placesshowpage')


# def placesdisplaydata(request):
#     #select  * from tablename
#     all_data= PlaceLived.objects.all()
#     return render(request,'app/livingpage.html',{'key1':all_data}) 
 

# def placesEditpage(request,pk):
#     #fetching the data of particular id
#     get_data=PlaceLived.objects.get(id=pk)    #pk - primary key
#     return render(request,'app/edit_place.html',{'key2':get_data})


# # def placesUpdatedata(request, pk):
# #     udata = PlaceLived.objects.get(id=pk)
    
# #     if request.method == 'POST':
# #         # Update the place, start_date, and end_date fields
# #         udata.place = request.POST.get('Place', '')

# #         # Check if the Start_date is provided and in the correct format
# #         place_start_date = request.POST.get('Start_date', '')
# #         if place_start_date:
# #             try:
# #                 udata.place_start_date = datetime.strptime(place_start_date, "%Y-%m-%d").date()
# #             except ValueError:
# #                 # Handle the error or invalid date format
# #                 pass

# #         # Check if the End_date is provided and in the correct format
# #         place_end_date = request.POST.get('End_date', '')
# #         if place_end_date:
            
# #             try:
# #                 udata.place_end_date = datetime.strptime(place_end_date, "%Y-%m-%d").date()
# #             except ValueError:
# #                 # Handle the error or invalid date format
# #                 pass

# #         # # Update the currently_living_in field if provided
# #         # currently_living_in = request.POST.get('Currently_living_in', '')
# #         # if currently_living_in.lower() == 'true':
# #         #     udata.currently_living_in = True
# #         # elif currently_living_in.lower() == 'false':
# #         #     udata.currently_living_in = False

# #         # Save the data
# #         udata.save()

# #         return redirect('placesshowpage')

# def placesUpdatedata(request, pk):
#     try:
#         # Attempt to retrieve the PlaceLived object with the specified 'pk' (primary key)
#         place = get_object_or_404(PlaceLived, id=pk)
#     except PlaceLived.DoesNotExist:
#         # Handle the case where the object does not exist
#         raise Http404("PlaceLived object does not exist")  # You can customize this error message

#     # Rest of your view logic here
#     # You can render a template, perform updates, or return an HTTP response

#     return redirect('placesshowpage')









# def placesDeletedata(request,pk):
#     ddata =PlaceLived.objects.get(id=pk)
#     ddata.delete()
#     return redirect('placesshowpage')



# # ---------------------- -----------Relationship OK----------------------------------------


# def relationshipdata(request):
#  if request.method == 'POST':
    
#     #data come from html too view
#     Name = request.POST['Name']
    
#     Relationship_type = request.POST['Relationship_type']

#     newuser=Relationship.objects.create(name=Name,relationship_type=Relationship_type)
#     # action=request.POST['action']
    
#     #creating objct of model class
    
    
#     newuser.save()
    
#     #After insert render on show.html page
#     #return render(request,'app/show.html')
#     return redirect('relationshipeditpage',pk=newuser.id)
#  else:
#         return render(request, 'app/insert.html')
 

# # def person_update_name(request, pk):
# #     person_data = get_object_or_404(PlaceLived, pk=pk)

# #     if request.method == 'POST':
# #         person_data.name  = request.POST.get('Name')
# #         person_data.save()

# #     return redirect('relationshipshowpage')

# # def person_update_relationships(request, pk):
# #     person_data = get_object_or_404(PlaceLived, pk=pk)

# #     if request.method == 'POST':
# #         person_data.relationship_type  = request.POST.get('Relationship_type')
# #         person_data.save()

# #     return redirect('relationshipshowpage')
# def person_update_name(request, pk):
#     person = get_object_or_404(Relationship, pk=pk)
#     if request.method == 'POST':
#         Name = request.POST.get('Name')
#         person.name = Name
#         person.save()
#     return redirect('relationshipshowpage')
#     #     return JsonResponse({'success': True})
#     # return JsonResponse({'success': False})

# # Update person's relationships view
# def person_update_relationships(request, pk):
#     person = get_object_or_404(Relationship, pk=pk)
#     if request.method == 'POST':
#         Relationship_type = request.POST.get('Relationship_type')
#         person.relationship_type = Relationship_type
#         person.save()
#     return redirect('relationshipshowpage')
#     #     return JsonResponse({'success': True})
#     # return JsonResponse({'success': False})

 
# def relationshipdisplaydata(request):
#     #select  * from tablename
#     all_data= Relationship.objects.all()
#     return render(request,'app/relationshippage.html',{'key1':all_data})  #key1



# def relationshipEditpage (request,pk):
#     #fetching the data of particular id
#     get_data=Relationship.objects.get(id=pk)    #pk - primary key
#     return render(request,'app/edit_relationship.html',{'key2':get_data})



# def relationshipUpdatedata(request,pk):
#     udata=Relationship.objects.get(id=pk)
#     udata.name = request.POST['Name']
#     udata.relationship_type= request.POST.get('Relationship_type')
    
#     #udata the data use save()
#     udata.save()
#     return redirect('relationshipshowpage')



# def relationshipDeletedata(request,pk):
#     ddata =Relationship.objects.get(id=pk)
#     ddata.delete()
#     return redirect('relationshipshowpage')

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.utils.dateparse import parse_date
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from datetime import datetime
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact,Experience,Skill,Education,Achievement,About,WorkPortfolio,PlaceLived,Relationship
from .forms import ContactForm,RelationshipForm,AchievementForm,AboutForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def Insertview(request):  #index html view
    return render(request,'app/insert.html')

# ---------------------------------------Contact Total OK---------------------------

def Insertdata(request):
 if request.method == 'POST':
    
    #data come from html too view
    Contact_number = request.POST['Contact_number']
    Email = request.POST['Email']
    Lives_in= request.POST['Lives_in']
    Last_studied_in = request.POST['Last_studied_in']
    Gender = request.POST['Gender']
    Total_experience = request.POST['Total_experience']
    Relationship_status= request.POST['Relationship_status']
    Languages = request.POST['Languages']
    Birthday= request.POST['Birthday']
    Website= request.POST['Website']
    Religion= request.POST['Religion']
    # action=request.POST['action']
    
    #creating objct of model class
    
    newusers = Contact.objects.create(
            contact_number =Contact_number,
            email =Email,
            lives_in=Lives_in,
            last_studied_in =Last_studied_in,
            gender=Gender,
            total_experience=Total_experience,
            relationship_status =Relationship_status,
            languages =Languages,
            birthday =Birthday,
            website =Website,
            religion =Religion
        )
    newusers.save()
    
    #After insert render on show.html page
    #return render(request,'app/show.html')
    return redirect('editpage', pk=newusers.id)
 else:
        return render(request, 'app/insert.html')
 



def displaydata(request):
    #select  * from tablename
    all_data= Contact.objects.all()
    return render(request,'app/show_profile_form.html',{'key1':all_data})  #key1


#Edit page view
def Editpage(request,pk):
    #fetching the data of particular id
    get_data=Contact.objects.get(id=pk)    #pk - primary key
    # return render(request,'app/edit.html',{'key2':get_data})

    return render(request,'app/edit_overview.html',{'key2':get_data})








def Updatedata(request, pk):
    udata = Contact.objects.get(id=pk)

    # Update fields only if they are provided in the POST data
    udata.contact_number = request.POST.get('Contact_number', udata.contact_number)
    udata.email = request.POST.get('Email', udata.email)
    udata.lives_in = request.POST.get('Lives_in', udata.lives_in)
    udata.last_studied_in = request.POST.get('Last_studied_in', udata.last_studied_in)
    udata.gender = request.POST.get('Gender', udata.gender)
    udata.total_experience = request.POST.get('Total_experience', udata.total_experience)
    udata.relationship_status = request.POST.get('Relationship_status', udata.relationship_status)
    udata.languages = request.POST.get('Languages', udata.languages)

    # Handle the date format for 'Birthday' if it's not empty
    birthday_str = request.POST.get('Birthday', '')
    if birthday_str:
        try:
            # Parse the date in "DD/MM/YYYY" format
            birthday_obj = datetime.strptime(birthday_str, '%d/%m/%Y')
            formatted_birthday = birthday_obj.strftime('%Y-%m-%d')
            udata.birthday = formatted_birthday
        except ValueError:
            # Handle invalid date format
            # You can add a validation message or take appropriate action here
            pass

    udata.website = request.POST.get('Website', udata.website)
    udata.religion = request.POST.get('Religion', udata.religion)
    
    # Save the data
    udata.save()
    
    return redirect('showpage')

#delete the
def Deletedata(request,pk):
    ddata =Contact.objects.get(id=pk)
    ddata.delete()
    return redirect('showpage')


def update_contact_number(request, pk):
    if request.method == 'POST':
        Contact_number = request.POST['Contact_number']
        contact = Contact.objects.get(id=pk)
        contact.contact_number = Contact_number
        contact.save()
        return redirect('showpage')

    # Handle GET request if needed
    # ...

def update_email(request, pk):
    if request.method == 'POST':
        Email = request.POST['Email']
        contact = Contact.objects.get(id=pk)
        contact.email = Email
        contact.save()
        return redirect('showpage')

    # Handle GET request if needed
    # ...

def update_lives_in(request, pk):
    if request.method == 'POST':
        Lives_in = request.POST['Lives_in']
        contact = Contact.objects.get(id=pk)
        contact.lives_in = Lives_in
        contact.save()
        return redirect('showpage')

    # Handle GET request if needed
    # ...

def update_last_studied_in(request, pk):
    if request.method == 'POST':
        Last_studied_in = request.POST['Last_studied_in']
        contact = Contact.objects.get(id=pk)
        contact.last_studied_in = Last_studied_in
        contact.save()
        return redirect('showpage')


# Update Gender
def update_gender(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.gender = request.POST.get('Gender')
        contact.save()
        return redirect('showpage')
    # return render(request, 'update_gende.html', {'contact': contact})

# Update Total Experience
def update_total_experience(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.total_experience = request.POST.get('Total_experience')
        contact.save()
        return redirect('showpage')
    # return render(request, 'update_total_experience.html', {'contact': contact})

# Update Relationship Status
def update_relationship_status(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.relationship_status = request.POST.get('Relationship_status')
        contact.save()
        return redirect('showpage')
    # return render(request, 'update_relationship_status.html', {'contact': contact})

# # Update Languages
def update_languages(request, pk):
    if request.method == 'POST':
        Languages= request.POST['Languages']
        contact = Contact.objects.get(id=pk)
        contact.languages = Languages
        contact.save()
        return redirect('showpage')


def update_birthday(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        Birthday = request.POST.get('Birthday')
        try:
            # Parse the date in "DD/MM/YYYY" format
            birthday_obj = datetime.strptime(Birthday, '%d/%m/%Y')
            formatted_birthday = birthday_obj.strftime('%Y-%m-%d')
            contact.birthday = formatted_birthday
            contact.save()
            return redirect('showpage')
        except ValueError:
            # Handle invalid date format
            # You can add a validation message or take appropriate action here
            pass

    return render(request, 'app/edit_overview.html', {'contact': contact})    

# Update Website
def update_website(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.website = request.POST.get('Website')
        contact.save()
        return redirect('showpage')
    # return render(request, 'update_website.html', {'contact': contact})

# Update Religion
def update_religion(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.religion = request.POST.get('Religion')
        contact.save()
        return redirect('showpage')
    # return render(request, 'update_religion.html', {'contact': contact})

    
def overview_contact_update_visibility(request, pk):
    if request.method == 'POST':
        overview_contact_visibility  = request.POST.get('overview_contactVisibility')
        # description_visibility = request.POST.get('descriptionVisibility')
        about_data = Contact.objects.get(id=pk)

        about_data.overview_contact_visibility  = overview_contact_visibility  
        # about_data.description_visibility = description_visibility
        about_data.save()
    return render(request,'app/edit_overview.html',{'key2':about_data})
    # return redirect('showpage')

#-------------------------------------------------------------------------------------------------


# ----------------------------------- Experience Total OK -------------------------------------------------

def experiencedata(request):
 if request.method == 'POST':
    
    #data come from html too view
    Job_title = request.POST['Job_title']
    Company_name = request.POST['Company_name']
    Location = request.POST['Location']
    Start_date = request.POST['Start_date']
    End_date = request.POST['End_date']
    Description = request.POST['Description']
    # action=request.POST['action']
    
    #creating objct of model class
    
    newuser=Experience.objects.create(
            # profile=profile,
    job_title=Job_title,
    company_name=Company_name,
    location=Location,
    ex_start_date=Start_date,
    ex_end_date=End_date,
    ex_des=Description
    )
    newuser.save()
    
    #After insert render on show.html page
    #return render(request,'app/show.html')
    return redirect('experienceeditpage', pk=newuser.id)
 else:
        return render(request, 'app/insert.html') 






def ex_update_job_title(request, pk):
    contact = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        contact.job_title = request.POST.get('Job_title')
        contact.save()
        return redirect('experienceshowpage')
    # return render(request, 'update_job_title.html', {'contact': contact})

# Update Company Name
def ex_update_company_name(request, pk):
    contact = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        contact.company_name = request.POST.get('Company_name')
        contact.save()
        return redirect('experienceshowpage')
    # return render(request, 'update_company_name.html', {'contact': contact})

# Update Location
def ex_update_location(request, pk):
    contact = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        contact.location = request.POST.get('Location')
        contact.save()
        return redirect('experienceshowpage')
    # return render(request, 'update_location.html', {'contact': contact})

# Update Start Date (You can do the same for End Date, Description, etc.)
def ex_update_start_date(request, pk):
    contact = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        contact.ex_start_date = request.POST.get('Start_date')
        contact.save()
        return redirect('experienceshowpage')

# Update End Date
def ex_update_end_date(request, pk):
    contact = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        contact.ex_end_date = request.POST.get('End_date')
        contact.save()
        return redirect('experienceshowpage')
    # return render(request, 'update_end_date.html', {'contact': contact})

# Update Description
def ex_update_description(request, pk):
    contact = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        contact.ex_des = request.POST.get('Description')
        contact.save()
        return redirect('experienceshowpage')
    # return render(request, 'update_description.html', {'contact': contact})










def experiencedisplaydata(request):
    all_skills = Experience.objects.all()
    return render(request, 'app/experiencepage.html', {'key1': all_skills}) 


def experienceEditpage(request,pk):
    #fetching the data of particular id
    get_data=Experience.objects.get(id=pk)    #pk - primary key
    return render(request,'app/edit_experience.html',{'key2':get_data})





def experienceUpdatedata(request, pk):
    # Retrieve the Experience object
    udata = Experience.objects.get(id=pk)

    # Get the values from the request.POST dictionary, handling missing fields
    udata.job_title = request.POST.get('Job_title', udata.job_title)
    udata.company_name = request.POST.get('Company_name', udata.company_name)
    udata.location = request.POST.get('Location', udata.location)

    # Parse and format the 'Start_date' and 'End_date' fields
    start_date_str = request.POST.get('Start_date', '')
    end_date_str = request.POST.get('End_date', '')

    if start_date_str:
        start_date_obj = datetime.strptime(start_date_str, '%Y-%m-%d')
        udata.ex_start_date = start_date_obj

    if end_date_str:
        end_date_obj = datetime.strptime(end_date_str, '%Y-%m-%d')
        udata.ex_end_date = end_date_obj

    # Get the description field, using the existing value if not provided
    udata.ex_des = request.POST.get('Description', udata.ex_des)

    # Save the data
    udata.save()
    
    return redirect('experienceshowpage')




def experienceDeletedata(request,pk):
    ddata =Experience.objects.get(id=pk)
    ddata.delete()
    return redirect('experienceshowpage')



def ex_jobtitle_update_visibility(request, pk):
    if request.method == 'POST':
        ex_jobtitle_visibility = request.POST.get('ex_jobtitleVisibility')
        # description_visibility = request.POST.get('descriptionVisibility')
        about_data = Experience.objects.get(id=pk)

        about_data.ex_jobtitle_visibility = ex_jobtitle_visibility 
        # about_data.description_visibility = description_visibility
        about_data.save()
    return render(request,'app/edit_experience.html',{'key2':about_data})
    # return redirect('experienceshowpage')
#----------------------------------------------------------------------------------------------------

# ----------------------------------skill total OK----------------------------------------------------------





def skilldata(request):
    if request.method == 'POST':
        Select_skills = request.POST.get('Select_skills')
        Rating = request.POST.get('Rating')
        
        new_skill = Skill.objects.create(skill=Select_skills, rating=Rating)
        return redirect('skillseditpage',pk=new_skill.id)

    return render(request, 'app/insert.html')



def skills_update_select_skill(request, pk):
    contact = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        contact.skill= request.POST.get('Select_skills')
        contact.save()
        return redirect('skillsshowpage')
    # return render(request, 'update_end_date.html', {'contact': contact})



def skills_update_rating(request, pk):
    udata = Skill.objects.get(id=pk)
    udata.skill = request.POST.get('Select_skills')

    # Check if 'Rating' is present in the request data
    if 'Rating' in request.POST:
        udata.rating = request.POST['Rating']

    udata.save()
    
    return redirect('skillsshowpage')


def skilldisplaydata(request):
    all_skills = Skill.objects.all()
    return render(request, 'app/skillspage.html', {'key1': all_skills})

# Edit page view
def skillEditpage(request, pk):
    get_skill = Skill.objects.get(id=pk)
    return render(request, 'app/edit_skills.html', {'key2': get_skill})



def skillUpdatedata(request, pk):
    udata = Skill.objects.get(id=pk)
    udata.skill = request.POST.get('Select_skills')
    
    # Do not update 'rating' in the database
    # Check if 'Rating' is present in the request data
    if 'Rating' in request.POST:
        udata.rating = request.POST['Rating']
    
    udata.save()
    return redirect('skillsshowpage')

# Delete the data
def skillDeletedata(request, pk):
    ddata = Skill.objects.get(id=pk)
    ddata.delete()
    return redirect('skillsshowpage')


def skills_name_update_visibility(request, pk):
    if request.method == 'POST':
        skills_name_visibility  = request.POST.get('skills_name_Visibility')
        # description_visibility = request.POST.get('descriptionVisibility')
        about_data =Skill.objects.get(id=pk)

        about_data.skills_name_visibility= skills_name_visibility  
        # about_data.description_visibility = description_visibility
        about_data.save()
    return render(request,'app/edit_skills.html',{'key2':about_data})
    # return redirect('skillsshowpage')

def skills_rating_update_visibility(request, pk):
    if request.method == 'POST':
        skills_rating_visibility  = request.POST.get('skills_rating_Visibility')
        # description_visibility = request.POST.get('descriptionVisibility')
        about_data =Skill.objects.get(id=pk)

        about_data.skills_rating_visibility= skills_rating_visibility  
        # about_data.description_visibility = description_visibility
        about_data.save()
    return render(request,'app/edit_skills.html',{'key2':about_data})
    # return redirect('skillsshowpage')

# ------------------------------  Education Total OK -----------------------------------------------




def educationdata(request):
    if request.method == 'POST':
        
        # Get the form data directly from request.POST
        School_college = request.POST['School_college']
        Degree = request.POST['Degree']
        Field_of_study = request.POST['Field_of_study']
        University_name = request.POST['University_name']
        Start_date = request.POST['Start_date']
        End_date = request.POST['End_date']
        Description = request.POST['Description']
        
        # Create a new education record for the profile
        newuser=Education.objects.create(
            # profile=profile,
            school_college=School_college,
            degree=Degree,
            field_of_study=Field_of_study,
            university_name=University_name,
            edu_start_date=Start_date,
            edu_end_date=End_date,
            edu_des=Description
        )
        return redirect('educationeditpage',pk=newuser.id)

    return render(request, 'app/insert.html')

def educationdisplaydata(request):
    all_skills = Education.objects.all()
    return render(request, 'app/educationpage.html', {'key1': all_skills})

# Edit page view
def educationEditpage(request, pk):
    get_skill = Education.objects.get(id=pk)
    return render(request, 'app/edit_education.html', {'key2': get_skill})




def edu_update_school_college(request, pk):
    education_data = get_object_or_404(Education, pk=pk)

    if request.method == 'POST':
        education_data.school_college = request.POST.get('School_college')
        education_data.save()

    return redirect('educationshowpage')  # You can redirect to the detail page or wherever you want

# Update degree
def edu_update_degree(request, pk):
    education_data = get_object_or_404(Education, pk=pk)

    if request.method == 'POST':
        education_data.degree = request.POST.get('Degree')
        education_data.save()

    return redirect('educationshowpage')



# Update field of study
def edu_update_field_of_study(request, pk):
    education_data = get_object_or_404(Education, pk=pk)

    if request.method == 'POST':
        education_data.field_of_study = request.POST.get('Field_of_study')
        education_data.save()

    return redirect('educationshowpage')  # You can redirect to the detail page or wherever you want

# Update university name
def edu_update_university_name(request, pk):
    education_data = get_object_or_404(Education, pk=pk)

    if request.method == 'POST':
        education_data.university_name = request.POST.get('University_name')
        education_data.save()

    return redirect('educationshowpage')

# Update education start date
def edu_update_start_date(request, pk):
    education_data = get_object_or_404(Education, pk=pk)

    if request.method == 'POST':
        start_date_str = request.POST.get('Start_date')
        if start_date_str:
            start_date_obj = datetime.strptime(start_date_str, '%Y-%m-%d')
            education_data.edu_start_date = start_date_obj
            education_data.save()

    return redirect('educationshowpage')

# Update education end date
def edu_update_end_date(request, pk):
    education_data = get_object_or_404(Education, pk=pk)

    if request.method == 'POST':
        end_date_str = request.POST.get('End_date')
        if end_date_str:
            end_date_obj = datetime.strptime(end_date_str, '%Y-%m-%d')
            education_data.edu_end_date = end_date_obj
            education_data.save()

    return redirect('educationshowpage')

# Update education description
def edu_update_des(request, pk):
    education_data = get_object_or_404(Education, pk=pk)

    if request.method == 'POST':
        education_data.edu_des = request.POST.get('Description')
        education_data.save()

    return redirect('educationshowpage')

def edu_college_update_visibility(request, pk):
    if request.method == 'POST':
        edu_title_visibility = request.POST.get('edu_collegeVisibility')
        # description_visibility = request.POST.get('descriptionVisibility')
        about_data = Education.objects.get(id=pk)

        about_data.edu_title_visibility = edu_title_visibility 
        # about_data.description_visibility = description_visibility
        about_data.save()
    return render(request,'app/edit_education.html',{'key2':about_data})
    # return redirect('educationshowpage')





def educationUpdatedata(request, pk):
    udata = Education.objects.get(id=pk)
    school_college = request.POST.get('School_college')
    degree = request.POST.get('Degree')
    description = request.POST.get('Description')
    end_date_str = request.POST.get('EndDate')

    # Check if 'Degree' is present in the request data
    if degree:
        udata.degree = degree

    # Check if 'EndDate' is present in the request data and not empty
    if end_date_str:
        end_date_obj = datetime.strptime(end_date_str, '%Y-%m-%d')
        udata.edu_end_date = end_date_obj


    if description is not None and description.strip() != '':
        udata.edu_des = description

    udata.save()

    return redirect('educationshowpage')


# Delete the data
def educationDeletedata(request, pk):
    ddata = Education.objects.get(id=pk)
    ddata.delete()
    return redirect('educationshowpage')






# ----------------------------- Achivement TOtal  OK-----------------------------------




def achivementdata(request):
    if request.method == 'POST':
        
        # Get the form data directly from request.POST
        Title = request.POST['Title']
        Start_date = request.POST['Start_date']
        End_date= request.POST['End_date']
       
        Description = request.POST['Description']
        Image = request.FILES.get('Image')
        # Create a new education record for the profile
        newuser=Achievement.objects.create(
            # profile=profile,
            ach_title =Title,
            
            start_date=Start_date,
            end_date=End_date,
            ach_des=Description,
            image=Image
        )
        return redirect('achivementeditpage',pk=newuser.id)

    return render(request, 'app/insert.html')

def achivementdisplaydata(request):
    all_skills = Achievement.objects.all()
    return render(request, 'app/achievementspage.html', {'key1': all_skills})
    # return render(request, 'app/skillspage.html', {'key1': all_skills})

# Edit page view
def achivementEditpage(request, pk):
    get_skill = Achievement.objects.get(id=pk)
    return render(request, 'app/edit_achivement.html', {'key2': get_skill})


# Update Title view


def ach_update_title(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    if request.method == 'POST':
        Title = request.POST.get('Title')
        achievement.ach_title = Title
        achievement.save()
    return redirect('achivementshowpage')
    #     return JsonResponse({'success': True})
    # return JsonResponse({'success': False})




def ach_update_start_date(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    if request.method == 'POST':
        start_date = request.POST.get('Start_date')
        achievement.start_date = start_date
        achievement.save()
    return redirect('achivementshowpage')    
    #     return JsonResponse({'success': True})
    # return JsonResponse({'success': False})




def ach_update_end_date(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    if request.method == 'POST':
        End_date = request.POST.get('End_date')
        achievement.end_date = End_date
        achievement.save()
    return redirect('achivementshowpage')
    #     return JsonResponse({'success': True})
    # return JsonResponse({'success': False})





def ach_update_des(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    if request.method == 'POST':
        Description = request.POST.get('Description')
        achievement.ach_des = Description
        achievement.save()
    return redirect('achivementshowpage')
    #     return JsonResponse({'success': True})
    # return JsonResponse({'success': False})

    

def ach_update_image(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    
    if request.method == 'POST':
        # Clear the previous image, if any, before saving the new one
        if achievement.image:
            achievement.image.delete()
        
        # Save the new image
        image = request.FILES.get('Image')
        if image:
            achievement.image = image
        
        achievement.save()
    return redirect('achivementshowpage')
        # return JsonResponse({'success': True})
    

def ach_title_update_visibility(request, pk):
    if request.method == 'POST':
        ach_title_visibility = request.POST.get('ach_titleVisibility')
        # description_visibility = request.POST.get('descriptionVisibility')
        about_data = Achievement.objects.get(id=pk)

        about_data.ach_title_visibility  = ach_title_visibility
        # about_data.description_visibility = description_visibility
        about_data.save()
    return render(request,'app/edit_achivement.html',{'key2':about_data})
    # return redirect('achivementshowpage')








def achivementUpdatedata(request, pk):
    udata = get_object_or_404(Achievement, pk=pk)
    if request.method == 'POST':
      udata = Achievement.objects.get(id=pk)
      ach_title = request.POST.get('Title')
      start_date = request.POST.get('Start_date')
      end_date = request.POST.get('End_date')
      ach_des = request.POST.get('Description')
      image = request.POST.get('Image')

    # Check if 'Degree' is present in the request data
    if ach_title:
        udata.ach_title = ach_title

    # Check if 'EndDate' is present in the request data and not empty
    if end_date:
        end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
        udata.edu_end_date = end_date_obj


    if ach_des is not None and ach_des.strip() != '':
        udata.ach_des = ach_des

    udata.save()

    return redirect('achivementshowpage')



# ...
# Delete the data
# def achivementDeletedata(request, pk):
#     ddata = Achievement.objects.get(id=pk)
#     ddata.delete()
#     return redirect('achivementshowpage')  # Corrected the URL name
def achivementDeletedata(request, pk):
    ddata = get_object_or_404(Achievement, pk=pk)
    ddata.delete()
    return redirect('achivementshowpage')


#--------------------------------about Total OK-------------------------------------------------------


# def aboutdata(request):
#  if request.method == 'POST':
    
#     #data come from html too view
#     Title= request.POST['Title']
#     Description = request.POST['Description']
    
#     # action=request.POST['action']
    
#     #creating objct of model class
    
#     newusers = About.objects.create(
#            about_title=Title,
#            about_des=Description 
            
#         )
#     newusers.save()
    
#     #After insert render on show.html page
#     #return render(request,'app/show.html')
#     return redirect('abouteditpage',pk=newusers.id)
#  else:
#         return render(request, 'app/insert.html')

def aboutdata(request):
    title_error = None
    description_error = None

    if request.method == 'POST':
        Title = request.POST['Title']
        Description = request.POST['Description']

        if not Title:
            title_error = 'Title is required'

        if not Description:
            description_error = 'Description is required'

        if Title and Description:
            newusers = About.objects.create(about_title=Title, about_des=Description)
            newusers.save()
            return redirect('abouteditpage', pk=newusers.id)

    return render(request, 'app/insert.html', {
        'title_error': title_error,
        'description_error': description_error
    })
 
# Update Title view
def update_title(request, pk):
    if request.method == 'POST':
        Title = request.POST['Title']
        udata = About.objects.get(id=pk)
        udata.about_title = Title
        udata.save()
    return redirect('aboutshowpage')

# Update Description view
def update_description(request, pk):
    if request.method == 'POST':
        Description = request.POST['Description']
        udata = About.objects.get(id=pk)
        udata.about_des = Description
        udata.save()
    return redirect('aboutshowpage')

# Add more views for other fields if needed



def aboutdisplaydata(request):
    #select  * from tablename
    all_data= About.objects.all()
    return render(request,'app/aboutpage.html',{'key1':all_data})  #key1


#Edit page view
def aboutEditpage(request,pk):
    #fetching the data of particular id
    get_data=About.objects.get(id=pk)    #pk - primary key
    return render(request,'app/edit_about.html',{'key2':get_data})


#update data view

#don't delete


def title_update_visibility(request, pk):
    if request.method == 'POST':
        title_visibility = request.POST.get('titleVisibility')
        # description_visibility = request.POST.get('descriptionVisibility')
        about_data = About.objects.get(id=pk)

        about_data.title_visibility = title_visibility
        # about_data.description_visibility = description_visibility
        about_data.save()
    return render(request,'app/edit_about.html',{'key2':about_data})

    # return redirect('aboutshowpage')

def des_update_visibility(request, pk):
    if request.method == 'POST':
        # title_visibility = request.POST.get('titleVisibility')
        description_visibility = request.POST.get('descriptionVisibility')
        about_data = About.objects.get(id=pk)

        # about_data.title_visibility = title_visibility
        about_data.description_visibility = description_visibility
        about_data.save()
    return render(request,'app/edit_about.html',{'key2':about_data})
    # return redirect('aboutshowpage')

def aboutUpdatedata(request,pk):
    udata=About.objects.get(id=pk)
    udata.about_title = request.POST['Title']
    udata.about_des = request.POST['Description']
   
    #udata the data use save()
    udata.save()
    return redirect('aboutshowpage')


    
#delete the
# def aboutDeletedata(request,pk):
#     ddata =About.objects.get(id=pk)
#     ddata.delete()
#     return redirect('aboutshowpage')

def aboutDeletedata(request, pk):
    try:
        ddata = About.objects.get(id=pk)
        ddata.delete()
    except About.DoesNotExist:
        pass
    return redirect('aboutshowpage')



def save_radio_data(request, pk):
    if request.method == 'POST':
        title_visibility = request.POST.get('titleVisibility')
        description_visibility = request.POST.get('descriptionVisibility')
        
        # Assuming you have a model to save this data
        about_data = About.objects.get(id=pk)
        about_data.title_visibility = title_visibility
        about_data.description_visibility = description_visibility
        about_data.save()
        
        return HttpResponse('Data saved successfully')
    else:
        return HttpResponse('Invalid request method')


# -----------------------------Workportfolio NOT ((none)OK------------------------------------------------




def workportfoliodata(request):
    if request.method == 'POST':
        
        # Get the form data directly from request.POST
        Title = request.POST['Title']
       
       
        Description = request.POST['Description']
        Link = request.POST['Link']
        # Create a new education record for the profile
        newuser=WorkPortfolio.objects.create(
                # profile=profile,
                work_title=Title,
                work_des=Description,
                link=Link
            )
        return redirect('workportfolioeditpage',pk=newuser.id)

    return render(request, 'app/insert.html')


# Update Title view for Work Portfolio
def work_update_title(request, pk):
    if request.method == 'POST':
        Title = request.POST['Title']
        work_item = WorkPortfolio.objects.get(id=pk)
        work_item.work_title = Title
        work_item.save()
    return redirect('workportfolioshowpage')  # Redirect to the appropriate page

# Update Description view for Work Portfolio
def work_update_description(request, pk):
    if request.method == 'POST':
        Description = request.POST['Description']
        work_item = WorkPortfolio.objects.get(id=pk)
        work_item.work_des = Description
        work_item.save()
    return redirect('workportfolioshowpage')  # Redirect to the appropriate page

# Update Link view for Work Portfolio
def work_update_link(request, pk):
    if request.method == 'POST':
        Link = request.POST['Link']
        work_item = WorkPortfolio.objects.get(id=pk)
        work_item.link = Link
        work_item.save()
    return redirect('workportfolioshowpage')  # Redirect to the appropriate page


def workportfoliodisplaydata(request):
    #select  * from tablename
    all_data= WorkPortfolio.objects.all()
    return render(request,'app/workportfolio.html',{'key1':all_data})  #key1



def workportfolioEditpage(request,pk):
    #fetching the data of particular id
    get_data=WorkPortfolio.objects.get(id=pk)    #pk - primary key
    return render(request,'app/edit_workportfolio.html',{'key2':get_data})


def workportfolioUpdatedata(request,pk):
    udata=WorkPortfolio.objects.get(id=pk)
    udata.work_title = request.POST.get('Title')
    udata.work_des = request.POST.get('Description')
    udata.link = request.POST.get('Link')
    #udata the data use save()
    udata.save()
    return redirect('workportfolioshowpage')






def workportfolioDeletedata(request,pk):
    ddata =WorkPortfolio.objects.get(id=pk)
    ddata.delete()
    return redirect('workportfolioshowpage')


def work_title_update_visibility(request, pk):
    if request.method == 'POST':
        work_title_visibility = request.POST.get('work_title_Visibility')
        # description_visibility = request.POST.get('descriptionVisibility')
        about_data =WorkPortfolio.objects.get(id=pk)

        about_data.work_title_visibility= work_title_visibility  
        # about_data.description_visibility = description_visibility
        about_data.save()
    return render(request,'app/edit_workportfolio.html',{'key2':about_data})
    # return redirect('workportfolioshowpage')


def work_des_update_visibility(request, pk):
    if request.method == 'POST':
        work_des_visibility = request.POST.get('work_des_Visibility')
        # description_visibility = request.POST.get('descriptionVisibility')
        about_data =WorkPortfolio.objects.get(id=pk)

        about_data.work_des_visibility= work_des_visibility  
        # about_data.description_visibility = description_visibility
        about_data.save()
    return render(request,'app/edit_workportfolio.html',{'key2':about_data})
    # return redirect('workportfolioshowpage')


def work_link_update_visibility(request, pk):
    if request.method == 'POST':
        work_link_visibility = request.POST.get('work_link_Visibility')
        # description_visibility = request.POST.get('descriptionVisibility')
        about_data =WorkPortfolio.objects.get(id=pk)

        about_data.work_link_visibility= work_link_visibility  
        # about_data.description_visibility = description_visibility
        about_data.save()
    return render(request,'app/edit_workportfolio.html',{'key2':about_data})
    # return redirect('workportfolioshowpage')




#--------------------------------------Place lived Total OK  -----------------------------

def placesdata(request):
 if request.method == 'POST':
    
    #data come from html too view
    Place = request.POST['Place']
    Start_date = request.POST['Start_date']
    End_date = request.POST['End_date']
    # Currently_living_in = request.POST.get('Currently_living_in') == 'on'
    # action=request.POST['action']
    
    #creating objct of model class
    
    newuser=PlaceLived.objects.create(place=Place,place_start_date=Start_date,
                                         place_end_date=End_date)#,currently_living_in=Currently_living_in
       
    newuser.save()
    
    #After insert render on show.html page
    #return render(request,'app/show.html')
    return redirect('placeseditpage',pk=newuser.id)
 else:
        return render(request, 'app/insert.html')
 

def place_update_name(request, pk):
    place_data = get_object_or_404(PlaceLived, pk=pk)

    if request.method == 'POST':
        place_data.place = request.POST.get('Place')
        place_data.save()

    return redirect('placesshowpage')

# Update Place Lived in start date
def place_update_start_date(request, pk):
    place_data = get_object_or_404(PlaceLived, pk=pk)

    if request.method == 'POST':
        start_date_str = request.POST.get('Start_date')
        if start_date_str:
            start_date_obj = datetime.strptime(start_date_str, '%Y-%m-%d')
            place_data.place_start_date = start_date_obj
            place_data.save()

    return redirect('placesshowpage')

# Update Place Lived in end date
def place_update_end_date(request, pk):
    place_data = get_object_or_404(PlaceLived, pk=pk)

    if request.method == 'POST':
        end_date_str = request.POST.get('End_date')
        if end_date_str:
            end_date_obj = datetime.strptime(end_date_str, '%Y-%m-%d')
            place_data.place_end_date = end_date_obj
            place_data.save()

    return redirect('placesshowpage')


def placesdisplaydata(request):
    #select  * from tablename
    all_data= PlaceLived.objects.all()
    return render(request,'app/livingpage.html',{'key1':all_data}) 
 

def placesEditpage(request,pk):
    #fetching the data of particular id
    get_data=PlaceLived.objects.get(id=pk)    #pk - primary key
    return render(request,'app/edit_place.html',{'key2':get_data})


def placesUpdatedata(request, pk):
    udata = PlaceLived.objects.get(id=pk)
    
    if request.method == 'POST':
        # Update the place, start_date, and end_date fields
        udata.place = request.POST.get('Place', '')

        # Check if the Start_date is provided and in the correct format
        place_start_date = request.POST.get('Start_date', '')
        if place_start_date:
            try:
                udata.place_start_date = datetime.strptime(place_start_date, "%Y-%m-%d").date()
            except ValueError:
                # Handle the error or invalid date format
                pass

        # Check if the End_date is provided and in the correct format
        place_end_date = request.POST.get('End_date', '')
        if place_end_date:
            
            try:
                udata.place_end_date = datetime.strptime(place_end_date, "%Y-%m-%d").date()
            except ValueError:
                # Handle the error or invalid date format
                pass

        # # Update the currently_living_in field if provided
        # currently_living_in = request.POST.get('Currently_living_in', '')
        # if currently_living_in.lower() == 'true':
        #     udata.currently_living_in = True
        # elif currently_living_in.lower() == 'false':
        #     udata.currently_living_in = False

        # Save the data
        udata.save()

        return redirect('placesshowpage')

# def placesUpdatedata(request, pk):
#     try:
#         # Attempt to retrieve the PlaceLived object with the specified 'pk' (primary key)
#         place = get_object_or_404(PlaceLived, id=pk)
#     except PlaceLived.DoesNotExist:
#         # Handle the case where the object does not exist
#         raise Http404("PlaceLived object does not exist")  # You can customize this error message

#     # Rest of your view logic here
#     # You can render a template, perform updates, or return an HTTP response

#     return redirect('placesshowpage')









def placesDeletedata(request,pk):
    ddata =PlaceLived.objects.get(id=pk)
    ddata.delete()
    return redirect('placesshowpage')




def place_update_visibility(request, pk):
    if request.method == 'POST':
        place_visibility   = request.POST.get('placeVisibility')
        # description_visibility = request.POST.get('descriptionVisibility')
        about_data = PlaceLived.objects.get(id=pk)

        about_data.place_visibility    = place_visibility    
        # about_data.description_visibility = description_visibility
        about_data.save()
    return render(request,'app/edit_place.html',{'key2':about_data})
    # return redirect('placesshowpage')


# ---------------------- -----------Relationship Total OK----------------------------------------


def relationshipdata(request):
 if request.method == 'POST':
    
    #data come from html too view
    Name = request.POST['Name']
    
    Relationship_type = request.POST['Relationship_type']

    newuser=Relationship.objects.create(name=Name,relationship_type=Relationship_type)
    # action=request.POST['action']
    
    #creating objct of model class
    
    
    newuser.save()
    
    #After insert render on show.html page
    #return render(request,'app/show.html')
    return redirect('relationshipeditpage',pk=newuser.id)
 else:
        return render(request, 'app/insert.html')
 

# def person_update_name(request, pk):
#     person_data = get_object_or_404(PlaceLived, pk=pk)

#     if request.method == 'POST':
#         person_data.name  = request.POST.get('Name')
#         person_data.save()

#     return redirect('relationshipshowpage')

# def person_update_relationships(request, pk):
#     person_data = get_object_or_404(PlaceLived, pk=pk)

#     if request.method == 'POST':
#         person_data.relationship_type  = request.POST.get('Relationship_type')
#         person_data.save()

#     return redirect('relationshipshowpage')
def person_update_name(request, pk):
    person = get_object_or_404(Relationship, pk=pk)
    if request.method == 'POST':
        Name = request.POST.get('Name')
        person.name = Name
        person.save()
    return redirect('relationshipshowpage')
    #     return JsonResponse({'success': True})
    # return JsonResponse({'success': False})

# Update person's relationships view
def person_update_relationships(request, pk):
    person = get_object_or_404(Relationship, pk=pk)
    if request.method == 'POST':
        Relationship_type = request.POST.get('Relationship_type')
        person.relationship_type = Relationship_type
        person.save()
    return redirect('relationshipshowpage')
    #     return JsonResponse({'success': True})
    # return JsonResponse({'success': False})

 
def relationshipdisplaydata(request):
    #select  * from tablename
    all_data= Relationship.objects.all()
    return render(request,'app/relationshippage.html',{'key1':all_data})  #key1



def relationshipEditpage (request,pk):
    #fetching the data of particular id
    get_data=Relationship.objects.get(id=pk)    #pk - primary key
    return render(request,'app/edit_relationship.html',{'key2':get_data})




def relationshipUpdatedata(request, pk):
    # Get the existing Relationship object
    udata = get_object_or_404(Relationship, id=pk)

    if request.method == 'POST':
        # Bind the form to the POST data and instance
        form = RelationshipForm(request.POST, instance=udata)

        if form.is_valid():
            # Save the updated data from the form
            form.save()
            return redirect('relationshipshowpage')
    else:
        # Display the form pre-filled with the existing data
        form = RelationshipForm(instance=udata)

    return render(request, 'app/edit_relationship.html', {'form': form, 'relationship': udata})


def relationshipDeletedata(request,pk):
    ddata =Relationship.objects.get(id=pk)
    ddata.delete()
    return redirect('relationshipshowpage')

def relationship_name_update_visibility(request, pk):
    if request.method == 'POST':
        relationship_name_visibility  = request.POST.get('relationship_name_Visibility')
        # description_visibility = request.POST.get('descriptionVisibility')
        about_data = Relationship.objects.get(id=pk)

        about_data.relationship_name_visibility= relationship_name_visibility  
        # about_data.description_visibility = description_visibility
        about_data.save()
    return render(request,'app/edit_relationship.html',{'key2':about_data})
    # return redirect('relationshipshowpage')


def relationship_type_update_visibility(request, pk):
    if request.method == 'POST':
        relationship_type_visibility  = request.POST.get('relationship_type_Visibility')
        # description_visibility = request.POST.get('descriptionVisibility')
        about_data = Relationship.objects.get(id=pk)

        about_data.relationship_type_visibility= relationship_type_visibility  
        # about_data.description_visibility = description_visibility
        about_data.save()
    return render(request,'app/edit_relationship.html',{'key2':about_data})
    # return redirect('relationshipshowpage')