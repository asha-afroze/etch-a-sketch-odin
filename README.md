# etch-a-sketch-odin

To run the backend
```
1. Navigate to the `backend` directory:
cd backend

2. Create a virtual environment: (This is a best practice to keep project dependencies isolated)
python3 -m venv env

3. Activate the virtual environment:
source env/bin/activate

4. Install the required packages: (This might take a few minutes as it will download the model files)
pip install --index-url https://pypi.org/simple -r requirements.txt

5. Start the FastAPI server:
uvicorn main:app --reload
```