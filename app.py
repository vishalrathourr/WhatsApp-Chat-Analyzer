import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

image = Image.open('pngtree-whatsapp-icon-png-image.png')

st.sidebar.image(image,output_format='PNG', width=100)
st.sidebar.title("WhatsApp Chat Analyzer :iphone:")

welcome = st.chat_message("assistant")
welcome.write("Hello! Welcome to WhatsApp Chat Analyzer")


uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data=bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)
    # welcome.write("Here are your results")
    # st.dataframe(df)
    
#----> fetch unique users
    
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Group")
    selected_user = st.sidebar.selectbox("Show Analysis For: ", user_list)
    
    if st.sidebar.button("Show Analysis"):
        
#----> Stats area
        num_messages ,words, num_media, num_links = helper.fetch_stats(selected_user, df)
        st.title('Top Statistics')
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.header("Total Messages")
            st.title(num_messages)
            
        with col2:
            st.header("Total Words")
            st.title(words)
            
        with col3:
            st.header("Media Shared")
            st.title(num_media)
            
        with col4:
            st.header("Links Shared")
            st.title(num_links)
            
        st.divider()
            
        
            
#----> Monthly timeline
        st.title('Monthly Timeline')
        timeline = helper.mothly_timeline(selected_user,df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'],timeline['message'], color='r', alpha=0.6)
        ax.scatter(timeline['time'],timeline['message'], color='red', marker='o')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
        
#----> Daily timeline
        st.title('Daily Timeline')
        daily = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily['only_date'],daily['message'], color='tab:blue')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
        
#----> Activity Map
        st.title('Activity Map')
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.header('Most Busy Day')
            busy_day = helper.weekly_activity_map(selected_user, df)
            fig, ax = plt.subplots() 
            ax.bar(busy_day.index,busy_day.values, color='b', alpha=0.6)
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
            
        with col2:
            st.header('Most Busy Month')
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots() 
            ax.bar(busy_month.index,busy_month.values, color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
            
            
        st.title('Weekly Activity Map')
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)
                    
#----> Most Busy Users in chat(Only for group chat level)

        if selected_user=='Group':
            st.title("Most Busy Users")
            top5 , top5perc = helper.most_busy_users(df)
            fig, ax = plt.subplots()
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Top 5 Busy Users")
                ax.bar(top5.index, top5.values, color='g')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
                
            with col2:
                st.subheader("Messages Percent")
                st.dataframe(top5perc)
            
#----> WordCloud

        st.title('Wordcloud')
        df_wc = helper.create_wordcloud(selected_user,df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        plt.axis('off')
        st.pyplot(fig,dpi=1000) 
        
#----> Most Common words
    
        st.title('Most Common Words')
        most_common_df = helper.most_common_words(selected_user,df)
        most_common_df=most_common_df[::-1]
        fig, ax = plt.subplots()
        ax.barh(most_common_df[0],most_common_df[1], color='r', alpha=0.6)
        st.pyplot(fig)
        
#----> Emoji analysis
        emoji_df = helper.emoji_helper(selected_user,df)
        st.title("Emoji Analysis")
        
        st.dataframe(emoji_df,width=100, height=500,use_container_width=True)
            

    
