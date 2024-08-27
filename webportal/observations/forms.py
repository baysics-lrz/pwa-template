from django import forms
from django.contrib.gis.geos import Point
from django.core.exceptions import ValidationError

from .models import Category1, Category2, Category3, Category4, CERTAINTY_CHOICES, CATEGORY3FEATURE1_CHOICES, YESNO_CHOICES
from .util import is_point_in_bavaria


class Category1Form(forms.ModelForm):
    Certainty = forms.ChoiceField(widget=forms.RadioSelect(), choices=CERTAINTY_CHOICES,
                                  label='Certainty', required=False)
    Lat = forms.DecimalField(
        widget=forms.NumberInput(attrs={'step': '0.000001', 'placeholder': '00.000000'}), label='Latitude')
    Lon = forms.DecimalField(
        widget=forms.NumberInput(attrs={'step': '0.000001', 'placeholder': '00.000000'}), label='Longitude')
    ObservationTime = forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={'placeholder': '00:00 - 23:59'}),
                                      label='Observation time')
    ClimateStation = forms.IntegerField(required=False)
    Municipal = forms.CharField(required=False)
    Cell = forms.IntegerField(required=False)
    AccuracyGPS = forms.DecimalField(required=False)

    class Meta:
        model = Category1
        fields = ('Category1Subject', 'Certainty', 'Number', 'Category1Feature1', 'Category1Feature2',
                  'Category1Feature3', 'ObservationDate', 'ObservationTime', 'Photo', 'Lat', 'Lon', 'Position',
                  'ClimateStation', 'Municipal', 'Cell', 'AccuracyGPS')

    def clean(self):
        cleaned_data = super().clean()
        point = Point(float(cleaned_data.get('Lat')), float(cleaned_data.get('Lon')))
        if not is_point_in_bavaria(point=point):
            raise ValidationError("The selected point is not located in Bavaria!")
        return cleaned_data


class Category2Form(forms.ModelForm):
    Certainty = forms.ChoiceField(widget=forms.RadioSelect(), choices=CERTAINTY_CHOICES,
                                  label='Certainty')
    Category2Feature3 = forms.ChoiceField(widget=forms.RadioSelect(), choices=YESNO_CHOICES, label='Category2Feature1')
    Category2Feature4 = forms.ChoiceField(widget=forms.RadioSelect(), choices=YESNO_CHOICES, label='Category2Feature2')
    Category2Feature5 = forms.ChoiceField(widget=forms.RadioSelect(), choices=YESNO_CHOICES, label='Category2Feature3')
    Category2Feature6 = forms.ChoiceField(widget=forms.RadioSelect(), choices=YESNO_CHOICES, label='Category2Question4', required=False)
    Category2Feature1 = forms.ChoiceField(widget=forms.RadioSelect(), choices=YESNO_CHOICES, label='Category2Question5', required=False)
    Category2Feature2 = forms.ChoiceField(widget=forms.RadioSelect(), choices=YESNO_CHOICES, label='Category2Question6', required=False)
    Lat = forms.DecimalField(
        widget=forms.NumberInput(attrs={'step': '0.000001', 'placeholder': '00.000000'}), label='Latitude')
    Lon = forms.DecimalField(
        widget=forms.NumberInput(attrs={'step': '0.000001', 'placeholder': '00.000000'}), label='Longitude')
    ClimateStation = forms.IntegerField(required=False)
    Municipal = forms.CharField(required=False)
    Cell = forms.IntegerField(required=False)
    AccuracyGPS = forms.DecimalField(required=False)

    class Meta:
        model = Category2
        fields = (
            'Category2Subject', 'Certainty', 'Category2Feature1', 'Category2Feature2', 'Category2Feature3',
            'Category2Feature4', 'Category2Feature5', 'Category2Feature6','Category2Feature7', 'Category2Feature8',
            'Lat', 'Lon', 'Position', 'ClimateStation', 'Municipal', 'Cell', 'ObservationDate', 'Photo', 'AccuracyGPS'
                )

    def clean(self):
        cleaned_data = super().clean()
        point = Point(float(cleaned_data.get('Lat')), float(cleaned_data.get('Lon')))
        if not is_point_in_bavaria(point=point):
            raise ValidationError("The selected point is not located in Bavaria!")
        return cleaned_data


class Category3Form(forms.ModelForm):
    Certainty = forms.ChoiceField(widget=forms.RadioSelect(), choices=CERTAINTY_CHOICES, label='Certainty')
    Category3Feature1 = forms.ChoiceField(widget=forms.RadioSelect(), choices=CATEGORY3FEATURE1_CHOICES, label='Category3Feature1')
    Lat = forms.DecimalField(
        widget=forms.NumberInput(attrs={'step': '0.000001', 'placeholder': '00.000000'}), label='Latitude')
    Lon = forms.DecimalField(
        widget=forms.NumberInput(attrs={'step': '0.000001', 'placeholder': '00.000000'}), label='Longitude')
    ClimateStation = forms.IntegerField(required=False)
    Municipal = forms.CharField(required=False)
    Cell = forms.IntegerField(required=False)
    AccuracyGPS = forms.DecimalField(required=False)

    class Meta:
        model = Category3
        fields = ('Category3Subject', 'Certainty', 'Category3Feature1', 'Category3Feature2', 'ObservationDate', 'Photo',
                  'Lat', 'Lon', 'Position', 'AccuracyGPS'
                  )

    def clean(self):
        cleaned_data = super().clean()

        point = Point(float(cleaned_data.get('Lat')), float(cleaned_data.get('Lon')))
        if not is_point_in_bavaria(point=point):
            raise ValidationError("The selected point is not located in Bavaria!")
        return cleaned_data


class Category4Form(forms.ModelForm):
    Certainty = forms.ChoiceField(widget=forms.RadioSelect(), choices=CERTAINTY_CHOICES, label='Certainty')
    Category4Feature1 = forms.ChoiceField(widget=forms.RadioSelect(), choices=YESNO_CHOICES, label='Category4Feature1')
    Category4Feature2 = forms.ChoiceField(widget=forms.RadioSelect(), choices=YESNO_CHOICES, label='Category4Feature2')
    Category4Feature3 = forms.ChoiceField(widget=forms.RadioSelect(), choices=YESNO_CHOICES, label='Category4Feature3')

    Lat = forms.DecimalField(
        widget=forms.NumberInput(attrs={'step': '0.000001', 'placeholder': '00.000000'}), label='Latitude')
    Lon = forms.DecimalField(
        widget=forms.NumberInput(attrs={'step': '0.000001', 'placeholder': '00.000000'}), label='Longitude')
    ClimateStation = forms.IntegerField(required=False)
    Municipal = forms.CharField(required=False)
    Cell = forms.IntegerField(required=False)
    AccuracyGPS = forms.DecimalField(required=False)

    class Meta:
        model = Category4
        fields = (
            'Category4Subject', 'Certainty', 'Category4Feature1',
            'Category4Feature2', 'Category4Feature3',
            'Lat', 'Lon', 'Position', 'ClimateStation', 'Municipal', 'Cell', 'ObservationDate', 'Photo', 'AccuracyGPS'
        )

    def clean(self):
        cleaned_data = super().clean()
        point = Point(float(cleaned_data.get('Lat')), float(cleaned_data.get('Lon')))
        if not is_point_in_bavaria(point=point):
            raise ValidationError("The selected point is not located in Bavaria!")
        return cleaned_data
