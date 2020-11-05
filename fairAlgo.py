# one, two, three, four, five = 1, 2, 3, 4, 5

padInherent = input("Probability of Action Deterrence - Inherent: ")
print(padInherent)
padControls = input("Probability of Action Deterrence - Controls: ")
print(padControls)

rsvInheritent = input("Resistance Strength Vulnerability - Inherent: ")
print(rsvInheritent)
rsvControls = input("Resistance Strength Vulnerability - Controls: ")
print(rsvControls)

cfaInheritent = input("Contact Frequency Avoidance - Inherent: ")
print(cfaInheritent)
cfaControls = input("Contact Frequency Avoidance - Controls: ")
print(Controls)

threatCapacity = input("Threat Capability: ")
print(threatCapacity)

plmrInheritent = input("Primary Loss Magnitude Responsive - Inheritance: ")
print(plmrInheritent)
plmrControls = input("Primary Loss Magnitude Responsive - Controls: ")
print(plmrControls)

slpPercent = input("Secondary Loss Probability: ")
print(slpPercent)

slmrInheritent = input("Secondary Loss Magnitude Responsive - Inheritance: ")
print(slmpInheritent)
slmrControls = input("Secondary Loss Magnitude Responsive - Controls: ")
print(slmpControls)

tefInheritant = cfaInheritent + padInherent
	if tefInheritant < 5
		print("1")
	elif tefInheritant = 5
		print("2")
	elif tefInheritant = 6
		print("3")
	elif tefInheritant = 7
		print("4")
	else: tefInheritant > 7
		print("5")

vInherent = cfaInheritent + padInherent
	if vInherent < 5
		print("1")
	elif vInherent = 5
		print("2")
	elif vInherent = 6
		print("3")
	elif vInherent = 7
		print("4")
	else: vInherent > 7
		print("5")

plefInherent = vInherent + tefInheritant
	if plefInherent < 5
		print("1")
	elif plefInherent = 5
		print("2")
	elif plefInherent = 6
		print("3")
	elif plefInherent = 7
		print("4")
	else: plefInherent > 7
		print("5")

prInherent = plefInherent + plmrInheritent
	if prInherent < 5
		print("Very Low")
	elif prInherent = 5
		print("Low")
	elif prInherent = 6
		print("Medium")
	elif prInherent = 7
		print("High")
	else: prInherent > 7
		print("Very High")

slefInherent = plefInherent + slpPercent
	if plefInherent < 5
		print("1")
	elif plefInherent = 5
		print("2")
	elif plefInherent = 6
		print("3")
	elif plefInherent = 7
		print("4")
	else: plefInherent > 7
		print("5")
		
srInherent = slmrInheritent + slefInherent
	if srInherent < 5
		print("Very Low")
	elif srInherent = 5
		print("Low")
	elif srInherent = 6
		print("Medium")
	elif srInherent = 7
		print("High")
	else: srInherent > 7
		print("Very High")
		
overallRisk