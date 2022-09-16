## Name: Common Sub-Strings Problem Set-1 Question-4 

## Usage
python PS1.py string1 string2 k

## Explanation
Here I used two different approaches to solve the problem searching for common substrings of two different strings.

The first one is done with using Cyclic Rolling Hash Function. I will explain my algorithm step by step.

1. Since there are two strings I will firstly take the first string and hash the keys into a list of linked lists. 
2. The hash function that I used is the cyclic polynomial function that I explained in the third question. I implemented that function in the function cyclic.
3. How my code hash the key into hash table is so trivial, it is taking their hash values (h_k) from the cyclic function and go to the h_k'th index of the result array.
4. If there is an element in that index it will traverse the linked list and put the new one into the tail. Otherwise it is going to create a new linked list and add the new element as its head.
5. After our job is done with the first string we move on to the second string.
6. I used the same hash function to the second string's keys but now I didn't add them into the list. I just checked whether the hash'th index of the list is empty or not.
7. If it is empty I just simply wrote that "There are no collisions." to the file. Otherwise, I checked whether they are really the same bit-by-bit. If they are the same I wrote the index of the both same keys on the strings.

Also, I created the linked list class with Nodes.

The second one is much more easier because I used the built-in hash function and the dictionary of Python.

1. Since there are two strings I will firstly take the first string and hash the keys into a dictionary.
5. After our job is done with the first string we move on to the second string.
6. I used the same hash function to the second string's keys but now I didn't add them into the dictionary. I just checked whether the dictionary has the same key or not.
7. If it has I just simply wrote that "There are no collisions." to the file. Otherwise, I checked whether they are really the same bit-by-bit. If they are the same I wrote the index of the both same keys on the strings.


## Testing
I did a bunch of tests with several inputs and k sizes and checked whether the results are correct by using online tools. And also I compared the two different functions. You can find the comparison in the .pdf file that I uploaded.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
