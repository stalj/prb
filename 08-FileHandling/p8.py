file_name = '08-FileHandling\pets.txt'

# Function to count words
def count_words(text):
    words = text.split()
    return len(words)

# Read and process the file
try:
    with open(file_name, 'r') as file:
        content = file.read()
        print("Text from the file:")
        print(content)  # Print the text
        word_count = count_words(content)
        print(f"\nNumber of words in the text: {word_count}")
except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")