def main():
    """Get the score and display the status"""
    score = float(input("Enter score: "))
    print(determine_status(score))


def determine_status(score):
    """Determine the status from the score given"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
