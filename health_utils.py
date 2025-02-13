def calculate_bmi(height, weight):
    """Calculate Body Mass Index (BMI) given height in meters and weight in kilograms."""
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be greater than zero.")
    return round(weight / (height ** 2), 2)


def calculate_bmr(height, weight, age, gender):
    """Calculate Basal Metabolic Rate (BMR) using the Harris-Benedict equation."""
    if height <= 0 or weight <= 0 or age <= 0:
        raise ValueError("Height, weight, and age must be greater than zero.")
    
    height_in_cm = height * 100  # Convert height to centimeters
    
    if gender.lower() == "male":
        return round(88.36 + (13.4 * weight) + (4.8 * height_in_cm) - (5.7 * age), 2)
    elif gender.lower() == "female":
        return round(447.6 + (9.2 * weight) + (3.1 * height_in_cm) - (4.3 * age), 2)
    else:
        raise ValueError("Gender must be 'male' or 'female'.")