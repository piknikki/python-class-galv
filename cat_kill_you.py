list_of_questions = {
    "How often does your cat press on your internal organs?": ["daily", "weekly", "monthly", "never"],
    "Has your cat ever left a 'present' on your doorstep? Note: this isn't a gift; it's a warning.": ["many times", "a few times", "never"],
    "Does your cat like to engage in staring contests with you? Never look away; this is how your cat tests your strength and resolve.": ["often", "sometimes", "never"],
    "Does your cat stare at you while hiding in dark places?": ["often", "sometimes", "never"],
    "Does your cat typically stay up at night?": ["often (my cat is like Batman if he pooped in a box)", "sometimes", "never"],
    "Does your cat sleep on your electronics?": ["often (my cat is trying to disrupt communications to the outside world)", "sometimes", "never"],
    "How often does your cat give you the stink eye?": ["daily", "weekly", "monthly", "never"],
    "When you enter a room, does your cat suddenly sprint out of it? This is a failed ambush.": ["often", "sometimes", "never"],
    "Does your cat kick litter all over the room? This is practice for burying bodies.": ["often", "sometimes", "never"],
    "Does your cat paw at your face while you sleep?": ["often (my face is a nocturnal sparring bag)", "sometimes", "never"],
    "Please give your cat a once-over to estimate their Spooky MurderRageSauce. Be fair. ": ["Scale of 1 to 10"]
}

murder_sauce = 0  # global variable

def display_starting_message():  # opening message
    """
    print a beginning message
    """
    starting_message = "Is your cat plotting to kill you??  \nLet's find out.  \n(Please note that this is merely a pythonic presentation of an app created by The Oatmeal. \nI do not claim credit for its brilliance. I'm just trying to learn Python.)"
    print(starting_message)

def check_murder_sauce(question, response):
    """
    check responses for lower case, keep track of score in global variable
    """
    global murder_sauce
    responses_low = 'never'
    responses_med = 'weekly', 'monthly','sometimes', 'a few times'
    responses_high = 'daily', 'often', 'many times'
    if response.lower() in responses_low:
        murder_sauce += 3
    elif response.lower() in responses_med:
        murder_sauce += 8
    elif response.lower() in responses_high:
        murder_sauce += 10
    elif response.isdigit():
        murder_sauce += 10
    else:
        print("You didn't answer correctly. Follow directions plz.")

def murder_sauce_result(murder_sauce):
    """
    use global variable to print a result, depending on score
    """
    if murder_sauce < 30:
        print("There is a {}% chance your cat is plotting to kill you.".format(str(murder_sauce)))
        print("You lucky bastard! Watch your step; this result could change at any moment.")

    elif 30 <= murder_sauce < 60:
        print("There is a {}% chance your cat is plotting to kill you.".format(str(murder_sauce)))
        print("May your death be merciful and just.")

    elif 60 <= murder_sauce:
        print("There is a {}% chance your cat is plotting to kill you.".format(str(murder_sauce)))
        print("Been nice knowing you. You will be missed.")

def play():
    """
    print questions one at a time
    keep track of murder sauce in global variable
    print result
    """
    display_starting_message()
    print("")
    print("*"*10)
    for question_number, question in enumerate(list_of_questions):
        print(question)
        print("")
        for responses in list_of_questions[question]:
            print(responses)
        pick_one = input("pick one: ")
        check_murder_sauce(question, pick_one)

    print(murder_sauce_result(murder_sauce))
