# Static wiki verification pattern

Use this after writing `wiki/index.html` or an equivalent self-contained artifact:

```python
from html.parser import HTMLParser
from pathlib import Path
import sys

path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8")

class Check(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.hrefs = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and "href" in attrs:
            self.hrefs.append(attrs["href"])

check = Check()
check.feed(text)
assert "<title>" in text
assert len(check.hrefs) > 0
assert all(h[1:] in check.ids for h in check.hrefs if h.startswith("#"))
for href in check.hrefs:
    if href.startswith("../"):
        assert (path.parent / href).resolve().exists(), href
assert not any(tag in text.lower() for tag in ("<script", "<iframe"))
print("static wiki verification passed")
```

The actual project path is passed as an argument; do not hard-code a repository path into a reusable checker.
