## Member of group
1. 2106657292 - Moza Adirafi Satria Jaka
2. 2106656522 - Muhammad Ghazian Gunawan  
3. 2106720973 - Nicolas Ananda 
4. 2106657815 - Raizaz Achmad Asyraf
5. 2106720891 - Jovian Marvin Chrisniady
6. 2106720866 - David Christianto

## Heroku Link
https://ariculture.herokuapp.com/

## Brief Description of the App
Our group chose the theme of agriculture, we plan to make a web that helps farmers in cultivating land and helps to market it. First, each farmer needs to create an account, then the web asks for the category of that farmer (fruit farmer/vegetable farmer/palm oil farmer). after that, farmers enter the area of the land that they own (in hectares or m^2). After that, farmers enter the location of their land (in mountainous areas / valleys / etc.) so that the web can help choose the right fertilizer for their plants. The web will also assist farmers in providing the fertilizer dose for land per m^2 and the appropriate amount of water. After that, farmers are asked to enter their harvest (success/fail). If successful, farmers are asked to enter the amount of their harvest in tons/kilo so that the website can help farmers advertise and market their crops. The purpose of making this Web is to help improve the standard of living of farmers in the modern era in an effective way so that they can advance the agricultural sector in Indonesia as a tropical country with abundant resources, especially fertile soil.

## Instructions on how to build, run, and deploy the app
To initialzie the app, we need to use the command "python manage.py startapp agricultura". Then on settings.py in folder project_django, we need to add the app name on the installed_app variable. Django follows the MTV design pattern, therefore we need to make files views.py, urls.py and HTML template. Then create the neccecary models to store on file models.py. Which we route to the HTML templates through the functions that we add on views.py and path it with urls.py.

To run it locally, we can use the command "python manage.py runserver" in the directory terminal, and open http://localhost:8000 in the browser. As for deploying, we use the cloud service HEROKU. First, we need to get the API key from the HEROKU account to add it to GitHub repository secrets. Insert the app name alongside the API key to the repository secret wtih HEROKU_APP_NAME and HEROKU_API_KEY as the name respectively. Lastly, connect the Heroku app with the GitHub repository with automatic deployment. And done. We can see the app deployed with the url https://ariculture.herokuapp.com/.

## List of Modules
1. Homepage (NA)
2. Account Registration and Farmland registration (Raizaz)
3. Farmland info (for obtaining Fertilizer type, Fertilizer dose, and etc. (Jovian)
4. News regarding agriculture (Moza)
5. Advertisements about the farmer's farm land. (Ghazian)
6. Reviews and rating regarding the farmers.
7. Contact us page for filing complaints. (David)
