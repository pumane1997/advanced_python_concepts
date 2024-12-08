
class CalorieCalculator:
    ''' Calorie Calculator based on gender, age, height, weight, activity level, and 
    temperature. '''

    def __init__(self, gender, age, height, weight, activity, temperature):
        self.gender = gender  # 'male' or 'female'
        self.age = age        # in years
        self.height = height  # in cm
        self.weight = weight  # in kg
        self.activity = activity  # 1 (sedentary) to 5 (super active)
        self.temperature = temperature  # in degrees Celsius

    def calculateCalories(self):
        # Step 1: Calculate BMR using Mifflin-St Jeor Equation
        if self.gender.lower() == 'male':
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        else:  # Assuming gender is female for other cases
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161

        # Step 2: Activity adjustment using activity factor
        activity_factors = {
            1: 1.2,    # Sedentary (little or no exercise)
            2: 1.375,  # Lightly active (light exercise 1-3 days/week)
            3: 1.55,   # Moderately active (moderate exercise 3-5 days/week)
            4: 1.725,  # Very active (hard exercise 6-7 days/week)
            5: 1.9     # Super active (intense physical activity or job)
        }

        activity_factor = activity_factors.get(self.activity, 1.2)  # Default to sedentary if invalid

        tdee = bmr * activity_factor  # Total Daily Energy Expenditure

        # Step 3: Temperature adjustment
        # Hot climates (>= 30°C): Increase TDEE by 3%
        # Cold climates (<= 10°C): Increase TDEE by 5%
        if self.temperature >= 30:
            temperature_factor = 1.03  # Hot climate
        elif self.temperature <= 10:
            temperature_factor = 1.05  # Cold climate
        else:
            temperature_factor = 1.0  # Moderate climate

        # Step 4: Adjusted maintenance calories
        maintenance_calories = tdee * temperature_factor

        return round(maintenance_calories, 2)


# my_cals = CalorieCalculator('male', 28, 170, 74, 2, 30).calculateCalories()
# print(my_cals)