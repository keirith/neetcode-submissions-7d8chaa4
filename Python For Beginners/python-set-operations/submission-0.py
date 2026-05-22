from typing import List

def count_unique_words(words: List[str]) -> int:
    if len(words) == 0:
        return 0
    
    remove_dups = set(words)
    return len(remove_dups)

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
