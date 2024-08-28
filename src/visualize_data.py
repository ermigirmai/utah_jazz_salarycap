import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

num_clusters_by_year = {
    2011: 5,
    2012: 5, 
    2013: 8, 
    2014: 7, 
    2015: 7, 
    2016: 7, 
    2017: 6, 
    2018: 7, 
    2019: 7, 
    2020: 7, 
    2021: 7, 
    2022: 7, 
    2023: 8, 
    2024: 8, 
    2025: 7, 
    2026: 6, 
    2027: 6, 
    2028: 5, 
    2029: 2}

#Method to aggregate data by year and plot
def split_data_and_analyze(contracts):
    #generate_scatter_plot(contracts)
    #generate_elbow_plot
    generate_kmeans_scatter_plot(contracts)   

def generate_scatter_plot(contracts):
    for year, contracts_by_year in contracts.items():
        player_dpm = []
        percent_of_cap = []
        for _, contract in contracts_by_year.items():
            player_dpm.append(contract['player_dpm'])
            percent_of_cap.append(contract['percent_of_cap'])

        '''
        plt.figure(figsize=(10, 6))
        plt.scatter(player_dpm, percent_of_cap, alpha=0.7, edgecolors='w', s=100)
        plt.title(f'{year} DPM vs. Percent of Cap Scatter Plot')
        plt.xlabel('Player DPM')
        plt.ylabel('Percent of Cap')
        plt.grid(True)
        plt.show()
        '''

def generate_kmeans_scatter_plot(contracts):
    for year, contracts_by_year in contracts.items():
        player_dpm = []
        percent_of_cap = []
        for _, contract in contracts_by_year.items():
            player_dpm.append(contract['player_dpm'])
            percent_of_cap.append(contract['percent_of_cap'])
            
        data = list(zip(player_dpm, percent_of_cap))
        kmeans = KMeans(n_clusters=num_clusters_by_year[year]).fit(data)
        centroids = kmeans.cluster_centers_

        np_data = np.array(data)
        ranges = []
        labels = kmeans.labels_
        for i in range(num_clusters_by_year[year]):
            cluster_data = np_data[labels == i]

            player_dpm_values = cluster_data[:, 0]
            player_dpm_median = np.median(player_dpm_values)

            percent_cap_values = cluster_data[:, 1]
            percent_cap_min = np.min(percent_cap_values)
            percent_cap_max = np.max(percent_cap_values)
            bin_count_of_cluster = np.size(percent_cap_values)

            ranges.append((percent_cap_min, percent_cap_max, bin_count_of_cluster, player_dpm_median))
    
        for i, (cluster_min, cluster_max, cluster_size, dpm_median) in enumerate(ranges):
            print(f"{year} Cluster {i} min: {cluster_min} -- max: {cluster_max} -- count: {cluster_size} / DPM Median: {dpm_median}")
        print()

        plt.scatter(player_dpm, percent_of_cap, c=kmeans.labels_)
        plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='o', label='Centroids')

        for i, (cluster_min, cluster_max, cluster_size, dpm_median) in enumerate(ranges):
            plt.axhline(y=cluster_min, color='r', linestyle='--')

        plt.title(f'{year} DPM vs. Percent of Cap Clustered')
        plt.xlabel('Player DPM')
        plt.ylabel('Percent of Cap')
        plt.grid(True)
        plt.savefig(f"../plots/{year}_DPM_vs_Percent_Cap.png")
        plt.close()

def generate_elbow_plot(contracts):

    for year, contracts_by_year in contracts.items():
        player_dpm = []
        percent_of_cap = []
        for _, contract in contracts_by_year.items():
            player_dpm.append(contract['player_dpm'])
            percent_of_cap.append(contract['percent_of_cap'])

    data = list(zip(percent_of_cap, player_dpm))
    inertias = []
    for i in range(1,len(player_dpm)+1):
        kmeans = KMeans(n_clusters=i)
        kmeans.fit(data)
        inertias.append(kmeans.inertia_)

    '''
    plt.plot(range(1,len(player_dpm)+1), inertias, marker='o')
    plt.title(f'{year} Elbow method')
    plt.xlabel('Number of clusters')
    plt.ylabel('Inertia')
    plt.show()
    '''