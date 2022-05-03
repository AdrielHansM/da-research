def print_string(string):
    print(string)

def get_age_range(age):
    if age < 36 :   return 0 #UnderWeight
    elif age > 35 and age  < 41:   return 1 #NormalWeight
    elif age > 40 and age < 46:  return 2 #OverWeight
    elif age > 45 and age < 51:  return 3 #ClassObesity_1
    elif age > 50 and age < 56:  return 4 #ClassObesity_2
    elif age > 55 and age < 61:  return 5 #ClassObesity_2
    elif age > 61:  return 6 #ClassObesity_3

def get_bmi_class(bmi):
    if bmi < 18.5 :   return 0 #UnderWeight
    elif bmi > 18.5 and bmi  < 24.9:   return 1 #NormalWeight
    elif bmi > 24.9 and bmi < 29.9:  return 2 #OverWeight
    elif bmi > 29.9 and bmi < 34.9:  return 3 #ClassObesity_1
    elif bmi > 34.9 and bmi < 39.9:  return 4 #ClassObesity_2
    elif bmi > 39.9:  return 5 #ClassObesity_3

def get_map_class(diastolic):
    if diastolic < 79.9: return 0 #Normal
    elif diastolic > 79.9 and diastolic < 89.9:  return 1 #Normal
    elif diastolic > 89.9 and diastolic < 99.9:  return 2 #Normal
    elif diastolic > 99.9 and diastolic < 109.9:  return 3 #High
    elif diastolic > 109.9 and diastolic < 119.9:  return 4 #Normal
    elif diastolic > 119.9:  return 5 #High

def get_cholesterol_class(cholesterol):
    if cholesterol < 201: return 0 #Normal
    elif cholesterol > 200 and cholesterol < 240:  return 1 #High
    elif cholesterol > 239: return 2 #High

def get_glucose_class(glucose):
    if glucose < 101: return 0 #Normal
    elif glucose > 100 and glucose < 126:  return 1 #High
    elif glucose > 125: return 2 #High Requires medical attention