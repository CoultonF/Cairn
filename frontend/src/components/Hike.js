import { FaChevronCircleRight } from 'react-icons/fa'

const Hike = ( { hike } ) => {
    return (
        <div className='task'>
            <h3>{hike.text} <FaChevronCircleRight style={{color:'grey', cursor: 'pointer'}} /></h3>
            <p>{hike.date}</p>
        </div>
    )
}

export default Hike
