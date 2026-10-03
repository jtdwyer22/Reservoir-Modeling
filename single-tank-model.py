pressure = 5000.0
pore_volume = 2_000_000.0
compressibility = 2e-5
rate = 200.0
dt = 1
total_time = 20.0

pressure_history = [pressure]
time_history = [0.0]

number_of_steps = int(total_time/dt)

for step in range(number_of_steps):
    
    pressure_change = -(rate * dt)/(compressibility * pore_volume)
    pressure = pressure + pressure_change
    pressure_history.append(pressure)
    time_history.append((step+1)*dt)

print(time_history, pressure_history)