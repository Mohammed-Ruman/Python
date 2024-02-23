# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

def main():
    print(replace_poor_good(get_input()))


def replace_poor_good(sentence):
    not_index=sentence.find("not")
    poor_index=sentence.find("poor")

    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        return sentence[:not_index]+"good"+sentence[poor_index+4:]
    else:
        return sentence
    

def get_input():
    return input("Enter the String? ")
    

main()