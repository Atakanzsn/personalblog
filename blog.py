from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/youtube_video_indirici")
def d1():
    return render_template("youtubedownloader.html")

@app.route("/yazihiztesti")
def d2():
    return render_template("yazihizitesti.html")

@app.route("/inthiztesti")
def d3():
    return render_template("inthiztesti.html")

@app.route("/snakegame")
def d4():
    return render_template("snakegame.html")

@app.route("/notfcs")
def d5():
    return render_template("notfcs.html")

@app.route("/rps")
def d6():
    return render_template("rps.html")

@app.route("/qrcodegen")
def d7():
    return render_template("qrcodegen.html")

@app.route("/passgen")
def d8():
    return render_template("passgen.html")

@app.route("/sendmail")
def d9():
    return render_template("sendmail.html")

@app.route("/facedetector")
def d10():
    return render_template("facedetector.html")

@app.route("/instabot")
def d11():
    return render_template("instabot.html")

@app.route("/fidgetspinner")
def d12():
    return render_template("fidgetspinner.html")

@app.route("/virtualassist")
def d13():
    return render_template("virtualassist.html")



if __name__ == "__main__":
    app.run(debug=True)