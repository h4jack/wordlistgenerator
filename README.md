# Password Wordlist Generator
This Python script generates a wordlist of passwords based on the combinations of input words provided. It's a handy tool for generating potential passwords for security testing or other purposes.
## Usage

#### Clone the Repository:

```cmd
git clone https://github.com/h4jack/wordlistgenerator.git
```

#### Navigate to the Directory:
```cmd
cd wordlistgenerator
```

#### Run the Script:
```cmd
python main.py <filename> [-l <length>] [-v] <word1> <word2> ...
```
- `<filename>:` Name of the file to save the wordlist.
- `-l, --length:` (Optional) Length of combined words (default: None).
- `-v, --verbose:` (Optional) Enable verbose output.
- `<word1> <word2> ...:` List of words to generate combinations from.

#### Example:
Generate a wordlist with combinations of words "hello", "@" and "123" and save it to a file named "wordlist.txt":
```cmd
python main.py wordlist.txt -l 3 "hello" "@" "123"
```

## Features
- Customizable: You can specify the length of the combined words to generate varied password lengths.
- Verbose Output: Enable verbose mode to see detailed progress information while generating the wordlist.
- Flexible Input: Input any number of words to be combined into passwords.

## Tech Stack
**Language:** Python 3.x+

## Authors
- [@h4jack](https://www.github.com/h4jack)

## License
This project is licensed under the [MIT License](https://github.com/h4jack/wordlistgenerator/blob/main/LICENSE/)

## Feedback
If you have any feedback or suggestions, please feel free to [create an issue](https://github.com/h4jack/wordlistgenerator/issues) or [contact us](https://github.com/h4jack).