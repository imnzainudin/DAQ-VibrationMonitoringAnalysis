-----------------------------------------------------------------------
Vibration Online Data Acquisition System (DAQ)
-----------------------------------------------------------------------

Vibration Online Data Acquisition (DAQ) is a system for monitoring real-time data from a hardware. 
This system also enables user to do Time-Domain Analysis and Frequency-Domain Analysis.

-----------------------------------------------------------------------
Acknowledgement
-----------------------------------------------------------------------

This project is created as a requirement to complete intership training at 
Universiti Tun Hussein Onn Malaysia (UTHM). 
Thanks to Muhammad Iman Bin Zainudin, @imnzainudin, for completing and sharing this project files.

-----------------------------------------------------------------------
Usage Tips
-----------------------------------------------------------------------

This project consisting two different folders, each with different virtual environment set for each
folder and one folder consisting hardware Arduino code. The SERVER and IMAN ZAINUDIN folder ideally should be installed in different directory for
a better environment settings.

Each folder are included with requirements.txt file which can be use to install all the package
needed for the project to work.

-----------------------------------------------------------------------
Installation
-----------------------------------------------------------------------

This module is tested on Python 3.9+ on Visual Studio Code (VS Code) Windows 10.
The project folder are saved on saperate directories on Desktop.

***************
    SERVER
***************

1. Install Python 3.9+. Check out documentation's FAQ for additional guidelines: https://www.python.org/doc/
2. Docker will be used to manage Redis-server for this project. Check out documetation's FAQ for additional guidelines: https://docs.docker.com/get-docker/
3. To install virtual environment, virtualenv, use: $ pip install virtualenv
4. Enter enviroment path with $ cd <environment_names>. For example: $ cd environment and activate virtualenv
using: $ .\Scripts\activate
5. Install all package dependencies using command $ pip install -r requirements.txt
6. Activate Redis-server using docker using $ docker run -p 6379:6379 -d redis:5
7. Run the django development server with $ python manage.py runserver

***************
 IMAN ZAINUDIN
***************

1. Install Python 3.9+. Check out documentation's FAQ for additional guidelines: https://www.python.org/doc/
2. To install virtual environment, virtualenv, use: $ pip install virtualenv
3. Enter enviroment path with $ cd <environment_names>. For example: $ cd environment and activate virtualenv
using: $ .\Scripts\activate
4. Install all package dependencies using command $ pip install -r requirements.txt
5. Connect the hardware to the machine port. Change the computer port number in the code if needed.
6. Run the code after running django development server.

*****************
    Hardware
*****************

This is an Arduino code which utilize FreeRTOS to use dual-core processor. The components used for
this project:

1. ESP32 Devkit-V1
2. GY61 DXL335 3-Axis Accelerometer module
3. DHT22 Temperature & Humidity sensor