my_name = "Namie Namson"
my_age: int = 35
my_height = 182.8  # height in cm
my_weight = 68.4  # kg value

# the % variable needs to be inside the parenthesis in the print function.
print("Here are the stats on %s." % my_name)
print("I'm %d years old" % my_age)
print("I'm also %d heavy" % my_weight)

print("If I add %d, %d, and %d, I get %d" % (my_age, my_height, my_weight, my_age + my_height + my_weight))
