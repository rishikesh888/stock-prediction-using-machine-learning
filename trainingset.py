 data = pd.read_csv(r'C:\Users\KOTLA SAI SANDEEP\Desktop\Venkat\NIFTY_C.csv')
    week_and_month = KMeans(n_clusters=3)
    month_and_year = KMeans(n_clusters=3)
    week_and_year = KMeans(n_clusters=3)
    week_and_month.fit(x_wm)
    month_and_year.fit(x_my)
    week_and_year.fit(x_wy)
    y1 = week_and_month.predict(x_wm)
    y2 = month_and_year.predict(x_my)
    y3 = week_and_year.predict(x_wy)





