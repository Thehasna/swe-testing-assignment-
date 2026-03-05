\# Quick-Calc



Quick-Calc is a simple calculator application written in Python. It can perform addition, subtraction, multiplication, division, and clear the result. The application is fully tested using unit and integration tests.





\## Setup Instructions



1\. Make sure Python 3.10+ is installed on your computer.

2\. Open Command Prompt and go to the project folder:





\## How to Run Tests



To run all unit and integration tests, open Command Prompt in the project folder and type:





\## Testing Framework Comparison: Pytest vs Unittest



\*\*Pytest\*\* is a modern testing framework for Python. It is simple to use, requires less boilerplate code, and allows writing readable tests using plain Python functions. Pytest also has powerful features like fixtures, parameterized tests, and detailed failure reports.



\*\*Unittest\*\* is the built-in Python testing framework. It uses a class-based structure which can be more formal and structured, but requires more code to set up each test. Unittest is good for large projects and for developers who prefer object-oriented testing.



For this project, Pytest was chosen because it allows writing quick, readable tests for our calculator functions and easily runs both unit and integration tests with a single command.



Clone the repository

git clone https://github.com/yourusername/swe-testing-assignment.git

Navigate into the project folder

cd swe-testing-assignment

Install required dependencies

pip install pytest

Running the Application

To run the calculator application:



python app.py

The program will prompt the user to enter numbers and select an operation.



Running the Tests

The project uses the Pytest testing framework.



To run the full test suite:



pytest

This command will automatically discover and execute all tests located in the tests directory.



Testing Framework Research

Pytest

Pytest is a widely used Python testing framework known for its simplicity and flexibility. It allows developers to write test cases using simple Python functions instead of complex class structures. Pytest provides features such as automatic test discovery, fixtures, and powerful assertion introspection, making it easier to write and maintain tests.



Another advantage of Pytest is that it requires less boilerplate code, which makes test files shorter and more readable. Because of these features, Pytest is commonly used in modern Python development projects.



Unittest

Unittest is Python’s built-in testing framework and is inspired by the JUnit testing framework used in Java. It uses a class-based structure where test cases are organized into classes and methods. Unittest is reliable and stable since it is included in the Python standard library, meaning it does not require any external installation.



However, writing tests in Unittest often requires more code and setup compared to Pytest. Assertions are also less readable, which can make tests harder to understand for beginners.



Framework Choice

For this project, Pytest was chosen as the primary testing framework. Pytest provides a simpler syntax, automatic test discovery, and better readability compared to Unittest. These features make it more suitable for small projects like Quick-Calc where quick development and clear test cases are important.



Version

Current release: v1.0.0



This release includes the initial implementation of the Quick-Calc application along with unit tests, integration tests, and project documentation.

