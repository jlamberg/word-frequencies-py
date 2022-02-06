# Word Frequencies

Read and print word frequencies from a given text file.

## Usage

```bash
python main.py <YOUR INPUT FILE HERE>
```

## Input

The file content is expected to be Unicode text, emojis, URLs, mentions, hashtags, and sequencies of emojis–basically anything that you would see in chats and on social media.

To get a better idea, you can take a look at the [example input](data/example_input.txt).

## Output

Sample output could look like this:

```text
Whose 1
track 1
is 1
familiar!😍 1
This 1
sounds 1
this? 1
```

## TODO

- Write tests.
- Think of a proper folder structure.
- Write the definition of a word in the context of this application.
- Split emojis from the end of a word.
- Split emojis from the beginning of a word?
- Split sequences of emojis so that they are each counted as a separate word.
- Trim most special characters from the end of a word.
- Trim most special characters from the beginning of a word.
- Treat mentions (@foobar, any characters until the next space) as one word and don't trim it.
- Treat hashtags (#foobar, including numbers and underscores until the next space) as one word and don't trim it.
- Don't count sequencies of special characters as words.
- Check that a URL is counted as one word.
- Make sure it works on Python 3.x.
- Use virtualenv.

## License

[MIT](https://choosealicense.com/licenses/mit/)
