from rest_framework import serializers

from .models import Category4, Category3, Category2, Category1


class Category1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category1
        fields = ('id', 'Category1Subject', 'Certainty', 'Number', 'Category1Feature1', 'Category1Feature2',
                  'Category1Feature3', 'ObservationDate', 'ObservationTime', 'Photo', 'Lat', 'Lon', 'Municipal',
                  'Position', 'AccuracyGPS')
        write_only_fields = (
            'ClimateStation', 'Cell', 'Position', 'geom'
        )


class Category2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category2
        fields = (
            'id', 'Category2Subject', 'Certainty', 'Category2Feature1', 'Category2Feature2', 'Category2Feature3',
            'Category2Feature4', 'Category2Feature5', 'Category2Feature6', 'Category2Feature7', 'Category2Feature8',
            'Lat', 'Lon', 'Municipal', 'ObservationDate', 'Photo', 'AccuracyGPS', 'Position', )
        write_only_fields = (
            'ClimateStation', 'Cell', 'geom', 'Position'
        )


class Category3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category3
        fields = (
            'id', 'Category3Subject', 'Certainty', 'Category3Feature1', 'Category3Feature2', 'ObservationDate', 'Photo',
            'Lat', 'Lon', 'Municipal', 'AccuracyGPS', 'Position',
        )
        write_only_fields = (
            'ClimateStation', 'Cell', 'geom', 'Position',
        )


class Category4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category4
        fields = (
            'id', 'Category4Subject', 'Certainty', 'Category4Feature1', 'Category4Feature2', 'Category4Feature3',
            'Lat', 'Lon', 'Municipal', 'ObservationDate', 'Photo', 'Position', 'AccuracyGPS')
        write_only_fields = (
            'ClimateStation', 'Cell', 'geom', 'Position'
        )


