def result_as_dict(cursor):
    columns=[column[0] for column in cursor.description]
    result=[]
    for row in cursor.fetchall():
        result1=dict()
        for i in range(len(columns)):
            result1[columns[i]]=row[i]
        result.append(result1)
    return result