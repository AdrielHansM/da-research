def compute_mean_arterial_pressure(systolic, diastolic):
    return ((2 * diastolic) + systolic) / 3

def compute_bmi(weight, height):
    return weight / (height/100)**2

def get_age_class(age):
    if age < 36 :   return 0 
    elif age > 35 and age  < 41:   return 1 
    elif age > 40 and age < 46:  return 2 
    elif age > 45 and age < 51:  return 3 
    elif age > 50 and age < 56:  return 4 
    elif age > 55 and age < 61:  return 5 
    elif age > 61:  return 6 

def get_bmi_class(bmi):
    if bmi < 18.5 :   return 0 #UnderWeight
    elif bmi > 18.5 and bmi  < 24.9:   return 1 #NormalWeight
    elif bmi > 24.9 and bmi < 29.9:  return 2 #OverWeight
    elif bmi > 29.9 and bmi < 34.9:  return 3 #ClassObesity_1
    elif bmi > 34.9 and bmi < 39.9:  return 4 #ClassObesity_2
    elif bmi > 39.9:  return 5 #ClassObesity_3

def get_map_class(mean_arterial_pressure):
    if mean_arterial_pressure < 70: return 0 #Low
    elif mean_arterial_pressure > 69 and mean_arterial_pressure < 101:  return 1 #Normal
    elif mean_arterial_pressure > 100 and mean_arterial_pressure < 111:  return 2 #Elevated
    elif mean_arterial_pressure > 110 and mean_arterial_pressure < 121:  return 3 #Risk of Hypertension 1
    elif mean_arterial_pressure > 120 and mean_arterial_pressure < 131:  return 4 #Risk of Hypertension 2
    elif mean_arterial_pressure > 130:  return 5 #Emergency Care Needed

def get_cholesterol_class(cholesterol):
    if cholesterol < 201: return 0 #Normal
    elif cholesterol > 200 and cholesterol < 240:  return 1 #Medium
    elif cholesterol > 239: return 2 #High

def get_glucose_class(glucose):
    if glucose < 101: return 0 #Normal
    elif glucose > 100 and glucose < 126:  return 1 #Medium
    elif glucose > 125: return 2 #High

def get_health_status(bmi_class, map_class, cholesterol_class, glucose_class, cvd_prediction, diabetes_prediction):
    health_status = {}

    health_status['bmi_status'] = ("Underweight" if bmi_class == '0' 
    else "Normal" if bmi_class == '1'
    else "Overweight" if bmi_class == '2'
    else "Obesity Class 1" if bmi_class == '3'
    else "Obesity Class 2" if bmi_class == '4'
    else "Obesity Class 3")
    
    health_status['map_status'] = ("Low" if map_class == '0' 
    else "Normal" if map_class == '1' 
    else "Elevated" if map_class == '2' 
    else "Risk of hypertension 1" if map_class == '3' 
    else "Risk of hypertension 2" if map_class == '4' 
    else "Requires Emergency Care")

    health_status['glucose_status'] = "Normal" if glucose_class == '0' else "Borderline High" if glucose_class == '1' else "High"

    health_status['cholesterol_status'] = ("Normal" if cholesterol_class == '0' else "Borderline High" if cholesterol_class == '1' 
    else "High")

    health_status['cvd_risk'] = "Low Risk" if cvd_prediction == '0' else "High Risk"

    health_status['diabetes_risk'] = "Low Risk" if diabetes_prediction == '0' else "High Risk"

    return health_status