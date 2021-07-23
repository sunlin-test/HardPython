sql_file = open('test_input.sql', 'a+')

for i in range(50000):
    sql_file.write("select * from tab_t1 limit 1;")
    if i == (50000-1):
        print i


sql_file.close()


