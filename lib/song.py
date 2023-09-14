class Song:

    #Add class attribute for counts and genre so Song class keeps track
    # of them rather than the individual instances
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count() #class method called within __init__
        self.add_to_genres(genre)
        self.add_to_genre_count(genre)
        self.add_to_artists(artist)
        self.add_to_artist_count(artist)

    @classmethod #adds functionality to our method
    def add_song_to_count(cls): #increments the count when a song is added
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
       if genre not in cls.genres: # checks to make sure genre is not already in
        #our list and if not then it appends the passed in genre to the list
        # prevents duplicates
        cls.genres.append(genre)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count: #checks to see if the passed genre already exists
            # within our genre_count dict
            cls.genre_count[genre] += 1 #if it does then were gonna update our [genre] key
            #value to increment and set by 1
        else: #if the genre isn't already in our dict
            cls.genre_count[genre] = 1 #then were gonna add the new genre as the key and value to 1
            #since this is it's first instance(occurance)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists: #when adding artist we want to check to see
            # if the passed artist is not in our artists list already so we dont get duplicates
            cls.artists.append(artist) # if not already there then it adds the passed artist
            

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count: #checks if artist already exists in our dict
            cls.artist_count[artist] += 1 #if it does then we want to update that artist
            # key value +1
        else: #if artist doesn't already exist 
            cls.artist_count[artist] = 1 #then add the artist as the key and set value to 1
