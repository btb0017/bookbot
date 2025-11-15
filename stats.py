   
def get_num_words(text):
    num_words = 0
    word_list = [] 
    word_list = text.split()
    
    for word in word_list:
        num_words += 1
    
    return num_words
    
    
def get_num_chars(text):
    
    lower_text = text.lower()
    
    chars = {}
    
    for ch in lower_text:
        if ch in chars:
            chars[ch] += 1
        else:
            chars[ch] = 1
    
    return chars


def sort_dict(chars):
    char_list = []
    
    for ch, num in chars.items():
        if ch.isalpha():
            new_dict = {"char": ch, "num": num}
            char_list.append(new_dict)
        else:
            continue
        
    char_list.sort(key=sort_on, reverse=True)
    
    return char_list

def sort_on(d):
    return d["num"]