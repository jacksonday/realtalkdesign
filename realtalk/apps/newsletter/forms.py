from django import forms
from .models import RevJoin, SubJoin

class JoinForm(forms.ModelForm):
	email = forms.EmailField(label='', 
			widget = forms.EmailInput(
					 attrs={'placeholder':'email address', 
					 		# 'class':'form-control'
					 		}))

class RevJoinForm(JoinForm):

	class Meta:
		model = RevJoin
		fields = ['email']

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get("email")
		qs = RevJoin.objects.filter(email__iexact=email)
		if qs.exists():
			raise forms.ValidationError("This email address is already signed up as a reviewer")
		return email

class SubJoinForm(JoinForm):

	class Meta:
		model = SubJoin
		fields = ['email']

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get("email")
		qs = SubJoin.objects.filter(email__iexact=email)
		if qs.exists():
			raise forms.ValidationError("This email address is already signed up as a submitter")
		return email