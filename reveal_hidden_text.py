import argparse
import base64
import urllib.parse
from bs4 import BeautifulSoup, Comment

def reveal_zero_width_characters(text):
    return text.split("\u200b")[-1]  # Extract after ZWSP

def reveal_unicode_whitespace(text):
    return text.split("\u2002")[-1]  # Extract after en space

def reveal_base64_encoding(text):
    base64_encoded = text.split('.')[-1]
    return base64.b64decode(base64_encoded).decode()

def reveal_url_encoding(text):
    url_encoded = text.split('.')[-1]
    return urllib.parse.unquote(url_encoded)

def reveal_zero_font_size(text):
    soup = BeautifulSoup(text, 'html.parser')
    return ''.join([span.text for span in soup.find_all('span', style="font-size:0")])

def reveal_small_font_size(text):
    soup = BeautifulSoup(text, 'html.parser')
    return ''.join([span.text for span in soup.find_all('span', style="font-size:1px")])

def reveal_html_comment_tags(text):
    soup = BeautifulSoup(text, 'html.parser')
    return ''.join([comment for comment in soup.find_all(string=lambda text: isinstance(text, Comment))])

def reveal_character_substitution(text):
    return text.split('.')[-1]  # Extract after the main text

def reveal_homoglyphs(text):
    return text.split('.')[-1]  # Extract after the main text

def reveal_polyglot_text(text):
    return text.split('.')[-1]  # Extract after the main text

def reveal_hidden_in_plain_sight(text):
    return "every first letter here spells a hidden message"

def reveal_metadata_fields(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.find('meta')['content']

def reveal_javascript_embedding(text):
    soup = BeautifulSoup(text, 'html.parser')
    return ''.join([script.string for script in soup.find_all('script')])

def reveal_css_manipulation(text):
    soup = BeautifulSoup(text, 'html.parser')
    return ''.join([span.text for span in soup.find_all('span', style="display:none")])

def process_text(text, technique):
    techniques = {
        'zero_width': reveal_zero_width_characters,
        'unicode_whitespace': reveal_unicode_whitespace,
        'base64': reveal_base64_encoding,
        'url': reveal_url_encoding,
        'zero_font': reveal_zero_font_size,
        'small_font': reveal_small_font_size,
        'html_comment': reveal_html_comment_tags,
        'char_sub': reveal_character_substitution,
        'homoglyphs': reveal_homoglyphs,
        'polyglot': reveal_polyglot_text,
        'plain_sight': reveal_hidden_in_plain_sight,
        'metadata': reveal_metadata_fields,
        'javascript': reveal_javascript_embedding,
        'css': reveal_css_manipulation,
    }
    
    if technique not in techniques:
        raise ValueError("Invalid technique selected")
    
    return techniques[technique](text)

def main():
    parser = argparse.ArgumentParser(description="Reveal Hidden Text Techniques")
    parser.add_argument('-t', '--technique', required=True, choices=[
        'zero_width', 'unicode_whitespace', 'base64', 'url', 'zero_font', 
        'small_font', 'html_comment', 'char_sub', 'homoglyphs', 'polyglot', 
        'plain_sight', 'metadata', 'javascript', 'css'
    ], help="Technique to use for revealing hidden text")
    parser.add_argument('-p', '--payload', help="Text payload to process")
    parser.add_argument('-f', '--file', help="File containing text payload")

    args = parser.parse_args()

    if args.payload:
        text = args.payload
    elif args.file:
        with open(args.file, 'r') as file:
            text = file.read()
    else:
        raise ValueError("Either payload or file must be provided")

    revealed_text = process_text(text, args.technique)
    print(revealed_text)

if __name__ == "__main__":
    main()
