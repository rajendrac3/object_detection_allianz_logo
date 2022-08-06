#python detect.py --weights allianz_model.pt --img 640 --conf 0.25 --source D:\Nvidia_ML\All\test\t3.jpeg --save-crop
import uvicorn
from detect import run
from fastapi import File, UploadFile, FastAPI

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        with open('inference_images/'+file.filename, 'wb') as f:
            f.write(contents)
            
        infer = run(weights = 'allianz_model.pt', source = 'inference_images/'+file.filename)
    except Exception as e:
        print(e)
        return {"message": "There was an error uploading the file"}
    finally:
        await file.close()
        
    return {"message": f"Successfuly uploaded {file.filename}"}
    

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)