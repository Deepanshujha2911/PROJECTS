# step1 -> import the important libraries 
import pandas as pd
import matplotlib.pyplot as plt

# step2-> read the data from csv
df=pd.read_csv("star.csv")
print(df.head())

#step3-> clean the data 
# print(df.columns)
df=df.dropna(subset=["show_type","rating ","view's(million)","duration (min)","relese_year"])
# dropna function remove the row contaning NaN or inf value 

#step-> use of matplotlib to generate png of charts ,graph 


#MOVIE VS REALITYSHOW VS SERIES BAR GRAPH
type=df["show_type"].value_counts()  
#type is variabl and value count take data from show_type row 
plt.figure(figsize=(6,5))#jo figuare aayega uska size declare 
plt.bar(type.index,type.values,color='red',label='show type ')
plt.title("Bar graph of show types ")
plt.xlabel("type")
plt.ylabel("count")
plt.tight_layout()
plt.savefig("show_type.png") 
# plt.show()


#PIE CHART OF RATING COLUMN
rating=df["rating "].value_counts()
plt.figure(figsize=(7,5))
plt.pie(rating,labels=rating.index,autopct='%1.1f%%')
plt.title("pie chart of rating ")
plt.tight_layout()
plt.savefig("pie_chart.png")
# plt.show()

#HISTOGRAM OF MOVIE DURATION
movie_df=df[df["show_type"] == "movie"].copy()
movie_df['duration_int']=movie_df['duration (min)']

plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'],bins=5,color="blue",edgecolor="black")
plt.title('Movie duration histogram')
plt.xlabel('Duration in minuutes')
plt.ylabel("Number of movie ")
plt.tight_layout()
plt.savefig("histogram.png")
# plt.show()

#scatter plot of realease year 

release=df["relese_year"].value_counts().sort_index()
plt.figure(figsize=(8,5))
plt.scatter(release.index,release.values,color='red',marker='^')
plt.title("Scatter plot of release year")
plt.xlabel('release year')
plt.legend()
plt.ylabel('number of movie')
plt.tight_layout()
plt.savefig("scatter.png")
plt.show()
