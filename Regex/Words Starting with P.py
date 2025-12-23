import re

try:
    # Read a line of input from the user
    st = input()

    # Regular expression explanation:
    # \b        -> word boundary (ensures match starts at the beginning of a word)
    # p         -> matches the letter 'p'
    # \w*       -> matches zero or more word characters after 'p'
    #
    # flags=re.IGNORECASE:
    # Allows matching both lowercase 'p' and uppercase 'P'
    #
    # This extracts all words that start with 'p' or 'P'
    opt = re.findall(r'\bp\w*', st, flags=re.IGNORECASE)

    # Print the list of matched words
    print(opt)

except Exception as e:
    # In case of any unexpected runtime error, print an empty list
    print([])
