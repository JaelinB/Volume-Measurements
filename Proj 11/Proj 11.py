UNITS = ["ml","oz"]
MLperOZ = 29.5735295625  # ml per oz
DELTA = 0.000001

class Volume(object):
    def __init__(self,magnitude = 0,units = "ml"):   # this line is incomplete: parameters needed
        self.magnitude = magnitude
        self.units = units

        if type(magnitude) == float or type(magnitude) == int:
            if magnitude < 0:
                self.magnitude = 0
                self.units = None

        else:
            self.magnitude = 0
            self.units = None

        if units != "ml" and units != "oz":
            self.units = None
            self.magnitude = None

    
    def __str__(self):    # this line is incomplete: parameters needed
        if self.units == None:
           return "Not a Volume"
        
        else:
            return("{:.3f} {}".format(self.magnitude,self.units))  
        
    def __repr__(self):    # this line is incomplete: parameters needed
        if self.units == None:
           return "Not a Volume"
        
        else:
            return("{:.6f} {}".format(self.magnitude,self.units)) 
        
    def is_valid(self):     # this line is incomplete: parameters needed
        if self.units != None:
            return True
        else:
            return False
    
    def get_units(self):     # this line is incomplete: parameters needed
        return self.units
    
    def get_magnitude(self):  # this line is incomplete: parameters needed
        return self.magnitude
    
    def metric(self):      # this line is incomplete: parameters needed
        if self.is_valid():
            if self.units == "ml":
                v = Volume(self.magnitude,self.units)
                return v
            else:
                v1 = self.magnitude * MLperOZ
                v = Volume(v1,"ml")
                return v
        
    def customary(self):    # this line is incomplete: parameters needed
        if self.is_valid():
            if self.units == "oz":
                v = Volume(self.magnitude,self.units)
                return v
            else:
                v1 = self.magnitude / MLperOZ
                v = Volume(v1,"oz")
                return v
    def __eq__(self,vol):  # this line is incomplete: parameters needed
        if self.is_valid:
            if self.units == vol.units:
                minus = self.magnitude - vol.magnitude
                minus_abs = abs(minus)

                if minus_abs < DELTA:
                    return True

                else:
                    return False

            if self.units != vol.units:
                if self.units == "ml":
                    ml = vol.metric()
                    minus = self.magnitude - ml.magnitude
                    minus_abs = abs(minus)

                    if minus_abs < DELTA:
                        return True

                    else:
                        return False

                if self.units == "oz":
                    oz = vol.customary()
                    minus = self.magnitude - oz.magnitude
                    minus_abs = abs(minus)

                    if minus_abs < DELTA:
                        return True

                    else:
                        return False

    def add(self, mag):  # this line is incomplete: parameters needed
        
        if type(mag) == Volume:
            if self.units == mag.units:
                add = self.magnitude + mag.magnitude
                m = Volume(add,self.units)
                return m
            if self.units != mag.units:
                if self.units == "ml":
                    m = mag.metric()
                    add = self.magnitude + m.magnitude
                    a = Volume(add,self.units)
                    return a
                if self.units == "oz": 
                    m = mag.customary()
                    add = self.magnitude + m.magnitude
                    a = Volume(add,self.units)
                    return a

        if type(mag) == float or type(mag) == int:    
            add = mag + self.magnitude
            a = Volume(add,self.units)
            return a

        else:
            v = Volume(None, None)
            return v
    def sub(self,mag): # this line is incomplete: parameters needed
        if type(mag) == Volume:
            if self.units == mag.units:
                add = self.magnitude - mag.magnitude
                m = Volume(add,self.units)
                return m
            if self.units != mag.units:
                if self.units == "ml":
                    m = mag.metric()
                    add = self.magnitude - m.magnitude
                    a = Volume(add,self.units)
                    return a
                if self.units == "oz": 
                    m = mag.customary()
                    add = self.magnitude - m.magnitude
                    a = Volume(add,self.units)
                    return a

        if type(mag) == float or type(mag) == int:    
            add = self.magnitude - mag
            a = Volume(add,self.units)
            return a

        else:
            v = Volume(None, None)
            return v

