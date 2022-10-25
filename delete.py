import difflib

string1 = "I love to eat apple."
string2 = "I do not like to eat pineapple."

temp = difflib.SequenceMatcher(None, string1, string2)

print(temp.get_matching_blocks())
print("Similarity Score: ", temp.ratio())
