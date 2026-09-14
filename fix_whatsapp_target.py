files = ["first10_ar.html", "first10_en.html"]
for filename in files:
    try:
        with open(filename, "rb") as f:
            c = f.read().decode("utf-8")
    except FileNotFoundError:
        print(f"SKIP {filename}")
        continue
    has_crlf = "\r\n" in c
    c = c.replace("\r\n", "\n")

    # Add target="_blank" to all wa.me links that don't have it
    old1 = 'href="https://wa.me/971568447560" class="cta-button"'
    new1 = 'href="https://wa.me/971568447560" target="_blank" rel="noopener" class="cta-button"'
    old2 = 'href="https://wa.me/971568447560" class="whatsapp-btn"'
    new2 = 'href="https://wa.me/971568447560" target="_blank" rel="noopener" class="whatsapp-btn"'

    n = 0
    if old1 in c: c = c.replace(old1, new1); n += 1
    if old2 in c: c = c.replace(old2, new2); n += 1
    print(f"{filename}: {n} links fixed")

    if has_crlf:
        c = c.replace("\n", "\r\n")
    with open(filename, "wb") as f:
        f.write(c.encode("utf-8"))
