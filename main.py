# import library 
import requests

def get_all_characters():
    # api url
    url = "https://swapi.dev/api/people/"

    # list to store all character data
    characters = []
    
    # loop through all pages
    while url:
        response_api = requests.get(url)

        # check response status; if successful, api response content is returned
        if response_api.status_code == 200:
            data = response_api.json()
        else:
            print(f"Error: Unable to retrieve data (Status Code: {response_api.status_code})")

        # append characters from current page to the 'characters' list
        characters.extend(data['results'])
        
        # get the next page URL
        url = data.get('next')

    return characters


def filter_female_characters(characters):
    # filter the 'characters' list to return only 'female' characters
    female_characters = [character for character in characters if character['gender'] == 'female']
    return female_characters


def output_to_file(characters, filename):
    # open the file in write mode
    with open(filename, 'w') as file:
        # write header
        file.write("Row_Number, Name, ID, Eye_Color\n")

        # wite each row with female character details
        for i, character in enumerate(characters, start=1):
            # starts with row number and retrieves name, id (extracts from the url), and eye_color
            file.write(f"{i}, {character['name']}, {character['url'].split('/')[-2]}, {character['eye_color']}\n")


def main():
    # call functions
    characters = get_all_characters()
    female_characters = filter_female_characters(characters)

    # output to a text file
    output_to_file(female_characters, 'star_wars_female_characters.txt')


if __name__ == "__main__":
    main()