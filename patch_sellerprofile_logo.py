with open("src/pages/SellerProfilePage.tsx", "rb") as f:
    c = f.read().decode("utf-8")
has_crlf = "\r\n" in c
c = c.replace("\r\n", "\n")

old = '              : <span className="text-3xl">🏠</span>'
new = '              : <img src="/logo-icon.png" alt={seller.shop_name} className="w-full h-full object-contain p-2" />'

if old in c:
    c = c.replace(old, new)
    print("OK fallback logo replaced")
else:
    print("MISS")

if has_crlf:
    c = c.replace("\n", "\r\n")
with open("src/pages/SellerProfilePage.tsx", "wb") as f:
    f.write(c.encode("utf-8"))
