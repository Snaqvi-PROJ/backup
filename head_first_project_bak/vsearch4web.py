from flask import Flask, render_template, request, redirect, escape
from vsearch import search4letters
from sqlite3 import connect

app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
  """ Log details of the web request and the resuts. """
  conn = connect('vsearchlog.db')
  cursor = conn.cursor()
  _query = """insert into log
              (phrase, letters, ip, browser_string, results)
              values
              (?, ?, ?, ?, ?)"""
  cursor.execute(_query, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res, ))
  conn.commit()
  cursor.close()
  conn.close()


@app.route('/')
def hello() -> str:
  return redirect('/entry')


@app.route('/search4', methods=['POST'])
def do_search() -> str:
  phrase = request.form['phrase']
  letters = request.form['letters']
  title = 'Here are your results:'
  results = str(search4letters(phrase, letters))
  log_request(request, results)
  return render_template('results.html', the_title=title, the_phrase=phrase, the_letters=letters, the_results=results,)


@app.route('/entry')
def entry_page():
  return render_template('/entry.html', the_title='Welcome to search4vowels on web')


@app.route('/viewlog')
def view_the_log() -> 'html':
  contents = []
  with open('vsearch.log', 'r') as log:
    for line in log:
      contents.append([])
      for item in line.split('|'):
        contents[-1].append(escape(item))
  titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
  return render_template('/viewlog.html', the_title='View Log', the_row_titles=titles, the_data=contents,)


if __name__ == '__main__':
  app.run(debug=True)
