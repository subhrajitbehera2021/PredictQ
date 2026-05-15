from apps.hospitals.models import Hospital


class HospitalService:

    @staticmethod
    def create_hospital(validated_data, user):

        return Hospital.objects.create(
            hospital_admin=user,
            **validated_data
        )

    @staticmethod
    def update_hospital(instance, validated_data):

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    @staticmethod
    def deactivate_hospital(instance):

        instance.is_active = False
        instance.save()
        return instance