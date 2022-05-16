class Patient:
    def __init__(self, cluster, age, gender, glucose, cholesterol, systolic_bp, diastolic_bp, mean_arterial_pressure, pregnancies, skin_thickness, insulin, bmi, dpf, age_class, bmi_class, map_class, cholesterol_class, glucose_class, smoke, active, cvd_prediction, diabetes_prediction):
        self.__cluster = cluster    # KModes cluster of the patient
        self.__age = age    # age of the patient
        self.__gender = gender    # gender 0 for female and 1 for male
        self.__glucose = glucose    # glucose level
        self.__cholesterol = cholesterol    # cholesterol level
        self.__systolic_bp = systolic_bp    # systolic blood pressure
        self.__diastolic_bp = diastolic_bp    # diastolic blood pressure
        self.__mean_arterial_pressure = mean_arterial_pressure    # Mean arterial pressure
        self.__pregnancies = pregnancies    # Number of pregnancies
        self.__skin_thickness = skin_thickness    # Thickness of skin fold
        self.__insulin = insulin    # Insulin level
        self.__bmi = bmi    # Body mass index
        self.__dpf = dpf    # Diabetes pedigree function
        self.__age_class = age_class    # Age class or Age range
        self.__bmi_class = bmi_class    # BMI class
        self.__map_class = map_class    # MAP class
        self.__cholesterol_class = cholesterol_class    # Cholesterol class
        self.__glucose_class = glucose_class    # Glucose class
        self.__smoke = smoke    # 1 if the patient smokes
        self.__active = active    # Active or physically active
        self.__cvd_prediction = cvd_prediction    # Cardiovascular Disease Prediction
        self.__diabetes_prediction = diabetes_prediction    # Diabetes Prediction

    def __init__(self):
        pass

    @property
    def cluster(self):
        return self.__cluster

    @cluster.setter
    def cluster(self, cluster):
        self.__cluster = cluster

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def glucose(self):
        return self.__glucose

    @glucose.setter
    def glucose(self, glucose):
        self.__glucose = glucose

    @property
    def cholesterol(self):
        return self.__cholesterol

    @cholesterol.setter
    def cholesterol(self, cholesterol):
        self.__cholesterol = cholesterol

    @property
    def systolic_bp(self):
        return self.__systolic_bp

    @systolic_bp.setter
    def systolic_bp(self, systolic_bp):
        self.__systolic_bp = systolic_bp

    @property
    def diastolic_bp(self):
        return self.__diastolic_bp

    @diastolic_bp.setter
    def diastolic_bp(self, diastolic_bp):
        self.__diastolic_bp = diastolic_bp

    @property
    def mean_arterial_pressure(self):
        return self.__mean_arterial_pressure

    @mean_arterial_pressure.setter
    def mean_arterial_pressure(self, mean_arterial_pressure):
        self.__mean_arterial_pressure = mean_arterial_pressure

    @property
    def pregnancies(self):
        return self.__pregnancies

    @pregnancies.setter
    def pregnancies(self, pregnancies):
        self.__pregnancies = pregnancies

    @property
    def skin_thickness(self):
        return self.__skin_thickness

    @skin_thickness.setter
    def skin_thickness(self, skin_thickness):
        self.__skin_thickness = skin_thickness

    @property
    def insulin(self):
        return self.__insulin

    @insulin.setter
    def insulin(self, insulin):
        self.__insulin = insulin

    @property
    def bmi(self):
        return self.__bmi

    @bmi.setter
    def bmi(self, bmi):
        self.__bmi = bmi

    @property
    def dpf(self):
        return self.__dpf

    @dpf.setter
    def dpf(self, dpf):
        self.__dpf = dpf

    @property
    def age_class(self):
        return self.__age_class

    @age_class.setter
    def age_class(self, age_class):
        self.__age_class = age_class

    @property
    def bmi_class(self):
        return self.__bmi_class

    @bmi_class.setter
    def bmi_class(self, bmi_class):
        self.__bmi_class = bmi_class

    @property
    def map_class(self):
        return self.__map_class

    @map_class.setter
    def map_class(self, map_class):
        self.__map_class = map_class

    @property
    def cholesterol_class(self):
        return self.__cholesterol_class

    @cholesterol_class.setter
    def cholesterol_class(self, cholesterol_class):
        self.__cholesterol_class = cholesterol_class

    @property
    def glucose_class(self):
        return self.__glucose_class

    @glucose_class.setter
    def glucose_class(self, glucose_class):
        self.__glucose_class = glucose_class

    @property
    def smoke(self):
        return self.__smoke

    @smoke.setter
    def smoke(self, smoke):
        self.__smoke = smoke

    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, active):
        self.__active = active

    @property
    def cvd_prediction(self):
        return self.__cvd_prediction

    @cvd_prediction.setter
    def cvd_prediction(self, cvd_prediction):
        self.__cvd_prediction = cvd_prediction

    @property
    def diabetes_prediction(self):
        return self.__diabetes_prediction

    @diabetes_prediction.setter
    def diabetes_prediction(self, diabetes_prediction):
        self.__diabetes_prediction = diabetes_prediction

    # create a method that returns a dictionary of the values in patient_details
    def map_patient_details(self):
        return {
            "cluster": str(self.__cluster),
            "age": str(self.__age),
            "gender": str(self.__gender),
            "cholesterol": str(self.__cholesterol),
            "systolic_bp": str(self.__systolic_bp),
            "diastolic_bp": str(self.__diastolic_bp),
            "mean_arterial_pressure": str(self.__mean_arterial_pressure),
            "skin_thickness": str(self.__skin_thickness),
            "insulin": str(self.__insulin),
            "bmi": str(self.__bmi),
            "dpf": str(self.__dpf),
            "age_class":str(self.__age_class),
            "bmi_class": str(self.__bmi_class),
            "map_class": str(self.__map_class),
            "cholesterol_class": str(self.__cholesterol_class),
            "glucose_class": str(self.__glucose_class),
            "smoke": str(self.__smoke),
            "active": str(self.__active),
            "cvd_prediction": str(self.__cvd_prediction),
            "diabetes_prediction": str(self.__diabetes_prediction)
        }
