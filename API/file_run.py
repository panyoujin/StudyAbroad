from flask import Flask,request
import json
import time
import uuid
import os
import sys
app = Flask(__name__)
#UPLOAD_FOLDER = 'static/Uploads' 
UPLOAD_FOLDER = '/home/attachment'
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024

def allowed_file(filename):
  return '.' in filename and \
      filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload', methods=['POST'])
def upload():
    path = "";
    try:
        if len(request.files):
            fileItem = request.files['file']
            date = time.strftime("%Y-%m-%d", time.localtime())
            save_path = os.path.join("files",date)
            if not os.path.exists(os.path.join(UPLOAD_FOLDER,save_path)):
                os.makedirs(os.path.join(UPLOAD_FOLDER,save_path))
            file_name_str = fileItem.filename.split('.',-1)
            path = os.path.join(save_path, str(uuid.uuid1())+'.'+file_name_str[len(file_name_str)-1])
            fileItem.save(os.path.join(UPLOAD_FOLDER,path))
        else:
            return json.dumps({'status': 500, 'message': "上传失败"}, ensure_ascii=False)
    except:
        info = sys.exc_info()
        return json.dumps({'status': 500, 'message': info}, ensure_ascii=False)

    data = {"file_path":path.replace('\\','/')}
    return json.dumps({'status':200,'message':"成功",'data':data}, ensure_ascii=False)

app.run(port=7000)