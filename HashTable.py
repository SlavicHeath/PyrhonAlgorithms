###################################################################################
# Your name: Slavic Heath
###################################################################################


class HashTable:
    '''
    Create a hashtable to store words and tuples
    '''
    def __init__(self, size):
        # Create a list with 31 slots
        '''
        initialize size of the
        table data to be contained in each hash
        file to write updates on hash
        key - values in contained in table
        occupied - values result in conflict
        :param size: size of the table
        '''
        self.size = size
        self.data = [None] * self.size
        self.logfile = open("logfile.txt", "a")
        self.key = 0
        self.occupied = 0


    def store(self, word, data):
        '''
        store word and data tuple
        :param word: word from songs to be hashed
        :param data: tuple song data to be hashed with the word
        :return:None
        '''
        #Create a hash value
        hash_value = self.hash(word)

        # if Nothing contained in hash append word and tuple to hash
        if self.data[hash_value] is None:
            self.data[hash_value] = []
            self.data[hash_value].append(word)
            self.data[hash_value].append(data)
        else:
            # If the same value is found
            if self.data[hash_value][0] == word:
                self.data[hash_value].append(data)  # replace
            else:
                # Count number of collisions occupied and rehash
                self.occupied += 1
                next_slot = self.rehash(hash_value)
                while self.data[next_slot] is not None and self.data[next_slot] != word:
                    next_slot = self.rehash(next_slot)
                # update hash with the next slot
                if self.data[next_slot] is None:
                    self.data[next_slot] = []
                    self.data[next_slot].append(word)
                self.data[next_slot].append(data)

        # count number of keys in the hash table
        self.key += 1
        # if load factor exceeds 0.7 update log file and remap
        if self.load_factor() > 0.7:
            self.logfile.write("  " + str(self.key) + " keys read, HashTable expansion needed \n")
            self.logfile.write("     Before expansion: " + str(self) + "\n")
            self.remap()
            self.logfile.write("     After expansion: " + str(self) + "\n")

    # Load factor 2 items out of 11 = 0.2 if load factor exceed .7 add more hash
    def rehash(self, old_hash):
        '''
        rehash old hash value by adding one and modding to the list size
        :param old_hash: value of the old hash
        :return: new hash value
        '''
        return (old_hash + 1) % self.size

    def get(self, item):
        '''
        get the hashed value from hash table
        :param item: hashed value song
        :return: the songs found at the hashed item word
        '''
        slots_found = 0
        i = self.hash(item)
        # if key hash value found update number of slots looked at and return data contained in the hash key
        if self.data[i][0] == item:
            slots_found += 1
            return [self.data[i], slots_found]
        else:
            # iterate the through word hashes and find the key with its data
            while self.data[i][0] != item:
                slots_found += 1
                i += 1
            return [self.data[i], slots_found]  # Item at index of self.data

    def remap(self):
        '''
        Remap the hashtable to a new size updating hash values
        :return: None
        '''
        # Create new size with doubling the list size and finding its next prime with prime function
        new_size = self.get_next_prime(self.size * 2)
        # Create a new table
        new_table = HashTable(new_size)
        # Iterate through old hashes and add them to the new sized list
        for item in self.data:
            if item is not None:
                for song in item[1:]:
                    new_table.store(item[0], song)
        self.data = new_table.data
        self.size = new_size

    def load_factor(self):
        '''
        Get the load factor of the hash table
        :return: load factor
        '''
        # number of slots filled
        filled = 0
        #iterate trhough list and count number of slots filled
        for slot in self.data:
            if slot is not None:
                filled += 1
        # find load factor by dividing filled slots by the table size
        return filled / self.size

    def get_next_prime(self, num):
        '''
        Get next prime number to remap the size of the table
        :param num: value to be checked and found next prime
        :return: next prime number
        '''
        for i in range(num + 1, num + 200):
            if i > 1:
                pr = True
                for j in range(2, i):
                    if (i % j) == 0:
                        pr = False
                        break
                if pr:
                    return i

    def __str__(self):
        '''
        Get the string interplotation of the hashed table
        :return: number of slots in the table slots occupied and load factor
        '''
        return str(self.size) + " slots " + str(self.load_factor() * self.size) + " occupied, load factor = " + str(self.load_factor())

    def __repr__(self):
        return str(self)

    def hash(self, item):
        '''
        Hash words in the table
        :param item: song word to be hashed
        :return: slot at which word is hashed
        '''
        total = 0

        for i in range(len(item)):
            total += ord(item[i]) * (i + 1)

        slot_number = total % self.size
        return slot_number
# Assignment Hashing songs
# Hash word and create a list in that location adding all the song tuples to a list
# Hash_table = [None, Smoke > [song tuple, song tuple ...] None, None]
# Only full words smoke but not smoky
# Phrase search
# Load Factor stay bellow .7 do not let exceed
