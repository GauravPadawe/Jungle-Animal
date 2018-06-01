def jungle_animal(animal, my_speed):
	while animal == "zebra":
	    return "Try to ride a zebra!"
		
	while animal == "cheetah":
		if my_speed >= 115:
			return "Run!"
		else:
			return "Stay calm and wait!"
			
	while animal != "zebra" or "cheetah":
	    return "Introduce yourself!"
	    
print jungle_animal("cheetah", 114.9)