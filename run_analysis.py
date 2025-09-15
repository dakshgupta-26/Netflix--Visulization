"""
Simple script to run Netflix data visualization analysis
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

def main():
    print("🎬 Netflix Data Visualization Analysis")
    print("="*50)
    
    # Load data
    try:
        df = pd.read_csv('netflix_titles.csv', encoding='utf-8', on_bad_lines='skip')
        print(f"✅ Dataset loaded successfully! Shape: {df.shape}")
    except FileNotFoundError:
        print("❌ Dataset file 'netflix_titles.csv' not found!")
        return
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return
    
    # Basic info
    print(f"\n📊 Dataset Overview:")
    print(f"Total records: {len(df)}")
    print(f"Movies: {len(df[df['type'] == 'Movie'])}")
    print(f"TV Shows: {len(df[df['type'] == 'TV Show'])}")
    print(f"Date range: {df['release_year'].min()} - {df['release_year'].max()}")
    
    # Create visualizations
    print("\n📈 Creating visualizations...")
    
    # Set up the plotting area
    fig, axes = plt.subplots(3, 4, figsize=(20, 15))
    fig.suptitle('Netflix Movies and TV Shows Analysis', fontsize=20, fontweight='bold')
    
    # 1. Content Type Distribution (Bar Plot)
    ax1 = axes[0, 0]
    type_counts = df['type'].value_counts()
    colors = ['#E50914', '#221F1F']  # Netflix colors
    bars = ax1.bar(type_counts.index, type_counts.values, color=colors)
    ax1.set_title('Movies vs TV Shows', fontweight='bold')
    ax1.set_ylabel('Count')
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{int(height)}', ha='center', va='bottom', fontweight='bold')
    
    # 2. Release Year Distribution (Histogram)
    ax2 = axes[0, 1]
    ax2.hist(df['release_year'].dropna(), bins=20, color='skyblue', alpha=0.7, edgecolor='black')
    ax2.set_title('Content by Release Year', fontweight='bold')
    ax2.set_xlabel('Release Year')
    ax2.set_ylabel('Frequency')
    
    # 3. Rating Distribution (Bar Plot)
    ax3 = axes[0, 2]
    rating_counts = df['rating'].value_counts().head(8)
    bars = ax3.bar(range(len(rating_counts)), rating_counts.values, color='lightcoral')
    ax3.set_title('Top Content Ratings', fontweight='bold')
    ax3.set_ylabel('Count')
    ax3.set_xticks(range(len(rating_counts)))
    ax3.set_xticklabels(rating_counts.index, rotation=45)
    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + 0.2,
                f'{int(height)}', ha='center', va='bottom', fontsize=8)
    
    # 4. Top Countries (Horizontal Bar)
    ax4 = axes[0, 3]
    top_countries = df['country'].value_counts().head(8)
    ax4.barh(range(len(top_countries)), top_countries.values, color='lightgreen')
    ax4.set_title('Top Countries by Content', fontweight='bold')
    ax4.set_xlabel('Number of Titles')
    ax4.set_yticks(range(len(top_countries)))
    ax4.set_yticklabels([country[:15] + '...' if len(country) > 15 else country 
                        for country in top_countries.index])
    
    # 5. Movie Duration Analysis (Box Plot)
    ax5 = axes[1, 0]
    df_movies = df[df['type'] == 'Movie'].copy()
    df_movies['duration_minutes'] = df_movies['duration'].str.extract(r'(\d+)').astype(float)
    ax5.boxplot(df_movies['duration_minutes'].dropna(), labels=['Movies'])
    ax5.set_title('Movie Duration Distribution', fontweight='bold')
    ax5.set_ylabel('Duration (Minutes)')
    
    # 6. Content Added Over Time (Line Plot)
    ax6 = axes[1, 1]
    df['date_added_clean'] = pd.to_datetime(df['date_added'], errors='coerce')
    yearly_additions = df.groupby(df['date_added_clean'].dt.year).size()
    ax6.plot(yearly_additions.index, yearly_additions.values, marker='o', linewidth=2, color='purple')
    ax6.set_title('Content Added Over Time', fontweight='bold')
    ax6.set_xlabel('Year')
    ax6.set_ylabel('Titles Added')
    
    # 7. Genre Analysis (Violin Plot)
    ax7 = axes[1, 2]
    all_genres = []
    for genres in df['listed_in'].dropna():
        all_genres.extend([genre.strip() for genre in genres.split(',')])
    genre_counts = pd.Series(all_genres).value_counts().head(6)
    
    # Create data for violin plot
    genre_year_data = []
    genre_labels = []
    for genre in genre_counts.index:
        genre_movies = df[df['listed_in'].str.contains(genre, na=False)]
        years = genre_movies['release_year'].dropna()
        if len(years) > 0:
            genre_year_data.append(years)
            genre_labels.append(genre[:10])
    
    if genre_year_data:
        parts = ax7.violinplot(genre_year_data, positions=range(len(genre_labels)))
        ax7.set_title('Release Years by Genre', fontweight='bold')
        ax7.set_ylabel('Release Year')
        ax7.set_xticks(range(len(genre_labels)))
        ax7.set_xticklabels(genre_labels, rotation=45)
    
    # 8. Content Type by Rating (Stacked Bar)
    ax8 = axes[1, 3]
    rating_type_cross = pd.crosstab(df['rating'], df['type'])
    rating_type_cross.plot(kind='bar', stacked=True, ax=ax8, color=['#E50914', '#221F1F'])
    ax8.set_title('Content Type by Rating', fontweight='bold')
    ax8.set_xlabel('Rating')
    ax8.set_ylabel('Count')
    ax8.legend(title='Type')
    ax8.tick_params(axis='x', rotation=45)
    
    # 9. Movie Duration vs Release Year (Scatter Plot)
    ax9 = axes[2, 0]
    movies_clean = df_movies.dropna(subset=['duration_minutes', 'release_year'])
    ax9.scatter(movies_clean['release_year'], movies_clean['duration_minutes'], 
               alpha=0.6, color='orange', s=20)
    ax9.set_title('Movie Duration vs Release Year', fontweight='bold')
    ax9.set_xlabel('Release Year')
    ax9.set_ylabel('Duration (Minutes)')
    
    # 10. Top Directors (Bar Plot)
    ax10 = axes[2, 1]
    top_directors = df['director'].value_counts().head(6)
    ax10.bar(range(len(top_directors)), top_directors.values, color='teal')
    ax10.set_title('Top Directors', fontweight='bold')
    ax10.set_ylabel('Number of Titles')
    ax10.set_xticks(range(len(top_directors)))
    ax10.set_xticklabels([name[:12] + '...' if len(name) > 12 else name 
                         for name in top_directors.index], rotation=45)
    
    # 11. Content by Month Added (KDE Plot)
    ax11 = axes[2, 2]
    df['month_added'] = df['date_added_clean'].dt.month
    monthly_dist = df['month_added'].dropna()
    if len(monthly_dist) > 0:
        sns.kdeplot(monthly_dist, fill=True, color='red', alpha=0.7, ax=ax11)
        ax11.set_title('Content Added by Month', fontweight='bold')
        ax11.set_xlabel('Month')
        ax11.set_ylabel('Density')
        ax11.set_xticks(range(1, 13))
        ax11.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    
    # 12. TV Show Seasons Distribution (Swarm Plot)
    ax12 = axes[2, 3]
    df_shows = df[df['type'] == 'TV Show'].copy()
    df_shows['duration_seasons'] = df_shows['duration'].str.extract(r'(\d+)').astype(float)
    seasons_data = df_shows['duration_seasons'].dropna()
    if len(seasons_data) > 0:
        y_data = np.random.normal(0, 0.1, len(seasons_data))
        ax12.scatter(seasons_data, y_data, alpha=0.6, s=15, color='darkblue')
        ax12.set_title('TV Show Seasons', fontweight='bold')
        ax12.set_xlabel('Number of Seasons')
        ax12.set_ylabel('')
        ax12.set_yticks([])
    
    plt.tight_layout()
    plt.savefig('netflix_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Generate insights
    print("\n💡 Key Insights:")
    print("="*30)
    
    movie_count = len(df[df['type'] == 'Movie'])
    show_count = len(df[df['type'] == 'TV Show'])
    total_count = len(df)
    
    print(f"📊 Content Distribution: {movie_count} movies ({movie_count/total_count*100:.1f}%) and {show_count} TV shows ({show_count/total_count*100:.1f}%)")
    
    recent_content = len(df[df['release_year'] >= 2010])
    print(f"🎬 Recent Content: {recent_content} titles ({recent_content/total_count*100:.1f}%) released in 2010 or later")
    
    top_rating = df['rating'].value_counts().index[0]
    top_rating_count = df['rating'].value_counts().iloc[0]
    print(f"📺 Most Common Rating: {top_rating} with {top_rating_count} titles")
    
    top_country = df['country'].value_counts().index[0]
    top_country_count = df['country'].value_counts().iloc[0]
    print(f"🌍 Top Country: {top_country} produces {top_country_count} titles")
    
    if len(df_movies) > 0:
        avg_duration = df_movies['duration_minutes'].mean()
        print(f"⏱️ Average Movie Duration: {avg_duration:.1f} minutes")
    
    all_genres = []
    for genres in df['listed_in'].dropna():
        all_genres.extend([genre.strip() for genre in genres.split(',')])
    if all_genres:
        top_genre = pd.Series(all_genres).value_counts().index[0]
        print(f"🎭 Most Popular Genre: {top_genre}")
    
    print(f"\n✅ Analysis complete! Visualization saved as 'netflix_analysis.png'")

if __name__ == "__main__":
    main()
