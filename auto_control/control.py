class RobotControl:
    def __init__(self):
        self.state = "Idle"

    def act(self, environment_input):
        # Simple state-based decision-making (can be expanded)
        if environment_input == "threat_detected":
            self.state = "Defense"
        elif environment_input == "food_detected":
            self.state = "Gather"
        else:
            self.state = "Idle"
        return self.state
