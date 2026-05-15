from ai_engine.core.runtime_manager import RuntimeManager
from ai_engine.core.state_manager import StateManager
from ai_engine.core.event_dispatcher import EventDispatcher

from ai_engine.core.workflow_engine import WorkflowEngine

from ai_engine.queue_ai.queue_builder import QueueBuilder
from ai_engine.queue_ai.queue_optimizer import QueueOptimizer
from ai_engine.queue_ai.queue_balancer import QueueBalancer

from ai_engine.prediction_ai.queue_time_estimator import (
    QueueTimeEstimator
)

from ai_engine.prediction_ai.wait_time_predictor import (
    WaitTimePredictor
)

from ai_engine.realtime_ai.realtime_sync_manager import (
    RealtimeSyncManager
)

from ai_engine.realtime_ai.realtime_event_processor import (
    RealtimeEventProcessor
)

from ai_engine.patient_ai.patient_priority_engine import (
    PatientPriorityEngine
)

from ai_engine.doctor_ai.doctor_availability_engine import (
    DoctorAvailabilityEngine
)

from ai_engine.ml.pipelines.inference_pipeline import (
    InferencePipeline
)

from ai_engine.ml.pipelines.realtime_pipeline import (
    RealtimePipeline
)

from ai_engine.monitoring.system_monitor import (
    SystemMonitor
)

from ai_engine.analytics_ai.hospital_insights_ai import (
    HospitalInsightsAI
)

from ai_engine.analytics_ai.queue_analytics_engine import (
    QueueAnalyticsEngine
)

from ai_engine.optimization_ai.realtime_decision_engine import (
    RealtimeDecisionEngine
)


class AIQueueEngine:

    def __init__(self):

        self.runtime_manager = RuntimeManager()
        self.state_manager = StateManager()
        self.event_dispatcher = EventDispatcher()

        self.patient_priority_engine = PatientPriorityEngine()
        self.doctor_availability_engine = DoctorAvailabilityEngine()

        self.queue_builder = QueueBuilder(
            self.state_manager
        )

        self.queue_optimizer = QueueOptimizer()
        self.queue_balancer = QueueBalancer()

        self.queue_estimator = QueueTimeEstimator()
        self.wait_time_predictor = WaitTimePredictor()

        self.realtime_sync_manager = RealtimeSyncManager()

        self.realtime_event_processor = (
            RealtimeEventProcessor(
                self.realtime_sync_manager,
                self.event_dispatcher
            )
        )

        self.workflow_engine = WorkflowEngine(
            self.state_manager,
            self.doctor_availability_engine,
            self.queue_builder,
            self.wait_time_predictor
        )

        self.inference_pipeline = InferencePipeline()
        self.realtime_pipeline = RealtimePipeline()

        self.system_monitor = SystemMonitor()
        self.hospital_insights_ai = HospitalInsightsAI()
        self.queue_analytics_engine = QueueAnalyticsEngine()
        self.realtime_decision_engine = RealtimeDecisionEngine()

    # =====================================================
    # BOOT ENGINE
    # =====================================================

    def boot(self):

        self.runtime_manager.start()

        return {
            "engine": "PredictQ AI Engine",
            "status": "BOOTED"
        }

    # =====================================================
    # CREATE DEPARTMENT
    # =====================================================

    def create_department(
        self,
        department_name: str
    ):

        self.state_manager.create_department(
            department_name
        )

        return {
            "created": True,
            "department": department_name
        }

    # =====================================================
    # REGISTER DOCTOR
    # =====================================================

    def register_doctor(
        self,
        doctor_id: str,
        name: str,
        department: str
    ):

        self.doctor_availability_engine.register_doctor(
            doctor_id,
            name,
            department
        )

        return {
            "registered": True,
            "doctor_id": doctor_id,
            "name": name,
            "department": department
        }

    # =====================================================
    # REGISTER PATIENT
    # =====================================================

    def register_patient(
        self,
        department: str,
        patient_data: dict
    ):

        patient_data = (
            self.patient_priority_engine
            .enrich_patient_priority(
                patient_data
            )
        )

        queue = self.queue_builder.enqueue_patient(
            department,
            patient_data
        )

        self.event_dispatcher.dispatch(
            "PATIENT_REGISTERED",
            patient_data
        )

        self.event_dispatcher.dispatch(
            "QUEUE_UPDATED",
            {
                "department": department,
                "queue_size": len(queue)
            }
        )

        self.realtime_sync_manager.sync_department_queue(
            department,
            queue
        )

        return queue

    # =====================================================
    # ADVANCED WORKFLOW REGISTRATION
    # =====================================================

    def register_patient_workflow(
        self,
        department: str,
        patient_data: dict
    ):

        result = (
            self.workflow_engine
            .process_patient_registration(
                department,
                patient_data
            )
        )

        queue = self.state_manager.get_department_queue(
            department
        )

        self.realtime_event_processor.process_queue_update(
            department,
            queue
        )

        return result

    # =====================================================
    # CALL NEXT PATIENT
    # =====================================================

    def call_next_patient(
        self,
        department: str
    ):

        patient = self.queue_builder.dequeue_patient(
            department
        )

        self.event_dispatcher.dispatch(
            "PATIENT_CALLED",
            patient
        )

        self.realtime_sync_manager.sync_department_queue(
            department,
            self.state_manager.get_department_queue(
                department
            )
        )

        return patient

    # =====================================================
    # ADVANCED NEXT PATIENT WORKFLOW
    # =====================================================

    def call_next_patient_workflow(
        self,
        department: str
    ):

        result = (
            self.workflow_engine
            .process_next_patient(
                department
            )
        )

        queue = self.state_manager.get_department_queue(
            department
        )

        self.realtime_event_processor.process_queue_update(
            department,
            queue
        )

        return result

    # =====================================================
    # COMPLETE CONSULTATION
    # =====================================================

    def complete_consultation(
        self,
        doctor_id: str,
        patient_id: str
    ):

        return (
            self.workflow_engine
            .complete_consultation(
                doctor_id,
                patient_id
            )
        )

    # =====================================================
    # BASIC ETA ESTIMATION
    # =====================================================

    def estimate_wait_time(
        self,
        queue_position: int
    ):

        return self.queue_estimator.estimate(
            queue_position,
            avg_consultation_time=10
        )

    # =====================================================
    # DEPARTMENT WAIT PREDICTION
    # =====================================================

    def predict_department_wait_time(
        self,
        department: str
    ):

        queue = self.state_manager.get_department_queue(
            department
        )

        available_doctors = (
            self.doctor_availability_engine
            .get_available_doctors(
                department
            )
        )

        return self.wait_time_predictor.predict_wait_time(
            queue_size=len(queue),
            available_doctors=len(available_doctors)
        )

    # =====================================================
    # DIRECT WAIT PREDICTION
    # =====================================================

    def predict_wait_time(
        self,
        queue_size: int,
        available_doctors: int,
        avg_consultation_time: int = 10
    ):

        return self.wait_time_predictor.predict_wait_time(
            queue_size=queue_size,
            available_doctors=available_doctors,
            avg_consultation_time=avg_consultation_time
        )

    # =====================================================
    # RUN INFERENCE PIPELINE
    # =====================================================

    def run_inference_pipeline(
        self,
        payload: dict
    ):

        return self.inference_pipeline.run_pipeline(
            payload
        )

    # =====================================================
    # RUN REALTIME PIPELINE
    # =====================================================

    def run_realtime_pipeline(
        self,
        patient_data: dict
    ):

        return self.realtime_pipeline.process_realtime_data(
            patient_data
        )

    # =====================================================
    # DEPARTMENT SNAPSHOT
    # =====================================================

    def get_department_snapshot(
        self,
        department: str
    ):

        return (
            self.workflow_engine
            .get_department_snapshot(
                department
            )
        )

    # =====================================================
    # REALTIME SNAPSHOT
    # =====================================================

    def get_realtime_snapshot(
        self,
        department: str
    ):

        return (
            self.realtime_sync_manager
            .get_live_snapshot(
                department
            )
        )

    # =====================================================
    # MONITOR SYSTEM
    # =====================================================

    def monitor_system(
        self,
        queue_size: int,
        available_doctors: int
    ):

        return (
            self.system_monitor
            .generate_monitoring_report(
                queue_size,
                available_doctors
            )
        )

    # =====================================================
    # HOSPITAL INSIGHTS
    # =====================================================

    def generate_hospital_insights(
        self,
        department_data: dict
    ):

        return (
            self.hospital_insights_ai
            .generate_hospital_insights(
                department_data
            )
        )

    # =====================================================
    # QUEUE ANALYTICS
    # =====================================================

    def generate_queue_analytics(
        self,
        department: str,
        wait_times: list
    ):

        queue = self.state_manager.get_department_queue(
            department
        )

        return (
            self.queue_analytics_engine
            .analyze_department(
                department,
                queue,
                wait_times
            )
        )

    # =====================================================
    # REALTIME DECISIONS
    # =====================================================

    def generate_realtime_decisions(
        self,
        department_data: dict
    ):

        return (
            self.realtime_decision_engine
            .generate_realtime_decisions(
                department_data
            )
        )

    # =====================================================
    # SYSTEM SUMMARY
    # =====================================================

    def system_summary(self):

        return (
            self.workflow_engine
            .system_summary()
        )