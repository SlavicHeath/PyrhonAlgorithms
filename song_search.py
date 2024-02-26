###################################################################################
# Your name:Slavic Heath
###################################################################################
from HashTable import HashTable

def build_hash_table(filename):
    print("Building hash table using data in", filename)
    #initiate hash table
    hash_table = HashTable(31)
    with open(filename, 'r') as f:
        # Strip from charcters other than words and change to lower
        for line in f:
            line = line.strip()
            line = line.split(' :: ')

            title = line[0].split(' ')

            song = (int(title[0]), ' '.join(title[1:]), line[1])

            for word in title[1:]:
                word = word.lower()
                new_word = ""
                for letter in word:
                    if letter.isalpha():
                        new_word = new_word + letter
                hash_table.store(new_word, song)
        # Update the logfile function
        hash_table.logfile.write("End reading songs from file " + filename + "\n")
        hash_table.logfile.write("HashTable details: " + str(hash_table) + "\n")
        hash_table.logfile.write("Number of unique keys inserted into HashTable = " + str(hash_table.key) + "\n")
        hash_table.logfile.write("Number of key conflicts encountered = " + str(hash_table.occupied) + "\n")
    return hash_table


def find_words(hash_table, filename):
    # For each word listed in filename
    # find corresponding song titles in hash_table and
    # print the results out in the format
    # shown in assignment
    print("Searching for words listed in ", filename)
    with open(filename, 'r') as f:
        slot_found = 0
        # Iterate through file seperating by word from the song title
        for line in f:
            line = line.strip()
            result = hash_table.get(line)
            song_list = result[0]


            print()
            print(str(len(song_list) - 1) + " songs contain the word " + line + " in their title")
            print()
            # Get the song number Title and Artist
            for num in range(1, len(song_list)):
                slot_found += 1
                song_tuple = song_list[num]
                output = str(num) + '. ' + str(song_tuple[0]) + ", " + song_tuple[1] + ", " + song_tuple[2]
                print(output)
            print()
            print("This search examined " + str(slot_found) + " slots in the hash table")
    return None


def find_phrases(hash_table, filename):
    # For each phrase listed in filename
    # find corresponding song titles in hash_table and
    # print the results out in the format
    # shown in assignment
    print("Searching for phrases listed in ", filename)
    with open(filename, 'r') as f:
        slot_found = 0
        for line in f:
            line = line.strip()
            phrase = line.split(' ')
            result = hash_table.get(phrase[0])
            song_list = result[0]

            count = 0
            songs = []
            for song in song_list:
                slot_found += 1
                if song != song_list[0]:
                    title = song[1].lower()
                    if line in title:
                        songs.append(song)
                        count += 1

            print()
            print(str(count) + " songs contain the phrase " + line + " in their title")
            print()

            count = 0
            for song in songs:
                count += 1
                output = str(count) + '. ' + str(song[0]) + ", " + song[1] + ", " + song[2]
                print(output)
            print()
            print("This search examined " + str(slot_found) + " slots in the hash table")
    return None


def main():
    hash_table = build_hash_table("songs.txt")

    find_words(hash_table, "words.txt")

    find_phrases(hash_table, "phrases.txt")


main()
