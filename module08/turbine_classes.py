# importing relevant libraries here:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd # Needed for loading data from URL

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
    Inherits from GeneralWindTurbine and uses a specific
    power curve data (n-by-2 numpy array) for power calculation 
    via interpolation.
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
    # Write the main script to use the classes and make the plot here
    
    # --- Task 1.3: Initialize Objects ---
    
    # Define parameters for LEANWIND_8MW_164_RWT
    # Data from: https://nrel.github.io/turbine-models/LEANWIND_8MW_164_RWT.html
    LW_params = {
        "rotor_diameter": 164.0,  # m
        "hub_height": 110.0,   # m
        "rated_power": 8000.0, # kW
        "v_in": 4.0,       # m/s
        "v_rated": 12.5,     # m/s
        "v_out": 25.0,     # m/s
        "name": "LEANWIND 8MW"
    }

    # URL for the power curve data (Raw version of the link from the assignment)
    csv_url = "https://raw.githubusercontent.com/NREL/turbine-models/main/turbine_models/data/Offshore/LEANWIND_Reference_8MW_164.csv"
    
    # Load data, using comment='#' to skip metadata rows
    df_pc = pd.read_csv(csv_url, comment='#') 
    
    # Get data as numpy array. Headers are from the CSV file.
    power_curve_data = df_pc[['Wind Speed [m/s]', 'Power [kW]']].values

    # Initialize the GeneralWindTurbine object
    turbine_gen = GeneralWindTurbine(**LW_params)
    
    # Initialize the WindTurbine (real curve) object
    turbine_real = WindTurbine(
        power_curve_data=power_curve_data,
        **LW_params
    )

    # --- Task 1.4: Plot and Compare ---
    
    # Create a range of wind speeds for plotting
    v_range = np.linspace(0, 30, 300) # 0 to 30 m/s

    # Calculate power for each turbine (looping is required for now)
    power_gen = []
    power_real = []
    
    for v in v_range:
        power_gen.append(turbine_gen.get_power(v))
        power_real.append(turbine_real.get_power(v))

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(v_range, power_gen, 'r--', label='GeneralWindTurbine (Rule-Based)')
    plt.plot(v_range, power_real, 'b-', label='WindTurbine (Interpolated)')
    
    # Add labels and title
    plt.title(f'Power Curve Comparison: {LW_params["name"]}')
    plt.xlabel('Wind Speed (m/s)')
    plt.ylabel('Power (kW)')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)
    
    # Save the plot
    plt.savefig('module08_power_curves.png')
    print("Plot 'module08_power_curves.png' created successfully.")
    # plt.show()