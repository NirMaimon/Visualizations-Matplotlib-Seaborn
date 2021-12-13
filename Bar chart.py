#-------------------------------------------------------------------------------
#Bar Charts with Python & Matplotlib
# https://medium.com/@anshulrajput046/bar-charts-with-python-matplotlib-7eaac7ae76c9
#-------------------------------------------------------------------------------
# all kinds of bar charts




#-------------------------------------------------------------------------------
#Easy grouped bar charts in Python
#https://towardsdatascience.com/easy-grouped-bar-charts-in-python-b6161cdd563d
-------------------------------------------------------------------------------
#How to create bar charts with two, three or more bars per entry






#-------------------------------------------------------------------------------
#--Bar Plot  -- with seaborn and matplotlib
# https://betterprogramming.pub/3-how-to-python-code-snippets-for-data-analysts-6a9b850c254d
#-------------------------------------------------------------------------------


df = pd.read_excel('D:/NirM/Python/20-Solar-PowerPlats.xlsx')

# Set up Matplotlib Figure
f, ax1 = plt.subplots(1, 1, figsize=(9, 4))

# Set up the data for the visualization
data_for_plot = df.groupby(by='Country').sum()
data_for_plot.reset_index(inplace=True)
data_for_plot.sort_values(by='Area_Acres', inplace=True)
values_on_x_axis = 'Country'
values_on_y_axis = 'Area_Acres'

# Setup actual data visualization in Seaborn
sns.barplot(x=values_on_x_axis,y=values_on_y_axis,
            data=data_for_plot,
            ax = ax1,
            palette="Blues")

# Set additional elements of the Visualization

plt.title("Total Area per country", fontsize=20)
plt.xlabel("Country", fontsize=15)
plt.ylabel("Total Area in Acres", fontsize=15)
