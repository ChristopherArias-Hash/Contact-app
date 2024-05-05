# Import necessary modules and classes
from flask import request, jsonify
from config import app, db
from models import Contact

# Define endpoint to retrieve all contacts
@app.route("/contacts", methods=["GET"])
def get_contacts():
    # Query all contacts from the database
    contacts = Contact.query.all()
    # Convert contacts to JSON format
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    # Return JSON response with contacts
    return jsonify({"contacts": json_contacts})

# Define endpoint to create a new contact
@app.route("/create_contact", methods=["POST"])
def create_contract():
    # Get first_name, last_name, and email from request JSON
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    # Return an error response if any field is missing
    if not first_name or not last_name or not email:
        return jsonify({"message": "You must include a first name, last name and email"}), 400

    # Create a new Contact object
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        # Add the new contact to the database
        db.session.add(new_contact)
        # Commit the changes
        db.session.commit()
    except Exception as e:
        # Return an error message if the operation fails
        return jsonify({"message": str(e)}), 400

    # Return a success message
    return jsonify({"message": "User Created!"}), 201

# Define endpoint to update a contact
@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    # Find the contact with the given user_id
    contact = Contact.query.get(user_id)
    # Return a "User not found" message if the contact doesn't exist
    if not contact:
        return jsonify({"message": "User not found"}), 404

    # Get the new data from the request
    data = request.json
    # Update the contact's first_name, last_name, and email if a new value is provided
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    # Save the changes to the database
    db.session.commit()

    # Return a success message
    return jsonify({"message": "Contact updated"}), 200

# Define endpoint to delete a contact
@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    # Find the contact with the given user_id
    contact = Contact.query.get(user_id)
    # Return a "User not found" message if the contact doesn't exist
    if not contact:
        return jsonify({"message": "User not found"}), 404

    # Delete the contact from the database
    db.session.delete(contact)
    # Commit the changes
    db.session.commit()

    # Return a success message
    return jsonify({"message": "User deleted!"}), 200

# Run the Flask application
if __name__ == "__main__":
    # Create the database tables
    with app.app_context():
        db.create_all()

    # Run the application in debug mode
    app.run(debug=True)