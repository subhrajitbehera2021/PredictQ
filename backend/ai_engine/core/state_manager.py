from typing import Dict, List
  
  
class StateManager:

    def __init__(self):
        self.departments: Dict[str, List[dict]] = {}
        self.active_patients = {}
        self.active_doctors = {}

    def create_department(self, department_name: str):
        if department_name not in self.departments:
            self.departments[department_name] = []

    def get_department_queue(self, department_name: str):
        return self.departments.get(department_name, [])

    def add_patient(self, department_name: str, patient_data: dict):
        self.departments[department_name].append(patient_data)

    def remove_patient(self, department_name: str, patient_id: str):
        queue = self.departments[department_name]
    
        self.departments[department_name] = [
          p for p in queue
          if p["patient_id"] != patient_id
      ]