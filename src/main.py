class RiskAssessment:
    """Handle risk assessment calculations and data management."""
    
    def __init__(self):
        """Initialize the risk assessment tool."""
        self.assessment_data = {}

    # Age input loop
    while True:
        try:
            age = int(input("Enter age: "))
            if 18 <= age <= 100:  # Basic validation
                break
            print("Please enter a valid age between 18 and 100")
        except ValueError:
            print("Please enter a valid number")
    
    # Previous convictions input loop
    while True:
        try:
            previous_convictions = int(input("Enter number of previous convictions: "))
            if previous_convictions >= 0:
                # Here's where we update the dictionary with new information
                self.risk_factors["previous_convictions"] = previous_convictions
                break
            print("Please enter a valid number of convictions")
        except ValueError:
            print("Please enter a valid number")
        
        self.assessment_data.update({
            "name": name,
            "age": age,
            "previous_convictions": previous_convictions
        })

def main():
    """Main program entry point."""
    tool = RiskAssessment()
    tool.get_offender_details()

if __name__ == "__main__":
    main()

risk_factors = {
    "previous_convictions": 0,
    "age_at_first_offense": 0,
    "substance_use": False,
    "employment_status": "unemployed",
    "stable_housing": True
}