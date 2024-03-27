import React from 'react';
import axios from 'axios';
import './traveladd.css';

function PopularItem(props) {
    const deletePopularHandler = (place_id) => {
        axios.delete(`http://localhost:8000/api/popular_destination/${encodeURIComponent(place_id)}`)
        .then(res =>console.log(res))
        .catch(error => console.error('Error deleting place:', error));
    }

        return (
            <div class="output">
                {/* <p class="form">{props.popular_destination.place_id}</p> */}
                <div class="data">
                <label>Place:</label>
                <p class="form">{props.popular_destination.place}</p>
                </div>
                <div class="data">
                <label>Destination:</label>
                <p class="form">{props.popular_destination.description}</p>
                </div>
                <button onClick={() => deletePopularHandler(props.popular_destination.place_id)}>Delete</button>
            </div>
        )
}

export default PopularItem;
