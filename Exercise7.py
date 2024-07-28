# Exercise 7: Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.

# Given:

# str_x = "Emma is good developer. Emma is a writer"
# Expected Output:

# Emma appeared 2 times

def word_count(x):
    word_x = x.split()
    word_dict = {}
    
    for word in word_x:
        if word in word_dict:
            word_dict[word] += 1
            
        else:
            word_dict[word] = 1
    
    for word, count in word_dict.items():
        print(f"{word} appered {count} times.")
            
if __name__ == "__main__":
    y = str(input("Enter your string: "))
    word_count(y)