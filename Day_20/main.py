import requests

# Day 20
# 1. the provided url gives some error

# 2. Work with the Cat API

cat_api = 'https://api.thecatapi.com/v1/breeds'

cache = {}

def get_cat_breeds():
    # Check if the result is already cached
    if 'cat_breeds' in cache:
        return cache['cat_breeds']
    try:
        response = requests.get(cat_api)
        response.raise_for_status()  # Raise an error for bad responses
        breeds = response.json()
        # Cache the result
        cache['cat_breeds'] = breeds
        return breeds
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []
    
# i. get the min, max, mean, median, standard deviation of cats' weight in metric units
def get_weight_stats(breeds):
    weights = []
    for breed in breeds:
        weight = breed.get('weight', {})
        if 'metric' in weight:
            try:
                # Convert both min and max weights to float and add to the list
                min_max = weight['metric'].split(' - ')
                if len(min_max) == 2:
                    weights.append(float(min_max[0]))
                    weights.append(float(min_max[1]))
            except ValueError:
                continue  # Skip if conversion fails

    if not weights:
        return None

    min_weight = min(weights)
    max_weight = max(weights)
    mean_weight = sum(weights) / len(weights)
    median_weight = sorted(weights)[len(weights) // 2]
    
    # Calculate standard deviation
    variance = sum((x - mean_weight) ** 2 for x in weights) / len(weights)
    std_dev = variance ** 0.5
    
    return {
        'min': min_weight,
        'max': max_weight,
        'mean': mean_weight,
        'median': median_weight,
        'std_dev': std_dev
    }


# ii. get the min, max, mean, median, standard deviation of cats' lifespan in years
def get_lifespan_stats(breeds):
    lifespans = []
    for breed in breeds:
        lifespan = breed.get('life_span', '')
        if lifespan:
            try:
                # Convert both min and max weights to float and add to the list
                min_max = lifespan.split(' - ')
                lifespans.append(float(min_max[0]))
                lifespans.append(float(min_max[1]))
            except ValueError:
                continue  # Skip if conversion fails

    if not lifespans:
        return None

    min_lifespan = min(lifespans)
    max_lifespan = max(lifespans)
    mean_lifespan = sum(lifespans) / len(lifespans)
    median_lifespan = sorted(lifespans)[len(lifespans) // 2]
    
    # Calculate standard deviation
    variance = sum((x - mean_lifespan) ** 2 for x in lifespans) / len(lifespans)
    std_dev = variance ** 0.5
    
    return {
        'min': min_lifespan,
        'max': max_lifespan,
        'mean': mean_lifespan,
        'median': median_lifespan,
        'std_dev': std_dev
    }


# iii. Create a frequency table of country and breed of cats
def get_country_breed_frequency(breeds):
    country_breed_count = {}
    
    for breed in breeds:
        country = breed.get('origin', 'Unknown')
        breed_name = breed.get('name', 'Unknown')
        
        if country not in country_breed_count:
            country_breed_count[country] = {}
        
        if breed_name not in country_breed_count[country]:
            country_breed_count[country][breed_name] = 0
        
        country_breed_count[country][breed_name] += 1
    
    return country_breed_count


def display_weight_stats(breeds):
    weight_stats = get_weight_stats(breeds)
    if not weight_stats:
        print("No valid weight data found.")
        return
    print("Weight Statistics (in metric):")
    print(f"Min: {weight_stats['min']:.2f}")
    print(f"Max: {weight_stats['max']:.2f}")
    print(f"Mean: {weight_stats['mean']:.2f}")
    print(f"Median: {weight_stats['median']:.2f}")
    print(f"Standard Deviation: {weight_stats['std_dev']:.2f}")

def display_lifespan_stats(breeds):
    lifespan_stats = get_lifespan_stats(breeds)
    if not lifespan_stats:
        print("No valid lifespan data found.")
        return
    print("\nLifespan Statistics (in years):")
    print(f"Min: {lifespan_stats['min']:.2f}")
    print(f"Max: {lifespan_stats['max']:.2f}")
    print(f"Mean: {lifespan_stats['mean']:.2f}")
    print(f"Median: {lifespan_stats['median']:.2f}")
    print(f"Standard Deviation: {lifespan_stats['std_dev']:.2f}")

def display_country_breed_frequency(breeds):
    country_breed_freq = get_country_breed_frequency(breeds)
    if not country_breed_freq:
        print("No valid country and breed data found.")
        return
    print("\nCountry and Breed Frequency:")
    for country, breeds in country_breed_freq.items():
        print(f"{country}:")
        for breed, count in breeds.items():
            print(f"  {breed}: {count}")

if __name__ == "__main__":
    breeds = get_cat_breeds()
    if breeds:
        display_weight_stats(breeds)
        display_lifespan_stats(breeds)
        display_country_breed_frequency(breeds)
    else:
        print("No cat breeds data available.")