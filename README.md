# Reveal Hidden Text Techniques

This script reveals hidden text that has been embedded using various techniques. It can process text input directly or read from a file.

## Available Techniques

1. **Zero Width Characters**: Reveals text hidden with zero-width characters.
2. **Unicode Whitespace**: Reveals text hidden with Unicode whitespace characters.
3. **Base64 Encoding**: Decodes Base64 encoded hidden text.
4. **URL Encoding**: Decodes URL encoded hidden text.
5. **Zero Font Size**: Reveals text hidden with zero font size.
6. **Small Font Size**: Reveals text hidden with a very small font size.
7. **HTML Comment Tags**: Reveals text hidden within HTML comment tags.
8. **Character Substitution**: Reveals text hidden with character substitution.
9. **Homoglyphs**: Reveals text hidden with homoglyphs.
10. **Polyglot Text**: Reveals text hidden with polyglot text.
11. **Hidden in Plain Sight**: Reveals text hidden in plain sight.
12. **Metadata Fields**: Reveals text hidden within metadata fields.
13. **JavaScript Embedding**: Reveals text hidden within JavaScript code.
14. **CSS Manipulation**: Reveals text hidden using CSS.

## Installation

Requires the `beautifulsoup4` package.

```
pip install beautifulsoup4
```
Usage
Run the script with the desired technique, specifying either a payload or a file containing the text.

Command-Line Options
-t, --technique: Technique to use. Choices are zero_width, unicode_whitespace, base64, url, zero_font, small_font, html_comment, char_sub, homoglyphs, polyglot, plain_sight, metadata, javascript, css.
-p, --payload: Text payload to process.
-f, --file: File containing text payload.

Examples

Using Payload:

Zero Width Characters
```
python reveal_hidden_text.py -t zero_width -p "This is a test.‍hidden"
```
Output:


hidden
Unicode Whitespace


```
python reveal_hidden_text.py -t unicode_whitespace -p "This is a test. hidden"
```
Output:


hidden
Base64 Encoding

```
python reveal_hidden_text.py -t base64 -p "This is a test.VGhpcyBpcyBhIHRlc3Q=hidden"
```
Output:


hidden
URL Encoding

```
python reveal_hidden_text.py -t url -p "This is a test.hidden"
```
Output:



hidden
Zero Font Size

```
python reveal_hidden_text.py -t zero_font -p "<p>This is a test.<span style=\"font-size:0\">hidden</span></p>"
```
Output:

hidden
Small Font Size

```
python reveal_hidden_text.py -t small_font -p "<p>This is a test.<span style=\"font-size:1px\">hidden</span></p>"
```
Output:


hidden
HTML Comment Tags

```
python reveal_hidden_text.py -t html_comment -p "<p>This is a test.<!-- hidden --></p>"
```
Output:

hidden
Character Substitution

```
python reveal_hidden_text.py -t char_sub -p "This is a test.h\u0435\u0456\u0440d"
```
Output:

hеіr

Homoglyphs

```
python reveal_hidden_text.py -t homoglyphs -p "This is a test.hidden"
```
Output:


hidden
Polyglot Text

```
python reveal_hidden_text.py -t polyglot -p "This is a test.hidden"
```
Output:


hidden
Hidden in Plain Sight

```
python reveal_hidden_text.py -t plain_sight -p "This is a test. By the way, every first letter here spells a hidden message."
```
Output:


every first letter here spells a hidden message
Metadata Fields

```
python reveal_hidden_text.py -t metadata -p "<meta name=\"description\" content=\"hidden\">"
```

Output:


hidden
JavaScript Embedding

```
python reveal_hidden_text.py -t javascript -p "<script>var hidden=\"hidden\";</script>"
```
Output:


hidden
CSS Manipulation

```
python reveal_hidden_text.py -t css -p "<p>This is a test.<span style=\"display:none\">hidden</span></p>"
```
Output:


hidden
Using File:

Zero Width Characters

```
python reveal_hidden_text.py -t zero_width -f input.txt
```
Output:


hidden
Unicode Whitespace

```
python reveal_hidden_text.py -t unicode_whitespace -f input.txt
```
Output:


hidden
Base64 Encoding

```
python reveal_hidden_text.py -t base64 -f input.txt
```
Output:


hidden
URL Encoding

```
python reveal_hidden_text.py -t url -f input.txt
```
Output:

hidden
Zero Font Size

```
python reveal_hidden_text.py -t zero_font -f input.txt
```
Output:

hidden
Small Font Size

```
python reveal_hidden_text.py -t small_font -f input.txt
```
Output:


hidden
HTML Comment Tags

```
python reveal_hidden_text.py -t html_comment -f input.txt
```
Output:


hidden
Character Substitution

```
python reveal_hidden_text.py -t char_sub -f input.txt
```
Output:


hidden
Homoglyphs

```
python reveal_hidden_text.py -t homoglyphs -f input.txt
```
Output:


hidden
Polyglot Text

```
python reveal_hidden_text.py -t polyglot -f input.txt
```
Output:

hidden
Hidden in Plain Sight

```
python reveal_hidden_text.py -t plain_sight -f input.txt
```
Output:


every first letter here spells a hidden message
Metadata Fields

```
python reveal_hidden_text.py -t metadata -f input.txt
```
Output:


hidden
JavaScript Embedding

```
python reveal_hidden_text.py -t javascript -f input.txt
```
Output:

hidden
CSS Manipulation

```
python reveal_hidden_text.py -t css -f input.txt
```
Output:


hidden

License
This project is licensed under the MIT License.
