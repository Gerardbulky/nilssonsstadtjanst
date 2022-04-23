#  **Superclean Cleaning Service**
- This is a simple project built entirely using HTML, CSS, Bootstrap, Jquery, Javascrpit, Python and Flask and [hosted](https://nilssonsstadtjanst.herokuapp.com/) on Heroku.
- The project is divided into the **header,body and footer**. The header contains the **logo image** and three **photos** showing pictures of the types of cleaning offered by the company and a **navigation bar**.
- The body section contains an **image slider** together with two card one containing information about the **opening hours** and the other card providing some **contact information**.
- The footer contains a **wave image** and below that is the **company name** and **contact information** and **social links** and lastly we have the **copyright** section.

# **UX**
- This project is intended for users who are looking for a website that offers cleaning services such as home cleaning,company cleaning,window cleaning etc. Below is a **sketch** of the Desktop and Mobile version the project website.
<img src="static/images/sketchDesktop.jpg" width=300> <img src="static/images/sketchMobil.jpg" width=300>.
- Attached is a [link to the deployed project on github](https://github.com/gerardambe/nilssonsstadtjanst) and a [link to the hosted site](https://nilssonsstadtjanst.herokuapp.com/).
- The project in its entirety provides easy access to users with images of what the service offers in both mobile and Desktop easy to access versions.
- As a user by clicking on the different features will provide you with more elaborated and explicit detailed information on what to expect.
- In the contact section you have a mail section to send your request and also a map section that provides the users with the locations.
# **Features**
- In this section, am gonna walk you through the different parts of the project from the header right down to the footer with a brief description of the different features implemented. 
## **Existing Features**
### **The Header**
- The **header** contains a logo with a name of the cleaning service.
- It also contains three cleaning images that shows some services offered.
- it contains a navigation bar which contains **Home,Services,Prices,Discount,About and Contact**.
- The site always opens up into the **home page** which is the active page.
- The **service button** in the navigation bar when clicked will redirect the user to the different cleaning services offered by the company.
- The **price button** in the navigation bar when clicked will redirect the user to the price section of the site that contains price information. 
- The **discount button** in the navigation bar when clicked redirects the user to the discount section of the site that provides discount informations.
- The **About button** in the navigation bar when clicked redirect the user to the page containing informations about the company.
- The **contact button** in the navigation bar when click redirects the user to the contact page which contains a **map** showing locations of the company in different areas and a mail section for the user to send a message to the company.
- On smaller and medium screens sizes, the logo image occupies full width of the screen, while on larger screens sizes,it goes by the rule of thirds. And also, the three cleaning images are only visible on large and xtra large screens.
### **The Body**
- The **body** contains an image fader, that fades into different images at every two seconds. it also contains two cards,the **contact card** and the **opening hours card**.
- The **contact card** contains **phone number,email address** and **location** to the user. while,
- The phone number, when clicked makes a call to the company from the site.
- The location icon, when clicked will open into the google map, showing the different routes and duration to the company's location.
- An email address to the company.
- An a website of the company.
- The **opening hour card** provides the contact hours to the user and working days. 
### **The Footer**
- The footer contains three sections,the **wave image** section,the **company name** section and the **copyright** section.
- The **company name** section also contains some **contact informations** and **social links**, which at the moment have not been linked to any social sites.

### **Features Left To implement**
I would like to implement a feature whereby users can be able to book and pay for their services online.

# **Technology Used**
- **CSS and HTML**
- **Javascript**
- **Python**
- **Flask**
- **SQL**
- **bootstrap** - Is a framework used entirely to build the site,. [link](https://www.bootstrapcdn.com/).
- **Emailjs** - To incorporate google email into the site. [link](https://www.emailjs.com/).
- **Google Map.js** - To incorporate the google map into the site. [link](https://developers.google.com/maps/documentation/javascript/tutorial).
- **JQuery** - To simplify DOM manipulation. [link](https://jquery.com/download/).
- **sweetalert** - To alert if message is sent or failed to send.[link](https://sweetalert.js.org/guides/).

# **Testing**
### **Home page**
- On the home page, there is a **contact card**, that has a **phone number** clicking on it helps the user make a call.
- There is also a **gmail address** to send emails which when click on takes you to the contact page.
- There is a **location icon** which provides google direction to the user.
- The **website link** and **social links icons** are not linked to any social websites at the moment clicking on it brings the user back to the home page.
### **Contact page**
- On the contact page, there is a **google map** with **map markers**. Hovering over, pops a message that says **click the icon**, when the icon is clicked, pops up another box with contact informations of the different areas.
- On the contact trying to submit an empty form,appears a pop up alert saying **fields are empty,fill out the field**.
- Trying to submit the form with a missing field, pops up and alert, saying **fields are empty, please fill out the field**
- Trying to submit the form with all fields filled up, pops up an alert saying **successfully submitted** with an **ok button** 

#### ** Different Screen Sizes**
- On ipads and smaller divices, the logo image occupies the full width of the device while on larger devices and desktops it goes by the rule of thirds. 1/3 of the screen is  the logo image and 2/3 the gallery images.
- On ipads and smaller divices the gallery images are not displayed while on larger screen the gallery images are displayed.
- Similarly the map and email section takes 2/3 on larger screens and the contact card and opening hour cards takes 1/3 on larger screens.
- On smaller screens they take up full widths. 

# **Deployment**
The project was deployed to GitHub Pages using the following steps...

- Log in to GitHub and locate the [GitHub Repository](https://github.com/gerardambe/cleaning-company/settings)
- At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
- Scroll down the Settings page until you locate the "GitHub Pages" Section.
- Under "Source", click the dropdown called "None" and select "Master Branch".
- The page will automatically refresh.
- Scroll back down through the page to locate the now published site [link](https://gerardambe.github.io/cleaning-company/) in the "GitHub Pages" section.
- You can run the server using **python3 -m http.server**
 
# **Credit**
## **Content**
- I owe a big thank you to all those who contributed in one way or another during this project.
- Some ideas where obtained,like the rule of thirds from some materials at code institude.
- The idea of using the sweetalert obtained from [link](https://www.youtube.com/watch?v=GC-9Bn7_eXs).
- The idea of pop up when hovering over the google markers were obtained from [link](https://www.youtube.com/watch?v=Zxf1mnP5zcw&list=LLdR7i1DWa2mvrstuxruyJVw&index=13&t=900s).
## **Media**
- Some of the photos used where obtained from Can Stock Photo.
## **Acknowledgements**
- I recieved inspiration from myself because i work as a cleaner in a cleaning company. Just wanted to experiment what is like building a cleaning company.
- I would like to thank my Mentor for his support throughout this journey.
- The tutor for their relentless efforts
