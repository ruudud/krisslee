from django.forms import ModelForm

from krisslee.contribution.models import Contribution

class ContributionForm(ModelForm):
    class Meta:
        model = Contribution
