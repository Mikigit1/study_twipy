import config

import tweepy

def TwiSearch(key_word,directory_pass):
    #コンフィグファイルから各種キーを代入したものを引っ張る
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET

    auth = tweepy.OAuthHandler(CK,CS)
    auth.set_access_token(AT,ATS)

    api = tweepy.API(auth, wait_on_rate_limit =True)

    tweet_list =[]

    for tweet in tweepy.Cursor(api.search, key_word=key_word, count=100,tweet_mode='extended').items():
        tweet_list.append(tweet.full_text + '\n')
    
    fname = r"'"+ directory_pass + "'"
    fname = fname.replace("'","")

    #ファイル出力
    with open(fname, "w",encoding="utf-8") as f:
        f.writelines(tweet_list)


if __name__ == "__main__":
    print('取得したいキーワードを入力してください')
    key_word = input('>  ')

    print('出力先ディレクトリを入力してください。')
    directory_pass = input('>   ')

    TwiSearch(key_word,directory_pass)