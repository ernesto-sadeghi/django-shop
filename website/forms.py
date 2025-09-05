from django.forms import ModelForm
from website.models import Contact,Newsteller

# forms ===> forms.Form 
# forms ===> forms.ModelForm
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
class NewstellerForm(ModelForm):
    class Meta:
        model = Newsteller
        fields = "__all__"



