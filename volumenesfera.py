#analorenacamargo 12/11/2023
#Calcula el volumen de una esfera


def calculate_sphere_volume(radius):
    volume = (4/3) * 3.1416 * (radius ** 3)
    return volume

radius = float(input("Enter the radius of the sphere: "))
    
volume = calculate_sphere_volume(radius)
print(f"The volume of the sphere is {volume:.2f} cubic units.")
