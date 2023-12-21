# Model_Deployment
Step by step to using our model for deployment using Cloud Run. This code build from Python.

Clone the repository then open it using your code editor.
Supposedly you have trained the model (from the Machine-Learning repository), download the model file with the .h5 file format. You can see the model in this repository.
This code is using Google Cloud Storage, so you have to make your own GCS Bucket, make a folder named text_uploads inside the bucket, get the credentials file (.json file) and name it "toekangku-credentials.json" (to match with the scripts) then copy it to the root directory of this project.
Open terminal in the project root directory, then run pip install -r requirements.txt to install the dependencies.
Run the app using the command: python classifier_api.py.
By default, the server will run on the localhost with the port 5000, open http://localhost:5000 to view it in your browser.
If it shows 'OK' then you have successfully run the predict api.
The next step is to configure the backend service.
