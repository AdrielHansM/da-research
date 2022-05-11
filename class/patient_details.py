class Patient:
  def __init__(self, cluster, age, gender, glucose, systolic_bp, diastolic_bp, mean_arterial_pressure,skin_thickness, insulin, bmi, dpf, age_bin, bmi_class, map_class, cholesterol_class, glucose_class, smoke, active):
    self.__cluster = cluster
    self.__age = age
    self.__gender = gender
    self.__glucose = glucose
    self.__systolic_bp = systolic_bp
    self.__diastolic_bp = diastolic_bp
    self.__mean_arterial_pressure = mean_arterial_pressure
    self.__skin_thickness = skin_thickness
    self.__insulin = insulin
    self.__bmi = bmi
    self.__dpf = dpf
    self.__age_bin = age_bin
    self.__bmi_class = bmi_class
    self.__map_class = map_class
    self.__cholesterol_class = cholesterol_class
    self.__glucose_class = glucose_class
    self.__smoke = smoke
    self.__active = active

  def __int__(self):
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
    self._glucose = glucose

  @property
  def systolic_bp(self):
    return self.__systolic_bp
  
  @systolic_bp.setter
  def systolic_bp(self, systolic_bp):
    self._systolic_bp = systolic_bp

  @property
  def diastolic_bp(self):
    return self.__diastolic_bp
  
  @diastolic_bp.setter
  def diastolic_bp(self, diastolic_bp):
    self._diastolic_bp = diastolic_bp

  @property
  def mean_arterial_pressure(self):
    return self.__mean_arterial_pressure

  @mean_arterial_pressure.setter
  def mean_arterial_pressure(self, mean_arterial_pressure):
    self._mean_arterial_pressure = mean_arterial_pressure

  @property
  def skin_thickness(self):
    return self.__skin_thickness
  
  @skin_thickness.setter
  def skin_thickness(self, skin_thickness):
    self._skin_thickness = skin_thickness

  @property
  def insulin(self):
    return self.__insulin
  
  @insulin.setter
  def insulin(self, insulin):
    self._insulin = insulin

  @property
  def bmi(self):
    return self.__bmi
  
  @bmi.setter
  def bmi(self, bmi):
    self._bmi = bmi

  @property
  def dpf(self):
    return self.__dpf
  
  @dpf.setter
  def dpf(self, dpf):
    self._dpf = dpf

  @property
  def age_bin(self):
    return self.__age_bin
  
  @age_bin.setter
  def age_bin(self, age_bin):
    self._age_bin = age_bin

  @property
  def bmi_class(self):
    return self.__bmi_class
  
  @bmi_class.setter
  def bmi_class(self, bmi_class):
    self._bmi_class = bmi_class

  @property
  def map_class(self):
    return self.__map_class
  
  @map_class.setter
  def map_class(self, map_class):
    self._map_class = map_class

  @property
  def cholesterol_class(self):
    return self.__cholesterol_class
  
  @cholesterol_class.setter
  def cholesterol_class(self, cholesterol_class):
    self._cholesterol_class = cholesterol_class

  @property
  def glucose_class(self):
    return self.__glucose_class
  
  @glucose_class.setter
  def glucose_class(self, glucose_class):
    self._glucose_class = glucose_class

  @property
  def smoke(self):
    return self.__smoke
  
  @smoke.setter
  def smoke(self, smoke):
    self._smoke = smoke

  @property
  def active(self):
    return self.__active
  
  @active.setter
  def active(self, active):
    self._active = active