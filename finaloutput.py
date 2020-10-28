 while(True):
        data = pd.read_csv(r"C:\Users\KOTLA SAI SANDEEP\Desktop\Venkat\NIFTY_C.csv")
        value_predict = float(input("enter the data to predict"))
        week = (value_predict - data.values[:,1][-7]) / data.values[:,1][-7]
        month = (value_predict - data.values[:,1][-30]) / data.values[:,1][-30]
        year = (value_predict - data.values[:,1][-7]) / data.values[:,1][-365]
        c = np.array([value_predict, week, month, year]).reshape(1, 4)
        a=np.append(a,c)
        a=a.reshape(int(len(a)/4),4)
        df = pd.DataFrame(a,columns=['day','week','month','year'])
        df.to_csv(r"C:\Users\KOTLA SAI SANDEEP\Desktop\Venkat\NIFTY_C.csv")
        r1 = week_and_month.predict([[week, month]])
        r2 = month_and_year.predict([[month, year]])
        r3 = week_and_year.predict([[week, year]])
        axs[0].scatter(week, month, c='blue',s=200,alpha=0.5)
        plt.show()
        p=stats.mode([r1,r2,r3])[0]
        if(p==sell):
            print("Sell the Stock")
        elif(p==buy):
            print("Buy the Stock")
        else:
            print("Neither Buy nor sell the Stock")
        ch=int(input("Press 1 to continue.."))
        if(ch!=1):
            break






main()







