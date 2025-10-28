# importing relevant libraries here:
import numpy as np
import matplotlib.pyplot as plt

class GeneralWindTurbine(object):
    """
    Describes the general characteristics of a wind turbine.
    
    Encapsulates key parameters and provides a method to calculate
    power output based on a defined power curve logic.
    """
    # write the class here:
    def __init__(self, rotor_diameter, hub_height, rated_power, 
                 v_in, v_rated, v_out, name=None):
        """
        Initializes the GeneralWindTurbine object.

        Parameters:
        rotor_diameter (float): Rotor diameter [m]
        hub_height (float): Hub height [m]
        rated_power (float): Rated power [kW]
        v_in (float): Cut-in wind speed [m/s]
        v_rated (float): Rated wind speed [m/s]
        v_out (float): Cut-out wind speed [m/s]
        name (str, optional): Name of the turbine. Defaults to None.
        """
        self.rotor_diameter = rotor_diameter
        self.hub_height = hub_height
        self.rated_power = rated_power
        self.v_in = v_in
        self.v_rated = v_rated
        self.v_out = v_out
        self.name = name

    def get_power(self, v):
        """
        Calculates the power output P (kW) for a given 
        wind speed v (m/s) using the following rules:
        
        - if v < v_in or v >= v_out, P = 0
        - if v_in <= v < v_rated, P = rated_power * (v / v_rated)**3
        - if v_rated <= v < v_out, P = rated_power
        """
        
        if v < self.v_in or v >= self.v_out:
            # Rule 1
            power = 0.0
        elif self.v_in <= v < self.v_rated:
            # Rule 2
            power = self.rated_power * (v / self.v_rated)**3
        elif self.v_rated <= v < self.v_out:
            # Rule 3
            power = self.rated_power
            
        return power

class WindTurbine(GeneralWindTurbine):
    """
    Inherits from GeneralWindTurbine and will use a specific
    power curve data for power calculation via interpolation.
    """
    # write the class here:
    def __init__(self, rotor_diameter, hub_height, rated_power, 
                 v_in, v_rated, v_out, power_curve_data, name=None):
        """
        Initializes the WindTurbine object.

        Parameters:
        (Inherited params): ...
        power_curve_data (np.ndarray): n-by-2 numpy array.
                                       Column 0: wind speed [m/s]
                                       Column 1: power [kW]
        name (str, optional): Name of the turbine. Defaults to None.
        """
        # Initialize parent class attributes
        super().__init__(rotor_diameter, hub_height, rated_power, 
                         v_in, v_rated, v_out, name=name)
        
        # Add the new attribute
        self.power_curve_data = power_curve_data

    def get_power(self, v):
        """
        Overrides the get_power method.
        
        Calculates the power output P (kW) for a given 
        wind speed v (m/s) using interpolation on the
        power_curve_data.
        """
        # Extract wind speed (1st col) and power (2nd col)
        ws_data = self.power_curve_data[:, 0]
        p_data = self.power_curve_data[:, 1]
        
        # Use numpy.interp to find the power at wind speed v
        power = np.interp(v, ws_data, p_data)
        
        return power

if __name__ == '__main__':
    #
    # Main script to use the classes and make the plot
    # will be written here.
    #
    pass