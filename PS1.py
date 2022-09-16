import sys
import argparse
import time 

parser = argparse.ArgumentParser()
parser.add_argument('string1', type=argparse.FileType('r'))
parser.add_argument('string2', type=argparse.FileType('r'))
parser.add_argument('k', type=int)
args = parser.parse_args()

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
        print("---")


def cyclic(pattern, length):
    hash = ord(pattern[length-1])
    for i in range(length - 1):
        # key = "{0:b}".format(pattern[i+1])
        hash = hash ^ (ord(pattern[i])) << (length - i - 1)
        # print(hash)
    return hash


def hashlist(text1, text2, k, q):
    n = len(text1)
    m = len(text2)
    result = []
    for i in range(2**16):
        result.append(None)
    #First store each key {k1,k2,...,kn} of the text1 in a list of linked lists based on their hash values
    p = cyclic(text1, k)
    print(p)
    for i in range(n-k+1):
        if result[p] == None:
            #If there are not any elements index p then create a linked list and add the position and the key as its head
            elem = Node([i,text1[i:i+k]])
            linked = SLinkedList()
            linked.headval = elem
            result[p] = linked
        else:
            #If there are elements in that index go to the tail of the linked list and add the position and the key 
            position = Node([i,text1[i:i+k]])
            pointer = result[p].headval
            while pointer.nextval:
                pointer = pointer.nextval
            pointer.nextval = position
        #calculate the next hash value
        if i < n-k:
            a = (p << 1) ^ (ord(text1[i]) << k) ^ ord(text1[i+k])
            p=a
            if p < 0:
                p = p+q
    #Then, calculate each of the keys {l1,l2,...,ln} of the text2 and check whether there is a collision
    h = cyclic(text2, k)
    for i in range(m-k+1):
        #Check if there is an element on the table before with the same hash value
        if result[h] == None:
            print("There are no collisions.")
        else:
            #If there are elements that have the same hash value check wheter they are actually the same
            pointer = result[h].headval
            while pointer.nextval:
                flag = 1
                for l in range(k):
                    #if any of the characters are different then break the loop early
                    if text2[i+l] != pointer.dataval[1][l]:
                        flag = 0
                l+=1
                if flag==1:
                    #flag = 1 means that you traverse to the end of them and they're the same
                    print("There are collisions at positions:", i, ",", pointer.dataval[0])
                else:
                    #otherwise you broke the loop early then there are no collisions
                    print("There are no collisions.")
                pointer = pointer.nextval
        
        #calculate the next hash value
        if i < m-k:
            t = (h << 1) ^ (ord(text2[i]) << k) ^ ord(text2[i+k])
            h=t
            if h < 0:
                h = h+q


def default(text1, text2, k, q):
    n = len(text1)
    m = len(text2)
    result = {}
    for i in range(n-k+1):
        #calculate the default hash function for each key
        h = hash(text1[i:i+k])
        result[h] = [i,text1[i:i+k]]
    #Then, calculate each of the keys {l1,l2,...,ln} of the text2 and check whether there is a collision
    for i in range(m-k+1):
        #calculate the default hash function for each key
        h = hash(text2[i:i+k])
        if h in result.keys():
            print("There are collisions at positions:", i, ",", result[h])
        else:
            print("There are no collisions.")

        


text1 = args.string1.read().rstrip()
text2 = args.string2.read().rstrip()

q = 786433
# result = search(text1[:10], text2, q, 1)
# print(result)
k = args.k
# hashlist(text1, text2, k, q)
# print("00000000000000000000")
# default(text1, text2, k, q)
start_time = time.time()
with open('output1.txt', 'w') as h:
    sys.stdout = h
    hashlist(text1, text2, k, q)
    print("--- %s seconds ---" % (time.time() - start_time))



start_time = time.time()

with open('output2.txt', 'w') as g:
    sys.stdout = g
    default(text1, text2, k, q)
    print("--- %s seconds ---" % (time.time() - start_time))


