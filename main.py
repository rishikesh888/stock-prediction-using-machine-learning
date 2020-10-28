def main():
    print("Plotting the nifty data")
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    data = pd.read_csv(r'C:\Users\KOTLA SAI SANDEEP\Downloads\nifty-historical-indices\NIFTY_Data.csv', index_col=0,
                       parse_dates=True)
    closing_date = data['NIFTY_50_CLOSE']
    closing_date.plot(ax=ax, style='b-')
    plt.show()


    print("making a CSV file ")
    data = pd.read_csv(r'C:\Users\KOTLA SAI SANDEEP\Downloads\nifty-historical-indices\NIFTY_Data.csv', index_col=0,
                       parse_dates=True)
    close = data['NIFTY_50_CLOSE']
    a = np.array([])
    for i in range(len(close)-365-1,0,-1):
        a = np.append(a, np.array(
            [close[i], (close[i] - close[i + 7]) / close[i], (close[i] - close[i + 30]) / close[i],
             (close[i] - close[i + 365]) / close[i]]))
    b=a
    a = a.reshape(int(len(a)/4), 4)
    df = pd.DataFrame(a, columns=['day', 'week', 'month', 'year'])
    df.to_csv(r'C:\Users\KOTLA SAI SANDEEP\Desktop\Venkat\NIFTY_C.csv')

    data = pd.read_csv(r'C:\Users\KOTLA SAI SANDEEP\Desktop\Venkat\NIFTY_C.csv')
    x_wm=np.array([])
    x_my=np.array([])
    x_wy=np.array([])
    for i,j,k in zip(data['week'],data['month'],data['year']):
        a1=np.append(i,j).reshape(1,2)
        b1=np.append(j,k).reshape(1,2)
        c1=np.append(i,k).reshape(1,2)
        x_wm=np.append(x_wm,a1)
        x_my=np.append(x_my,b1)
        x_wy=np.append(x_wy,c1)
    x_wm=x_wm.reshape(int(len(x_wm)/2),2)
    x_my=x_my.reshape(int(len(x_my)/2),2)
    x_wy=x_wy.reshape(int(len(x_wy)/2),2)




