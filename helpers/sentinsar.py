import paralleldots
def return_sentiments(msg) :
    paralleldots.set_api_key("b6IJBihauZBESHXNQdWtO9ODVyzJDauTG3ntQePKRDY")
    response = paralleldots.sentiment(msg,"en")
    return  "Negative % "+str(response['sentiment']['negative'])+" Positive % " + str(response ['sentiment']['positive']) + " Neutral % " + str(response['sentiment']['neutral'])

def return_sarcasm(msg) :     
    paralleldots.set_api_key("b6IJBihauZBESHXNQdWtO9ODVyzJDauTG3ntQePKRDY")
    response=paralleldots.sarcasm(msg) 
    return  "Non-Sarcastic % "+ str(response['Non-Sarcastic']) + " Sarcastic %  " + str(response['Sarcastic']) 


print (return_sentiments("I hurt myself today"))
print(return_sarcasm("I'm heartless"))