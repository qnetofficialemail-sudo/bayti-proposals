import re

files = ["auntyzkitchen.html", "auntyzkitchen_ar.html", "first10_ar.html", "first10_en.html"]

for filename in files:
    try:
        with open(filename, "rb") as f:
            c = f.read().decode("utf-8")
    except FileNotFoundError:
        print(f"SKIP {filename} — not found in this folder")
        continue

    has_crlf = "\r\n" in c
    c = c.replace("\r\n", "\n")
    count_before = c.count("🏠")

    # Replace brand-icon divs (the square logo box) with an actual img
    c = c.replace(
        '<div class="brand-icon">🏠</div>',
        '<img src="logo.png" alt="Bayti" class="brand-icon" style="width:44px;height:44px;border-radius:12px;object-fit:contain;background:white;padding:2px;" />'
    )

    # Any remaining standalone 🏠 emoji in text/icons -> keep as is (too risky to blanket-replace inline text emoji)
    count_after = c.count("🏠")
    print(f"{filename}: brand-icon replaced, {count_after} standalone 🏠 emoji remain (left as-is)")

    if has_crlf:
        c = c.replace("\n", "\r\n")
    with open(filename, "wb") as f:
        f.write(c.encode("utf-8"))
