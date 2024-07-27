def searchEngine():
        map = {1:'DeepSeaVisitor', 2:'SteelCushion', 3:'TheBrimstone', 4:'StarlightEngine', 5:'Housekeeper', 6:'DrillRigRedAxis', 7:'KaboontheCanoon'}
        while(True):
            try:
                WEngine = int(input("Please choose your W-Engine!\n [1:DeepSeaVisitor][2:SteelCushion][3:TheBrimstone][4:StarlightEngine][5:Housekeeper][6:DrillRigRedAxis][7:KaboontheCanoon]\n >>>"))
                if WEngine in map:
                    chosen_engine = map[WEngine]
                    print(f"You have chosen: {chosen_engine}")
                    return chosen_engine
                else:
                    print("Invalid choice. Please enter a number between 1 and 7.")
            except:
                print("Invalid input. Please enter a number between 1 and 7.") 