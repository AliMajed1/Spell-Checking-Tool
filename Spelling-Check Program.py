#Spelling-Check Program (CourseWork 01)

#Import Section
from difflib import SequenceMatcher
import re
import time, os
from datetime import date
from datetime import datetime
import time
import os.path
from os import path

#Creating a list that conatains all the words in the txt file.
f= open("EnglishWords.txt")
Content=f.read()
Words_list=Content.splitlines()

#  An amazing function that we can use to filter the input into lowercase letters ONLY.
def words(text): 
			return re.sub("[^a-z \n]+" ,"", text.lower())

# Main Loop(Main Menu, You will return here if you want to enter a new sentence or file)
while True: 
	print("Welcome To My Spell-Checking Program!")
	c = (input("\n\n Would you like to :  \n1-Spell-Check a sentence.  \n2-Spell-Check a File  \n3-Quit \n "))
    
    # Spell-Check a Sentence.
	if (c == "1"):

		InputSentence=input("Enter a sentence : \n")
		StartingTime=time.time()

		# Filter The inputed sentence using our function, then transform it into a list.
		FilteredSentence = words(InputSentence) 
		InputWords= FilteredSentence.split()

		#The List that will contain the words of our final(Spellchecked) Sentence.
		List=[0]*len(InputWords) 

		# Defining important variables before going into the "Spell-Checking loop".
		Wordnumber=0
		NumofIncorrectWords=0
		NumofcorrectWords=0
		NumofWordsAddedToDic=0
		NumofWordsChanged=0
		print("Loading....")

		# The Spell-Checking Loop, where all the work are being processed to spell chaeck a whole Sentence.
		while Wordnumber < len(InputWords) : 
			
			# Resetting the variables to 0 each time a new word is going through the loop.
			count=0 # Represnts 
			highestscore=0.0
			
			# The loop for Spell-Checking each single word.
			while count < len(Words_list): 
		
				score= SequenceMatcher(None, InputWords[Wordnumber] , Words_list[count]).ratio()
				
				# If we found a matching word from the txt file.
				if (score == 1.0): 
					List[Wordnumber]= InputWords[Wordnumber] # Then place the input word by it's order in the final list, since we found it's correctly spelled.
					count=len(Words_list) # Set the variable "count" to it's maximmum value, so the condition for the while loop is achieved, and we can move on to Spell-Check the next word.
					NumofcorrectWords +=1

				# When The Word does'nt match	
				else: 
					# If The word is the most similar to the original word so far.
					if (score > highestscore) : 

						highestscore = score
						SuggestedWord= Words_list[count] # Then make it the suggested Spell-Checked word.

					# If there already exist a more similar word, move to the next one.
					else: 
						pass

				count +=1 # Each time "count" increases by 1 , a new word from the txt file will be tested.

			# If The Spell-Checking loop didnt find any matching word.
			if (score< 1.0) : 
				Choice="0"
				print("\n\nOops!! The Word (" + InputWords[Wordnumber] +") is spelt Incorrectly , Do You Want To :  \n1-Ignore  \n2-Mark \n3-Add To Dictionary \n4-Suggest Likely Correct Spelling \n" )
				
				# A Sub-Menu to choose what to do with an incorrectly spelled word.
				while Choice not in ("1","2","3","4"): 
					
					Choice=input()

					if (Choice=="1"): 

						print("\nThe Mistake will be Ignored")
						List[Wordnumber]=InputWords[Wordnumber] # Set the original word as it is in the final Sentence.
						NumofIncorrectWords +=1

					elif (Choice=="2"):
						
						List[Wordnumber]=("?"+InputWords[Wordnumber]+"?")
						print("\nThe Word (" + InputWords[Wordnumber] +") has been Marked Successfully")	# Set the original word between question marks in the final Sentence.
						NumofIncorrectWords +=1

					elif (Choice=="3"):
						 # Add the word to the txt file.
						a = open("EnglishWords.txt", "a")
						a.write(str("\n") +str(InputWords[Wordnumber]))
						a.close()
						print("\nThe Word (" + InputWords[Wordnumber] +") has been Added To The Dictionary")
						List[Wordnumber]=InputWords[Wordnumber] # Set the intial word as it is in the final Sentence.
						NumofcorrectWords +=1
						NumofWordsAddedToDic +=1
						time.sleep(2)

					elif (Choice=="4"):
						m="0"
						print("Loading....")
						time.sleep(2)
						# Inner loop to choose either accept the suggested word or not.
						while m not in ("1","2") :
							m=input("\nDid You Mean? :  " +SuggestedWord +"\n1-Yes! Thats the word \n2-No \n " )
							
							# If the Suggested word is correct.
							if (m=="1"): 
								List[Wordnumber]=SuggestedWord # Set the Suggested word in by it's order in the final Sentence.
								print("The Word (" + InputWords[Wordnumber] +") has been Corrected To ("+ List[Wordnumber] +").")
								NumofcorrectWords +=1
								NumofWordsChanged +=1
							
							#If the suggested word is incorrect.
							elif (m=="2"):  
								print("\nSorry our surmise is not correct, The Word (" + InputWords[Wordnumber] + ") Will Be Marked Incorrect")
								List[Wordnumber]=("?"+InputWords[Wordnumber]+"?") # Mark the word as incorrect in the final Sentence.
								NumofIncorrectWords +=1
							
							else:
								print("\nInvalid Input!!!  Try Again.\n")	

					else:
						print("\nInvalid Input!!!  Try Again.\n")
						time.sleep(2)

			Wordnumber +=1  # Each time "Wordnumber" increases by 1 , a new word from the the input Sentence will be Spell-Checked.

		# Creating Some Variables for a Well designed Summary Statitics.
		time.sleep(2)	
		today = date.today()
		Date=  today.strftime("%b-%d-%Y")
		now = datetime.now()
		Time = now.strftime("%H:%M:%S")	
		FinalSentence = ' '.join([str(elem) for elem in List])
		FinishTime=time.time()
		print("\nSpell-Check Completed!")
		time.sleep(2)

		# Our Great Script for the Summary.
		Summary=("Summary : \nTotal Number of Words: " + str(len(List)) +"\nthe number of words spelt correctly: " + str(NumofcorrectWords) + "\nthe number of incorrectly spelt words : " + str(NumofIncorrectWords)+ "\nthe number of words added to the dictionary : " + str(NumofWordsAddedToDic)+ "\nthe number of words changed by the user accepting the suggested word : " + str(NumofWordsChanged) + "\nDate : " + str(Date) +"      Time: " +str(Time)+"\nTime Elapsed : "+str(FinishTime-StartingTime) + " Seconds")
		print("\n\n\nYour Spell-Checked Sentence is : " + FinalSentence)
		print(Summary)
		time.sleep(3)

		#Creating a New File for step 8
		Filename=input("\n\nA new file that contains the output of this Spell-Check will be created, What do you wish to name it? : ")
		f=open(str(Filename)+".txt", "x")
		f.write(Summary + "\n\nOriginal Input : " + FilteredSentence + "\n\nSpell-Checked Input(Output) : " + FinalSentence)
		time.sleep(2)
		print("\n The File ("+Filename +".txt"+ ") has been created Successfully.")
		time.sleep(2)

		# After completing Spell-Checking 
		while True: 
			Restart= input("\n\n\nDo You Want To :  \n1-Go Back To Main Menu   \n2-Quit  \n")

			if (Restart=="1"):
				break

			elif (Restart=="2"):
				quit()

			else:
				print("\nInvalid Input!!!  Try Again. \n")			

	#Spell Check a File,,,,,,,,,,,,,,,,,,,,,,IMORTANT: Most of the operations for Spell-Checking a file are Copy-Pasted from above, so you will notice less commenting for duplicated operations.			
	elif (c == "2"): 
		X="0"

		#The loop for checking if the file exists(contains the inner spell-chaecking loop of course) 
		while X != "1" :

			FileName=input("Enter a file name :   ")
			CheckExist= os.path.isfile(FileName)
			
			# The File exists
			if (CheckExist==True):

				# Filter the file name into lowercase letters ONLY.
				RemoveExtension= [".".join(FileName.split(".")[:-1])]
				TurnToString=' '.join([str(elem) for elem in RemoveExtension])
				FileWord=words(TurnToString)
				InputWords= FileWord.split()
				print("The File exists, We will spell-check the word ("+FileWord+") for you.\n" )
				time.sleep(2)
				print("\nLoading....\n")
				time.sleep(2)

				# Declaring important variables before going into the "Spell-Checking loop".
				StartingTime=time.time()
				Wordnumber=0
				NumofIncorrectWords=0
				NumofcorrectWords=0
				NumofWordsAddedToDic=0
				NumofWordsChanged=0
				
				# List that will contain the output.
				List=[0]*len(InputWords) 

				# The Spell-Checking Loop.
				while Wordnumber < len(InputWords) : 

					# Resetting the variable to 0 each time a new word is going through the loop.
					count=0
					highestscore=0.0
					
					while count < len(Words_list):
					 	
						score= SequenceMatcher(None, InputWords[Wordnumber] , Words_list[count]).ratio()
						
						# If we found a matching word from the txt file.
						if (score == 1.0): 
							List[Wordnumber]= InputWords[Wordnumber] 
							count=len(Words_list) 
							NumofcorrectWords +=1

						# When The Word does'nt match
						else: 

							if (score > highestscore) : 

								highestscore = score
								SuggestedWord= Words_list[count] 

							else: 
								pass

						count +=1 # Each time "count" increases by 1 , a new word from the txt file will be tested.

					# If The Spell-Checking loop didnt find any matching word.
					if (score< 1.0) : 
						Choice="0"
						print("Oops!! The Word (" + InputWords[Wordnumber] +") is spelt Incorrectly , Do You Want To :  \n1-Ignore  \n2-Mark \n3-Add To Dictionary \n4-Suggest Likely Correct Spelling \n" )
						
						# A Sub-Menu to choose what to do with an incorrectly spelled word.
						while Choice not in ("1","2","3","4"): 
							Choice=input()

							if (Choice=="1"): 

								print("The Mistake will be Ignored")
								List[Wordnumber]=InputWords[Wordnumber] 
								NumofIncorrectWords +=1

							elif (Choice=="2"):
								
								List[Wordnumber]=("?"+InputWords[Wordnumber]+"?")
								print("The Word (" + InputWords[Wordnumber] +") has been Marked Successfully")	
								NumofIncorrectWords +=1

							elif (Choice=="3"):
								 # Add the word to the txt file.
								a = open("EnglishWords.txt", "a")
								a.write(str("\n") +str(InputWords[Wordnumber]))
								a.close()
								
								print("The Word (" + InputWords[Wordnumber] +") has been Added To The Dictionary")
								List[Wordnumber]=InputWords[Wordnumber] 
								NumofcorrectWords +=1
								NumofWordsAddedToDic +=1
								time.sleep(2)

							elif (Choice=="4"):
								m= "0"
								print("\nLoading.....")
								time.sleep(2)
								while m not in ("1","2") :

									m=input("\nDid You Mean? :  " +SuggestedWord +"\n1-Yes! Thats the word \n2-No \n " )

									# If the Suggested word is correct.
									if (m=="1"): 
										List[Wordnumber]=SuggestedWord 
										print("\nThe Word (" + InputWords[Wordnumber] +") has been Corrected To ("+ List[Wordnumber] +").")
										NumofcorrectWords +=1
										NumofWordsChanged +=1
									
									#If the suggested word is incorrect.
									elif (m=="2"):  
										print("\nSorry our surmise is not correct, The Word (" + InputWords[Wordnumber] + ") Will Be Marked Incorrect")
										List[Wordnumber]=("?"+InputWords[Wordnumber]+"?") # Mark the word as incorrect in the final Sentence.
										NumofIncorrectWords +=1

							else:
								print("\nInvalid Input!!!  Try Again.\n")
								time.sleep(2)			

					Wordnumber +=1  # Each time "Wordnumber" increases by 1 , a new word from the the input Sentence will be Spell-Checked.

				# Creating Some Variables for a Well designed Summary Statitics.
				time.sleep(2)	
				today = date.today()
				Date=  today.strftime("%b-%d-%Y")
				now = datetime.now()
				Time = now.strftime("%H:%M:%S")	
				FinalSentence = ' '.join([str(elem) for elem in List])
				FinishTime=time.time()
				print("\nSpell-Check Completed!")
				time.sleep(2)

				# Our Great Script for the summary.
				Summary=("\nSummary : \nTotal Number of Words: " + str(len(List)) +"\nthe number of words spelt correctly: " + str(NumofcorrectWords) + "\nthe number of incorrectly spelt words : " + str(NumofIncorrectWords)+ "\nthe number of words added to the dictionary : " + str(NumofWordsAddedToDic)+ "\nthe number of words changed by the user accepting the suggested word : " + str(NumofWordsChanged) + "\nDate : " + str(Date) +"      Time: " +str(Time)+"\nTime Elapsed : "+str(FinishTime-StartingTime) + " Seconds")
				print("\n\n\nYour Spell-Checked Sentence is : " + FinalSentence)
				print(Summary)
				time.sleep(3)

				#Creating a New File for step 8
				Filename=input("\n\nA new file that contains the output of this Spell-Check will be created, What do you wish to name it? : ")
				f=open(str(Filename)+".txt", "x")
				f.write(Summary + "\n\nOriginal Input : " + FileWord + "\n\nSpell-Checked Input(Output) : " + FinalSentence)
				time.sleep(2)
				print("\nThe File ("+Filename +".txt"+ ") has been created Successfully.")
				time.sleep(2)
				X="0"

				# After completing Spell-Checking
				while X not in ("1","2"): 
					X= input("\n\n\nDo You Want To :  \n1-Go Back To Main Menu   \n2-Quit  \n")
					
					if (X=="1"):
						break

					elif (X=="2"):
						quit()

					else:
						print("Invalid Input!!!  Try Again ")
						pass

			# If the file does not exist.			
			else:
				print("\nThe file does NOT exist!\n\n")
				X="0"
				sleep.time(2)

				while X not in ("1","2"):
					X=input("Do you want to : \n\n1-Go to main menu  \n2-Enter another file/directory")
					
					if (X=="2"):
						pass

					elif (X=="1"):
						break


					else:
						print("\n\nInvalid Input!! Try Again\n\n")
						pass	

	elif (c == "3"):
	
		quit()	


	else:
		print("Invalid input!! Try Again")
		

