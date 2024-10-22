def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_in(n):
    cm_to_inches = 0.393701
    return round(n*cm_to_inches, 2)

def cm_to_fai(n):
    cm_to_inches = 0.393701
    inches_to_feet = 12

    # Convert centimeters to inches
    height_inches = n * cm_to_inches

    # Calculate feet and inches
    feet = height_inches // inches_to_feet
    inches = height_inches % inches_to_feet

    feet = int(feet)
    inches = int(inches)

    feet = str(feet)
    inches = str(inches)

    return feet + "ft and " + inches + "in"

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'170 cm = {cm_to_in(170)} inches')
    print(f'170 cm = {cm_to_fai(170)}')

