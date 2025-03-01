import streamlit as st
from streamlit_option_menu import option_menu

#import other apps here
import dataCollectionApp, analyzeData, donationApp, about, ask4Donation, classificationApp


# Authentication
if "username" not in st.session_state:
    st.session_state["username"] = ""
if "password" not in st.session_state:
    st.session_state["password"] = ""
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

#setting page config
st.set_page_config(page_title='Sustainability Donation and Distribution System for People with Disabilities')

if not st.session_state["authenticated"]:
    st.title('Sustainability Donation and Distribution System for People with Disabilities')
    st.title("Login panel")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    # Simulate authentication
    if login_button and username == "user" and password == "user":
        st.session_state["authenticated"] = True

if st.session_state["authenticated"]:
    # Linking pages
    class multiApp:
        def __init__(self):
            self.apps = []
    
        def add_app(self, title, function):
            self.apps.append({
                'title': title,
                'function': function
            })
            
        def run(self):  # Added 'self' as the first parameter
            with st.sidebar:
                app = option_menu(
                    #page tittles goes here
                    menu_title='Disability Donation and Distribution System',
                    
                    #setting options for navigation
                    options=['Home', 'Data Collection', 'Analyze Dataset', 'Distribution',
                             'Ask for Donation', 'About'],
                    
                    #setting icons for the navigation
                    icons=['house-fill', 'database', 'graph-up', 'gift', 'heart',
                           'person-circle', 'info-circle-fill'],
                    
                    menu_icon='chat-text-fill',
                    
                    default_index=1,
                    
                    #styling the menu with css               
                    styles={
                        'container': {'padding': '5!important',
                                      'background-color': ''},
                        
                        'icon': {'color': 'white', 'font-size': '23px'},
                        
                        'nav-link': {'font-size': '20px',
                                     'text-align': 'left',
                                     'color': 'white'},
                        
                        'nav-link-selected': {'background-color': '#02ab21'},
                    }
                )
            
            #setting logic here
            if app == 'Home':
                classificationApp.app()
            elif app == 'Data Collection':
                dataCollectionApp.main()
            
            elif app == 'Analyze Dataset':
                analyzeData.app()
                            
            elif app == 'Distribution':
                donationApp.main()
                
            elif app == 'Ask for Donation':
                ask4Donation.app()
                
            elif app == 'About':
                about.app()

    # Instantiate and run the multiApp
    if __name__ == "__main__":
        multi_app = multiApp()
        multi_app.run()
