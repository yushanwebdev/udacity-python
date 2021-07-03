# The current volume of a water reservior (in cubic metres)
reservior_volume = 4.445e8

# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall *= .9

# add the rainfall variable to the reservior_volume variable
reservior_volume += rainfall

# increase reservior_volume by 5% to account for stormwater that flows
# into the reservior in the days following the storm
reservior_volume *= 1.05

# decrease reservior volume by 5% to account for stormwater that flows
# into the reservior in the days following the storm
reservior_volume *= .95

# subtract 2.5e5 cubic metres from reservior_volume to account for water 
# that's piped to arid regions.
reservior_volume -= 2.5e5

# print the new value of the reservior_volume variable
print(reservior_volume)