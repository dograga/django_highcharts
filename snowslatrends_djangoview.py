def snowslatrends(request):
'''
   Django view reads snow sla from snow_summary table
'''
    cnxn=[[ DB connection ]]
    sql="select (totaltasks-active) as resolved,breachedsla,month,year,monthlysla from snow_summary"
    dfsla = pd.read_sql_query(sql, cnxn)
    dfsla = dfsla.sort_values(['year','month'])
    dfsla.reset_index(inplace=True)
    dfsla=dfsla.T.to_dict()
    return render(request, 'snowslatrends.html', {'dfsla': dfsla})
