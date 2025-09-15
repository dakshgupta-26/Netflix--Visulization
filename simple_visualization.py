"""
Simple Netflix Data Visualization - Easy to run version
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def main():
    print("🎬 Netflix Data Visualization Analysis")
    print("="*50)
    
    # Load data
    try:
        df = pd.read_csv('netflix_titles.csv')
        print(f"✅ Dataset loaded successfully! Shape: {df.shape}")
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return
    
    # Basic info
    print(f"\n📊 Dataset Overview:")
    print(f"Total records: {len(df)}")
    print(f"Movies: {len(df[df['type'] == 'Movie'])}")
    print(f"TV Shows: {len(df[df['type'] == 'TV Show'])}")
    print(f"Date range: {df['release_year'].min()} - {df['release_year'].max()}")
    
    # Create a simple 2x2 subplot
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Netflix Movies and TV Shows Analysis', fontsize=16, fontweight='bold')
    
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
    ax2.hist(df['release_year'].dropna(), bins=15, color='skyblue', alpha=0.7, edgecolor='black')
    ax2.set_title('Content by Release Year', fontweight='bold')
    ax2.set_xlabel('Release Year')
    ax2.set_ylabel('Frequency')
    
    # 3. Rating Distribution (Bar Plot)
    ax3 = axes[1, 0]
    rating_counts = df['rating'].value_counts().head(6)
    bars = ax3.bar(range(len(rating_counts)), rating_counts.values, color='lightcoral')
    ax3.set_title('Top Content Ratings', fontweight='bold')
    ax3.set_ylabel('Count')
    ax3.set_xticks(range(len(rating_counts)))
    ax3.set_xticklabels(rating_counts.index, rotation=45)
    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + 0.2,
                f'{int(height)}', ha='center', va='bottom', fontsize=9)
    
    # 4. Top Countries (Horizontal Bar)
    ax4 = axes[1, 1]
    top_countries = df['country'].value_counts().head(6)
    ax4.barh(range(len(top_countries)), top_countries.values, color='lightgreen')
    ax4.set_title('Top Countries by Content', fontweight='bold')
    ax4.set_xlabel('Number of Titles')
    ax4.set_yticks(range(len(top_countries)))
    ax4.set_yticklabels([country[:12] + '...' if len(country) > 12 else country 
                        for country in top_countries.index])
    
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('netflix_simple_analysis.png', dpi=300, bbox_inches='tight')
    print(f"\n📈 Visualization saved as 'netflix_simple_analysis.png'")
    
    # Show the plot
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
    
    # Genre analysis
    all_genres = []
    for genres in df['listed_in'].dropna():
        all_genres.extend([genre.strip() for genre in genres.split()])
    if all_genres:
        top_genre = pd.Series(all_genres).value_counts().index[0]
        print(f"🎭 Most Popular Genre: {top_genre}")
    
    print(f"\n✅ Analysis complete!")

if __name__ == "__main__":
    main()
