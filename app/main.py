from app.dash_app.app import create_dash_app


app = create_dash_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)
