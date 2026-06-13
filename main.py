import sys

# various string utilities
# added more as needed

def reverse(s): return s[::-1]
def palindrome(s): return s == s[::-1]
def count_words(s): return len(s.split())
def count_chars(s): return len(s)
def to_slug(s): return s.lower().replace(" ", "-")
def to_camel(s): 
    words = s.split()
    return words[0].lower() + "".join(w.capitalize() for w in words[1:])
def to_snake(s): return "_".join(s.lower().split())

ops = {
    "reverse": reverse,
    "palindrome": palindrome,
    "words": count_words,
    "chars": count_chars,
    "slug": to_slug,
    "camel": to_camel,
    "snake": to_snake,
}

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"usage: python main.py <op> <text>")
        print(f"ops: {', '.join(ops.keys())}")
        sys.exit()
    op = sys.argv[1]
    text = " ".join(sys.argv[2:])
    fn = ops.get(op)
    if not fn:
        print(f"unknown op: {op}")
    else:
        print(fn(text))
