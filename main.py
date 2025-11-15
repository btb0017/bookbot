from stats import get_num_words, get_num_chars, sort_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        
        return file_contents
   

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")

    line_1 = f"Analysing book found at {sys.argv[1]}..."
    print(line_1)
    print("----------- Word Count ----------")
    
    text = get_book_text(sys.argv[1])
    
    num_words = get_num_words(text)
    result = f"Found {num_words} total words"
    print(result) 
    print("--------- Character Count -------")
    
    num_chars = get_num_chars(text)
    char_list = sort_dict(num_chars)
    
    for item in char_list:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

        
main()