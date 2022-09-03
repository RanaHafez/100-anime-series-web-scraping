from bs4 import BeautifulSoup
import requests
import pandas


URL_SOUP = "https://www.imdb.com/list/ls057577566/"
NAME_SELECTOR = "h3 a"
YEAR_SELECTOR = "h3 span.lister-item-year"
GENRE_SELECTOR = "p.text-muted span.genre"
RATING_SELECTOR = "span.ipl-rating-star__rating"
DESCRIPTION_SELECTOR = "div.list-description p"


response = requests.get(url=URL_SOUP)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())
divs = soup.select(selector="div .lister-item")
anime_dic = {'Name': [],
             'Year': [],
             'Genre': [],
             'Rating': [],
             'Description': []
             }

for anime_div in divs:
    anime_name = anime_div.select_one(NAME_SELECTOR).text
    anime_year = anime_div.select_one(YEAR_SELECTOR).text
    anime_genre = anime_div.select_one(GENRE_SELECTOR).text.strip()
    rating = float(anime_div.select_one(RATING_SELECTOR).text)
    description = anime_div.select_one(DESCRIPTION_SELECTOR).text

    anime_dic['Name'].append(anime_name)
    anime_dic['Year'].append(anime_year)
    anime_dic['Genre'].append(anime_genre)
    anime_dic['Rating'].append(rating)
    anime_dic['Description'].append(description)


print(anime_dic)

anime_df = pandas.DataFrame(anime_dic)
print(anime_df)
anime_df.to_csv("100_anime.csv")

print(f"The anime with the highest rating is ....... {anime_df.Rating.max()} and it is "
      f"\n{anime_df.loc[anime_df.Rating.idxmax()]}")

print("-----------------------------------------------------")
print(f"The anime with the lowest rating is ....... {anime_df.Rating.min()} "
      f"and it is \n{anime_df.loc[anime_df.Rating.idxmin()]}")

print("-----------------------------------------------------")
print(f"The average rating of the ratings ? {anime_df.Rating.mean()}")
