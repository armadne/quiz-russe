import random

question = ("where are you from", "I am from ....", "bye (informal)", "goodbye (formal)", "see you", "nice to meet you"
            "my russian isn't good", "what ?", "How to I get to the (destination_name) ?", "How much does it cost ?", "I don't understand",
            "I understand", "Bonne apétit", "Tastes good", "I like it", "I don't like it", "It's my first time in Russia", "a little bit",
            "maybe", "maybe not (don't really want to)")



for i in range(4):
    
    robot = random.choice(question)
    
    
    print(robot)
    you = input("Translate the word or the phrase: ")

    if robot == "where are you from ?" and you == "vi atkoda":
        print("Correct")

    elif robot == "I am from ...." and you == "Ya iz ....":
        print("Correct")
        
    elif robot == "bye (informal)" and you == "paka":
        print("Correct")
        
    elif robot == "goodbye (formal)" and you == "dasvidania":
        print("Correct")
        
    elif robot == "see you" and you =="ouvidimsieuh":
        print("Correct")
        
    elif robot == "nice to meet you" and you == "rad vstréché":
        print("Correct")
        
    elif robot == "My russian isn't good" and you == "ya ploho govoryou po rouski":
        print("Correct")
        
    elif robot == "What ?" and you == "chto":
        print("Correct")

    elif robot == "How to I get to the (destination_name) ?" and you == "kak pratyk ?":
        print("Correct")
        
    elif robot == "How much does it cost ?" and you == "skolka éta stoïte ?":
        print("Correct")
        
    elif robot == "I don't understand" and you == "ya niè panimayou":
        print("Correct")
        
    elif robot == "I understand" and you == "ya panimayou":
        print("Correct")
        
    elif robot == "Bonne apétit" and you == "Priyatnava apetita":
        print("Correct")
        
    elif robot == "Tastes good" and you == "vkousna":
        print("Correct")
        
    elif robot == "I like it" and you == "mné nravitsya":
        print("Correct")
        
    elif robot == "I don't like it" == "mné niè nravitsya":
        print("Correct")
        
    elif robot == "It's my first time in Russia" and you == "yav perveuiy rassi":
        print("Correct")
        
    elif robot == "a little bit" and you == "nimnogueuh":
        print("Correct")
        
    elif robot == "maybe" and you == "navièrna":
        print("Correct")
        
    elif robot == "maybe not (not really want to)" and you == "Da nyète navièrna":
        print("Correct")
        
    else:
        print("Incorrect")