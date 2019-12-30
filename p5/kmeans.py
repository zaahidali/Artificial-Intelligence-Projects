import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
import numpy as np
import copy

############################## This program is written in Python using PyCharm ################################
x = []
y = []
pdf = PdfPages('plot.pdf')
with open('data.txt', 'r') as f:
    next(f)
    for line in f:
        line = line.split(',')
        x.extend([int(line[0])])
        y.extend([int(line[1])])


df = pd.DataFrame({
    'x': x,
    'y': y
})
#########################################################################################
minx = min(x)
miny = min(y)
maxx = max(x)
maxy = max(y)
colmap = {1: 'b', 2: 'g', 3: 'r', 4: 'c', 5: 'm'}

for k in range(2, 6):
    centroids = {
        i + 1: [np.random.randint(minx, maxx), np.random.randint(miny, maxy)]
        for i in range(k)
    }


    def assignment(df, centroids):
        for i in centroids.keys():
            df['distance_from_{}'.format(i)] = (
                np.sqrt(
                    (df['x'] - centroids[i][0]) ** 2
                    + (df['y'] - centroids[i][1]) ** 2
                )
            )
        centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
        df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
        df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
        df['color'] = df['closest'].map(lambda x: colmap[x])
        return df


    #########################################################################################

    df = assignment(df, centroids)
    print(df.head())

    #########################################################################################
    old_centroids = copy.deepcopy(centroids)


    def update(k):
        for i in centroids.keys():
            centroids[i][0] = np.mean(df[df['closest'] == i]['x'])
            centroids[i][1] = np.mean(df[df['closest'] == i]['y'])
        return k


    #########################################################################################
    centroids = update(centroids)

    df = assignment(df, centroids)

    while True:
        closest_centroids = df['closest'].copy(deep=True)
        centroids = update(centroids)
        df = assignment(df, centroids)
        if closest_centroids.equals(df['closest']):
            break
    #########################################################################################
    fig = plt.figure(figsize=(5, 5))
    plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
    for i in centroids.keys():
        plt.scatter(*centroids[i], color=colmap[i])
    plt.xlim(minx, maxx)
    plt.ylim(miny, maxy)
    plt.title('k = ' + str(k))
    # plt.show()
    # fig.savefig("plot.pdf")
    pdf.savefig(fig)
    plt.close()
pdf.close()