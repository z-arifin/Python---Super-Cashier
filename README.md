# Python---Super-Cashier

# Background
Final assignment for Python Learning in Pacmann Academy, we are required to create features for a self-service checkout counter at a supermarket. Customers can enter their own purchases using this cashier system. The customers can enter the goods, quantities, and pricing of their purchases, and also able to edit their previous input. Discount and payment calculation are also included.

This project was motivated by the needs of Andi, who is a supermarket owner. Andi aims to create a cashier self-service digital system. Thus, customers can carry out the transaction process independently, and can also be accessed by customers outside the city. Andi request us to provide the system (programming using Python) with some features on this system.

Project Objective
Provide cashier self-service system with Python with the requested features
Ensure the system has fulfilled all of Andi’s requests and needs
Do a test on the system that has been created and make sure it runs well

# Requirement/Objective
The following is a list of requirements to accomplish the project:

1. Customers are able enter their purchases, including the quantities and price.
2. Customers are able to edit their previous input.
3. Customers have option either to delete their purchases one by one or all at once.
4. Discount calculation for each transaction.
5. Final payment calculation for each transaction.

**Flowchart**
![image](https://user-images.githubusercontent.com/83034551/218335053-3a11c799-8c37-43dc-9d8d-d86f56590f4b.png)


# Function & Attribute
Based on Andi’s need there is some mandatory feature on our system there are:

add_item ⇒ to add the item name, quantity, and the price
update_item_name ⇒ to change the item name if the first input is the wrong value
update_item_qty ⇒ to change the quantity if the first input is the wrong value
update_item_price ⇒ to change the price if the first input is the wrong value
delete_item ⇒ to remove one of the items that have been inputted
reset_transaction ⇒ to remove all items
check_order ⇒ to check the item has been inputted in the table form
total_price ⇒ to calculate the total price before discount
total_cost (additional) ⇒ to calculate the total cost after discount
This feature should be arranged on 2 documents py those are:

super_cashier.py (document modular code contains: class and function)
test_case.py (document cashier self-service system code)

Note:
Discount rule:

if total price > Rp 200000 ⇒ discount = 5%
if total price > Rp 300000 ⇒ discount = 8%
if total price > Rp 500000 ⇒ discount = 10%

# Test Case
![1](https://user-images.githubusercontent.com/83034551/218335805-fe03f787-9806-411f-bf67-88051a9b4ae5.jpg)
![2](https://user-images.githubusercontent.com/83034551/218335798-a18075b3-0359-4c62-b4cc-7debb3003115.jpg)
![3](https://user-images.githubusercontent.com/83034551/218335799-fa51c32a-1b6a-403b-9432-9312bd2af1fd.jpg)
![4](https://user-images.githubusercontent.com/83034551/218335800-0839cdaf-1c89-4b2a-90f0-3332e0fd52a2.JPG)
![5](https://user-images.githubusercontent.com/83034551/218335801-a5abef1a-0296-4abc-b5ae-5366104ce391.jpg)
![6](https://user-images.githubusercontent.com/83034551/218335803-c7c1aa2b-a3ac-4451-98fd-8914ba3575b6.JPG)


# Conclusion
With the result of the test for the python script (code) that have created, it can be concluded that:

The script on test_case.py can be used to satisfy Andi's needs with the requirements that have been requested, which features have been defined in the modular super_cashier.py
The features and requirements Andi's need already covered on the system has been developed
Currently, the system is running well and also has effective responses when an error occurs (user input wrong data/type)

