#!/usr/bin/env python3
"""
Messenger Prank Generator
Creates a fake messenger reveal screen as an HTML file
"""

def generate_prank_html():
    """Generate the messenger prank HTML content"""
    html_content = '''<!DOCTYPE html>
<html>
<head>
<title>Messenger Reveal Prank</title>
<style>
body{
  background: black;
  color: lime;
  font-family: monospace;
  text-align: center;
  padding-top: 100px;
  margin: 0;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

h1 {
  font-size: 24px;
  margin-bottom: 30px;
}

#msg {
  font-size: 30px;
  animation: blink 0.5s infinite;
  margin: 20px 0;
}

@keyframes blink {
  0%, 49% { opacity: 1; }
  50%, 100% { opacity: 0; }
}

.prank-revealed {
  animation: slideIn 0.5s ease-in-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: scale(0.8);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
</style>
</head>
<body>

<h1>🔍 Connecting to Messenger...</h1>
<div id="msg">Revealing Messages...</div>

<script>
const revealTime = 5000; // 5 seconds

setTimeout(() => {
  document.body.innerHTML = `
    <div class="prank-revealed">
      <h1 style="color: red; font-size: 48px;">PRANK! 😂</h1>
      <p style="color: lime; font-size: 20px;">You got pranked! This is just a fake hacker screen</p>
      <button onclick="location.reload()" style="
        margin-top: 30px;
        padding: 10px 20px;
        background: lime;
        color: black;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
        font-family: monospace;
        font-weight: bold;
      ">Try Again</button>
    </div>
  `;
}, revealTime);
</script>

</body>
</html>'''
    return html_content


def save_prank_file(filename="messenger_prank.html"):
    """Save the prank HTML to a file"""
    content = generate_prank_html()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Prank file created: {filename}")
    return filename


def main():
    """Main function"""
    import os
    
    print("🎭 Messenger Prank Generator")
    print("-" * 40)
    
    filename = save_prank_file()
    print(f"📁 File saved to: {os.path.abspath(filename)}")
    print("\n💡 Usage:")
    print(f"   1. Open {filename} in your browser")
    print("   2. Share the file link with friends")
    print("   3. Watch them get pranked! 😂")


if __name__ == "__main__":
    main()
