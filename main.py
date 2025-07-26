#Ancien Programme supprimé et reinstallé à partir de replit
#Programme pour remplir le fichier todo.txt
maDate = input("Entrez une date au format jj/mm/aaaa : ")
#Espagnol
tacheDuolingo = input("Avez-vous fait Duolingo : ")
tacheMosalingua = input("Avez-vous fait mosalingua : ")
tacheCafeynVocable = input("Avez-vous lu un caféyn ou vocable : ")
tacheMondly = input("Avez-vous fait Mondly : ")
#Japonais
tacheKana = input("Avez-vous fait Kana : ")
tacheDrops = input("Avez-vous fait les drops : ")
tacheMosaJaponais = input("Avez-vous fait Mosa Japonais : ")
tachekawai = input("Avez-vous fait Kawai : ")
tacheMinnaNoNihongo = input("Avez-vous fait Minna no Nihongo : ")
#Python
tacheGithub = input("Avez-vous un commit : ")
tacheDatacamp = input("Avez-vous fait Datacamp : ")
tachetuto = input("Avez-vous fait un tuto : ")
tachereplit = input("Avez-vous fait du Replit : ")
tacheRealPython = input("Avez-vous fait Real Python : ")
#Sport/Sante
tacheSport = input("Avez-vous fait du sport : ")
tacheApprentissage = input("Avez-vous fait de l'apprentissage : ")
tacheDiet = input("Avez-vous noté vos repas : ")
#Famille
tacheFamille = input("Avez-vous fait un truc pour la  famille : ")

#on affiche les résultats dans le fichier todo
#on teste

fichier = open("todo.txt", "a")
#écrire dans le fichier
fichier.write("Date : " + maDate + "\n\n")
fichier.write("Version 01 : \n")
#Espagnol
fichier.write("Objectifs Espagnol\n")
fichier.write("Duolingo : " + tacheDuolingo + "\n")
fichier.write("Mosalingua : " + tacheMosalingua + "\n")
fichier.write("Caféyn vocable : " + tacheCafeynVocable + "\n")
fichier.write("Mondly : " + tacheMondly + "\n")

#Japonais
fichier.write("Objectifs Japonais\n")
fichier.write("Kana : " + tacheKana + "\n")
fichier.write("Drops : " + tacheDrops + "\n")
fichier.write("Japonais : " + tacheMosaJaponais + "\n")
fichier.write("Kawai : " + tachekawai + "\n")
fichier.write("Minna no Nihongo : " + tacheMinnaNoNihongo + "\n")
#Python
fichier.write("Objectifs Python\n")
fichier.write("Github Commit : " + tacheGithub + "\n")
fichier.write("Datacamp : " + tacheDatacamp + "\n")
fichier.write("Tuto : " + tachetuto + "\n")
fichier.write("Repli : " + tachereplit + "\n")
fichier.write("Real Python : " + tacheRealPython + "\n")
#Sport/Sante
fichier.write("Objectifs Sport/Sante\n")
fichier.write("Sport : " + tacheSport + "\n")
fichier.write("Apprentissage : " + tacheApprentissage + "\n")
fichier.write("Regime : " + tacheDiet + "\n")

#Famille
fichier.write("Objectifs Famille\n")
fichier.write("Famille : " + tacheFamille + "\n")
fichier.write("===================================\n")
#fermer le fichier
fichier.close()
print("Fichier todo.txt mis à jour")
