# This program calculates distance traveled
# 6.21.2021
# CTI-110 P2HW1 - DistanceTraveled
# John Green

speed = int(input('Enter car speed: '))        
time = int(input('Enter time: '))   

if time <= 0:  
print(1)
else:
print(time)     

#Calculate distance traveled
distance = speed * time    

# Display speed, time and distance
print('Speed Entered: ', speed)
print('Time Entered: ', time)
print('Distance traveled: ', distance)