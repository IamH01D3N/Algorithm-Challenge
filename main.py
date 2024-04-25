# This program checks what scholarship you can get based off of your GPA and SAT score

def check_scholarship_eligibility(gpa, sat_score, extracurricular_activities):
    if gpa >= 3.5 and sat_score >= 1300 and extracurricular_activities >= 3:
        return "top-tier"
    elif gpa >= 3.0 and sat_score >= 1200 or extracurricular_activities >= 2:
        return "mid-tier"
    elif gpa >= 2.5 or sat_score >= 1100:
        return "basic"
    else:
        return "not eligible"

def main():
    print("Welcome to the Scholarship Eligibility Checker!")
    gpa = float(input("Enter your GPA: "))
    sat_score = int(input("Enter your SAT score: "))
    extracurricular_activities = int(input("Enter the number of extracurricular activities: "))
    
    eligibility = check_scholarship_eligibility(gpa, sat_score, extracurricular_activities)
    if eligibility != "not eligible":
        print(f"Congratulations! You are eligible for the {eligibility} scholarship.")
    else:
        print("Sorry, you are not eligible for any scholarship at this time.")

if __name__ == "__main__":
    main()
