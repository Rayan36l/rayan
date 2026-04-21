# File: average_vowels.py

# --- 1. Counting Vowels ---
def counting_vowels_and_consonants(s):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return (v_count, c_count)

# --- 2. Average Vowels ---
def average_vowels_and_consonants(paragraph):
    sentences = paragraph.replace("!", ".").split(". ")
    sentences = [s for s in sentences if s.strip()]
    
    num_sentences = len(sentences)
    total_vowels = 0
    total_consonants = 0
    
    for s in sentences:
        v, c = counting_vowels_and_consonants(s)
        total_vowels += v
        total_consonants += c
        
    avg_vowels = total_vowels / num_sentences
    avg_consonants = total_consonants / num_sentences
    
    return (num_sentences, avg_vowels, avg_consonants)

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# --- Output ---
num_s, avg_v, avg_c = average_vowels_and_consonants(paragraph)

print("Analysis of Feynman's Quote:")
print(f"Total Sentences: {num_s}")
print(f"Average Vowels per Sentence: {avg_v:.2f}")
print(f"Average Consonants per Sentence: {avg_c:.2f}")