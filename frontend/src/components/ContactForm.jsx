import { useState } from "react";
import React from 'react';

const ContactForm = ({ existingContact = {}, updateCallback }) => {
  // State variables for form inputs
  const [firstName, setFirstName] = useState(existingContact.firstName || "");
  const [lastName, setLastName] = useState(existingContact.lastName || "");
  const [email, setEmail] = useState(existingContact.email || "");
  
  // Check if the form is used for updating an existing contact
  const updating = Object.entries(existingContact).length !== 0;

  // Function to handle form submission
  const onSubmit = async (e) => {
    e.preventDefault(); // Prevent default form submission

    // Create an object with the form data
    const data = {
      firstName,
      lastName,
      email
    }; 

    // URL for the fetch request
    const url = "http://127.0.0.1:5000/" + (updating ? `update_contact/${existingContact.id}` : "create_contact");

    // Options for the fetch request
    const options = {
      method: updating ? "PATCH" : "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    };

    // Send the fetch request
    const response = await fetch(url, options);

    // Check if the request was successful
    if (response.status !== 201 && response.status !== 200) {
      // If not successful, parse the response JSON and display an alert with the error message
      const data = await response.json();
      alert(data.message);
    } else {
      // If successful, clear the form inputs
      updateCallback();
    }
  };

  return (
    <form onSubmit={onSubmit}>
      <div>
        <label htmlFor="firstName">First Name:</label>
        <input
          type="text"
          id="firstName"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="lastName">Last Name:</label>
        <input
          type="text"
          id="lastName"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="email">Email:</label>
        <input
          type="text"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>
      <button type="submit">{updating ? "Update" : "Create"}</button>
    </form>
  );
};

export default ContactForm;
