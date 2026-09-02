import os, ssl, sys, hashlib
from urllib.request import Request, urlopen

OUT = "/Users/a1-6/My_channel/papers/papers_html/pdfs/2026-09-02-ml-classics"

BOOKS = [
    ("01-understanding-ml.pdf",
     "https://raw.githubusercontent.com/ms3452/CS5780/master/understanding-machine-learning-theory-algorithms.pdf"),
    ("02-math-for-ml.pdf",
     "https://mml-book.github.io/book/mml-book.pdf"),
    ("03-ml-algorithms-math-analysis.pdf",
     "https://tongzhang-ml.org/lt-book/lt-book.pdf"),
    ("04-deep-learning-theory.pdf",
     "https://arxiv.org/pdf/2106.10165"),
    ("05-neural-networks-and-ml.pdf",
     "https://arxiv.org/pdf/1901.05639"),
    ("06-deep-learning-on-graphs.pdf",
     "https://yaoma24.github.io/dlg_book/dlg_book.pdf"),
    ("07-ml-algorithmic-perspective.pdf",
     "https://people.csail.mit.edu/moitra/docs/bookexv2.pdf"),
    ("08-probability-theory-and-examples.pdf",
     "https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf"),
    ("09-elementary-probability-for-applications.pdf",
     "https://sites.math.duke.edu/~rtd/EP4A/EP4A_April2021.pdf"),
    ("10-advanced-data-analysis.pdf",
     "https://stat.cmu.edu/~cshalizi/ADAfaEPoV/ADAfaEPoV.pdf"),
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def fetch(url, timeout=120):
    req = Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Accept": "application/pdf,*/*",
    })
    return urlopen(req, timeout=timeout, context=ctx).read()

for fname, url in BOOKS:
    path = os.path.join(OUT, fname)
    try:
        print(f"[{fname}] downloading {url}", flush=True)
        data = fetch(url)
        if len(data) < 50_000:
            raise RuntimeError(f"too small ({len(data)} bytes), likely error page")
        with open(path, "wb") as f:
            f.write(data)
        h = hashlib.sha256(data).hexdigest()[:16]
        print(f"  ok: {len(data):>12,} bytes  sha256:{h}", flush=True)
    except Exception as e:
        print(f"  FAIL: {e}", flush=True)
        sys.exit(1)

print("\n=== ALL DONE ===")
for fname, _ in BOOKS:
    p = os.path.join(OUT, fname)
    if os.path.exists(p):
        print(f"{fname}  {os.path.getsize(p):>12,} bytes")