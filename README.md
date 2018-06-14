# Cricket_Scoreboard_python

Instructions:
1.	All program files must be placed in the same folder
2.	The folder called Teams must be placed in the same directory as the program
3.	Minimum screen resolution must be 1366 x 768


There will be two parts of the software. 
1.	Data Entry Application
2.	Scoreboard 

Data Entry Application
New App Start
User will start the data entry app, he will be asked if it is a new match or not. If it is a new match, details like 2 teams, venue, number of overs will be entered and a new match starts. 
Ball By Ball Data Entry
User will be entering updates for everything that happens in the match, every ball played. For a T20 match, there will be 120 balls match (without extra). In a one-day match, there will be 300 balls (without extras). We are not handling test matches. 
Team Entry Screen
When a new match is started, team member names and their speciality is entered in the system so that they can be picked easily on "Ball By Ball Data Entry" screen. 
File/s
You will be saving all information in files. The files will be saving team information, match information and everything that the app is handling. 
Score Board
The score board app will be shown for a given match. 
Scoreboard details
When user starts the score-board screen, he will be asked to select a match that is going on right now. The scoreboard will be running in a loop and every few seconds it will be reading information from the file. (The files saved in ball-by-ball-data-entry screen). It is important that you read and update the scoreboard after every few seconds. 
Scoreboard will show full match details including current score, balls played, current overs played, which player scored what data, what player is still playing with what score, which bowler balled how many overs, score he gave, maiden overs bowled and wickets taken.

Other requirements

Object Orientation
The applications that you are building should be object oriented. You should have proper classes to make a proper application architecture. There will be some classes that are related to the screens, like: 
•	New Match Screen
•	Load Match Screen
•	Data Entry Screen
•	Score board screen 

You will also have data logic classes including classes like:
•	Match
•	Team
•	Player
•	Batsman
•	Bowler
