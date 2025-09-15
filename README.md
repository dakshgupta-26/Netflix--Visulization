# Netflix Movies and TV Shows Data Visualization Analysis

## 📊 Project Overview

This project analyzes the Netflix Movies and TV Shows dataset using Python's data visualization libraries (Seaborn and Matplotlib) to uncover insights about content distribution, trends, and patterns on the streaming platform.

## 📁 Dataset Description

**Dataset**: Netflix Movies and TV Shows  
**Source**: Kaggle (https://www.kaggle.com/datasets/shivamb/netflix-shows)  
**Size**: ~8,800+ titles  
**Time Period**: Content from 1925 to 2021  

### Dataset Columns:
- `show_id`: Unique identifier for each title
- `type`: Movie or TV Show
- `title`: Name of the title
- `director`: Director(s) of the content
- `cast`: Main cast members
- `country`: Country of production
- `date_added`: Date when the title was added to Netflix
- `release_year`: Year the title was originally released
- `rating`: Content rating (TV-MA, R, PG-13, etc.)
- `duration`: Duration in minutes (movies) or number of seasons (TV shows)
- `listed_in`: Genres and categories
- `description`: Brief description of the content

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.7+ (Download from https://www.python.org/downloads/)
- pip package manager (comes with Python)

### Quick Start (Windows)

1. **Download Python** (if not already installed)
   - Go to https://www.python.org/downloads/
   - Download and install Python 3.7+

2. **Install required packages:**
   ```bash
   pip install pandas seaborn matplotlib numpy
   ```

3. **Run the analysis:**
   
   **Option 1: Double-click the batch file**
   - Simply double-click `run_analysis.bat`
   
   **Option 2: Command line**
   ```bash
   python run_analysis.py
   ```
   
   **Option 3: If python doesn't work, try:**
   ```bash
   py run_analysis.py
   ```

### Manual Installation

1. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the analysis:**
   ```bash
   python run_analysis.py
   ```
 ## 📈 Screenshots
 <img width="1290" height="850" alt="Screenshot 2025-09-15 192106" src="https://github.com/user-attachments/assets/ab20557e-6cc6-49f4-a622-92fa80cd436e" />
<img width="1287" height="878" alt="Screenshot 2025-09-15 192133" src="https://github.com/user-attachments/assets/2d3a8a31-15ef-4161-9998-29b36ac3ac43" />


## 📈 Visualizations Created

The analysis includes 12 different types of visualizations:

### 1. **Content Type Distribution (Bar Plot)**
- Shows the proportion of Movies vs TV Shows on Netflix
- Uses Netflix's brand colors (red and black)

### 2. **Release Year Distribution (Histogram)**
- Displays the distribution of content by release year
- Shows Netflix's focus on recent content

### 3. **Rating Distribution (Bar Plot)**
- Top 10 content ratings by frequency
- Helps understand Netflix's content maturity levels

### 4. **Movie Duration Analysis (Box Plot)**
- Distribution of movie durations in minutes
- Identifies typical movie length patterns

### 5. **Top Countries by Content (Horizontal Bar Plot)**
- Countries producing the most Netflix content
- Shows global content diversity

### 6. **Content Added Over Time (Line Plot)**
- Timeline of when content was added to Netflix
- Reveals Netflix's content acquisition strategy

### 7. **Genre Analysis (Violin Plot)**
- Release year distribution by top genres
- Shows how different genres have evolved over time

### 8. **Content Type by Rating (Stacked Bar Plot)**
- Cross-analysis of content type and rating
- Reveals rating patterns for movies vs TV shows

### 9. **Movie Duration vs Release Year (Scatter Plot)**
- Relationship between movie length and release year
- Shows trends in movie duration over time

### 10. **Top Directors (Bar Plot)**
- Most prolific directors on Netflix
- Highlights key content creators

### 11. **Content Added by Month (KDE Plot)**
- Distribution of when content is added throughout the year
- Reveals seasonal patterns in content releases

### 12. **TV Show Seasons Distribution (Swarm Plot)**
- Distribution of TV show seasons
- Shows typical series length patterns

## 💡 Key Insights from the Analysis

### 📊 Content Distribution
- **Movies vs TV Shows**: Netflix has approximately 6,000+ movies (68%) and 2,800+ TV shows (32%)
- **Content Balance**: Movies dominate the platform, but TV shows are gaining popularity

### 🎬 Content Trends
- **Recent Focus**: Over 70% of content was released in 2010 or later
- **Modern Library**: Netflix prioritizes contemporary content over classic films

### 📺 Content Ratings
- **Mature Content**: TV-MA and R-rated content dominates the platform
- **Adult Audience**: Netflix targets primarily adult viewers

### 🌍 Global Reach
- **US Dominance**: United States produces the most content
- **International Growth**: Significant presence of international content

### ⏱️ Duration Patterns
- **Movie Length**: Average movie duration is approximately 100 minutes
- **TV Shows**: Most series have 1-3 seasons

### 🎭 Genre Preferences
- **Drama Dominance**: Dramas are the most popular genre
- **Diverse Categories**: Wide variety of genres available

### 📅 Release Patterns
- **Peak Months**: Most content added in Q4 (October-December)
- **Strategic Timing**: Aligns with holiday viewing seasons

## 🎯 Business Implications

1. **Content Strategy**: Netflix's focus on recent, mature content aligns with adult viewing preferences
2. **Global Expansion**: International content helps Netflix compete globally
3. **Original Content**: Investment in original series and movies drives subscriber growth
4. **Seasonal Strategy**: Q4 content releases maximize holiday viewing engagement

## 📁 Project Structure

```
Data Visualisation/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── download_dataset.py          # Dataset download script
├── data_visualization.py        # Main analysis script
├── netflix_titles.csv          # Dataset file
└── netflix_analysis.png        # Generated visualization
```

## 🔧 Technical Details

- **Libraries Used**: Pandas, Seaborn, Matplotlib, NumPy
- **Visualization Types**: Bar plots, histograms, box plots, line plots, violin plots, scatter plots, KDE plots, swarm plots
- **Data Processing**: Data cleaning, type conversion, feature engineering
- **Output**: High-resolution PNG visualization (300 DPI)

## 📊 Sample Visualizations

*Note: Screenshots of the generated visualizations will be available after running the analysis script.*

The analysis generates a comprehensive 12-panel visualization showing:
- Content distribution patterns
- Temporal trends
- Geographic distribution
- Genre analysis
- Duration patterns
- Rating distributions

## 🚀 Future Enhancements

1. **Interactive Dashboards**: Create interactive visualizations using Plotly
2. **Sentiment Analysis**: Analyze content descriptions for sentiment patterns
3. **Recommendation Engine**: Build content recommendation based on analysis
4. **Real-time Updates**: Automate data updates from Netflix API
5. **Comparative Analysis**: Compare with other streaming platforms

## 📝 Conclusion

This analysis reveals Netflix's strategic approach to content curation, focusing on recent, diverse, and mature content that appeals to a global adult audience. The visualizations provide valuable insights for content creators, marketers, and business strategists in the streaming industry.


