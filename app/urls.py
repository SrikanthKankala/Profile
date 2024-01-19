from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Insertview, name='insertpage'),

    path('insert/',views.Insertdata, name='insert'),
    path('showpage/',views.displaydata, name='showpage'),
    

    path('update_contact_number/<int:pk>/', views.update_contact_number, name='update_contact_number'),
    path('update_email/<int:pk>/', views.update_email, name='update_email'),
    path('update_lives_in/<int:pk>/', views.update_lives_in, name='update_lives_in'),
    path('update_last_studied_in/<int:pk>/', views.update_last_studied_in, name='update_last_studied_in'),
    #  # Update Last Studied In
    # path('update_last_studied_in/<int:pk>/', views.update_last_studied_in, name='update_last_studied_in'),
    # Update Gender
    path('update_gender/<int:pk>/', views.update_gender, name='update_gender'),
    # Update Total Experience
    path('update_total_experience/<int:pk>/', views.update_total_experience, name='update_total_experience'),
    # Update Relationship Status
    path('update_relationship_status/<int:pk>/', views.update_relationship_status, name='update_relationship_status'),
     # Update Languages
    path('update_languages/<int:pk>/', views.update_languages, name='update_languages'),
    # Update Birthday
    path('update_birthday/<int:pk>/', views.update_birthday, name='update_birthday'),
    
    # Update Website
    path('update_website/<int:pk>/', views.update_website, name='update_website'),
    
    # Update Religion
    path('update_religion/<int:pk>/', views.update_religion, name='update_religion'),


    path('editpage/<int:pk>',views.Editpage, name='editpage'),
    path('update/<int:pk>',views.Updatedata, name='update'),
    path('delete/<int:pk>',views.Deletedata, name='delete'),
path('overview_contact_update_visibility/<int:pk>/', views.overview_contact_update_visibility, name='overview_contact_update_visibility'),

# __________________________________________________________________________________________________


    path('experiencepage/', views.experiencedata, name='experiencepage'),

    path('ex_update_job_title/<int:pk>/', views.ex_update_job_title, name='ex_update_job_title'),
    path('ex_update_company_name/<int:pk>/', views.ex_update_company_name, name='ex_update_company_name'),
    path('ex_update_location/<int:pk>/', views.ex_update_location, name='ex_update_location'),
    path('ex_update_start_date/<int:pk>/', views.ex_update_start_date, name='ex_update_start_date'),
    path('ex_update_end_date/<int:pk>/', views.ex_update_end_date, name='ex_update_end_date'),
    path('ex_update_description/<int:pk>/', views.ex_update_description, name='ex_update_description'),
    # 

    path('experienceshowpage/', views.experiencedisplaydata, name='experienceshowpage'),
    path('experienceeditpage/<int:pk>/', views.experienceEditpage, name='experienceeditpage'),
    path('experienceupdatepage/<int:pk>/', views.experienceUpdatedata, name='experienceupdatepage'),
    path('experiencedeletepage/<int:pk>/', views.experienceDeletedata, name='experiencedeletepage'),

path('ex_jobtitle_update_visibility/<int:pk>/', views.ex_jobtitle_update_visibility, name='ex_jobtitle_update_visibility'),


#---------------------------------------------------------------------------------------------
    
    path('skillspage/', views.skilldata, name='skillspage'),

    path('skills_update_select_skill/<int:pk>/', views.skills_update_select_skill, name='skills_update_select_skill'),
    path('skills_update_rating/<int:pk>/', views.skills_update_rating, name='skills_update_rating'),
    

    path('skillsshowpage/', views.skilldisplaydata, name='skillsshowpage'),
    path('skillseditpage/<int:pk>/', views.skillEditpage, name='skillseditpage'),
    path('skillsupdatepage/<int:pk>/', views.skillUpdatedata, name='skillsupdatepage'),
    path('skillsdeletepage/<int:pk>/', views.skillDeletedata, name='skillsdeletepage'),


path('skills_name_update_visibility/<int:pk>/', views.skills_name_update_visibility, name='skills_name_update_visibility'),
path('skills_rating_update_visibility/<int:pk>/', views.skills_rating_update_visibility, name='skills_rating_update_visibility'),

#--------------------------------------------------------------------------------

    path('educationpage/', views.educationdata, name='educationpage'),

    path('edu_update_school_college/<int:pk>/', views.edu_update_school_college, name='edu_update_school_college'),

    # Update degree
    path('edu_update_degree/<int:pk>/', views.edu_update_degree, name='edu_update_degree'),

    # Update field of study
    path('edu_update_field_of_study/<int:pk>/', views.edu_update_field_of_study, name='edu_update_field_of_study'),

    # Update university name
    path('edu_update_university_name/<int:pk>/', views.edu_update_university_name, name='edu_update_university_name'),

    # Update education start date
    path('edu_update_start_date/<int:pk>/', views.edu_update_start_date, name='edu_update_start_date'),

    # Update education end date
    path('edu_update_end_date/<int:pk>/', views.edu_update_end_date, name='edu_update_end_date'),

    # Update education description
    path('edu_update_des/<int:pk>/', views.edu_update_des, name='edu_update_des'),


    path('educationshowpage/', views.educationdisplaydata, name='educationshowpage'),
    path('educationeditpage/<int:pk>/', views.educationEditpage, name='educationeditpage'),
    path('educationupdatepage/<int:pk>/', views.educationUpdatedata, name='educationupdatepage'),
    path('educationdeletepage/<int:pk>/', views.educationDeletedata, name='educationdeletepage'),


path('edu_college_update_visibility/<int:pk>/', views.edu_college_update_visibility, name='edu_college_update_visibility'),

#------------------------------------------------------------------------------------------------------
    

    path('achivementpage/', views.achivementdata, name='achivementpage'),
    
    path('ach_update_title/<int:pk>/', views.ach_update_title, name='ach_update_title'),

    # Update achievement start date
    path('ach_update_start_date/<int:pk>/', views.ach_update_start_date, name='ach_update_start_date'),

    # Update achievement end date
    path('ach_update_end_date/<int:pk>/', views.ach_update_end_date, name='ach_update_end_date'),

    # Update achievement description
    path('ach_update_des/<int:pk>/', views.ach_update_des, name='ach_update_des'),

    # Update achievement image
    path('ach_update_image/<int:pk>/', views.ach_update_image, name='ach_update_image'),
    path('achivementshowpage/', views.achivementdisplaydata, name='achivementshowpage'),
    path('achivementeditpage/<int:pk>/', views.achivementEditpage, name='achivementeditpage'),
    path('achivementupdatepage/<int:pk>/', views.achivementUpdatedata, name='achivementupdatepage'),
    path('achivementdeletepage/<int:pk>/', views.achivementDeletedata, name='achivementdeletepage'),


path('ach_title_update_visibility/<int:pk>/', views.ach_title_update_visibility, name='ach_title_update_visibility'),
#________________________________________________________________________________________________
    path('aboutpage/', views.aboutdata, name='aboutpage'),
    # path('aboutpage/', views.aboutdata, name='aboutpage'),

path('update_title/<int:pk>/', views.update_title, name='update_title'),
path('update_description/<int:pk>/', views.update_description, name='update_description'),

# Add a URL for saving the radio button data
path('save_radio_data/<int:pk>/', views.save_radio_data, name='save_radio_data'),
path('title_update_visibility/<int:pk>/', views.title_update_visibility, name='title_update_visibility'),
path('des_update_visibility/<int:pk>/', views.des_update_visibility, name='des_update_visibility'),

# Add more URLs for other fields if needed

    path('aboutshowpage/', views.aboutdisplaydata, name='aboutshowpage'),
    path('abouteditpage/<int:pk>/', views.aboutEditpage, name='abouteditpage'),
    path('aboutupdatepage/<int:pk>/', views.aboutUpdatedata, name='aboutupdatepage'),
    path('aboutdeletepage/<int:pk>/', views.aboutDeletedata, name='aboutdeletepage'),


#-----------------------------------------------------------------------------------------------------
    
    path('workportfoliopage/', views.workportfoliodata, name='workportfoliopage'),

    path('work_update_title/<int:pk>/', views.work_update_title, name='work_update_title'),
    path('work_update_description/<int:pk>/', views.work_update_description, name='work_update_description'),
    path('work_update_link/<int:pk>/', views.work_update_link, name='work_update_link'),


    path('workportfolioshowpage/', views.workportfoliodisplaydata, name='workportfolioshowpage'),
    path('workportfolioeditpage/<int:pk>/', views.workportfolioEditpage, name='workportfolioeditpage'),
    path('workportfolioupdatepage/<int:pk>/', views.workportfolioUpdatedata, name='workportfolioupdatepage'),
    path('workportfoliodeletepage/<int:pk>/', views.workportfolioDeletedata, name='workportfoliodeletepage'),


path('work_title_update_visibility/<int:pk>/', views.work_title_update_visibility, name='work_title_update_visibility'),
path('work_des_update_visibility/<int:pk>/', views.work_des_update_visibility, name='work_des_update_visibility'),
path('work_link_update_visibility/<int:pk>/', views.work_link_update_visibility, name='work_link_update_visibility'),

#------------------------------------------------------------------------------------------


    path('placespage/', views.placesdata, name='placespage'),

    # Update place name
    path('place_update_name/<int:pk>/', views.place_update_name, name='place_update_name'),

    # Update place start date
    path('place_update_start_date/<int:pk>/', views.place_update_start_date, name='place_update_start_date'),

    # Update place end date
    path('place_update_end_date/<int:pk>/', views.place_update_end_date, name='place_update_end_date'),



    path('placesshowpage/', views.placesdisplaydata, name='placesshowpage'),
    path('placeseditpage/<int:pk>/', views.placesEditpage, name='placeseditpage'),
    path('placesupdatepage/<int:pk>/', views.placesUpdatedata, name='placesupdatepage'),
    path('placesdeletepage/<int:pk>/', views.placesDeletedata, name='placesdeletepage'),


path('place_update_visibility/<int:pk>/', views.place_update_visibility, name='place_update_visibility'),

#----------------------------------------------------------------------------------------

    path('relationshippage/', views.relationshipdata, name='relationshippage'),

    path('person_update_name/<int:pk>/', views.person_update_name, name='person_update_name'),

    # Update person's relationships
    path('person_update_relationships/<int:pk>/', views.person_update_relationships, name='person_update_relationships'),

    
    path('relationshipshowpage/', views.relationshipdisplaydata, name='relationshipshowpage'),
    path('relationshipeditpage/<int:pk>/', views.relationshipEditpage, name='relationshipeditpage'),
    path('relationshipupdatepage/<int:pk>/', views.relationshipUpdatedata, name='relationshipupdatepage'),
    path('relationshipdeletepage/<int:pk>/', views.relationshipDeletedata, name='relationshipdeletepage'),

path('relationship_name_update_visibility/<int:pk>/', views.relationship_name_update_visibility, name='relationship_name_update_visibility'),
path('relationship_type_update_visibility/<int:pk>/', views.relationship_type_update_visibility, name='relationship_type_update_visibility'),

    # path('profilepage/', views.display_data, name='profilepage'),
]


