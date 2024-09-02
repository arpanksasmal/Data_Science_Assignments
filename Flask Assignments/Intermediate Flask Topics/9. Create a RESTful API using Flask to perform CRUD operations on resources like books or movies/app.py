from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dummy data for initial testing
movies = [
    {'id': 1, 'title': 'Inception', 'director': 'Christopher Nolan'},
    {'id': 2, 'title': 'The Dark Knight', 'director': 'Christopher Nolan'},
    {'id': 3, 'title': 'Pulp Fiction', 'director': 'Quentin Tarantino'},
]


@app.route('/')
def index():
    return render_template('index.html')


# Get all movies
@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify({'movies': movies})


# Get a specific movie
@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = next((m for m in movies if m['id'] == movie_id), None)
    if movie:
        return jsonify({'movie': movie})
    else:
        return jsonify({'error': 'Movie not found'}), 404


# Add a new movie
@app.route('/movies', methods=['POST'])
def add_movie():
    new_movie = {'id': len(movies) + 1, 'title': request.json['title'], 'director': request.json['director']}
    movies.append(new_movie)
    return jsonify({'movie': new_movie}), 201


# Update a movie
@app.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    movie = next((m for m in movies if m['id'] == movie_id), None)
    if movie:
        movie['title'] = request.json.get('title', movie['title'])
        movie['director'] = request.json.get('director', movie['director'])
        return jsonify({'movie': movie})
    else:
        return jsonify({'error': 'Movie not found'}), 404


# Delete a movie
@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    global movies
    movies = [m for m in movies if m['id'] != movie_id]
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
