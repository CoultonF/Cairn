import Hike from './Hike'
const Hikes = ({ hikes }) => {

    return (
        <div>
            <>
            {hikes.map((hike) => (
           <Hike key={hike.id} hike={hike} />
            ))}
            </>
        </div>
    )
}

export default Hikes
