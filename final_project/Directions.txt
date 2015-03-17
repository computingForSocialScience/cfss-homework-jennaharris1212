Final Project: Facebook Networks
In this project you will bring together all of the tools you’ve learned so far to implement Facebook. Just kidding. Sort of.

Part 0: Attempt to download your Facebook friend network data.
Assuming you use Facebook, first try to use the Facebook app Give Me My Data to pull down data about your friends as well as the mutual friend edges between them. Do this with the app by generating a JSON file of “Friends (data)” as well as a JSON file of “Mutual Friends Network Graph”, and copying them into files friend_attributes.json and friend_edges.json, respectively.

With the mutual friend edges you will be able to learn quite about about your social network structure (such as it is represented by Facebook “friends”, that is). Some of the cool images others have generated with this data can be seen here.

NOTE: Facebook is phasing out this functionality (See “Friends now has a new permission” under “User IDs and Friends” in their App Upgrade Guide, and so we recommend that you download this data as soon as possible.

However, in the event that you cannot use your own data, we will provide somewhat-carefully faked plausible friend data which simulates a basic friend network.

Part 1: Put your social network data into MySQL
Using your local MySQL database, you should create two tables, friend_attributes and friend_edges, on your local server, each which have columns corresponding to the JSON data exported by the Facebook app. Write code to import the two .json files into your local database. You will probably want to inspect the variables and only bother creating columns for fields which have data worth representing (or data at all). You can use your subjective judgment here on what’s interesting to display, but we recommend at least uid, the name fields, pic, religion, birthday_date, sex, hometown_location, current_location, relationship_status, significant_other_id, political, locale, profile_url, and website.

You will want to be careful to create your tables as Unicode (UTF8) and to pass the charset='utf8' to MySQLdb.connect() when you connect. Also, depending on how you insert into MySQL you may also want to be on the lookout for single quotes in last names (e.g. “O’Keefe”) which may need to be escaped with a backslash.

Part 2: Create an index page
Create a Flask web application with a single page: the index (conventionally index.html). The index page (http://127.0.0.1:5000/) should be an HTML list of all of your friends’ names. Each name should link to a (as yet nonexistent) profile page (accessible at http://127.0.0.1:5000/profile/[userid]).

Part 3: Create profile pages
The profile pages (at http://127.0.0.1:5000/profile/[userid], e.g. /profile/03428930 or /profile/942387) should display, in whatever aesthetically pleasing way you like, all of the information from the friend_attributes data (except, say, locale, label, and id, the latter of which is in the URL itself).

(Those using their own Facebook data will enjoy adding <img src> links to the URL in the attributes’ table’s pic or pic_big column to link directly to their friend’s profile pics).

Part 4: Construct a graph in Python
Add to the code in Part 3 code to construct a graph object, using Python’s networkx library. This object should be a subgraph of the entire graph, representing just the local friend-neighborhood of the user whose profile it is. (This subgraph will include that user.) So, for example, if you have a distant friend Bob who is only friends with one of your other friends, Alice, then this subgraph will have two nodes representing Bob and Alice and one edge connecting them.

(This won’t affect what each profile page will look like, but we will use this subgraph for Part 5 and 6.)

Part 5: Add list of friends to each profile page
Now that you have a per-profile graph object every time someone loads a /profile/[userid] page, change the profile pages to also have a list of that user’s friends. Each name in the list should link to that user’s profile page.

Part 6: Visualize each friend’s subgraph
Add a visual representation of each profile’s subgraph to the profile pages. This can be either a dynamically-generated .png file, or you can use d3.js’ Force-Directed Graphs (will require the use of JavaScript, which is – unfortunately or fortunately – not taught in this course, but is one of the more overly googleable scripting languages due to the high proportion of self-taught learners).

The user should be able to see the full names of the users associated with each node.

Part 7: Create forms to upload a graph
Create a new page /upload, with forms (using Flask and HTML) which allow the user to upload a pair of friend_attributes.json and friend_edges.json files. You should test these on both your own data (if available) and our randomly-generated fake data.

Note that this means that if you manage to run your project on a real live web server (Note: not required), your friends will be able to upload their networks (as exported by the Give Me My Data app, while it works) and your program can visualize their data for them.

Turning it in
You will demonstrate your project on March 18 between 6–8pm, and also include all code within the final_project folder (two or more scripts) in your GitHub repository. Please also include a file called README.txt or README.md that describes how to run your project, including any setup scripts that download data, etc. Finally, if you make any large data files in the course of running your website, please use a .gitignore file to exclude these from the repository.
