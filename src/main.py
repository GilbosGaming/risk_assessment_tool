class RiskAssessment:
    """Handle risk assessment calculations and data management."""
    
    def __init__(self):
        """Initialize the risk assessment tool."""
        self.assessment_data = {}

    def get_offender_details(self):
        """Collect offender details from user input."""
        print("=== Offender Risk Assessment Tool ===")
        
        name = input("Enter offender name: ")
        while True:
            try:
                age = int(input("Enter age: "))
                if 18 <= age <= 100:  # Basic validation
                    break
                print("Please enter a valid age between 18 and 100")
            except ValueError:
                print("Please enter a valid number")
        
        self.assessment_data.update({
            "name": name,
            "age": age
        })

def main():
    """Main program entry point."""
    tool = RiskAssessment()
    tool.get_offender_details()

if __name__ == "__main__":
    main()