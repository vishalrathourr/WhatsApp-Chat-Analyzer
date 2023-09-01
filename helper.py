from wordcloud import WordCloud
from collections import Counter
import pandas as pd
from urlextract import URLExtract
import emoji


extractor = URLExtract()

def fetch_stats(selected_user, df):
    
    if selected_user != 'All':
        df = df[df['user']== selected_user]
        
    # 1. Fetch number of messages
    num_messages = df.shape[0]
    
    # 2. Fetch total Number of words
    words = []
    for message in df['message']:
        words.extend(message.split())
        
    # 3. fetch number of media messages
    num_media = df[df['message']=='<Media omitted>\n'].shape[0]
    
    #4. Fetch the URLs
    links = []
    for message in df['message']:
        extracted_urls = extractor.find_urls(message)
    
    # Filter out non-link phrases
        filtered_urls = [url for url in extracted_urls if not any(word in url for word in ['M.Sc','M.sc','M. sc','M. Sc','m.tech','m.sc'])]
    
        links.extend(filtered_urls)
    
    
    return num_messages, len(words), num_media, len(links)


def most_busy_users(df):
    top5 = df['user'].value_counts().head()
    df = round((df['user'].value_counts()/df['user'].shape[0])*100,2).reset_index().rename(columns={'user':'name','count':'percent'})

    return top5, df

def create_wordcloud(selected_user,df):

    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()

    if selected_user != 'All':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)

    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    temp['message'] = temp['message'].apply(remove_stop_words)
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user,df):

    f = open('stop_hinglish.txt','r')
    stop_words = f.read()

    if selected_user != 'All':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df


def emoji_helper(selected_user, df):
    if selected_user != 'All':
        df = df[df['user'] == selected_user]
        
    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.distinct_emoji_list(message)])
        
    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    return emoji_df


def mothly_timeline(selected_user, df):
    if selected_user != 'All':
        df = df[df['user'] == selected_user]
        
    timeline=df.groupby(['year','month_num','month']).count()['message'].reset_index()
    
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i]+ "-" + str(timeline['year'][i]))
    timeline['time']=time
    
    return timeline

def daily_timeline(selected_user, df):
    if selected_user != 'All':
        df = df[df['user'] == selected_user]   
        
    daily_timeline=df.groupby(['only_date']).count()['message'].reset_index()  
    
    return daily_timeline 


def weekly_activity_map(selected_user, df):
    if selected_user != 'All':
        df = df[df['user'] == selected_user] 
        
    return df['day_name'].value_counts()  
    

def month_activity_map(selected_user, df):
    if selected_user != 'All':
        df = df[df['user'] == selected_user] 
        
    return df['month'].value_counts()  

def activity_heatmap(selected_user, df):
    if selected_user != 'All':
        df = df[df['user'] == selected_user] 
    
    user_heatmap = df.pivot_table(index='day_name',columns='period', values='message', aggfunc='count').fillna(0)    
    return user_heatmap
    
    
    
    
