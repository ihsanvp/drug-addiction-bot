class AddictionDetector:
    def __init__(self):
        self.stages = {
            'Stage 1': 'Mild addiction',
            'Stage 2': 'Moderate addiction',
            'Stage 3': 'Severe addiction',
            'Stage 4': 'Critical addiction'
        }

        # Define thresholds for each stage based on the number of 'Yes' answers
        self.thresholds = {
            'Stage 1': (0, 1),  # Between 0 and 1 'Yes' answers
            'Stage 2': (2, 5),  # Between 2 and 5 'Yes' answers
            'Stage 3': (6, 8),  # Between 6 and 8 'Yes' answers
            'Stage 4': (9, 11)  # Between 9 and 11 'Yes' answers
        }

    def detect_addiction_stage(self, user_answers):
        yes_count = sum(answer == 'yes' for answer in user_answers)
        for stage, (lower, upper) in self.thresholds.items():
            if lower <= yes_count <= upper:
                return stage
        # If no stage is detected, return the highest stage
        return 'Stage 4'

class RecommendationSystem:
    def __init__(self):
        self.solutions = {
            'Stage 1': ['Join a support group', 'Seek counseling'],
            'Stage 2': ['Therapy sessions', 'Behavioral interventions'],
            'Stage 3': ['Inpatient rehabilitation', 'Medication-assisted treatment'],
            'Stage 4': ['Immediate medical attention required. Seek help at nearest hospital']
        }

    def recommend_solution(self, stage):
        return self.solutions.get(stage, ['No recommendation available'])