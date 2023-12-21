# Model_Deployment
## Step by step to using our model for deployment using Cloud Run.

1. Clone the repository then open it using your code editor.
2. Supposedly you have trained the model (from the [Model_Deployment](https://github.com/TOEKANGKU/Model_Deployment) repository), download the model file with the .h5 file format. You can see the model in this repository.
3. This code is using Google Cloud Storage, so you have to make your own GCS Bucket, make a folder named _text_uploads_ inside the bucket, get the credentials file (.json file) and name it _"toekangku-credentials.json"_ (to match with the scripts) then copy it to the root directory of this project.
4. Open terminal in the project root directory, then run `pip install -r requirements.txt` to install the dependencies.
5. Run the app using the command: `python classifier_api.py`.
6. By default, the server will run on the localhost with the port 5000, open [http://localhost:5000](http://localhost:5000) to view it in your browser.
7. If it shows 'OK' then you have successfully run the predict api.
8. The next step is to configure the backend service.
