from fastapi import File, UploadFile
@app.post("/upload-photo/")
def upload_photo(student_id: int, file: UploadFile = File(...)):
    # Logic to save the file on the server
