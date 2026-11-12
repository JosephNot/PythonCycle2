import matplotlib.pyplot as plt
 
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
visitors = [42, 55, 48, 63, 80]
 
plt.plot(days, visitors, marker="o") 
plt.title("Weekly Visitor Numbers") 
plt.xlabel("Day") 
plt.ylabel("Number of visitors") 
plt.grid(True) 
plt.tight_layout() 
plt.show()

# Task 2

activities = ["Swimming", "Gym", "Yoga", "Football", "Badminton"] 
bookings = [38, 65, 22, 47, 31] 
 
# TODO 1: Create a bar chart with plt.bar(). 
# TODO 2: Add a title and labels. 
# TODO 3: Show the chart

plt.bar(activities, bookings)
plt.title("Activity Bookings Popularity")
plt.xlabel("Activity")
plt.ylabel("Number of Bookings")
plt.grid(True, axis="y", alpha=0.5)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
