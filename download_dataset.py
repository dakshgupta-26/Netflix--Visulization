"""
Script to download the Netflix Movies and TV Shows dataset from Kaggle
"""

import os
import zipfile
import pandas as pd

def create_sample_dataset():
    """Create a sample dataset for demonstration purposes"""
    print("Creating sample Netflix dataset...")
    
    # Sample data
    sample_data = {
        'show_id': ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10'],
        'type': ['Movie', 'TV Show', 'Movie', 'TV Show', 'Movie', 'Movie', 'TV Show', 'Movie', 'TV Show', 'Movie'],
        'title': ['The Crown', 'Stranger Things', 'Bird Box', 'Money Heist', 'Extraction', 'The Irishman', 'Ozark', '6 Underground', 'The Witcher', 'Red Notice'],
        'director': ['Peter Morgan', 'Matt Duffer', 'Susanne Bier', 'Álex Pina', 'Sam Hargrave', 'Martin Scorsese', 'Jason Bateman', 'Michael Bay', 'Lauren Schmidt', 'Rawson Marshall'],
        'cast': ['Claire Foy, Matt Smith', 'Millie Bobby Brown, Finn Wolfhard', 'Sandra Bullock, Trevante Rhodes', 'Úrsula Corberó, Álvaro Morte', 'Chris Hemsworth, Rudhraksh Jaiswal', 'Robert De Niro, Al Pacino', 'Jason Bateman, Laura Linney', 'Ryan Reynolds, Mélanie Laurent', 'Henry Cavill, Anya Chalotra', 'Dwayne Johnson, Ryan Reynolds'],
        'country': ['United Kingdom', 'United States', 'United States', 'Spain', 'United States', 'United States', 'United States', 'United States', 'United States', 'United States'],
        'date_added': ['2016-11-04', '2016-07-15', '2018-12-21', '2017-05-02', '2020-04-24', '2019-11-27', '2017-07-21', '2019-12-13', '2019-12-20', '2021-11-12'],
        'release_year': [2016, 2016, 2018, 2017, 2020, 2019, 2017, 2019, 2019, 2021],
        'rating': ['TV-MA', 'TV-14', 'R', 'TV-MA', 'R', 'R', 'TV-MA', 'R', 'TV-MA', 'PG-13'],
        'duration': ['4 Seasons', '4 Seasons', '124 min', '5 Seasons', '116 min', '209 min', '4 Seasons', '128 min', '2 Seasons', '118 min'],
        'listed_in': ['British TV Shows, TV Dramas, TV Mysteries', 'Crime TV Shows, International TV Shows, TV Action & Adventure', 'International Movies, Thrillers', 'Crime TV Shows, International TV Shows, Spanish-Language TV Shows', 'Action & Adventure, International Movies, Thrillers', 'Dramas, International Movies', 'Crime TV Shows, TV Dramas, TV Mysteries', 'Action & Adventure, International Movies, Thrillers', 'TV Action & Adventure, TV Dramas, TV Fantasy', 'Action & Adventure, Comedies, International Movies'],
        'description': ['A royal drama about the reign of Queen Elizabeth II', 'Supernatural thriller set in 1980s Indiana', 'Post-apocalyptic thriller about mysterious creatures', 'Spanish heist drama series', 'Action thriller about a black-ops mercenary', 'Epic crime drama about organized crime', 'Financial advisor turned money launderer', 'Action thriller about a billionaire vigilante', 'Fantasy series based on the book series', 'Action comedy heist film']
    }
    
    # Create DataFrame
    df = pd.DataFrame(sample_data)
    
    # Save to CSV
    df.to_csv('netflix_titles.csv', index=False)
    print("Sample dataset created successfully!")
    return df

def download_kaggle_dataset():
    """Download the actual dataset from Kaggle (requires Kaggle API)"""
    try:
        import kaggle
        
        print("Downloading Netflix dataset from Kaggle...")
        
        # Download the dataset
        kaggle.api.dataset_download_files('shivamb/netflix-shows', 
                                        path='.', 
                                        unzip=True)
        
        print("Dataset downloaded successfully!")
        return True
        
    except Exception as e:
        print(f"Error downloading from Kaggle: {e}")
        print("Creating sample dataset instead...")
        return False

def main():
    """Main function"""
    print("🎬 Netflix Dataset Setup")
    print("="*40)
    
    # Check if dataset already exists
    if os.path.exists('netflix_titles.csv'):
        print("Dataset already exists!")
        return
    
    # Try to download from Kaggle first
    if not download_kaggle_dataset():
        # If that fails, create sample data
        create_sample_dataset()
    
    # Verify the dataset
    if os.path.exists('netflix_titles.csv'):
        df = pd.read_csv('netflix_titles.csv')
        print(f"✅ Dataset ready! Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
    else:
        print("❌ Failed to create dataset")

if __name__ == "__main__":
    main()
