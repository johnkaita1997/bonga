from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.core.validators import MinValueValidator
from django.forms.widgets import Select
from dal import autocomplete

from appuser.models import AppUser
from constants.models import Constant
from contact.models import Contact
from mobile.models import Mobile
from school.models import School
from mobile.models import SchoolWebCreate
from student.models import Student
from web.models import ImportStudentModel, ImportParentModel, MobileMinutes


class AppUserBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None


# create a ModelForm
class AppUserForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = AppUser
        fields = "__all__"


# create a ModelForm
class EditParentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Contact
        fields = (
            'mobile',
            'name',
            'mobiletwo',
        )


# create a ModelForm
class EditStudentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Student
        exclude = (
            'active',
            'activefromdate',
            'registrationnumber',
            'phonenumber',
            'password',
            'confirmpassword',
            'tokenbalance',
            'totalnumberofcalls',
            'username',
            'email',
            'school',
            'user',
        )


class ReadOnlySelect(Select):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs["disabled"] = "disabled"


class AddStudentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Student
        exclude = (
            'active',
            'activefromdate',
            'phonenumber',
            'password',
            'confirmpassword',
            'tokenbalance',
            'totalnumberofcalls',
            'username',
            'email',
            'contacts',
            'user',
        )

        widgets = {
            'school': ReadOnlySelect,
            'hidden_school': forms.HiddenInput,
        }

    # add a hidden field for school
    hidden_school = forms.CharField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        # pass the initial value of school to the hidden field
        initial = kwargs.get('initial', {})
        self.base_fields['hidden_school'].initial = initial.get('school')
        super().__init__(*args, **kwargs)


class AddParentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Contact
        exclude = (
            'contactuser',
        )


class EditSchoolForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = School
        exclude = ('mobile',)

        # widgets = {
        #     'mobile': ReadOnlySelect,
        #     'hidden_mobile': forms.HiddenInput,
        # }

    # add a hidden field for mobile
    # hidden_mobile = forms.CharField(widget=forms.HiddenInput, required=False)

    # def __init__(self, *args, **kwargs):
    #     # pass the initial value of mobile to the hidden field
    #     initial = kwargs.get('initial', {})
    #     self.base_fields['hidden_mobile'].initial = initial.get('mobile')
    #     super().__init__(*args, **kwargs)


class AddSchoolForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = SchoolWebCreate
        exclude = ()


class EditMobileForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Mobile
        fields = ('active',)


class EditAgentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = AppUser
        fields = (
            'school',
            'fullname',
            'phone',
        )

    def __init__(self, *args, **kwargs):
        super(EditAgentForm, self).__init__(*args, **kwargs)
        self.fields['school'].required = True
        self.fields['fullname'].required = True
        self.fields['phone'].required = True


class AddAgentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = AppUser
        exclude = (
            'last_login',
            'groups',
            'user_permissions',
            'date_deleted',
            'date_joined',
            'first_name',
            'last_name',
            'is_staff',
            'is_agent',
            'is_superuser',
            'is_active',
            'id',
            'username',
            'email',
            'password',
            'confirmpassword',
            'isstudent',
            'isadmin',
            'isparent',
            'isagent',
        )


class EditSettingsForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Constant
        fields = (
            'activationamount',
            'minutepershilling',
            'minutespertokenOrequivalentminutes',)

    def __init__(self, *args, **kwargs):
        super(EditSettingsForm, self).__init__(*args, **kwargs)
        self.fields['activationamount'].required = True
        self.fields['minutepershilling'].required = True
        self.fields['minutespertokenOrequivalentminutes'].required = True

        self.fields['activationamount'].validators.append(MinValueValidator(0))
        self.fields['minutepershilling'].validators.append(MinValueValidator(0))
        self.fields['minutespertokenOrequivalentminutes'].validators.append(MinValueValidator(0))

    def clean_activationamount(self):
        activationamount = self.cleaned_data.get('activationamount')
        if activationamount <= 0:
            raise forms.ValidationError("Activation amount cannot be less than zero.")
        return activationamount

    def clean_minutepershilling(self):
        minutepershilling = self.cleaned_data.get('minutepershilling')
        if minutepershilling <= 0:
            raise forms.ValidationError("Minute per shilling must be greater than zero.")
        return minutepershilling

    def clean_minutespertokenOrequivalentminutes(self):
        minutespertokenOrequivalentminutes = self.cleaned_data.get('minutespertokenOrequivalentminutes')
        if minutespertokenOrequivalentminutes <= 0:
            raise forms.ValidationError("Minutes per token or equivalent minutes must be greater than zero.")
        return minutespertokenOrequivalentminutes


class ImportStudentsExcelForm(forms.ModelForm):
    excel_file = forms.FileField(label='Upload Excel file', required=True)

    class Meta:
        model = ImportStudentModel
        fields = "__all__"


class ImportParentExcelForm(forms.ModelForm):
    excel_file = forms.FileField(label='Upload Excel file', required=True)

    class Meta:
        model = ImportParentModel
        fields = "__all__"


class MinutesForm(forms.ModelForm):
    class Meta:
        model = MobileMinutes
        fields = "__all__"


class DevicesForm(forms.ModelForm):
    school = forms.ModelChoiceField(
        queryset=School.objects.all(),
        fields=["active", "mobile", "school"],
        widget=autocomplete.ModelSelect2(
            url='school-autocomplete',
            attrs={
                'data-placeholder': 'Search for a school...',
                'data-minimum-input-length': 1,  # Minimum number of characters to trigger search
            },
        ),
    )

    class Meta:
        model = Mobile
