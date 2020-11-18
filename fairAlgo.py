# one, two, three, four, five = 1, 2, 3, 4, 5

padInherent = input("Probability of Action Deterrence - Inherent: ")
padInherentinput = int(padInherent)
print(padInherentinput)
padControls = input("Probability of Action Deterrence - Controls: ")
print(padControls)

rsvInherent = input("Resistance Strength Vulnerability - Inherent: ")
rsvInherentinput = int(rsvInherent)
print(rsvInherentinput)
rsvControls = input("Resistance Strength Vulnerability - Controls: ")
print(rsvControls)

cfaInheritent = input("Contact Frequency Avoidance - Inherent: ")
cfaInheritentinput = int(cfaInheritent)
print(cfaInheritentinput)
cfaControls = input("Contact Frequency Avoidance - Controls: ")
print(cfaControls)

threatCapacity = input("Threat Capability: ")
threatCapacityinput = int(threatCapacity)
print(threatCapacityinput)

plmrInheritent = input("Primary Loss Magnitude Responsive - Inheritance: ")
plmrInheritentinput = int(plmrInheritent)
print(plmrInheritentinput)
plmrControls = input("Primary Loss Magnitude Responsive - Controls: ")
print(plmrControls)

slpPercent = input("Secondary Loss Probability: ")
print(slpPercent)

slmrInheritent = input("Secondary Loss Magnitude Responsive - Inheritance: ")
slmrInheritentinput = int(slmrInheritent)
print(slmrInheritentinput)
slmrControls = input("Secondary Loss Magnitude Responsive - Controls: ")
print(slmrControls)

def tefInherent():
	tefInherent = cfaInheritent + padInherent
	if tefInherent < 5:
		print("1")
	elif tefInherent == 5:
		print("2")
	elif tefInherent == 6:
		print("3")
	elif tefInherent == 7:
		print("4")
	elif tefInherent > 7:
		print("5")
	else:
    		print("undefined")


def vInherent():
	vInherent= cfaInheritent + padInherent
	if vInherent < 5:
		print("1")
	elif vInherent == 5:
    		print("2")
	elif vInherent == 6:
		print("3")
	elif vInherent == 7:
		print("4")
	elif vInherent > 7:
		print("5")
	else:
    		print("undefined")

def plefInherent():
	plefInherent = tefInherent + vInherent
	if plefInherent < 5:
		print("1")
	elif plefInherent == 5:
		print("2")
	elif plefInherent == 6:
		print("3")
	elif plefInherent == 7:
		print("4")
	elif plefInherent > 7:
		print("5")
	else:
    		print("undefined")

def prInherent():
	prInherent = plefInherent + plmrInheritent
	if prInherent < 5:
		print("Very Low")
	elif prInherent == 5:
		print("Low")
	elif prInherent == 6:
		print("Medium")
	elif prInherent == 7:
		print("High")
	elif prInherent > 7:
		print("Very High")
	else:
    		print("undefined")

def slefInherent():
	slefInherent = plefInherent + slpPercent
	if plefInherent < 5:
		print("1")
	elif plefInherent == 5:
		print("2")
	elif plefInherent == 6:
		print("3")
	elif plefInherent == 7:
		print("4")
	elif plefInherent > 7:
		print("5")
	else:
    		print("undefined")
		
def srInherent():
	srInherent = slmrInheritent + slefInherent
	if srInherent < 5:
		print("Very Low")
	elif srInherent == 5:
		print("Low")
	elif srInherent == 6:
		print("Medium")
	elif srInherent == 7:
		print("High")
	elif srInherent > 7:
		print("Very High")
	else:
    		print("undefined")
		
def overallRisk():
	overallRisk = prInherent + srInherent
	if prInherent < 5 and srInherent < 5:
		print("Very Low")
	elif  prInherent < 5 and srInherent == 5:
		print("Low")
	elif prInherent < 5 and srInherent == 6:
		print("Medium")
	elif prInherent < 5 and srInherent == 7:
		print("High")
	elif prInherent < 5 and srInherent > 7:
		print("Very High")
	elif  prInherent == 5 and srInherent < 5:
		print("Low")
	elif prInherent == 5 and srInherent == 5:
		print("Low")
	elif prInherent == 5 and srInherent == 6:
		print("Medium")
	elif prInherent == 5 and srInherent == 7:
		print("High")
	elif prInherent == 5 and srInherent > 7:
		print("Very High")
	elif prInherent == 6 and srInherent < 5:
		print("Medium")
	elif prInherent == 6 and srInherent == 5:
		print("Medium")
	elif prInherent == 6 and srInherent == 6:
		print("Medium")
	elif prInherent == 6 and srInherent == 7:
		print("High")
	elif prInherent == 6 and srInherent > 7:
		print("Very High")
	elif prInherent == 7 and srInherent < 5:
		print("High")
	elif prInherent == 7 and srInherent == 5:
		print("High")
	elif prInherent == 7 and srInherent == 6:
		print("High")
	elif prInherent == 7 and srInherent == 7:
		print("High")
	elif prInherent == 7 and srInherent > 7:
		print("Very High")
	elif prInherent > 7 and srInherent < 5:
		print("Very High")
	elif prInherent > 7 and srInherent == 5:
		print("Very High")
	elif prInherent > 7 and srInherent == 6:
		print("Very High")
	elif prInherent > 7 and srInherent == 7:
		print("Very High")
	elif prInherent > 7 and srInherent > 7:
		print("Very High")
	else:
		print("undefined")

tefInherent()
vInherent()
plefInherent()
prInherent()
slefInherent()
srInherent()
overallRisk()