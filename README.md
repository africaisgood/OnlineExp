OnlineExp
=========
This babay face guessing experiment ask users to guess the gender of each baby face image.

********************
***** Back-end *****
********************
===== babyface.py =====
It imports Facebook API - Planout, which is designed for conducting online experiments. Planout generates different trial orders for each user and ensure that the same user will receive the same order everytime he/she logs in to the system.

===== application.py =====
def runBabyFace():
It imports babyface.py to generate different trial order for different users. 

def answer():
It validates users' answer from front-end and send feedback according to their response.

def check_ans():
It checks users' inputs with the database to calculate the accuracy for them.

def clear():
It will clear the current session record, and restart a new session for you.

===== models.py =====
It imports SQLAlchemy to create databese.

*********************
***** Front-end *****
*********************
===== babyFaceExp.html ===== 
The basic layout for the main experiment page. It imports app.css to do other UI stuffs.

===== thanks.html ===== 
It displays users' score for the guessing experiment.

**********************
***** References *****
**********************
===== face imgs ===== 
http://www.openu.ac.il/home/hassner/Adience/data.html#agegender
