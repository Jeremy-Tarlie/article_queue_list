class Choose:
    def main_menu(queue_article, history):
        while True:
            print("\n=== Menu ===")
            print("1. Lire un article de la file")
            print("2. Afficher le dernier article lu depuis l'historique")
            print("3. Quitter l'application")
            
            choice = input("Choisissez une option : ")
            
            if choice == "1":
                if queue_article.isEmpty():
                    print("La file d'attente est vide. Aucun article à lire.")
                else:
                    article = queue_article.dequeue()
                    title, url = article
                    print(f"\nTitre : {title}\nURL : {url}")
                    history.push(article)
            elif choice == "2":
                if history.isEmpty():
                    print("L'historique est vide. Aucun article consulté.")
                else:
                    last_article = history.pop()
                    title, url = last_article
                    print(f"\nDernier article lu :\nTitre : {title}\nURL : {url}")
            elif choice == "3":
                print("Au revoir !")
                break
            else:
                print("Option invalide. Veuillez réessayer.")