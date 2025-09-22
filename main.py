from stats import get_word_count, get_char_count, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as x:
        return x.read()


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    print('============ BOOKBOT ===========')
    print(f'Analyzing book found at {book_path}...')
    print('----------- Word Count ----------')
    text = get_book_text(f'{book_path}')

    count = get_word_count(text)
    print(f'Found {count} total words')

    print('--------- Character Count -------')
    char_count = get_char_count(text)
    

    sorted_dict=sort_dict(char_count)
    for item in sorted_dict:
        c = item["char"]
        if not c.isalpha():
            continue
        n = item["num"]
        print(f"{c}: {n}")
    print('============= END ===============')

if __name__ == '__main__':
    main()