print(" Multi-stage cascading Leaching via Agitators ")

element = input("The element that is being extracted from its ore is: \n")

solvent = input("The solvent being used to extract is: \n")

weightofore = float(input("Enter the weight of the ore in kilogram\n"))
x = float(input("The weight ratio of the ore to the entrained solvent is   \n"))
y = float(input ("to \n"))
oreentrainedsolventratio = x/y

percentageofelementinore = float(input("Enter the percentage of element in ore in (%)\n"))

weightofelementinore = weightofore * (percentageofelementinore/100)

weightofsolvent = float(input("Enter the weight of the solvent being used in kilogram \n"))

Totalsolution = weightofsolvent

weightoforewithoutelement = weightofore - weightofelementinore

count = 0
TCE = 0
if percentageofelementinore <= 100 :
	tee= input("\nDo you want to know the total element extracted? (yes/no) \n")
	
	weo= input("\nDo you want to know the weight of element in ore?(yes/no) \n")
	
	eess=input("\nDo you want to know the weight element entrained in the solvent? (yes/no) \n")
	
	e2sr=input(" \nDo you want to know the element to solvent ratio? (yes/no) \n")
	
	weio=input(" \n Do you want to know the weight of element in overflow? (yes/no) \n")

	
	choice = int(input("Enter 1 to determine the number of stages with percentage provided and Enter 2 to determine the percentage with number of stages provided: \n"))
	
	if (choice == 1) :
		percentage=int(input("The percentage you want as a limit is: \n"))
		if percentage<=100 :
			x = (percentage/100)*weightofelementinore
			while ( TCE < x):
				elementsolventratio = weightofelementinore/Totalsolution
				weightofentrainedsolvent =(weightoforewithoutelement/ oreentrainedsolventratio)
				elemententrainedinsolvent = elementsolventratio * weightofentrainedsolvent
				
				weightofelementoverflow= weightofelementinore - elemententrainedinsolvent
				if weightofelementoverflow < 0 :
					print("You have entered an incorrect combination of input")
					break
				
				TCE = TCE + weightofelementoverflow
				count +=1
				Totalsolution = Totalsolution + weightoforewithoutelement
				
				weightofelementinore = elemententrainedinsolvent
				
			print("The number of agitators required to get" , percentage,"% of",element,"are" ,count)
	
			
			if tee.lower() == "yes" :
				print("The total weight of", element,"extracted is", (round(TCE,1)),"Kg")
				
			if weo.lower()== "yes" :
				print("The weight of" ,element,"in the  ore is", (round(weightofelementinore,1)),"Kg")
				
			if eess.lower() == "yes" :
				print("The weight of",element,"entrained in",solvent,"solution is",(round(elemententrainedinsolvent,1)),"Kg")
				
			if e2sr.lower() == "yes" :
				print("The",element,"to",solvent,"ratio is",(round(elementsolventratio,3)))
				
			if weio.lower() == "yes" :
				print ("The weight of",element,"in overflow is",(round(weightofelementoverflow,2)),"Kg")
		else:
			print("Percentage error")
		
				
			
	elif (choice ==2):
		stage = int(input("Enter the number of stages you are calculating for: \n"))
		
		while (count < stage) :
			elementsolventratio = weightofelementinore/Totalsolution
			
			weightofentrainedsolvent =(weightoforewithoutelement/ oreentrainedsolventratio)
			elemententrainedinsolvent = elementsolventratio * weightofentrainedsolvent
				
			weightofelementoverflow= weightofelementinore - elemententrainedinsolvent
			if weightofelementoverflow < 0 :
					print("You have entered an incorrect combination of input")
					break
			
			TCE = TCE + weightofelementoverflow
			
			count +=1
			Totalsolution = Totalsolution + weightoforewithoutelement
			
			weightofelementinore = elemententrainedinsolvent
			answer = (TCE * 100)/(weightofore * (percentageofelementinore/100) )
		print((round(answer,1)), "% of", element ,"is extracted after", stage, "stages")
		
		if tee.lower()== "yes" :
			print("The total weight of", element,"extracted is", (round(TCE,1)),"Kg")
			
		if weo.lower()== "yes" :
			print("The weight of" ,element,"in the  ore is",(round( weightofelementinore,1)),"Kg")
			
		if eess.lower() == "yes" :
			print("The weight of",element,"entrained in",solvent,"solution is",(round(elemententrainedinsolvent,1)),"Kg")
			
		if e2sr.lower() == "yes" :
			print("The",element,"to",solvent,"ratio is",(round(elementsolventratio,3)))
			
		if weio.lower() == "yes" :
			print ("The weight of",element,"in overflow is",(round(weightofelementoverflow,1)),"Kg")
	else:
		print("Invalid response")
else:
		print("Percentage error")
