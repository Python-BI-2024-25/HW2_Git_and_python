# Homework for the Python Bioinformatics course 2024/2025
This task was completed by the brave team of five samurais:

 - Ivan Chicherin
 - Anna Kalygina
 - Mark Kachanovskiy
 - Kirill Vishnyakov
 - Ekaterina Scheglova

![team_photo](team_photo.png)

## How the script works
   
Our code implements a simple calculator that performs four different mathematical operations: addition, subtraction, multiplication, and division. 
The calculator accepts input in the form of a string `"int_1 operator int_2"`, where:

- int_1 and int_2 are numbers (either integers or floats).
- operator is one of the following: +, -, *, /.

The scripts recognises the operator being passed and calls  corresponding function to compute the result. Here is the short discription of each function:

### Add

If the script receives the operator `+`, it performs basic addition:

int_1 + int_2

### Subtract

For the operator `-`, the script performs subtraction:

int_1 - int_2

### Multiply

When the operator is `*`, the script performs multiplication:

int_1 * int_2

### Divide

For the operator `/`, the script performs division:

int_1 / int_2

The function includes a check to ensure that division by zero is not allowed.
