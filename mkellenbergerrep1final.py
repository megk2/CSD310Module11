import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "willson_owner",
    "password": "finances",
    "host": "127.0.0.1",
    "port": "3306", #change this to port number 3306, or remove entirely depending on user.
    "database": "willson_financial",
    "raise_on_warnings": True

}




try:

    db = mysql.connector.connect(**config)
    print("\nDatabase user connected to MySQL on host {} with database {}".format(
        config["user"], config["host"], config["database"]))

    cursor = db.cursor()

    cursor.execute("select customer.customer_name, customer.date_added from customer where customer.date_added > DATE_SUB(now(), INTERVAL 6 MONTH) group by customer.date_added, customer.customer_name order by customer.date_added DESC")

    my_results = cursor.fetchall()
    print("Display results by month added for last 6 months in descending order--")

    for x in my_results:
        print(x)


except mysql.connector.Error as err:

    if err.errno==errorcode.ERROR_ER_ACCESS_DENIED_ERROR:
        print("The supplied username and password are invalid")
    elif err.errno==errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
finally:
    db.close()

#some code modified from teammate report 3, Dylan Bonis


