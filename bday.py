import streamlit as st

# Define questions, answers, and hints
questions = [
    "The moment when you both first cried, yet all around you smiled. What significant lunar event marks this memorable occasion?",
    "Which sister, shapes the future turning innovation into reality?",
    "Which sister, sprinkle smiles and sparkle in day to day life?",
    "The place i passed my time as teen away from messy world, when stress filled the air, still passed exams with flying colours, Tell me who am I?",
    "Nameera, The place where you meet random idiots, and now are your favourites?",
    "Mahwish, Tell me the name of the organization you work under,Enjoy - Chill, Have fun. Even you have a t-shirt of it.",
    "How is more Introvert, Shy and silent-killer? Nameera or Mahwish",
    "Nameera, where top achievers are made, creativity takes a backseat, and hobbies are forgotten, where the journey from JEE to EAMCET ignites sparks. Despite spending years here, COVID-19 has passed through the academic halls. What place is this?",
    "Mahwish, among the lectures and labs, where friendships blossomed and knowledge flourished, Name the college which provides a roller coaster ride for your career."
]

answers = [
    ["10/04/1425", "10/4/1425", "9/4/1425", "09/04/1425"],
    ["Nameera", "nameera"],
    ["Mehwish", "Mahwish", "mehwish", "mahwish"],
    ["Vidyaniketan Academy", "vidyaniketan academy", "VNA", "Vidyaniketan academy"],
    ["MJCET", "mjcet"],
    ["Mavericks", "mavericks"],
    ["Nameera", "nameera"],
    ["Narayana", "narayana"],
    ["PMVIDS", "pmvids", "Pmvids"]
]

hints = [
    "Enter in DD/MM/YYYY format",
    "Kitta simple hai yeh",
    "Kitta simple hai yeh",
    "The place where you spend your school memeries went",
    "Short-name of current best place after home with homies.",
    "Single word hai, that too you see this name every day in your college looking at top right",
    "Kitta simple hai yeh",
    "Name of your previous college, sirf first word dallo uska",
    "short form of your current college"
]

# Streamlit app
st.title("Birthday Quiz")
st.markdown("Answer the following questions to unlock the surprise!")

feedback_display = st.empty()
question_display = st.empty()

question_number = st.session_state.get('question_number', 0)
if question_number < len(questions):
    st.markdown(f"### Question {question_number + 1}:")
    question_display.markdown(questions[question_number])
    user_answer = st.text_input("Your Answer:", value="", key=f"user_answer_{question_number}")
    
    if st.button("Submit"):
        # Check if answer is correct
        if user_answer.strip().lower() in answers[question_number]:
            feedback_display.success("Correct!")
            st.session_state['question_number'] = question_number + 1
        else:
            feedback_display.error("Incorrect! Try again.")
            st.text(f"Hint: {hints[question_number]}")
            
    if st.session_state.get('question_number', 0) == question_number + 1:
        if st.button("Next Question"):
            st.session_state[f'user_answer_{question_number}'] = ""  # Clear the answer input
else:
    st.write("One specific quality or trait that you've come to admire about your twin as you've grown older and experienced life together?")
    abc=st.text_input("Your Answer:")
    if st.button("proceed"):
        st.success("Congratulations! You've come so far and put in a lot of effort to answer all these questions. It looks like you found them pretty easy and fun! Keep up the great work and enjoy every moment. Your enthusiasm and dedication are truly amazing!")
        st.video("final-vid.mp4")
