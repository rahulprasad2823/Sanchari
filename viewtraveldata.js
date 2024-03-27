import TravelItem from "./traveladd";

function TravelView(props) {
    return (
        <div>
            <ul>
            {props.travellist.map(travel => <TravelItem travel={travel} />)}
            </ul>
        </div>
    )
}

export default TravelView;
