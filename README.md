# words2anki

A personal collection of words that I want to learn along with a script that
retrieves the definitions of each word by using the [python wordnik API][1].

The resulting definitions file can be used to import into [Anki][2], a flash
card application which takes into account [spaced repetition][3] to make
learning more efficient.

## Usage

Assuming you have a [wordnik][4] API key:

```shell
$ export WORDNIK_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
$ ./words2anki words.list > definitions.csv
```

[1]: https://github.com/wordnik/wordnik-python
[2]: https://apps.ankiweb.net/
[3]: https://apps.ankiweb.net/docs/manual.html#spaced-repetition
[4]: http://developer.wordnik.com/
