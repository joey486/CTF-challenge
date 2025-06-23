from flask import Flask, send_file, render_template_string

app = Flask(__name__)

# HTML page with a button to request the image
html_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Sender</title>
</head>
<body>
    <h1>Click the button to receive the image</h1>
    <form action="/send-image" method="GET">
        <button type="submit">Get Image</button>
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_page)

@app.route('/send-image')
def send_image():
    # Replace 'image.png' with the path to your image
    return send_file('frame.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
