import streamlit as st
import json
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import instaloader
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup
import time
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager



#########################################################################################################


# Set Streamlit page layout
st.set_page_config(page_title="Brandfluence",layout="wide")

# Initialize session state for authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False  # User is not logged in initially

# Function to handle login
def login(user, password):
    L = instaloader.Instaloader()
    try:
        # Log in to Instagram
        L.login(user, password)
        st.success("✅ Login Successful!")
        st.session_state.authenticated = True  # Set authentication state
        st.rerun()  # Refresh the page to load dashboard
    except instaloader.exceptions.BadCredentialsException:
        st.warning("❌ Login Failed: Invalid username or password!")
    except Exception as e:
        st.warning(f"⚠️ Login Failed: {e}")

# Show login page if not authenticated
if not st.session_state.authenticated:
    c1, c2, c3 = st.columns([1, 3, 1])
    with c1:
        st.image("b1.png")
    with c2:
        st.markdown(
            """
            <style>
                .pink-title {
                    font-size: 64px;
                    font-weight: bold;
                    color: #FFB6C1;
                    font-family: 'Times New Roman', sans-serif;
                    text-align: center;
                    padding: 10px;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                }
            </style>
            <div class="pink-title">BRANDFLUENCE</div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <h2 style="color: #ffffff; font-size: 20px; font-family: 'Times New Roman', serif; text-align: center; margin-bottom: 30px;">
                Insightful Analytics for Smarter Brand Decisions <br> 
                Smart Insights. Stronger Influence.
            </h2>
            """,
            unsafe_allow_html=True
        )
    with c3:
        st.image("b3.png")

    st.subheader("----------------------------------------------------------------------------------------------------------------------")

    st.markdown(
        """
        <div style="text-align: center;">
            <h3 style="color: #FFB6C1; font-size: 24px; font-family: 'Times New Roman', serif;">
                Log In to Brandfluence – Power Your Influence!
            </h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    a, b, c = st.columns([1, 3, 1])
    with b:
        st.markdown(
            """
            <style>
                div[data-baseweb="input"] input {
                    width: 100%;
                    padding: 15px;
                    font-size: 18px;
                    font-weight: 500;
                    color: #ffffff;
                    background-color: transparent;
                    border: 2px solid #ffb6c1;
                    border-radius: 12px;
                    outline: none;
                    text-align: left;
                    transition: border-color 0.3s ease, box-shadow 0.3s ease;
                }
                div[data-baseweb="input"] input::placeholder {
                    color: #ffb6c1;
                    opacity: 0.8;
                }
                div[data-baseweb="input"] input:focus {
                    border-color: #ffb6c1;
                    box-shadow: 0px 0px 12px rgba(255, 105, 180, 0.5);
                    background-color: rgba(255, 255, 255, 0.05);
                }
            </style>
            """,
            unsafe_allow_html=True
        )

        username = st.text_input("Enter Username:", key="username")
        password = st.text_input("Enter Password:", type="password", key="password")

        if st.button("Login"):
            if username and password:
                login(username, password)
            else:
                st.warning("⚠️ Please enter both username and password.")

    st.subheader("----------------------------------------------------------------------------------------------------------------------")

    st.markdown(
        """
        <div style="text-align: center; padding: 20px;">
            <h2 style="color: #FFB6C1; font-size: 28px; font-family: 'Times New Roman', serif;">
                Unlock the Power of Data-Driven Branding
            </h2>
            <p style="color: #ffffff; font-size: 18px; line-height: 1.8;">
                In today’s competitive digital landscape, building a strong and influential brand presence on social media is more important than ever.
                <b>Brandfluence</b> is your all-in-one platform for gaining deep insights into your brand’s performance on <b>Instagram</b> — 
                helping you make smarter decisions, create engaging content, and build a loyal audience.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    co1,co2,co3=st.columns([1,4,1])
    with co2:
        st.image("b1.jpg")
    st.markdown(
        """
        <div style="text-align: center; padding: 20px;">
            <h3 style="color: #FFB6C1; font-size: 24px; font-family: 'Times New Roman', serif;">
                Why Brandfluence?
            </h3>
            <ul style="color: #ffffff; font-size: 18px; line-height: 1.8; text-align: left; display: inline-block;">
                <li><b>Track Performance:</b> Gain a comprehensive view of your brand’s reach, engagement, and audience behavior.</li>
                <li><b>Identify Trends:</b> Discover what content works best and why — from hashtags to post timing.</li>
                <li><b>Competitor Benchmarking:</b> See how your brand stacks up against competitors and uncover opportunities to outperform them.</li>
                <li><b>Audience Understanding:</b> Get to know your followers — their interests, demographics, and engagement patterns.</li>
                <li><b>Influencer Partnerships:</b> Find and collaborate with influencers who align with your brand’s values and goals.</li>
            </ul>
            <h3 style="color: #FFB6C1; font-size: 24px; font-family: 'Times New Roman', serif;margin-top: 30px;"> Transform Data into Actionable Insights</h3>
                <p style="color: #ffffff; font-size: 18px; line-height: 1.8;">
                    Brandfluence doesn’t just give you numbers — it helps you understand the story behind them. 
                    Our advanced AI algorithms analyze your brand’s data to provide actionable recommendations, helping you adjust your strategy for maximum impact.
                </p>
                <h3 style="color: #FFB6C1; font-size: 24px; font-family: 'Times New Roman', serif;margin-top: 30px;"> Empower Your Brand's Journey</h3>
                <p style="color: #ffffff; font-size: 18px; line-height: 1.8;">
                    Success on social media is about more than just likes and follows — it’s about building meaningful connections and driving real results. 
                    Whether you’re a startup looking to grow or an established brand aiming to sharpen your strategy, 
                    <b>Brandfluence</b> is your key to mastering the art of influence.
                </p>
        </div>
        """,
        unsafe_allow_html=True
    )


#############################################################################################################


# Show dashboard if authenticated
if st.session_state.authenticated:
    

    
    st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            border: 3px solid pink !important; /* Adjust width and color here */
            border-radius: 10px; /* Optional: for rounded corners */
            padding: 10px;
            min-width: 300px !important;
            max-width: 300px !important;
        }
    </style>
    """,
    unsafe_allow_html=True
    )



    # Sidebar
    with st.sidebar:
        st.sidebar.title("BRANDFLUENCE")
        option=option_menu("Menu",options=["Home","Analyse Brands","Trending Hashtags","Top Brands","Optimal Posting Time","AI Chatfluence","Logout"],icons=["house","","","","","","person"],styles={
                "container": {"padding": "5px", "background-color": "#0B0C10"},  
                "icon": {"color": "white", "font-size": "20px"}, 
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "5px",
                    "background-color": "#1a1a1a",   # Background color
                    "color": "#ffffff",               # Text color
                    "border-radius": "10px",
                    "transition": "background-color 0.3s ease"
                },
                "nav-link-selected": {
                    "border": "3px solid pink",  # Border color for selected option
                    "border-radius": "10px"
                },
            })


    #############################################################################################################

    if option=="Home":

        c1, c2 = st.columns([3, 1])
        with c1:
            st.markdown(
            """
            <style>
                .pink-title {
                    font-size: 48px; /* Large font size */
                    font-weight: bold;
                    color: #FFB6C1; /* Pink color */
                    font-family: 'Times New Roman', sans-serif; /* Attractive font */
                    text-align: center;
                    padding: 10px;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.3); /* Light shadow for 3D effect */
                }
            </style>
            <div class="pink-title">BRANDFLUENCE</div>
            """,
            unsafe_allow_html=True
            )
            st.markdown("""
            <style>
                .tagline {
                    font-size: 18px;
                    color: white;
                    font-family: 'Times New Roman', serif;
                    font-weight: bold;
                    text-align: center;
                    margin-top: -10px;
                    letter-spacing: 1px;
                    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.6); /* Shadow effect */
                }
            </style>
            <h2 style="color: #ffffff; font-size: 20px; font-family: 'Times New Roman', serif;text-align: center; margin-bottom: 30px;">
                    Insightful Analytics for Smarter Brand Decisions <br> 
                    Smart Insights. Stronger Influence.
                </h2>
                        
            """, unsafe_allow_html=True)


        with c2:
            file_path = r"E:/brandfluenceProject/Animation - 1741873969447.json"
            with open(file_path) as f:
                lottie_json = json.load(f)

            # Wrap Lottie animation in a container
            st.markdown('<div class="lottie-container">', unsafe_allow_html=True)
            st_lottie(lottie_json, speed=0.5)
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown(
            """
            <div style="text-align: center; padding: 20px;">
                <h2 style="color: #FFB6C1; font-size: 28px; font-family: 'Times New Roman', serif;margin-bottom: 30px;">Unlock the Power of Data-Driven Branding</h2>
                <p style="color: #ffffff; font-size: 18px; line-height: 1.8;">
                    In today’s competitive digital landscape, building a strong and influential brand presence on social media is more important than ever.
                    <b>Brandfluence</b> is your all-in-one platform for gaining deep insights into your brand’s performance on <b>Instagram</b> — 
                    helping you make smarter decisions, create engaging content, and build a loyal audience.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        a1,a2=st.columns(2)
        with a1:
            st.image("br1.gif")
            
        with a2:
            st.image("br3.gif")
        st.markdown(
            """
            <div style="text-align: center; padding: 20px;">
                <h3 style="color: #FFB6C1; font-size: 24px; font-family: 'Times New Roman', serif;margin-top: 30px;"> Why Brandfluence?</h3>
                <ul style="color: #ffffff; font-size: 18px; line-height: 1.8; text-align: left; display: inline-block;">
                    <li><b>Track Performance:</b> Gain a comprehensive view of your brand’s reach, engagement, and audience behavior.</li>
                    <li><b>Identify Trends:</b> Discover what content works best and why — from hashtags to post timing.</li>
                    <li><b>Competitor Benchmarking:</b> See how your brand stacks up against competitors and uncover opportunities to outperform them.</li>
                    <li><b>Audience Understanding:</b> Get to know your followers — their interests, demographics, and engagement patterns.</li>
                    <li><b>Influencer Partnerships:</b> Find and collaborate with influencers who align with your brand’s values and goals.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
        c1,c2,c3=st.columns([1,4,1])
        with c2:
            st.image("b1.jpg")
        st.markdown(
            """
            <div style="text-align: center; padding: 20px;">
                <h3 style="color: #FFB6C1; font-size: 24px; font-family: 'Times New Roman', serif;margin-top: 30px;"> Transform Data into Actionable Insights</h3>
                <p style="color: #ffffff; font-size: 18px; line-height: 1.8;">
                    Brandfluence doesn’t just give you numbers — it helps you understand the story behind them. 
                    Our advanced AI algorithms analyze your brand’s data to provide actionable recommendations, helping you adjust your strategy for maximum impact.
                </p>
                <h3 style="color: #FFB6C1; font-size: 24px; font-family: 'Times New Roman', serif;margin-top: 30px;"> Empower Your Brand's Journey</h3>
                <p style="color: #ffffff; font-size: 18px; line-height: 1.8;">
                    Success on social media is about more than just likes and follows — it’s about building meaningful connections and driving real results. 
                    Whether you’re a startup looking to grow or an established brand aiming to sharpen your strategy, 
                    <b>Brandfluence</b> is your key to mastering the art of influence.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


    #############################################################################################################




    elif option=="Analyse Brands":
        st.markdown(
            """
            <style>
                .pink-title {
                    font-size: 48px; /* Large font size */
                    font-weight: bold;
                    color: #FFB6C1; /* Pink color */
                    font-family: 'Times New Roman', sans-serif; /* Attractive font */
                    text-align: center;
                    padding: 10px;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.3); /* Light shadow for 3D effect */
                }
            </style>
            <div class="pink-title">Analyse Brand</div>
            """,
            unsafe_allow_html=True
            )

        

        ##########################################################################################################
    # Custom CSS for Streamlit text input

        a,b,c=st.columns([1,3,1])
        with b:
        # Custom CSS for Streamlit input box
            st.markdown("""
                <style>
                div[data-baseweb="input"] {
                    display: flex;
                    justify-content: center;
                    margin-top: 20px;
                }
                div[data-baseweb="input"] input {
                    width: 100%; /* Adjust width */
                    padding: 15px;
                    font-size: 18px;
                    font-weight: 500;
                    color: #ffffff;
                    background-color: transparent;
                    border: 2px solid #ffb6c1;
                    border-radius: 12px;
                    outline: none;
                    text-align: left;
                    transition: border-color 0.3s ease, box-shadow 0.3s ease;
                }
                div[data-baseweb="input"] input::placeholder {
                    color: #ffb6c1;
                    opacity: 0.8;
                }
                div[data-baseweb="input"] input:focus {
                    border-color: #ffb6c1;
                    box-shadow: 0px 0px 12px rgba(255, 105, 180, 0.5);
                    background-color: rgba(255, 255, 255, 0.05);
                }
                </style>
            """, unsafe_allow_html=True)

            # Use Streamlit's native text_input to store the value in session state
            search_query = st.text_input("Search Brand:",key="search_query")

            # Store in a variable
            brand_name = search_query
                    # st.write(f"✅ Brand stored in variable: `{brand_name}`")




        

    #################################################################################################################

        
        # Custom CSS for equal-sized buttons
        st.markdown(
            """
            <style>
            .stButton>button {
                background-color: transparent;
                color: white;
                border: 2px solid pink;
                padding: 12px;
                border-radius: 12px;
                font-size: 16px;
                font-weight: bold;
                transition: background-color 0.3s ease, transform 0.2s;
                width: 240px; /* Fixed width */
                height: 70px; /* Fixed height */
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;
                text-align: center;
                
            }

            .stButton>button:hover {
                background-color: rgba(255, 182, 193, 0.2); /* Light pink hover */
                color: white;
                border: 2px solid pink;
                padding: 12px;
                border-radius: 12px;
                transform: translateY(-2px);
            }
            
            .selected-button {
                background-color: transparent ;
                color: white ;
                border: 2px solid pink ;
                font-weight: bold ;
                transform: none ;
            }

            </style>
            """,
            unsafe_allow_html=True
        )

    
        # First row of buttons
        col1, col2, col3= st.columns(3)

        with col1:
            if st.button("KPI Overview", key="btn1"):
                st.session_state.selected_button = "KPI Overview"

        with col2:
            if st.button("Engagement Trends & Comparisions", key="btn2"):
                st.session_state.selected_button = "Engagement Trends & Comparisions"

        with col3:
            if st.button("Top Performing Posts", key="btn3"):
                st.session_state.selected_button = "Top Performing Posts"

        # Second row of buttons
        col4, col5, col6= st.columns(3)

        with col4:
            if st.button("Competitor Benchmarking", key="btn4"):
                st.session_state.selected_button = "Competitor Benchmarking"

        with col5:
            if st.button("Sentimental Analysis", key="btn5"):
                st.session_state.selected_button = "Sentimental Analysis"

        with col6:
            if st.button("Brand in the Wild", key="btn6"):
                st.session_state.selected_button = "Brand in the Wild"

        
        # Display dynamic content based on clicked button
        if "selected_button" in st.session_state and st.session_state.selected_button:
            st.markdown(f"<h2 style='color: white;'>{st.session_state.selected_button}</h2>", unsafe_allow_html=True)

            if st.session_state.selected_button == "KPI Overview":
                st.write("Here you can see the overall performance metrics of your Instagram account.")
                #st.write(brand_name)
                def get_instagram_stats(username):
                    loader = instaloader.Instaloader()

                    try:
                        # Load profile data
                        profile = instaloader.Profile.from_username(loader.context, username)
                        
                        followers = profile.followers
                        following = profile.followees
                        posts = profile.mediacount
                        
                        return {
                            "username": username,
                            "followers": followers,
                            "following": following,
                            "posts": posts
                        }
                    
                    except Exception as e:
                        st.error(f"Error: {e}")
                        return None

                if brand_name:
                    with st.spinner(f"Fetching data for **{brand_name}**..."):
                        data = get_instagram_stats(brand_name)
                        if data:
                            # st.success("✅ Data Fetched Successfully!")
                            
                            # Display Data using styled buttons
                            a1,a2,a3=st.columns([2,1,2])
                            with a2:
                                st.subheader(f" @{data['username']}")
                            st.subheader("------------------------------------------------------------------------------------")
                            col1, col2, col3 = st.columns(3)

                            with col1:
                                # followers
                                st.markdown(f"<div style='text-align: center; padding: 12px; background-color: #1e1e1e; border: 2px solid #ffb6c1; border-radius: 12px;'>👥 Followers<br><b>{data['followers']:,}</b></div>", unsafe_allow_html=True)
                            with col2:
                                # following
                                st.markdown(f"<div style='text-align: center; padding: 12px; background-color: #1e1e1e; border: 2px solid #ffb6c1; border-radius: 12px;'>👤 Following<br><b>{data['following']:,}</b></div>", unsafe_allow_html=True)
                            with col3:
                                # posts
                                st.markdown(f"<div style='text-align: center; padding: 12px; background-color: #1e1e1e; border: 2px solid #ffb6c1; border-radius: 12px;'>📸 Posts<br><b>{data['posts']:,}</b></div>", unsafe_allow_html=True)
                            st.subheader(" ")
                            st.title("Unlock Your Audience's Heart: The Power of Engagement")
                            st.write("10 Posts, Deeper Insights: Unpacking Recent Performance")
                            url = "https://instagram-scrapper-posts-reels-stories-downloader.p.rapidapi.com/user_id_by_username"
                            username = brand_name
                            querystring = {"username": username}
                            
                            headers = {
                                    "x-rapidapi-key": "",  # subscribe API and enter your key here
                                    "x-rapidapi-host": "instagram-scrapper-posts-reels-stories-downloader.p.rapidapi.com"
                            }

                            response = requests.get(url, headers=headers, params=querystring)
                            response_dict = response.json()

                            # Store in a dictionary
                            data = {
                                    'UserID': response_dict.get('UserID'),
                                    'UserName': response_dict.get('UserName')
                            }

                            # Display only UserID
                            id=data['UserID']
                            #print(id)


                            url1 = "https://instagram230.p.rapidapi.com/user/reels"

                            querystring1 = {"user_id": id}

                            headers1 = {
                                "x-rapidapi-key": "",  # subscribe API and enter your key here
                                "x-rapidapi-host": "instagram230.p.rapidapi.com"
                            }

                            response1 = requests.get(url1, headers=headers1, params=querystring1)
                            dd = response1.json()


                            reel_data = []

                            if 'items' in dd and len(dd['items']) > 0:
                                for i in range(min(10, len(dd['items']))):
                                    try:
                                        like_count = dd['items'][i]['media']['like_count']
                                        comment_count = dd['items'][i]['media']['comment_count']
                                        play_count = dd['items'][i]['media']['play_count']
                                        reel_data.append([like_count, comment_count, play_count])
                                    except KeyError:
                                        print(f"Reel {i+1}: Incomplete data, skipping")
                            else:
                                st.write("No reels data Available.")
                            df = pd.DataFrame(reel_data, columns=['Likes', 'Comments', 'Plays'])
                            #st.write(df)
                            l=df["Likes"].sum()
                            c=df["Comments"].sum()
                            p=df["Plays"].sum()
                            x,y,z=st.columns(3)
                            st.write(" ")
                            st.write(" ")
                            with x:
                                st.markdown(f"<div style='text-align: center; padding: 12px; background-color: #1e1e1e; border: 2px solid #ffb6c1; border-radius: 12px;'>❤️ Likes<br><b>{l}</b></div>", unsafe_allow_html=True)
                            with y:
                                st.markdown(f"<div style='text-align: center; padding: 12px; background-color: #1e1e1e; border: 2px solid #ffb6c1; border-radius: 12px;'>💬 Comments<br><b>{c}</b></div>", unsafe_allow_html=True)
                            with z:
                                st.markdown(f"<div style='text-align: center; padding: 12px; background-color: #1e1e1e; border: 2px solid #ffb6c1; border-radius: 12px;'>▶️ Plays<br><b>{p}</b></div>", unsafe_allow_html=True)
                            
                            df['Engagements'] = df['Likes'] + df['Comments']
                            # Calculate Engagement Rate (using Plays as Reach in this case)
                            df['Engagement Rate'] = (df['Engagements'] / df['Plays']) * 100
                            er=df["Engagement Rate"].sum()
                            st.write(" ")
                            st.write("Engagement Rate from Recent 10 reels:")
                            st.subheader("Engagement Rate:")
                            st.subheader(er)

                        else:
                            st.error("❌ Failed to Fetch Data!")
                else:
                    st.warning("⚠️ Please enter a valid username!")

    ##############################################################################################################


            elif st.session_state.selected_button == "Engagement Trends & Comparisions":
                st.write("Tracking Engagement Rate and Performing Comparisions.")
                if brand_name:
                    with st.spinner(f"Fetching data for **{brand_name}**..."):
                            a1,a2,a3=st.columns([2,1,2])
                            with a2:
                                st.subheader(f" @{brand_name}")
                            st.subheader("Unlock Your Audience's Heart: The Power of Engagement")
                            st.write("10 Posts, Deeper Insights: Unpacking Recent Performance")
                            url = "https://instagram-scrapper-posts-reels-stories-downloader.p.rapidapi.com/user_id_by_username"
                            username = brand_name
                            querystring = {"username": username}

                            headers = {
                                    "x-rapidapi-key": "",   # subscribe API and enter your key here
                                    "x-rapidapi-host": "instagram-scrapper-posts-reels-stories-downloader.p.rapidapi.com"
                            }

                            response = requests.get(url, headers=headers, params=querystring)
                            response_dict = response.json()

                            # Store in a dictionary
                            data = {
                                    'UserID': response_dict.get('UserID'),
                                    'UserName': response_dict.get('UserName')
                            }

                            # Display only UserID
                            id=data['UserID']
                            


                            url1 = "https://instagram230.p.rapidapi.com/user/reels"

                            querystring1 = {"user_id": id}

                            headers1 = {
                                "x-rapidapi-key": "",  # subscribe API and enter your key here
                                "x-rapidapi-host": "instagram230.p.rapidapi.com"
                            }

                            response1 = requests.get(url1, headers=headers1, params=querystring1)
                            dd = response1.json()


                            reel_data = []

                            if 'items' in dd and len(dd['items']) > 0:
                                for i in range(min(10, len(dd['items']))):
                                    try:
                                        like_count = dd['items'][i]['media']['like_count']
                                        comment_count = dd['items'][i]['media']['comment_count']
                                        play_count = dd['items'][i]['media']['play_count']
                                        reel_data.append([like_count, comment_count, play_count])
                                    except KeyError:
                                        print(f"Reel {i+1}: Incomplete data, skipping")
                            else:
                                st.write("No reels data Available.")
                            df = pd.DataFrame(reel_data, columns=['Likes', 'Comments', 'Plays'])
                            #st.write(df)
                            l=df["Likes"].sum()
                            c=df["Comments"].sum()
                            p=df["Plays"].sum()
                            x,y,z=st.columns(3)
                            st.write(" ")
                            st.write(" ")
                            with x:
                                st.markdown(f"<div style='text-align: center; padding: 12px; background-color: #1e1e1e; border: 2px solid #ffb6c1; border-radius: 12px;'>❤️ Likes<br><b>{l}</b></div>", unsafe_allow_html=True)
                            with y:
                                st.markdown(f"<div style='text-align: center; padding: 12px; background-color: #1e1e1e; border: 2px solid #ffb6c1; border-radius: 12px;'>💬 Comments<br><b>{c}</b></div>", unsafe_allow_html=True)
                            with z:
                                st.markdown(f"<div style='text-align: center; padding: 12px; background-color: #1e1e1e; border: 2px solid #ffb6c1; border-radius: 12px;'>▶️ Plays<br><b>{p}</b></div>", unsafe_allow_html=True)
                            
                            df['Engagements'] = df['Likes'] + df['Comments']
                            # Calculate Engagement Rate (using Plays as Reach in this case)
                            df['Engagement Rate'] = (df['Engagements'] / df['Plays']) * 100
                            st.write(" ")
                            st.subheader("How Engaging Are Your Posts? A Deep Dive into Engagement Rate")
                            st.write(" ")

                        # Set dark background
                            plt.style.use("dark_background")
                            sns.set_theme(style="darkgrid")

                            # Create figure
                            plt.figure(figsize=(10, 6))

                            # Bar plot with pink bars
                            ax = sns.barplot(x=df.index, y=df["Engagement Rate"], palette=["#404040"] * len(df), edgecolor="#ffb6c1", linewidth=3)

                            # Set black background for figure and axes
                            ax.set_facecolor("#121212")
                            plt.gcf().set_facecolor("#121212")

                            # Customize axes labels, title, and ticks
                            ax.set_xlabel("Recent Posts", fontsize=12, color="white")
                            ax.set_ylabel("Engagement Rate (%)", fontsize=12, color="white")
                            ax.set_title("Engagement Rate for Recent 10 Posts", fontsize=14, color="white")

                            # Change tick labels color
                            ax.tick_params(axis="both", colors="white")

                            # Customize grid lines
                            ax.grid(color="gray", linestyle="--", linewidth=0.5)

                            # Show values on bars in white
                            for p in ax.patches:
                                ax.annotate(f"{p.get_height():.2f}", 
                                            (p.get_x() + p.get_width() / 2, p.get_height()), 
                                            ha="center", va="bottom", fontsize=10, color="white")

                            # Save the plot
                            plt.savefig("a1.png", dpi=300, bbox_inches="tight")

                            st.image("a1.png")


                            ###############################
                            st.write("--------------------------------------------------------------------------")

                            st.write(" ")
                            st.subheader("Battle of Engagement: Likes❤️ vs. Comments💬 on Recent Posts")
                            st.write(" ")
                            # Set seaborn style
                            sns.set_theme(style="whitegrid", rc={"axes.facecolor": "none"})  # Transparent bg

                            # Create Figure
                            fig, ax = plt.subplots(figsize=(10, 6))

                            # Plot bars
                            bar_width = 0.4
                            x = range(len(df))

                            bars1 = ax.bar(
                                [i - bar_width/2 for i in x], df["Likes"], width=bar_width,
                                color="#ffb6c1", edgecolor="white", label="Likes"
                            )
                            bars2 = ax.bar(
                                [i + bar_width/2 for i in x], df["Comments"], width=bar_width,
                                color="#a9a9a9", edgecolor="white", label="Comments"
                            )

                            # Titles and labels
                            ax.set_title("Comparison of Likes vs. Comments Over Time", fontsize=14, color="white")
                            ax.set_xlabel("Recent Posts", fontsize=12, color="white")
                            ax.set_ylabel("Count", fontsize=12, color="white")

                            # X-axis ticks
                            ax.set_xticks(x)
                            ax.set_xticklabels([f"Post {i+1}" for i in x], rotation=45, color="white")

                            # Y-axis ticks
                            ax.tick_params(axis="y", colors="white")

                            # Grid styling
                            ax.yaxis.grid(True, linestyle="--", alpha=0.5, color="gray")

                            # Legend
                            ax.legend(facecolor="black", edgecolor="white", fontsize=12)

                            # Make background transparent
                            fig.patch.set_alpha(0)
                            ax.set_facecolor("none")

                            # Save the figure with transparent background
                            plt.savefig("a2.png", dpi=300, bbox_inches="tight", transparent=True)
                            st.image("a2.png")

                            # Close the plot to prevent display issues
                            plt.close()
                        

                else:
                    st.warning("⚠️ Please enter a valid username!")


##########################################################################################################


            elif st.session_state.selected_button == "Top Performing Posts":
                st.write("🔥 These are your top-performing posts based on likes.")
                if brand_name:
                    st.markdown("""
                        
                        Dive into the most engaging content from the profile.  
                        Below, we highlight the **Top 5 Posts** ranked by the highest number of likes — a strong indicator of audience interest, visual appeal, and impactful messaging.

                        Each post listed here links directly to Instagram, allowing you to explore the real content in its native format.

                        ---

                        """, unsafe_allow_html=True)
                    st.markdown("""
                        <style>
                            .styled-table {
                                width: 100%;
                                border-collapse: separate;
                                border-spacing: 0;
                                background: transparent;
                                font-size: 16px;
                                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                                border: 2px solid white;  /* ✅ Changed from #ffb6c1 to white */
                                
                                
                            }
                            .styled-table thead tr {
                                background-color: transparent;
                                color: #ffb6c1;
                                font-weight: 600;
                                font-size: 17px;
                            }
                            .styled-table th, .styled-table td {
                                padding: 14px 18px;
                                text-align: left;
                                border-bottom: 1px solid rgba(255, 182, 193, 0.2);
                            }
                            .styled-table tbody tr:hover {
                                background-color: rgba(255, 182, 193, 0.2);
                            }
                            .styled-table td:last-child {
                                color: white;
                                font-weight: bold;
                            }
                            .styled-table td a {
                                color: #1DA1F2;
                                text-decoration: none;
                            }
                            .styled-table td a:hover {
                                text-decoration: underline;
                            }
                        </style>
                    """, unsafe_allow_html=True)



                    
                    # API call
                    url = "https://instagram230.p.rapidapi.com/user/posts"
                    querystring = {"username": brand_name}
                    headers = {
                        "x-rapidapi-key": "",  # subscribe API and enter your key here
                        "x-rapidapi-host": "instagram230.p.rapidapi.com"
                    }
                    response = requests.get(url, headers=headers, params=querystring)
                    data = response.json()

                    # Extract posts
                    posts = data.get("items", [])
                    df = pd.DataFrame(posts)

                    # Build post URL and select top 5 by likes
                    df['url'] = "https://www.instagram.com/p/" + df['code']
                    df['url'] = df['url'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')
                    df_top5 = df[['url', 'like_count']].sort_values(by='like_count', ascending=False).head(5)
                    df_top5.columns = ['Instagram Post URL', 'Likes']

                    # Convert to HTML
                    html_table = df_top5.to_html(classes='styled-table', index=False, escape=False)

                    # Render the styled table
                    st.markdown(html_table, unsafe_allow_html=True)
                    st.markdown("""
                        ### 🔗 What Happens When You Click a Post?

                        When you click on any post URL:
                        - 🖼️ **Visual Preview**: Instantly view the image or video that caught followers' attention.
                        - 📝 **Caption Reveal**: Read the full caption to understand the tone, hashtags, and call-to-actions used.
                        - 💬 **Comment Insights**: Explore real user comments to see how people reacted — their thoughts, emotions, and feedback.

                        This helps in identifying not just *which* posts performed well, but *why* they did — offering valuable takeaways for crafting high-engagement content in the future.

                        ---

                        **Pro Tip** 💡  
                        Use this data to analyze trends. Are posts with bold visuals performing better? Is humor working? Do emotional captions lead to more interaction? Let the numbers and real audience feedback guide your content strategy.

                        """, unsafe_allow_html=True)

                else:
                     st.warning("⚠️ Please enter a valid username!")



##############################################################################################################


            elif st.session_state.selected_button == "Competitor Benchmarking":
                st.write("🔎 Compare your account's performance with competitors.")
                if brand_name:
                    a,b,c=st.columns([1,3,1])
                    with b:
                    # Custom CSS for Streamlit input box
                        st.markdown("""
                            <style>
                            div[data-baseweb="input"] {
                                display: flex;
                                justify-content: center;
                                margin-top: 20px;
                            }
                            div[data-baseweb="input"] input {
                                width: 100%; /* Adjust width */
                                padding: 15px;
                                font-size: 18px;
                                font-weight: 500;
                                color: #ffffff;
                                background-color: transparent;
                                border: 2px solid #ffb6c1;
                                border-radius: 12px;
                                outline: none;
                                text-align: left;
                                transition: border-color 0.3s ease, box-shadow 0.3s ease;
                            }
                            div[data-baseweb="input"] input::placeholder {
                                color: #ffb6c1;
                                opacity: 0.8;
                            }
                            div[data-baseweb="input"] input:focus {
                                border-color: #ffb6c1;
                                box-shadow: 0px 0px 12px rgba(255, 105, 180, 0.5);
                                background-color: rgba(255, 255, 255, 0.05);
                            }
                            </style>
                        """, unsafe_allow_html=True)

                        # Use Streamlit's native text_input to store the value in session state
                        cmptitr= st.text_input("Enter Brand:",key="cmptitr")

                        brand_cmp= cmptitr
                        

                        # Custom CSS button
                        st.markdown(
                            """
                            <style>
                            .stButton>button {
                                background-color: transparent;
                                color: white;
                                border: 2px solid pink;
                                padding: 12px;
                                border-radius: 12px;
                                font-size: 16px;
                                font-weight: bold;
                                transition: background-color 0.3s ease, transform 0.2s;
                                width: 240px; /* Fixed width */
                                height: 70px; /* Fixed height */
                                display: flex;
                                align-items: center;
                                justify-content: center;
                                cursor: pointer;
                                text-align: center;
                                
                            }

                            .stButton>button:hover {
                                background-color: rgba(255, 182, 193, 0.2); /* Light pink hover */
                                color: white;
                                border: 2px solid pink;
                                padding: 12px;
                                border-radius: 12px;
                                transform: translateY(-2px);
                            }
                            
                            .selected-button {
                                background-color: transparent ;
                                color: white ;
                                border: 2px solid pink ;
                                font-weight: bold ;
                                transform: none ;
                            }

                            </style>
                            """,
                            unsafe_allow_html=True
                        )

                    
                        # First row of buttons
                    col1, col2, col3= st.columns(3)

                    with col2:
                            if st.button("Compare Brands", key="btnt"):
                                st.session_state.selected_button = "Compare Brands"
                    if "selected_button" in st.session_state and st.session_state.selected_button:
                        if st.session_state.selected_button == "Compare Brands":
                            st.subheader("------------------------------------------------------------------------------------")
                            cc1,cc2=st.columns(2)
                            with cc1:
                                        def get_instagram_stats(username):
                                            loader = instaloader.Instaloader()

                                            try:
                                                # Load profile data
                                                profile = instaloader.Profile.from_username(loader.context, username)
                                                
                                                followers = profile.followers
                                                following = profile.followees
                                                posts = profile.mediacount
                                                
                                                return {
                                                    "username": username,
                                                    "followers": followers,
                                                    "following": following,
                                                    "posts": posts
                                                }
                                            
                                            except Exception as e:
                                                st.error(f"Error: {e}")
                                                return None

                                        if brand_name:
                                            with st.spinner(f"Fetching data for **{brand_name}**..."):
                                                data = get_instagram_stats(brand_name)
                                                if data:
                                                    # st.success("✅ Data Fetched Successfully!")
                                                    
                                                    # Display Data using styled buttons
                                                    
                                                    st.subheader(f" @{data['username']}")
                                                    st.subheader("----------------------------------------")
                                                    col1, col2, col3 = st.columns([1,2,1])

                                                    with col2:
                                                        # followers
                                                        st.markdown(f"<div style='text-align: center; padding: 8px; background-color: #1e1e1e; border: 2px solid #ffb6c1; border-radius: 12px;'>👥 Followers<br><b>{data['followers']:,}</b></div>", unsafe_allow_html=True)
                                                        st.write(" ")
                                                        # following
                                                        st.markdown(f"<div style='text-align: center; padding: 8px; background-color: #1e1e1e; border: 2px solid #ffb6c1; border-radius: 12px;'>👤 Following<br><b>{data['following']:,}</b></div>", unsafe_allow_html=True)
                                                        st.write(" ")
                                                        # posts
                                                        st.markdown(f"<div style='text-align: center; padding: 8px; background-color: #1e1e1e; border: 2px solid #ffb6c1; border-radius: 12px;'>📸 Posts<br><b>{data['posts']:,}</b></div>", unsafe_allow_html=True)
                                                    
                                            
                                        else:
                                            st.warning("⚠️ Please enter a valid username!")




                            with cc2:
                                        def get_instagram_stats(username):
                                            loader = instaloader.Instaloader()

                                            try:
                                                # Load profile data
                                                profile = instaloader.Profile.from_username(loader.context, username)
                                                
                                                followers = profile.followers
                                                following = profile.followees
                                                posts = profile.mediacount
                                                
                                                return {
                                                    "username": username,
                                                    "followers": followers,
                                                    "following": following,
                                                    "posts": posts
                                                }
                                            
                                            except Exception as e:
                                                st.error(f"Error: {e}")
                                                return None

                                        if brand_cmp:
                                            with st.spinner(f"Fetching data for **{brand_cmp}**..."):
                                                data = get_instagram_stats(brand_cmp)
                                                if data:
                                                    # st.success("✅ Data Fetched Successfully!")
                                                    
                                                    # Display Data using styled buttons
                                                    
                                                    st.subheader(f" @{data['username']}")
                                                    st.subheader("----------------------------------------")
                                                    col1, col2, col3 = st.columns([1,2,1])

                                                    with col2:
                                                        # followers
                                                        st.markdown(f"<div style='text-align: center; padding: 8px; background-color: #1e1e1e; border: 2px solid #ffb6c1; border-radius: 12px;'>👥 Followers<br><b>{data['followers']:,}</b></div>", unsafe_allow_html=True)
                                                        st.write(" ")
                                                        # following
                                                        st.markdown(f"<div style='text-align: center; padding: 8px; background-color: #1e1e1e; border: 2px solid #ffb6c1; border-radius: 12px;'>👤 Following<br><b>{data['following']:,}</b></div>", unsafe_allow_html=True)
                                                        # posts
                                                        st.write(" ")
                                                        st.markdown(f"<div style='text-align: center; padding: 8px; background-color: #1e1e1e; border: 2px solid #ffb6c1; border-radius: 12px;'>📸 Posts<br><b>{data['posts']:,}</b></div>", unsafe_allow_html=True)
                                            
                                        else:
                                            st.warning("⚠️ Please enter a valid username!")
                            st.subheader("------------------------------------------------------------------------------------")
                            st.subheader("Engagement Growth from Recent 10 reels:")
                            def ybrand():
                                url = "https://instagram-scrapper-posts-reels-stories-downloader.p.rapidapi.com/user_id_by_username"
                                username = brand_name
                                querystring = {"username": username}
                                                        
                                headers = {
                                        "x-rapidapi-key": "",  # subscribe API and enter your key here
                                        "x-rapidapi-host": "instagram-scrapper-posts-reels-stories-downloader.p.rapidapi.com"
                            }

                                response = requests.get(url, headers=headers, params=querystring)
                                response_dict = response.json()

                                                    # Store in a dictionary
                                data = {
                                                            'UserID': response_dict.get('UserID'),
                                                            'UserName': response_dict.get('UserName')
                                                    }

                                                    # Display only UserID
                                id=data['UserID']
                                
                                                    #print(id)


                                url1 = "https://instagram230.p.rapidapi.com/user/reels"

                                querystring1 = {"user_id": id}

                                headers1 = {
                                                        "x-rapidapi-key": "",  # subscribe API and enter your key here
                                                        "x-rapidapi-host": "instagram230.p.rapidapi.com"
                                                    }

                                response1 = requests.get(url1, headers=headers1, params=querystring1)
                                dd = response1.json()


                                reel_data = []

                                if 'items' in dd and len(dd['items']) > 0:
                                                        for i in range(min(10, len(dd['items']))):
                                                            try:
                                                                like_count = dd['items'][i]['media']['like_count']
                                                                comment_count = dd['items'][i]['media']['comment_count']
                                                                play_count = dd['items'][i]['media']['play_count']
                                                                reel_data.append([like_count, comment_count, play_count])
                                                            except KeyError:
                                                                print(f"Reel {i+1}: Incomplete data, skipping")
                                else:
                                    st.write("No reels data Available.")
                                df = pd.DataFrame(reel_data, columns=['Likes', 'Comments', 'Plays'])
                                df['Engagements'] = df['Likes'] + df['Comments']
                                # Calculate Engagement Rate (using Plays as Reach in this case)
                                df['bEngagement Rate'] = (df['Engagements'] / df['Plays']) * 100
                                return df
                            


                            def cbrand():
                                url = "https://instagram-scrapper-posts-reels-stories-downloader.p.rapidapi.com/user_id_by_username"
                                username = brand_cmp
                                querystring = {"username": username}
                                                    # 0983224848mshe5a4489a85075f8p102ac8jsn2fd51f27dfb5
                                headers = {
                                        "x-rapidapi-key": "",  # subscribe API and enter your key here
                                        "x-rapidapi-host": "instagram-scrapper-posts-reels-stories-downloader.p.rapidapi.com"
                            }

                                response = requests.get(url, headers=headers, params=querystring)
                                response_dict = response.json()

                                                    # Store in a dictionary
                                data = {
                                                            'UserID': response_dict.get('UserID'),
                                                            'UserName': response_dict.get('UserName')
                                                    }

                                                    # Display only UserID
                                id=data['UserID']
                                                    #print(id)


                                url1 = "https://instagram230.p.rapidapi.com/user/reels"

                                querystring1 = {"user_id": id}

                                headers1 = {
                                                        "x-rapidapi-key": "",  # subscribe API and enter your key here
                                                        "x-rapidapi-host": "instagram230.p.rapidapi.com"
                                                    }

                                response1 = requests.get(url1, headers=headers1, params=querystring1)
                                dd = response1.json()


                                reel_data = []

                                if 'items' in dd and len(dd['items']) > 0:
                                                        for i in range(min(10, len(dd['items']))):
                                                            try:
                                                                like_count = dd['items'][i]['media']['like_count']
                                                                comment_count = dd['items'][i]['media']['comment_count']
                                                                play_count = dd['items'][i]['media']['play_count']
                                                                reel_data.append([like_count, comment_count, play_count])
                                                            except KeyError:
                                                                print(f"Reel {i+1}: Incomplete data, skipping")
                                else:
                                    st.write("No reels data Available.")
                                df = pd.DataFrame(reel_data, columns=['Likes', 'Comments', 'Plays'])
                                df['Engagements'] = df['Likes'] + df['Comments']
                                # Calculate Engagement Rate (using Plays as Reach in this case)
                                df['cEngagement Rate'] = (df['Engagements'] / df['Plays']) * 100
                                return df
                            yb=ybrand()
                            cb=cbrand()
                            dfn=pd.DataFrame({"Bengage":yb["bEngagement Rate"],"Cengage":cb["cEngagement Rate"]})
                            



                            fig, ax = plt.subplots(figsize=(8, 5))

                            # Set background color to transparent
                            fig.patch.set_alpha(0)
                            ax.set_facecolor("none")

                            # Plot engagement rates with pink and light gray lines
                            ax.plot(dfn.index, dfn["Bengage"], marker="o", linestyle="-", color="#FFB6C1", linewidth=2, label=f"{brand_name} Engagement")  
                            ax.plot(dfn.index, dfn["Cengage"], marker="s", linestyle="--", color="#D3D3D3", linewidth=2, label=f"{brand_cmp} Engagement")  

                            # Customizing labels, titles, and legend with theme colors
                            ax.set_xlabel("Posts", fontsize=12, color="white")
                            ax.set_ylabel("Engagement Rate (%)", fontsize=12, color="white")
                            ax.set_title("Engagement Rate Trend", fontsize=14, color="#FFB6C1")  # Light Pink Title

                            # Set tick labels color
                            ax.tick_params(colors="white")

                            # Customizing the grid, legend, and removing background
                            ax.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.5)  # Gray dashed grid
                            ax.legend(facecolor="black", edgecolor="white", fontsize=10, labelcolor="white")  # Legend styling

                            # Display chart in Streamlit
                            st.pyplot(fig)

                            # Add some styling with Streamlit markdown
                            st.markdown(
                                """
                                <style>
                                body {
                                    background-color: transparent;
                                    color: white;
                                }
                                </style>
                                """,
                                unsafe_allow_html=True
                            )
                else:
                    st.warning("⚠️ Please enter a valid username!")

##############################################################################################################

            elif st.session_state.selected_button == "Sentimental Analysis":
                st.write("💬 Sentiment Analysis on Instagram Comments: Understanding Audience Reactions")
                if brand_name:
                    st.markdown("""
                        <div style='color: #ffb6c1; font-size: 16px;'>
                            Dive into the emotional tone of Instagram comments.<br>
                            Understand how audiences are reacting — positively, negatively, or neutrally — to brand content.
                        </div>
                        """, unsafe_allow_html=True)
                    nltk.download('vader_lexicon')
                    sia = SentimentIntensityAnalyzer()


                    # ------------------------------
                    # Classifier Function (5 categories)
                    # ------------------------------
                    def classify_sentiment_5(compound_score):
                        if compound_score > 0.6:
                            return "Very Positive"
                        elif 0.2 < compound_score <= 0.6:
                            return "Positive"
                        elif -0.2 <= compound_score <= 0.2:
                            return "Neutral"
                        elif -0.6 <= compound_score < -0.2:
                            return "Negative"
                        else:
                            return "Very Negative"

                    # ------------------------------
                    # API Calls to Fetch Instagram Post and Comments
                    # ------------------------------
                    st.write(" ")
                    with st.spinner("Fetching latest Instagram post and analyzing comments..."):
                        # Get latest post
                        post_url = "https://instagram230.p.rapidapi.com/user/posts"
                        querystring = {"username": brand_name}
                        headers = {
                            "x-rapidapi-key": "",  # subscribe API and enter your key here
                            "x-rapidapi-host": "instagram230.p.rapidapi.com"
                        }

                        response = requests.get(post_url, headers=headers, params=querystring)
                        dd1 = response.json()
                        latest_post = dd1.get('items', [])[0] if dd1.get('items') else {}
                        postid = latest_post.get('pk')

                        latest_code = latest_post.get('code')
                        posturl = f"https://www.instagram.com/p/{latest_code}" if latest_code else None



                        # Get comments
                        comment_url = "https://instagram-api-fast-reliable-data-scraper.p.rapidapi.com/comments"
                        querystring1 = {"id": postid}
                        headers1 = {
                            "x-rapidapi-key": "",  # subscribe API and enter your key here
                            "x-rapidapi-host": "instagram-api-fast-reliable-data-scraper.p.rapidapi.com"
                        }

                        response1 = requests.get(comment_url, headers=headers1, params=querystring1)
                        d = response1.json()
                        comments_list = d.get('comments', [])
                        texts = [comment.get('text', '') for comment in comments_list if isinstance(comment, dict)]
                        df = pd.DataFrame(texts, columns=['comment'])

                    # ------------------------------
                    # Sentiment Analysis
                    # ------------------------------
                    results = []
                    for comment in df['comment']:
                        scores = sia.polarity_scores(str(comment))
                        sentiment = classify_sentiment_5(scores['compound'])
                        results.append({
                            'comment': comment,
                            'compound': scores['compound'],
                            'sentiment': sentiment
                        })

                    df_sentiment = pd.DataFrame(results)

                    # ------------------------------
                    # Sentiment Percentages
                    # ------------------------------
                    total_comments = len(df_sentiment)
                    sentiment_counts = df_sentiment['sentiment'].value_counts()
                    all_sentiments = ['Very Positive', 'Positive', 'Neutral', 'Negative', 'Very Negative']
                    sentiment_percentages = {
                        s: round((sentiment_counts.get(s, 0) / total_comments) * 100, 2) for s in all_sentiments
                    }
                    sentiment_percent_df = pd.DataFrame(list(sentiment_percentages.items()), columns=['Sentiment', 'Percentage'])


                    # .........................
                    # brand name and url 

                    st.markdown(f"""
                    <hr style='border: 1px solid #ffb6c1; margin-top: 20px; margin-bottom: 10px;' />

                    <h3 style='color: #ffb6c1;'>🔍 Sentiment Analysis on <b>{brand_name}</b></h3>
                    <h4 style='color: #cccccc;'>📌 Post URL: <a href="{posturl}" target="_blank">{posturl}</a></h4>

                    <hr style='border: 1px solid #ffb6c1; margin-top: 10px; margin-bottom: 30px;' />
                    """, unsafe_allow_html=True)


                    # ------------------------------
                    # Pie Chart Visualization
                    # ------------------------------
                    fig = px.pie(
                        sentiment_percent_df,
                        values='Percentage',
                        names='Sentiment',
                        color='Sentiment',
                        color_discrete_map={
                            'Very Positive': '#8BC34A',
                            'Positive': '#CDDC39',
                            'Neutral': '#FFEB3B',
                            'Negative': '#FF9800',
                            'Very Negative': '#F44336',
                        },
                        title="Sentiment Distribution of Instagram Comments"
                    )
                    fig.update_traces(textinfo='label+percent', textfont_size=14)

                    # ------------------------------
                    # Show Pie Chart in Streamlit
                    # ------------------------------
                    st.subheader("📊 Sentiment Pie Chart")
                    st.plotly_chart(fig, use_container_width=True)

                    st.subheader("-------------------------------------------------------------------------------")
                    total_comments = len(df_sentiment)
                    sentiment_counts = df_sentiment['sentiment'].value_counts()
                    all_sentiments = ['Very Positive', 'Positive', 'Neutral', 'Negative', 'Very Negative']

                    # Real sentiment percentages
                    sentiment_percentages = {
                        s: round((sentiment_counts.get(s, 0) / total_comments) * 100, 2) for s in all_sentiments
                    }
                    sentiment_percent_df = pd.DataFrame(list(sentiment_percentages.items()), columns=['Sentiment', 'Percentage'])

                    # Display the 5 animated button counters
                    cols = st.columns(5)

                    # Inject CSS
                    btn_style = """
                        <style>
                            .custom-btn {
                                display: inline-block;
                                width: 120px;
                                height: 90px;
                                line-height: 80px;
                                text-align: center;
                                border-radius: 12px;
                                font-size: 36px;
                                font-weight: bold;
                                margin: 5px auto;
                                color: white;
                            }
                            .btn-very-green {
                                background-color: rgba(0, 255, 0, 0.2);
                                border: 4px solid #00ff00;
                            }
                            .btn-green {
                                background-color: rgba(144, 238, 144, 0.2);
                                border: 4px solid #28a745;
                            }
                            .btn-yellow {
                                background-color: rgba(255, 255, 153, 0.2);
                                border: 4px solid #ffc107;
                            }
                            .btn-orange {
                                background-color: rgba(255, 165, 0, 0.2);
                                border: 4px solid #ff7300;
                            }
                            .btn-red {
                                background-color: rgba(255, 99, 71, 0.2);
                                border: 4px solid #dc3545;
                            }
                        </style>
                    """
                    st.markdown(btn_style, unsafe_allow_html=True)

                    # Emoji and color map
                    emoji_color_map = {
                        'Very Positive': ('😊', '#00ff00', 'btn-very-green'),
                        'Positive': ('🙂', '#28a745', 'btn-green'),
                        'Neutral': ('😐', '#ffc107', 'btn-yellow'),
                        'Negative': ('🙁', '#ff7300', 'btn-orange'),
                        'Very Negative': ('😠', '#dc3545', 'btn-red')
                    }

                    # Loop through sentiments and display
                    for i, sentiment in enumerate(all_sentiments):
                        emoji, color, btn_class = emoji_color_map[sentiment]
                        target = sentiment_percentages.get(sentiment, 0)

                        with cols[i]:
                            counter_placeholder = st.empty()
                            for percent in range(0, int(target) + 1):
                                counter_placeholder.markdown(
                                    f"""
                                    <div style='text-align: center; color: {color}; padding: 6px;'>
                                        <button class="custom-btn {btn_class}">{emoji}</button>
                                        <div style='font-size: 18px; font-weight: bold; margin-top: 5px;'>{sentiment}</div>
                                        <div style='font-size: 24px;'>{percent}%</div>
                                    </div>
                                    """,
                                    unsafe_allow_html=True
                                )
                                time.sleep(0.01)
                    st.subheader("-------------------------------------------------------------------------------")
                    
                    st.markdown("""
                        <style>
                            .insight-heading {
                                font-size: 24px;
                                font-weight: 700;
                                color: #ffb6c1;
                                margin-bottom: 15px;
                            }
                            .insight-text {
                                font-size: 17px;
                                color: white;
                                line-height: 1.65;
                            }
                            .insight-bullets {
                                font-size: 16px;
                                margin-top: 15px;
                                margin-left: 20px;
                                color: white;
                            }
                            .insight-bullets li {
                                margin-bottom: 10px;
                            }
                        </style>

                        <div class='insight-heading'>💡 Insights Summary</div>

                        <div class='insight-text'>
                            This sentiment analysis provides a detailed overview of how audiences are emotionally reacting to the brand's latest content. 
                            By classifying real user comments into five emotional tones — <strong>Very Positive</strong>, <strong>Positive</strong>, <strong>Neutral</strong>, 
                            <strong>Negative</strong>, and <strong>Very Negative</strong> — we uncover the true perception of your brand.
                        </div>
                        <br>
                        <div class='insight-heading'>
                            <strong>📊 Key Takeaways:</strong>
                        </div>
                        <div class='insight-text'>
                            <ul class='insight-bullets'>
                                <li>Identify content strategies that emotionally resonate with your audience.</li>
                                <li>Spot sentiment drops early to respond or pivot campaigns effectively.</li>
                                <li>Maintain a consistent brand voice across all posts and platforms.</li>
                                <li>Engage better with your audience through emotionally aware communication.</li>
                            </ul>
                        </div>
                    """, unsafe_allow_html=True)



                else:
                     st.warning("⚠️ Please enter a valid username!")


#############################################################################################################

            elif st.session_state.selected_button == "Brand in the Wild":
                st.write("🏷️ Discover how your brand is organically appearing across user-generated content. These real-life captions show how your audience is engaging with and tagging your brand in their daily stories, photos, and moments.")
                if brand_name:
                    st.write(" ")
                    url = "https://instagram-scrapper-posts-reels-stories-downloader.p.rapidapi.com/user_id_by_username"
                    username = brand_name
                    querystring = {"username": username}
                                            
                    headers = {
                                "x-rapidapi-key": "",  # subscribe API and enter your key here
                                "x-rapidapi-host": "instagram-scrapper-posts-reels-stories-downloader.p.rapidapi.com"
                                }

                    response = requests.get(url, headers=headers, params=querystring)
                    response_dict = response.json()

                                                # Store in a dictionary
                    data = {
                            'UserID': response_dict.get('UserID'),
                            'UserName': response_dict.get('UserName')
                            }

                                                # Display only UserID
                    id=data['UserID']

                    # --- CONFIG ---

                    url = "https://instagram230.p.rapidapi.com/user/tags"
                    querystring = {"user_id": id}
                    headers = {
                        "x-rapidapi-key": "",  # subscribe API and enter your key here
                        "x-rapidapi-host": "instagram230.p.rapidapi.com"
                    }

                    # --- FETCH DATA ---
                    response = requests.get(url, headers=headers, params=querystring)
                    p = response.json()

                    captions = []

                    # --- EXTRACT CAPTIONS ---
                    edges = p['data']['user']['edge_user_to_photos_of_you']['edges']

                    for post in edges:
                        try:
                            caption_edges = post['node']['edge_media_to_caption']['edges']
                            if caption_edges:
                                caption_text = caption_edges[0]['node']['text']
                                # Filter by brand name (case-insensitive)
                                if brand_name.lower() in caption_text.lower():
                                    captions.append(caption_text)
                        except KeyError:
                            continue

                    # --- DISPLAY ---
                    df_captions = pd.DataFrame(captions, columns=['caption'])

                    st.markdown(f"""
                    <hr style='border: 1px solid #ffb6c1; margin-top: 20px; margin-bottom: 10px;' />

                    <h3 style='color: #ffb6c1;'>Captions Mentioning: {brand_name.capitalize()}</b></h3>
                    <hr style='border: 1px solid #ffb6c1; margin-top: 10px; margin-bottom: 30px;' />
                    """, unsafe_allow_html=True)

                    for i, row in df_captions.iterrows():
                        st.markdown(f"**{i+1}.** {row['caption']}")
                else:
                     st.warning("⚠️ Please enter a valid username!")

#########################################################################################################

    elif option=="Trending Hashtags":
        

        # Web Scraping
        url = "https://best-hashtags.com/hashtag/brand/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        popular_div = soup.find("div", {"id": "popular"})
        table = popular_div.find("table")

        # Extract headers
        headers = [th.text.strip() for th in table.find_all("th")]

        # Extract rows
        rows = []
        for tr in table.find_all("tr")[1:]:
            cells = tr.find_all("td")
            if len(cells) == 3:
                row = [cell.text.strip() for cell in cells]
                rows.append(row)

        # Create DataFrame
        df = pd.DataFrame(rows, columns=headers)

        # Streamlit App
        
        st.markdown(
            """
            <h1 style='color:#ffb6c1; font-family: "Times New Roman", serif; text-align: center;'>
                🔥 Trending Instagram Hashtags for Brands
            </h1>
            """,
            unsafe_allow_html=True
        )

        st.write(" ")
        st.markdown("""
        <div style='text-align: center; color: white; font-size:18px;'>
            Discover the most <span style='color:#ffb6c1;'>trending hashtags</span> associated with brands on Instagram. <br>
            </div>
        """, unsafe_allow_html=True)
        st.write(" ")
        ca,cb,cc=st.columns(3)
        with ca:
            st.image("s1.jpg")
        with cb:
            st.image("br5.gif")
        with cc:
            st.image("s2.jpg")
        

        st.markdown("""
        <div style='text-align: center; color: white; font-size:18px;'>
            Use these hashtags to maximize your reach, increase engagement, and stay aligned with current trends.
            Whether you're a fashion influencer, brand strategist, or content creator—these are the tags making noise right now!
        </div>
        """, unsafe_allow_html=True)


        # Custom CSS for table styling
        st.markdown("""
            <style>
            .custom-table {
                width: 100%;
                border-collapse: collapse;
                background-color: transparent;
            }
            .custom-table th, .custom-table td {
                border: 2px solid #ffb6c1;
                padding: 20px;
                color: white;
                text-align: center;
            }
            .custom-table thead {
                background-color: rgba(255, 182, 193, 0.2);
            }
            </style>
        """, unsafe_allow_html=True)

        # Convert DataFrame to HTML table with custom class
        table_html = df.to_html(classes="custom-table", index=False, escape=False)

        # Display the table
        st.markdown(table_html, unsafe_allow_html=True)

        st.write(" ")

        st.markdown("""
        <div style='text-align: center; color: white; font-size:16px;'>
            These hashtags are curated based on the volume of Instagram posts and popularity across categories like fashion, shopping, luxury, and entrepreneurship.
            Keep experimenting with these tags in your captions to find what resonates best with your audience.
        </div>

        <div style='text-align: center; color: #ffb6c1; font-size:16px; margin-top:10px;'>
            💡 Tip: Combine 3-5 of these trending hashtags with niche-specific tags for optimal discoverability!
        </div>
        """, unsafe_allow_html=True)



##########################################################################################################

    elif option=="Top Brands":
        # Set up Chrome WebDriver
        options = webdriver.ChromeOptions()
        #options.add_argument("--headless")  # Uncomment if you want headless mode
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # Open the StarNgage page
        driver.get("https://starngage.com/app/global/brand/ranking/all")

        # Accept cookie if it appears
        try:
            cookie_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "cc-btn"))
            )
            cookie_btn.click()
        except:
            pass  # continue if no cookie button

        # Scroll to load full content
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)  # Let content load

        # Wait until the table is ready
        wait = WebDriverWait(driver, 20)
        table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "table-responsive-sm")))

        # Extract table rows
        rows = table.find_elements(By.TAG_NAME, "tr")
        data = []

        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if cols:
                data.append([col.text.strip() for col in cols])

        driver.quit()

        # Define headers
        headers = ["#","blank", "Brand Full", "Country/Region", "Categories", "Followers", "Engagement Rate"]
        df = pd.DataFrame(data, columns=headers)

        df[['Brand Name', 'Username']] = df['Brand Full'].str.extract(r'^(.*?)\n@?(\S+)', expand=True)

        # Step 3: Drop 'Brand Full' and 'blank' columns
        df.drop(columns=['Brand Full', 'blank'], inplace=True)
        df['Username'] = '@' + df['Username']
        df = df[["#", "Brand Name", "Username", "Country/Region", "Categories", "Followers", "Engagement Rate"]]




        df = df[df["#"].astype(str).str.isdigit()]  # Keep only rows where # is a number
        df = df.dropna()                            # Drop any rows with NaN
        df = df.reset_index(drop=True)   


        # Filter required columns
        df = df[["#", "Brand Name", "Username", "Followers", "Engagement Rate"]]

        # Select first 10 rows
        df_display = df.head(20)

        st.markdown("<h1 style='color: #ffb6c1;'>🔥 Top Performing Instagram Brands</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='color: white;'>Updated Daily • Based on Highest Followers</h4>", unsafe_allow_html=True)


        st.markdown("""
                    <style>
                    .custom-table {
                        width: 100%;
                        border-collapse: collapse;
                        background-color: transparent;
                    }
                    .custom-table th, .custom-table td {
                        border: 2px solid #ffb6c1;
                        padding: 20px;
                        color: white;
                        text-align: center;
                    }
                    .custom-table thead {
                        background-color: rgba(255, 182, 193, 0.2);
                    }
                    </style>
                """, unsafe_allow_html=True)




        # Convert DataFrame to HTML table with custom classes
        html_table = df_display.to_html(classes="custom-table", index=False, escape=False)

        # Display HTML with custom styling
        st.markdown(f'<div class="custom-table-container">{html_table}</div>', unsafe_allow_html=True)


        st.markdown("---")
        st.markdown("""
        <div style="color: white; font-size: 16px;">
            <p>This table showcases the top 20 brands leading the way in Instagram performance, ranked by engagement rate and follower strength.</p>
            <br>
            <p>Use this overview to track influencer marketing trends, explore audience reach, and identify brands making the biggest impact on social media.</p>
        </div>
        """, unsafe_allow_html=True)

##########################################################################################################
    elif option=="Optimal Posting Time":
        st.markdown(
                    """
                    <style>
                        .title {
                            text-align: center;
                            font-size: 42px;
                            font-weight: bold;
                            color: #FFB6C1;
                            font-family: 'Times New Roman', serif;
                            margin-bottom: 20px;
                        }
                        .subheading {
                            font-size: 24px;
                            font-weight: bold;
                            color: white;
                            text-align: center;
                            margin-bottom: 10px;
                        }
                        .content {
                            font-size: 18px;
                            color: white;
                            text-align: justify;
                            line-height: 1.8;
                        }
                        .highlight {
                            color: #FFB6C1;
                            font-weight: bold;
                        }
                    </style>
                    """,
                    unsafe_allow_html=True
           )
        
        # Display heading
        st.markdown('<div class="title">Optimal Posting Time for Instagram</div>', unsafe_allow_html=True)


        st.markdown('<div class="content">Instagram’s algorithm prioritizes content that receives quick engagement. By posting when your audience is <span class="highlight">most active</span>, you increase the chances of getting <span class="highlight">more likes, comments, shares, and interactions</span>, boosting your reach.</div>', unsafe_allow_html=True)
        st.write(" ")
        st.markdown(
                """
                <h2 style="color: #FFB6C1; text-align: center;">
                    Best Times to Post on Instagram (Based on Engagement Trends)
                </h2>
                """,
                unsafe_allow_html=True
            )

                # Best time breakdown
        st.markdown(
                    """
                    **Weekday Posting Schedule:**
                    - **Monday:** 11 AM - 1 PM, 7 PM - 9 PM
                    - **Tuesday:** 9 AM - 11 AM, 6 PM - 8 PM
                    - **Wednesday:** 10 AM - 12 PM, 7 PM - 9 PM *(Highest engagement day)*
                    - **Thursday:** 11 AM - 1 PM, 6 PM - 8 PM
                    - **Friday:** 10 AM - 12 PM, 5 PM - 7 PM *(Good for weekend content buildup)*
                    
                    **Weekend Posting Schedule:**
                    - **Saturday:** 10 AM - 1 PM *(More active in late mornings)*
                    - **Sunday:** 11 AM - 2 PM *(Best for lifestyle, travel, and leisure content)*
                    """
                )

        st.image("op.png")

        st.markdown("""
                ## 📊 Best Time to Post Based on Content Type
                """)

        st.markdown(
                    """
                    - **📽️ Instagram Reels:** 12 PM - 3 PM *(Best engagement during lunch breaks)*
                    - **🖼️ Instagram Posts:** 10 AM - 12 PM, 7 PM - 9 PM *(Peak times before and after work)*
                    - **📖 Instagram Stories:** 8 AM - 10 AM, 5 PM - 7 PM *(Pre-engagement before posts)*
                    """
                )
        
        c1,c2=st.columns([3,2])
        with c1:
            st.subheader(" ")
            st.markdown("""
                ## Watch Video to know more...
                """)
            st.subheader(" ")
            st.markdown(
                """
                <div style="text-align: center; padding: 20px;">
                    <p style="color: #ffffff; font-size: 18px; line-height: 1.8;">
                        Want to master the perfect timing for your Instagram posts? Watch this video to uncover the best posting strategies for higher engagement!
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c2:
            st.video("vid1.mp4")
        st.markdown("""
                ## ⏳ Factors That Influence Optimal Posting Time
                """)

        st.markdown(
                    """
                    - **1️⃣ Audience Behavior & Activity Patterns**: Use **Instagram Insights** to check when followers are active.
                    - **2️⃣ Time Zones Matter**: If your audience is global, **schedule posts** according to their time zones.
                    - **3️⃣ Frequency & Consistency**: Posting too often can cause **audience fatigue**. Focus on **quality over quantity**.
                    - **4️⃣ Experiment & Track Performance**: Test different posting times and measure **engagement rates**.
                    """
                )


#########################################################################################################

    elif option=="AI Chatfluence":
        st.markdown(
            """
            <h1 style='color:#ffb6c1; font-family: "Times New Roman", serif; text-align: center;'>
                AI ChatBot for Instant Brand Insights
            </h1>
            """,
            unsafe_allow_html=True
        )

        st.write(" ")
        st.markdown("""
        <div style='text-align: center; color: white; font-size:18px;'>
            Your AI-powered guide for social media strategy and performance.
            </div>
        """, unsafe_allow_html=True)
        st.write(" ")
        a,b,c=st.columns([1,3,1])
        with b:
                # Custom CSS for Streamlit input box
            st.markdown("""
                        <style>
                        div[data-baseweb="input"] {
                            display: flex;
                            justify-content: center;
                            margin-top: 20px;
                        }
                        div[data-baseweb="input"] input {
                            width: 100%; /* Adjust width */
                            padding: 15px;
                            font-size: 18px;
                            font-weight: 500;
                            color: #ffffff;
                            background-color: transparent;
                            border: 2px solid #ffb6c1;
                            border-radius: 12px;
                            outline: none;
                            text-align: left;
                            transition: border-color 0.3s ease, box-shadow 0.3s ease;
                        }
                        div[data-baseweb="input"] input::placeholder {
                            color: #ffb6c1;
                            opacity: 0.8;
                        }
                        div[data-baseweb="input"] input:focus {
                            border-color: #ffb6c1;
                            box-shadow: 0px 0px 12px rgba(255, 105, 180, 0.5);
                            background-color: rgba(255, 255, 255, 0.05);
                        }
                        </style>
                    """, unsafe_allow_html=True)

                    # Use Streamlit's native text_input to store the value in session state
        aisrch= st.text_input("Search about Instagram:",key="aisrch")
        ais= aisrch

        st.markdown(
                """
                <style>
                .stButton>button {
                    background-color: transparent;
                    color: white;
                    border: 2px solid pink;
                    padding: 12px;
                    border-radius: 12px;
                    font-size: 16px;
                    font-weight: bold;
                    transition: background-color 0.3s ease, transform 0.2s;
                    width: 100px;
                    height: 50px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    cursor: pointer;
                    text-align: center;
                }

                .stButton>button:hover {
                    background-color: rgba(255, 182, 193, 0.2);
                    transform: translateY(-2px);
                }
                </style>
                """,
                unsafe_allow_html=True
            )

            # Single styled button
        if st.button("AI Chatbot", key="ai_button"):
                 
                url = "https://chatgpt-42.p.rapidapi.com/chat"

                payload = {
                    "messages": [
                        {
                            "role": "assistant",
                            "content": ais
                        }
                    ],
                    "model": "gpt-4o-mini"
                }
                headers = {
                    "x-rapidapi-key": "", # subscribe API and enter your key here
                    "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
                    "Content-Type": "application/json"
                }

                response = requests.post(url, json=payload, headers=headers)

                #print(response.json())

                data=response.json()
                content = data['choices'][0]['message']['content']

                # Print the extracted content
                st.write(content)


#########################################################################################################
    elif option=="Logout":
        
        st.markdown("""
            <style>
                .logout-heading {
                    font-size: 36px;
                    font-weight: bold;
                    color: #FFB6C1;
                    text-align: center;
                    margin-top: 30px;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                }
                .logout-button {
                    display: flex;
                    justify-content: center;
                    margin-top: 20px;
                }
                .stButton>button {
                    background-color: transparent;
                    color: white;
                    border: 2px solid pink;
                    padding: 12px;
                    border-radius: 10px;
                    font-size: 16px;
                    font-weight: bold;
                    transition: background-color 0.3s ease, transform 0.2s;
                    width: 200px;
                }
                .stButton>button:hover {
                    background-color: rgba(255, 182, 193, 0.2);
                    transform: translateY(-2px);
                }
                .bottom-content {
                    font-size: 18px;
                    color: white;
                    text-align: center;
                    margin-top: 50px;
                    padding: 20px;
                    line-height: 1.8;
                }
            </style>
        """, unsafe_allow_html=True)

        # Heading at the top
        st.markdown(
        """
        <div style="text-align: center;">
            <h3 style="color: #FFB6C1; font-size: 50px; font-family: 'Times New Roman', serif;">
                🔒 Logout from Brandfluence
            </h3>
        </div>
        """,
        unsafe_allow_html=True
    )
        st.write(" ")
        st.markdown(
        """
        <div style="text-align: center; padding: 20px;">
            <p style="color: #ffffff; font-size: 18px;">
                Thanks for using <b>Brandfluence</b>! Your journey towards data-driven branding continues. 🚀
            </p>
           </div>
        """,
        unsafe_allow_html=True
    )
        # Logout Button in the middle
        col1, col2, col3 = st.columns([2,1,2])
        with col2:
            if st.button("Logout"):
                st.session_state.authenticated = False  # Reset authentication
                st.rerun()

        
        st.markdown(
        """
        <div style="text-align: center; padding: 20px;">
            <p style="color: #ffffff; font-size: 18px;">
                Want to stay ahead of the competition? <br>
                <b>Log in again</b> to explore insightful analytics and optimize your social media impact.
            </p>
           </div>
        """,
        unsafe_allow_html=True
    )
        
