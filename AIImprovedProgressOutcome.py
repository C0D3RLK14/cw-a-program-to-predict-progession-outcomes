from typing import List, Literal

# Define constants for credit values and outcome messages
VALID_CREDITS = [0, 20, 40, 60, 80, 100, 120]
TOTAL_CREDITS = 120

ProgressOutcomeType = Literal["Progress", "Progress (module trailer)", "Do not Progress – module retriever", "Exclude"]

def progress_outcome(pass_credit: int, defer_credit: int, fail_credit: int) -> ProgressOutcomeType:
    """
    Determine the progression outcome based on the credits.
    
    Args:
        pass_credit (int): The number of pass credits
        defer_credit (int): The number of defer credits
        fail_credit (int): The number of fail credits
        
    Returns:
        str: The progression outcome
        
    Raises:
        Exception: If the credit combination is invalid
    """
    # Progress outcome
    if pass_credit == TOTAL_CREDITS and defer_credit == 0 and fail_credit == 0:
        return "Progress"
    
    # Progress (module trailer) outcomes
    if pass_credit == 100 and (defer_credit == 20 or fail_credit == 20):
        return "Progress (module trailer)"
    
    # Exclude outcomes - when fail credits are too high
    if fail_credit >= 80:
        return "Exclude"
    
    # Do not Progress – module retriever for all other valid combinations
    if pass_credit + defer_credit + fail_credit == TOTAL_CREDITS:
        return "Do not Progress – module retriever"
        
    raise Exception("Invalid credit combination.")

def validate_credit_range(credit: int) -> int:
    """
    Validate if the credit value is within the allowed range.
    
    Args:
        credit (int): The credit value to validate
        
    Returns:
        int: The validated credit value
        
    Raises:
        Exception: If the credit value is not in the valid range
    """
    if credit in VALID_CREDITS:
        return credit
    raise Exception("Credits must be one of these values: 0, 20, 40, 60, 80, 100, 120")

def validate_total_credits(pass_credit: int, defer_credit: int, fail_credit: int) -> None:
    """
    Validate if the total credits sum up to the required total.
    
    Args:
        pass_credit (int): The number of pass credits
        defer_credit (int): The number of defer credits
        fail_credit (int): The number of fail credits
        
    Raises:
        Exception: If the total credits do not sum up to 120
    """
    if pass_credit + defer_credit + fail_credit != TOTAL_CREDITS:
        raise Exception(f"Total credits must be {TOTAL_CREDITS}.")

def main():
    """Main program loop for the student progression outcome prediction system."""
    progress_outcomes: List[str] = []
    outcome_counts = {
        "Progress": 0,
        "Progress (module trailer)": 0,
        "Do not Progress – module retriever": 0,
        "Exclude": 0
    }

    while True:
        # Input and validation loop
        while True:
            try:
                pass_credit = validate_credit_range(int(input("Enter your pass credits: ")))
                defer_credit = validate_credit_range(int(input("Enter your defer credits: ")))
                fail_credit = validate_credit_range(int(input("Enter your fail credits: ")))
                
                validate_total_credits(pass_credit, defer_credit, fail_credit)
                print()  # Add blank line for readability
                break
                
            except ValueError:
                print("Integers required\n")
            except Exception as ex:
                print(f"{ex}\n")

        # Process outcome
        current_outcome = progress_outcome(pass_credit, defer_credit, fail_credit)
        print(current_outcome)
        
        progress_outcomes.append(current_outcome)
        outcome_counts[current_outcome] += 1
        print()

        # Prompt for continuation
        while True:
            print("Would you like to enter another set of data?")
            choice = input("Enter 'y' for yes or 'q' to quit and view results: ").lower()
            
            if choice == 'q':
                display_results(progress_outcomes, outcome_counts)
                return
            if choice == 'y':
                print()
                break
            print("Invalid input. Please try again.\n")

def display_results(outcomes: List[str], counts: dict) -> None:
    """
    Display the final results of all progression outcomes.
    
    Args:
        outcomes (List[str]): List of all progression outcomes
        counts (dict): Dictionary containing counts of each outcome type
    """
    print()
    print(outcomes)
    print()
    print(f"""Progress outcomes: {counts['Progress']}
Progress (module trailer): {counts['Progress (module trailer)']}
Do not Progress – module retriever: {counts['Do not Progress – module retriever']}
Exclude: {counts['Exclude']}""")
    print()
    print("Program quit successfully.")
    print()

if __name__ == "__main__":
    main()