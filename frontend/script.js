let input_title = document.getElementById('title');
let input_location = document.getElementById('location');
let input_description = document.getElementById('description');
let input_noofroom = document.getElementById('noofroom');
let input_noofbath = document.getElementById('noofbath');
let input_property = document.getElementById('property');
let input_img = document.getElementById('img');
let input_price = document.getElementById('price');
let input_boydesc = document.getElementById('boydesc');
let form = document.getElementById('myForm');
let url = "http://127.0.0.1:8000/property/";  

form.addEventListener('submit', (e)=>{

// Prepare the request body
var data = {
    title: input_title.value,
    location: input_location.value,
    description:input_description.value,
    price:input_price.value,
    number_of_rooms: input_noofroom.value,
    number_of_bath: input_noofbath.value,
    boys_quarters_descriptions:input_boydesc.value,
    property_size:input_property.value,
    uploaded_images:input_img.value
};

// Set up the request options
let options = {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify(data)
};

// Make the request using fetch
fetch(url, options)
  .then(function (response) {
    if (response.ok) {
      // Request was successful
      return response.json();
    } else {
      // Request failed
      throw new Error("Error: " + response.status);
    }
  })
  .then(function (data) {
        // Process the response data if needed
        console.log(data); // Log the data to the console
        // Display a success message to the user
        alert("Data submitted successfully!");
  })
  .catch(function (error) {
    // Handle the error
    console.log(error.message);
  });
})

let patei = document.querySelector('.datar')
let html='';


fetch(url)
  .then(function (response) {
    if (response.ok) {
      // Request was successful
      return response.json();
    } else {
      // Request failed
      throw new Error("Error: " + response.status);
    }
  })
  .then(function (data) {
        console.log(data); // Log the data to the console
    data.forEach(element => {
      html+=`<div>
      <h1>${element?.id}</h1>
      <img src='${element?.img}' width='100'>
      </div>`
    });
// console.log(html)
patei.innerHTML=html

  })
  .catch(function (error) {
    // Handle the error
    console.log(error.message);
  });




  // {
  //   "uploaded_images": [
  //     "https://images.unsplash.com/photo-1554995207-c18c203602cb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80"
  //   ],
  //   "title": "4 bedroom bungalow",
  //   "location": "Lagos, Nigeria",
  //   "description": "Your description goes here...",
  //   "img": "https://images.unsplash.com/photo-1554995207-c18c203602cb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80",
  //   "price": "2000000",
  //   "number_of_rooms": 4,
  //   "number_of_bath": 5,
  //   "boys_quarters_descriptions": "none",
  //   "property_size": 600
  // }
  