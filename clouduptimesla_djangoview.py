def cloudmonthlysla(request):
    '''
       Sample django view for monthly SLA report
    '''
    cnxn=[[ DB connection ]]
    sql="select top 4 zone,year,month,sla from auto_sla_monthly order by year desc, month desc"  ## top [[ number of cloud zones ]] for latest month,year
    df = pd.read_sql_query(sql, cnxn)
    year=str(df['year'][0])
    month=int(df['month'][0])
    from calendar import month_name
    month=month_name[month]
    datetile=str(month)+" "+year
    dfsla=df.drop(df.columns[[1,2]],axis=1)   ## year, month columns no longer required
    cloudaverage=dfsla['sla'].mean()
    dfsla.loc[len(dfsla)]=['Cloud All zones',cloudaverage] ## add all zone average row
    dfsla=dfsla.T.to_dict()
    return render(request, 'cloudmonthlysla.html',{'dfsla': dfsla,'datetile': datetile})
