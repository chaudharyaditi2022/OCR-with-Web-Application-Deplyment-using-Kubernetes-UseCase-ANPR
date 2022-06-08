
print("content-type: application/json\r\n")

from flask import Flask,render_template,request,redirect
import os,cv2
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import Character_Recognition as cr
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['IMAGE_UPLOADS'] = '/var/ANPR_PROJECT/static/Images'
@app.route("/", methods=['POST', 'GET'])

def upload_image():
	if request.method == "POST":
		image = request.files['file']
		if(image.filename == ''):
			print("File name is invalid")
			return redirect(request.url)

		filename = secure_filename(image.filename)

		basedir = os.path.abspath(os.path.dirname(__file__))
		path = os.path.join(basedir,app.config["IMAGE_UPLOADS"],filename)
		image.save(path)

		frame = cv2.imread(path)
		plate, image = cr.nameplate_extractor(frame)
		character_list_final = cr.imageSegementation(plate)
		plate_num = cr.recognizeCharacters(character_list_final)
		formatted_data = cr.get_vehicle_info(plate_num)
		return render_template("main.html", data = formatted_data)


	return render_template("main.html")




app.run(host='0.0.0.0',port=80)
