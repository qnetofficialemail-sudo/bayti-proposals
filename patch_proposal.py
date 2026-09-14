import sys
p = sys.argv[1] if len(sys.argv) > 1 else "auntyzkitchen.html"
with open(p, "rb") as f:
    c = f.read().decode("utf-8")
has_crlf = "\r\n" in c
c = c.replace("\r\n", "\n")
n = 0

# Add bulk upload to AI tools section
old = '''    <div class="ai-card">
      <div class="ai-card-icon">🌐</div>
      <div class="ai-card-title">Auto-Translation</div>
      <div class="ai-card-desc">Write your shop description in English → instantly translated to Arabic. Or write in Arabic → translated to English. Automatic on save.</div>
    </div>
  </div>
</div>'''

new = '''    <div class="ai-card">
      <div class="ai-card-icon">🌐</div>
      <div class="ai-card-title">Auto-Translation</div>
      <div class="ai-card-desc">Write your shop description in English → instantly translated to Arabic. Or write in Arabic → translated to English. Automatic on save.</div>
    </div>
    <div class="ai-card">
      <div class="ai-card-icon">🚀</div>
      <div class="ai-card-title">Smart Bulk Upload</div>
      <div class="ai-card-desc">Upload up to 20 product photos at once. Group photos that belong to the same product — AI writes the name & description for each group automatically. Add the price and publish. Done.</div>
    </div>
  </div>
</div>'''

if old in c: c=c.replace(old,new); n+=1; print("OK proposal AI tools")
else: print("MISS proposal AI tools")

# Add bulk upload to seller page features
old2 = '''    <div class="feature-item">
      <div class="feature-icon">📊</div>
      <div>
        <div class="feature-title">Order Dashboard</div>
        <div class="feature-desc">Manage all incoming orders from one simple screen</div>
      </div>
    </div>
  </div>'''

new2 = '''    <div class="feature-item">
      <div class="feature-icon">📊</div>
      <div>
        <div class="feature-title">Order Dashboard</div>
        <div class="feature-desc">Manage all incoming orders from one simple screen</div>
      </div>
    </div>
    <div class="feature-item">
      <div class="feature-icon">🚀</div>
      <div>
        <div class="feature-title">Bulk Product Upload</div>
        <div class="feature-desc">Upload 20 photos at once, group them by product, AI writes descriptions — publish everything in minutes</div>
      </div>
    </div>
  </div>'''

if old2 in c: c=c.replace(old2,new2); n+=1; print("OK proposal features")
else: print("MISS proposal features")

# Add bulk upload to stats
old3 = '''    <div class="stat-card">
      <div class="stat-icon">🤖</div>
      <div class="stat-value">4 AI Tools</div>
      <div class="stat-label">Free for you</div>
    </div>'''
new3 = '''    <div class="stat-card">
      <div class="stat-icon">🤖</div>
      <div class="stat-value">5 AI Tools</div>
      <div class="stat-label">Free for you</div>
    </div>'''

if old3 in c: c=c.replace(old3,new3); n+=1; print("OK stats")
else: print("MISS stats")

if has_crlf:
    c = c.replace("\n", "\r\n")
with open(p, "wb") as f:
    f.write(c.encode("utf-8"))
print(f"\nDone {n}/3 proposal")
