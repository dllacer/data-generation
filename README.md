# data-generation
A little python code to generate random user data to test systems.

It generates data according to spanish stuff (phone, id card, names, etc).

It works only in Python 3

## Code example

To generate 10 users with fields Name, Age and Phone:<br/>
`python3 data_generator_complete.py --filename foo.csv --rows_num 10 --name --age --phone`

To generate 20 users with fields Name, Lastname and DNI (id card) everything quoted:<br/>
`python3 data_generator_complete.py --filename foo.csv --rows_num 20 --nameandlastname --dni --quote`
