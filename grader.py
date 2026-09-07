import re
from pathlib import Path

FILE = Path("index.html")
TOTAL = 50
marks = 0

html = FILE.read_text(encoding="utf-8", errors="ignore")
css_match = re.search(r"<style\b[^>]*>(.*?)</style>", html, re.I | re.S)
css = css_match.group(1) if css_match else ""

def normalize(s):
    return re.sub(r"\s+", " ", s.strip().lower())

def selector_block(selector):
    # Find a simple CSS rule such as: p { ... }
    pattern = re.compile(
        r"(?<![\w.#-])" + re.escape(selector) + r"\s*\{([^{}]*)\}",
        re.I | re.S
    )
    m = pattern.search(css)
    return m.group(1) if m else None

def has_declaration(selector, prop, value):
    block = selector_block(selector)
    if block is None:
        return False
    pattern = re.compile(
        r"(?<![\w-])" + re.escape(prop) +
        r"\s*:\s*" + re.escape(value) + r"\s*;?",
        re.I
    )
    return bool(pattern.search(block))

def check(name, condition, points):
    global marks
    if condition:
        marks += points
        print(f"PASS [{points:2d}] {name}")
    else:
        print(f"FAIL [ 0] {name}")

# -------------------------------------------------
# HTML structure and content: 10 marks
# -------------------------------------------------
check("DOCTYPE declaration", bool(re.search(r"<!doctype\s+html>", html, re.I)), 2)
check("<main> element exists", bool(re.search(r"<main\b[^>]*>", html, re.I)), 1)
check("<h1> contains required heading", "This Season's Speaker Lineup" in html, 2)
check("Jeffrey Toobin paragraph exists", "October: Jeffrey Toobin" in html, 1)
check("Andrew Ross Sorkin paragraph exists", "November: Andrew Ross Sorkin" in html, 1)
check("Copyright paragraph has id='copyright'", bool(re.search(
    r"<p\b[^>]*\bid\s*=\s*['\"]copyright['\"]", html, re.I)), 1)
check("Copyright text exists", "Copyright 2015" in html, 1)
check("<footer> element exists", bool(re.search(r"<footer\b[^>]*>", html, re.I)), 1)

# -------------------------------------------------
# CSS selectors and declarations: 35 marks
# -------------------------------------------------
check("Universal selector * with margin .5em 1em",
      has_declaration("*", "margin", r"\.5em\s+1em"), 5)

check("main selector with border 2px solid black",
      has_declaration("main", "border", r"2px\s+solid\s+black"), 5)

check("main selector with padding 1em",
      has_declaration("main", "padding", r"1em"), 5)

check("h1 selector with Arial sans-serif",
      has_declaration("h1", "font-family", r"Arial\s*,\s*sans-serif"), 5)

check("p selector with margin-left 3em",
      has_declaration("p", "margin-left", r"3em"), 5)

check("#copyright selector with font-size 80%",
      has_declaration("#copyright", "font-size", r"80%"), 5)

check(".blue selector with color blue",
      has_declaration(".blue", "color", r"blue"), 3)

check(".right selector with text-align right",
      has_declaration(".right", "text-align", r"right"), 2)

# -------------------------------------------------
# HTML class usage: 5 marks
# -------------------------------------------------
check("Speaker paragraphs use class='blue'",
      len(re.findall(r"<p\b[^>]*\bclass\s*=\s*['\"][^'\"]*\bblue\b", html, re.I)) >= 2, 2)

check("Copyright paragraph uses both blue and right classes",
      bool(re.search(
          r"<p\b[^>]*\bid\s*=\s*['\"]copyright['\"][^>]*\bclass\s*=\s*['\"][^'\"]*\bblue\b[^'\"]*\bright\b",
          html, re.I
      )) or bool(re.search(
          r"<p\b[^>]*\bid\s*=\s*['\"]copyright['\"][^>]*\bclass\s*=\s*['\"][^'\"]*\bright\b[^'\"]*\bblue\b",
          html, re.I
      )), 3)

print("----------------------------------------------")
print(f"Final Score: {marks}/{TOTAL}")

if marks == TOTAL:
    print("RESULT: PASS - Excellent work!")
elif marks >= 25:
    print("RESULT: PARTIAL PASS - Review the failed tests.")
else:
    print("RESULT: NEEDS IMPROVEMENT - Review the CSS selectors.")

# GitHub Actions fails the job if the student does not reach 50/50.
raise SystemExit(0 if marks == TOTAL else 1)
