
''' * Fazer Login
    * Coletar tweets com a palavra 'Cerveja' 
    * Agrupar as localidades dos tweets
    * Transformar e csv os dados coletados '''

import tweepy
import pandas as pd

consumer_key = ' '

consumer_secret = ' '

bearer_token = ' '

access_token = ' '

access_token_secret = ' ' 

# Autenticar com a API do Twitter
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

# Criar um objeto da API
api = tweepy.API(auth)

print("Status")
print(api.verify_credentials().screen_name)

# Palavra-chave para busca
keyword = "cerveja"

# Lista para armazenar os tweets
tweets_data = []

# Realizar a busca usando o Cursor
for tweet in tweepy.Cursor(api.search_tweets, q=keyword, tweet_mode='extended').items(10):
    tweet_data = {
        "Tweet": tweet.full_text,
        "Localização do Usuário": tweet.user.location if tweet.user.location else "Não disponível"
    }
    tweets_data.append(tweet_data)

# Criar um DataFrame usando o pandas
df = pd.DataFrame(tweets_data)

# Exportar o DataFrame para um arquivo Excel
df.to_excel("tweets_sobre_cerveja.xlsx", index=False)