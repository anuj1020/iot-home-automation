import streamlit as st

from src.page import tabs as tb

# Set the page configuration
st.set_page_config(
    page_title="House Assistant",
    layout="wide",  # Use wide layout for better responsiveness
    initial_sidebar_state="collapsed",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main-title {
        font-size: 3em;
        color: #4CAF50;
        text-align: center;
        margin-top: 20px;
    }
    .section-title {
        font-size: 2em;
        color: #FF5722;
        margin-top: 20px;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 0.9em;
        color: #888;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 16px;
    }
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: royalblue;
        padding: 10px;
    }
    .navbar a {
        color: white;
        padding: 14px;
        text-decoration: none;
    }
    .navbar .user-info {
        position: relative;
        display: inline-block;
    }
    .navbar .user-info:hover .user-details {
        display: block;
    }
    .navbar .user-details {
        display: none;
        position: absolute;
        top: 30px;
        right: 0;
        background-color: white;
        border: 1px solid #ddd;
        padding: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        z-index: 1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state for user login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = True
    st.session_state.user_name = "Anuj"
    st.session_state.user_email = "test@mail.com"



# Define the pages dictionary
pages = {
    "Home": tb.show_home,
    "Login": tb.show_controls,
    "Signup": tb.show_settings,
}

# Custom navigation bar
def render_navbar():
    # st.markdown('<div class="navbar">', unsafe_allow_html=True)
    menu_items_col, login_col = st.columns([1, .3])
    with menu_items_col:
        st.markdown(
            f"""
            <div class="navbar">
            <a href="Home" onclick="window.location.reload()">Home</a>
            {"" if st.session_state.logged_in else '<a href="Controls" onclick="window.location.reload()">Controls</a>'}
            {"" if st.session_state.logged_in else '<a href="Settings" onclick="window.location.reload()">Settings</a>'}   
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Display user information if logged in
    if st.session_state.logged_in:
        st.markdown(
            f"""
            <div class="user-info">
                <span>👤 {st.session_state.user_name}</span>
                <div class="user-details">
                    <p><strong>Name:</strong> {st.session_state.user_name}</p>
                    <p><strong>Email:</strong> {st.session_state.user_email}</p>
                    <button onclick="document.location.reload()">Logout</button>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        with login_col:
            st.markdown(f"""
                <div class="navbar">
                {"" if st.session_state.logged_in else '<a href="login" onclick="window.location.reload()">Login</a>'}
                {"" if st.session_state.logged_in else '<a href="signup" onclick="window.location.reload()">Sign Up</a>'}
            </div>""", unsafe_allow_html=True)

        
        # # with login_col:
        #     if st.button("Login"):
        #         st.session_state.logged_in = True
        #         st.session_state.user_name = "John Doe"
        #         st.session_state.user_email = "john.doe@example.com"
        #         st.experimental_rerun()
        # # with signup_col:
        #     if st.button("Sign Up"):
        #         st.session_state.logged_in = True
        #         st.session_state.user_name = "Jane Doe"
        #         st.session_state.user_email = "jane.doe@example.com"
        #         st.experimental_rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# Render the navigation bar
render_navbar()

# Title of the app
st.markdown('<h1 class="main-title">House Assistant</h1>', unsafe_allow_html=True)

# Call the appropriate page function based on the selected page
selected_page = st.sidebar.radio("Go to", list(pages.keys()))
pages[selected_page]()

# Footer
st.markdown('<div class="footer">© 2023 House Assistant</div>', unsafe_allow_html=True)