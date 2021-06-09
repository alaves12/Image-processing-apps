from flask import Flask, jsonify, request
from flask_cors import CORS,cross_origin
import torch
import os
from PIL import Image
import base64
from torchvision import transforms as T
from model.Unet import Unet

app = Flask(__name__)
CORS(app, support_credentials=True)
BASE_DIR = os.getcwd()
model = Unet()
model.load_state_dict(torch.load('model/multi_U_151.pth', map_location=torch.device('cpu')))
model.cpu()
model.eval()

def dehaze(input):
    with torch.no_grad():
        result = model(input)

    return resultf

@app.route('/')
def hello():
    name = "Hello World"
    return name

@app.route('/good')
def good():
    name = "Good"
    return name

@app.route("/res", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)  # ■■■ この行すべて
def res():
    response = jsonify({'ha':'hello'})
    print(request.files)
    return response

@app.route("/upload", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)  # ■■■ この行すべて
def upload():  
    print(request.files.getlist('yourFile'), "myfile")
    #画像データの取得
    files = request.files.getlist('yourFile')

    if request.method =='POST' and files:
        result=[]
        labels=[]
        #json_dict = json.loads(request.body)
        #for file in request.body:
            #print("file", file)
        for file in files:
            img = Image.open(file)
            y,x = img.size
            print(y,x)
            img1 = T.Resize((512,(int(512*(y/x)//8)*8)))(img)
            img_te = T.ToTensor()(img1)
            img_te = img_te.unsqueeze(0)
            img_r = dehaze(img_te)
            img_r = img_r.squeeze(0).mul(255).add_(0.5).clamp_(0, 255).permute(1, 2, 0).to('cpu', torch.uint8).numpy()
            img_r = Image.fromarray(img_r)
            input_path = os.path.join(BASE_DIR,'static', 'img','input.jpg')
            output_path = os.path.join(BASE_DIR,'static','img','output.jpg')
            img.save(input_path)
            img_r.save(output_path)

            with open(input_path, 'rb') as f:
                in_data = f.read()
            data1=base64.b64encode(in_data)
            data1 = str(data1)[2:-1]
                        
            with open(output_path, 'rb') as f:
                out_data = f.read()
            data2=base64.b64encode(out_data)
            data2 = str(data2)[2:-1]

            result.append((data1, data2))

        context = {
            'result': result
            }
        response = jsonify(context)
        return response
## おまじない
if __name__ == "__main__":
    app.run(debug=True,  host='0.0.0.0',port=8000)

