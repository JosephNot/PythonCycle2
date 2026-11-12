import matplotlib.pyplot as plt 
 
days = ["Mon", "Tue", "Wed", "Thu", "Fri"] 
week_one = [42, 55, 48, 63, 71] 
week_two = [50, 52, 60, 67, 75] 

# TODO 1: Plot week_two with a different marker. 
# TODO 2: Add a suitable chart title. 
# TODO 3: Label both axes. 
# TODO 4: Add plt.legend() and plt.grid(True). 
# TODO 5: Display the chart. 
total_week_one = sum(week_one) / len(week_one)
total_week_two = sum(week_two) / len(week_two)

plt.plot(days, week_one, marker="o", label=f"Week 1: Total({total_week_one:.1f})") 
plt.plot(days, week_two, marker="s", label=f"Week 2: Total({total_week_two:.1f})") 
plt.title("Weekly Attendance Numbers") 
plt.xlabel("Days") 
plt.ylabel("Number of Attendees") 
plt.grid(True) 
plt.legend() 
plt.tight_layout()
plt.show()
