import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

function EventDetail() {
    const { slug } = useParams();
    const [event, setEvent ] = useState(null);
    const [loading, setLoading ] = useState(true);

    useEffect(() => {
        async function fetchEvent() {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/stage/event/${slug}`);
                setEvent(response.data);
                setLoading(false);
            } catch(error) {
                console.log(error);
                setLoading(false);
            }
        }

        fetchEvent();
    }, [slug]);

    if (loading) return <p>Loading??...</p>;

    return (
        <div>
            Event
            <h1>{event.title}</h1>
            <p>{event.description}</p>
        </div>
    );
}

export default EventDetail;