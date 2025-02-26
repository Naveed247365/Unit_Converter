# unit_converter.py
import streamlit as st
import math

# Conversion functions for all categories
def convert_length(value, from_unit, to_unit):
    factors = {
        'meter': 1, 'kilometer': 1000, 'centimeter': 0.01,
        'millimeter': 0.001, 'mile': 1609.34, 'yard': 0.9144,
        'foot': 0.3048, 'inch': 0.0254
    }
    base = value * factors[from_unit]
    return base / factors[to_unit]

def convert_mass(value, from_unit, to_unit):
    factors = {
        'gram': 1, 'kilogram': 1000, 'milligram': 0.001,
        'pound': 453.592, 'ounce': 28.3495
    }
    base = value * factors[from_unit]
    return base / factors[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit': return (value * 9/5) + 32
        if to_unit == 'Kelvin': return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius': return (value - 32) * 5/9
        if to_unit == 'Kelvin': return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius': return value - 273.15
        if to_unit == 'Fahrenheit': return (value - 273.15) * 9/5 + 32
    return value

def convert_area(value, from_unit, to_unit):
    factors = {
        'square meter': 1, 'square kilometer': 1e6,
        'square centimeter': 1e-4, 'square millimeter': 1e-6,
        'square mile': 2.58999e6, 'square yard': 0.836127,
        'square foot': 0.092903, 'square inch': 0.00064516,
        'hectare': 10000, 'acre': 4046.86
    }
    base = value * factors[from_unit]
    return base / factors[to_unit]

def convert_data_transfer(value, from_unit, to_unit):
    factors = {
        'bps': 1, 'Kbps': 1e3, 'Mbps': 1e6,
        'Gbps': 1e9, 'Tbps': 1e12
    }
    base = value * factors[from_unit]
    return base / factors[to_unit]

def convert_digital_storage(value, from_unit, to_unit):
    factors = {
        'bit': 0.125, 'byte': 1,
        'kilobyte': 1024, 'megabyte': 1024**2,
        'gigabyte': 1024**3, 'terabyte': 1024**4,
        'petabyte': 1024**5
    }
    base = value * factors[from_unit]
    return base / factors[to_unit]

def convert_energy(value, from_unit, to_unit):
    factors = {
        'joule': 1, 'kilojoule': 1e3, 'calorie': 4.184,
        'kilocalorie': 4184, 'watt-hour': 3600,
        'kilowatt-hour': 3.6e6, 'electronvolt': 1.60218e-19
    }
    base = value * factors[from_unit]
    return base / factors[to_unit]

def convert_frequency(value, from_unit, to_unit):
    factors = {
        'hertz': 1, 'kilohertz': 1e3,
        'megahertz': 1e6, 'gigahertz': 1e9,
        'terahertz': 1e12
    }
    base = value * factors[from_unit]
    return base / factors[to_unit]

def convert_fuel_economy(value, from_unit, to_unit):
    if from_unit == 'mpg':
        km_l = value * 1.60934 / 3.78541
    elif from_unit == 'km/l':
        km_l = value
    elif from_unit == 'l/100km':
        km_l = 100 / value
    
    if to_unit == 'mpg':
        return km_l * 3.78541 / 1.60934
    elif to_unit == 'km/l':
        return km_l
    elif to_unit == 'l/100km':
        return 100 / km_l

def convert_plane_angle(value, from_unit, to_unit):
    factors = {
        'degree': math.pi/180,
        'radian': 1,
        'gradian': math.pi/200
    }
    base = value * factors[from_unit]
    return base / factors[to_unit]

def convert_pressure(value, from_unit, to_unit):
    factors = {
        'pascal': 1, 'kilopascal': 1e3,
        'bar': 1e5, 'atmosphere': 101325,
        'psi': 6894.76, 'torr': 133.322
    }
    base = value * factors[from_unit]
    return base / factors[to_unit]

def convert_speed(value, from_unit, to_unit):
    factors = {
        'm/s': 1, 'km/h': 0.277778,
        'mph': 0.44704, 'knot': 0.514444,
        'ft/s': 0.3048
    }
    base = value * factors[from_unit]
    return base / factors[to_unit]

def convert_time(value, from_unit, to_unit):
    factors = {
        'second': 1, 'millisecond': 0.001,
        'microsecond': 1e-6, 'nanosecond': 1e-9,
        'minute': 60, 'hour': 3600,
        'day': 86400, 'week': 604800,
        'year': 31557600
    }
    base = value * factors[from_unit]
    return base / factors[to_unit]

def convert_volume(value, from_unit, to_unit):
    factors = {
        'liter': 1, 'milliliter': 0.001,
        'cubic meter': 1000, 'cubic centimeter': 0.001,
        'cubic inch': 0.0163871, 'gallon': 3.78541,
        'quart': 0.946353, 'pint': 0.473176,
        'cup': 0.24, 'fluid ounce': 0.0295735
    }
    base = value * factors[from_unit]
    return base / factors[to_unit]

# Streamlit UI
st.title("📐 Ultimate Unit Converter")

conversion_categories = [
    "Length", "Mass", "Temperature", "Area",
    "Data Transfer Rate", "Digital Storage", "Energy",
    "Frequency", "Fuel Economy", "Plane Angle",
    "Pressure", "Speed", "Time", "Volume"
]

conversion_type = st.selectbox("Select Conversion Type", conversion_categories)

units = []
if conversion_type == "Length":
    units = ['meter', 'kilometer', 'centimeter', 'millimeter', 
             'mile', 'yard', 'foot', 'inch']
elif conversion_type == "Mass":
    units = ['gram', 'kilogram', 'milligram', 'pound', 'ounce']
elif conversion_type == "Temperature":
    units = ['Celsius', 'Fahrenheit', 'Kelvin']
elif conversion_type == "Area":
    units = ['square meter', 'square kilometer', 'square centimeter',
             'square millimeter', 'square mile', 'square yard',
             'square foot', 'square inch', 'hectare', 'acre']
elif conversion_type == "Data Transfer Rate":
    units = ['bps', 'Kbps', 'Mbps', 'Gbps', 'Tbps']
elif conversion_type == "Digital Storage":
    units = ['bit', 'byte', 'kilobyte', 'megabyte',
             'gigabyte', 'terabyte', 'petabyte']
elif conversion_type == "Energy":
    units = ['joule', 'kilojoule', 'calorie', 'kilocalorie',
             'watt-hour', 'kilowatt-hour', 'electronvolt']
elif conversion_type == "Frequency":
    units = ['hertz', 'kilohertz', 'megahertz', 'gigahertz', 'terahertz']
elif conversion_type == "Fuel Economy":
    units = ['mpg', 'km/l', 'l/100km']
elif conversion_type == "Plane Angle":
    units = ['degree', 'radian', 'gradian']
elif conversion_type == "Pressure":
    units = ['pascal', 'kilopascal', 'bar', 'atmosphere', 'psi', 'torr']
elif conversion_type == "Speed":
    units = ['m/s', 'km/h', 'mph', 'knot', 'ft/s']
elif conversion_type == "Time":
    units = ['second', 'millisecond', 'microsecond', 'nanosecond',
             'minute', 'hour', 'day', 'week', 'year']
elif conversion_type == "Volume":
    units = ['liter', 'milliliter', 'cubic meter', 'cubic centimeter',
             'cubic inch', 'gallon', 'quart', 'pint', 'cup', 'fluid ounce']

col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From", units)
with col2:
    to_unit = st.selectbox("To", units)

value = st.number_input("Enter Value", min_value=0.0, format="%.6f")

if st.button("Convert"):
    result = None
    try:
        if conversion_type == "Length":
            result = convert_length(value, from_unit, to_unit)
        elif conversion_type == "Mass":
            result = convert_mass(value, from_unit, to_unit)
        elif conversion_type == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
        elif conversion_type == "Area":
            result = convert_area(value, from_unit, to_unit)
        elif conversion_type == "Data Transfer Rate":
            result = convert_data_transfer(value, from_unit, to_unit)
        elif conversion_type == "Digital Storage":
            result = convert_digital_storage(value, from_unit, to_unit)
        elif conversion_type == "Energy":
            result = convert_energy(value, from_unit, to_unit)
        elif conversion_type == "Frequency":
            result = convert_frequency(value, from_unit, to_unit)
        elif conversion_type == "Fuel Economy":
            result = convert_fuel_economy(value, from_unit, to_unit)
        elif conversion_type == "Plane Angle":
            result = convert_plane_angle(value, from_unit, to_unit)
        elif conversion_type == "Pressure":
            result = convert_pressure(value, from_unit, to_unit)
        elif conversion_type == "Speed":
            result = convert_speed(value, from_unit, to_unit)
        elif conversion_type == "Time":
            result = convert_time(value, from_unit, to_unit)
        elif conversion_type == "Volume":
            result = convert_volume(value, from_unit, to_unit)
        
        st.success(f"**Result:** {value:.4f} {from_unit} = {result:.4f} {to_unit}")
    except Exception as e:
        st.error(f"Error in conversion: {str(e)}")

# Streamlit UI