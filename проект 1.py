import math
import matplotlib.pyplot as plt

#const
g=9.81
h_hoop=3.05

print('Welcome to the basketball shot simulator!')

distance=float(input('Enter the distance to the hoop in meters'))
height=float(input('Enter your height in meters'))

def_arms= 0.35
def_jump=0.40
h_release= height+def_arms+def_jump

print(f'Default release height calculated as {round(h_release, 2)} m.')
advanced=input('Do you want to enter exact arm reach and vertical jump? (yes/no):').strip().lower()

if advanced=='yes':
    print('advanced Settings')
    arms=float(input('Arm reach above head in meters'))
    jump=float(input('Vertical jump in meters'))
    h_release=height+arms+jump
    print(f'New release height saved: {round(h_release, 2)} m.')
else:
    print('Using default settings')

#BIOMECHANICS ENGINE
print('Biomechanics Analysis')
delta_y=h_hoop-h_release

tan_alpha=1+((2*delta_y)/distance)
optimal_angle_rad=math.atan(tan_alpha)
optimal_angle_deg=math.degrees(optimal_angle_rad)
#RESULTS AND ADVISE
print(f'For a perfect 45-degree splash from{distance}m:')
print(f'Your optimal release angle is: {round(optimal_angle_deg, 1)}')

if optimal_angle_deg >= 52:
    print("Coach's Note: You need a high arc for this shot. Aim higher!")
elif optimal_angle_deg <=46:
    print("Coach's Note: You can shoot with a flat, fast trajectory.")
else:
    print("Coach's Note: a standard shooting arc is perfectly fine here.")

#visualisation
print(" Generating trajectory graph...")
#V0
term1 = 2 * (math.cos(optimal_angle_rad) ** 2)
term2 = h_release + distance * math.tan(optimal_angle_rad) - h_hoop
v0 = math.sqrt((g * (distance ** 2)) / (term1 * term2))
x_points = []
y_points = []
steps = 50
for i in range(steps + 1):
    x = (distance / steps) * i
    y = h_release + x * math.tan(optimal_angle_rad) - (g * x**2) / (2 * v0**2 * math.cos(optimal_angle_rad)**2)
    x_points.append(x)
    y_points.append(y)
#graph
plt.figure(figsize=(10, 5))
plt.plot(x_points, y_points, label="Optimal Trajectory", color="orange", linewidth=2)
plt.scatter([0], [h_release], color="blue", s=100, label="Release Point (You)")
plt.scatter([distance], [h_hoop], color="red", s=100, label="Hoop (3.05m)")
plt.title(f"Perfect Shot Arc ({round(optimal_angle_deg, 1)}°)")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.axis('equal')
plt.ylim(0, max(y_points) + 1)
plt.show()


