## DFSportsLineup

### Introduction

Calculates most frequent players from winning lineups on DraftKings.

### Usage

1. Download .csv lineups from DraftKings event.

2. Store .csv files into a folder.

3. run ```python frequency.py <path-to-csv-files> <top-n-lineups>```.

### Example

* .csv files are contained in the games folder

* looking only for the top 10 lineups from DraftKings event

* run ```python frequency.py ./games 10```

* sample output:
```
{
	'Caris LeVert': {'frequency': 14, 'drafted': '16.95%', 'average_points': 54.5}, 
	'Julius Randle': {'frequency': 10, 'drafted': '8.31%', 'average_points': 34.94}, 
	'Tobias Harris': {'frequency': 10, 'drafted': '4.94%', 'average_points': 43.75}, 
	'Aron Baynes': {'frequency': 10, 'drafted': '0.06%', 'average_points': 34.75}, 
	'Lonzo Ball': {'frequency': 9, 'drafted': '4.37%', 'average_points': 49.0}, 
	'Devin Booker': {'frequency': 9, 'drafted': '10.67%', 'average_points': 47.88}, 
	'Al Horford': {'frequency': 9, 'drafted': '4.04%', 'average_points': 37.0}, 
	'Cory Joseph': {'frequency': 9, 'drafted': '0.04%', 'average_points': 29.0},
	...
}
```