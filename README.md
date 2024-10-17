This application is being developed as a recruitment task.
PESEL via wikipedia: 'Universal Electronic System for Registration of the Population' is the national identification number used in Poland since 1979. The number is 11 digits long, identifies exactly one person, and cannot be changed once assigned, except in specific situations.
App is anable to check correctness of PESEL number, and provide feedback about incorrect or correct PESEL with information of gender and birth date. 

# Installation:
1. Clone this repository.
2. Contact with me for SECRET_KEY.
3. Install requirements: <code>pip install -r requirements.txt</code>
4. Enter <code>python manage.py runserver</code> in terminal.

# How to use:
1. Visit <code>http://127.0.0.1:8000/</code>
2. Enter Pesel:

![alt text](readme_images/image.png)

3. Wait for result: (PESEL from generator: https://pesel.cstudios.pl/o-generatorze/generator-on-line)

correct:

![alt text](readme_images/image-1.png)

or for incorrect PESEL:

![alt text](readme_images/image-2.png)


![alt text](readme_images/image-3.png)


![alt text](readme_images/image-4.png)


Tests passed:


![alt text](readme_images/image-5.png)