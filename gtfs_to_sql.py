tables = ["agency", "calendar", "calendar_dates", "routes", "shapes", "stop_times", "stops", "transfers", "trips"]

for table in tables:
    with open("./gtfs_stcp/" + table + ".txt") as f:
        with open("./gtfs_stcp_sql/" + table + ".sql", "w+") as out:
            for l in f.readlines()[1:]:
                l = l.replace("'", "''")
                arr = l[:-1].split(',')
                s = ""
                print(arr)
                for i in range(len(arr)):
                    s += "'" + arr[i] + "'" +','
                    
                out.write("insert into " + table + " values (" + s[:-1] + ");\n")
                print("insert into", table, "values (", s[:-1], ")")