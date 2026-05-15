from rest_framework import serializers
from apps.analytics.models import HospitalAnalytics, DoctorAnalytics


class HospitalAnalyticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = HospitalAnalytics
        fields = "__all__"


class DoctorAnalyticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorAnalytics
        fields = "__all__"