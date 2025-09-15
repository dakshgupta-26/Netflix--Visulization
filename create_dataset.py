"""
Create a comprehensive Netflix dataset for visualization
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def create_netflix_dataset():
    """Create a realistic Netflix dataset"""
    
    # Set random seed for reproducibility
    np.random.seed(42)
    random.seed(42)
    
    # Sample data
    titles = [
        "Stranger Things", "The Crown", "Money Heist", "Ozark", "The Witcher",
        "Bridgerton", "Squid Game", "Dark", "Narcos", "House of Cards",
        "Orange is the New Black", "13 Reasons Why", "The Queen's Gambit",
        "Tiger King", "Making a Murderer", "Chef's Table", "Abstract",
        "Our Planet", "Explained", "The Social Dilemma", "Extraction",
        "6 Underground", "Red Notice", "The Irishman", "Marriage Story",
        "Roma", "Bird Box", "Bright", "The Old Guard", "Enola Holmes",
        "To All the Boys I've Loved Before", "The Kissing Booth",
        "Tall Girl", "The Half of It", "The Platform", "Parasite",
        "The Trial of the Chicago 7", "Da 5 Bloods", "Mank", "Ma Rainey's Black Bottom"
    ]
    
    directors = [
        "Matt Duffer", "Peter Morgan", "Álex Pina", "Jason Bateman", "Lauren Schmidt",
        "Chris Van Dusen", "Hwang Dong-hyuk", "Baran bo Odar", "José Padilha", "Beau Willimon",
        "Jenji Kohan", "Brian Yorkey", "Scott Frank", "Eric Goode", "Laura Ricciardi",
        "David Gelb", "Scott Dadich", "Alastair Fothergill", "Ezra Klein", "Jeff Orlowski",
        "Sam Hargrave", "Michael Bay", "Rawson Marshall Thurber", "Martin Scorsese",
        "Noah Baumbach", "Alfonso Cuarón", "Susanne Bier", "David Ayer", "Gina Prince-Bythewood",
        "Harry Bradbeer", "Susan Johnson", "Vince Marcello", "Nzingha Stewart", "Alice Wu",
        "Galder Gaztelu-Urrutia", "Bong Joon-ho", "Aaron Sorkin", "Spike Lee", "David Fincher", "George C. Wolfe"
    ]
    
    countries = [
        "United States", "United Kingdom", "Spain", "South Korea", "Germany",
        "India", "Japan", "France", "Italy", "Brazil", "Mexico", "Canada",
        "Australia", "Netherlands", "Sweden", "Norway", "Denmark", "Poland",
        "Turkey", "Argentina", "Chile", "Colombia", "Peru", "Venezuela"
    ]
    
    ratings = ["TV-MA", "TV-14", "R", "PG-13", "TV-PG", "PG", "TV-Y7", "TV-Y", "G", "NC-17"]
    
    genres = [
        "Dramas", "International Movies", "Action & Adventure", "Comedies", "Thrillers",
        "Romantic Movies", "Documentaries", "Horror Movies", "Sci-Fi & Fantasy", "Kids & Family",
        "Anime Features", "Stand-Up Comedy", "Music & Musicals", "Sports Movies", "LGBTQ Movies",
        "Classic Movies", "Independent Movies", "Faith & Spirituality", "Military Movies", "Westerns"
    ]
    
    # Generate dataset
    data = []
    
    for i in range(1000):  # Create 1000 records
        show_id = f"s{i+1:04d}"
        
        # Type (70% movies, 30% TV shows)
        content_type = "Movie" if random.random() < 0.7 else "TV Show"
        
        title = random.choice(titles) + f" {random.randint(1, 5)}" if random.random() < 0.3 else random.choice(titles)
        
        director = random.choice(directors)
        
        # Cast (multiple actors)
        cast_list = [
            "Ryan Reynolds", "Dwayne Johnson", "Gal Gadot", "Chris Hemsworth", "Scarlett Johansson",
            "Robert Downey Jr.", "Chris Evans", "Mark Ruffalo", "Chris Pratt", "Tom Holland",
            "Zendaya", "Timothée Chalamet", "Anya Taylor-Joy", "Millie Bobby Brown", "Finn Wolfhard"
        ]
        cast = ", ".join(random.sample(cast_list, random.randint(2, 4)))
        
        country = random.choice(countries)
        
        # Date added (random date between 2015-2023)
        start_date = datetime(2015, 1, 1)
        end_date = datetime(2023, 12, 31)
        random_days = random.randint(0, (end_date - start_date).days)
        date_added = (start_date + timedelta(days=random_days)).strftime("%B %d, %Y")
        
        # Release year (between 1990-2023)
        release_year = random.randint(1990, 2023)
        
        rating = random.choice(ratings)
        
        # Duration based on type
        if content_type == "Movie":
            duration = f"{random.randint(80, 180)} min"
        else:
            duration = f"{random.randint(1, 8)} Season{'s' if random.randint(1, 8) > 1 else ''}"
        
        # Listed in (multiple genres)
        num_genres = random.randint(1, 3)
        listed_in = ", ".join(random.sample(genres, num_genres))
        
        # Description
        descriptions = [
            "A gripping story that will keep you on the edge of your seat.",
            "An emotional journey through love, loss, and redemption.",
            "A thrilling adventure that takes you to new worlds.",
            "A heartwarming tale of friendship and family.",
            "A dark and mysterious story with unexpected twists.",
            "A hilarious comedy that will make you laugh out loud.",
            "A thought-provoking documentary about real-life events.",
            "An action-packed thriller with stunning visuals.",
            "A romantic story that will touch your heart.",
            "A sci-fi epic that explores the future of humanity."
        ]
        description = random.choice(descriptions)
        
        data.append({
            'show_id': show_id,
            'type': content_type,
            'title': title,
            'director': director,
            'cast': cast,
            'country': country,
            'date_added': date_added,
            'release_year': release_year,
            'rating': rating,
            'duration': duration,
            'listed_in': listed_in,
            'description': description
        })
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Save to CSV
    df.to_csv('netflix_titles.csv', index=False)
    print(f"✅ Netflix dataset created successfully!")
    print(f"📊 Dataset shape: {df.shape}")
    print(f"📋 Columns: {list(df.columns)}")
    print(f"🎬 Movies: {len(df[df['type'] == 'Movie'])}")
    print(f"📺 TV Shows: {len(df[df['type'] == 'TV Show'])}")
    
    return df

if __name__ == "__main__":
    create_netflix_dataset()
