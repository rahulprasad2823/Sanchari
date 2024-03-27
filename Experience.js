import "./Experience.css";
import TravelView from "./viewTraveldata";
import React, {useState, useEffect} from 'react';
import axios from 'axios';
const Experience = () => {
    const [travellist, setTravel] = useState([{}])
    const [travel_id, setTravelid] = useState('')
    const [name, setName] = useState('')
    const [place_visited, setPlace_visited] = useState('')
    const [dates, setDates] = useState('')
    const [budget, setBudget] = useState('')
    const [experience, setExperience] = useState('')
    const [suggestions, setSuggestions] = useState('')
    
    //Read all travel data
    useEffect(() => {
      axios.get('http://localhost:8000/api/travel')
      .then(res => {
        setTravel(res.data)
      })
    });

     //Post Travel Data
  const addTravelHandler = () => {
    axios.post('http://localhost:8000/api/travel/', { 'travel_id':travel_id,'name':name,'place_visited':place_visited,'dates':dates,'budget':budget,'experience':experience,'suggestions':suggestions})
    .then(res => console.log(res))
  }

  
    return (
  <section id="Experience">
       <div class="bby">
        <div class="popup">
            <div class="form">
                <h2>Travel Experience</h2>
                <div class="form-element">
                    <label for="travel_id">Travel ID</label>
                    <input type="text" id="travel_id" placeholder="Enter Travel ID" onChange={event=>setTravelid(event.target.value)} required />
                </div>
                <div class="form-element">
                    <label for="name">Name</label>
                    <input type="text" id="name" placeholder="Enter Your Name" required onChange={event=>setName(event.target.value)} />
                </div>
                <div class="form-element">
                    <label for="place_visisted">Place Visisted</label>
                    <input type="text" id="place_visisted" placeholder="Enter the Place Visisted" required onChange={event=>setPlace_visited(event.target.value)}/>
                </div>
                <div class="form-element">
                    <label for="dates">Dates</label>
                    <input type="text"   placeholder="Enter The Date you Traveled" onChange={event=>setDates(event.target.value)} required />
                </div>
                <div class="form-element">
                    <label for="budget">Budget</label>
                    <input type="text" id="budget" placeholder="Enter Your Trip Budget" required onChange={event=>setBudget(event.target.value)} />
                </div>
                <div class="form-element">
                    <label for="experience">Experience</label>
                    <input type="text"  placeholder="Enter Your Trip Experience" required onChange={event=>setExperience(event.target.value)}/>
                </div>
                <div class="form-element">
                    <label for="suggestions">Suggestions</label>
                    <input type="text" id="suggestions"  placeholder="Enter Your Suggestions" required onChange={event=>setSuggestions(event.target.value)}/>
                </div>
                <div class="form-element">
                   <button onClick={addTravelHandler}>Submit</button>
                </div>
                <div class="form-element">
                   <a href="#">View Experience's</a>
                 </div>
            </div>
        </div>
        <div class="popup2">
            <div class="form">
                <h2>Travel Experience</h2>
                <div class="form-element">
                    <TravelView travellist={travellist}/>
                </div>
            </div>
        </div>
       </div>
  </section>
);
}

export default Experience;
