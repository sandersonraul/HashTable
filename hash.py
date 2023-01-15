
def display_hash(hashtable):
	
	for i in range(len(hashtable)):
		print(i, end = " ")
		
		for j in hashtable[i]:
			print("->", end = " ")
			print(j, end = " ")
			
		print("-> \ ")

def Hashing(keyvalue):
	return keyvalue % len(hashtable)

def insert(hashtable, keyvalue):
	hash_key = Hashing(keyvalue)
	hashtable[hash_key].append(keyvalue)
    
inputs = int(input())

for i in range(inputs):
    args = input().split()
    size = int(args[0])
    inputs_number = int(args[1])
    hashtable = [[] for _ in range(size)]
    numbers = input().split()
    for j in range(inputs_number):
        insert(hashtable, int(numbers[j]))
    display_hash(hashtable)