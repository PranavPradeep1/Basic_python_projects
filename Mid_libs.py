# Mad Libs Generator

print("Welcome to the Mad Libs Generator!")
print("Please enter the following words:\n")

adjective1 = input("Adjective: ")
noun1 = input("Noun: ")
verb1 = input("Verb (past tense): ")
adverb = input("Adverb: ")
adjective2 = input("Another adjective: ")
noun2 = input("Another noun: ")
verb2 = input("Verb: ")

# Create the story
story = f"""
One {adjective1} day, a {noun1} {verb1} {adverb} through the park.
It was a very {adjective2} afternoon, and everyone was watching.
Suddenly, the {noun1} spotted a {noun2} and decided to {verb2}.
The crowd cheered, and the adventure became a legendary story!
"""

print("\n--- Your Mad Libs Story ---")
print(story)