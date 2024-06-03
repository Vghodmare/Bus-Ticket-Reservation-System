Step-by-Step Process for Setting Up and Running a Flask Application
Prerequisites
Install Python:

Ensure Python is installed on your system. You can download it from python.org.
During installation, make sure to check the option to add Python to your PATH.
Install a Code Editor:

Install a code editor like Visual Studio Code, Sublime Text, or any other of your choice.
Step 1: Create Project Directory
Open a Command Prompt or PowerShell.
Navigate to the directory where you want to create your project:
sh
Copy code
cd path\to\your\desired\directory
Create the project directory:
sh
Copy code
mkdir BusTicketReservation
cd BusTicketReservation
Step 2: Set Up a Virtual Environment
Create a virtual environment:
sh
Copy code
python -m venv venv
Activate the virtual environment:
On Windows:
sh
Copy code
.\venv\Scripts\activate
Step 3: Install Flask
Install Flask using pip:
sh
Copy code
pip install Flask
Step 4: Create Directory Structure
Create the templates folder:
sh
Copy code
mkdir templates
Create the static folder:
sh
Copy code
mkdir static
Step 5: Create Python Script
Open your code editor.
Create a file named app.py in the project root directory.
Write the Flask application code (Refer to step-by-step code documentation).
Step 6: Create HTML Templates
In the templates folder, create the following files:
index.html
output.html
Write the HTML code for the templates (Refer to step-by-step code documentation).
Step 7: Create CSS for Styling
In the static folder, create a file named styles.css.
Write the CSS code for styling (Refer to step-by-step code documentation).
Step 8: Run the Flask Application
Activate the virtual environment (if not already activated):
sh
Copy code
.\venv\Scripts\activate
Run the Flask application:
sh
Copy code
python app.py
Step 9: Access the Application
Open your web browser.
Navigate to:
arduino
Copy code
http://127.0.0.1:5000/
Troubleshooting
Error: The term 'app.py' is not recognized as the name of a cmdlet...:

Ensure you are in the correct directory.
Use .\app.py to run the script in PowerShell.
Static Files Not Loading:

Ensure the static folder is named correctly and placed at the same level as app.py.
Ensure the file paths in the HTML files use the correct syntax for loading static files.
Form Submission Errors:

Ensure all form field names match those expected in the Flask route (e.g., name, email, from, to, date, seats).
Conclusion
By following these steps, you should be able to set up and run your Bus Ticket Reservation System using Flask. If you encounter any issues, refer to the troubleshooting section or check the terminal for error messages.
