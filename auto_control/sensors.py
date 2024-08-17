class Sensors:
    @staticmethod
    def detect_environment():
        # Simulate simple environmental detection
        return np.random.choice(["threat_detected", "food_detected", "nothing_detected"])
