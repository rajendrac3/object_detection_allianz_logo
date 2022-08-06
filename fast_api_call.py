#python detect.py --weights allianz_model.pt --img 640 --conf 0.25 --source D:\Nvidia_ML\All\test\t3.jpeg --save-crop
import uvicorn
from detect import run
from fastapi import File, UploadFile, FastAPI
from pyngrok import ngrok
import nest_asyncio
from fastapi.responses import FileResponse


app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        print(file.filename, type(file.filename))
        with open('inference_images/'+file.filename, 'wb') as f:
            f.write(contents)
            
        infer = run(weights = 'allianz_model.pt', source = 'inference_images/'+file.filename)
    except Exception as e:
        print(e)
        return {"message": "There was an error uploading the file"}
    finally:
        await file.close()
        
    # return {"message": f"Successfuly uploaded {file.filename}"}
    return FileResponse("results/"+file.filename)
    

if __name__ == '__main__':
    ngrok_tunnel = ngrok.connect(8000)
    print('Public URL:', ngrok_tunnel.public_url)
    nest_asyncio.apply()
    uvicorn.run(app, host='0.0.0.0', port=8000)