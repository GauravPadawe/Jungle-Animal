def jungle_animal(animal, my_speed):                     # Defining a procedure accepting a String and Number
	while animal == "zebra":                         # While animal is "zebra"
	    return "Try to ride a zebra!"                # Will return ""Try to ride a zebra!"
		
	while animal == "cheetah":                       # While loop for "Cheetah"
		if my_speed >= 115:                      # If statement to check if your speed equals or exceeds 115
			return "Run!"                    # If Yes the "Run"
		else:                                    # else "Stay calm and wait!"
			return "Stay calm and wait!"
			
	while animal != "zebra" or "cheetah":            # While loop again if animal is not "cheetah" or "zebra"
	    return "Introduce yourself!"                 # returning "Introduce yourself"
	    
print jungle_animal("cheetah", 114.9)

# CODED BY - GAURAV PADAWE
