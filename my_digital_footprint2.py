import streamlit as st
import os  # To check file existence
import time  # For simulating delays

# Set page title and icon
st.set_page_config(page_title="Student Portfolio", page_icon="🎓")

# Sidebar navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go To:", ["Home", "Projects", "Skills", "Testimonials", "Timeline", "Settings", "Contact"])

# Smooth animation with St.spinner
with st.spinner('Loading... Please wait!'):
    time.sleep(1)  # Simulate loading time, you can adjust or remove this as needed

# Home section
if page == "Home":
    st.title("🎓 Student Portfolio")

    # Profile image upload
    uploaded_image = st.file_uploader("Upload Profile Picture", type=["jpg", "png"])
    if uploaded_image is not None:
        st.image(uploaded_image, width=150, caption="Uploaded Image")
    else:
        st.image("kaneza.jpeg", width=150, caption="Default Image")

    # Editable Student details
    name = st.text_input("Name:", "KANEZA Delphine")
    location = st.text_input("Location:", "Musanze, Rwanda")
    field_of_study = st.text_input("Field of Study:", "Computer Science, SWE")
    university = st.text_input("University:", "INES - Ruhengeri")

    st.write(f"📍 {location}")
    st.write(f"📚 {field_of_study}")
    st.write(f"🎓 {university}")

    # Resume Upload & Download
    st.subheader("📄 Resume")
    resume_path = "RESUME.pdf"

    # Upload resume features
    resume_upload = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    if resume_upload is not None:
        with open(resume_path, "wb") as f:
            f.write(resume_upload.getbuffer())
        st.success("✅ Resume uploaded successfully!")

    # Resume Download button
    if os.path.exists(resume_path):
        with open(resume_path, "rb") as file:
            resume_bytes = file.read()
        st.download_button(label="📄 Download Resume", data=resume_bytes, file_name="resume.pdf", mime="application/pdf")
    else:
        st.warning("⚠️ Resume file not found! Please upload your resume.")

# Projects section with filtering
elif page == "Projects":
    st.title("💻 My Projects")
    project_category = st.selectbox("Filter by Category", ["All", "Year 1", "Year 2", "Year 3", "Dissertation"])

    projects = {
        "Year 1": "stock management system",
        "Year 2": "AI-Powered Chatbot",
        "Year 3": "trafic AI-powered",
        "Dissertation": "ENCHANSING URBAN PLANNING THROUGH CITIZEN FEEDBACK USING DIGITAL PLATFORMS"
    }

    for category, title in projects.items():
        if project_category == "All" or project_category == category:
            with st.expander(f"📊 {title}"):
                st.write(f"Project Type: {category}")
                st.write("Description: Developed using Python, AI, and ML techniques.")
                st.write("[🔗 GitHub Repo](#)")

# Skills section
elif page == "Skills":
    st.title("⚡ Skills and Achievements")

    # Dynamic skill levels using sliders
    st.subheader("Programming Skills")
    python_skill = st.slider("Python", 0, 100, 90)
    js_skill = st.slider("JavaScript", 0, 100, 75)
    ai_skill = st.slider("AI & Machine Learning", 0, 100, 65)
    web_dev_skill = st.slider("Web Development (HTML, CSS, React, Flask)", 0, 100, 70)

    # Display the selected skill levels
    st.write(f"🟢 *Python:* {python_skill}%")
    st.write(f"🟡 *JavaScript:* {js_skill}%")
    st.write(f"🔵 *AI & ML:* {ai_skill}%")
    st.write(f"🟠 *Web Development:* {web_dev_skill}%")

    st.subheader("Certifications & Achievements")
    st.write("✔️ Completed AI & ML in Business Certification")
    st.write("✔️ Certified in AI Research and Course Preparation for Education")

# Testimonials Section
elif page == "Testimonials":
    st.title("🗣️ Student Testimonials")

    # Initialize session state to store testimonials
    if "testimonials" not in st.session_state:
        st.session_state.testimonials = []

    # Input for a new testimonial
    new_testimonial = st.text_area("Add a testimonial from colleges:")

    # Button to submit testimonial
    if st.button("Submit Testimonial"):
        if new_testimonial.strip():
            st.session_state.testimonials.append(new_testimonial)
            st.success("✅ Testimonial added successfully!")
        else:
            st.warning("⚠️ Please enter a valid testimonial before submitting.")

    # Display existing testimonials
    st.subheader("📢 Testimonials Received")
    if st.session_state.testimonials:
        for i, testimonial in enumerate(st.session_state.testimonials, start=1):
            st.write(f"*{i}.* {testimonial}")
    else:
        st.info("No testimonials yet. Be the first to add one!")

# Timeline Section
elif page == "Timeline":
    st.title("⏳ Academic & Project Milestones")
    milestones = [
        "✅ Year 1: Completed stock management system",
        "🏆 Year 2: Developed AI-Powered Chatbot and participated in university Kigali",
        "💼 Year 3: Worked on trafic AI-powered",
        "📖 Year 3: Completed Dissertation on ENCHANSING URBAN PLANNING THROUGH CITIZEN FEEDBACK USING DIGITAL PLATFORMS",
        "🎓 Year 3: Final Year Project Defense & Graduation Preparation"
    ]
    for milestone in milestones:
        st.write(milestone)


# Settings Page
elif page == "Settings":
    st.title("⚙️ Settings")

    st.subheader("Edit Profile Details")
    name = st.text_input("Your Name", "KANEZA Delphine")
    location = st.text_input("Location", "Musanze, Rwanda")
    field_of_study = st.text_input("Field of Study", "Software Engineering, Year 3")
    university = st.text_input("University", "INES Ruhengeri")
    about_me = st.text_area("About Me", "I see myself in tomorrow's world techinology")

    if st.button("Save Changes"):
        st.success("✅ Profile updated successfully!")

    st.subheader("Change Password")
    old_password = st.text_input("Current Password", type="password")
    new_password = st.text_input("New Password", type="password")
    confirm_password = st.text_input("Confirm New Password", type="password")

    if st.button("Update Password"):
        if new_password == confirm_password:
            st.success("🔑 Password updated successfully!")
        else:
            st.error("❌ Passwords do not match. Please try again.")

# Contact Section
elif page == "Contact":
    st.title("📬 Contact Me")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("✅ Message sent successfully!")

    st.write("📧 Email: ug2322570@ines.ac.rw")
    st.write("[🔗 LinkedIn](http://www.linkedin.com/in/kanezadephine)")
   

# Sidebar footer
st.sidebar.write("---")
st.sidebar.write("🔹 Made with ❤️ using Streamlit")