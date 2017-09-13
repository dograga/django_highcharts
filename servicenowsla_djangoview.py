def snowmonthlysla(request):
    '''
       Sample django view for monthly ServiceNow SLA report
       Data collection codes on ServiceNow repo
    '''
    sql="select top 1 year, month, monthlysla from snow_summary order by year desc, month desc"
    cnxn=[[ get DB connection]]
    df= pd.read_sql_query(sql, cnxn)
    year=str(df['year'][0])
    month=int(df['month'][0])
    year=int(df['year'][0])
    month=int(df['month'][0])
    from calendar import month_name
    month=month_name[month]
    datetile=str(month)+" "+str(year)
    dfsla=df.drop(df.columns[[0,1]],axis=1)
    dfsla=dfsla.T.to_dict()
    return render(request, 'snowmonthlysla.html',{'dfsla': dfsla,'datetile': datetile})
