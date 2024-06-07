import sys
import argparse
import itertools

def generate_wordlist(words, combination_length=None, verbose=False):
    """
    Generate all possible combinations of the given words with specified length.
    
    Args:
        words (list): List of words
        combination_length (int): Length of combined words (default: None)
        verbose (bool): Flag to enable verbose output (default: False)
    
    Returns:
        list: List of all combinations of the given words with specified length
    """
    if combination_length is None:
        combinations = []
        for length in range(1, len(words) + 1):
            combinations.extend(generate_wordlist(words, length, verbose))
        return combinations
    
    wordlist = []
    total_combinations = len(list(itertools.combinations(words, combination_length)))
    for i, combination in enumerate(itertools.combinations(words, combination_length), start=1):
        if not verbose:
            sys.stdout.write(f"\rGenerated {i}/{total_combinations} combinations")
            sys.stdout.flush()
        if verbose:
            print(f"Generating combination {i}/{total_combinations}: {' '.join(combination)}")
        wordlist.extend([''.join(comb) for comb in itertools.permutations(combination)])
    if not verbose:
        print("\nGeneration completed.")
    return wordlist

def save_wordlist_to_file(wordlist, filename, verbose=False):
    """
    Save the wordlist to a file.
    
    Args:
        wordlist (list): List of words
        filename (str): Name of the file to save the wordlist
        verbose (bool): Flag to enable verbose output (default: False)
    """
    with open(filename, 'w') as file:
        for i, word in enumerate(wordlist, start=1):
            file.write(word + '\n')
            if verbose:
                print(f"Saved {i} words to {filename}", end='\r')
    if verbose:
        print(f"Saved all {len(wordlist)} words to {filename}")

def main(args):
    """
    Main function to execute the program.
    """
    parser = argparse.ArgumentParser(description="Generate a wordlist and save it to a file.")
    parser.add_argument("filename", help="Name of the file to save the wordlist")
    parser.add_argument("-l", "--length", type=int, default=None, help="Length of combined words (default: None)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("words", nargs="+", help="List of words")
    args = parser.parse_args(args)

    if not args.words:
        print("Error: No words provided.")
        return
    if args.length is not None and args.length <= 0:
        print("Error: Invalid length of combined words. Length should be greater than 0.")
        return

    wordlist = generate_wordlist(args.words, args.length, args.verbose)
    save_wordlist_to_file(wordlist, args.filename, args.verbose)
    print("Wordlist saved to", args.filename)
    if not args.verbose:
        print("Number of passwords generated:", len(wordlist))

if __name__ == "__main__":
    main(sys.argv[1:])
