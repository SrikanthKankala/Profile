# from django import forms
# from .models import Contact,Achievement,About


# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = '__all__'

#     def save(self, commit=True):
#         instance = super(ContactForm, self).save(commit=False)

#         # Exclude fields that are not provided in the form submission
#         for field in self.Meta.model._meta.fields:
#             if field.name not in self.cleaned_data:
#                 setattr(instance, field.name, None)

#         if commit:
#             instance.save()
#         return instance
    

# class AchievementForm(forms.ModelForm):
#     class Meta:
#         model = Achievement
#         fields = ['ach_title', 'start_date', 'end_date', 'ach_des', 'image']



# class AboutForm(forms.ModelForm):
#     class Meta:
#         model = About
#         fields = '__all__'



from django import forms
from .models import Contact,Achievement,About,Relationship


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def save(self, commit=True):
        instance = super(ContactForm, self).save(commit=False)

        # Exclude fields that are not provided in the form submission
        for field in self.Meta.model._meta.fields:
            if field.name not in self.cleaned_data:
                setattr(instance, field.name, None)

        if commit:
            instance.save()
        return instance
    

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = '__all__'
class RelationshipForm(forms.ModelForm):
    class Meta:
        model = Relationship
        # fields = '__all__'
        fields = ['name', 'relationship_type']

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'