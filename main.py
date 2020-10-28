import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin
from scipy import stats


def find_cluster(x, n_clusters, reseed=2):
    rng = np.random.RandomState(reseed)
    i = rng.permutation(x.shape[0])[:n_clusters]
    centers = x[i]
    while True:
      labels = pairwise_distances_argmin(x, centers)
      new_centers = np.array([x[labels == i].mean(0) for i in range(n_clusters)])
      if (np.all(centers == new_centers)):
          break
      centers = new_centers
    return (centers, labels)



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














    fig, axs = plt.subplots(3)
    (centers1, labels) = find_cluster(x_wm, 3)
    (centers2, labels) = find_cluster(x_my, 3)
    (centers3, labels) = find_cluster(x_wy, 3)
    axs[0].scatter(x_wm[:, 0], x_wm[:, 1], c=y1, s=50, cmap='viridis')
    axs[0].set(xlabel='week', ylabel='month')
    axs[1].scatter(x_my[:, 0], x_my[:, 1], c=y2, s=50, cmap='viridis')
    axs[1].set(xlabel='month', ylabel='year')
    axs[2].scatter(x_wy[:, 0], x_wy[:, 1], c=y3, s=50, cmap='viridis')
    axs[2].set(xlabel='week', ylabel='year')
    axs[0].scatter(centers1[:, 0], centers1[:, 1], c='pink', s=200, alpha=0.9)
    axs[1].scatter(centers2[:, 0], centers2[:, 1], c='pink', s=200, alpha=0.9)
    axs[2].scatter(centers3[:, 0], centers3[:, 1], c='pink', s=200, alpha=0.9)
    plt.show()

    buy=week_and_month.predict([[0.05,0.1]])
    sell=week_and_month.predict([[-0.02,-0.1]])








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



