def matchingStrings(strings, queries):
    # Write your code here
    no_occurance = [strings.count(query) for query in queries]
    print(no_occurance)
        

str_strings = """abcde
sdaklfj
asdjf
na
basdn
sdaklfj
asdjf
na
asdjf
na
basdn
sdaklfj
asdjf""".splitlines()
print(str_strings)

str_queries = """abcde
sdaklfj
asdjf
na
basdn""".splitlines()
print(str_queries)

matchingStrings(strings=str_strings,queries=str_queries)