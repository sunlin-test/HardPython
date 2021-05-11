sql_file = open('2G.sql', 'a+')

for i in range(8000000):
    sql_file.write("insert into tab_t2 values('sdfsfsdfsfsasdfsdfsdfsdfsfsdfsdfsdfsfsdfdssdfdsdfs','sdfsfsdfsfsasdfsdfsdfsdfsfsdfsdfsdfsfsdfdssdfdsdfs');\n")
    if i == (8000000-1):
        print i


sql_file.close()


