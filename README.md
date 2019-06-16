#ASE 1 FINAL PROJECT PROPOSAL
##College E-wallet



##Project Description

Project Scope: An e-wallet for students to make transactions with vendors in IIITS be added to the wallet from a bank or through PayPal. Students will be able to log in to their accounts using mobile number and password. They can buy coupons from the mess vendor, rent cycles from cycle store or pay library due with the wallet. All the payment details shall be encrypted and the databases of the project shall be secure.

Project Outcome: When the project is complete, any user would be able to login to his/her account and add money through PayPal/bank. When a student sends money to his/her peers, their wallet’s balance shall be updated and would be notified. Students shall be able to pay to the vendors securely, and the vendors shall be informed about the payment.


##Project Team Members

D.Sai Krishna.                         S20170020201
Vasundhara Singh                       S20170010174
A.Anirudh                              S20170010011
S.B.Koushik                 				   S20170010131
D.Sai Ram Praveen Kumar     	         S20170020236
J.Sai Hemanth               			     S20170010059      


##FUNCTIONAL REQUIREMENTS

Shall use a Django based web application as a front-end.
Users shall be able to log in with their email-id and password.
Shall have a secure password authentication system.
Shall be able to recharge e-wallet from bank account.
Shall be able to send money to peers.
Shall support transactions via mobile numbers.
Shall update wallet balance after every transaction.
Shall be able to purchase coupons from vendors.
Sharing mess tokens with peers shall be in.
Paying library dues should be made possible.
Could be able to manage monthly/weekly subscription of cycles.
Peek time price escalation for cycle sharing should be enabled.
Handling payments at canteen should be possible.
Monthly subscription from mess vendors should be enabled.
Mess vendor shall be able to give discounts for the payments.
Admins should be able to create new payment portals.
Shall display a message if transaction is successful/unsuccessful .
Shall handle failed transaction history.
Shall maintain a database of user details, transaction history.
Database shall include user id, wallet balance, transaction log.
User shall be able to check his/her transaction log and available balance.
User shall be able to request an email regarding his transaction receipts.   


##SECURITY:
Shall have a separate backup server which shall be used is the original server is down.
Shall have a separate second database that would be synced with the main database in regular intervals.
128 bit encryption of database using algorithms that ensure security of data according to RBI guidelines for electronic wallets.
Fraud detection algorithms to ensure wallet security.


##MESS VENDOR:
Mess vendor should be able to view received payments.
Mess vendor should be able to put up discounts.
He shall have a facility to stop taking request from the users.


##Non Functional Requirements:
Internet connection shall be required.
Data  from the academic office would be required.
PayPal subscription would be required for the app.
Access to the campus server/AWS server would be required.
Server shall be Able to handle more no of request at a time.
backup for the database shall be done.
google suite service to send emails (Transaction notifications).
merchant bank account would be required.
