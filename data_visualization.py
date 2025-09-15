"""
Data Visualization Project: Netflix Movies and TV Shows Analysis
Using Seaborn and Matplotlib to create meaningful visualizations
Based on Kaggle Netflix Dataset: https://www.kaggle.com/datasets/shivamb/netflix-shows
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style for better-looking plots
plt.style.use('default')
sns.set_style("whitegrid")
sns.set_palette("husl")

def load_and_prepare_data():
    """Load and prepare the Netflix dataset"""
    try:
        # Load the dataset
        df = pd.read_csv('netflix_titles.csv')
        print(f"Dataset loaded successfully! Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        return df
    except FileNotFoundError:
        print("Dataset file not found. Please ensure 'netflix_titles.csv' is in the current directory.")
        return None

def basic_data_info(df):
    """Display basic information about the dataset"""
    print("\n" + "="*50)
    print("DATASET OVERVIEW")
    print("="*50)
    print(f"Total records: {len(df)}")
    print(f"Total columns: {len(df.columns)}")
    print(f"Date range: {df['date_added'].min()} to {df['date_added'].max()}")
    print(f"Missing values per column:")
    print(df.isnull().sum())
    
    print(f"\nContent types distribution:")
    print(df['type'].value_counts())
    
    print(f"\nTop 10 countries by content:")
    print(df['country'].value_counts().head(10))

def create_visualizations(df):
    """Create various types of visualizations"""
    
    # Set up the plotting area
    fig = plt.figure(figsize=(20, 24))
    
    # 1. Content Type Distribution (Bar Plot)
    plt.subplot(4, 3, 1)
    type_counts = df['type'].value_counts()
    colors = ['#E50914', '#221F1F']  # Netflix red and black
    bars = plt.bar(type_counts.index, type_counts.values, color=colors)
    plt.title('Distribution of Movies vs TV Shows', fontsize=14, fontweight='bold')
    plt.xlabel('Content Type')
    plt.ylabel('Count')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{int(height)}', ha='center', va='bottom', fontweight='bold')
    
    # 2. Release Year Distribution (Histogram)
    plt.subplot(4, 3, 2)
    plt.hist(df['release_year'].dropna(), bins=30, color='skyblue', alpha=0.7, edgecolor='black')
    plt.title('Distribution of Content by Release Year', fontsize=14, fontweight='bold')
    plt.xlabel('Release Year')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    
    # 3. Rating Distribution (Bar Plot)
    plt.subplot(4, 3, 3)
    rating_counts = df['rating'].value_counts().head(10)
    bars = plt.bar(range(len(rating_counts)), rating_counts.values, color='lightcoral')
    plt.title('Top 10 Content Ratings', fontsize=14, fontweight='bold')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.xticks(range(len(rating_counts)), rating_counts.index, rotation=45)
    
    # Add value labels
    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 20,
                f'{int(height)}', ha='center', va='bottom')
    
    # 4. Duration Analysis by Type (Box Plot)
    plt.subplot(4, 3, 4)
    # Extract numeric duration for movies
    df_movies = df[df['type'] == 'Movie'].copy()
    df_movies['duration_minutes'] = df_movies['duration'].str.extract('(\d+)').astype(float)
    
    # Extract numeric duration for TV shows (seasons)
    df_shows = df[df['type'] == 'TV Show'].copy()
    df_shows['duration_seasons'] = df_shows['duration'].str.extract('(\d+)').astype(float)
    
    # Create box plot for movie durations
    plt.boxplot(df_movies['duration_minutes'].dropna(), labels=['Movies'])
    plt.title('Movie Duration Distribution (Minutes)', fontsize=14, fontweight='bold')
    plt.ylabel('Duration (Minutes)')
    
    # 5. Top Countries by Content (Horizontal Bar Plot)
    plt.subplot(4, 3, 5)
    top_countries = df['country'].value_counts().head(10)
    plt.barh(range(len(top_countries)), top_countries.values, color='lightgreen')
    plt.title('Top 10 Countries by Content Count', fontsize=14, fontweight='bold')
    plt.xlabel('Number of Titles')
    plt.yticks(range(len(top_countries)), top_countries.index)
    
    # 6. Content Added Over Time (Line Plot)
    plt.subplot(4, 3, 6)
    df['date_added_clean'] = pd.to_datetime(df['date_added'], errors='coerce')
    monthly_additions = df.groupby(df['date_added_clean'].dt.to_period('M')).size()
    monthly_additions.plot(kind='line', color='purple', linewidth=2)
    plt.title('Content Added to Netflix Over Time', fontsize=14, fontweight='bold')
    plt.xlabel('Date')
    plt.ylabel('Number of Titles Added')
    plt.xticks(rotation=45)
    
    # 7. Genre Analysis (Violin Plot)
    plt.subplot(4, 3, 7)
    # Get top genres
    all_genres = []
    for genres in df['listed_in'].dropna():
        all_genres.extend([genre.strip() for genre in genres.split(',')])
    
    genre_counts = pd.Series(all_genres).value_counts().head(8)
    
    # Create data for violin plot (release years by top genres)
    genre_year_data = []
    genre_labels = []
    
    for genre in genre_counts.index:
        genre_movies = df[df['listed_in'].str.contains(genre, na=False)]
        years = genre_movies['release_year'].dropna()
        if len(years) > 0:
            genre_year_data.append(years)
            genre_labels.append(genre)
    
    if genre_year_data:
        plt.violinplot(genre_year_data, positions=range(len(genre_labels)))
        plt.title('Release Year Distribution by Top Genres', fontsize=14, fontweight='bold')
        plt.xlabel('Genre')
        plt.ylabel('Release Year')
        plt.xticks(range(len(genre_labels)), [label[:15] + '...' if len(label) > 15 else label 
                                            for label in genre_labels], rotation=45)
    
    # 8. Content Type by Rating (Stacked Bar Plot)
    plt.subplot(4, 3, 8)
    rating_type_cross = pd.crosstab(df['rating'], df['type'])
    rating_type_cross.plot(kind='bar', stacked=True, ax=plt.gca())
    plt.title('Content Type Distribution by Rating', fontsize=14, fontweight='bold')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.legend(title='Type')
    plt.xticks(rotation=45)
    
    # 9. Movie Duration vs Release Year (Scatter Plot)
    plt.subplot(4, 3, 9)
    movies_clean = df_movies.dropna(subset=['duration_minutes', 'release_year'])
    plt.scatter(movies_clean['release_year'], movies_clean['duration_minutes'], 
               alpha=0.6, color='orange', s=20)
    plt.title('Movie Duration vs Release Year', fontsize=14, fontweight='bold')
    plt.xlabel('Release Year')
    plt.ylabel('Duration (Minutes)')
    
    # 10. Top Directors (Bar Plot)
    plt.subplot(4, 3, 10)
    top_directors = df['director'].value_counts().head(8)
    plt.bar(range(len(top_directors)), top_directors.values, color='teal')
    plt.title('Top 8 Directors by Content Count', fontsize=14, fontweight='bold')
    plt.xlabel('Director')
    plt.ylabel('Number of Titles')
    plt.xticks(range(len(top_directors)), [name[:15] + '...' if len(name) > 15 else name 
                                         for name in top_directors.index], rotation=45)
    
    # 11. Content by Month Added (KDE Plot)
    plt.subplot(4, 3, 11)
    df['month_added'] = df['date_added_clean'].dt.month
    monthly_dist = df['month_added'].dropna()
    sns.kdeplot(monthly_dist, fill=True, color='red', alpha=0.7)
    plt.title('Distribution of Content Added by Month', fontsize=14, fontweight='bold')
    plt.xlabel('Month')
    plt.ylabel('Density')
    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    
    # 12. TV Show Seasons Distribution (Swarm Plot)
    plt.subplot(4, 3, 12)
    seasons_data = df_shows['duration_seasons'].dropna()
    if len(seasons_data) > 0:
        # Create swarm plot data
        y_data = np.random.normal(0, 0.1, len(seasons_data))
        plt.scatter(seasons_data, y_data, alpha=0.6, s=10, color='darkblue')
        plt.title('TV Show Seasons Distribution', fontsize=14, fontweight='bold')
        plt.xlabel('Number of Seasons')
        plt.ylabel('')
        plt.yticks([])
    
    plt.tight_layout()
    plt.savefig('netflix_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

def generate_insights(df):
    """Generate insights from the data analysis"""
    insights = []
    
    # Content type insights
    movie_count = len(df[df['type'] == 'Movie'])
    show_count = len(df[df['type'] == 'TV Show'])
    total_count = len(df)
    
    insights.append(f"📊 **Content Distribution**: Netflix has {movie_count:,} movies ({movie_count/total_count*100:.1f}%) and {show_count:,} TV shows ({show_count/total_count*100:.1f}%)")
    
    # Release year insights
    recent_content = len(df[df['release_year'] >= 2010])
    insights.append(f"🎬 **Recent Content**: {recent_content:,} titles ({recent_content/total_count*100:.1f}%) were released in 2010 or later")
    
    # Rating insights
    top_rating = df['rating'].value_counts().index[0]
    top_rating_count = df['rating'].value_counts().iloc[0]
    insights.append(f"📺 **Most Common Rating**: {top_rating} is the most common rating with {top_rating_count:,} titles")
    
    # Country insights
    top_country = df['country'].value_counts().index[0]
    top_country_count = df['country'].value_counts().iloc[0]
    insights.append(f"🌍 **Top Country**: {top_country} produces the most content with {top_country_count:,} titles")
    
    # Duration insights
    df_movies = df[df['type'] == 'Movie'].copy()
    df_movies['duration_minutes'] = df_movies['duration'].str.extract('(\d+)').astype(float)
    avg_duration = df_movies['duration_minutes'].mean()
    insights.append(f"⏱️ **Average Movie Duration**: {avg_duration:.1f} minutes")
    
    # Genre insights
    all_genres = []
    for genres in df['listed_in'].dropna():
        all_genres.extend([genre.strip() for genre in genres.split(',')])
    top_genre = pd.Series(all_genres).value_counts().index[0]
    insights.append(f"🎭 **Most Popular Genre**: {top_genre} is the most common genre")
    
    return insights

def main():
    """Main function to run the analysis"""
    print("🎬 Netflix Movies and TV Shows Data Visualization Analysis")
    print("="*60)
    
    # Load data
    df = load_and_prepare_data()
    if df is None:
        return
    
    # Display basic info
    basic_data_info(df)
    
    # Create visualizations
    print("\n📈 Creating visualizations...")
    create_visualizations(df)
    
    # Generate insights
    print("\n💡 Generating insights...")
    insights = generate_insights(df)
    
    print("\n" + "="*50)
    print("KEY INSIGHTS")
    print("="*50)
    for insight in insights:
        print(insight)
    
    print(f"\n✅ Analysis complete! Visualization saved as 'netflix_analysis.png'")

if __name__ == "__main__":
    main()
