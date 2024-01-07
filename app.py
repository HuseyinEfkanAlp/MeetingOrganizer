# server.py

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

meetings = []

@app.route('/')
def index():
    return render_template('index.html', meetings=meetings)

@app.route('/add_meeting', methods=['POST'])
def add_meeting():
    meeting_data = {
        'topic': request.form['topic'],
        'date': request.form['date'],
        'start_time': request.form['start_time'],
        'end_time': request.form['end_time'],
        'participants': request.form.getlist('participants')
    }
    meetings.append(meeting_data)
    return redirect('/')

@app.route('/edit_meeting/<int:meeting_id>', methods=['GET', 'POST'])
def edit_meeting(meeting_id):
    if request.method == 'GET':
        meeting = meetings[meeting_id]
        return render_template('edit_meeting.html', meeting=meeting, meeting_id=meeting_id)
    elif request.method == 'POST':
        meetings[meeting_id]['topic'] = request.form['topic']
        meetings[meeting_id]['date'] = request.form['date']
        meetings[meeting_id]['start_time'] = request.form['start_time']
        meetings[meeting_id]['end_time'] = request.form['end_time']
        meetings[meeting_id]['participants'] = request.form.getlist('participants')
        return redirect('/')

@app.route('/delete_meeting/<int:meeting_id>')
def delete_meeting(meeting_id):
    del meetings[meeting_id]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
