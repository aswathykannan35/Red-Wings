def check_eligibility(age, weight, hemoglobin):
    if age >= 18 and weight >= 50 and hemoglobin >= 12.5:
        return True
    else:
        return False
