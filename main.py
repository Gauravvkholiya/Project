import streamlit as st

st.title("Visulaizer")
if st.button("start Recording"):
    st.write("Recording and detecting objects")
    detected_objects = capture_and_display()
    st.write("Detected objects after recording:", st.session_state.detected_objects)

if st.button("ASK"):
    st.write("Listening, speak after 2 seconds...")
    time.sleep(2)  # Allow time for user to prepare
    # text = recognize_speech()
    # st.write("You said:", text)
    # words = process_question(text)
    # st.write("Processed words:", words)
    # ans = query_json(st.session_state.detected_objects, words)
    # speak_text(ans)
    # st.write("Answer:", ans)
