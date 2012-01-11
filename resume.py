import os
import misaka
from flask import Flask, render_template, Markup


app = Flask(__name__)

@app.route("/resume")
def cv():
	fd = open("resume.md", "r")
	md = fd.read()
	html = misaka.html(md)
	fd.close()

	partition = html.partition('</p>')
	contact = partition[0] + partition[1]
	resume = partition[2]

	ret = render_template('resume.html', contact=contact, resume=resume)
	return ret

if __name__ == "__main__":
	app.debug = True
	app.run()

