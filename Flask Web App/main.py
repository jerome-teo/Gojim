from website import create_app

# when you put the init file in a folder,
# it makes that folder a python package that you can import from

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)