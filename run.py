from flask import Flask, request, redirect, url_for, render_template, jsonify, flash, session, json

app = Flask(__name__,
            static_url_path='', 
            static_folder='static')

@app.route('/')
def index():
  return 'Web App with Python Flask!'
  
if __name__ == '__main__':
  app.run()

