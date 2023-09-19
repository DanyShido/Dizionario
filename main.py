meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            }


while True:
    parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")
    if parola in meme_dict.keys():
        print(parola, meme_dict[parola])
    else:
        print("la parola inserita non è all'interno del mio database")
    x= input("vuoi continuare? y or n")
    if x == "n":
        print("Arrivederci")
        break
