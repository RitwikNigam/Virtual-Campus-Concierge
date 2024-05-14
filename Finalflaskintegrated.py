from flask import Flask, render_template, request,send_file
import nltk
from nltk.chat.util import Chat, reflections
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random
import pandas as pd

nltk.download('punkt')
nltk.download('stopwords')
pairs = [
    ['bye', ['goodbye', 'bye', 'see you']],
    ['hi', ['Hello, how can I assist you today?','hello', 'hi', 'hey']],
    ['hello', ['hi', 'hey', 'hello''Hello, how can I assist you today?']],
    ['goodbye', ['Goodbye! Have a great day.''goodbye', 'bye', 'see you']],
    ['how are you', ['Im here to help you with any questions you have.','good', 'fine', 'great']],
    ['Are Extracurricular Activities in College Important?', ['Extracurricular activities in college play a crucial role in holistic development, providing opportunities for personal growth, skill enhancement, and networking.']],
    ['Are there age limitations to attend this university?', ['In general, prospective students must have completed high school and be at least 17 years of age to attend our university.']],
    ['What are the admission requirements for [specific program/degree]?', ['To qualify for admission, applicants typically need to achieve a minimum aggregate of sixty percentage either in 10+2 or in 10+diploma and must have appeared in the CUET examination.']],
    ['What is the application deadline?', ['The application deadline usually falls 3-4 weeks after the CU-ET examination.']],
    ['How do I apply as an international student?', ['International students can apply through a separate quota allocated for them in our university.']],
    ['Are there any scholarships or financial aid available?', ['Yes, our university offers various scholarships provided by the MP government and the central government.']],
    ['What academic programs and degrees does the college offer?', ['For detailed information on academic programs and degrees, please visit the academic section of our website.']],
    ['Can I double major or pursue a minor?', ['Yes, students have the option to double major or pursue a minor.']],
    ['Are there any opportunities for internships or co-op programs?', ['Our college provides numerous internship opportunities across various courses.']],
    ['What is campus life like?', ['Campus life here is vibrant and dynamic. We organize a wide range of cultural, technical, literature, sports, and e-sports events every year, fostering a lively and engaging atmosphere.']],
    ['What clubs and organizations are available for students to join?', ['There are various clubs in every department of the university, catering to diverse interests and passions. Students are encouraged to join clubs aligned with their interests.']],
    ['Are there any campus events or traditions?', ['We host a multitude of campus events and traditions, including cultural festivals, sports tournaments, and academic symposiums.']],
    ['What recreational facilities are available on campus?', ['Our campus offers a range of recreational activities, including sports facilities, music jam sessions, and leisure spaces for relaxation.']],
    ['What are the housing options for students?', ['Students have access to both on-campus and off-campus housing options, providing a comfortable and convenient living environment.']],
    ['How do I apply for on-campus housing?', ['To apply for on-campus housing, you can visit the specific hostel you wish to be admitted to and follow the application process outlined there.']],
    ['Are there any off-campus housing resources available?', ['Yes, there are numerous off-campus housing facilities available in the surrounding area, catering to the student population.']],
    ['What are the tuition fees for the upcoming academic year?', ['Tuition fees vary depending on the specific course. For detailed fee structures, please refer to the academic section of our website.']],
    ['How do I pay my tuition fees?', ['Tuition fees can be paid directly through the MP-ONLINE gateway of DAVV.']],
    ['What is the refund policy for tuition fees?', ['Our university does not have a specific refund policy for tuition fees.']],
    ['Are there any work-study opportunities available for students?', ['Yes, there are several clubs and programs offering work-study opportunities, including collaborations with companies such as Google Cloud and AWS.']],
    ['What academic support services are available (e.g., tutoring, writing center)?', ['Our university offers a range of academic support services, including tutoring and writing centers, to assist students in their studies.']],
    ['Is there counseling or mental health services available for students?', ['We provide counseling and mental health services to support students well-being and address any personal or emotional challenges they may face.']],
    ['Are there disability support services available for students with disabilities?', ['Yes, our university offers various support services and accommodations for students with disabilities to ensure equal access to education and facilities.']],
    ['What career services are available to students (e.g., resume building, job placement assistance)?', ['Our centralized placement cell (CPC) provides career services such as resume building and job placement assistance to help students transition into the workforce successfully.']],
    ['How can I connect with alumni for networking and career advice?', ['You can connect with alumni through platforms like LinkedIn or attend alumni meetups and networking events organized by the university.']],
    ['What technology resources are available to students (e.g., computer labs, Wi-Fi)?', ['Our campus is equipped with state-of-the-art technology resources, including computer labs, free Wi-Fi zones, and a dedicated IT center.']],
    ['What library and research facilities are available on campus?', ['Our campus features departmental libraries as well as a centralized library with extensive research facilities and resources to support academic pursuits.']],
    ['What health services are available on campus?', ['We have a student wellness center on campus staffed with medical professionals who provide free healthcare services to students.']],
    ['What safety measures are in place on campus?', ['Our campus prioritizes safety and security, with measures such as 24/7 police patrol and a student wellness center to ensure the well-being of our students.']],
    ['What transportation options are available for students inside the campus (e.g., public transit, campus shuttles)?', ['Students have access to various transportation options, including public transit and campus shuttles, to navigate within the campus.']],
    ['Is parking available on campus?', ['Yes, our campus provides ample parking space for both two-wheelers and four-wheelers, with designated parking areas for bicycles as well.']],
]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('2.html')

@app.route('/academic')
def academic():
    return render_template('123.html')

@app.route('/sorting')
def sorting():
    return render_template('sorting.html')
@app.route('/process_csv', methods=['POST'])
def process_csv():
    
    import pandas as pd

    
    csv_file1 = request.files['csvFile1']
    csv_file2 = request.files['csvFile2']
    csv_file3 = request.files['csvFile3']
    csv_file2_path = request.files['csvFile2'].filename
    csv_file3_path = request.files['csvFile3'].filename
    


    
    path=csv_file1

# Read the CSV file into a DataFrame
    data = pd.read_csv(path,header=None)

# Sort the data by the "Percentage" column in descending order
    sorted_data = data.sort_values(by=1, ascending=False)

# Display the sorted data
    print(sorted_data)
    dataA=sorted_data.iloc[::2]
    dataB=sorted_data.iloc[1::2]

    print("data frame 1:",dataA)  
    print("data frame 2:",dataB)
    table_dataA = dataA.to_html(index=False, header=None)
    table_dataB = dataB.to_html(index=False, header=None)
    
    dataA.to_csv(csv_file2_path, index=False, header=None)
    dataB.to_csv(csv_file3_path, index=False, header=None)
    html_output = f"""
    <div style="display: flex;">
        <div style="flex: 50%; padding-right: 20px; background-color: #8A9FA3 ;">
            <p>Data A:</p>
            {table_dataA}
        </div>
        <div style="flex: 50%;background-color: #8A9FA3 ;">
            <p>Data B:</p>
            {table_dataB}
        </div>
    </div>
    """

    return html_output




    #return f"<p>Data A:</p>{table_dataA}<p>Data B:</p>{table_dataB}"


@app.route('/randomize')
def randomize():
    return render_template('randomize.html')
@app.route('/abc', methods=['POST'])
def abc():
    
    import pandas as pd
    csv_file1 = request.files['csvFile1']
    csv_file2 = request.files['csvFile2']
    students_df = pd.read_csv(csv_file1,header=None)
    teachers_df = pd.read_csv(csv_file2,header=None)
    def randomize_assignment(students, teachers):
       random.shuffle(students)
       assignments = {}
       for i, student in enumerate(students):
           teacher = teachers[i % len(teachers)]
           if teacher not in assignments:
               assignments[teacher] = []
           assignments[teacher].append(student)
       return assignments


# Convert DataFrame columns to lists
    students = students_df[0].tolist()
    teachers = teachers_df[0].tolist()

# Randomly assign students to teachers
    assignments = randomize_assignment(students, teachers)

# Create a DataFrame to store the assignments
    df = pd.DataFrame(assignments.items(), columns=["Teacher", "Students"])
    #a=str(df)
    html_table = df.to_html(index=False)

# Write the DataFrame to a CSV file

    
    # Randomization code goes here
    return render_template('tt.html', table=html_table)

@app.route('/chatbot')
def chatbot():
    return render_template('web.html')

    


# Create chatbot
chatbot = Chat(pairs, reflections)


# Define route to handle user input and provide chatbot response
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    exists = any(user_input in sublist for sublist in pairs)
    if exists:
        
        response = chatbot.respond(user_input)
        
    else:
        response="This chatbot is trained to answer a limited scope of questions. Please select a question from the above mentioned list. "
    print("Chatbot:", response)  #debugging
    return response

if __name__ == '__main__':
    app.run(debug=True)
