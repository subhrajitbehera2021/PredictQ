from django.db.models import Count, Avg, F
from apps.bookings.models import Booking
from apps.queue_management.models import Queue
from apps.doctors.models import Doctor
from apps.hospitals.models import Hospital


class AnalyticsService:

    # --------------------------------------------------
    # 🏥 HOSPITAL LEVEL ANALYTICS
    # --------------------------------------------------
    @staticmethod
    def generate_hospital_analytics(hospital):

        total_patients = Booking.objects.filter(
            hospital=hospital
        ).count()

        total_doctors = Doctor.objects.filter(
            hospital=hospital
        ).count()

        avg_wait_time = Queue.objects.filter(
            hospital=hospital
        ).aggregate(
            avg=Avg("estimated_wait_time")
        )["avg"] or 0

        completed_cases = Queue.objects.filter(
            hospital=hospital,
            status="COMPLETED"
        ).count()

        pending_cases = Queue.objects.filter(
            hospital=hospital,
            status="WAITING"
        ).count()

        return {
            "hospital_id": str(hospital.id),
            "hospital_name": hospital.name,
            "total_patients": total_patients,
            "total_doctors": total_doctors,
            "completed_cases": completed_cases,
            "pending_cases": pending_cases,
            "avg_wait_time": round(avg_wait_time, 2),
        }

    # --------------------------------------------------
    # 👨‍⚕️ DOCTOR LEVEL ANALYTICS
    # --------------------------------------------------
    @staticmethod
    def generate_doctor_analytics(doctor):

        total_patients = Booking.objects.filter(
            doctor=doctor
        ).count()

        completed_queue = Queue.objects.filter(
            doctor=doctor,
            status="COMPLETED"
        ).count()

        avg_wait_time = Queue.objects.filter(
            doctor=doctor
        ).aggregate(
            avg=Avg("estimated_wait_time")
        )["avg"] or 0

        return {
            "doctor_id": str(doctor.id),
            "doctor_name": doctor.user.username,
            "total_patients": total_patients,
            "completed_cases": completed_queue,
            "avg_wait_time": round(avg_wait_time, 2),
        }

    # --------------------------------------------------
    # 📈 SYSTEM-WIDE ANALYTICS
    # --------------------------------------------------
    @staticmethod
    def generate_system_analytics():

        total_hospitals = Hospital.objects.count()
        total_doctors = Doctor.objects.count()
        total_bookings = Booking.objects.count()
        total_queue_entries = Queue.objects.count()

        active_queues = Queue.objects.filter(status="WAITING").count()

        completed_queues = Queue.objects.filter(status="COMPLETED").count()

        return {
            "total_hospitals": total_hospitals,
            "total_doctors": total_doctors,
            "total_bookings": total_bookings,
            "total_queue_entries": total_queue_entries,
            "active_queues": active_queues,
            "completed_queues": completed_queues,
        }