Watersome Website and Backend

This repository contains the single-page index.html website for Watersome and a simple Python Flask backend to handle contact form submissions.



Deployment to Render.com

Render is a cloud platform that makes it easy to deploy web applications and services. We will deploy this project as two separate services: a Static Site for the HTML/CSS/JS frontend and a Web Service for the Python backend.



Step 1: Push to GitHub

Create a new repository on your GitHub account (e.g., watersome-website).



Upload the following three files to your new GitHub repository:



index.html



app.py



requirements.txt



Step 2: Deploy the Python Backend (Web Service)

Create a New Service on Render:



Go to your Render Dashboard and click "New +" > "Web Service".



Connect your GitHub account and select your watersome-website repository.



Configure the Web Service:



Name: Give it a clear name, like watersome-backend.



Region: Choose a region close to you.



Branch: Select main (or your default branch).



Root Directory: Leave this blank.



Runtime: Python 3



Build Command: pip install -r requirements.txt



Start Command: gunicorn app:app



Choose an Instance Type:



The Free instance is sufficient for this project. Note that free services will "spin down" after a period of inactivity and may take 30-60 seconds to respond to the first request after being idle.



Click "Create Web Service".



Render will start building and deploying your backend.



Once deployed, Render will provide you with a public URL for your backend (e.g., https://watersome-backend.onrender.com). Copy this URL.



Step 3: Update the Frontend with the Live Backend URL

Edit index.html in GitHub:



Go back to your index.html file in your GitHub repository and edit it.



Find the fetch URL inside the <script> tag at the bottom of the file (around line 430).



Replace the placeholder URL with your live Render backend URL:



// --- FROM ---

const response = await fetch('\[http://127.0.0.1:5000/send\_email](http://127.0.0.1:5000/send\_email)', {



// --- TO (example) ---

const response = await fetch('\[https://watersome-backend.onrender.com/send\_email](https://watersome-backend.onrender.com/send\_email)', {



Commit the change directly to your main branch.



Step 4: Deploy the Frontend (Static Site)

Create a New Service on Render:



Go back to your Render Dashboard and click "New +" > "Static Site".



Select your watersome-website repository again.



Configure the Static Site:



Name: watersome-frontend (or just watersome).



Branch: main.



Build Command: Leave this blank.



Publish Directory: . (a single dot, meaning the root directory where index.html is).



Click "Create Static Site".



Render will deploy your index.html file.



Once finished, you will have a public URL for your live website!



Your website is now live, and the contact form will send requests to your live backend service.

