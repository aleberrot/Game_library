games = []


def library(): 
    user_input = input("""\n Welcome to the Game Dex, input:\n
    a => For adding a new game.

    d => For deleting a game.

    r => For displaying all the games.
    
    f => For finding  a game.

    s => For stopping the program.\n""").lower()
    while user_input != 's':
        if user_input == "a":
            addGame()
            library()
            break
            
        elif user_input == "r":
             showGames()
             library()
             break
            
        elif user_input == "f":
            looking_for = input("What do you want to delete?=> ").title()
            game = list(filter(lambda x: x['Title'] == looking_for, games)) 
            print(f"""
            Title => {game['Title']}
            Year => {game['Year']}
            Argument => {game['Argument']}
            Calification => {game['Calification']}""" or 'No games found.')
            library()
            break
          
        elif user_input == "d":
            looking_for = input("What do you want to delete?=> ").title()
            game = list(filter(lambda x: x['Title'] == looking_for, games))
            for game in games:
                if game in games: games.remove(game)
            library() 
            break

        else:
            print('Unknown command, please try again')
            library()
            break
            
def addGame():
    try:
        new_game = {
            'Title': input('Game title => ').title(),
            'Year': int(input('Game year => ')),
            'Argument': input('Game argument => '),
            'Calification': int(input('Game calification => '))
        }
        
        if new_game['Calification'] > 10 or new_game['Calification'] < 1:  raise Exception
        games.append(new_game);
    except ValueError as error: print('\n Fill with numbers')
    except Exception as error: print('\n Only values between 1 and 10') 

def showGames():
        for game in games:
            print(f"""
            Title => {game['Title']}
            Year => {game['Year']}
            Argument => {game['Argument']}
            Calification => {game['Calification']}""")
        if len(games): print('There are no games in the library')

library()
