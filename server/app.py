#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, session
from flask_migrate import Migrate

from models import db, Article, User, ArticleSchema, UserSchema

app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


with app.app_context():
    db.create_all()
    if Article.query.first() is None:
        user = User(name='Test User')
        db.session.add(user)

        articles = []
        for i in range(1, 6):
            content = f'Content for article {i}'
            article = Article(
                author=f'Author {i}',
                title=f'Title {i}',
                content=content,
                preview=content[:25] + '...',
                minutes_to_read=i,
                user=user,
            )
            articles.append(article)

        db.session.add_all(articles)
        db.session.commit()

@app.route('/clear')
def clear_session():
    session['page_views'] = 0
    return {'message': '200: Successfully cleared session data.'}, 200

@app.route('/articles')
def index_articles():
    articles = [ArticleSchema().dump(a) for a in Article.query.all()]
    return make_response(articles)

@app.route('/articles/<int:id>')
def show_article(id):
    if 'page_views' not in session:
        session['page_views'] = 0

    session['page_views'] += 1

    if session['page_views'] > 3:
        return {'message': 'Maximum pageview limit reached'}, 401

    article = Article.query.get(id)
    if article is None:
        return {'error': 'Not Found'}, 404

    return make_response(ArticleSchema().dump(article), 200)


if __name__ == '__main__':
    app.run(port=5555)
