import cx_Oracle
import traceback
conn=None
try:
    conn=cx_Oracle.connect("mouzikka/music@127.0.0.1/xe")
    print("connect succesfully to oracle")
except cx_Oracle.DatabaseError:
    print("error in connect to oracle")
    print(traceback.format_exc())
finally:
    if conn is not None:
        conn.close()
        print("disconnected with oracle succesfully")


        #oracle database
        # go to sql lite and write connect then enter username=mouzikka password=music
        # and check select * from tab .kitne row present hai
        # desc myfavourites  .myfavourites table name.