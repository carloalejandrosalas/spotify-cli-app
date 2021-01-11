from services import Search
import json

class Spotify :
    def __init__(self):
        self.step = 'init'
        self.ask()
        self.searchOption = None

    def search(self, query):
        
        if self.searchOption == 'general'
            results = Search.general(query)

        elif self.searchOption == 'song'
            results = Search.songs(query)
        
        self.step = 'results'
        self.ask()

    def selectOption(self):
        pass

    def ask(self):
        if(self.step == 'init') :
            option = input("""
            What you Want to do?
            1 - Search
            2 - Song
            3 - Exit
            """)

            message = ''

            if option == '1':
                self.searchOption = 'general'
                message = 'Artist/Song/Playlist: '

            elif option == '2':
                self.searchOption = 'song'
                message = 'Name of song: '

            if option != '3':
                query = input(message)
                self.search(query)