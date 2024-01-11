import random

questions = ["Good to see you", "I am a pilot", "she is not a captain", "she", "he", "here, ici", "a cook", "coach", "you are a teacher", "this is",
             "Are you a doctor","Is this Dima ?", "Je parle russe", "where ?" , "You", "who ?", "friend", "I am here", "My", "who is there", "this is my friend Mark",
             "Is she here ?", "Who are you ?", "he is an idiot", "food", "ideal"]




for i in range(5):
    
    robot = random.choice(questions)
    
    print(robot)
    
    you = input("Translate the word or phrase: ")
    
    
    if robot == "Good to see you" and you == "rad tibyé vityète":
        print("Correct")
    
    elif robot == "I am a pilot" and you == "ya pilot":
        print("Correct")
        
    elif robot == "she is not a captain" and you == "ona nié capitane":
        print("Correct")
        
    elif robot == "she" and you == "ona":
        print("Correct")
        
    elif robot == "he" and you == "one":
        print("Correct")
        
    elif robot == "here" and you == "zdisse":
        print("Correct")
        
    elif robot == "a cook" and you == "Poveure":
        print("Correct")
        
    elif robot == "coach" and you == "trénère":
        print("Correct")
        
    elif robot == "you are a teacher" and you == "vi ouchitèle":
        print("Correct")
        
    elif robot == "this is" and you == "eta, eto":
        print("Correct")
        
    elif robot == "Are you a doctor" and you == "vi doctor":
        print("Correct")
        
    elif robot == "Is this Dima ?" and you == "eto Dima":
        print("Correct")
    
    elif robot == "I speak russian" and you == "ya govoryou po rousski":
        print("Correct")
        
    elif robot == "where" and you == "gdé":
        print("Correct")
        
    elif robot == "you, tu" and you == "ti":
        print("Correct")
        
    elif robot == "you , vous" and you == "vi":
        print("Correct")
        
    elif robot == "who" and you == "kto":
        print("Correct")
        
    elif robot == "he is an idiot" and you == "one idiot":
        print("Correct")
        
    elif robot == "friend" and you == "droug":
        print("Correct")
        
        
    elif robot == "I am here" and you == "ya zdisse":
        print("Correct")
        
    elif robot == "my" and you == "moy":
        print("Correct")
        
    elif robot == "who is there" and you == "kto zdisse":
        print("Correct")
        
    elif robot == "this is my friend Mark" and you == "eto my droug Mark":
        print("Correct")
        
    elif robot == "Is she here ?" and you == "ona zdisse":
        print("Correct")
    
    elif robot == "Who are you" and you == "kto ti":
        print("Correct")
        
    elif robot == "food" and you == "yèda":
        print("Correct")
        
    elif robot == "ideal" and you == "idealni":
        print("Correct")
        
    else:
        print("Incorrect")
     



