from flask import Flask, jsonify
import json

with open("cv_data.json", "r", encoding="utf-8") as file:
    cv_data = json.load(file)

app = Flask(__name__)


@app.route("/cv", defaults={"section": None}, methods=["GET"])
@app.route("/cv/<section>", methods=["GET"])
def get_section(section):
    """Retrieves the requested section of the CV.

    Args:
        section (str): The section of the CV to retrieve. If not provided, returns the entire CV.

    Returns:
        JSON response:
            - If no section is specified, returns the entire CV data as a JSON object.
            - If a section is specified, returns the data of that section as a JSON object.
            - If the section is not found, returns a message indicating that the section is not available.
    """
    if section is None:
        return jsonify(cv_data)
    return jsonify({section: cv_data.get(section, f"Section '{section}' is not found.")})


if __name__ == "__main__":
    app.run(debug=True)
