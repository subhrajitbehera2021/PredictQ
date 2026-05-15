from apps.staff_management.models import Staff


class StaffService:

    @staticmethod
    def create_staff(validated_data):
        return Staff.objects.create(**validated_data)

    @staticmethod
    def update_staff(instance, validated_data):

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    @staticmethod
    def deactivate_staff(staff):
        staff.is_active = False
        staff.save()
        return staff