import requests
import json

def get_random_joke():
    """
    Fetch a random joke from the JokeAPI external API.
    Returns a formatted joke string.
    """
    try:
        # Using JokeAPI (free, no authentication required)
        url = "https://v2.jokeapi.dev/joke/Any"
        
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad status codes
        
        joke_data = response.json()
        
        # JokeAPI returns two types: "single" and "twopart"
        if joke_data["type"] == "single":
            return joke_data["joke"]
        else:
            # Two-part joke (setup and delivery)
            setup = joke_data["setup"]
            delivery = joke_data["delivery"]
            return f"{setup}\n\n{delivery}"
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching joke: {e}"
    except (KeyError, json.JSONDecodeError) as e:
        return f"Error parsing joke data: {e}"

def get_joke_by_category(category="Any"):
    """
    Fetch a random joke from a specific category.
    Categories: General, Knock-Knock, Programming, Misc, Dark, Pun, Spooky, Christmas
    
    Args:
        category (str): The joke category
    """
    try:
        url = f"https://v2.jokeapi.dev/joke/{category}"
        
        response = requests.get(url)
        response.raise_for_status()
        
        joke_data = response.json()
        
        if joke_data["type"] == "single":
            return joke_data["joke"]
        else:
            setup = joke_data["setup"]
            delivery = joke_data["delivery"]
            return f"{setup}\n\n{delivery}"
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching joke: {e}"
    except (KeyError, json.JSONDecodeError) as e:
        return f"Error parsing joke data: {e}"

def get_multiple_jokes(count=5, category="Any"):
    """
    Fetch multiple random jokes.
    
    Args:
        count (int): Number of jokes to fetch
        category (str): The joke category
    """
    jokes = []
    for i in range(count):
        try:
            url = f"https://v2.jokeapi.dev/joke/{category}"
            response = requests.get(url)
            response.raise_for_status()
            
            joke_data = response.json()
            
            if joke_data["type"] == "single":
                jokes.append(joke_data["joke"])
            else:
                joke = f"{joke_data['setup']}\n{joke_data['delivery']}"
                jokes.append(joke)
        
        except Exception as e:
            jokes.append(f"Error fetching joke {i+1}: {e}")
    
    return jokes

if __name__ == "__main__":
    print("=" * 50)
    print("🎭 RANDOM JOKE GENERATOR 🎭")
    print("=" * 50)
    
    # Get a single random joke
    print("\n📌 Random Joke:")
    print("-" * 50)
    print(get_random_joke())
    
    # Get a programming joke
    print("\n\n💻 Programming Joke:")
    print("-" * 50)
    print(get_joke_by_category("Programming"))
    
    # Get multiple jokes
    print("\n\n🎪 5 Random Jokes:")
    print("-" * 50)
    jokes = get_multiple_jokes(5)
    for idx, joke in enumerate(jokes, 1):
        print(f"\n{idx}. {joke}")
    
    print("\n" + "=" * 50)
