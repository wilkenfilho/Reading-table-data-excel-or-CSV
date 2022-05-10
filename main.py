                                        #NETLYIC script voltado para este site #NETLYIC
import pandas as pd
tabela = pd.read_excel("/content/Bolsonaro.xlsx")
                                        #informando qual planilha estou trabalhando

                                            
informacoes = tabela[["title", "retweet_count", "favorite_count", "tweet_type", "user_followers_count", "user_created_at"]].groupby(["title", "retweet_count", "favorite_count", "tweet_type", "user_followers_count", "user_created_at"]).sum()
                                        #as colunas que eu quero trabalhar no arquivo xlsx.
pd.set_option('display.min_rows', 2500) # <-add this!
pd.set_option('display.max_rows', None)
pd.options.display.max_columns = 999

#com esse comando, eu consigo aumentar a quantidade de colunas exibidas.
freq = tabela[['title', 'tweet_type']].value_counts()
                                        #utilizando essa função .value_counts(), eu consigo descobrir a quantidade de itens dentro de uma célula.
display(informacoes)                                      

tabela.loc[tabela["title"].str.contains("voto", "votar")].to_excel("votar.xlsx")
tabela.loc[tabela["title"].str.contains("votei", "elegi")].to_excel("eleger.xlsx")
tabela.loc[tabela["title"].str.contains("eleger", "eleição")].to_excel("eleicao.xlsx")
                                        #para verificar se encontrou os dados corretos, retire a síntaxe.to_excel("outpu.xlsx").

analise = tabela[['title', 'retweet_count', 'tweet_type', 'favorite_count']]

analise.to_excel("title_retweet_count_tweet_type_favorite_count.xlsx")

                                        #para fazer análises de estatísticas
                                        
analise = tabela[['title', 'retweet_count', 'tweet_type', 'favorite_count']].groupby(by=['title', 'retweet_count', 'tweet_type', 'favorite_count']).apply(list)

analise.to_excel("title_retweet_count_tweet_type_favorite_count.xlsx")

                                        #para agrupar informações
freq.to_excel("output.xlsx")
                                        #para exportar a lista freq
